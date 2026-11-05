# Tablero de encargos

Una fila por encargo, lo más nuevo arriba; el detalle va en el ESTADO.md de cada cliente. **Responsable** es el socio (Santiago o Mathias) que lo tomó; **Lo hace** es quién ejecuta (Claude, un especialista o el socio). Antes de empezar algo, ponle responsable y "en curso" y corre `sincronizar.ps1`. Lo que está en curso a nombre del otro socio no se toca sin hablarlo.

Estados: **por hacer** · **en curso** · **en revisión** · **esperando al socio** · **esperando al cliente** · **listo** · **descartado**

| Fecha | Cliente | Encargo | Responsable | Lo hace | Estado | Próximo paso |
|---|---|---|---|---|---|---|
| 2026-11-05 | Ascensus | Web corporativa editorial y demos por rubro | Mathias | Codex | en curso | Tomado por Mathias. Carpeta `ascensus-web/`. Referencia visual aprobada; nueva dirección blanco marfil y negro. Código y continuidad en GitHub; sin publicar en dominio. |
| 2026-11-05 | Ascensus (ventas) | Subir a la oficina todo lo comercial: tarifario, panel, método, contactados, logos y PDF | Mathias | Claude | esperando al socio | Hecho en `ventas/` (guía en `ventas/LEEME_ASCENSUS.md`). Falta subirlo a GitHub con `sincronizar.ps1` después de dejar el repositorio privado |
| 2026-11-05 | Basketline | Etapa 1: selector de 3 mochilas y modelos 3D | Santiago | Claude | esperando al cliente | Selector listo en la rama `etapa1-mochilas-3d` (sin probar en navegador). Modelos 3D y diseño con Gustavo cuando lleguen las fotos de Alexis (~2026-11-19) |
| 2026-11-03 | B-Zeta Ingeniería | Alta del cliente | Santiago | Santiago | por hacer | Completar descripción y límites en clientes/b-zeta-ingenieria/CLAUDE.md |
| 2026-11-03 | La Ritoqueña | Diagnóstico de laritoquena.com (prospecto) | Santiago | Claude | esperando al socio | Revisar el informe, poner precios y plazos a los 3 niveles y compartirlo con el dueño |
| 2026-11-03 | La Ritoqueña | Alta del cliente | Santiago | Claude | listo | — |
| 2026-11-03 | Basketline | Etapa 3: panel de administración | Santiago | Claude | en curso | Tomado 2026-11-05. Plan por bloques en la rama `etapa3-panel`: 1) login y roles, 2) pedidos y etiqueta, 3) productos y fotos, 4) inventario, 5) pagos, 6) dashboard, 7) clientes, correos, contenido, configuración y campañas, 8) README, guion de demo, CALIDAD.md y `revisor-seguridad`. Sin publicar en Vercel. Para probar en este PC hace falta copiar `demo/.env` |
| 2026-11-03 | Basketline | Etapa 2: checkout y pago por transferencia | Santiago | Claude | esperando al socio | Construida, en GitHub (`main`) y sin publicar. Santiago la prueba (`admin:clave` para su clave del panel); antes del banco real, preguntas 1 a 5 a Alexis |
| 2026-11-03 | Basketline | Revisión de seguridad de la etapa 1 | Santiago | `revisor-seguridad` | por hacer | Primera prueba del especialista |
| 2026-11-03 | Basketline | Preguntas para Alexis (boleta, banco, envíos, reserva) | Santiago | Santiago | por hacer | Ver PREGUNTAS_CLIENTE.md |
| 2026-11-03 | Basketline | Alta del cliente en la oficina | Santiago | Claude | listo | Santiago borra el respaldo del Escritorio cuando confirme que todo funciona |
| 2026-10-30 | Basketline | Etapa 1: tienda y stock por talla | Santiago | Claude | listo | Publicada en basketline.vercel.app |
