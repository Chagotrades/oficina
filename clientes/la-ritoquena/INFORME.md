# Diagnóstico de laritoquena.com

Para: La Ritoqueña, hotel de playa en Ritoque (Quintero, región de Valparaíso).
Revisado el 3 de noviembre de 2026, mirando la web como la vería un huésped, en celular (390 px) y en computador (1440 px). No enviamos formularios ni hicimos reservas.

## En cinco líneas

1. El botón "Reserva" lleva a una pantalla en inglés con fechas de julio de 2024 y un aviso rojo que dice que no hay disponibilidad. Es la puerta de entrada de las reservas directas y hoy recibe al cliente con un error.
2. En un celular con 4G lenta, la foto principal de la portada tarda unos 22 segundos en aparecer. La página pesa 5,2 MB y casi todo son fotos sin optimizar.
3. La web no dice cuánto cuesta una noche, no muestra las buenas notas que el hotel tiene en otros sitios y no tiene un mapa en las páginas del menú.
4. Google ve 23 páginas, varias viejas o repetidas, con nombres como "Habitaciones v2" o "Nosotros v3", y ninguna tiene descripción. La portada no tiene foto para cuando alguien comparte el link.
5. El formulario de contacto pide nombre y correo sin explicar qué se hace con esos datos, y no hay política de privacidad. La nueva ley de datos personales (Ley 21.719) empieza a regir el 1 de diciembre de 2026.

Todo esto tiene arreglo y lo más caro de no arreglar (el botón de reserva) es de lo más rápido de corregir.

## Lo que está bien

- Las fotos son lindas y muestran bien el lugar: dunas, mar, madera, vista desde la pieza.
- La web usa https (el candado) y redirige bien desde http y desde www.
- El botón verde de WhatsApp funciona y abre un chat con "Reservas La Ritoquena".
- En las páginas del menú no aparecieron errores en la consola, ni imágenes rotas, ni partes que se salgan de la pantalla del celular.

## Hallazgos, de lo que más cuesta a lo que menos

### 1. El botón de reserva recibe al cliente con un error

**Qué pasa.** Los botones "Reserva" de la foto principal y del pie abren el motor de reservas (Cloudbeds) con un link que trae fechas fijas: llegada el 17 de julio de 2024 y salida el 18. Esas fechas ya pasaron, así que el sistema muestra en rojo: "There's no availability for the specified dates. Please select different dates." Toda la pantalla está en inglés. Además, el "Reserva" del menú de arriba no abre las reservas: baja al pie de la página, donde hay otro botón.

**Evidencia.** Captura `diagnostico/capturas/reserva-error.jpg`. El link es el mismo en las cuatro páginas del menú.

**Qué cuesta.** Es el momento en que la persona ya decidió y quiere ver fechas y precio. Si ve un error en otro idioma, lo fácil es cerrar y reservar por Booking u otra plataforma, que cobran comisión por cada reserva, o irse a otro hotel.

**Cómo se arregla.** Cambiar el link para que abra en español y sin fechas fijas (o con un selector de fechas en la propia web), y que el "Reserva" del menú abra directo el motor de reservas. Es un cambio chico.

### 2. La portada tarda demasiado en el celular

**Qué pasa.** Medimos la portada simulando un celular con 4G lenta y un procesador de gama media:

| | Portada |
|---|---|
| Peso total | 5,2 MB (41 archivos) |
| De eso, fotos | 4,8 MB |
| Aparece lo primero | 3,2 s |
| Aparece la foto principal | 22,5 s |
| Termina de cargar | 30 s |

La página de habitaciones pesa casi lo mismo (5,1 MB, 29,6 s). En computador, con nuestra conexión normal, la portada terminó de cargar en 7 s.

La foto grande de la portada pesa 1,5 MB y las de la galería se bajan en tamaño completo (1080 × 1440) aunque en el celular se ven de 149 px de ancho.

**Evidencia.** Mediciones en `diagnostico/mediciones/inicio-movil.json` y `habitaciones-v3-movil.json`. Hicimos la prueba con las mismas 8 fotos más pesadas de la portada: optimizadas para la web pasan de 4,7 MB a 1,1 MB, y se ven igual.

**Qué cuesta.** Mucha gente busca alojamiento desde el celular, y es poco probable que espere 20 segundos mirando una pantalla a medio cargar.

**Cómo se arregla.** Achicar y convertir las fotos a un formato liviano (WebP), cargar versiones chicas en el celular y dejar que las fotos de más abajo carguen recién cuando la persona baja.

### 3. No responde las preguntas que hace alguien antes de reservar

**Qué pasa.**
- No hay precios. El pie dice "Consulta disponibilidad y precios aquí" y lleva al error del punto 1. Los precios sí existen en el motor de reservas: en el calendario de noviembre y diciembre de 2026 aparecen noches de entre unos $72 mil y $96 mil.
- No se muestran opiniones de huéspedes. En los listados que encontramos en sitios de viaje, el hotel aparece con notas altas (alrededor de 9,4 a 9,7 de 10, según el sitio). Eso no aparece en la web.
- La portada dice que el lugar es "casi imperceptible en los mapas", y en el menú no hay mapa ni dirección. Existe una página de ubicación con un mapa de Google, pero no está en el menú.
- En el pie, el teléfono abre WhatsApp (no una llamada) y el correo es solo texto: para escribir un correo hay que copiarlo a mano.
- La página de habitaciones cuenta lo básico (4 habitaciones matrimoniales con baño privado y balcón con vista al mar, más un módulo para hasta 4 personas, desayuno incluido), pero no separa cada tipo de habitación con sus fotos, capacidad y precio.
- La ventana de WhatsApp dice "Start a Conversation", en inglés, y no trae un mensaje listo para que la persona solo apriete enviar.

**Evidencia.** Capturas `celular-portada.jpg`, `celular-habitaciones.jpg`, `reserva-error.jpg`.

**Qué cuesta.** Cada duda sin respuesta es un mensaje que alguien tiene que contestar o un cliente que se va a comparar a otro lado.

**Cómo se arregla.** Poner "desde $..." por noche, una sección de habitaciones con lo que incluye cada una, reseñas reales, mapa y "cómo llegar", un botón para llamar y el correo como link, y WhatsApp en español con un mensaje inicial.

### 4. Google y los links compartidos muestran una versión descuidada

**Qué pasa.**
- El mapa del sitio que lee Google tiene 23 páginas. Varias son borradores o copias: "Habitaciones v2", "Habitaciones v3", "Nosotros v3", "Servicio v3", "El Hotel v2", "Inicio" (una portada antigua) y dos páginas distintas de "Qué hacer en Ritoque".
- Las páginas del menú tienen esos nombres como título: en la pestaña del navegador y en Google se lee "Nosotros v3 - La Ritoquena".
- Ninguna de las 23 páginas tiene descripción. Google elige solo qué texto mostrar debajo del título.
- La portada no tiene imagen para compartir. Cuando alguien pega el link en WhatsApp u otra app de mensajes, lo más probable es que salga sin foto.
- El nombre aparece como "La Ritoquena", sin ñ, en los títulos.

**Evidencia.** `https://laritoquena.com/sitemap_index.xml` y la lista revisada página por página.

**Qué cuesta.** Menos clics desde Google, y un link compartido sin foto, que llama mucho menos la atención en un chat.

**Cómo se arregla.** Dejar una sola versión de cada página, sacar o redirigir las viejas, poner títulos y descripciones pensadas para quien busca "hotel en Ritoque" y agregar una foto para compartir.

### 5. Páginas abandonadas que restan confianza

**Qué pasa.**
- "Eventos" es una página con el título y nada más.
- "Blog" muestra un artículo en inglés de otro sitio (ArchDaily) sobre la arquitectura del "Hostal Ritoque", y abajo un recuadro que dice "null".
- El ícono de Instagram lleva a la página del lugar en Instagram, no a la cuenta del hotel.

No están en el menú, pero sí en el mapa del sitio que lee Google, así que alguien puede llegar a ellas desde un buscador.

**Evidencia.** Capturas `celular-eventos.jpg` y `celular-blog.jpg`.

**Cómo se arregla.** Completar o borrar esas páginas, y apuntar Instagram a la cuenta correcta.

### 6. Datos personales sin aviso ni política de privacidad

**Qué pasa.** La página "Contacto y Reservas" tiene un formulario que pide nombre, correo y mensaje. No hay ningún texto que explique para qué se usan esos datos, ni un link a una política de privacidad. Probamos las direcciones habituales (`/politica-de-privacidad/` y `/privacy-policy/`) y no existen.

**Qué cuesta.** La Ley 21.719 de protección de datos personales empieza a regir el 1 de diciembre de 2026. Hay un proyecto en el Congreso para postergarla un año, pero mientras no se apruebe, la fecha es esa. También es un tema de confianza: a la gente le da más tranquilidad dejar sus datos cuando ve quién los guarda y para qué.

**Cómo se arregla.** Publicar una política de privacidad simple (qué datos se piden, para qué, cuánto tiempo se guardan, a quién escribir para borrarlos) y un aviso corto junto al botón de enviar. Conviene que la revise un abogado.

### 7. Detalles de uso en el celular

- La página bloquea el zoom: quien ve mal no puede agrandar el texto con los dedos.
- Los párrafos se ven en letra de 13,65 px, un poco chica para leer en un teléfono.
- Los puntos del carrusel miden 7 × 7 px y el botón "Reserva" de la foto principal mide 82 × 31 px. Se recomienda que lo que se toca mida al menos 44 × 44 px.
- 9 de las 10 imágenes de la portada no tienen descripción (texto alternativo), que sirve a Google y a personas con lectores de pantalla.
- En la portada, bajo la galería, queda un espacio vacío grande antes del texto (se ve en `celular-portada.jpg`).

**Cómo se arregla.** Son ajustes de diseño chicos que se hacen junto con lo demás.

## Lo que podemos hacer

Los precios y plazos los define Santiago.

**Nivel 1: arreglos urgentes sobre la web actual.**
Botón de reserva en español y sin fechas viejas; fotos optimizadas; botón para llamar y correo como link; títulos, descripciones y foto para compartir; limpiar páginas viejas y duplicadas; política de privacidad y aviso en el formulario; quitar el bloqueo del zoom.
Precio: por definir. Plazo: por definir.

**Nivel 2: una web pensada para vender desde el celular.**
Todo lo del nivel 1, más una portada nueva que muestre de entrada precio "desde", habitaciones con fotos y qué incluyen, opiniones de huéspedes, mapa y cómo llegar, selector de fechas conectado al motor de reservas y WhatsApp con mensaje listo. Rápida en 4G y medida antes de entregar.
Precio: por definir. Plazo: por definir.

**Nivel 3: web + asistente que responde las consultas.**
Todo lo del nivel 2, más un asistente en la web o en WhatsApp que conteste las preguntas de siempre (precios, qué incluye, cómo llegar, horarios de llegada) y pase al equipo lo que no sabe o lo que es una reserva. Incluye revisión mensual de visitas y consultas.
Precio: por definir. Plazo: por definir.

## Lo que no pudimos comprobar

- Cómo se ve el link compartido en un WhatsApp real: lo deducimos de lo que la página le entrega a esas apps, no lo probamos en un teléfono.
- Si Google muestra hoy las páginas "v2"/"v3" en sus resultados: vimos que están en el mapa del sitio, no buscamos una por una en Google.
- Las notas en sitios de viaje vienen de resultados de búsqueda, no las abrimos en cada sitio.
- Los tiempos son de una simulación de 4G lenta en nuestro equipo; un celular real puede andar algo mejor o peor.
- No enviamos el formulario, así que no sabemos si los mensajes llegan.
- No revisamos la seguridad interna del sitio (versiones de WordPress y complementos, administración): eso necesita acceso del dueño.
- No sabemos cuántas reservas llegan hoy por la web y cuántas por plataformas: eso hay que preguntárselo al dueño.
