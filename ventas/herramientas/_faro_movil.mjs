// Revisión en celular (emulación 375x812) con Edge headless vía CDP. Uso: node _faro_movil.mjs urls.json salida.json
import {spawn} from 'node:child_process';import fs from 'node:fs';import os from 'node:os';import path from 'node:path';
const [,,inF,outF]=process.argv;const urls=JSON.parse(fs.readFileSync(inF,'utf8'));
const prof=fs.mkdtempSync(path.join(os.tmpdir(),'faroedge'));const port=9400+Math.floor(Math.random()*500);
const ed=spawn('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',['--headless=new',`--remote-debugging-port=${port}`,`--user-data-dir=${prof}`,'--no-first-run','--disable-extensions','about:blank'],{stdio:'ignore'});
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
let ver;for(let i=0;i<40;i++){try{ver=await (await fetch(`http://127.0.0.1:${port}/json/version`)).json();break}catch{await sleep(500)}}
const EXPR=`(()=>{const vw=innerWidth,sw=document.documentElement.scrollWidth;const els=[...document.querySelectorAll('body *')].filter(e=>e.offsetParent&&e.childNodes.length&&[...e.childNodes].some(n=>n.nodeType===3&&n.textContent.trim().length>2));
const small=els.filter(e=>parseFloat(getComputedStyle(e).fontSize)<12).length;
const taps=[...document.querySelectorAll('a,button')].filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&r.height>0&&(r.height<24||r.width<24)}).length;
const wa=!![...document.querySelectorAll('a')].find(a=>/wa\.me|whatsapp/i.test(a.href));const tel=!!document.querySelector('a[href^="tel:"]');
const first=(document.body.innerText||'').split(String.fromCharCode(10)).join(' ').slice(0,160);
const vp=document.querySelector('meta[name=viewport]')?.content||'';
return JSON.stringify({vw,sw,small,taps,wa,tel,vp,first,txt:(document.body.innerText||'').length})})()`;
async function check(url){
  const t=await (await fetch(`http://127.0.0.1:${port}/json/new?about:blank`,{method:'PUT'})).json();
  const ws=new WebSocket(t.webSocketDebuggerUrl);await new Promise(r=>ws.onopen=r);let id=0;const pend={};
  ws.onmessage=m=>{const d=JSON.parse(m.data);if(d.id&&pend[d.id]){pend[d.id](d);delete pend[d.id]}};
  const send=(method,params={})=>new Promise(r=>{const i=++id;pend[i]=r;ws.send(JSON.stringify({id:i,method,params}))});
  try{
    await send('Emulation.setDeviceMetricsOverride',{width:375,height:812,deviceScaleFactor:2,mobile:true});
    await send('Emulation.setUserAgentOverride',{userAgent:'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Mobile Safari/537.36'});
    await send('Page.enable');send('Page.navigate',{url});await sleep(10000);
    const r=await Promise.race([send('Runtime.evaluate',{expression:EXPR,returnByValue:true}),sleep(8000).then(()=>null)]);
    return r?.result?.result?.value?JSON.parse(r.result.result.value):{err:'sin respuesta'};
  }catch(e){return {err:String(e).slice(0,80)}}finally{ws.close();fetch(`http://127.0.0.1:${port}/json/close/${t.id}`).catch(()=>{})}
}
const out={};const q=[...urls];
await Promise.all([0,1,2,3,4,5].map(async()=>{while(q.length){const u=q.shift();out[u]=await Promise.race([check(u),sleep(30000).then(()=>({err:'tiempo agotado'}))])}}));
fs.writeFileSync(outF,JSON.stringify(out,null,0));ed.kill();process.exit(0);console.log('revisadas',Object.keys(out).length);
