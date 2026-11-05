# Rutina diaria de prospección: Santiago y Mathias (acordada 5-nov-2026)

Complementa [FLUJO_PROSPECCION.md](FLUJO_PROSPECCION.md) (cómo se busca y diagnostica) y [RUTINA_DIARIA.md](RUTINA_DIARIA.md) (cómo se programa en Gmail). Si algo choca, manda este archivo.

## Cuota diaria
| Canal | Quién envía | Cantidad | Desde |
|---|---|---|---|
| Correo | Santiago | **20** (meta 30) | barriossantiago754@gmail.com |
| Correo | Mathias | **20** (meta 30) | Gmail de Mathias |
| WhatsApp | Santiago | **15** | +56 9 3244 7140 |

- Se parte en 20 correos por cuenta. A las dos semanas (≈19-nov) se revisan rebotes, respuestas y avisos de Gmail y, si está todo bien, se sube a 30.
- Los 14 borradores de Mathias que ya estaban aprobados **no** cuentan dentro de sus 20. Si los manda el mismo día, ese día pasa de 20: avisar.

## Quién prepara los lotes
- Puede hacerlo el Claude de cualquiera de los dos. **El 6-nov los prepara todos el Claude de Santiago** (40 correos + 15 WhatsApp).
- Antes de redactar, cada Claude baja lo último de GitHub (`sincronizar.ps1`) y cruza cada empresa contra `registro/prospectos.csv`, `registro/tabla_comercial.csv`, `lotes/` y la copia del tablero. Al terminar, registra el lote en `prospectos.csv` y lo sube. Así no se repiten empresas entre socios.

## Todo mensaje es personalizado
Cada correo y cada WhatsApp se escribe para esa empresa: nombra algo concreto y comprobado de ella (lo que hacen bien, su rubro y comuna, lo que se vio en su web, Maps o redes) y le ofrece el servicio que resuelve **su** problema. Si no hay un hecho particular verificable, no se escribe: queda "pendiente", como pasó con El Quincho. Nada de plantillas con solo el nombre cambiado; antes de entregar el lote, cada texto pasa por `humanizador`.

## Correos
- Mismas reglas de siempre: uno por empresa, sin adjuntos, sin seguimientos automáticos, ~90 palabras, trato de usted, sin dominios en el cuerpo, enganche positivo (no partir por un error), un solo servicio del tarifario, línea legal de baja.
- **Firmas**
  - Santiago: `Santiago Barrios · Ascensus · WhatsApp +56 9 3244 7140`
  - Mathias: `Mathias Lezana · Ascensus · WhatsApp +56 9 4931 1482`
- **Entrega**
  - Santiago: borradores en su Gmail. Se programan o envían solo cuando él aprueba el lote en el chat.
  - Mathias: archivo `ventas/lotes/AAAA-MM-DD-mathias/correos.md` en GitHub (empresa, correo, asunto y cuerpo), listo para que su Claude los cargue como borradores.

## WhatsApp
- Solo empresas que publican WhatsApp o celular y **no** publican correo (antes se descartaban). Nunca la misma empresa por los dos canales.
- **Tampoco se cruzan entre socios:** una empresa que Mathias ya contactó por correo o WhatsApp no se le escribe por WhatsApp a Santiago, y al revés. El cruce es el mismo que para los correos.
- Mensaje más corto que el correo (≈50 palabras), mismo enganche personalizado, presentarse con nombre y empresa, ofrecer el diagnóstico gratis y cerrar con una pregunta. Si responden "no", no se vuelve a escribir.
- Claude prepara un artefacto con los 15 del día: empresa, por qué se le escribe y un botón `wa.me` con el mensaje ya escrito. Santiago lo abre, revisa y envía uno por uno desde su teléfono.
- Registrar en `prospectos.csv` con canal WhatsApp.

## Prioridad de rubros (6-nov)
Repartir entre: turismo y cabañas del litoral (Sernatur), salud (clínicas, kinesiología), construcción y hogar, restaurantes y comercio especializado. Empresas ya formadas.

**Zona: partir por las comunas con más ingresos de la región** y bajar desde ahí. Lista inicial, que se confirma con datos de ingreso (CASEN) al preparar el primer lote: Concón, Viña del Mar (Reñaca, Jardín del Mar, Recreo), Zapallar y Cachagua, Papudo, Maitencillo (Puchuncaví) y Santo Domingo.
