# Correos reescritos (3-nov-2026) para los 60 envíos de mié 4 a vie 6. Uso: python -I correos_v2.py
# La marca es Ascensus (antes Faro SaMa). En los textos va como [NOMBRE] y se reemplaza al generar.
import json, re
N = "Ascensus"
FIRMA = "Mathias Lezana\n" + N + "\nWhatsApp +56 9 4931 1482"
BAJA = "Le escribo porque su correo está publicado como contacto de {e}. Si prefiere no recibir más mensajes, responda \"no\" y no volveré a escribirle."
MOVIL = "prueba con pantalla de celular (375 px, Edge, 3-nov)"

# (fecha, hora, empresa, correo, servicio, problemas[], fuente, incertidumbre, asunto, cuerpo)
C = [
("2026-11-04","08:30","Clínica Dental Centenario","contacto@cdentalcentenario.cl","Aparece en tu comuna ($119.990)",
 ["Nota 5,0 con solo 18 reseñas en Google Maps pese a atender desde 1917","Sin teléfono para tocar en celular (sí tiene WhatsApp)"],
 "Lista de Google Maps y web propia (3-nov)","El número de reseñas puede haber cambiado; confirmar antes de enviar.",
 "Sus reseñas en Google",
 """Hola, equipo de Clínica Dental Centenario:

En Google Maps la clínica tiene nota 5,0, pero con 18 reseñas. Para una clínica que atiende en San Antonio desde 1917, es poco reflejo de todos los pacientes que han pasado por ahí.

Una idea simple: pedir la reseña al terminar cada tratamiento, con un enlace directo por WhatsApp, y responderlas. Quien compara dentistas en Maps ve la cantidad de opiniones junto a la nota.

Soy Mathias Lezana, de [NOMBRE]. Hacemos webs y ayudamos a negocios de la región a aparecer mejor en Google Maps.

¿Hoy les piden reseñas a sus pacientes o todavía no lo han intentado?"""),
("2026-11-04","08:41","Imprenta Victoria","contacto@imprentavictoria.cl","Web lista ($249.990) + Aparece en tu comuna ($119.990)",
 ["17 reseñas en Google pese a funcionar desde 1910","Sin botón de WhatsApp ni teléfono para tocar en la web"],
 "Web propia (Nuestra Historia, Testimonios) y lista de Google Maps","Ninguna relevante.",
 "Desde 1910 y 17 reseñas",
 """Hola, equipo de Imprenta Victoria:

Su web cuenta que la imprenta funciona desde 1910, y los testimonios que publican hablan muy bien de la atención. En Google Maps, en cambio, aparecen 17 reseñas.

Esos mismos clientes podrían dejar su opinión en Google, donde muchos buscan una imprenta. Y en el celular, un botón de WhatsApp para cotizar ahorraría tener que copiar el número.

Soy Mathias Lezana, de [NOMBRE]. Hacemos webs y ayudamos a negocios de la región a aparecer mejor en Google.

¿La mayoría de sus pedidos llega por teléfono, por correo o en persona?"""),
("2026-11-04","08:52","Clínica Juncal","contacto@clinicajuncal.cl","Renovación de web existente ($249.990)",
 ["Web en WordPress 4.8 (versión de 2017)","En celular la página queda más ancha que la pantalla"],
 "Web propia + "+MOVIL,"Ninguna relevante.",
 "Coronas en un día, vistas desde el celular",
 """Hola, equipo de Clínica Juncal:

Ofrecer coronas y carillas en un día con CEREC es un argumento fuerte, y sus más de 400 reseñas en Google muestran que la clínica tiene movimiento.

En una prueba con pantalla de celular, su web queda más ancha que la pantalla y hay que deslizar hacia el lado para leerla. Además, funciona sobre WordPress 4.8, una versión de 2017.

Soy Mathias Lezana, de [NOMBRE]. Renovamos webs para que se lean bien en el celular y lleven directo a pedir hora.

¿Sus pacientes suelen pedir hora por la web o casi todo llega por teléfono?"""),
("2026-11-04","09:00","Consultora Tax","secretaria@consultoratax.cl","Web informativa ($249.990, alcance por confirmar)",
 ["Las descripciones de contabilidad, tributación, auditoría y asesoría laboral son texto de relleno (Lorem ipsum)"],
 "Web propia, comprobado de nuevo el 3-nov (9 apariciones de 'lorem ipsum')","Empresa de Rancagua (fuera de la región). La web no carga por HTTPS.",
 "Las descripciones de sus servicios",
 """Hola, equipo de Consultora Tax:

Su web presenta bien las líneas de servicio, la atención presencial y virtual y la oficina en Rancagua.

Al llegar a la descripción de cada servicio, eso sí, aparece texto de ejemplo («Lorem ipsum») en vez de lo que incluye. Para una empresa que está eligiendo contador, ese es justo el lugar donde busca saber si el servicio le sirve. Bastarían dos o tres frases reales por servicio.

Soy Mathias Lezana, de [NOMBRE]. Hacemos y renovamos webs para pymes, y podríamos ayudarles a redactar y ordenar esa parte.

¿Ya tienen esas descripciones escritas en algún documento o habría que partir desde cero?"""),
("2026-11-04","09:11","Transportes ANFER","anfer@anfer.cl","Corrección puntual de contacto (a cotizar)",
 ["La página Contacto muestra datos de plantilla: dirección en Los Angeles (EE. UU.), teléfono +123 456 789 y correo kargix@mail.com","Preguntas frecuentes con texto de relleno"],
 "anfer.cl/contacto, comprobado de nuevo el 3-nov","No se probó el formulario.",
 "La página de contacto de ANFER",
 """Hola, equipo de Transportes ANFER:

Su web explica bien las modalidades de transporte, los 30 años de trayectoria y las bases en Concón, Santiago y Talcahuano.

Un detalle que quizás no han visto: la página Contacto, a la que se llega desde Servicios, muestra una dirección en Los Angeles, un teléfono de ejemplo y un correo de la plantilla. Sus datos reales solo aparecen al pie.

Soy Mathias Lezana, de [NOMBRE]. Hacemos y corregimos webs de empresas; esa página se puede dejar con sus datos y preguntas reales.

¿La web la administra alguien de su equipo o una agencia?"""),
("2026-11-04","09:22","Constructora Comasca","comasca@comasca.cl","Renovación de web existente ($249.990)",
 ["Web no adaptada a celular (472 px de ancho)","Sin WhatsApp, formulario ni teléfono para tocar"],
 "Web propia + "+MOVIL,"Ninguna relevante.",
 "Comasca en el celular",
 """Hola, equipo de Comasca:

Más de 25 años en edificación y obras civiles se notan en la lista de proyectos ejecutados y en desarrollo que muestra su web.

En una prueba con pantalla de celular, el sitio no se adapta: queda más ancho que la pantalla y no hay un botón para llamar, escribir por WhatsApp o enviar una consulta. Un mandante que revisa constructoras desde el teléfono tendría que hacer zoom y buscar el número.

Soy Mathias Lezana, de [NOMBRE]. Renovamos webs existentes para que funcionen bien en el celular.

¿Sus clientes llegan más por licitaciones y contactos, o también por búsquedas en internet?"""),
("2026-11-04","09:33","Clínica Veterinaria Garrasvet","clinicaveterinaria@garrasvet.cl","Renovación de web existente ($249.990)",
 ["Web no adaptada a celular (981 px de ancho)","Sin WhatsApp ni formulario: la hora solo se pide por teléfono fijo"],
 "Web propia + "+MOVIL,"Ninguna relevante.",
 "Pedir hora en Garrasvet desde el celular",
 """Hola, equipo de Garrasvet:

Su web muestra una oferta completa en Villa Alemana: consultas, cirugías, ecografía, radiografía y atención a domicilio.

Para pedir hora, el único camino que aparece es el teléfono fijo. Y en una prueba con pantalla de celular, la página no se adapta y hay que hacer zoom para leerla. Un botón de WhatsApp o un formulario corto permitiría pedir un domicilio aunque estén ocupados atendiendo.

Soy Mathias Lezana, de [NOMBRE]. Renovamos webs para que sea fácil contactar desde el celular.

¿Hoy reciben consultas por WhatsApp aunque no esté en la web?"""),
("2026-11-04","09:44","Restaurant Cría Cuervos","rtoledo10@gmail.com","Web lista ($249.990)",
 ["La web registrada en su ficha de Sernatur hoy muestra un aviso de dominio a la venta","1.450 reseñas en Google"],
 "Ficha Sernatur + visita al dominio (3-nov)","Puede que hayan dejado la web a propósito.",
 "La web de su ficha de Sernatur",
 """Hola, equipo de Cría Cuervos:

Con más de 1.400 opiniones en Google, el restaurante es muy comentado en Quintero.

La web que figura en su ficha de Sernatur hoy muestra un aviso de que el dominio está a la venta. Quien llega desde ahí no encuentra la carta ni cómo reservar.

Soy Mathias Lezana, de [NOMBRE]. Hacemos webs para negocios de la región: una página simple con carta, horario, ubicación y WhatsApp para reservar, en una dirección propia.

¿Dejaron esa web a propósito o el dominio venció sin que se dieran cuenta?"""),
("2026-11-04","09:55","Restaurante Doña Elena","saboresdeolmue.restaurant@gmail.com","Web lista ($249.990)",
 ["El dominio registrado en su ficha de Sernatur no existe (DNS sin respuesta, 3-nov)","1.259 reseñas en Google"],
 "Ficha Sernatur + consulta DNS (3-nov)","Puede que tengan otra web no registrada en Sernatur.",
 "La web de su ficha de Sernatur",
 """Hola, equipo del Restaurante Doña Elena:

Más de 1.200 opiniones en Google es mucho para un restaurante de Olmué.

La dirección web que aparece en su ficha de Sernatur no abre: hoy ese dominio no existe. Para quien planifica un almuerzo de fin de semana en Olmué, una página con la carta, el horario y un botón de WhatsApp para reservar resolvería sus dudas antes de viajar.

Soy Mathias Lezana, de [NOMBRE]. Hacemos webs simples para restaurantes y negocios de la región.

¿Hoy las reservas les llegan más por teléfono, WhatsApp o Instagram?"""),
("2026-11-04","10:06","Restaurante El Sauce Lo Abarca","elsauceloabarca@live.cl","Web lista ($249.990)",
 ["Sin web propia registrada en su ficha de Sernatur","5.140 reseñas en Google"],
 "Ficha Sernatur + lista de Google Maps","No se buscó si tienen web en otro lugar; el correo lo plantea como duda.",
 "Una página propia para El Sauce",
 """Hola, equipo de El Sauce:

Más de 5.000 opiniones en Google es una cifra que muy pocos restaurantes alcanzan.

En su ficha de Sernatur no aparece una web propia. No sé si la tienen en otra parte; si no, una página sencilla con la carta, los horarios y un botón de WhatsApp respondería lo que necesita saber quien planea ir a Lo Abarca un fin de semana.

Soy Mathias Lezana, de [NOMBRE]. Hacemos webs para negocios de la región.

¿Les preguntan seguido por la carta y los horarios por teléfono o redes?"""),
("2026-11-04","10:17","Bijit Materiales","limache@barracasbijit.cl","Corrección y mejora informativa (a cotizar)",
 ["La página Contacto publica dos numeraciones para la sucursal de Limache en Av. Eastman: 1683 y 1896"],
 "bijit.cl/contacto-3, comprobado de nuevo el 3-nov","Ninguna relevante.",
 "Dos direcciones para la sucursal de Limache",
 """Hola, equipo de Bijit:

Su web presenta bien el catálogo y las sucursales de Limache y Quilpué.

Un detalle en la página Contacto: la sucursal de Limache aparece en Av. Eastman con dos numeraciones distintas, 1683 y 1896. Parece menor, pero es lo que alguien pone en el GPS antes de ir a buscar materiales.

Soy Mathias Lezana, de [NOMBRE]. Hacemos y corregimos webs de empresas; junto con eso, se podría sumar una forma de consultar productos directo a cada sucursal.

¿Cuál de las dos numeraciones es la correcta?"""),
("2026-11-04","10:28","Dunares","rgonzalez@dunares.cl","Web lista ($249.990)",
 ["La web solo muestra 'Lo siento, estamos haciendo trabajos en el sitio'","235 reseñas en Google"],
 "Visita a la web (3-nov) + lista de Google Maps","Puede haber una renovación en curso; el correo lo reconoce.",
 "La web de Dunares en mantención",
 """Hola, equipo de Dunares:

Dunares recibe eventos y convenciones en Mantagua y suma 235 opiniones en Google.

Hoy su web muestra solo el aviso «estamos haciendo trabajos en el sitio». Si la renovación está en curso, perfecto. Si quedó pendiente, quien cotiza un evento de empresa o un matrimonio no puede ver salones, capacidad ni fotos antes de escribir.

Soy Mathias Lezana, de [NOMBRE]. Hacemos webs para negocios de la región.

¿La web está en manos de alguien o quedó detenida?"""),
("2026-11-04","10:39","AMV Transportes","contacto@amvtransportes.cl","Actualización informativa (a cotizar)",
 ["La portada muestra un permiso de transporte hacia Argentina, Paraguay y Brasil 'válido hasta el año 2024'"],
 "Portada de amvtransportes.cl, comprobado el 3-nov","No significa que el permiso real esté vencido; el correo lo aclara.",
 "La fecha de su permiso en la portada",
 """Hola, equipo de AMV Transportes:

Su web explica bien la combinación de transporte de carga, almacenamiento y logística, y sus 20 años de experiencia en Chile y Sudamérica.

En la portada, el permiso para operar hacia Argentina, Paraguay y Brasil aparece como «válido hasta el año 2024». Imagino que ya está renovado; el tema es que un cliente que evalúa proveedores lee esa fecha y no sabe si sigue vigente.

Soy Mathias Lezana, de [NOMBRE]. Actualizamos y renovamos webs de empresas.

¿Tienen a alguien a cargo de actualizar la web o se hace cuando se puede?"""),
("2026-11-04","10:50","Gerbau","contacto@gerbau.cl","Mejora de portada (a cotizar)",
 ["La portada tiene texto de relleno (Lorem ipsum) en los segmentos de clientes y algunos servicios"],
 "Portada de gerbau.cl, comprobado el 3-nov","Empresa de La Florida (RM) y Osorno.",
 "La portada de Gerbau",
 """Hola, equipo de Gerbau:

Su página de instalación y mantención de quicios hidráulicos explica muy bien el servicio y qué datos tener para cotizar.

En la portada, en cambio, los segmentos de clientes y algunos servicios todavía tienen texto de ejemplo («Lorem ipsum»). Un administrador de edificio que entra por la portada podría irse sin llegar a la ficha buena.

Soy Mathias Lezana, de [NOMBRE]. Hacemos y mejoramos webs de empresas.

¿Qué servicio les gustaría que la gente encontrara primero: quicios, accesos u otro?"""),
("2026-11-04","11:01","Vistalibre","contacto@vistalibre.cl","Corrección de navegación y contenido (a cotizar)",
 ["La tarjeta de ventanas PVC de la portada lleva a una ficha de plantilla (Lorem ipsum, cliente 'Qode', ubicación France)","El menú sí lleva a la página real del producto"],
 "Ficha portfolio de vistalibre.cl, comprobado el 3-nov","Ninguna relevante.",
 "La tarjeta de ventanas PVC",
 """Hola, equipo de Vistalibre:

Su web tiene fichas técnicas y un formulario de cotización según el tipo de solicitud, algo muy útil para quien compara ventanas.

Un detalle: en la portada, la tarjeta de ventanas y puertas de PVC lleva a una ficha de plantilla (texto «Lorem ipsum», cliente «Qode», ubicación France), mientras que el menú lleva a la página real del producto.

Soy Mathias Lezana, de [NOMBRE]. Corregimos y mejoramos webs de empresas.

¿Prefieren que esa tarjeta lleve a la ficha del producto o directo a cotizar?"""),
("2026-11-04","11:12","Altometal","ventas2@altometal.cl","Sección de proyectos y enlaces (a cotizar)",
 ["La página Proyectos muestra títulos genéricos en inglés, sin obras reales","Varios enlaces a redes sociales llevan a Wix"],
 "altometal.cl/projects, comprobado el 3-nov","No se afirma que no tengan proyectos reales.",
 "Sus proyectos en la web",
 """Hola, equipo de Altometal:

Su web describe bien los sistemas Allround, Blitz y Euro 2300, y tiene un formulario de cotización claro.

La página Proyectos, en cambio, muestra títulos genéricos en inglés, y varios íconos de redes llevan a Wix en vez de a sus cuentas. Para quien arrienda andamios, ver obras reales hechas con Altometal puede pesar tanto como la ficha técnica.

Soy Mathias Lezana, de [NOMBRE]. Hacemos y mejoramos webs de empresas.

¿Tienen fotos de obras que podrían mostrar con permiso del cliente?"""),
("2026-11-04","11:23","VePrint","ventas@veprint.cl","Contenido y contacto (a cotizar)",
 ["Las preguntas frecuentes de la portada dicen 'Pregunta 1, 2, 3' con Lorem ipsum","La ficha de pendones no indica medidas ni cómo preparar el archivo"],
 "veprint.cl y ficha Pendones, comprobado el 3-nov","No contactar por separado a Alceprint ni Alce Doble Cero.",
 "Las preguntas frecuentes de VePrint",
 """Hola, equipo de VePrint:

La opción de juntar pendones y otros productos en un solo presupuesto es muy práctica.

Revisando la web, las preguntas frecuentes de la portada todavía dicen «Pregunta 1, 2, 3» con texto de ejemplo, y la ficha de pendones no indica medidas ni cómo preparar el archivo. Son dos dudas típicas de quien cotiza impresos por primera vez.

Soy Mathias Lezana, de [NOMBRE]. Hacemos y mejoramos webs de empresas.

¿Qué es lo que más les preguntan antes de cotizar un pendón?"""),
("2026-11-04","11:38","Clínica Dental T&T","contacto@clinicadentaltyt.cl","Renovación de web existente ($249.990)",
 ["En celular la página queda más ancha que la pantalla (392 px)","La primera vista en celular muestra muy poco texto"],
 "Web propia + "+MOVIL,"El poco contenido visible lo midió un script; revisarlo a mano antes de enviar.",
 "Lo que ve un paciente en el celular",
 """Hola, equipo de Clínica Dental T&T:

En Google tienen nota 5,0 con 30 reseñas, y su web cuenta más de 15 años de trayectoria en San Antonio.

En una prueba con pantalla de celular, la página queda un poco más ancha que la pantalla y la primera vista muestra muy poco texto: casi no se alcanza a ver qué tratamientos hacen ni cómo pedir hora.

Soy Mathias Lezana, de [NOMBRE]. Renovamos webs para que se lean bien en el celular y lleven directo a agendar.

¿Qué tratamiento les gustaría que los pacientes nuevos encontraran primero?"""),
("2026-11-04","11:46","Bellora Clinic","contacto@belloraclinic.cl","Renovación de web existente ($249.990)",
 ["En celular la página mide 687 px en una pantalla de 375","31 textos menores a 12 px"],
 "Web propia + "+MOVIL,"Ninguna relevante.",
 "Bellora Clinic en pantalla de celular",
 """Hola, equipo de Bellora Clinic:

Reunir odontología, armonización facial y medicina integral en un mismo lugar es una propuesta clara, y sus 37 reseñas con nota 5,0 la respaldan.

En una prueba con pantalla de celular, la página queda casi el doble de ancha que la pantalla y varios textos quedan muy pequeños. Quien la abre desde el teléfono tiene que hacer zoom para leer.

Soy Mathias Lezana, de [NOMBRE]. Renovamos webs para que funcionen bien en el celular.

¿La mayoría de sus pacientes nuevos llega desde redes sociales, Google o recomendación?"""),
("2026-11-04","11:54","Clínica Pinares","contacto@clinicapinares.cl","Web lista ($249.990) + Aparece en tu comuna ($119.990)",
 ["Sin botón de WhatsApp para agendar","No aparece entre los primeros resultados de 'clínica dental Concón' en Google Maps"],
 "Web propia + búsqueda en Google Maps (3-nov)","Los resultados de Maps varían según quién y dónde busca.",
 "Clínica Pinares en Google Maps",
 """Hola, equipo de Clínica Pinares:

Rehabilitar con CEREC en una sesión es un buen motivo para elegir una clínica en Concón.

En una búsqueda de «clínica dental Concón» en Google Maps, Clínica Pinares no aparece entre los primeros resultados. Y en la web no hay botón de WhatsApp: para pedir hora hay que llamar o llenar el formulario.

Soy Mathias Lezana, de [NOMBRE]. Hacemos webs y ayudamos a clínicas a aparecer mejor en Google Maps.

¿Hoy la mayoría de sus pacientes nuevos llega por recomendación o por búsquedas?"""),
("2026-11-05","08:30","Montemar Brokers","contacto@montemarbrokers.cl","Renovación de web existente ($249.990)",
 ["En celular la página mide 446 px en una pantalla de 375","Sin WhatsApp, formulario ni teléfono para tocar","100 reseñas en Google"],
 "Web propia + "+MOVIL,"Ninguna relevante.",
 "Montemar Brokers en el celular",
 """Hola, equipo de Montemar Brokers:

Tienen 100 reseñas en Google y propiedades en Viña, Reñaca y Concón, además de Santiago.

En una prueba con pantalla de celular, la web queda más ancha que la pantalla y no aparece un botón de WhatsApp, un teléfono para tocar ni un formulario. Quien ve un departamento con vista al mar desde el teléfono tiene que buscar otra forma de escribirles.

Soy Mathias Lezana, de [NOMBRE]. Renovamos webs para que sea fácil consultar desde el celular.

¿Hoy la mayoría de las consultas por propiedades les llega por portales, WhatsApp o la web?"""),
("2026-11-05","08:41","Atienzo Automotriz","contacto@atienzoautomotriz.cl","Renovación de web existente ($249.990)",
 ["Web en WordPress 4.8 con © 2018","Sin WhatsApp ni teléfono para tocar pese a ofrecer asistencia en ruta 24/7","117 reseñas en Google"],
 "Web propia + "+MOVIL,"Ninguna relevante.",
 "Asistencia 24/7 y un botón para llamar",
 """Hola, equipo de Atienzo Automotriz:

Ser especialistas en Hyundai, con diagnóstico CRDI y asistencia en ruta 24/7, es una oferta muy concreta en Quilpué.

Justamente por la asistencia 24/7: en la web no aparece un teléfono que se pueda tocar desde el celular ni un botón de WhatsApp. Quien queda en panne busca desde el teléfono y necesita llamar con un toque. La web, además, todavía lleva el © 2018.

Soy Mathias Lezana, de [NOMBRE]. Renovamos webs para que contactar sea inmediato desde el celular.

¿Las llamadas de asistencia les llegan a un número fijo o a un celular?"""),
("2026-11-05","08:52","Clínica Dental ProDent","contacto@clinicadentalprodent.cl","Renovación ($249.990) + Aparece en tu comuna ($119.990)",
 ["Web en WordPress 5.1","Sin WhatsApp ni teléfono para tocar","21 reseñas en Google"],
 "Web propia + lista de Google Maps","Ninguna relevante.",
 "ProDent en Google y en el celular",
 """Hola, equipo de ProDent:

Su web reúne en una página ortodoncia, endodoncia, implantes y odontopediatría, con el horario de atención.

Dos cosas que llaman la atención: no hay botón de WhatsApp ni un teléfono que se pueda tocar desde el celular, y en Google Maps la clínica tiene 21 reseñas. Las dos las ve quien busca dentista en La Ligua desde el teléfono antes de decidir.

Soy Mathias Lezana, de [NOMBRE]. Renovamos webs y ayudamos a clínicas a aparecer mejor en Google.

¿Hoy las horas se piden más por teléfono o por mensaje?"""),
("2026-11-05","09:03","Imprenta 1177 Express","imprenta1177@gmail.com","Renovación de web existente ($249.990)",
 ["La portada muestra el texto de plantilla 'A nice ad goes here!'","La web no se adapta al celular","155 reseñas en Google"],
 "Web propia, comprobado el 3-nov","Ninguna relevante.",
 "Un espacio libre en su portada",
 """Hola, equipo de Imprenta 1177:

Más de 19 años en Valparaíso y 155 reseñas en Google son una buena base, y la web muestra todo lo que hacen: papel químico, gigantografías, timbres, pendones y diseño.

En la portada todavía aparece el texto de la plantilla «A nice ad goes here!», y en una prueba con pantalla de celular la página no se adapta. Ese espacio podría ser un acceso directo para cotizar por WhatsApp.

Soy Mathias Lezana, de [NOMBRE]. Renovamos webs existentes.

¿Qué producto les gustaría que más gente cotizara?"""),
("2026-11-05","09:14","Hogar Don Bosco","contacto@hogardonbosco.cl","Renovación de web existente ($249.990)",
 ["En celular la página mide 451 px en una pantalla de 375"],
 "Web propia + "+MOVIL,"Hallazgo único; rubro sensible, tono cuidadoso.",
 "Su web en el celular",
 """Hola, equipo de Hogar Don Bosco:

Su web presenta con claridad la atención multidisciplinaria, las actividades y los tipos de habitación, con 15 años de experiencia en Quilpué.

En una prueba con pantalla de celular, la página queda más ancha que la pantalla y hay que deslizar hacia el lado para leerla. Es probable que parte de las familias la revise desde el teléfono.

Soy Mathias Lezana, de [NOMBRE]. Renovamos webs para que se lean bien en cualquier pantalla.

¿Las familias suelen preguntar primero por valores, por disponibilidad o por una visita?"""),
("2026-11-05","09:25","Clínica Veterinaria Animaland","clinicavet.animaland@gmail.com","Web lista ($249.990)",
 ["Sin WhatsApp ni formulario","Muy poco contenido en la primera vista en celular","509 reseñas en Google"],
 "Web propia + "+MOVIL,"El contenido visible lo midió un script.",
 "Atención 24 horas y WhatsApp",
 """Hola, equipo de Animaland:

Atender las 24 horas en Villa Alemana, con más de 500 reseñas en Google, los hace una opción clara cuando una mascota necesita atención.

En su web no hay botón de WhatsApp ni formulario, y en una prueba con pantalla de celular la primera vista muestra muy poco. Para alguien que busca de noche, lo útil es ver en segundos que están abiertos, cómo llegar y cómo llamar.

Soy Mathias Lezana, de [NOMBRE]. Hacemos webs pensadas para contactar rápido desde el celular.

¿Las urgencias les llegan más por teléfono o la gente llega directo?"""),
("2026-11-05","09:36","Shoji Chile","ventas@shojichile.cl","Renovación de web existente ($249.990)",
 ["Web con © 2006","132 textos menores a 12 px en celular"],
 "Web propia + "+MOVIL,"Ninguna relevante.",
 "Los textos de Shoji Chile en el celular",
 """Hola, equipo de Shoji Chile:

Las puertas y espacios de estilo japonés son un producto muy visual, y su web tiene galería, videos de instalaciones y la opción de agendar visita técnica.

En una prueba con pantalla de celular, más de cien textos quedan bajo 12 px, muy chicos para leer sin hacer zoom, y el pie de página todavía dice © 2006. Con textos legibles y fotos grandes, esos proyectos lucirían más.

Soy Mathias Lezana, de [NOMBRE]. Renovamos webs existentes.

¿Sus clientes llegan más por la web, por redes o por recomendación?"""),
("2026-11-05","09:47","AmbienteMar Cabañas","reservas@ambientemar.cl","Web lista ($249.990)",
 ["Sin botón de WhatsApp para consultas de reserva","Leve desborde en celular (381 px)"],
 "Web propia + "+MOVIL,"Hallazgo moderado; la web ya tiene reserva online.",
 "Dudas antes de reservar en AmbienteMar",
 """Hola, equipo de AmbienteMar:

Cabañas equipadas a pasos de la playa en Papudo, con 4,7 en Google y casi 300 reseñas: la propuesta se entiende rápido.

En la web, el camino para consultar es el formulario; no hay botón de WhatsApp. Para dudas cortas de un huésped, como si cabe una persona más o desde qué hora se puede llegar, un mensaje suele resolver lo que un formulario deja esperando.

Soy Mathias Lezana, de [NOMBRE]. Hacemos webs para alojamientos y negocios de la región.

¿Las dudas antes de reservar les llegan más por correo o por teléfono?"""),
("2026-11-05","09:58","Cabañas de Peppino","reservas@depeppino.cl","Renovación de web existente ($249.990)",
 ["Web con muy poco texto (unos 650 caracteres) y © 2022","Sin teléfono para tocar en celular"],
 "Web propia + "+MOVIL,"Ninguna relevante.",
 "Cabañas clásicas o mediterráneas",
 """Hola, equipo de Cabañas de Peppino:

Su web separa las cabañas clásicas de las mediterráneas y publica las condiciones, algo que un huésped agradece.

La página, eso sí, tiene muy poco texto, así que la diferencia entre una cabaña clásica y una mediterránea queda poco explicada. Tampoco hay un teléfono que se pueda tocar desde el celular.

Soy Mathias Lezana, de [NOMBRE]. Renovamos webs de alojamientos.

¿Qué es lo que más les preguntan los huéspedes antes de reservar?"""),
("2026-11-05","10:09","Hospital Veterinario Integral","contacto@hospitalveterinariointegral.com","Renovación de web existente ($249.990)",
 ["En celular la página mide 412 px","39 botones menores a 24 px","Sin teléfono para tocar pese a atender urgencias"],
 "Web propia + "+MOVIL,"Ninguna relevante.",
 "Un teléfono para tocar en urgencias",
 """Hola, equipo del Hospital Veterinario Integral:

Siete años en Viña del Mar y 679 reseñas en Google, con urgencias, hospitalización y exámenes en el mismo lugar.

En una prueba con pantalla de celular, la web queda algo más ancha que la pantalla, varios botones son chicos para el dedo y no aparece un teléfono que se pueda tocar. El WhatsApp sí está, pero en una urgencia hay quienes prefieren llamar.

Soy Mathias Lezana, de [NOMBRE]. Renovamos webs para que el contacto sea rápido desde el celular.

¿Las urgencias les llegan más por WhatsApp o por llamada?"""),
("2026-11-05","10:20","Restaurante Cormorán","restaurantcormoran@gmail.com","Web lista ($249.990)",
 ["Sin web propia registrada en su ficha de Sernatur","1.553 reseñas en Google"],
 "Ficha Sernatur + lista de Google Maps","Puede que tengan web en otro lugar.",
 "La carta del Cormorán en internet",
 """Hola, equipo del Cormorán:

Con más de 1.500 opiniones en Google, es un restaurante muy comentado en El Quisco.

En su ficha de Sernatur no figura una web propia. Si no la tienen, una página simple con la carta, el horario de temporada y un botón para reservar por WhatsApp le ahorraría preguntas a quien planifica su visita en verano.

Soy Mathias Lezana, de [NOMBRE]. Hacemos webs para restaurantes y negocios de la región.

¿Hoy dónde publican la carta: Instagram, Google o en ninguna parte?"""),
("2026-11-05","10:31","Querida Lima","restqueridalima@gmail.com","Web lista ($249.990)",
 ["Sin web propia registrada en su ficha de Sernatur","1.348 reseñas en Google"],
 "Ficha Sernatur + lista de Google Maps","Puede que tengan web en otro lugar.",
 "Una página para Querida Lima",
 """Hola, equipo de Querida Lima:

Más de 1.300 opiniones en Google es mucha gente hablando de comida peruana en San Antonio.

En su ficha de Sernatur no figura una web propia. Una página con la carta y fotos de los platos, horario, ubicación y un botón para reservar o pedir por WhatsApp les daría un lugar propio adonde mandar a los clientes, sin depender solo de las redes.

Soy Mathias Lezana, de [NOMBRE]. Hacemos webs para restaurantes de la región.

¿Hacen reservas o pedidos para llevar, o atienden por orden de llegada?"""),
("2026-11-05","10:42","Alto Poniente Propiedades","contacto@altoponiente.cl","Aparece en tu comuna ($119.990) + WhatsApp",
 ["Solo 6 reseñas en Google pese a más de 30 años","Sin botón de WhatsApp en la web"],
 "Web propia + lista de Google Maps","Confirmar el número de reseñas antes de enviar.",
 "30 años en Limache y 6 reseñas",
 """Hola, equipo de Alto Poniente:

Más de 30 años vendiendo y arrendando casas, parcelas y terrenos en Limache y Olmué es mucha historia.

En Google Maps, sin embargo, la corredora aparece con 6 reseñas. Pedir una reseña a cada cliente que cierra una venta o un arriendo iría juntando esa confianza a la vista. Y en la web, un botón de WhatsApp en cada propiedad facilitaría la primera consulta.

Soy Mathias Lezana, de [NOMBRE]. Ayudamos a negocios de la región a aparecer mejor en Google.

¿Hoy les piden reseñas a sus clientes al cerrar una operación?"""),
("2026-11-05","10:53","Corredora Curauma","contacto@corredoracurauma.cl","Web lista ($249.990)",
 ["Sin WhatsApp ni formulario de contacto","46 botones menores a 24 px en celular"],
 "Web propia + "+MOVIL,"Ninguna relevante.",
 "Consultar por una propiedad",
 """Hola, equipo de Corredora Curauma:

Tienen 4,9 en Google con 80 reseñas y más de 14 años en el sector; la web muestra bien las propiedades destacadas con su precio.

Lo que no aparece es una forma directa de preguntar por una propiedad: no hay botón de WhatsApp ni formulario, solo el teléfono. Un botón «Consultar por esta propiedad» en cada ficha, que abra WhatsApp con la propiedad ya escrita, ahorraría pasos a quien mira desde el celular.

Soy Mathias Lezana, de [NOMBRE]. Hacemos webs listas para recibir consultas.

¿Hoy las consultas llegan más por portales inmobiliarios o directo?"""),
("2026-11-05","11:04","Inalto Salud","contacto@inalto.cl","Renovación de web existente ($249.990)",
 ["Web en WordPress 5.3 (2019)","Sin formulario y sin teléfono para tocar (solo WhatsApp)","721 reseñas en Google"],
 "Web propia + "+MOVIL,"Ninguna relevante.",
 "Pedir hora en Inalto desde el celular",
 """Hola, equipo de Inalto Salud:

Con 721 reseñas en Google, Inalto es un centro muy conocido en Quillota, y su web incluso publica artículos sobre medicina general, ecotomografía y holter.

Para pedir hora, en cambio, solo aparece el WhatsApp: no hay formulario ni un teléfono que se pueda tocar desde el celular. Hay pacientes que prefieren llamar.

Soy Mathias Lezana, de [NOMBRE]. Renovamos webs para que pedir hora sea fácil.

¿La agenda la manejan por WhatsApp o tienen un sistema de reservas?"""),
("2026-11-05","11:15","Medikin Centro Médico","contactos@medikin.cl","Renovación de web existente ($249.990)",
 ["Leve desborde en celular (385 px)","Pie de página con © 2022"],
 "Web propia + "+MOVIL,"Hallazgo débil: la web ya tiene WhatsApp, formulario y teléfono. Sugiero no enviarlo.",
 "Medikin en el celular",
 """Hola, equipo de Medikin:

Su web presenta bien el enfoque en rehabilitación: kinesiología, osteopatía, exámenes y convenios.

Dos detalles: en una prueba con pantalla de celular la página queda un poco más ancha que la pantalla, así que se mueve hacia el lado al deslizar, y el pie todavía dice © 2022. Son cosas chicas, pero dan una impresión de web descuidada.

Soy Mathias Lezana, de [NOMBRE]. Renovamos webs existentes.

¿Los pacientes nuevos les llegan más derivados por médicos o buscando en internet?"""),
("2026-11-05","11:26","Gala Hotel y Centro de Eventos","galahotel@galahotel.cl","Web lista ($249.990)",
 ["Su web solo muestra la palabra 'available'","No se adapta a celular"],
 "Visita a la web (3-nov) + registro Sernatur","Ninguna relevante.",
 "La web de Gala Hotel",
 """Hola, equipo de Gala Hotel:

Gala combina hotel y centro de eventos en Viña del Mar, dos servicios que la gente suele revisar en internet antes de cotizar.

Hoy, al abrir su web, solo aparece la palabra «available». Quien busca dónde hacer un evento o dormir en Viña no ve salones, habitaciones ni cómo contactarlos.

Soy Mathias Lezana, de [NOMBRE]. Hacemos webs para negocios de la región: habitaciones, salones, fotos y un botón para cotizar por WhatsApp.

¿Saben qué pasó con la web o es algo que ya están viendo?"""),
("2026-11-05","11:37","Hotel Alhambra","contacto@alhambrahotel.cl","Renovación de web existente ($249.990)",
 ["Web no adaptada a celular (1.024 px)","Sin WhatsApp"],
 "Web propia + "+MOVIL,"Ninguna relevante.",
 "Reservar en Hotel Alhambra desde el celular",
 """Hola, equipo del Hotel Alhambra:

Su web explica bien la ubicación: en el centro de Llolleo, con acceso rápido al puerto de San Antonio y a Santo Domingo.

En una prueba con pantalla de celular, la página no se adapta: se ve como en un computador, en miniatura. Tampoco hay botón de WhatsApp para consultar disponibilidad.

Soy Mathias Lezana, de [NOMBRE]. Renovamos webs para que reservar sea simple desde el celular.

¿Sus huéspedes vienen más por trabajo o por turismo?"""),
("2026-11-05","11:48","Cabañas Campo y Playa","hugo@campoyplaya.cl","Renovación de web existente ($249.990)",
 ["Web no adaptada a celular (980 px)","Sin WhatsApp"],
 "Web propia + "+MOVIL,"El correo es de una persona (hugo@); no se usó el nombre porque no está confirmado.",
 "Cabañas en Pucalán y Laguna de Zapallar",
 """Hola, equipo de Cabañas Campo y Playa:

Tener cabañas en el campo, en Pucalán, y en la playa, en Laguna de Zapallar, le da al huésped dos opciones muy distintas con un solo contacto.

En una prueba con pantalla de celular, la web no se adapta y no hay un botón de WhatsApp. Para elegir entre campo y playa hay que comparar fotos y capacidad, y eso en miniatura cuesta.

Soy Mathias Lezana, de [NOMBRE]. Renovamos webs de alojamientos.

¿Qué les piden más: las cabañas de campo o las de playa?"""),
("2026-11-05","11:59","Los Troncos de La Cruz","lostroncosdelacruz@gmail.com","Renovación de web existente ($249.990)",
 ["La web aún muestra una sección 'Medidas Covid-19'","Varias secciones dicen 'Próximamente'"],
 "Web propia, comprobado el 3-nov","Ninguna relevante.",
 "Los «Próximamente» de su web",
 """Hola, equipo de Los Troncos:

Restobar y centro de eventos en La Cruz, con 258 reseñas y una web que ya tiene carta, horarios, métodos de pago y WhatsApp.

Lo que sí convendría revisar: todavía aparece una sección de «Medidas Covid-19» y varias partes dicen «Próximamente». Para quien cotiza un evento, esa sección es la clave y hoy se ve sin terminar.

Soy Mathias Lezana, de [NOMBRE]. Renovamos webs existentes.

¿Qué tipo de eventos les gustaría recibir más: cumpleaños, matrimonios o empresas?"""),
("2026-11-06","08:30","Oral Clinic","info@oralclinic.cl","Web lista ($249.990)",
 ["Sin botón de WhatsApp pese a destacar urgencias dentales","Muy poco contenido en la primera vista en celular"],
 "Web propia + "+MOVIL,"El contenido visible lo midió un script.",
 "Urgencias dentales y WhatsApp",
 """Hola, equipo de Oral Clinic:

Su web pone por delante las urgencias dentales en Concón y Quilpué, y más de 15 años atendiendo.

Para una urgencia, eso sí, no hay botón de WhatsApp, y en una prueba con pantalla de celular la primera vista muestra muy poco. Alguien con dolor quiere saber en segundos si lo pueden atender hoy y en qué sede.

Soy Mathias Lezana, de [NOMBRE]. Hacemos webs listas para recibir consultas desde el celular.

¿Atienden urgencias en las dos sedes o solo en una?"""),
("2026-11-06","08:41","Centro Más Salud Kinesiología","consultas@centromassalud.cl","Renovación de web existente ($249.990)",
 ["La portada muestra texto de plantilla 'Welcome to Health Lab'","Pantalla 'Espera mientras carga el Sitio Web'","© 2020"],
 "Web propia, comprobado el 3-nov","Ninguna relevante.",
 "«Welcome to Health Lab» en su portada",
 """Hola, equipo de Centro Más Salud:

Nota 5,0 con 246 reseñas y convenio con Fonasa e isapres: dos datos que un paciente de kinesiología en Viña quiere saber.

En la portada, en cambio, todavía aparece el texto de la plantilla «Welcome to Health Lab», una pantalla de «Espera mientras carga» y el © 2020. No reflejan el nivel de atención que muestran sus reseñas.

Soy Mathias Lezana, de [NOMBRE]. Renovamos webs existentes.

¿Hoy agendan más por WhatsApp o por teléfono?"""),
("2026-11-06","08:52","Fisiosalud Integral","fisiosaludintegra@gmail.com","Web lista ($249.990)",
 ["Sin botón de WhatsApp ni teléfono para tocar en celular"],
 "Web propia + "+MOVIL,"Ninguna relevante.",
 "Agendar en Fisiosalud desde el celular",
 """Hola, equipo de Fisiosalud Integral:

Reunir kinesiología, osteopatía, nutrición, psicología y entrenamiento en Quilpué es una propuesta completa, y la web la muestra con fotos de las instalaciones y testimonios.

La página termina con «¿Qué esperas para agendar?», pero en una prueba con pantalla de celular no hay un botón de WhatsApp ni un teléfono que se pueda tocar. Justo ahí calzaría un botón directo.

Soy Mathias Lezana, de [NOMBRE]. Hacemos webs listas para recibir consultas.

¿Hoy los pacientes agendan por mensaje, por llamada o en un sistema en línea?"""),
("2026-11-06","09:03","StockPro Propiedades","hola@stockpro.cl","Web lista ($249.990)",
 ["Sin botón de WhatsApp","30 textos menores a 12 px en celular"],
 "Web propia + "+MOVIL,"Ninguna relevante.",
 "Vender en Algarrobo y El Quisco",
 """Hola, equipo de StockPro:

Más de 30 propiedades vendidas en los últimos 12 meses en Algarrobo, El Quisco y El Tabo es un dato concreto, y su web lo pone bien a la vista.

Lo que no aparece es un botón de WhatsApp: quien quiere vender o pregunta por una propiedad tiene que buscar otra vía. Y en el celular varios textos quedan muy pequeños.

Soy Mathias Lezana, de [NOMBRE]. Hacemos webs listas para recibir consultas.

¿Les llegan más consultas de gente que quiere vender o de gente que busca comprar?"""),
("2026-11-06","09:14","Clínica Estética Vitaplace","info@vitaplace.cl","Web lista ($249.990)",
 ["Sin botón de WhatsApp para reservar evaluación","26 botones menores a 24 px"],
 "Web propia + "+MOVIL,"Ninguna relevante.",
 "Elegir tratamiento en Vitaplace",
 """Hola, equipo de Vitaplace:

Con 4,9 en Google, 221 reseñas y una oferta amplia de tratamientos faciales, corporales y depilación láser, hay mucho para elegir.

Justamente por eso, es probable que varias clientas nuevas no sepan cuál les conviene. En la web no hay botón de WhatsApp para preguntarlo; solo formulario y teléfono. Un botón «¿No sabes qué tratamiento elegir? Escríbenos» podría ordenar esas consultas.

Soy Mathias Lezana, de [NOMBRE]. Hacemos webs listas para recibir consultas.

¿Las clientas nuevas llegan sabiendo qué tratamiento quieren o piden orientación?"""),
("2026-11-06","09:25","Centro Médico Auramed","contacto@auramed.cl","Web lista ($249.990)",
 ["Sin WhatsApp ni teléfono para tocar en celular","99 reseñas en Google"],
 "Web propia + "+MOVIL,"Ninguna relevante.",
 "Pedir hora en Auramed desde el celular",
 """Hola, equipo de Auramed:

Su web reúne en San Antonio medicina general, fonoaudiología, obstetricia y tratamientos estéticos.

En una prueba con pantalla de celular no aparece un botón de WhatsApp ni un teléfono que se pueda tocar: quien quiere pedir hora tiene que copiar el número. Con servicios tan distintos, también ayudaría separar la parte de salud de la estética, para que cada paciente vaya directo a lo suyo.

Soy Mathias Lezana, de [NOMBRE]. Hacemos webs listas para recibir consultas.

¿Qué servicio les piden más hoy?"""),
("2026-11-06","09:36","Centro de Estética Bellavi","info@centrobellavi.com","Renovación de web existente ($249.990)",
 ["Web no adaptada a celular (1.050 px de ancho)","Sin WhatsApp ni teléfono para tocar"],
 "Web propia + "+MOVIL,"Ninguna relevante.",
 "Centro Bellavi en el celular",
 """Hola, equipo de Centro Bellavi:

Su web presenta los tratamientos y el centro en Concón.

En una prueba con pantalla de celular, la página no se adapta: se ve como en un computador, casi tres veces más ancha que la pantalla. Tampoco hay botón de WhatsApp ni un teléfono que se pueda tocar para reservar.

Soy Mathias Lezana, de [NOMBRE]. Renovamos webs para que se vean bien y se pueda reservar desde el celular.

¿Hoy sus clientas reservan por redes, WhatsApp o teléfono?"""),
("2026-11-06","09:47","Taller Automotriz Torres","etorres@tallerautomotriztorres.cl","Renovación de web existente ($249.990)",
 ["Leve desborde en celular (391 px)","Sin teléfono para tocar"],
 "Web propia + "+MOVIL,"Ninguna relevante.",
 "Mantenciones por kilometraje",
 """Hola, equipo de Taller Automotriz Torres:

Mantención por pauta de kilometraje, tren delantero, frenos y rectificado: su web deja claro qué hacen, y en Google tienen 4,6 con 108 reseñas.

Una idea concreta: quien busca mantención suele tener a mano su modelo y kilometraje. Un botón «Cotiza tu mantención» que abra WhatsApp pidiendo esos dos datos daría consultas más fáciles de responder. Hoy, en el celular, tampoco aparece un teléfono para tocar.

Soy Mathias Lezana, de [NOMBRE]. Renovamos webs existentes.

¿Qué les preguntan más: el precio de la mantención o la disponibilidad de hora?"""),
("2026-11-06","09:58","Adelma Restaurant","adelmarestaurant@gmail.com","Web lista ($249.990)",
 ["Sin web propia registrada en su ficha de Sernatur","4,8 con 264 reseñas en Google"],
 "Ficha Sernatur + lista de Google Maps","Puede que tengan web en otro lugar.",
 "Un enlace propio para Adelma",
 """Hola, equipo de Adelma:

Un 4,8 en Google con más de 260 opiniones es una buena carta de presentación en San Antonio.

En su ficha de Sernatur no figura una web propia. Si no la tienen, una página con la carta, el horario y un botón para reservar por WhatsApp les daría un enlace propio para poner en Google Maps y en sus redes.

Soy Mathias Lezana, de [NOMBRE]. Hacemos webs para restaurantes de la región.

¿Dónde los encuentran más los clientes nuevos: Google, redes o recomendación?"""),
("2026-11-06","10:09","Valhalla Restobar","valhalla.restobar.sa@gmail.com","Web lista ($249.990)",
 ["Sin web propia registrada en su ficha de Sernatur","4,9 con 232 reseñas en Google"],
 "Ficha Sernatur + lista de Google Maps","No sabemos si tienen música o eventos; el correo lo pregunta.",
 "La semana de Valhalla en una página",
 """Hola, equipo de Valhalla:

Un 4,9 en Google con más de 230 opiniones es una nota muy alta para un restobar en San Antonio.

En su ficha de Sernatur no figura una web propia. Para un restobar, una página con la carta, los horarios y lo que pasa cada semana (música, partidos o promociones, si los tienen) les daría un lugar fijo para anunciarlo, además de las redes.

Soy Mathias Lezana, de [NOMBRE]. Hacemos webs para negocios de la región.

¿Dónde anuncian hoy sus actividades?"""),
("2026-11-06","10:20","Restaurante Punta del Este","rpuntadeleste23120@gmail.com","Web lista ($249.990)",
 ["Sin web propia registrada en su ficha de Sernatur","1.443 reseñas en Google"],
 "Ficha Sernatur + lista de Google Maps","Puede que tengan web en otro lugar.",
 "Reservas para grupos en Punta del Este",
 """Hola, equipo del Restaurante Punta del Este:

Más de 1.400 opiniones en Google es mucha gente recomendándolos en Concón.

En su ficha de Sernatur no figura una web propia. Una idea concreta: una página con la carta y un botón para reservar mesa o consultar por grupos por WhatsApp, que pida la fecha y el número de personas desde el primer mensaje.

Soy Mathias Lezana, de [NOMBRE]. Hacemos webs para restaurantes de la región.

¿Reciben muchas reservas de grupos o atienden sobre todo por orden de llegada?"""),
("2026-11-06","10:31","Regina Restaurante","reservasreginaolmue@gmail.com","Web lista ($249.990)",
 ["Sin web propia registrada en su ficha de Sernatur","4,7 con 173 reseñas en Google"],
 "Ficha Sernatur + lista de Google Maps","Puede que tengan web en otro lugar.",
 "Las reservas de Regina",
 """Hola, equipo de Regina:

Su correo de contacto es de reservas, así que imagino que buena parte de sus mesas se reserva con anticipación. Y con 4,7 en Google y más de 170 opiniones, la gente los recomienda.

En su ficha de Sernatur no figura una web propia. Una página con la carta y un formulario de reserva con fecha, hora y número de personas les evitaría tener que preguntar cada dato por correo.

Soy Mathias Lezana, de [NOMBRE]. Hacemos webs para restaurantes de la región.

¿Hoy las reservas les llegan más por correo, teléfono o WhatsApp?"""),
("2026-11-06","10:42","Hostal Maison de la Mer","maisondelamervalpo@gmail.com","Web lista ($249.990)",
 ["Sin WhatsApp ni teléfono para tocar","Reserva solo por formulario o correo"],
 "Web propia + "+MOVIL,"Ninguna relevante.",
 "Reservar en Maison de la Mer",
 """Hola, equipo de Maison de la Mer:

Más de 20 años recibiendo huéspedes en Valparaíso, y una web que muestra las habitaciones, la ubicación y las recomendaciones que han recibido.

Para reservar, el camino es el formulario o el correo: no hay botón de WhatsApp ni un teléfono que se pueda tocar desde el celular. No se trata de quitar el correo, sino de sumar una vía rápida para quien ya está en la ciudad y busca dónde dormir.

Soy Mathias Lezana, de [NOMBRE]. Hacemos webs para alojamientos de la región.

¿La mayoría de sus huéspedes reserva con anticipación o a última hora?"""),
("2026-11-06","10:53","La Cocina de Teuh","lacocinadeteuh@hotmail.com","Renovación de web existente ($249.990)",
 ["Web no adaptada a celular (sin configuración móvil)","Casi sin contenido aparte del formulario y la galería","1.542 reseñas en Google"],
 "Web propia, comprobado el 3-nov","Ninguna relevante.",
 "La web de La Cocina de Teuh en el celular",
 """Hola, equipo de La Cocina de Teuh:

Más de 1.500 opiniones en Google son muchísimas para un restaurante de Quintero.

Su web, en cambio, no está preparada para celular: se abre como en un computador, en miniatura, y casi no tiene contenido aparte del formulario y la galería. Una página con la carta, el horario y un botón para reservar por WhatsApp aprovecharía mejor a toda esa gente que ya los conoce.

Soy Mathias Lezana, de [NOMBRE]. Renovamos webs de restaurantes y negocios de la región.

¿La web la hizo alguien del equipo o una empresa externa?"""),
("2026-11-06","11:04","Hotel Manoir Atkinson","info@hotelatkinson.cl","Renovación de web existente ($249.990)",
 ["Leve desborde en celular (385 px)","Sin formulario ni teléfono para tocar (solo WhatsApp)"],
 "Web propia + "+MOVIL,"Ninguna relevante.",
 "Reservas directas en Manoir Atkinson",
 """Hola, equipo de Hotel Manoir Atkinson:

Un hotel boutique en el Cerro Concepción, con vista a la bahía y servicio personalizado: la web transmite bien esa idea.

Para reservar, eso sí, solo aparece el WhatsApp, sin formulario ni teléfono para tocar, y en una prueba con pantalla de celular la página queda un poco más ancha que la pantalla. Un formulario simple con fechas y número de huéspedes ayudaría a quienes no usan WhatsApp.

Soy Mathias Lezana, de [NOMBRE]. Renovamos webs de alojamientos.

¿Qué parte de sus reservas llega directo y qué parte por plataformas?"""),
("2026-11-06","11:15","Restaurant Bote Salvavidas","rbsreservas@gmail.com","Renovación de web existente ($249.990)",
 ["Desborde en celular (383 px)","Sin WhatsApp ni teléfono para tocar","Muy poco contenido en la primera vista pese a 1.082 reseñas"],
 "Web propia + "+MOVIL,"Ninguna relevante.",
 "Reservar en el Bote Salvavidas desde el celular",
 """Hola, equipo del Bote Salvavidas:

Un restaurante en el Muelle Prat, ligado al Cuerpo de Voluntarios del Bote Salvavidas y con más de 1.000 reseñas en Google, tiene una historia propia.

En una prueba con pantalla de celular, la web muestra muy poco en la primera vista y no aparece un botón de WhatsApp ni un teléfono para tocar: para reservar o preguntar por el arriendo del local para eventos hay que buscar el contacto.

Soy Mathias Lezana, de [NOMBRE]. Renovamos webs existentes.

¿Qué les consultan más: reservas de mesa o arriendo para eventos?"""),
("2026-11-06","11:26","Domus Mare Boutique & Design Hotel","contacto@domusmare.cl","Web lista ($249.990)",
 ["Su web muestra una página genérica en inglés: 'Awesome Site in The Making'"],
 "Visita a la web (3-nov) + registro Sernatur","Ninguna relevante.",
 "La web de Domus Mare",
 """Hola, equipo de Domus Mare:

En el registro de Sernatur aparecen como hotel boutique y de diseño en Viña del Mar.

Hoy su web muestra una página genérica en inglés: «Awesome Site in The Making». Para un hotel cuyo atractivo es el diseño, las fotos de las habitaciones son justo lo que el huésped quiere ver antes de reservar.

Soy Mathias Lezana, de [NOMBRE]. Hacemos webs para alojamientos: habitaciones, fotos, ubicación y un botón para reservar.

¿La página en construcción es temporal o la web quedó pendiente hace tiempo?"""),
("2026-11-06","11:37","Chanagua Lodge","contacto@chanagua.com","Web lista ($249.990)",
 ["Su dominio muestra un listado de archivos del servidor ('Index of /') en vez de una web"],
 "Visita a la web (3-nov) + registro Sernatur","Revisar antes: el listado muestra la carpeta de otro sitio; no está claro que el lodge siga operando.",
 "La web de Chanagua Lodge",
 """Hola, equipo de Chanagua Lodge:

Están registrados en Sernatur como lodge en Los Molles.

Al abrir su web hoy aparece un listado de carpetas del servidor («Index of /») en lugar de una página. Quien busca alojamiento en Los Molles no ve fotos, tarifas ni cómo reservar, y además el listado deja a la vista los archivos del hosting.

Soy Mathias Lezana, de [NOMBRE]. Hacemos webs para alojamientos de la región.

¿El lodge sigue recibiendo huéspedes?"""),
("2026-11-06","11:48","New Voga","informacion@newvoga.cl","Web lista ($249.990)",
 ["Su web redirige a una página que solo dice 'Error'"],
 "Visita a la web en el navegador (3-nov) + registro Sernatur","Puede ser una falla pasajera; confirmar el día anterior al envío.",
 "La web de New Voga muestra un error",
 """Hola, equipo de New Voga:

Están registrados en Sernatur como alojamiento en Valparaíso.

Hoy, al entrar a su web, la dirección lleva a una página que solo dice «Error». Quizás es algo pasajero, pero quien busca dónde alojarse en Valparaíso y llega ahí no ve habitaciones ni cómo reservar.

Soy Mathias Lezana, de [NOMBRE]. Hacemos webs para alojamientos de la región.

¿Sabían de este error o es primera noticia?"""),
("2026-11-06","11:59","Espacio Mediterráneo","contacto@espaciomediterraneo.cl","Web lista ($249.990)",
 ["Sin WhatsApp ni formulario para cotizar un evento","Web sin configuración para celular"],
 "Web propia (3-nov) + registro Sernatur","Ninguna relevante.",
 "Cotizar un evento en Espacio Mediterráneo",
 """Hola, equipo de Espacio Mediterráneo:

Más de 20 años organizando eventos en Olmué, junto a Boss Producciones, y una sección de opiniones en la web.

Para cotizar, en cambio, no hay botón de WhatsApp ni formulario. Quien organiza un matrimonio o un evento de empresa suele tener claros tres datos: fecha, número de invitados y tipo de evento. Un formulario corto con esas tres preguntas les dejaría cada consulta lista para responder.

Soy Mathias Lezana, de [NOMBRE]. Hacemos webs listas para recibir consultas.

¿Qué tipo de evento reciben más?"""),
]

# Oferta del informe (pedido de Mathias, 3-nov: ya trajo 2 respuestas positivas). Va antes de la pregunta final.
SIN_WEB = {"Restaurant Cría Cuervos", "Restaurante Doña Elena", "Restaurante El Sauce Lo Abarca", "Dunares", "Restaurante Cormorán",
           "Querida Lima", "Gala Hotel y Centro de Eventos", "Adelma Restaurant", "Valhalla Restobar", "Restaurante Punta del Este",
           "Regina Restaurante", "Domus Mare Boutique & Design Hotel", "Chanagua Lodge", "New Voga"}
CON_GOOGLE = {"Clínica Dental Centenario", "Imprenta Victoria", "Clínica Pinares", "Clínica Dental ProDent", "Alto Poniente Propiedades"}
def oferta(e):
    if e in SIN_WEB:
        que = "de cómo los encuentra hoy un cliente en internet"
    elif e in CON_GOOGLE:
        que = "de su web y su ficha en Google"
    else:
        que = "de su web"
    return f"Si les sirve, les preparo sin costo un informe breve {que}: lo que encontré, en qué les afecta y cómo lo resolveríamos, con capturas reales. Sin compromiso."

R = []
for f, h, e, c, s, p, fu, inc, a, b in C:
    b = b.replace("[NOMBRE]", N)
    partes = b.rsplit("\n\n", 1)
    b = partes[0] + "\n\n" + oferta(e) + "\n\n" + partes[1]
    w = len(re.findall(r"\w+", b))
    rev = inc.startswith(("Revisar", "Hallazgo débil"))
    R.append({"id": re.sub(r"[^a-z0-9]+", "-", e.lower().translate(str.maketrans("áéíóúñ&", "aeioun-"))).strip("-"),
              "fecha": f, "hora": h, "zona": "America/Santiago", "empresa": e, "correo": c, "servicio": s,
              "problemas": p, "fuente": fu, "incertidumbre": inc, "asunto": a, "cuerpo": b,
              "firma": FIRMA, "baja": BAJA.format(e=e), "palabras": w,
              "estado": "revisar antes de aprobar" if rev else "pendiente de aprobación",
              "aprobacion": "pendiente", "comentario": ""})
json.dump(R, open("correos_semana_v2.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(R), "correos;", "palabras min/max:", min(x["palabras"] for x in R), max(x["palabras"] for x in R))
print("a revisar:", [x["empresa"] for x in R if x["estado"].startswith("revisar")])
print("ids repetidos:", len(R) - len({x["id"] for x in R}), "| restos de Faro:", sum("Faro" in x["cuerpo"] + x["firma"] for x in R))
