# Lista de calidad

Se pasa antes de decir "listo" y otra vez, por alguien que no hizo el trabajo, antes de que el cliente lo vea. Al informar, decir explícitamente qué no se pudo comprobar.

## Todo entregable
- [ ] Hace lo que pedía el encargo, ni más ni menos.
- [ ] No hay precios, plazos ni datos del cliente inventados. Lo no confirmado dice "de ejemplo" o "por confirmar".
- [ ] El ESTADO.md del cliente quedó actualizado.

## Web, landing o demo
- [ ] Se ve bien en celular (320, 375 y 390 px) y en computador (1440 px), sin desplazamiento hacia el lado.
- [ ] Nada se monta encima de otra cosa ni se sale de su caja (revisar varios anchos, no uno).
- [ ] Sin errores en la consola.
- [ ] Botones, formularios, cotizador y asistente funcionan con casos reales y con casos raros (números a la chilena, campos vacíos, respuestas sueltas).
- [ ] Si hay movimiento: no se traba con el procesador frenado 4× (`medir_fps.py` o `sonda3d.mjs`) y respeta a quien desactivó las animaciones. Una animación nunca puede dejar algo sin verse.
- [ ] Peso razonable al abrir en 4G (medido, no supuesto).
- [ ] Ningún contacto, canal o pago conectado sin aprobación.

## Asistente o chatbot
- [ ] No inventa respuestas comerciales: lo que no sabe lo deriva al equipo.
- [ ] No se queda pegado repitiendo la misma pregunta.
- [ ] Sus pruebas automáticas pasan completas.

## Textos para el cliente (propuesta, mensaje, post)
- [ ] Suena a persona, no a IA (`humanizador`).
- [ ] Las afirmaciones son ciertas (`verificador-datos`).
- [ ] Precios, condiciones y plazos coinciden con lo que decidió Santiago.
