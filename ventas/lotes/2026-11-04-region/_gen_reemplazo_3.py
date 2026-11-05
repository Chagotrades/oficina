import json
W='Web lista para recibir clientes ($249.990)';R='Renovación de web existente ($249.990)'
S1="\n\nSoy Mathias Lezana, de Faro SaMa. Ayudamos a empresas de la región a presentar mejor su negocio en internet.\n\nPuedo preparar un diagnóstico gratuito de una página, con tres mejoras y una propuesta visual en tres imágenes, sin compromiso de contratar.\n\n¿Le gustaría recibirlo por este correo?"
S2="\n\nSoy Mathias Lezana, de Faro SaMa.\n\nPuedo preparar un diagnóstico gratuito de una página, con tres mejoras y una propuesta visual en tres imágenes. No necesita contratar para quedarse con el material.\n\n¿Le gustaría recibirlo por este correo?"
H="Hola, buen día.\n\n"
C=[
('gala-hotel','Gala Hotel y Centro de Eventos','Viña del Mar','hotel y centro de eventos','galahotel@galahotel.cl','Una propuesta para Gala Hotel',W,'Su web (galahotel.cl) solo muestra la palabra "available" y no se adapta a celular; correo verificado (MX activo); registro Sernatur',
 H+"Vi que Gala Hotel, en calle Arlegui, combina hotel y centro de eventos en pleno centro de Viña del Mar. Es una combinación muy útil para empresas y familias que organizan algo en la ciudad, y pensé en una forma de que puedan cotizar ambas cosas directo."+S1),
('domus-mare','Domus Mare Boutique & Design Hotel','Viña del Mar','hotel boutique','contacto@domusmare.cl','Una propuesta para Domus Mare',W,'Su web muestra una página genérica de "sitio en construcción"; registro Sernatur como hotel boutique',
 H+"Vi que Domus Mare está registrado como hotel boutique y de diseño en avenida Diego Portales, en Viña del Mar. Es un concepto que se vende muy bien con fotos, y pensé en una forma de que los viajeros lo conozcan y reserven directo con ustedes."+S2),
('dunares','Dunares','Quintero (Mantagua)','club y centro de convenciones','rgonzalez@dunares.cl','Una propuesta para Dunares',W,'Su web muestra "estamos haciendo trabajos en el sitio"; 235 reseñas en Google (Dunares de Ritoque Club & Convention Center)',
 H+"Vi que Dunares, en el camino Concón-Quintero, recibe eventos y convenciones entre las dunas de Ritoque, con más de 230 opiniones en Google. Pensé en una forma de que las empresas que buscan dónde hacer su evento de fin de año vean el lugar y coticen directo."+S1),
('casa-henao','B&B La Casa de Henao','Valparaíso','bed and breakfast','contacto@lacasadehenao.cl','Una propuesta para La Casa de Henao',W,'Su web muestra "estamos haciendo trabajos en el sitio"; registro Sernatur',
 H+"Vi que La Casa de Henao recibe huéspedes en Vista Hermosa, en Valparaíso, y está registrada en Sernatur como bed and breakfast. Los viajeros que llegan al puerto suelen buscar alojamiento desde el celular, y pensé en una forma de que reserven directo con ustedes."+S2),
('chanagua','Chanagua Lodge','La Ligua (Los Molles)','lodge','contacto@chanagua.com','Una propuesta para Chanagua Lodge',W,'Su dominio muestra un listado de archivos ("Index of /") en vez de una web; registro Sernatur',
 H+"Vi que Chanagua Lodge recibe huéspedes en Los Molles, uno de los rincones más tranquilos del litoral norte. Quien busca una escapada así suele decidir por las fotos y la ubicación, y pensé en una forma de mostrar el lodge y recibir reservas directas."+S2),
('new-voga','New Voga','Valparaíso','alojamiento','informacion@newvoga.cl','Una propuesta para New Voga',W,'Su web abre una página de error; registro Sernatur',
 H+"Vi que New Voga recibe huéspedes en calle Galos, en pleno Cerro Alegre de Valparaíso. Es una de las zonas más buscadas por los turistas, y pensé en una forma de que quienes planifican su visita los encuentren y reserven directo."+S1),
('campo-y-playa','Cabañas Campo y Playa','Puchuncaví (Pucalán)','cabañas','hugo@campoyplaya.cl','Cabañas en Pucalán y Laguna de Zapallar',R,'Web no adaptada a celular (980 px) y sin WhatsApp; registro Sernatur',
 H+"Vi que Cabañas Campo y Playa recibe todo el año en Pucalán y en Laguna de Zapallar, con buen acceso para quienes vienen de Santiago y Mendoza. Pensé en una forma de que esas familias vean las cabañas y reserven fácil desde el celular."+S1),
('alhambra','Hotel Alhambra','San Antonio (Llolleo)','hotel','contacto@alhambrahotel.cl','Una propuesta para Hotel Alhambra',R,'Web no adaptada a celular (1.024 px) y sin WhatsApp; registro Sernatur',
 H+"Vi que el Hotel Alhambra, en el centro de Llolleo, ofrece 19 habitaciones con baño privado tras una remodelación completa, cerca del puerto y de Santo Domingo. Pensé en una forma de que quienes viajan por trabajo o turismo reserven directo desde el celular."+S1),
('espacio-mediterraneo','Espacio Mediterráneo','Olmué','centro de eventos','contacto@espaciomediterraneo.cl','Una propuesta para Espacio Mediterráneo',W,'Sin WhatsApp ni formulario de reserva en su web; registro Sernatur',
 H+"Vi que Espacio Mediterráneo es una empresa familiar con más de 20 años en eventos, con su espacio en Olmué. Quien organiza un matrimonio o un evento de empresa suele cotizar varias opciones a la vez, y pensé en una forma de que le escriban directo a ustedes."+S1),
('cabanas-maitencillo','Cabañas Maitencillo','Puchuncaví (Maitencillo)','cabañas','reservas@maitencillo.cl','Reservas para el verano en Maitencillo',R,'Web en WordPress 4 con © 2017 y sin WhatsApp; registro Sernatur',
 H+"Vi que Cabañas Maitencillo tiene ocho cabañas equipadas en un recinto privado, abierto todo el año. Se acerca la temporada y muchas familias comparan opciones desde el celular, y pensé en una forma de que reserven directo con ustedes."+S2),
]
out=[dict(id=a,negocio=b,comuna=c,rubro=d,correo=e,asunto=f,servicio=g,hallazgo=h,cuerpo=i) for a,b,c,d,e,f,g,h,i in C]
json.dump(out,open('correos_reemplazo_3.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(out),[len(o['cuerpo'].split()) for o in out])
