# Verificar cada prospecto en Google Maps antes de enviar

Paso obligatorio desde el 6-nov-2026, después de que un mensaje dijera "no encontré una web con su carta" y La Choca sí tenía menú en Google Maps. **Ningún lote (correo o WhatsApp) se entrega al socio sin pasar por aquí.**

> Desde el 6-nov (caso Piedra Blanca), Maps es **una parte** de la revisión completa, no toda. Además hay que buscar en Google, probar dominios probables a mano y revisar redes y web: ver [REGLAS_REVISION_Y_TONO.md](REGLAS_REVISION_Y_TONO.md). Que la ficha diga "Añadir sitio web" no significa que no tenga web.

## Quién lo hace y dónde
- Lo hace **Claude en el computador de un socio**, con la app Claude Desktop abierta en la carpeta de la oficina y la extensión **Claude in Chrome**, porque Google Maps no le muestra los datos a un navegador automático en la nube. No se fuerza la protección anti-bots de Google.
- El socio solo tiene que pedirlo (frase de abajo) y aprobar el resultado. No tiene que revisar nada a mano.

## Frase para pedirlo
> Verifica en Google Maps el lote `ventas/lotes/<carpeta-del-lote>/` siguiendo `ventas/metodo/VERIFICAR_EN_MAPS.md`.

## Qué revisa Claude en cada negocio (en la ficha de Google Maps, con Chrome)
1. **Que sea el negocio correcto:** nombre, dirección y teléfono coinciden con el lote. Si el teléfono de Maps es otro, usar el de Maps y anotarlo.
2. **Si sigue abierto:** "Cerrado permanentemente" o "temporalmente" → se saca del lote.
3. **Nota y cantidad de reseñas** (anotar los números exactos y la fecha).
4. **Web:** si la ficha tiene botón "Sitio web", abrirlo. Si tiene web que funciona, el mensaje no puede decir que no tiene. **Si la ficha dice "Añadir sitio web", igual buscar en Google y probar dominios a mano** (con y sin ñ): Piedra Blanca tenía web y no estaba enlazada.
5. **Menú o carta:** si la ficha tiene "Menú" (enlace o fotos de carta), el mensaje no puede decir que no tiene carta.
6. **Reservas y pedidos:** si tiene botón de reservar o pedir.
7. **Redes:** Instagram o Facebook enlazados (y si su biografía tiene web o Linktree).
8. **Qué destacan las reseñas** (dos o tres cosas concretas) para el enganche positivo.

## Qué hace con lo que encuentra
- **Reescribe cada mensaje** usando solo lo que vio en Maps y en su web o Instagram. Cada afirmación del mensaje ("tiene 4,6 con 197 reseñas", "no tiene web", "su carta es una foto") tiene que haberse visto ese día.
- **Cambia el servicio ofrecido si corresponde:** si ya tiene web y carta, no se ofrece "web lista"; buscar un problema real (web lenta o rota en celular, sin botón de reservar, carta en foto que Google no lee, pocas reseñas…). Si no hay oferta concreta del tarifario, **se saca del lote** (regla del 3-nov).
- **Anota por negocio**, en un archivo `verificacion_maps.md` dentro del lote: qué vio, con fecha, y si se mantiene, se corrige o se saca.
- **Actualiza** la página de WhatsApp del lote (o los correos), `filas_para_prospectos.csv` o `registro/prospectos.csv`, y la guía del lote; quita el aviso "EN REVISIÓN" solo cuando todos estén verificados.
- Si hay una página publicada en claude.ai para el lote, la vuelve a publicar en la misma dirección.

## Al terminar
Resumen corto para el socio: cuántos quedaron, cuántos se corrigieron, cuántos se sacaron y por qué. El socio aprueba y recién ahí se envía.
