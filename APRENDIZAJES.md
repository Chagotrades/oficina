# Aprendizajes de la oficina

Lo que aprendimos con un cliente y sirve para todos. Una línea por aprendizaje, con el cliente de origen. Lo que es solo de un cliente va en su ESTADO.md.

## Web
- Publicar como carpeta con las imágenes aparte, no como un solo HTML: en celular con 4G pasó de 5,8 MB y 27 s a 800 KB y 4,3 s. (Campo Verde)
- Hacer versiones de ~900 px de las fotos para celular (`srcset`/`<picture>`): la portada bajó de 327 KB a 110 KB. (Campo Verde)
- Un titular que se escribe solo reserva el alto de su frase más larga: si una frase ocupa 2 líneas, queda un hueco con todas. Medir todas las frases en varios anchos. (Campo Verde)
- Si una foto se desplaza al hacer scroll, tiene que estar agrandada lo suficiente para cubrir ese desplazamiento, o quedan huecos en el borde. (Campo Verde)
- Algunas vistas previas (por ejemplo, abrir el archivo dentro de la app de Claude) bloquean el envío de formularios: los botones de enviar no deben depender de eso. (Campo Verde)
- En un diagnóstico, abrir de verdad los botones de reserva o compra: pueden traer fechas fijas ya vencidas y mostrar un error (laritoquena.com llevaba a julio 2024). (La Ritoqueña)

## Asistentes y chatbots
- Leer los números a la chilena: "1.000" es mil. (Campo Verde)
- Un teléfono de 8 o más dígitos no es una superficie, y "sábado 15" no son 15 m². (Campo Verde)
- La gente escribe abreviado ("wsp", "cto", "ppto", "q"): normalizar antes de interpretar. (Campo Verde)
- Respuestas sueltas como "no", "ok" o "nada" necesitan su propia respuesta; si no, el bot se queda pegado. (Campo Verde)

## Alojamiento
- Netlify gratis funciona por créditos: si se agotan, pausa todos los sitios de la cuenta. Vercel Hobby no permite uso comercial. Para sitios estáticos de clientes, Cloudflare Pages con una cuenta a nombre del dueño. (Campo Verde)

## Herramientas
- Videos sin ffmpeg: Edge sin ventana + MediaRecorder graba MP4 directo desde un canvas. (Campo Verde)
- Leer un aviso de transferencia del banco no basta: hay que aceptar solo el banco de la tienda, exigir la cuenta de destino completa y desconfiar si el comentario del que paga trae etiquetas ("Cuenta", "Monto"); lo dudoso, a revisión. (Basketline)
- Si la demo usa la misma base que la versión publicada, cada prueba deja datos y mueve stock reales: marcarlos PRUEBA, tener un script que devuelva el stock y borrarlos al terminar. (Basketline)

## Prospección
- Nunca decir en un mensaje que un negocio "no tiene web" o "no tiene carta" sin haberlo visto en su ficha de Google Maps: Sernatur y los buscadores no bastan (La Choca sí tenía menú en Maps). Si no se pudo ver Maps, no se escribe ese hecho. (Lote WhatsApp 6-nov)
- Maps no basta: "Añadir sitio web" en la ficha no significa que no tenga web. Buscar en Google y probar dominios a mano (con y sin ñ) antes de afirmarlo. Y no presentar como problema lo que el dueño decidió (no publicar precios, no responder reseñas): el dueño de Piedra Blanca se ofendió con el informe. (Cabañas Piedra Blanca, 6-nov)
