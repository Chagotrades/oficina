import json,sys
sys.stdout.reconfigure(encoding='utf-8')
def senales(p,m):
    s=[];fuerte=0
    if m.get('err'): return ['sin medición móvil'],0
    if m.get('sw',375)>380: s.append(f"desborde {m['sw']}px");fuerte+=2 if m['sw']>400 else 1
    wa=p.get('wa') or m.get('wa')
    if not wa and not p.get('form'): s.append('sin WhatsApp ni formulario');fuerte+=2
    elif not wa: s.append('sin WhatsApp');fuerte+=1
    if not m.get('tel') and not wa: s.append('sin teléfono tocable');fuerte+=1
    if m.get('small',0)>=30: s.append(f"{m['small']} textos<12px");fuerte+=1
    if p.get('year') and p['year']<=2021: s.append(f"©{p['year']}");fuerte+=1
    if m.get('txt',9999)<700: s.append(f"poco contenido ({m['txt']})");fuerte+=1
    if 'WordPress 4' in p.get('gen','') or 'WordPress 5' in p.get('gen',''): s.append(p['gen']);fuerte+=1
    return s,fuerte
if __name__=='__main__':
    scan=json.load(open(sys.argv[1],encoding='utf-8'));mov=json.load(open(sys.argv[2],encoding='utf-8'))
    for p in scan:
        if not p.get('ok'): print('XX',p['n'][:32],'| web caída',p.get('err','')[:40]);continue
        m=mov.get(p['final'],{});s,f=senales(p,m)
        print(f,'|',p['n'][:32],'|',p.get('c','')[:12],'|',p.get('res','-'),'|',','.join(p.get('emails',[])[:1])[:34],'|',', '.join(s))
