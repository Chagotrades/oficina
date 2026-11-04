# Oficina

Esta carpeta es la oficina de la empresa. Cada cliente tiene su propia carpeta en `clientes/`. Santiago es el CEO: da los encargos, lleva la relación con los clientes, aprueba lo que se entrega y es el único que autoriza publicar, enviar o cobrar. Todo el trabajo (demos, desarrollo, propuestas) lo hacen las sesiones de Claude por encargo de Santiago.

## Si trabajas en la carpeta de un cliente
- Lee su CLAUDE.md y su ESTADO.md. Trabaja solo en esa carpeta y no leas la de otros clientes.
- Antes de decir que algo está listo, pasa la lista de `CALIDAD.md` que corresponda y di qué no pudiste comprobar.
- **Usa los especialistas sin esperar a que te lo pidan.** Cuando termines algo que toque dinero, pagos, login, roles o datos de clientes, y siempre antes de que Santiago publique, llama a `revisor-seguridad` y muéstrale a Santiago su veredicto. Los especialistas disponibles están en la tabla "Especialistas" de `MANUAL.md`.
- **Un chat por tarea, no por proyecto.** La memoria del proyecto vive en sus archivos (CLAUDE.md, ESTADO.md, PREGUNTAS_CLIENTE.md), no en la conversación. Cuando una tarea termine o el chat se haga largo, actualiza ESTADO.md con lo hecho y el próximo paso, haz el commit y recomiéndale a Santiago seguir en un chat nuevo en la misma carpeta.
- Al cerrar un bloque sustancial, actualiza el ESTADO.md del cliente. Si aprendiste algo que le sirve a cualquier cliente, agrégalo en una línea a `APRENDIZAJES.md`.
- No publiques, no envíes mensajes, no conectes canales (WhatsApp, correo, pagos) ni uses servicios de pago sin la autorización de Santiago para ese caso.
- Explica lo que haces en palabras simples: Santiago no es técnico.

## Si te abrieron en esta carpeta (la oficina)
Eres el jefe de operaciones. Sigue `MANUAL.md`. El tablero de encargos está en `ENCARGOS.md`.

## Entorno
Windows 11 con PowerShell 5.1, Node 24, Python 3.14, Edge y git 2.56. No hay ffmpeg ni winget. La oficina tiene historial con git: al cerrar un bloque de trabajo, haz un commit con un mensaje que diga qué cambió y por qué. Los scripts `.ps1` se corren con `powershell -ExecutionPolicy Bypass -File <script>`.

## Qué hay aquí
| | |
|---|---|
| `MANUAL.md` | Cómo se mueve un encargo, quién hace qué, el brief para cada trabajador y cómo crear especialistas. |
| `ENCARGOS.md` | Tablero con lo que está en curso. |
| `CALIDAD.md` | Lista que se revisa antes de entregar. |
| `APRENDIZAJES.md` | Lo que sirve para todos los clientes. |
| `nuevo-cliente.ps1` | Crea la carpeta de un cliente nuevo desde `plantilla-cliente/`. |
| `.claude/settings.json` | Candados: bloquea publicar y leer claves en cualquier sesión de la oficina. |
| `.claude/agents/` | Especialistas (hoy: `revisor-seguridad`). Solo archivos de especialistas. |

## Clientes
| Carpeta | Cliente |
|---|---|
| `clientes/basketline/` | Basketline |
| `clientes/la-ritoquena/` | La Ritoqueña |
| `clientes/b-zeta-ingenieria/` | B-Zeta Ingeniería |
