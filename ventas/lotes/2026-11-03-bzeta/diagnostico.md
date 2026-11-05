# Diagnóstico de mejoras web — B-Zeta Ingeniería (ingeniería eléctrica, La Ligua)

Borrador de trabajo de Ascensus · 3-nov-2026. **No es el informe final**: los PDF se preparan solo cuando Mathias lo indique.
Revisión hecha en el navegador integrado, en computador y en celular emulado (375×812, no un teléfono real).

Contacto: Clodomiro Aravena Lazcano, Project Manager y socio fundador — +56 9 9430 9410 · clodomiro.aravena@bzeta.cl. Respondió el 3-nov a las 16:04 pidiendo el diagnóstico.

## Lo que hay hoy (verificado 3-nov)
- WordPress 7.1.4 con tema Astra + Astra Addon, Elementor, Essential Addons, SpeedyCache Pro y CookieAdmin.
- Páginas: Inicio, Servicios (`/pagina_servicios/`), Sobre Nosotros (`/about/`), Contacto y 6 fichas de servicio en `/servicios/…`.
- Oferta: ingeniería eléctrica para minería subterránea y plantas desaladoras. Servicios: ingeniería (eléctrica, civil estructural, perfil/conceptual/básica/detalle, impacto ambiental, líneas de media tensión), estudios sistémicos (flujos de potencia, cortocircuito, coordinación de protecciones, arc flash, puesta a tierra), pruebas y ensayos (cables MT, transformadores, parques fotovoltaicos), fibra óptica, integración de tableros y montaje eléctrico.
- Fundada en 2022 por Clodomiro Aravena Lazcano (Ing. en Electricidad, Magíster en Ing. Industrial) y Maglio Pérez Fajardo (Ing. en Electricidad), ambos con más de 20 años de experiencia.
- Portada: 66+ proyectos, 4+ años, 20+ clientes, 100 % compromiso con calidad y seguridad.
- Contacto: teléfono, correo y dirección (Reserva Cora Lote 1, La Ligua) solo como texto. Sin formulario ni WhatsApp.
- A favor: carga razonable (≈1,9 s en esta prueba, 1,2 MB), fotos con texto alternativo, idioma correcto, robots.txt y sitemap presentes, y la página Servicios sí detalla bien la oferta.

## Hallazgos (por importancia)
1. **Texto de relleno en la portada** (Confianza) — Las 6 tarjetas de "Servicios de Calidad" dicen "Lorem ipsum dolor sit amet…". Para un gerente de proyecto o de mantenimiento de una minera, es la señal de una web sin terminar justo donde se presentan los servicios. Arreglo: una frase concreta por servicio (ej. "Estudios de cortocircuito, coordinación de protecciones y arc flash") con enlace a su ficha.
2. **5 de 6 fichas de servicio están vacías** (Confianza / Visitas) — Estudios sistémicos, Pruebas y ensayos, Fibra óptica, Integración de tableros y Montaje de sistemas eléctricos muestran solo el título y "Por admin / agosto 19, 2025". Solo Ingeniería tiene contenido. Además, la tarjeta "Montaje Eléctrico" de la portada no enlaza a nada y el menú del pie omite ese servicio. Arreglo: llenar cada ficha con alcance, normas, equipos, ejemplo de proyecto y botón de cotizar.
3. **Contactar cuesta más de lo necesario** (Consultas) — En ninguna página el teléfono o el correo son enlaces (tocar no llama ni abre el correo); no hay formulario de cotización ni WhatsApp. Los botones "Contáctanos" llevan a una página que vuelve a mostrar el mismo texto. Arreglo: teléfono y correo clicables, formulario corto de cotización (empresa, faena, servicio, plazo) y botón de WhatsApp.
4. **Detalles visibles en celular** (Confianza) — En Contacto el logo queda encima del título "Contacto". En las fichas, los enlaces "Servicio anterior / siguiente" son blancos sobre fondo claro (casi invisibles). En la portada aparece "B-Zeta Ingeniería" dos veces seguidas (logo + texto) y el aviso de cookies tapa casi la mitad de la primera pantalla, aunque la web no usa herramientas de analítica ni publicidad.
5. **Google recibe señales pobres** (Visitas) — La meta descripción de cada página es el texto pegado de la página ("B-Zeta Ingeniería Ingeniería Especializada… Nuestros Servicios Contáctanos…"); las fichas vacías no tienen. El dato de empresa (Schema Organization) tiene el nombre vacío. Las etiquetas para compartir en redes están duplicadas. El sitemap envía a Google la entrada de prueba "Hello world!" (pública, con un comentario de ejemplo y formulario de comentarios abierto) y dos plantillas internas de Elementor. Hay dos sitemaps distintos (`sitemap.xml` y `sitemap_index.xml`). Títulos dicen "Ingenieria" sin tilde.
6. **Sin medición** (Visitas) — No hay Google Analytics ni otra analítica: hoy no se puede saber cuántas visitas llegan ni desde dónde.

## Plan sugerido (según TARIFARIO.md)
- **Renovación de web existente — $249.990** (caso "web con relleno / sin botón de contacto"). Cubre los hallazgos 1–6 sobre su mismo WordPress.
- Por confirmar con Mathias: si se ofrece también el asistente o la ficha de Google Maps (no verificado si tienen ficha).

## Descartado en la revisión
- "El aviso de cookies reaparece en cada página": el navegador integrado bloquea cookies (`document.cookie` no guarda nada), así que no se puede atribuir a la web. Comprobar en un navegador normal si se quisiera incluir.

## Agregado al preparar los PDF (verificado 3-nov)
- Clientes (Albemarle, CDM Smith, Equans, Vandoorn, Inprodec, Enky, Mas Errázuriz, Organic) solo en "Sobre Nosotros", al fondo y en carrusel de a uno.
- Google Maps: "B-Zeta Ingeniería La Ligua" abre la ficha de Elektrón Ingeniería (cerrada temporalmente). No se encontró ficha de B-Zeta.
- En Google, el resultado de la página Servicios muestra el texto del pie y del aviso de cookies.
- El logo también tapa el título en "Sobre Nosotros"; el botón flotante de cookies muestra una imagen rota.

## Antes del informe final (hecho el 3-nov: PDF en `pdf/`)
- Capturas en celular para `capturas/` (portada con lorem ipsum, ficha vacía, Contacto con logo encima).
- Colores, logo y fotos de la web para los PDF (verde oscuro de marca, amarillo de titulares, logo `cropped-B-Zeta-Ingenieria-7.png`).
- Verificar ficha de Google Maps / reseñas y competidores de ingeniería eléctrica minera en la zona.
- Revisar en escritorio si el logo también pisa títulos en otras páginas internas.
