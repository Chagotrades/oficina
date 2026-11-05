# Ventas y prospección

Aquí se busca y se contacta a posibles clientes de Ascensus. Lo puede trabajar cualquiera de los dos socios.

## Antes de contactar a una empresa
1. Corre `sincronizar.ps1` (desde la carpeta de la oficina) para tener el tablero al día.
2. Busca la empresa en `PROSPECTOS.md`.
   - **Si ya está:** la lleva quien figura como responsable. No la contactes por tu cuenta; si quieres tomarla, se habla y se anota el traspaso.
   - **Si no está:** agrégala con tu nombre como responsable, corre `sincronizar.ps1` y recién ahí contáctala.
3. Después de cada contacto, actualiza la fila: estado, último contacto y próximo paso.

## Correos y mensajes
- Claude los redacta; **un socio los aprueba antes de enviarlos**. La aprobación vale para ese envío.
- Personalizados para cada empresa (qué vimos de su negocio, qué les podemos mejorar). Nada de envíos masivos iguales.
- Pasa los textos por la skill `humanizador`.
- Cada primer correo termina con una salida simple: "Si no te interesa, respóndeme y no te vuelvo a escribir". Si alguien la usa, su fila queda en "no contactar" para siempre.
- No se compran ni se descargan listas de contactos. Solo datos públicos del negocio (su web, su Instagram, Google Maps) y lo que la persona nos dio.
- Guarda solo lo necesario de cada contacto: nombre, cargo, correo o teléfono del negocio. Nada personal.

## Cuando un prospecto dice que sí
Se crea su carpeta de cliente con `nuevo-cliente.ps1`, se marca "cliente" en `PROSPECTOS.md` y desde ahí se sigue en `clientes/<cliente>/`.

## Qué hay aquí
| | |
|---|---|
| `PROSPECTOS.md` | Tablero de prospectos: quién es, quién lo lleva, en qué va. |
| `plantillas/` | Correos y mensajes que funcionaron, para reutilizar. Un archivo por plantilla. |
