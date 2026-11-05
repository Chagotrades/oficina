import urllib.request,urllib.parse,json,sys
q='[out:json][timeout:170];area["name"="Región de Valparaíso"]["admin_level"="4"]->.a;(nwr(area.a)["website"]["amenity"~"dentist|clinic|doctors|veterinary|restaurant|kindergarten|school|driving_school|cafe|events_venue"];nwr(area.a)["website"]["shop"];nwr(area.a)["website"]["tourism"~"hotel|guest_house|chalet|motel|apartment|camp_site"];nwr(area.a)["website"]["office"];nwr(area.a)["website"]["craft"];nwr(area.a)["website"]["leisure"~"fitness_centre|sports_centre"];);out tags center;'
for u in ['https://overpass-api.de/api/interpreter','https://overpass.kumi.systems/api/interpreter','https://overpass.private.coffee/api/interpreter']:
    try:
        r=urllib.request.urlopen(urllib.request.Request(u,data=urllib.parse.urlencode({'data':q}).encode(),headers={'User-Agent':'faro-prospeccion/1.0'}),timeout=200).read()
        open(sys.argv[1],'wb').write(r);print('ok',u,len(r));break
    except Exception as e: print('fail',u,e)
