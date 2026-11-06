# Ascensus web — continuidad

Actualizado: 5 de noviembre de 2026. Responsable: Mathias. Ejecuta: Codex.

## Encargo

Crear la web corporativa usando el contexto de Ascensus y la propuesta visual elegida, con código en `Chagotrades/oficina` para continuar con Claude. Última corrección de Mathias: **más blanco y negro, sin protagonismo naranja**.

## Hecho

- Web estática completa en `ascensus-web/`, sin dependencias de producción.
- Diseño editorial marfil/negro; logo existente de la oficina; titular aprobado; cascada de seis propuestas.
- Galería filtrable y seis demos navegables con vistas de escritorio y celular.
- Secciones del estudio, principios, proceso y contacto.
- Contacto sin backend: valida nombre, negocio e idea, prepara una vista previa y permite editar/copiar/abrir WhatsApp. Ningún envío automático ni datos guardados en esta web.
- Fotos y fuentes locales, con procedencia y licencias de fuentes documentadas.
- Instrucciones para continuar, referencia visual, capturas y verificación guardadas en esta carpeta.
- Sin testimonios ni cifras inventadas; ningún prospecto mostrado como cliente; ningún caso real usado sin permiso.

## Comprobado

- Edge/Chromium a 320, 375, 390, 640, 768, 1024 y 1440 px: sin desplazamiento horizontal, fotos rotas, anclas inexistentes ni botones de miniaturas cortados.
- Cinco filtros, seis demos, cambio a vista celular, navegación interna y Escape.
- Consulta desde una demo conserva la intención; validación de espacios vacíos, texto con etiquetas mostrado de forma segura y enlace de WhatsApp codificado.
- Menú móvil, movimiento reducido y sintaxis JavaScript.
- Cero errores de JavaScript y cero respuestas HTTP fallidas durante la QA.
- Perfil 4G simulado (1,6 Mbps / 150 ms / CPU 4× / caché vacía): aproximadamente 523 KB transferidos, primer contenido a 0,77 s y evento de carga a 3,12 s en localhost. No es una medición del futuro alojamiento ni de un teléfono real.
- Revisión independiente: **LISTO para entregar código y continuar en GitHub**, sin hallazgos importantes dentro del alcance. Detalle en `docs/VERIFICACION.md`.

## Estado y siguiente paso

Implementación terminada para revisión visual de Mathias. El código queda en la rama `main` del repositorio de la oficina. No se desplegó en un dominio ni se creó un servicio de alojamiento.

Después de la revisión visual: ajustar lo que pida Mathias y, si da el encargo, elegir dominio/alojamiento y comprobar la publicación. Instagram y correo corporativo no se enlazan porque todavía no hay canales confirmados.

## Límites de la comprobación

No se enviaron mensajes; no se probó la entrega real de WhatsApp. No se comprobó Safari/iOS, dispositivos físicos ni alojamiento de producción. Las demos son exploraciones visuales: no son motores de reservas, tiendas ni sistemas clínicos. Fotos de referencia, no fotografías de trabajos o clientes de Ascensus.

## Bloque 2 — 5 de noviembre de 2026, noche (Santiago con Claude)

Pedido de Santiago: logos nuevos, más animación, más atractiva y fácil de entender, manteniendo el diseño base.

- **Logo nuevo** en cabecera, pie (versión blanca grande), visor de demos y favicon. El punto del logo es un círculo CSS: cae y rebota al cargar, sube al pasar el mouse ("ascensus" = ascender).
- **Portada:** el titular entra línea por línea, "Hagámoslo visible" se subraya solo, las seis tarjetas entran en cascada y siguen al mouse con profundidad. Botón principal nuevo: "Diagnóstico sin costo" (abre el contacto con la idea ya escrita).
- **Cascada (ajuste final de Santiago):** diagonal con leve curva (se probó un cuarto de curva hacia la izquierda y Santiago prefirió volver a esta), tarjetas casi de frente (2° a 4°), perspectiva suave (`rotateY(-5deg)`, sin inclinarlas hacia atrás) y la primera más grande (1,14×). Posiciones en `--cx/--cy/--rotation/--s` por tarjeta; cada ancho comprime con `--sx/--sy` en `.hero-collage`. Al pasar el cursor: la tarjeta sube 42 px, se endereza, crece 4% y gana una sombra más amplia, en 350 ms sin rebote; la de adelante baja 30 px; ninguna cambia de capa. Comprobado de 320 a 1700 px: no tapa texto, no se sale por la derecha ni invade la cinta.
- `.hero-actions` lleva `pointer-events:none` y solo sus botones reciben el mouse: antes tapaba de forma invisible las tarjetas de abajo y no subían.
- **Fotos de las demos a color** (antes en gris) con degradado para leer el texto; al pasar el mouse se acercan y ganan color. Aviso "Abrir demo" (siempre visible en celular).
- **Orden nuevo:** portada → cinta → 01 Demos → 02 Qué hacemos → 03 El estudio → 04 Cómo trabajamos → contacto → pie negro.
- **Sección nueva "Qué hacemos"** con los tres servicios del tarifario explicados en simple (sin precios: la simplificación del tarifario sigue pendiente) y un bloque de diagnóstico sin costo. Cada "Me interesa" abre el contacto con la idea escrita, sin pisar lo que el visitante ya escribió.
- Cabecera fija con barra de progreso, cinta de beneficios que se detiene fuera de pantalla, apariciones al hacer scroll (ocultas solo si el JS corrió, con red de seguridad), botones que se inclinan hacia el mouse, ventanas que entran con fundido.

### Comprobado (5-nov, Edge del panel y sonda con Edge sin pantalla)
- 320, 375, 768 y 1440 px: sin desplazamiento lateral (las tarjetas que entran desde la derecha quedan recortadas con `overflow-x: clip`), menú móvil, filtros (Servicios = 3, Todos = 6), visor de demos, contacto con idea precargada, cero errores de consola, cero imágenes rotas.
- A 1000 px o menos se oculta "Cómo trabajamos" del menú de escritorio para que no se parta en dos líneas.
- Cuadros con CPU 4× en celular (ya cargada): 0 perdidos, igual que la versión anterior. **Durante la carga** con CPU 4×: 1–4 cuadros perdidos y 0–2 tareas largas en la nueva contra 0 en la anterior (3 corridas cada una): la entrada animada cuesta algo en un teléfono lento. Pendiente si molesta: acortar la entrada en celular.

### No comprobado
- Safari/iOS y teléfono físico. `prefers-reduced-motion` solo revisado en código y con una captura de la sonda.
- `ventas/marca/` sigue con el logo anterior; los PDF y correos no se tocaron.
