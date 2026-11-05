# Extrae texto útil de cada web para redactar el enganche. Uso: python -I _faro_texto.py pool.json salida.json
import json,sys,re,ssl,urllib.request,html,concurrent.futures as cf
ctx=ssl.create_default_context();ctx.check_hostname=False;ctx.verify_mode=ssl.CERT_NONE
UA={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/124 Safari/537.36'}
def clean(s): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',s))).strip()
def go(r):
    try: h=urllib.request.urlopen(urllib.request.Request(r['final'],headers=UA),timeout=15,context=ctx).read(800000).decode('utf-8','ignore')
    except Exception as e: return {'n':r['n'],'err':str(e)[:60]}
    h2=re.sub(r'<(script|style|noscript|svg)[^>]*>.*?</\1>',' ',h,flags=re.S|re.I)
    desc=(re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']*)',h,re.I) or [None,''])[1]
    heads=[clean(x) for x in re.findall(r'<h[1-3][^>]*>(.*?)</h[1-3]>',h2,re.S|re.I)]
    heads=[x for x in dict.fromkeys(heads) if 3<len(x)<90][:14]
    body=clean(h2)
    yrs=list(dict.fromkeys(m.group(0) for m in re.finditer(r'(desde (el )?(año )?(19|20)\d\d|más de \d+ años|\d+ años de (experiencia|trayectoria)|fundad[ao] en (19|20)\d\d)',body,re.I)))[:3]
    return {'n':r['n'],'desc':clean(desc)[:200],'heads':heads,'anios':yrs,'len':len(body)}
P=json.load(open(sys.argv[1],encoding='utf-8'))
with cf.ThreadPoolExecutor(12) as ex: R=list(ex.map(go,P))
json.dump(R,open(sys.argv[2],'w',encoding='utf-8'),ensure_ascii=False,indent=0);print(len(R))
