# La Ritoqueña

Prospecto. Hotel de playa con 6 habitaciones en Ritoque (Quintero, región de Valparaíso); reservas por Cloudbeds y WhatsApp, web en WordPress (laritoquena.com). Le hicimos un diagnóstico de su web para ofrecerle mejorarla.

## Leer al retomar
- ESTADO.md: estado resumido y próximo paso.
- INFORME.md: el diagnóstico de la web (la versión para compartir es una página de Claude, link en ESTADO.md).
- PREGUNTAS_CLIENTE.md: lo que el cliente aprobó, lo que no quiere y lo que falta preguntarle. Consultar antes de cambiar algo que él haya definido.

## Límites
- Todavía no es cliente: no tenemos acceso a su web ni a sus cuentas. Solo se mira como visitante (no enviar formularios ni hacer reservas).
- No publicar ni conectar WhatsApp, correo, pagos o atención humana sin autorización de Santiago.
- No inventar precios, plazos ni respuestas comerciales: lo no confirmado dice "de ejemplo" o "por confirmar".

## Cómo se prueba
- Mediciones: `node diagnostico/medir.mjs <url> movil|pc <salida>` (Edge sin pantalla; en celular simula 4G lenta y CPU 4x; `--sin-freno` lo quita). Guarda JSON y capturas.
