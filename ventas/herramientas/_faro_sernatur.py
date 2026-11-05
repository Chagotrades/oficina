# Lee el buscador público de Sernatur por comuna y tipo. Uso: python -I _faro_sernatur.py salida.json
import urllib.request,urllib.parse,ssl,re,sys,json,html,concurrent.futures as cf
c=ssl.create_default_context();c.check_hostname=False;c.verify_mode=ssl.CERT_NONE
B='https://serviciosturisticos.sernatur.cl'
def g(u):
    for _ in range(2):
        try: return urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0 Chrome/124'}),timeout=30,context=c).read().decode('utf-8','ignore')
        except Exception: pass
    return ''
COM='Valparaíso,Viña del Mar,Concón,Quilpué,Villa Alemana,Limache,Olmué,Quillota,La Cruz,La Calera,Hijuelas,Nogales,Los Andes,San Esteban,Calle Larga,Rinconada,San Felipe,Santa María,Putaendo,Llaillay,Catemu,Panquehue,Casablanca,Algarrobo,El Quisco,El Tabo,Cartagena,San Antonio,Santo Domingo,Quintero,Puchuncaví,Zapallar,Papudo,La Ligua,Cabildo,Petorca'.split(',')
links=set()
def lista(args):
    com,t=args;out=[]
    for p in range(1,8):
        h=g(f"{B}/resultado.php?page={p}&nombre=&tipo_servicio={t}&comuna_nombre={urllib.parse.quote(com)}")
        L=re.findall(r'href="(/\d+-[^"]+)"',h)
        if not L: break
        out+= [(l,t) for l in L]
    return out
with cf.ThreadPoolExecutor(8) as ex:
    for r in ex.map(lista,[(cm,t) for cm in COM for t in (1,2)]): links|=set(r)
def det(a):
    l,t=a;d=g(B+l)
    tx=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' | ',re.sub(r'<(script|style)[^>]*>.*?</\1>','',d,flags=re.S))))
    f=lambda k:(re.search(k+r':\s*\|\s*([^|]+)',tx) or [None,''])[1].strip()
    web=re.findall(r'href="(https?://[^"]+)"[^>]*>\s*(?:<[^>]+>\s*)*sitio web',d,re.I)
    nm=(re.search(r'<h1[^>]*>(.*?)</h1>',d,re.S) or re.search(r'<title>(.*?)</title>',d,re.S) or [None,''])[1]
    return {'url':B+l,'tipo':'alojamiento' if t==1 else 'restaurante','n':html.unescape(re.sub('<[^>]+>','',nm)).strip(),'dir':f('Dirección'),'loc':f('Localidad'),'tel':f('Teléfono'),'email':f('Email'),'web':web[0] if web else '','clase':''}
with cf.ThreadPoolExecutor(10) as ex: R=list(ex.map(det,sorted(links)))
json.dump(R,open(sys.argv[1],'w',encoding='utf-8'),ensure_ascii=False,indent=0)
print(len(links),'fichas;',sum(1 for r in R if r['email']),'con correo;',sum(1 for r in R if r['email'] and not r['web']),'con correo y sin web')
