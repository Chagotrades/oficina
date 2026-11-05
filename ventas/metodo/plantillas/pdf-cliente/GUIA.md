# Informe + propuesta en PDF (cuando un prospecto responde con interés)

Formato aprobado por Mathias el 3-nov-2026 con La Ritoqueña (se los envió por WhatsApp). Ejemplo completo, listo para copiar y adaptar: `lotes/2026-11-03-la-ritoquena/` (carpetas `maquetas/`, `pdf/`, `capturas/`, `fotos/`).

Se entregan **dos PDF A4 separados**: primero el informe y luego la propuesta. Sin "Valores en pesos chilenos / boleta de honorarios" (Mathias lo pidió quitar).

## 1. Estética del cliente
- Sacar de su web, con el navegador: colores de fondo y de texto, fuentes, logo (versión clara y oscura) y fotos (`getComputedStyle`, URLs de `wp-content/uploads`, etc.).
- Descargar las fotos en `fotos/`, hacer versiones livianas en `fotos/web/` (Pillow, 1400 px, calidad 78) y una hoja de contactos para elegir cuáles usar.
- Usar los colores, fuentes y logo del cliente en los PDF y en las maquetas. La marca Ascensus solo va en la portada ("Preparado por") y en el pie.

## 2. Informe (≈7 páginas) — `pdf/informe.html`
1. Portada: foto grande del lugar con su logo, título que habla del huésped o cliente, fecha y "Preparado para <nombre>".
2. "En una página": lo que ya tiene a favor y la lista de problemas con una etiqueta (Reservas / Visitas / Confianza).
3. Una página por problema: **Qué pasa hoy → En qué le afecta → Cómo lo resolvemos**, con una captura real en un marco de celular.
4. Cierre: "Todo esto tiene arreglo", una frase de que puede hacerlo por su cuenta, contacto WhatsApp y una nota de cómo se revisó.
- Solo datos verificados el mismo día. Lo que no se pudo comprobar, se quita. Capturas en tamaño celular con el navegador integrado (`resize_window` mobile); guardarlas en `capturas/` como `error-N-descripcion.jpg`.

## 3. Propuesta (≈6 páginas) — `pdf/propuesta.html`
1. Portada con otra foto del cliente.
2. Plan recomendado del TARIFARIO.md con su precio, la lista de lo que incluye unida a cada problema del informe, el pago 50/50 en montos, el plazo y los 15 días de cambios.
3. Maquetas en celular (2 grandes por página) y en computador, hechas con sus fotos y con el sello "Imagen de referencia, no es una web publicada".
4. Garantías de CONTEXTO.md.
5. Asistente (opcional): 2 conversaciones de ejemplo (una responde y la otra deriva a WhatsApp con el mensaje escrito) y las dos opciones de precio del tarifario. No mostrar disponibilidad inventada.
6. Otros servicios (Google Maps, mantención, anuncios), "Cómo empezamos" en 3 pasos y contacto.

## 4. Generar y revisar
```bash
bash plantillas/pdf-cliente/maquetas.sh "<lote>/maquetas"      # PNG de cada maqueta
bash plantillas/pdf-cliente/pdf.sh "<lote>/pdf" informe 7       # PDF + informe-hoja.png
bash plantillas/pdf-cliente/pdf.sh "<lote>/pdf" propuesta 6
```
- `doc.css` (aquí) tiene la base A4; copiarlo a `<lote>/pdf/` y cambiar las variables de color en `:root` por los del cliente.
- Para que el PDF pese poco: pasar las maquetas a JPG y recortarlas al teléfono. La Ritoqueña quedó en 1,1 MB y 2 MB.
- Mirar la `-hoja.png` de cada PDF: nada debe pisar el pie ni quedar muy chico. Repetir hasta que se vea bien.
- Copiar los PDF finales al escritorio con nombres `<Cliente>-Informe.pdf` y `<Cliente>-Propuesta.pdf`, sin sobrescribir otros archivos.

## 5. Antes de entregar
- Confirmar con Mathias lo que el tarifario no detalla (qué incluye la mantención, si el precio del asistente es total, etc.).
- Mathias envía los PDF él mismo. Registrar el envío en **los dos lugares** (el tablero no lee el CSV):
  - `prospectos.csv`: estado `propuesta enviada`.
  - Tablero (https://claude.ai/artifact/H8ocFj8fHuVTHwbxDByB4Y), colección `prospectos`, documento del cliente: `etapa: "propuesta"`, `notas` con qué se envió y cuándo, `proximo` (seguimiento) y `proximoFecha` (2–3 días después), `actualizado`.
- Después de enviar: esperar la respuesta. Si pasan 2–3 días, un solo mensaje corto ofreciendo 15 minutos.
