# Inspiración: tiendas streetwear y básquet (vista celular)

Investigación del 30-oct-2026 para la demo de Basketline. Idea central: copiar patrones de UX probados, no el diseño de nadie.

## Tiendas para mirar en el celular (y qué robarle a cada una)

| Tienda | Por qué mirarla | Idea concreta para Basketline |
|---|---|---|
| **Nike.com** (sección Basketball) | La referencia del diseñador | Tallas en grilla de botones, tallas agotadas tachadas en gris; foto a pantalla completa con deslizar horizontal; barra fija abajo "Agregar al carrito" |
| **SNS / Sneakersnstuff** (Suecia) | Ficha de zapatilla muy limpia y editorial | Selector de talla que cambia de sistema (US / EU / CM) con un toque; muestra precio y talla elegida en la barra fija |
| **END. Clothing** (UK) | Mejor manejo de drops y lanzamientos | Página "Próximos lanzamientos" con cuenta regresiva y botón "Avísame"; etiqueta "Últimas tallas" |
| **Kith** (USA) | Estética sobria blanco/negro, mucho aire | Home con foto grande + titular corto; menú hamburguesa a pantalla completa con categorías grandes en mayúsculas |
| **Aimé Leon Dore** (USA) | Fotos lifestyle en exterior, muy cercano a la línea "naturaleza" del diseñador | Alternar foto de producto (fondo neutro) con foto lifestyle en la grilla del catálogo |
| **Concepts / Bodega** (USA) | Historias detrás de cada lanzamiento | Bloque "La historia" en la ficha (por qué ese modelo, qué jugador lo usa) |
| **Foot Locker** | Baymard la usa de ejemplo de ficha móvil | Mostrar "Quedan 2" junto a la talla y "Recíbelo el jueves" bajo el botón |
| **Stüssy / Palace** | Minimalismo extremo, carga rapidísima | Grilla de 2 columnas, sin bordes, solo foto + nombre + precio |

## Patrones a copiar, por pantalla

**Navegación**
- Header mínimo: logo al centro, buscar y carrito a la derecha, menú a la izquierda. Se esconde al bajar y vuelve al subir.
- Menú a pantalla completa con categorías grandes: ZAPATILLAS, MOCHILAS, NUEVO, AGOTÁNDOSE.
- Chips horizontales arriba del catálogo para filtrar rápido: "Mi talla", marca, precio.

**Catálogo**
- 2 columnas en celular, foto cuadrada o 4:5, sin bordes.
- Al tocar "Mi talla" (ej. US 10) el catálogo muestra solo lo que tiene stock en esa talla. Se guarda la talla para la próxima visita. **Esto resuelve el dolor de Alexis ("¿dónde veo el stock?") mejor que cualquier otra cosa.**
- Etiquetas pequeñas sobre la foto: NUEVO, ÚLTIMAS TALLAS, AGOTADO.

**Ficha de producto**
- Galería a todo el ancho con deslizar y puntitos; tocar abre zoom.
- Grilla de tallas en botones (4 por fila). Sin stock: tachada y gris, pero tocable para "Avísame cuando llegue". Poco stock: puntito dorado + "Quedan 2".
- Barra fija abajo con precio + "Agregar" que se activa recién al elegir talla (si toca sin talla, la grilla vibra y se resalta).
- Guía de tallas en hoja que sube desde abajo (bottom sheet), con tabla US/EU/CM.
- Debajo: descripción corta, "La historia", envío y cambios en acordeones.

**Carrito y checkout**
- Carrito en panel lateral (no página nueva) con "Seguir comprando" y "Pagar".
- Checkout en una página, pasos colapsables, teclado correcto en cada campo (numérico para teléfono, email para correo), autocompletar región/comuna.
- Resumen del pedido siempre visible arriba, plegado.

**Drops / lanzamientos** (gran gancho para una tienda que vive de Instagram)
- Página de lanzamiento con cuenta regresiva, fotos y "Avísame por correo".
- Al abrir el drop, mismo flujo normal pero con stock en vivo bajando.
- Links directos desde las historias de Instagram a cada ficha (Open Graph con foto bonita).

## Toques "premium" baratos
- Fondo blanco roto, texto negro, dorado solo en precio de oferta, badges y botón principal al pasar.
- Titulares en tipografía condensada mayúscula (ej. "Archivo Black" o "Anton"), texto en "Inter".
- Transición suave al pasar de la tarjeta a la ficha (la foto "crece").
- Skeletons grises mientras carga en vez de spinners.

## Fuentes
- Ficha móvil de Foot Locker (Baymard): https://baymard.com/mcommerce-usability/benchmark/mobile-page-types/product-page/10818-foot-locker
- Guía de tallas de Nike (Baymard): https://baymard.com/ecommerce-design-examples/size-guide/19852-nike
- Sneakersnstuff en ecomm.design: https://ecomm.design/site/sneakersnstuff/
- Rediseño de Kith: https://avexdesigns.com/work/kith
- Awwwards, e-commerce en blanco y negro: https://www.awwwards.com/inspiration/black-and-white-e-commerce
- Hypebeast, mejores tiendas streetwear: https://hypebeast.com/2017/8/25-best-streetwear-shopping-websites
