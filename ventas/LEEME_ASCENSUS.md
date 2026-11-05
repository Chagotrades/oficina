# Ascensus comercial: todo lo trabajado hasta el 5-nov-2026

Resumen para que Santiago y Mathias tengan la misma información y puedan repartirse el trabajo. Lo armó Mathias con Claude a partir de su carpeta de trabajo (antes llamada FARO, en su computador). **Desde el 3-nov la empresa se llama Ascensus: no usar "Faro" ni "Faro SaMa" en nada nuevo.**

## En una frase
Buscamos empresas ya formadas de la Región de Valparaíso que tienen un problema medible en internet, les mandamos **un solo correo** personalizado ofreciendo un informe gratis y, a quien responde, le mandamos **informe + propuesta en PDF** con un servicio del tarifario.

## Dónde está cada cosa

| Quiero saber… | Archivo |
|---|---|
| Quiénes somos, garantías, tono y casos | [empresa/CONTEXTO.md](empresa/CONTEXTO.md) |
| **Qué tipo de clientes buscamos** y las reglas del correo | [empresa/RESUMEN_PARA_CODEX.md](empresa/RESUMEN_PARA_CODEX.md) (secciones "A quién le escribimos" y "Reglas del correo") |
| **Precios** | [tarifario/TARIFARIO.md](tarifario/TARIFARIO.md), el PDF para clientes [tarifario/Tarifario-Ascensus-2026.pdf](tarifario/Tarifario-Ascensus-2026.pdf) y el detalle de cada paquete (qué incluye, garantías, condiciones) en [tablero/TARIFAS_TABLERO.md](tablero/TARIFAS_TABLERO.md) |
| **Cómo buscamos prospectos y hacemos el diagnóstico** | [metodo/FLUJO_PROSPECCION.md](metodo/FLUJO_PROSPECCION.md) |
| **Cómo creamos los correos** | [metodo/plantillas/correo.md](metodo/plantillas/correo.md) + reglas en RESUMEN_PARA_CODEX.md + todos los correos reales en [tablero/CORREOS_TABLERO.md](tablero/CORREOS_TABLERO.md) |
| Cómo programamos los correos en Gmail cada día | [metodo/RUTINA_DIARIA.md](metodo/RUTINA_DIARIA.md) |
| **Cómo creamos los PDF** (informe + propuesta) | [metodo/plantillas/pdf-cliente/GUIA.md](metodo/plantillas/pdf-cliente/GUIA.md) (con `doc.css`, `maquetas.sh` y `pdf.sh`) |
| **Panel comercial** (copia del tablero) | [tablero/](tablero/): prospectos, correos, tarifas e ideas. Los datos crudos están en `tablero/datos/*.json` |
| **Todos los contactados** | [registro/tabla_comercial.csv](registro/tabla_comercial.csv) (172 empresas con diagnóstico, servicio, asunto y cuerpo) y [registro/prospectos.csv](registro/prospectos.csv) (151 filas) |
| Lotes de trabajo (diagnósticos, correos, PDF por empresa) | [lotes/](lotes/), una carpeta por fecha y lote |
| Logos | [marca/ascensus-logo.png](marca/ascensus-logo.png) (el que se usa) y [marca/logos/](marca/logos/) (las 3 propuestas, el avatar de Instagram y la comparativa; el elegido es `01-editorial-elegido.png`) |
| Scripts para buscar empresas y revisar sus webs | [herramientas/](herramientas/) (Python y Node, gratis: Google Maps sin sesión, OpenStreetMap, Sernatur, revisión en celular con Edge) |
| Historia completa día a día | [historial/ESTADO_PROSPECCION.md](historial/ESTADO_PROSPECCION.md) |

**Ojo con las rutas:** los documentos se copiaron tal cual, así que nombran rutas antiguas. Equivalencias: `plantillas/` → `metodo/plantillas/`, `lotes/` → `ventas/lotes/`, `prospectos.csv` y `tabla_comercial.csv` → `registro/`, `marca/` → `ventas/marca/`, scripts `_faro_*` → `herramientas/`.

## Cómo trabajamos (resumen del método)
1. **Buscar:** empresas formadas (muchas reseñas, años funcionando, SpA o razón social) en Viña, Concón, Quilpué, Litoral Central y el resto de la región. Solo si publican su correo de contacto. Fuentes gratis: lista de Google Maps, OpenStreetMap, registro de Sernatur (lo mejor para turismo) y la web de cada empresa.
2. **Diagnosticar:** revisar su web en celular (375 px), Google Maps y redes. Anotar un **problema medido** (se desborda en celular, web antigua o con texto de plantilla, sin WhatsApp/formulario, pocas reseñas…).
3. **Filtro "oferta concreta":** solo se escribe si podemos ofrecer **un servicio del tarifario** que resuelva ese problema. Sin eso, se descarta (así se descartaron 31 el 3-nov).
4. **Correo:** uno solo por empresa, sin seguimientos automáticos, sin adjuntos, ~90 palabras, trato de usted, sin dominios escritos en el texto. Estructura: algo que hacen bien → la oportunidad → "les preparo sin costo un informe breve" → una pregunta fácil. Firma "Mathias Lezana / Ascensus / WhatsApp +56 9 4931 1482" y la línea legal de baja (Ley 19.496).
5. **Aprobación:** un socio aprueba cada lote antes de programarlo. Máximo 15–20 correos al día desde Gmail.
6. **Si responden que sí:** informe (problema → en qué le afecta → cómo lo resolvemos, con capturas reales) + propuesta (plan con precio, maquetas, cómo empezamos), ambos con los colores y el logo del cliente. Ejemplos en `lotes/2026-11-03-la-ritoquena/pdf/`, `lotes/2026-11-03-bzeta/pdf/` y `lotes/2026-11-04-biosfera-lodge/pdf/`.
7. **Si dicen que no:** agradecer una vez y no volver a escribir nunca.

## Números al 5-nov
- **≈81 primeros correos enviados** (2-nov: 11 · 3-nov: 20 · 4-nov: 20 · 5-nov: 30).
- **3 interesados con propuesta enviada** ($249.990 cada uno).
- **1 cliente ganado:** Campo Verde San Pedro (Quillota), caso de portafolio.
- **6 rebotes** (la dirección no existe): Canemar, Consultora Tax, Reñaca Roller, Gala Hotel, Medikin, Campo y Playa.
- **2 rechazos:** Sastrería García Vellella (ya renuevan su web; se le contestó) y Ambientemar (dijo que no por WhatsApp).

## Clientes y prospectos calientes

| Empresa | Estado | Qué se mandó | Próximo paso |
|---|---|---|---|
| Campo Verde San Pedro (Quillota) | **Cliente** | Web + chatbot + cotizador + SEO, publicada en campoverdejardines.cl | Pedir testimonio y permiso para mostrarla como caso |
| B-Zeta Ingeniería (Clodomiro Aravena) | Propuesta enviada 3-nov por correo | Informe 8 págs. + propuesta 6 págs. — Renovación de web $249.990 | Un solo seguimiento por correo el **vie 6-nov** si no responde |
| La Ritoqueña (Diego Arenas) | Propuesta enviada 3-nov por WhatsApp | Informe + propuesta — Renovación de web $249.990 | Un solo seguimiento por WhatsApp el **vie 6-nov** si no responde |
| Biosfera Lodge (Juan Pablo Vásquez) | Propuesta enviada 4-nov por correo | Informe + propuesta — página de entrada conectada a su motor de reservas GoFeels, $249.990 | Un solo seguimiento el **sáb 7-nov** si no responde; averiguar qué permite GoFeels |

El detalle de cada prospecto (36 contactados, 14 por contactar, perdidos) está en [tablero/PROSPECTOS_TABLERO.md](tablero/PROSPECTOS_TABLERO.md).

## Tareas abiertas para repartir
Pongan nombre en `ventas/PROSPECTOS.md` o en `ENCARGOS.md` antes de tomar una.

1. **Viernes 6-nov:** de 20 correos aprobados solo 6 están programados en Gmail. Los otros 14 siguen en Borradores (Oral Clinic, Más Salud, Fisiosalud, StockPro, Auramed, Bellavi, Taller Torres, Adelma, Regina, Maison de la Mer, Bote Salvavidas, Domus Mare, Chanagua, New Voga). Decidir si se programan.
2. **Seguimientos únicos** a B-Zeta, La Ritoqueña (vie 6) y Biosfera (sáb 7).
3. **Revisar respuestas** en el Gmail de Mathias y contestar: sí → informe en 48 h; quiere hablar → 15 min por WhatsApp; no → "Gracias, no le volveré a escribir".
4. **Aprobar o no la simplificación del tarifario** (3 servicios principales; ver TARIFARIO.md).
5. **Testimonio de Campo Verde.**
6. **Pendientes del negocio:** definir cliente ideal (rubro y comuna), revisar dominio en NIC Chile y marca en INAPI, correo con dominio propio (hoy sale del Gmail personal de Mathias).
7. **Mantener al día `registro/prospectos.csv`** después de cada envío o respuesta (al 5-nov: 74 enviados o con propuesta, 6 rebotados, 2 no contactar, 6 programados para el 6-nov, 21 borradores, 42 descartados).

## Qué NO está aquí (y por qué)
- **El tablero en vivo** es una página de claude.ai de Mathias: https://claude.ai/artifact/H8ocFj8fHuVTHwbxDByB4Y (se abre solo si Mathias la compartió con tu cuenta). Esta carpeta tiene una **copia al 5-nov**.
- **Fotos originales y maquetas** de cada propuesta (≈45 MB): quedan en el computador de Mathias. Los PDF ya las incluyen.
- **Los correos de Gmail** (enviados, borradores, respuestas) viven en la cuenta de Mathias.
- **Datos personales:** solo guardamos datos de contacto que las empresas publican. Si alguien pide que lo borremos, se borra de todos los archivos (Ley 21.719).
