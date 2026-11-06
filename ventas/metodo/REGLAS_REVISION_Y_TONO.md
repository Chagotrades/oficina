# Reglas de revisión y tono: obligatorias para todo mensaje a una empresa

Acordadas por Santiago y Mathias el 6-nov-2026 después del caso **Cabañas Piedra Blanca** (El Quisco). El informe que le enviamos decía "No tiene una web propia", y sí tenía. Además, presentaba como "problemas que le hacen perder reservas" decisiones que el dueño había tomado a propósito: no publicar precios y no responder las reseñas. El dueño lo tomó como una ofensa y nos dijo, con razón, que no habíamos leído bien.

Estas reglas mandan sobre cualquier otro archivo de `ventas/`. Valen para correos, WhatsApp, informes PDF, propuestas y cualquier texto que vaya a leer una empresa, lo prepare el Claude de Santiago o el de Mathias.

## Regla 0 · Solo empresas con problemas EVIDENTES, sin rebuscar

**Solo se le escribe a una empresa con un problema evidente**: algo que cualquiera nota en segundos al buscarla, sin ser técnico. Por ejemplo: no tiene web, su web no abre, muestra un error, tiene "cuenta suspendida" o un aviso de mantención, el enlace lleva a otro sitio, o en el celular no se puede usar.

**No se rebusca.** Medir anchos en píxeles, contar botones que faltan, revisar el año del pie de página, "poco texto" o "sin formulario" no son motivos para escribirle a nadie. Si para encontrar el problema hubo que buscarlo con lupa, la empresa no entra al lote. Más vale un lote chico con problemas claros que uno grande con detalles discutibles.

Si al revisar un lote ya preparado (incluso con correos o WhatsApp programados) una empresa no tiene un problema evidente, **se descarta sin consultar**: se cancela su envío, se borra su borrador y queda `descartado_sin_problema_evidente` en `registro/prospectos.csv`.

## Regla 1 · Prohibido contactar sin revisión completa

**ESTÁ PROHIBIDO seleccionar una empresa para un mensaje real (correo, WhatsApp, informe o propuesta) sin una revisión completa de su presencia en internet, hecha el mismo día o el anterior.** Sin revisión completa, la empresa no entra al lote. No hay excepciones por apuro ni por cuota diaria.

La revisión completa tiene **todas** estas partes:

1. **Ficha de Google Maps** (según [VERIFICAR_EN_MAPS.md](VERIFICAR_EN_MAPS.md)): negocio correcto, abierto, nota, reseñas, botón de web, menú, reservas y redes.
2. **Búsqueda en Google** (no solo en Maps), con al menos estas búsquedas:
   - el nombre del negocio y la comuna (`cabañas piedra blanca el quisco`);
   - el nombre solo, entre comillas;
   - el nombre con "sitio web" o "web".
   Revisar la primera página completa de resultados: web propia, Instagram, Facebook, Booking, Airbnb, directorios y notas de prensa.
3. **Probar dominios probables escribiéndolos a mano**: `nombre.cl`, `nombre.com`, con y sin ñ (`cabañas` → `cabanas`), con y sin guiones, con y sin el rubro. Las direcciones con ñ casi nunca aparecen bien en los buscadores.
   Para dominios con ñ, sacar la forma real con `python -c "print('nombreconñ.cl'.encode('idna'))"`, no inventarla (con Don Pepe se probó mal y por eso no apareció).
4. **Redes sociales**: la biografía de Instagram y Facebook (web, Linktree, WhatsApp, precios, carta). **Abrir el enlace de la biografía**: es la forma más segura de saber si tienen web (Don Pepe, 6-nov: el enlace de Instagram era su web).
5. **Si tiene web**: abrirla en celular y en computador, recorrer las secciones principales y leer lo que dice antes de opinar sobre ella.
6. **Fuentes oficiales** si corresponde (Sernatur para turismo).

**Que Maps diga "Añadir sitio web" NO significa que la empresa no tenga web.** Solo significa que no la enlazó en su ficha. Esa fue exactamente la falla con Piedra Blanca.

**Toda la revisión se anota** en `verificacion.md` dentro del lote: por empresa, qué se buscó, qué se encontró (con la dirección web), la fecha y la decisión (se mantiene / se corrige / se saca). Si una parte no se pudo hacer (Google pidió verificación anti-robots, Maps no cargó), la empresa queda **pendiente** y no se le escribe.

## Regla 2 · Solo afirmar lo que se vio

- Cada afirmación del mensaje tiene que estar respaldada por algo que quedó anotado en `verificacion.md`.
- Las afirmaciones de ausencia ("no tiene web", "no tiene carta", "no aparece", "ninguna reseña tiene respuesta") son las más peligrosas: **solo se escriben si las seis partes de la revisión las confirman**, y aun así conviene describir lo que se vio en vez de afirmar la ausencia. Por ejemplo: "su ficha de Google todavía no enlaza su web", no "no tiene web".
- Nada de "Revisamos todo" ni "Revisamos su presencia en Google" si no se hizo la revisión completa.

## Regla 3 · Sugerir, no criticar

El dueño conoce su negocio mejor que nosotros. Muchas cosas que parecen fallas son decisiones suyas.

- **Las decisiones del dueño no son problemas.** No publicar precios, no responder reseñas, no aceptar mascotas, atender solo por teléfono o no tener redes son decisiones válidas. Se pueden mencionar solo como **opción**, con su motivo y dejando claro que es su decisión: "Si en algún momento quiere mostrar un valor 'desde', se puede agregar".
- **Títulos y etiquetas en clave de oportunidad.** En informes y propuestas:
  - "Lo que podría sumar", no "Lo que hoy le hace perder reservas".
  - "Oportunidad 1", no "Problema 1".
  - "Lo que podría ayudar", no "Le cuesta reservas".
  - "Qué vimos", no "Qué pasa hoy" cuando suena a acusación.
- **Sin absolutos ni culpas**: nada de "ninguna", "nadie", "no hay dónde", "le hace perder", "le cuesta clientes" si no lo podemos demostrar. No hablamos de pérdidas que no medimos.
- **Siempre partir por lo que hace bien**, con datos concretos (nota, reseñas, años, lo que destacan sus clientes). Esto ya era regla para el primer mensaje; ahora vale también para cada sección del informe.
- **Lo que ya tiene se reconoce.** Si tiene web, se nombra y se valora antes de sugerir algo: "Su web cabañaspiedrablanca.cl muestra las cabañas y el contacto. Lo que sugerimos es enlazarla en su ficha de Google, para que quien lo encuentra en Maps llegue a ella en un toque".
- **La oferta cambia si la revisión cambia.** Si ya tiene web, no se ofrece "web nueva" como si no existiera. Se busca qué podría mejorar de verdad (por ejemplo, que la web no esté enlazada en Maps, que no abra bien en el celular o que no tenga botón de WhatsApp). Si no hay nada concreto del tarifario que ofrecer, la empresa se saca del lote.

## Regla 4 · Prueba del dueño antes de enviar

Antes de entregar un lote o un PDF al socio, Claude relee cada texto como si fuera el dueño y se responde:

1. ¿Hay algo que el dueño pueda probar que es falso? (Si sí: se corrige o se saca).
2. ¿Hay algo que pueda leer como crítica a una decisión suya? (Si sí: se reescribe como opción o se quita).
3. ¿Se reconoce lo que ya tiene, incluida su web si la tiene?
4. ¿La revisión completa (Regla 1) está anotada para esta empresa?

En el resumen para el socio, Claude dice qué partes de la revisión no pudo hacer. Un socio aprueba recién después de eso.

## Regla 5 · Si un cliente se molesta

- Agradecer, reconocer el error concreto sin excusas ("Tiene razón: no vimos su web cabañaspiedrablanca.cl, fue un error nuestro") y no discutir su lectura del informe.
- No explicar que "era una sugerencia" ni citar "estudios de posicionamiento": suena a justificación.
- Ofrecer corregir el informe solo si él lo quiere. Si no, cerrar con amabilidad y no volver a escribirle salvo que él retome.
- Anotar el caso en `registro/prospectos.csv` y en `APRENDIZAJES.md`.

## Caso de referencia: Cabañas Piedra Blanca (6-nov-2026)

| Lo que dijo el informe | Lo que era en realidad | Cómo debió decirse |
|---|---|---|
| "No tiene una web propia" ("Añadir sitio web" en Maps) | Tiene web propia. Solo no estaba enlazada en Maps. | "Su web todavía no está enlazada en su ficha de Google. Enlazarla toma minutos y lleva a quien lo encuentra en Maps directo a sus cabañas". |
| "En Google no aparece ningún precio" como problema | El dueño decidió no publicar precios. | Una opción: "Si algún día quiere mostrar un valor 'desde', se puede; si prefiere conversarlo por teléfono, también funciona". |
| "Ninguna opinión tiene respuesta" como problema de confianza | Decisión del dueño. Tiene 95% de buenas opiniones. | Destacar sus opiniones. Responderlas se menciona, como mucho, como algo opcional. |
| "Lo que hoy le hace perder reservas" | No medimos ninguna pérdida. | "Lo que podría sumar". |
