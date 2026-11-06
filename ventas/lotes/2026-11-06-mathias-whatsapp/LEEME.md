# WhatsApp de Mathias, 6-nov-2026: zona alta de la costa

Lo preparó el Claude de Mathias el 6-nov a pedido de Mathias: 17 negocios (eran 20; se sacaron 3 en la revisión) de la zona de más ingresos de la Región de Valparaíso (Zapallar–Cachagua–La Laguna, Reñaca, Concón, Maitencillo y Santo Domingo), con el mensaje de WhatsApp ya escrito.

| Archivo | Qué es |
|---|---|
| [whatsapp.html](whatsapp.html) | Página para el celular: un botón "Abrir en WhatsApp" por negocio, botón copiar y check de enviado. |
| [filas_para_prospectos.csv](filas_para_prospectos.csv) | Las 17 filas del lote con el formato de `registro/prospectos.csv`: empresa, rubro, comuna, teléfono, hecho comprobado y servicio sugerido. |

Envía Mathias desde el +56 9 4931 1482.

**EN REVISIÓN — NO ENVIAR.** Varios mensajes dicen que el negocio no tiene web o carta y eso no se vio en Google Maps (La Choca sí tiene menú). Antes de enviar, Claude debe verificar los 17 en Maps desde el PC de Mathias siguiendo `ventas/metodo/VERIFICAR_EN_MAPS.md`.

**Pendiente:** copiar las 17 filas de `filas_para_prospectos.csv` al final de `registro/prospectos.csv` (estado `preparado_whatsapp`; al enviar, cambiar a `enviado` con la fecha). Se subieron aparte porque el lote se subió a GitHub por la conexión directa y el registro completo era demasiado grande para copiarlo entero sin riesgo. Mientras tanto, el cruce de repetidos también revisa `lotes/`, así que estas empresas ya cuentan como tomadas por Mathias.

## Cómo se armó
- **Fuente:** el registro público de Sernatur ya descargado en `lotes/2026-11-04-region/sernatur.json` (celulares publicados por los mismos negocios). Este entorno no llegaba a Google Maps ni a OpenStreetMap, así que no se usaron.
- **Sin repetidos:** cada nombre y cada teléfono se cruzó contra `registro/*.csv`, `tablero/` y todos los `lotes/`, incluido el lote del 6-nov de Santiago. Se sacaron Emeterio, Chorrillos, Las Suculentas, La Bahía, Santo Pez y La Pica de San Pedro porque ya aparecían.
- **Hechos:** todos están en Sernatur sin web en su ficha. El 6-nov se buscó cada uno en internet. Tienen un dato extra La Choca (4,3 con 371 reseñas), Laura del Mar (9,3 en Booking), La Pescá (notas de The Clinic y Diario Uno), Winecaina y Novellino (reseñas y guías). El resto casi no aparece en los buscadores.

## Revisión del 6-nov (segunda pasada)
- Se intentó revisar en Google Maps con el entorno "oficina", pero Maps no muestra los datos a un navegador automático y no se forzó la protección anti-bots de Google. La revisión se hizo con búsquedas web.
- **Se sacaron 3:** Bloom Bar (sí tiene web, bloombar.cl, y 4,7 con 219 reseñas), Apart Hotel Bocamar (2,0 de 10 en Hotels.com) y Club House by Concón (reseñas con quejas de limpieza). Quedan en Sernatur; no se les escribió.
- **Se reescribieron 2 con datos reales:** Café Glacé (4,5 con ~295 reseñas, desayunos y pan amasado) y Borde Mar (porciones generosas, paila marina, casona de madera).
- Antagonista, Bonafide, Tío Tomate, Carnivorus, Calesta, Obelisco/Palm Beach, Punta del Sol y el Club House de Santo Domingo casi no aparecen en internet: el mensaje dice eso y es cierto, pero puede que alguno haya cerrado. Mirar su Maps antes de enviar.

## Ojo antes de enviar (desvíos de la regla)
- **Estos negocios sí publican correo en Sernatur.** La rutina dice que WhatsApp es solo para quienes no publican correo. Se usó WhatsApp porque Mathias lo pidió así. No se les manda correo, para no escribirles por los dos canales.
- **No se pudo revisar Google Maps ni Instagram.** Antes de tocar enviar, mirar 1 minuto su Instagram o su Maps: si tienen web, ajustar ese mensaje o saltárselo.
- Los mensajes tienen unas 80 palabras, igual que los de Santiago, más que las ≈50 de la rutina. No pasaron por la skill `humanizador` porque no estaba disponible en este entorno.
- Algunos locales de playa (Maitencillo, Santo Domingo) abren solo en temporada: puede que no respondan hasta diciembre.
