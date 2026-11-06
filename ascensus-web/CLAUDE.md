# Web corporativa de Ascensus

Encargo de **Mathias**, 5 de noviembre de 2026: construir la web de la empresa a partir del contexto compartido y la propuesta visual aprobada, y subir el código a GitHub para continuar con Claude.

## Dirección vigente

- Predominan blanco marfil `#f4f2ed` y negro `#171716`. Mathias pidió explícitamente jugar más con blanco y negro, no con naranja.
- Conservar la cascada diagonal de sitios, la tipografía grande, el espacio editorial y las demos filtrables por rubro.
- `docs/referencia-visual.png` documenta la composición original. Su naranja fue reemplazado por la nueva indicación; no restaurarlo por seguir la imagen.
- Logo oficial desde el 5-nov-2026: los archivos que Santiago dejó en `Escritorio/Ascensus` (IMG_3314–3317). En la web: `assets/ascensus-word*.png` (palabra sin el punto; el punto se dibuja en CSS para animarlo), `assets/ascensus-logo*.png` (completo), `favicon.png` y `apple-touch-icon.png`. `ventas/marca/` todavía tiene el logo anterior. No cambiar identidades externas.
- Las fotos de las demos van a color (pedido de Santiago, 5-nov): el trabajo debe destacar más que la propia web, que sigue en blanco y negro.

## Límites

- Leer `ESTADO.md` antes de editar y actualizarlo al cerrar un bloque sustancial.
- Tomar y cerrar el encargo en el `ENCARGOS.md` de la oficina. Un solo agente modifica estos archivos a la vez.
- Trabajar solo en esta web; no hace falta leer otros clientes.
- No mostrar prospectos ni casos de clientes como portafolio sin permiso. Las seis marcas son ficticias y deben seguir identificadas como demos conceptuales.
- No inventar testimonios, cifras de resultados, precios, plazos ni perfiles de redes sociales.
- El teléfono comercial de Mathias está documentado en `ventas/empresa/RESUMEN_PARA_CODEX.md`. El enlace lo abre únicamente el visitante, después de revisar el texto. No enviar pruebas a WhatsApp ni a cuentas reales.
- No agregar formularios que parezcan enviar sin hacerlo. Actualmente no hay backend ni almacenamiento: la consulta se prepara solo en el navegador.
- Esta autorización fue para crear la web y subirla a GitHub. Publicar en un dominio, contratar alojamiento, conectar servicios o instalar seguimiento necesita el encargo correspondiente de un socio.

## Implementación

HTML, CSS y JavaScript, sin dependencias. `node server.mjs` para servir en localhost; `npm run check` para revisar sintaxis. Los datos de las demos viven en el arreglo `demos` de `app.js`. No convertirlo en una app compleja sin una necesidad concreta.

Antes de entregar un cambio, comprobar 320, 375, 390 y 1440 px, filtros, seis demos, vista móvil, Escape, menú, foco y formulario con campos vacíos y texto con caracteres especiales. Las cabeceras, HTTPS y funcionamiento real del alojamiento se revisan cuando se publique.
