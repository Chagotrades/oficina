# Uso: python -I _faro_scan.py entrada.json salida.json  (entrada: lista de {n,c,r,w,...})
import json,sys,re,ssl,urllib.request,urllib.parse,concurrent.futures as cf
ctx=ssl.create_default_context();ctx.check_hostname=False;ctx.verify_mode=ssl.CERT_NONE
UA={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36'}
EM=re.compile(r'[\w.+-]+@[\w-]+(?:\.[\w-]+)*\.(?:cl|com|net|org|info|biz|es)\b',re.I)
BAD=('sentry','wixpress','example','domain.com','tudominio','email.com','correo.com','.png','.jpg','.webp','godaddy','wordpress','jquery','@2x','yourdomain','ejemplo')
def get(u):
    try:
        r=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=15,context=ctx)
        return r.geturl(),r.read(600000).decode('utf-8','ignore')
    except Exception as e: return None,str(e)[:80]
def scan(it):
    w=it['w'];w=w if w.startswith('http') else 'https://'+w
    fin,h=get(w)
    if fin is None and w.startswith('https://'): fin,h=get('http://'+w[8:])
    o=dict(it);o['ok']=fin is not None
    if not fin: o['err']=h;return o
    pages=[h];base=fin
    links=re.findall(r'href=["\']([^"\']+)["\']',h,re.I)
    cont=[l for l in links if re.search(r'contact|nosotros|ubicac',l,re.I)][:2]
    for l in cont:
        u=urllib.parse.urljoin(base,l)
        if urllib.parse.urlparse(u).netloc==urllib.parse.urlparse(base).netloc:
            f2,h2=get(u)
            if f2: pages.append(h2)
    allh=' '.join(pages)
    allh2=urllib.parse.unquote(allh.replace('&#64;','@').replace('[at]','@'))
    ems=sorted(set(e.lower() for e in EM.findall(allh2) if not any(b in e.lower() for b in BAD)))
    o.update(final=fin,emails=ems,
      viewport=bool(re.search(r'name=["\']viewport',h,re.I)),
      wa=bool(re.search(r'wa\.me|api\.whatsapp|whatsapp\.com/send',allh,re.I)),
      tel=bool(re.search(r'href=["\']tel:',allh,re.I)),
      form=bool(re.search(r'<form',allh,re.I)),
      gen=(re.search(r'<meta[^>]+generator[^>]+content=["\']([^"\']+)',h,re.I) or [None,''])[1][:40],
      year=max([int(y) for y in re.findall(r'(?:©|&copy;|copyright)\D{0,15}(20[0-2]\d)',h,re.I)] or [0]),
      title=(re.search(r'<title[^>]*>(.*?)</title>',h,re.I|re.S) or [None,''])[1].strip()[:90],
      size=len(h))
    return o
L=json.load(open(sys.argv[1],encoding='utf-8'))
with cf.ThreadPoolExecutor(16) as ex: R=list(ex.map(scan,L))
json.dump(R,open(sys.argv[2],'w',encoding='utf-8'),ensure_ascii=False,indent=0)
print(len(R),'ok',sum(r['ok'] for r in R),'con correo',sum(1 for r in R if r.get('emails')))
