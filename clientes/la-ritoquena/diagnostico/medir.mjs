// Mide una página como visitante: peso, tiempos, errores, desbordes y capturas.
// node medir.mjs <url> <movil|pc> <salida-prefijo> [--sin-freno]
import { spawn } from 'node:child_process';
import { mkdtempSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const [url, modo, salida] = process.argv.slice(2);
const sinFreno = process.argv.includes('--sin-freno');
const movil = modo === 'movil';
const EDGE = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe';
const PUERTO = 9300 + Math.floor(Math.random() * 500);
const perfil = mkdtempSync(join(tmpdir(), 'medir-'));
spawn(EDGE, ['--headless=new', `--remote-debugging-port=${PUERTO}`, `--user-data-dir=${perfil}`,
  '--no-first-run', '--no-default-browser-check', '--disable-extensions', '--mute-audio', 'about:blank'], { stdio: 'ignore' });
const dormir = (ms) => new Promise((r) => setTimeout(r, ms));
let wsUrl;
for (let i = 0; i < 60 && !wsUrl; i++) {
  try { wsUrl = (await (await fetch(`http://127.0.0.1:${PUERTO}/json/list`)).json()).find((t) => t.type === 'page')?.webSocketDebuggerUrl; } catch {}
  if (!wsUrl) await dormir(250);
}
const ws = new WebSocket(wsUrl);
await new Promise((r) => ws.addEventListener('open', r, { once: true }));
let id = 0; const pend = new Map(); const consola = []; const red = new Map(); let t0 = 0; let cargaMs = 0; let domMs = 0;
ws.addEventListener('message', (ev) => {
  const m = JSON.parse(ev.data);
  if (m.id && pend.has(m.id)) { pend.get(m.id)(m); pend.delete(m.id); return; }
  const p = m.params;
  if (m.method === 'Runtime.consoleAPICalled' && ['error', 'warning'].includes(p.type)) consola.push(`[${p.type}] ` + p.args.map((a) => a.value ?? a.description ?? '').join(' ').slice(0, 250));
  if (m.method === 'Runtime.exceptionThrown') consola.push('[excepción] ' + (p.exceptionDetails.exception?.description || p.exceptionDetails.text).slice(0, 250));
  if (m.method === 'Log.entryAdded' && ['error', 'warning'].includes(p.entry.level)) consola.push(`[log ${p.entry.level}] ${p.entry.text.slice(0, 250)} ${p.entry.url || ''}`);
  if (m.method === 'Network.requestWillBeSent') red.set(p.requestId, { url: p.request.url, tipo: p.type, ini: p.timestamp });
  if (m.method === 'Network.responseReceived') Object.assign(red.get(p.requestId) || {}, { estado: p.response.status, mime: p.response.mimeType });
  if (m.method === 'Network.loadingFinished') Object.assign(red.get(p.requestId) || {}, { bytes: p.encodedDataLength, fin: p.timestamp });
  if (m.method === 'Network.loadingFailed') Object.assign(red.get(p.requestId) || {}, { error: p.errorText });
  if (m.method === 'Page.loadEventFired') cargaMs = p.timestamp;
  if (m.method === 'Page.domContentEventFired') domMs = p.timestamp;
});
const cdp = (method, params = {}) => new Promise((res, rej) => {
  const n = ++id; pend.set(n, (m) => (m.error ? rej(new Error(method + ': ' + m.error.message)) : res(m.result)));
  ws.send(JSON.stringify({ id: n, method, params }));
});
const evaluar = async (e) => (await cdp('Runtime.evaluate', { expression: e, awaitPromise: true, returnByValue: true })).result.value;

try {
  await cdp('Page.enable'); await cdp('Runtime.enable'); await cdp('Log.enable'); await cdp('Network.enable');
  await cdp('Network.setCacheDisabled', { cacheDisabled: true });
  await cdp('Emulation.setDeviceMetricsOverride', movil ? { width: 390, height: 844, deviceScaleFactor: 3, mobile: true } : { width: 1440, height: 900, deviceScaleFactor: 1, mobile: false });
  if (movil) {
    await cdp('Emulation.setTouchEmulationEnabled', { enabled: true, maxTouchPoints: 5 });
    await cdp('Emulation.setUserAgentOverride', { userAgent: 'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36' });
    if (!sinFreno) {
      // "4G lenta" (la de Lighthouse): 150 ms de latencia, 1,6 Mbps de bajada, 750 kbps de subida; CPU 4x.
      await cdp('Network.emulateNetworkConditions', { offline: false, latency: 150, downloadThroughput: 1.6e6 / 8, uploadThroughput: 750e3 / 8 });
      await cdp('Emulation.setCPUThrottlingRate', { rate: 4 });
    }
  }
  await cdp('Page.addScriptToEvaluateOnNewDocument', { source: `window.__lcp=0;window.__cls=0;
    try{new PerformanceObserver(l=>l.getEntries().forEach(e=>window.__lcp=Math.round(e.startTime))).observe({type:'largest-contentful-paint',buffered:true});}catch(e){}
    try{new PerformanceObserver(l=>l.getEntries().forEach(e=>{if(!e.hadRecentInput)window.__cls+=e.value})).observe({type:'layout-shift',buffered:true});}catch(e){}` });
  t0 = (await cdp('Runtime.evaluate', { expression: '0' }), Date.now() / 1000);
  // Usamos la marca de tiempo del protocolo para la carga: se fija con el primer request.
  await cdp('Page.navigate', { url });
  for (let i = 0; i < 240 && !cargaMs; i++) await dormir(250);
  await dormir(4000);
  // el t0 real: primer request del documento
  const reqs = [...red.values()];
  const tDoc = Math.min(...reqs.map((r) => r.ini).filter(Boolean));
  const ajustar = (ts) => ts ? Math.round((ts - tDoc) * 1000) : 0;
  const pagina = await evaluar(`(async()=>{
    const W=innerWidth, q=s=>[...document.querySelectorAll(s)];
    const desb=q('body *').filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&(r.right>W+1)&&getComputedStyle(e).position!=='fixed'}).slice(0,15).map(e=>e.tagName+'.'+String(e.className).slice(0,40)+' der='+Math.round(e.getBoundingClientRect().right));
    const chicos=q('a,button,[role=button],input').filter(e=>{const r=e.getBoundingClientRect();const s=getComputedStyle(e);return r.width>0&&r.height>0&&s.visibility!=='hidden'&&(r.width<44||r.height<44)}).slice(0,30).map(e=>(e.innerText||e.getAttribute('aria-label')||e.href||'').trim().slice(0,40)+' '+Math.round(e.getBoundingClientRect().width)+'x'+Math.round(e.getBoundingClientRect().height));
    const textoChico=q('p,li,span,a').filter(e=>e.childNodes.length&&[...e.childNodes].some(n=>n.nodeType===3&&n.textContent.trim().length>3)&&parseFloat(getComputedStyle(e).fontSize)<14&&e.getBoundingClientRect().width>0).slice(0,15).map(e=>e.innerText.trim().slice(0,40)+' '+getComputedStyle(e).fontSize);
    const rotas=q('img').filter(i=>i.complete&&i.naturalWidth===0&&(i.currentSrc||i.src)).map(i=>i.currentSrc||i.src);
    const sinAlt=q('img').filter(i=>!i.alt).length;
    const imgs=q('img').map(i=>({src:(i.currentSrc||i.src).split('/').pop(),nat:i.naturalWidth+'x'+i.naturalHeight,vis:Math.round(i.getBoundingClientRect().width)+'x'+Math.round(i.getBoundingClientRect().height),lazy:i.loading}));
    return {W,scrollW:document.documentElement.scrollWidth,alto:document.documentElement.scrollHeight,desb,chicos,textoChico,rotas,sinAlt,totalImg:q('img').length,imgs,lcp:window.__lcp,cls:+window.__cls.toFixed(3),
      fcp:Math.round(performance.getEntriesByName('first-contentful-paint')[0]?.startTime||0)}})()`);
  const total = reqs.reduce((a, r) => a + (r.bytes || 0), 0);
  const porTipo = {}; for (const r of reqs) porTipo[r.tipo] = (porTipo[r.tipo] || 0) + (r.bytes || 0);
  const malos = reqs.filter((r) => r.error || r.estado >= 400).map((r) => `${r.estado || ''} ${r.error || ''} ${r.url.slice(0, 150)}`);
  const pesados = reqs.filter((r) => r.bytes > 100e3).sort((a, b) => b.bytes - a.bytes).slice(0, 12).map((r) => `${Math.round(r.bytes / 1024)} KB ${r.url.slice(0, 140)}`);
  const dominios = [...new Set(reqs.map((r) => { try { return new URL(r.url).host; } catch { return ''; } }))];
  // captura de la primera pantalla y de página completa
  const sc = await cdp('Page.captureScreenshot', { format: 'jpeg', quality: 70 });
  writeFileSync(salida + '-pantalla.jpg', Buffer.from(sc.data, 'base64'));
  const alto = Math.min(pagina.alto, 12000);
  await cdp('Emulation.setDeviceMetricsOverride', movil ? { width: 390, height: alto, deviceScaleFactor: 1, mobile: true } : { width: 1440, height: alto, deviceScaleFactor: 1, mobile: false });
  await evaluar(`(async()=>{for(let y=0;y<document.documentElement.scrollHeight;y+=400){scrollTo(0,y);await new Promise(r=>setTimeout(r,120))}scrollTo(0,0)})()`);
  await dormir(2500);
  const full = await cdp('Page.captureScreenshot', { format: 'jpeg', quality: 60, captureBeyondViewport: true });
  writeFileSync(salida + '-completa.jpg', Buffer.from(full.data, 'base64'));
  const res = { url, modo, freno: movil && !sinFreno ? '4G lenta + CPU 4x' : 'sin freno', domMs: ajustar(domMs), cargaMs: ajustar(cargaMs),
    pedidos: reqs.length, totalKB: Math.round(total / 1024), porTipoKB: Object.fromEntries(Object.entries(porTipo).map(([k, v]) => [k, Math.round(v / 1024)])),
    pesados, malos, dominios, consola: [...new Set(consola)], ...pagina };
  writeFileSync(salida + '.json', JSON.stringify(res, null, 2));
  console.log(JSON.stringify(res, null, 2));
} finally {
  try { await cdp('Browser.close'); } catch {}
  process.exit(0);
}
