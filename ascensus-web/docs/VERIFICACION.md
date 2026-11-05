# Verificación — 5 de noviembre de 2026

## Comprobación funcional y visual

Edge/Chromium instalado, automatizado con Playwright del runtime disponible. No se agregaron paquetes al proyecto. La vista previa integrada no respondió; la revisión se realizó con el navegador local instalado y capturas.

| Prueba | Resultado |
|---|---|
| Anchos 320, 375, 390, 640, 768, 1024, 1440 px | Sin overflow horizontal ni botones de miniaturas recortados. |
| Imágenes, enlaces internos, consola y HTTP | Sin imágenes rotas, anclas inexistentes, errores de JavaScript ni HTTP fallidos. |
| Filtros | Todos 6, Turismo 1, Servicios 3, Gastronomía 1, Salud 1. |
| Demos | Las seis abren, cambian a ancho móvil, navegan al detalle y cierran con Escape. |
| Contacto desde demo | Conserva el nombre de la propuesta en el mensaje editable. |
| Formulario | Rechaza campos vacíos o solo espacios; permite revisar y editar antes de continuar. |
| Inyección | Las etiquetas de script permanecen como texto; no se ejecutan ni se crean nodos. |
| WhatsApp | URL con destino comercial verificado y texto codificado. No se siguió el enlace ni se envió mensaje. |
| Menú móvil | Abre, actualiza estado accesible y se cierra al navegar. |
| Movimiento reducido | Desactiva transiciones y desplazamiento suave. |
| Sintaxis | `node --check app.js` y `node --check server.mjs` correctos. |

Capturas: `portada.png`, `celular.png`. Resultado de automatización: `qa-report.json`.

## Peso y rendimiento

Perfil emulado en localhost, Edge: descarga de 1,6 Mbps, subida de 0,75 Mbps, latencia de 150 ms, CPU frenada 4× y caché vacía. Transferencia de la primera visita: **523.176 bytes** (aprox. 511 KiB). Primer contenido: **772 ms**. DOMContentLoaded: **744 ms**. Evento de carga: **3.122 ms**.

Son mediciones de esa ejecución, no garantías ni resultados del futuro alojamiento. La página no tiene animaciones continuas; las transiciones de interacción se desactivan al solicitar movimiento reducido. No se efectuó una medición independiente de FPS.

## Revisión independiente

Se aplicó el rol de revisión de seguridad descrito en `.claude/agents/revisor-seguridad.md` con un agente independiente, de solo lectura, distinto al constructor.

**Veredicto: LISTO para entregar el código y continuar en GitHub. Sin fallas importantes dentro del alcance.**

Comprobaciones del revisor:

- Preparar el mensaje no realiza solicitudes externas, no crea cookies ni escribe `localStorage`/`sessionStorage`.
- Contenido del usuario representado con `textContent`; caracteres del mensaje codificados en la URL de WhatsApp.
- Los usos de `innerHTML` reciben datos constantes del propio proyecto.
- Servidor de desarrollo limitado a `127.0.0.1`; intentos de salir de la carpeta devuelven 404, POST devuelve 405.
- Sin claves, servicios de pago, dependencias de producción ni envío automático.
- Demos identificadas como ficticias; no se aparenta completar reservas o compras.

Límites: no se revisó producción, HTTPS ni cabeceras del alojamiento definitivo; no se enviaron mensajes ni se comprobó entrega real; no se probó Safari/iOS ni teléfonos físicos; no se auditó cada autorización comercial de las fotos. La revisión independiente de seguridad no repitió toda la QA visual del constructor.
