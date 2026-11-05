import json,sys,re
ex=json.load(open('excluir.json',encoding='utf-8'));prev=set()
for f in sys.argv[2:]:
    try: prev|={re.sub(r'^https?://(www\.)?','',x['w']).split('/')[0].lower() for x in json.load(open(f,encoding='utf-8'))}
    except FileNotFoundError: pass
out=[];rub=com=''
for l in open('maps_raw.txt',encoding='utf-8'):
    l=l.strip()
    if not l: continue
    if l.startswith('#'): rub,com=l[1:].split('|');continue
    n,r,k,w=l.split('¦')
    d=w.split('/')[0].lower()
    if d in ex['dominios'] or d in prev: continue
    prev.add(d);out.append({'n':n,'c':com,'r':rub,'w':w,'nota':r,'res':k,'src':'maps'})
json.dump(out,open(sys.argv[1],'w',encoding='utf-8'),ensure_ascii=False);print(len(out))
