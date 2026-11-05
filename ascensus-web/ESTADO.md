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
