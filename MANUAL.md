# Manual de la oficina

Cómo funciona Ascensus cuando un socio (Santiago o Mathias) le da un encargo a Claude.

## Los roles

| Rol | Quién | Qué hace |
|---|---|---|
| Socios | Santiago y Mathias, con los mismos permisos | Dan encargos, deciden qué quiere el cliente, aprueban antes de que el cliente vea algo, prospectan y llevan clientes. Cualquiera de los dos autoriza publicar, enviar mensajes, conectar canales y cobrar. |
| Jefe de operaciones | La sesión de Claude abierta en la carpeta de la oficina | Recibe el encargo, lo reparte, revisa lo que vuelve y le informa al CEO. Casi nunca hace el trabajo largo él mismo. |
| Trabajadores | Sesiones de Claude abiertas en `clientes/<cliente>/` | Hacen el trabajo y lo comprueban. |
| Especialistas | Subagentes en `.claude/agents/` | Los llama el trabajador para una tarea puntual. Ver la tabla "Especialistas" más abajo. |

## Cómo se mueve un encargo

1. **Recibir.** Un socio da el encargo con sus palabras. Si falta algo que solo él sabe, preguntar lo mínimo (máximo 3 preguntas). Si lo que quiere todavía no está definido, usar la skill `entrevistador-procesos`.
2. **Anotar y tomar** en `ENCARGOS.md`: fecha, cliente, encargo, socio responsable, quién lo hace, estado. Correr `sincronizar.ps1` para que el otro socio lo vea antes de empezar.
3. **Repartir.**
   - Corto (una pregunta, un dato, un cambio pequeño): se resuelve aquí mismo.
   - Trabajo de verdad: se abre una sesión en `clientes/<cliente>/` con el **brief** de abajo. Solo cuando un socio dio el encargo, nunca por iniciativa propia.
   - Cliente nuevo: con `nuevo-cliente.ps1` (ver más abajo).
   - **Un solo trabajador edita una carpeta a la vez.** Dos encargos del mismo cliente van uno después del otro; encargos de clientes distintos pueden ir en paralelo.
4. **Revisar lo que vuelve.** El informe del trabajador no es una prueba: mirar el resultado (archivos, capturas, pruebas) antes de darlo por hecho.
5. **Revisión independiente** antes de que algo llegue al cliente: la hace un subagente o una sesión que **no** construyó el trabajo, con `CALIDAD.md`. Si hay dinero, datos personales o un asistente de IA de por medio, también con la skill `auditoria-web`. El revisor informa hallazgos; no corrige. Los arregla el trabajador.
6. **Informar al socio** en palabras simples: qué quedó hecho, qué se comprobó, qué no se pudo comprobar y qué tiene que decidir él.
7. **Cerrar.** Actualizar `ENCARGOS.md` y verificar que el trabajador actualizó el ESTADO.md del cliente. Si salió algo que sirve para otros clientes, anotarlo en `APRENDIZAJES.md`.

## Brief para un trabajador

El trabajador empieza de cero: no ve la conversación de la oficina. El brief tiene que bastar por sí solo.

```
Cliente y carpeta: clientes/<cliente>/
Encargo: qué hay que hacer, en una o dos frases.
Para qué: qué tiene que lograr con el cliente.
Lo que NO se hace: lo que queda fuera o no se toca.
Terminado es: cómo se ve el resultado cuando está listo.
Comprobar: qué pruebas o mediciones demuestran que funciona.
Necesita aprobación de un socio: publicar, enviar, precios nuevos, etc.
Al terminar: pasar CALIDAD.md, actualizar ESTADO.md e informar qué se hizo, qué se comprobó y qué falta.
```

## Cliente nuevo

Desde la carpeta de la oficina:

```
powershell -ExecutionPolicy Bypass -File .\nuevo-cliente.ps1 -Nombre "Campo Verde San Pedro"
```

Crea `clientes/campo-verde-san-pedro/` desde `plantilla-cliente/`, pone el nombre y la fecha, y agrega el cliente a la tabla del CLAUDE.md y a `ENCARGOS.md`. Si la carpeta ya existe, no toca nada. Después hay que llenar la descripción y los límites del CLAUDE.md del cliente.

## Qué skill usa cada tipo de trabajo

| Trabajo | Skills |
|---|---|
| Web, landing o demo | `animaciones`, `efectos-interactivos`, `escenas-3d` (solo si aporta) |
| App o herramienta nueva desde cero | `superpowers` |
| Revisar antes de entregar o de cobrar | `auditoria-web` |
| Propuesta, presentación para el cliente | `presentaciones-visuales` o `pptx`, más `humanizador` para los textos |
| Mensajes, posts, textos de la web | `humanizador`, `verificador-datos` |
| Vender AURA-OS | `ventas-aura-os` |
| Definir un proceso o una skill nueva | `entrevistador-procesos` |
| Cerrar una tanda de trabajo | `registrar-aprendizajes` |

Las skills están instaladas para el usuario (`C:\Users\cristobal\.claude\skills\`), así que funcionan en cualquier carpeta.

## Especialistas

| Especialista | Cuándo se llama | Método | Manos | Modelo |
|---|---|---|---|---|
| `revisor-seguridad` | Al terminar una etapa que toque dinero, login o datos de clientes, y siempre antes de publicar | OWASP Top 10:2025, lógica de negocio de tiendas, Ley 21.719, skill `auditoria-web` precargada | Leer código y correr pruebas o comandos contra `localhost`. No puede editar. | opus, esfuerzo alto, memoria propia |

Cómo se crea uno nuevo: un archivo por especialista en `.claude/agents/<nombre>.md`. Ahí solo van especialistas: ningún otro archivo. Antes de crearlo se investiga el mejor método publicado del área, y después de crearlo se prueba con un caso real, comparando el resultado con y sin él.

```markdown
---
name: nombre-en-minusculas
description: Qué hace y cuándo llamarlo, en una o dos frases. Claude decide a quién llamar leyendo esto.
tools: Read, Grep, Glob, WebSearch
model: sonnet
---
Su rol, cómo trabaja, qué entrega y qué lista de CALIDAD.md pasa.
```

- **Pocos y distintos entre sí.** Si dos se parecen, Claude no sabe a cuál llamar.
- **Solo las herramientas que necesita.** Un revisor no necesita `Write` ni `Edit`: así no puede cambiar lo que revisa.
- **Un especialista no ve la conversación.** Todo lo que necesita saber va en sus instrucciones o en el encargo.

## Dos socios, una oficina

Santiago y Mathias trabajan sobre la misma oficina, cada uno desde su computador. Para no hacer lo mismo dos veces:

1. **Todo lo que se hace pasa por un tablero.** Encargos de clientes en `ENCARGOS.md`; prospectos en `ventas/PROSPECTOS.md`.
2. **Antes de empezar, se toma:** nombre del socio + "en curso" en el tablero, y `sincronizar.ps1` para que el otro lo vea. Lo que está "en curso" a nombre del otro no se toca sin hablarlo.
3. **Antes de escribirle a una empresa, se busca en `ventas/PROSPECTOS.md`.** Si ya está, la lleva quien figura como responsable. Si no está, se agrega primero y después se contacta.
4. **Un cliente o prospecto tiene un solo socio responsable a la vez.** Se puede traspasar, pero se anota en el tablero.
5. **Las decisiones que afectan a los dos** (precios, servicios nuevos, gastos) se anotan en `APRENDIZAJES.md` o en el ESTADO del cliente para que el otro las vea.

Cada computador debe tener su nombre en git (`git config --global user.name "Mathias"`): así Claude sabe con quién trabaja y quién hizo cada cambio.

## Trabajar desde otro computador o desde la nube

La oficina está guardada en GitHub, en un repositorio privado: `https://github.com/Chagotrades/oficina`. Todos los computadores trabajan sobre esa misma copia.

- **Al empezar, al tomar algo y al terminar:** corre `powershell -ExecutionPolicy Bypass -File .\sincronizar.ps1`. Baja lo último y sube lo tuyo en un paso.
- No trabajes el mismo cliente en dos computadores a la vez sin bajar antes lo último. Si no, los cambios chocan.

**Primera vez en un computador nuevo:**
1. Instala git, Node y la app de Claude.
2. En `Documentos`, ejecuta `git clone https://github.com/Chagotrades/oficina.git Oficina` y abre Claude en esa carpeta.
3. Basketline tiene su propio repositorio: `git clone https://github.com/Chagotrades/basketline.git clientes/basketline/demo` y después `npm --prefix clientes/basketline/demo install`.
4. Las claves (`.env`) no están en GitHub, a propósito. Se copian a mano con un pendrive o un gestor de contraseñas. Nunca por WhatsApp, correo ni GitHub.

**Desde el celular, sin ningún computador prendido:** en la app de Claude, sección Code, abre una sesión en la nube sobre `Chagotrades/oficina`. Trabaja sobre una copia y devuelve los cambios en una rama de GitHub, que después se junta con `main`. No tiene las claves, así que sirve para informes, documentos y código, pero no para probar Basketline con su base de datos.

**Con este computador prendido:** el control remoto (Remote Control) deja seguir desde el celular un chat que corre aquí.

## Candados técnicos

`.claude/settings.json` bloquea, para cualquier sesión dentro de la oficina, los comandos que publican o envían (Netlify, Vercel, Cloudflare, `git push`, `npm publish`) y la lectura de archivos `.env` con claves. Aunque una sesión se equivoque, no puede publicar sola: un socio lo hace o lo autoriza en el momento. Si hay que agregar otro servicio de publicación, se suma a la lista `deny`.

## Reglas que no cambian

- Nada se publica, se envía, se conecta ni se cobra sin la autorización de un socio para ese caso. Una aprobación vale para ese caso, no para los siguientes.
- No se usan servicios ni APIs de pago sin autorización.
- Los datos de un cliente no pasan a la carpeta de otro.
- No se inventan precios, plazos ni respuestas del cliente: lo no confirmado dice "de ejemplo" o "por confirmar".
- Todo lo web se prueba en celular, no solo en computador.
