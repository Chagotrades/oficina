# WhatsApp de Mathias, 6-nov-2026: zona alta de la costa

Lo preparó el Claude de Mathias el 6-nov a pedido de Mathias: originalmente 17 negocios (eran 20; se sacaron 3 en la revisión). **Tras verificar en Google Maps el 6-nov quedaron 5, y se sumaron 12 buscados directo en Maps: hoy son 17** de la zona de más ingresos de la Región de Valparaíso (Zapallar–Cachagua–La Laguna, Reñaca, Concón, Maitencillo y Santo Domingo), con el mensaje de WhatsApp ya escrito.

| Archivo | Qué es |
|---|---|
| [whatsapp.html](whatsapp.html) | Página para el celular con los 17 revisados en Maps: un botón "Abrir en WhatsApp" por negocio, botón copiar y check de enviado. Publicada en https://claude.ai/code/artifact/a03e3bb6-7ba6-4c7a-8408-b63f225a30cc |
| [verificacion_maps.md](verificacion_maps.md) | Lo que se vio el 6-nov en Maps, web e Instagram de cada uno de los 17 originales (y por qué se mantiene o se saca) y de los 12 nuevos. |
| [filas_para_prospectos.csv](filas_para_prospectos.csv) | Las 17 filas del lote con el formato de `registro/prospectos.csv`: empresa, rubro, comuna, teléfono, hecho comprobado y servicio sugerido. |

Envía Mathias desde el +56 9 4931 1482.

**Verificado en Google Maps el 6-nov** (Claude de Mathias, con Claude in Chrome, según `ventas/metodo/VERIFICAR_EN_MAPS.md`). Quedan 5, todos con el mensaje reescrito: La Choca, La Pica de Octavio, Novellino, Calesta y Punta Natural. Se sacaron 12: 2 cerrados permanentemente (Café Glacé, Palm Beach), 4 que ya tienen web o lo tienen todo resuelto (Tío Tomate, Bonafide, Laura del Mar, Winecaina), 2 con carta y botón de reservar en Maps (Carnivorus, La Pescá) y 4 que no se pudieron confirmar (Antagonista, Borde Mar, Punta del Sol, Club House). Detalle en `verificacion_maps.md`. **Falta que Mathias apruebe y envíe** desde la página.

**Ampliación del 6-nov (pedido de Mathias): 12 negocios nuevos buscados solo en Google Maps, sin Sernatur.** Donde Gaston, Laguna Gourmet, Máskelados (La Laguna), Alazán y Chiringuito de Costa (Cachagua), Empanadas El Hoyo y Beach Break (Maitencillo), Don Rola, La Catita, Sunshine, La Cocinería y Rompeolas (Papudo). Todos con celular en Maps, sin web propia ni botón de reservar (o con un enlace roto que hace de web), cruzados contra el registro por nombre y teléfono. Detalle y descartados en `verificacion_maps.md`.

Las 17 filas ya están al final de `registro/prospectos.csv` (estado `preparado_whatsapp`; al enviar, cambiar a `enviado` con la fecha). En 3 se usa el teléfono de Maps, que era distinto al de Sernatur (La Choca, La Pica de Octavio, Punta Natural).

## Cómo se armó
- **Fuente:** el registro público de Sernatur ya descargado en `lotes/2026-11-04-region/sernatur.json` (celulares publicados por los mismos negocios). Este entorno no llegaba a Google Maps ni a OpenStreetMap, así que no se usaron.
- **Sin repetidos:** cada nombre y cada teléfono se cruzó contra `registro/*.csv`, `tablero/` y todos los `lotes/`, incluido el lote del 6-nov de Santiago. Se sacaron Emeterio, Chorrillos, Las Suculentas, La Bahía, Santo Pez y La Pica de San Pedro porque ya aparecían.
- **Hechos:** todos están en Sernatur sin web en su ficha. El 6-nov se buscó cada uno en internet. Tienen un dato extra La Choca (4,3 con 371 reseñas), Laura del Mar (9,3 en Booking), La Pescá (notas de The Clinic y Diario Uno), Winecaina y Novellino (reseñas y guías). El resto casi no aparece en los buscadores.

## Revisión del 6-nov (segunda pasada)
- Se intentó revisar en Google Maps con el entorno "oficina", pero Maps no muestra los datos a un navegador automático y no se forzó la protección anti-bots de Google. La revisión se hizo con búsquedas web.
- **Se sacaron 3:** Bloom Bar (sí tiene web, bloombar.cl, y 4,7 con 219 reseñas), Apart Hotel Bocamar (2,0 de 10 en Hotels.com) y Club House by Concón (reseñas con quejas de limpieza). Quedan en Sernatur; no se les escribió.
- **Se reescribieron 2 con datos reales:** Café Glacé (4,5 con ~295 reseñas, desayunos y pan amasado) y Borde Mar (porciones generosas, paila marina, casona de madera).
- Antagonista, Bonafide, Tío Tomate, Carnivorus, Calesta, Obelisco/Palm Beach, Punta del Sol y el Club House de Santo Domingo casi no aparecen en internet: el mensaje dice eso y es cierto, pero puede que alguno haya cerrado. Mirar su Maps antes de enviar. *(Superado: la verificación en Maps del 6-nov mostró que varios sí aparecen, tienen web o cerraron; ver `verificacion_maps.md`.)*

## Ojo antes de enviar (desvíos de la regla)
- **Estos negocios sí publican correo en Sernatur.** La rutina dice que WhatsApp es solo para quienes no publican correo. Se usó WhatsApp porque Mathias lo pidió así. No se les manda correo, para no escribirles por los dos canales.
- Los mensajes tienen entre 76 y 80 palabras (Mathias pidió 50 a 80). Se reescribieron el 6-nov con los datos de Maps y pasaron por la skill `humanizador`.
- Algunos locales de playa (Maitencillo, Santo Domingo) abren solo en temporada: puede que no respondan hasta diciembre.
