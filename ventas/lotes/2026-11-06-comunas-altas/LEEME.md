# Lote del viernes 6-nov-2026: comunas de más ingresos

Lo preparó el Claude de Santiago el 5-nov, según `metodo/RUTINA_DIARIA_SOCIOS.md`.

| Qué | Cuántos | Dónde | Estado |
|---|---|---|---|
| Correos de Santiago | 20 | [correos_santiago.md](correos_santiago.md) | Borradores en el Gmail de Santiago, **sin programar ni enviar**. Santiago aprueba y programa. |
| Correos de Mathias | 20 | [correos_mathias.md](correos_mathias.md) | **Programados** el 5-nov en el Gmail de Mathias para el 6-nov (8:00 a 11:24, intercalados con los 14 borradores antiguos). Horas verificadas una por una en Programados (40 en total ese día). |
| WhatsApp de Santiago | 15 | Artefacto "WhatsApp del día" (https://claude.ai/artifact/B8fqv7gh7hcnG56ZsQy49C), copia en [whatsapp-6nov.html](whatsapp-6nov.html) y datos en [whatsapp.json](whatsapp.json) | Santiago los envía uno por uno desde su celular. |

Los 55 quedaron en `registro/prospectos.csv` (estados `borrador`, `preparado` y `preparado_whatsapp`). Al enviar, cambiar el estado a `enviado` con la fecha.

## Cómo se armó
- **Fuentes:** registro de Sernatur (correos publicados), OpenStreetMap y Google Maps.
- **Zona:** Viña del Mar (Reñaca, Recreo), Concón, Maitencillo, Zapallar (La Laguna), Papudo y Santo Domingo. El orden por ingreso no se comprobó con CASEN.
- **Sin repetidos:** cada empresa se cruzó contra `registro/*.csv`, `tablero/datos/*.json`, `lotes/*/excluir.json` y los clientes actuales. También se buscó en el Gmail de Santiago, sin resultados. Ninguna empresa se repite entre canales ni entre socios.
- **Hechos:** cada correo nombra un hecho comprobado el 5-nov.
  - Web revisada en celular de 375 px con Edge (`herramientas/_faro_movil.mjs`).
  - Señales de contacto (WhatsApp, formulario, teléfono para tocar) con `_faro_scan.py`.
  - Los casos más llamativos se volvieron a abrir en el navegador: Hotel Florencia y Pica Los Canalla con la cuenta suspendida, Yemanyá con la página de prueba del servidor, Hollywood en mantenimiento, el enlace de Calipso que lleva a un casino en línea y el de Masamor que lleva a Ajinomoto Filipinas.
- **WhatsApp:** negocios con nota 4,3 o más, celular y sin web en Google Maps.
  - No se puede asegurar que no publiquen un correo en Instagram.
  - Varios son más chicos que el cliente ideal: electricistas y gasfíter.

## Pendiente
- Rubros: casi todo el lote es turismo y gastronomía, porque Sernatur es la fuente con más correos publicados. Salud tiene 1 correo (Clínica Dental Montemar) y 4 WhatsApp. Para construcción y hogar hay que seguir buscando en Google Maps en el próximo lote.
- Los correos tienen entre 108 y 138 palabras contando saludo, oferta del informe y pregunta. Es el mismo largo que los ya enviados, por sobre las ~90 del método.
