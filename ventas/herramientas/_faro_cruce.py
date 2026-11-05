# Cruza nombres de Sernatur con reseñas de listas de Maps. Uso: python -I _faro_cruce.py sernatur_nuevos.json maps_resenas.txt salida.json
import json,sys,re,unicodedata
sys.stdout.reconfigure(encoding='utf-8')
def norm(s):
    s=unicodedata.normalize('NFKD',s.lower());s=''.join(c for c in s if not unicodedata.combining(c))
    s=re.sub(r'[^a-z0-9 ]',' ',s)
    stop={'restaurant','restaurante','restobar','cabanas','cabana','hostal','hotel','de','del','la','las','el','los','y','bar','spa','limitada','ltda','e','i','r','l','sociedad','comercial','gastronomica','servicios','turisticos','eirl','spa'}
    return {w for w in s.split() if w not in stop and len(w)>2}
S=json.load(open(sys.argv[1],encoding='utf-8'))
M=[l.strip().split('¦') for l in open(sys.argv[2],encoding='utf-8') if '¦' in l]
out=[]
for n,r,k in M:
    a=norm(n)
    if not a: continue
    best=None
    for s in S:
        b=norm(s['n'])
        if a and b and (a<=b or b<=a) and len(a&b)>=1:
            best=s;break
    if best: out.append(dict(best,maps_n=n,nota=r,res=k)); print(k,'|',n,'|',best['n'][:40],'|',best['email'],'|',best['web'][:30])
json.dump(out,open(sys.argv[3],'w',encoding='utf-8'),ensure_ascii=False,indent=0)
