import json
W='Web lista para recibir clientes ($249.990)';R='Renovación de web existente ($249.990)'
S1="\n\nSoy Mathias Lezana, de Faro SaMa. Ayudamos a empresas de la región a presentar mejor su negocio en internet.\n\nPuedo preparar un diagnóstico gratuito de una página, con tres mejoras y una propuesta visual en tres imágenes, sin compromiso de contratar.\n\n¿Le gustaría recibirlo por este correo?"
S2="\n\nSoy Mathias Lezana, de Faro SaMa.\n\nPuedo preparar un diagnóstico gratuito de una página, con tres mejoras y una propuesta visual en tres imágenes. No necesita contratar para quedarse con el material.\n\n¿Le gustaría recibirlo por este correo?"
H="Hola, buen día.\n\n"
SW='Sin web propia registrada en Sernatur (por confirmar en el diagnóstico); fuente del correo: registro Sernatur'
C=[
('el-sauce','Restaurante El Sauce Lo Abarca','Cartagena','restaurante','elsauceloabarca@live.cl','Una propuesta para El Sauce',W,SW+'; 5.140 reseñas en Google',
 H+"Vi que El Sauce, en Lo Abarca, suma más de 5.000 opiniones en Google. Es un lugar al que la gente llega recomendada, y pensé en una forma de que quienes lo buscan puedan ver la carta, los horarios y reservar antes de viajar."+S1),
('cormoran','Restaurante Cormorán','El Quisco','restaurante','restaurantcormoran@gmail.com','Una propuesta para el Cormorán',W,SW+'; 1.553 reseñas en Google',
 H+"Vi que el Cormorán, en El Quisco, tiene más de 1.500 opiniones en Google. Con la temporada encima, mucha gente busca dónde comer en el litoral desde el celular, y pensé en una forma de que vean su carta y reserven directo."+S2),
('adelma','Adelma Restaurant','San Antonio','restaurante','adelmarestaurant@gmail.com','Una propuesta para Adelma',W,SW+'; 4,8 con 264 reseñas',
 H+"Vi que Adelma tiene una nota de 4,8 en Google con más de 260 opiniones, de las mejores de San Antonio. Me pareció una buena base para que quienes buscan dónde comer en el puerto vean su carta y reserven sin tener que llamar."+S1),
('valhalla','Valhalla Restobar','San Antonio','restobar','valhalla.restobar.sa@gmail.com','Una propuesta para Valhalla',W,SW+'; 4,9 con 232 reseñas',
 H+"Vi que Valhalla tiene una nota de 4,9 en Google con más de 230 opiniones en San Antonio. Es una reputación muy sólida, y pensé en una forma de que quienes están buscando panorama para el fin de semana los encuentren y reserven."+S1),
('querida-lima','Querida Lima','San Antonio','restaurante peruano','restqueridalima@gmail.com','Una propuesta para Querida Lima',W,SW+'; 1.348 reseñas en Google',
 H+"Vi que Querida Lima suma más de 1.300 opiniones en Google en San Antonio. Quien busca comida peruana en la zona suele decidir mirando la carta en el celular, y pensé en una forma de que la vean y reserven o pidan directo."+S2),
('punta-del-este','Restaurante Punta del Este','Concón','restaurante','rpuntadeleste23120@gmail.com','Una propuesta para Punta del Este',W,SW+'; 1.443 reseñas en Google',
 H+"Vi que el Restaurante Punta del Este, en Concón, tiene más de 1.400 opiniones en Google. En la costanera hay mucha competencia, y pensé en una forma de que quienes buscan dónde almorzar vean su carta y reserven antes de llegar."+S1),
('regina','Regina Restaurante','Olmué','restaurante','reservasreginaolmue@gmail.com','Una propuesta para Regina',W,SW+'; 4,7 con 173 reseñas',
 H+"Vi que Regina tiene una nota de 4,7 en Google en Olmué y que recibe reservas por correo. Mucha gente de Viña y Santiago planifica su visita a Olmué con anticipación, y pensé en una forma de que reserven directo desde el celular."+S1),
('cria-cuervos','Restaurant Cría Cuervos','Quintero','restaurante','rtoledo10@gmail.com','Una propuesta para Cría Cuervos',W,'El dominio de su web registrado en Sernatur (criacuervosrestaurant.cl) hoy aparece a la venta; 1.450 reseñas en Google',
 H+"Vi que Cría Cuervos suma más de 1.400 opiniones en Google en Quintero. Es un lugar muy recomendado, y pensé en una forma de que quienes lo buscan en internet encuentren su carta y su contacto en un sitio propio."+S2),
('cocina-teuh','La Cocina de Teuh','Quintero','restaurante','lacocinadeteuh@hotmail.com','Una propuesta para La Cocina de Teuh',R,'Su web no está adaptada a celular (sin configuración móvil); 1.542 reseñas en Google',
 H+"Vi que La Cocina de Teuh tiene más de 1.500 opiniones en Google en Quintero. La mayoría de esas personas la buscó desde el celular, y pensé en una forma de que su carta y su contacto se vean igual de bien ahí."+S1),
('dona-elena','Restaurante Doña Elena','Olmué','restaurante','saboresdeolmue.restaurant@gmail.com','Una propuesta para Doña Elena',W,'El dominio de su web registrado en Sernatur no responde; 1.259 reseñas en Google',
 H+"Vi que el Restaurante Doña Elena suma más de 1.200 opiniones en Google en Olmué. Es de los lugares que la gente recomienda al visitar la zona, y pensé en una forma de que encuentren su carta y reserven directo desde el celular."+S1),
]
out=[dict(id=a,negocio=b,comuna=c,rubro=d,correo=e,asunto=f,servicio=g,hallazgo=h,cuerpo=i) for a,b,c,d,e,f,g,h,i in C]
json.dump(out,open('correos_reemplazo_2.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(out),[len(o['cuerpo'].split()) for o in out])
