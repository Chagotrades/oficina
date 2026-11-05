# Ascensus — rutina diaria de correos (formato acordado 3-nov-2026)

Mathias trae cada día un archivo de Codex con prospectos A y sus correos ya redactados
(ej.: `E:\Trasladado_desde_C\Documentos\ChatGPT\FARO\Prospectos_A_TARIFARIO_para_Claude_AAAA-MM-DD.txt`).
Basta con decir: **"programa los A de hoy: <ruta> entre <hora> y <hora>"**. No hace falta volver a explicar el contexto.
Ese pedido, con archivo y horario, cuenta como aprobación del lote.

## Lo que hace Claude, en orden
1. Leer ESTADO.md (sección de la última campaña) y el archivo de Codex. Solo la tabla y los bloques ASUNTO/CUERPO; las fichas internas no se copian.
2. Cruzar cada empresa (nombre, dominio, marcas relacionadas que indique el archivo) con `prospectos.csv`, `tabla_comercial.csv`, `lotes/` y Gmail (enviados, borradores y programados). Sacar duplicados y `no_contactar`.
3. Crear un borrador por empresa con el conector de Gmail, texto plano: asunto, cuerpo, firma y línea de baja tal cual vienen. Sin dominios escritos en el cuerpo (el conector los convierte en enlaces de google.com).
4. Programar en Gmail web (navegador integrado): abrir borrador → flecha junto a Enviar → Programar envío → Elegir fecha y hora. Repartir en la ventana pedida, intercalados con lo que ya esté programado ese día. No dejar Gmail web abierto en un borrador mientras se edita por el conector. Antes de escribir la hora, confirmar que el diálogo "Elegir fecha y hora" está abierto (las capturas llegan atrasadas; si el diálogo no abrió, la hora se escribe en el cuerpo del correo).
5. Verificar el contador de **Programados** y registrar en `prospectos.csv` (estado `programado`, fecha, hora, id) y en ESTADO.md.
6. Entregar el reporte (formato abajo).

## Reglas
- Un solo correo por empresa, nunca seguimientos. Ver [CLAUDE.md](CLAUDE.md).
- Volumen recomendado: 15–20 por día desde Gmail personal. Si el pedido lo supera, avisar una vez; Mathias decide.
- Si el archivo dice "no enviar", "pendiente" o falta un dato bloqueante, no se programa.

## Reporte diario (corto)
- Tabla: hora · empresa · correo.
- Excluidos y por qué (duplicado, ya contactado, pendiente).
- Total programado hoy y conteo verificado en Gmail.
- Respuestas nuevas desde el último reporte y qué contestar: sí → diagnóstico en 48 h; pide hablar → 15 min por WhatsApp; no → "Gracias, no le volveré a escribir" y `no_contactar`.
