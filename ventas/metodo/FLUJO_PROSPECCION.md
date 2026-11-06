# Ascensus — flujo de prospección

Pedido tipo: "Busca 10 [rubro] en [comuna] y prepara el lote".
Claude hace los pasos 1 a 5 y se detiene. El paso 6 solo ocurre con aprobación en el chat.

> **Antes de todo:** [REGLAS_REVISION_Y_TONO.md](REGLAS_REVISION_Y_TONO.md). Prohibido seleccionar una empresa sin revisión completa (Maps + Google + dominios probables + redes + su web). Ese archivo manda sobre este.

## 1. Buscar prospectos — skill `lead-research-assistant`
- Fuentes gratis: Google Maps y búsqueda web con el navegador del panel (búsquedas a mano, sin descargas masivas), OpenStreetMap, Instagram público.
- Filtro "señal de necesidad" (al menos una), **confirmada con la revisión completa**: sin web (nunca deducido solo de Maps), web rota o vieja, sin botón de WhatsApp, perfil de Google sin fotos/horario, pocas reseñas o reseñas sin responder, vende por Instagram con pedidos a mano.
- Requisito para el correo: el negocio publica su correo de contacto (web, perfil de Google o Instagram). Si no hay correo público, se anota como "solo WhatsApp/llamada" y no se le escribe.
- Revisar prospectos.csv: si ya fue contactado o pidió no recibir más, se descarta.

## 2. Diagnóstico gratis — skills `auditoria-web` (si tiene web), `cro`, `verificador-datos`
- Ver web, Maps y redes como un cliente desde el celular. Comparar con 3 competidores de la comuna (qué tienen ellos que este negocio no).
- **Revisión en celular obligatoria para todas las empresas** (pedido de Mathias, 2-nov): navegador integrado con `resize_window` preset mobile (375×812). Registrar en `revision_movil` de la tabla: configuración móvil, ancho real (si supera 375 px hay desborde o vista de computador), texto menor a 12 px, botones menores a 24 px, WhatsApp y teléfono para tocar, y qué se ve en la primera pantalla. Esperar al menos 9 s antes de concluir que algo "queda en blanco" y anotar que es emulación, no un teléfono real.
- Completar [plantillas/diagnostico.md](plantillas/diagnostico.md): 3 arreglos prioritarios, cada uno con lo observado (dato verificable), por qué le cuesta clientes y qué hacer.
- Solo hechos comprobados. Nada inventado sobre ventas o visitas.
- Las decisiones del dueño (no publicar precios, no responder reseñas, etc.) no son fallas: se mencionan solo como opción. Ver Regla 3 de [REGLAS_REVISION_Y_TONO.md](REGLAS_REVISION_Y_TONO.md).

## 3. Propuesta visual (la "demo") — skill `frontend-design`
- 3 imágenes de propuesta (portada en celular, sección de servicios/cotizador, contacto), con el nombre y rubro del negocio y la marca de agua "Propuesta Ascensus – no es una web publicada".
- Se hacen en HTML y se capturan con Edge headless. No se publica ninguna web ni se regala una demo completa.

## 4. Elegir el plan
- Usar la tabla "Cómo elegir el plan" de [TARIFARIO.md](TARIFARIO.md). Recomendar uno solo; complementos solo si el diagnóstico lo justifica.

## 5. Redactar el correo — skills `email-writing-frameworks`, `email-1-variations-7`, `personalization-hooks`, `josh-braun-copywriting`, `humanizador`
- Plantilla: [plantillas/correo.md](plantillas/correo.md). Máximo ~90 palabras en el cuerpo.
- Gancho "ligero" basado en el diagnóstico real (ej.: "busqué 'pasto en rollo Quillota' y su negocio no aparece en el mapa").
- Adjuntos: informe PDF de 1 página + 3 imágenes (o enlace si el conector no permite adjuntar).
- Guardar todo el lote en `lotes/AAAA-MM-DD-rubro-comuna/` (informes, imágenes y textos).

## 6. Enviar — conector Gmail (solo con aprobación)
- Claude muestra el lote: tabla con negocio, correo, asunto y cuerpo. Mathias responde "aprobado" (o corrige). Sin eso no sale nada.
- Preferir crear borradores en Gmail; enviar solo si Mathias lo pide para ese lote.
- Volumen: máximo 15–20 correos al día desde Gmail personal, para no dañar la reputación de la cuenta.
- Un solo correo por negocio. Sin seguimientos automáticos.
- Registrar cada envío en prospectos.csv (fecha, estado).

## Requisitos legales (Chile)
- Ley 19.496, art. 28 B: toda comunicación promocional por correo debe indicar quién la envía, el asunto y una forma simple de pedir que no se envíen más. La plantilla ya lo incluye; nunca quitarlo.
- Ley 21.719 de datos personales (rige desde diciembre 2026): usar solo datos de contacto que el negocio publica para fines comerciales, no guardar datos personales innecesarios y borrar al que lo pida.
- Asunto honesto: nada de "RE:" falsos ni urgencias inventadas.

## Si responden
- Interesado: preparar **informe + propuesta en dos PDF** con la estética del cliente, según [plantillas/pdf-cliente/GUIA.md](plantillas/pdf-cliente/GUIA.md) (ejemplo: La Ritoqueña). Después, proponer una llamada o WhatsApp de 15 minutos; para objeciones, skill `cold-call-scripts` (incluye respuestas a objeciones).
- "No me interesa" o "no me escriban": responder agradeciendo (con aprobación), marcar `no_contactar` en prospectos.csv.
