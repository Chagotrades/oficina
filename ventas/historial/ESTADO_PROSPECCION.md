# Ascensus — estado (antes FARO; actualizado 3-nov-2026)

## Hecho
- Carpeta FARO creada con contexto, tarifario, flujo, plantillas y registro de prospectos.
- Skills instaladas en `~/.claude/skills` (gratis):
  - `lead-research-assistant` (Composio awesome-claude-skills).
  - `email-writing-frameworks`, `email-1-variations-7`, `personalization-hooks`, `josh-braun-copywriting`, `cold-call-scripts` (ColdIQ GTM Skills). Se les quitó el bloque "ColdIQ first", que pedía usar su API de pago.
- Descartado: Superpowers (es para programar), conectores de Composio (servicio con planes de pago), resto de ColdIQ (dependen de Clay/Apollo o son para secuencias de varios correos).
- Gmail conectado (conector oficial de Google).
- Primer lote, Viña del Mar: 5 empresas formadas con correo público y hallazgo comprobado (Parque del Mar, Kenz Joyería, Contacto Roller, Natural Bikes, Clínica Dib & Seymour).
  - Carpeta `lotes/2026-11-03-vina-del-mar/`: `datos.json` + por empresa diagnóstico PDF y 3 imágenes de propuesta.
  - 5 borradores creados en Gmail (ids en prospectos.csv). Firma: "Mathias · Faro SaMa · WhatsApp +56 9 4931 1482".
- Lote litoral (exploratorio, 4 rubros × 5): cabañas, clínicas dentales, constructoras y restaurantes en El Quisco, Algarrobo, San Antonio, Concón, Viña del Mar y Quilpué.
  - Carpeta `lotes/2026-11-03-litoral/`: `datos.json` + por empresa diagnóstico PDF, 3 imágenes de propuesta y `correo.txt`.
  - 20 borradores creados en Gmail, sin adjuntos (ids en prospectos.csv). Firma: "Mathias Lezana · Faro SaMa · WhatsApp +56 9 4931 1482".

## Decisiones del lote
- Solo empresas formadas (reseñas, años, razón social) y solo con correo público.
- El primer correo NO lleva adjuntos (los adjuntos de desconocidos caen en spam): menciona un hallazgo y ofrece el diagnóstico. El PDF y las imágenes se envían cuando respondan.
- Descartados por no tener correo público: 4 empresas de fletes (ver prospectos.csv).
- Google Maps sin sesión no abre fichas; PageSpeed sin clave bloquea por cuota. Fuentes que sí funcionan: OpenStreetMap (overpass-api.de), webs de las empresas y medición en el navegador del panel.
- Lote litoral: la lista de resultados de Google Maps (`/maps/search/...`) sí muestra nota, reseñas y web. El registro de Sernatur (serviciosturisticos.sernatur.cl, buscador por comuna y tipo) publica el correo de restaurantes y alojamientos: es la mejor fuente para turismo. Google Search empezó a pedir verificación anti-robots tras muchas búsquedas; no se salta.
- Lo que más se repite en el litoral: webs caídas o dominios que no existen pero siguen publicados en Sernatur o en guías, y webs sin botón de WhatsApp. Las clínicas dentales pequeñas del Litoral Central casi no publican correo; las de San Antonio y Concón con web propia sí.

## Envíos del 2-nov
- Enviados 2-nov 9:00 (11): Parque del Mar, Kenz, Contacto Roller, Natural Bikes, Dib & Seymour, Cabañas El Faro, Canemar, La Playa, Santa Bárbara, Aguasmarinas, Costa Mar.
- Cancelados y devueltos a Borradores (14): dentistas (Odentix, Delta Dent, Oceánica, Rialto), constructoras (AM Modular, Navarrete, MSP, Aconcagua, Vimac) y restaurantes (La Jovita, Los Cipreses, El Quincho, Nicho, Café & Bar de Paola).
- Decisión de Mathias (2-nov): no partir el correo recalcando un error del negocio; buscar otro enganche. Firma con nombre y apellido (Mathias Lezana). Los 14 se reescriben antes de volver a programar.
- Aprendizaje: el conector de Gmail convierte cualquier dominio escrito en el texto (ej. "empresa.cl") en un enlace largo de google.com/url. No escribir dominios en el cuerpo, o revisar el borrador en Gmail antes de enviar. Y no dejar un borrador abierto en Gmail web mientras se edita por el conector: lo sobrescribe.

## Campaña 3-nov (preparada el 2-nov)
- Tabla única: [tabla_comercial.csv](tabla_comercial.csv) con 77 empresas (11 enviadas, 15 A, 14 B de reserva, 37 C descartadas), fuente del correo, hallazgos, hipótesis, asunto, cuerpo, palabras, estado e id del borrador.
- Textos en `lotes/2026-11-03-campana/correos.json`, con las 3 plantillas de Mathias (hecho concreto, idea de renovación, situación del cliente), ≤90 palabras, sin dominios ni precios.
- 14 pausados: 11 reescritos en sus mismos borradores (sin duplicados); Los Cipreses, El Quincho y Nicho quedaron con asunto "[PENDIENTE - NO ENVIAR]" por falta de un hecho verificable. Aconcagua (C), Vimac (C), MSP (B) y Odentix (B) quedaron reescritos pero fuera de la programación.
- 8 nuevos A con borrador: Marglass, Reñaca Roller, Roller Solutions, Petreos Viña, Opendeco, Aire Puro Olmué, Cabañas El Canelo, Hostería Montemar.
- **Programados (aprobado por Mathias el 2-nov):** 15 correos A el 3-nov de 09:00 a 11:48, cada 12 minutos, America/Santiago. Verificado en Gmail: "Programados (15)". Se programaron desde Gmail web en el navegador integrado (Más opciones de envío → Programar envío → Elegir fecha y hora).
- Revisión en celular de 69 webs (columna `revision_movil`): 3 no adaptadas (Costa Mar, Navarrete Artigas, Aconcagua), 25 adaptadas con problemas, 35 adaptadas, 8 sin web activa. Hecha con emulación 375×812, no en un teléfono real.
- Fuentes que funcionaron: Google Maps (lista), Google Search con pausas, registro Sernatur y revisión de cada web con script. Bing por curl no sirve (resultados irrelevantes).

## Lote Codex A (programado el 3-nov, madrugada)
- Fuente: `E:\Trasladado_desde_C\Documentos\ChatGPT\FARO\Prospectos_A_TARIFARIO_para_Claude_2026-11-02.txt` (20 A). Desde ahora el trabajo diario sigue [RUTINA_DIARIA.md](RUTINA_DIARIA.md).
- Cruce: 19 sin contacto previo (archivos y Gmail). Excluido Café & Bar de Paola (A06): ya estaba programado el 3-nov 10:12.
- Por el límite de unos 20 al día, Mathias eligió repartir: 5 el 3-nov (Cumbres 9:06, Casa Inka 9:42, B-Zeta 10:18, GammaDentis 10:54, Espacio Fonoaudiológico 11:30) y 14 el 4-nov de 9:00 a 11:23, cada 11 min (A07–A20 en orden).
- Verificado en Gmail: "Programados (34)" = 20 del 3-nov + 14 del 4-nov. Detalle e ids de borrador en prospectos.csv.
- Incidente corregido: en B-Zeta la hora se escribió por error en el cuerpo ("10:18Vi que…"); se borró antes de programar. Para evitarlo, comprobar que el diálogo "Elegir fecha y hora" esté abierto antes de escribir (las capturas del panel llegan con un paso de atraso).

## Lote región 4–6 nov (preparado el 3-nov de madrugada)
- Pedido de Mathias (3-nov): 20 correos A diarios entre 08:30 y 11:59 hasta el viernes 6, empresas de toda la región, sin repetir.
- 60 empresas A nuevas (20 por día) con borrador en Gmail: [lotes/2026-11-04-region/LOTE_PARA_APROBAR.md](lotes/2026-11-04-region/LOTE_PARA_APROBAR.md). Ids en `ids_borradores.json`; filas agregadas a tabla_comercial.csv y prospectos.csv con estado `borrador` y hora propuesta.
- **Aprobado por Mathias (3-nov) y programado: 46 de los 60.** Verificado en Gmail: Programados (80) = mar 3: 20 · mié 4: 20 (6 nuestros a las 08:30, 08:45, 11:30, 11:38, 11:46 y 11:54, alrededor de 14 de Codex de 09:00 a 11:23) · jue 5: 20 (08:30–11:59 cada 11 min) · vie 6: 20 (08:30–11:59). Horas por correo en `programacion.json`.
- Se descubrió al programar que otra sesión ya había puesto 14 correos de Codex el miércoles 4; para respetar 20/día quedaron 14 de reserva, que Mathias aprobó para el **lunes 9 (08:30–11:58, cada 16 min; verificado, Programados 94)**: Vidriería Vitorio, Centro Frenos, Hotel Brighton, Sazón del Inka, El Campito, B&B Rocas, Océano, La Ritoqueña, Camping Chivato, Biosfera Lodge, BCW Casablanca, Get Up, García Vellella, Castillo y Garín (estado "borrador (reserva…)" en la tabla).
- Programación automatizada en Gmail web con un script en la página (buscar `in:draft to:correo` → Más opciones de envío → Programar envío → Elegir fecha y hora). Con el panel oculto usar `textContent`, no `innerText`.
- Comunas nuevas: Quillota, La Cruz, La Calera, Los Andes, San Felipe, Limache, Olmué, Curauma, Papudo, Los Molles, Puchuncaví, Ritoque, Santo Domingo, Casablanca, San Antonio, Valparaíso, Viña, Concón, Villa Alemana.
- Cruce hecho contra tabla, prospectos, lotes, archivos de Codex y Gmail (enviados, borradores y búsqueda in:anywhere): 0 coincidencias.
- Revisión en celular de las 88 webs del pool con Edge headless (375×812) en `movil_1.json`; resumen en la columna `revision_movil`.
- Método que funcionó: lista de Google Maps sin sesión (`/maps/search/rubro+comuna`) + OpenStreetMap (Overpass, con Python; curl falla por TLS) + script que lee la web y extrae correo. Scripts en la carpeta padre: `_faro_scan.py`, `_faro_texto.py`, `_faro_movil.mjs`, `_faro_maps2json.py`, `_faro_osm.py`.
- Reserva (con correo, sin redactar): Bosques Comestibles, Clau Joies, Hacienda Valdeperillo, Cetemel, TerraVets, Punto Mascotas, My Mundo Pets, Vetcare, Grupo Cueto, Propiedades Costa (web no adaptada a celular), Mahia, Hotel Mae, iDental, Tubo Stock.
- El lote de Codex del 3-nov (17 borradores: bzeta, veprint, altometal, etc.) es aparte y no se tocó.

### Filtro "oferta concreta del tarifario" (3-nov, pedido de Mathias)
- Regla nueva: solo se escribe a empresas donde se puede nombrar un servicio del TARIFARIO.md que les resuelva un problema medido (desborde en celular, web antigua o con texto de plantilla, sin WhatsApp/formulario/teléfono, pocas reseñas en Maps). Detalles menores (botones algo chicos, falta de formulario teniendo WhatsApp) no bastan.
- De los 60: **29 quedan programados** con su servicio en `servicio_recomendado` y el problema en `mejora_propuesta_hipotesis` (también en `lotes/2026-11-04-region/oferta_por_empresa.json`). **31 cancelados** (vuelven a Borradores, estado "descartado: sin oferta clara", prioridad C). Verificado: Programados (63), 0 descartados programados.
- Quedan por día: mié 4 = 4 nuestros + 14 Codex; jue 5 = 9; vie 6 = 6; lun 9 = 10. La cuota de 20/día ya no se cumple jueves y viernes.
- Revisados también con el filtro (3-nov madrugada): de 34 programados de campaña + Codex quedaron 16 y se cancelaron 18 (campaña: Delta Dent, Oceánica, Rialto, AM Modular, La Jovita, Marglass, Reñaca Roller, Roller Solutions, Petreos, Opendeco, Hostería Montemar; Codex: GammaDentis, Labopal, Transgesa, Farmacia Nahuen, Aquitania, Vivero San Pedro, Allegro). Mediciones en `revision_previos_scan.json` y `movil_lote2.json`.
- Quedan por día: mar 3 = 8; mié 4 = 12; jue 5 = 9; vie 6 = 6; lun 9 = 10. Reemplazos (3-nov): **35 aprobados por Mathias y programados**, verificado en Gmail: Programados (80) = mar 3: 8 · mié 4: 20 · jue 5: 20 · vie 6: 20 · lun 9: 12. Reparto de reemplazos: mié +8, jue +11, vie +14 (quedan 20/día) y lun +2. Detalle y textos: [lotes/2026-11-04-region/REEMPLAZOS_PARA_APROBAR.md](lotes/2026-11-04-region/REEMPLAZOS_PARA_APROBAR.md); horas en `programacion_reemplazos.json`.
- Fuente nueva que rinde: buscador de Sernatur (`_faro_sernatur.py`, 1.554 fichas de alojamiento y restaurantes de la región, con correo). Cruce con reseñas de listas de Maps (`_faro_cruce.py`). Dominios con web caída: verificar MX antes de escribir (Don Emelio y Cabañas Santa Fe sin MX, descartados).
- 3-nov 12:20, a pedido de Mathias ("pensé que teníamos 20 para hoy, envíalos"): los 12 del lun 9 se adelantaron a hoy, de 12:35 a 13:30 cada 5 min. Los 8 de la mañana (09:00–11:48) salieron sin rebotes. Verificado: Programados (72) = mar 3: 12 · mié 4: 20 · jue 5: 20 · vie 6: 20 · lun 9: 0. Respaldo de los CSV en `lotes/2026-11-04-region/_respaldo_*_antes_adelanto.csv`.
- Para cancelar un programado con script: `in:scheduled to:correo` → abrir → "Cancelar envío" → "Guardar y cerrar" (vuelve a Borradores); luego se programa igual que arriba.
- Para programar con script en Gmail web: `in:draft to:correo` → Más opciones de envío → Programar envío → Elegir fecha y hora (usar textContent, el panel suele estar oculto).

## Reescritura y aprobación por tablero (3-nov, tarde)
- **Marca nueva: Ascensus** (Mathias, 3-nov: "Nada más de FARO"). Los correos firman "Mathias Lezana / Ascensus". La carpeta sigue llamándose FARO hasta que Mathias diga otra cosa.
- Los 60 envíos de mié 4 a vie 6 se reescribieron uno por uno (motivo real → idea útil → pregunta fácil), con hechos comprobados el 3-nov. Textos y problemas: `lotes/2026-11-04-region/correos_semana_v2.json` (generado por `correos_v2.py`).
- Tablero (https://claude.ai/artifact/H8ocFj8fHuVTHwbxDByB4Y), pestaña **Correos**: problemas, asunto y cuerpo de cada uno, con Aprobar / Pedir cambios / No enviar. Colección `correos`, campo `aprobacion`.
- Marcados para revisar: Medikin (hallazgo débil, sugiero no enviarlo) y Chanagua (puede que el lodge no siga operando).
- Sin respuestas de prospectos en Gmail. Canemar (enviado el 2-nov) tiene aviso de entrega demorada.
- 3-nov, tarde: los 60 programados con el texto antiguo se cancelaron (Mathias: "Cancélalos tú") y volvieron a Borradores.
- **3-nov, noche: los 60 quedaron aprobados y reprogramados.** Mathias pidió ofrecer el informe "entremedio" (ya trajo 2 respuestas positivas) y luego "aprueba todos los correos". Cada correo lleva, antes de la pregunta final: "Si les sirve, les preparo sin costo un informe breve [de su web / de su web y su ficha en Google / de cómo los encuentra hoy un cliente en internet]: lo que encontré, en qué les afecta y cómo lo resolveríamos, con capturas reales. Sin compromiso." Textos en `correos_semana_v2.json`; ids de borrador en `gmail_actualizar.json`.
- Verificado en Gmail: Programados (60) con el texto nuevo (firma Ascensus, sin "Faro SaMa") y cada uno a su hora original: mié 4 = 20 (08:30–11:54), jue 5 = 20 (08:30–11:59), vie 6 = 20 (08:30–11:59), hora de Chile. Tablero: los 60 con `aprobacion: aprobado`.
- Medikin y Chanagua iban marcados "revisar" (hallazgo débil / quizás ya no opera); se enviaron igual por la aprobación de todos.
- Cómo programar con script en Gmail web (3-nov): `in:draft to:correo` → abrir → flecha "Más opciones de envío" → menuitem `[selector=scheduledSend]` (necesita mouseover+mousedown+mouseup+click) → "Elegir fecha y hora" → llenar Fecha ("4 nov 2026") y Hora ("8:30") → botón "Programar envío". El aviso "Envío programado para…" llega con un paso de atraso; verificar la hora con el título de cada fila en Programados o con `get_thread` (fecha en UTC).
- Cómo cancelar en Gmail web: la acción masiva ("Seleccionar las 60" → Cancelar envío → Aceptar) no surte efecto. Sí funciona uno por uno: buscar `in:scheduled to:correo` → abrir → "Cancelar envío" → "Guardar y cerrar", esperando a que cargue cada paso. Valhalla figura en Gmail como valhallarestobarsa@ (sin puntos); se encuentra buscando "valhalla".

## Cambio de marca a Ascensus (3-nov, tarde)
- Logo elegido (01 Editorial, del escritorio `Ascensus\Logos`) copiado y recortado en [marca/ascensus-logo.png](marca/ascensus-logo.png).
- Documentos de trabajo (CLAUDE, CONTEXTO, TARIFARIO, FLUJO, RUTINA, RESUMEN_PARA_CODEX, plantillas) ya dicen Ascensus.
- 25 diagnósticos y 75 propuestas (lotes Viña y litoral) llevan el logo y "Propuesta Ascensus"; PDF y PNG regenerados con Edge headless. Diagnóstico de La Ritoqueña actualizado.
- tabla_comercial.csv: "Faro SaMa" → "Ascensus" en 98 cuerpos aún no enviados; los enviados el 2 y 3-nov quedan como salieron.
- Tablero: logo en la cabecera (invertido en modo oscuro) y 5 tarifas corregidas en la base de datos.
- Sin cambiar, a propósito: textos ya enviados o aprobados (correo.txt, LOTE/REEMPLAZOS_PARA_APROBAR, correos_dia*/reemplazo*, respaldos), nombres de prospectos con "El Faro", nombre de la carpeta y scripts `_faro_*`.

## Pendiente
- 3-nov: después de las 13:30, confirmar en Enviados que salieron los 20 de hoy (8 de la mañana ya confirmados) y cambiar su estado a `enviado` en la tabla y en prospectos.csv.
- 4-nov: después de las 11:23, confirmar los 14 del lote Codex.
- Responder a quien acepte el diagnóstico: preparar PDF y 3 imágenes (incluir la revisión en celular).
- A los 11 enviados: si responden, contestar en el mismo hilo con su PDF y 3 imágenes.
- Aprobar o no la simplificación del tarifario.
- B-Zeta Ingeniería (Clodomiro Aravena, PM) pidió el diagnóstico el 3-nov 16:04. Diagnóstico en `lotes/2026-11-03-bzeta/diagnostico.md`. Informe (8 págs.) y propuesta (6 págs., Renovación $249.990) listos en `lotes/2026-11-03-bzeta/pdf/` y en el escritorio como `B-Zeta-Informe.pdf` / `B-Zeta-Propuesta.pdf`, con colores Manrope/Inter, verde #196B21 y amarillo #FFC03D. Hallazgos que más enganchan: lorem ipsum en portada, 5/6 fichas vacías, clientes (Albemarle, CDM Smith, Equans) escondidos y Maps muestra otra empresa (Elektrón Ingeniería). Mathias los envió el 3-nov por correo, en el mismo hilo. Próximo paso: esperar respuesta; si no hay en 2–3 días (≈6-nov), un solo seguimiento corto por correo ofreciendo 15 minutos.
- Biósfera Lodge (Juan Pablo Vásquez, recepcionbiosferalodge@gmail.com) aceptó la propuesta el 4-nov y avisó que la web está atada al motor de reservas (GoFeels). Santiago mandó diagnóstico y brief (zip en el escritorio). Informe (8 págs., con página "Su motor de reservas se queda") y propuesta (6 págs., $249.990, página de entrada que lleva a GoFeels sin tocarlo) en `lotes/2026-11-04-biosfera-lodge/pdf/` y en el escritorio como `Biosfera-Lodge-Informe.pdf` / `-Propuesta.pdf`. Colores: oliva #79804D, bosque #2F3B2A, Fraunces + Roboto. Mathias los envió el 4-nov por correo, en el mismo hilo, preguntando por el WhatsApp y las fotos originales. Próximo paso: esperar respuesta; si no hay en 2–3 días (≈7-nov), un solo seguimiento corto ofreciendo 15 minutos. Pendiente con el cliente: qué permite GoFeels (subdominio, panel).
- Edge headless: `pdf.sh`/`maquetas.sh` fallan si el perfil compartido está bloqueado; usar un perfil nuevo por llamada y esperar a que aparezca el archivo (Edge devuelve el control antes de terminar).

## Estados en prospectos.csv
`investigado` → `borrador` → `enviado` → `respondio` / `no_contactar` / `descartado_sin_correo`

## Próximo paso
Revisar respuestas; a quien diga que sí, responder en el mismo hilo con el PDF y las 3 imágenes de su carpeta.

## Propuestas enviadas (actualizado 4-nov)
- **B-Zeta Ingeniería** (Clodomiro Aravena): informe + propuesta PDF por correo en el mismo hilo, 3-nov 16:52. Renovación de web existente $249.990. Seguimiento único por correo el vie 6 si no responde.
- **La Ritoqueña** (Diego Arenas): informe + propuesta PDF por WhatsApp, 3-nov 15:47. Renovación de web existente $249.990. Seguimiento único por WhatsApp el vie 6 si no responde.
- Tablero: ambas en etapa "Propuesta enviada", valor $249.990, próximo paso al 6-nov. prospectos.csv ya decía "propuesta enviada"; tabla_comercial.csv actualizada (B-Zeta no está en esa tabla, es del lote Codex).
- **Biosfera Lodge** (Juan Pablo Vásquez): informe + propuesta PDF por correo en el mismo hilo, 4-nov. Página de entrada conectada a GoFeels, $249.990. Tablero en "Propuesta enviada"; seguimiento único por correo el vie 7 si no responde.

## Repaso general (5-nov, mediodía)
- Primeros correos enviados: 2-nov 11 · 3-nov 20 · 4-nov 20 · 5-nov 30 (29 a las 11:49 + Los Troncos a las 11:59) ≈ 81. Incluye los 11 rescatados (Delta Dent, Oceánica, Rialto, AM Modular, La Jovita, Marglass, Reñaca Roller, Roller Solutions, Petreos, Opendeco, Hostería Montemar), reescritos y enviados el 5-nov.
- Rebotes (dirección no existe): Canemar, Consultora Tax, Reñaca Roller, Gala Hotel, Medikin, Campo y Playa.
- Interesados: B-Zeta, La Ritoqueña y Biosfera Lodge (las 3 con informe + propuesta, $249.990 c/u). Rechazos: Sastrería García Vellella (ya renuevan su web; contestado) y Ambientemar (dijo que no por WhatsApp; excluido).
- **Viernes 6: de 20 aprobados, solo 6 están programados en Gmail** (Vitaplace, Valhalla, Punta del Este, La Cocina de Teuh, Atkinson, Espacio Mediterráneo). Los otros 14 están en Borradores con fecha del 6-nov: Oral Clinic, Más Salud, Fisiosalud, StockPro, Auramed, Bellavi, Taller Torres, Adelma, Regina, Maison de la Mer, Bote Salvavidas, Domus Mare, Chanagua, New Voga. No se sabe quién los canceló.
- Tablero actualizado: estado real de cada correo del 4, 5 y 6-nov en la pestaña Correos; Canemar y Reñaca Roller en "Perdido" por rebote.
- Ojo: prospectos.csv quedó desactualizado (94 aún dicen "programado"); la fuente al día es el tablero.
