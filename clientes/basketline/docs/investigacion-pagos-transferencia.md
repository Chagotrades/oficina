# Pago por transferencia directa, sin intermediarios (actualizado 30-oct-2026)

**Decisión del cliente:** nada de pasarelas (Khipu, Fintoc, Mercado Pago, Webpay). El cliente transfiere directo a la cuenta de la tienda, para no sumar reportes de terceros al SII. La automatización se construye alrededor de eso.

## Cómo se automatiza una transferencia directa
1. **Monto único por pedido ("huella"):** al total se le descuentan de $1 a $99, un valor único entre pedidos pendientes (ej. un pedido de $45.990 se cobra $45.937: se descuentan $53 que nadie más tiene pendiente). Así cada transferencia se puede identificar solo por monto. Además se pide poner el código del pedido (ej. BL-1042) en el comentario.
2. **Botón "Ya transferí" + comprobante:** el cliente sube foto/PDF del comprobante. Se lee con OCR (monto, fecha, banco de origen, nombre/RUT) y se pre-valida contra el pedido.
3. **Lectura de correos del banco (la parte más automática):** los bancos chilenos mandan un correo por cada transferencia recibida ("Has recibido una transferencia de…" con monto, nombre, RUT y comentario). El sistema lee esa casilla (IMAP o reenvío a un webhook de correo entrante), extrae los datos con un parser por banco y marca el pedido como pagado si coincide monto + código/RUT. Sin intermediario: es la notificación del propio banco.
4. **Conciliación por cartola:** respaldo diario. El admin sube la cartola (Excel/CSV) y el sistema cruza cada abono con los pedidos pendientes, mostrando coincidencias seguras, dudosas y abonos sin pedido.
5. **Aprobación manual con un clic** para lo que quede dudoso.
6. **Expiración:** pedidos sin pago en X horas liberan el stock reservado.

