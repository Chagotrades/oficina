# Manual de la oficina

Cómo funciona la empresa cuando Santiago (CEO) le da un encargo a Claude.

## Los roles

| Rol | Quién | Qué hace |
|---|---|---|
| CEO | Santiago | Da el encargo, decide qué quiere el cliente, aprueba antes de que el cliente vea algo. Prospecta, llama y lleva la relación con los clientes. Es el único que autoriza publicar, enviar mensajes, conectar canales y cobrar. |
| Jefe de operaciones | La sesión de Claude abierta en la carpeta de la oficina | Recibe el encargo, lo reparte, revisa lo que vuelve y le informa al CEO. Casi nunca hace el trabajo largo él mismo. |
| Trabajadores | Sesiones de Claude abiertas en `clientes/<cliente>/` | Hacen el trabajo y lo comprueban. |
| Especialistas | Subagentes en `.claude/agents/` | Los llama el trabajador para una tarea puntual. Ver la tabla "Especialistas" más abajo. |

## Cómo se mueve un encargo

1. **Recibir.** Santiago da el encargo con sus palabras. Si falta algo que solo él sabe, preguntar lo mínimo (máximo 3 preguntas). Si lo que quiere todavía no está definido, usar la skill `entrevistador-procesos`.
2. **Anotar** en `ENCARGOS.md`: fecha, cliente, encargo, quién lo hace, estado.
3. **Repartir.**
   - Corto (una pregunta, un dato, un cambio pequeño): se resuelve aquí mismo.
   - Trabajo de verdad: se abre una sesión en `clientes/<cliente>/` con el **brief** de abajo. Solo cuando Santiago dio el encargo, nunca por iniciativa propia.
   - Cliente nuevo: con `nuevo-cliente.ps1` (ver más abajo).
   - **Un solo trabajador edita una carpeta a la vez.** Dos encargos del mismo cliente van uno después del otro; encargos de clientes distintos pueden ir en paralelo.
4. **Revisar lo que vuelve.** El informe del trabajador no es una prueba: mirar el resultado (archivos, capturas, pruebas) antes de darlo por hecho.
5. **Revisión independiente** antes de que algo llegue al cliente: la hace un subagente o una sesión que **no** construyó el trabajo, con `CALIDAD.md`. Si hay dinero, datos personales o un asistente de IA de por medio, también con la skill `auditoria-web`. El revisor informa hallazgos; no corrige. Los arregla el trabajador.
6. **Informar al CEO** en palabras simples: qué quedó hecho, qué se comprobó, qué no se pudo comprobar y qué tiene que decidir él.
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
Necesita aprobación de Santiago: publicar, enviar, precios nuevos, etc.
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

## Candados técnicos

`.claude/settings.json` bloquea, para cualquier sesión dentro de la oficina, los comandos que publican o envían (Netlify, Vercel, Cloudflare, `git push`, `npm publish`) y la lectura de archivos `.env` con claves. Aunque una sesión se equivoque, no puede publicar sola: Santiago lo hace o lo autoriza en el momento. Si hay que agregar otro servicio de publicación, se suma a la lista `deny`.

## Reglas que no cambian

- Nada se publica, se envía, se conecta ni se cobra sin la autorización de Santiago para ese caso. Una aprobación vale para ese caso, no para los siguientes.
- No se usan servicios ni APIs de pago sin autorización.
- Los datos de un cliente no pasan a la carpeta de otro.
- No se inventan precios, plazos ni respuestas del cliente: lo no confirmado dice "de ejemplo" o "por confirmar".
- Todo lo web se prueba en celular, no solo en computador.
