# Prompt para construir la demo de Basketline

> Copia todo lo que está debajo de la línea y pégalo en Claude Code (o tu herramienta de código) dentro de una carpeta vacía.

---

## Rol y objetivo

Eres un desarrollador full‑stack senior y diseñador de producto. Vas a construir una **demo funcional y lista para mostrar al cliente** de **Basketline**, una tienda chilena de básquetbol que vende **zapatillas y mochilas**. Hoy vende **solo por Instagram** (DMs), no tiene web y lleva pedidos y stock a mano.

La web tiene dos caras, y la segunda es la más importante para el dueño:
1. **Tienda pública** bonita, sobria y rápida, donde el cliente ve el stock real, compra y paga por transferencia.
2. **Panel de administración** que funcione como "ayuda para el negocio": stock, pedidos, pagos, envíos, fotos y estadísticas.

En palabras del dueño (Alexis): *"Más que una página web para el cliente, que sea como una ayuda para mí."*

Todo el contenido, la interfaz y los textos van en **español de Chile**, precios en **CLP** con formato `$45.990`.

## Contexto real del negocio (sacado de audios del cliente y su diseñador)

- **Dolor principal:** la gente escribe por Instagram *"¿Dónde puedo ver el stock disponible?"* y se pierde porque no hay dónde verlo. El catálogo con **stock visible por talla** es el corazón de la tienda.
- **Flujo actual:** el cliente manda sus datos por DM, Alexis los anota, arma el pedido, y al despachar (otro día) le vuelve a escribir con el comprobante de envío. Quiere que eso ocurra solo.
- **Correos automáticos:** además de la confirmación de compra, quiere **un segundo correo el día del despacho** ("Hoy se envía tu pedido, atento a…") con el número de seguimiento.
- **Fotos:** cuando llegan zapatillas nuevas, su equipo les saca fotos y quiere **subirlas directo** desde el panel (también desde el celular).
- **Stock:** poder modificarlo y llevar registro de qué entra y qué sale, sin venderle algo que no tiene.
- **Etiqueta de despacho:** al confirmarse un pedido, poder **imprimir al tiro** una etiqueta con los datos del cliente y pegarla en el paquete.
- **Pago:** **sin Webpay y sin intermediarios** (ni Khipu, Fintoc ni Mercado Pago), por el tema de los reportes al SII. Solo **transferencia bancaria directa** a la cuenta de la tienda. El cliente transfiere y aprieta "Listo, ya transferí". Aun así el sistema debe confirmar pagos de forma lo más automática posible (ver sección Pagos).
- **Estadísticas:** quiere saber qué es lo que más se pide.
- **Datos de su Instagram (@basketline.cl, ~13 mil seguidores):** zona Osorno–Temuco, envíos a todo Chile por **Starken por pagar**, pago por transferencia, **sin cambios ni devoluciones** (dejarlo claro en ficha, checkout y FAQ). Vende zapatillas de básquet (Kobe 9, LeBron 21/22, KD17, Ja 1/2, Sabrina 2, GT Cut 3, Luka 2, Book 1, A'One…; $79.990–$189.990), mochilas Nike Elite ($64.990, también a pedido en ~2 semanas) y **calcetas** con precio por cantidad (1x $12.000, 2x $22.000, 3x $30.000; mayorista desde 10 unidades): agrega la categoría Calcetas y precios escalonados por cantidad. Muchos modelos aparecen como "vendido": muéstralos como Agotado con "Avísame". En los comentarios lo que más preguntan es **talla y stock**, si son **originales** y **cómo se paga**: la tienda debe responder esas tres cosas a la vista.
- **También vende por WhatsApp** (botón flotante de WhatsApp además de Instagram). Abre **listas de pedidos/preventa** que llegan en 2–3 semanas: la tienda debe permitir productos "Por encargo" con fecha estimada de llegada y abono o pago total. Hace **promos por fecha** (Cyber 35%, Fiestas Patrias 18%, Primavera 21%): el panel debe poder crear campañas con % de descuento, fechas de inicio/fin y banner.

## Dirección de arte (definida por el diseñador)

- Estilo **sobrio y minimalista**. Paleta: **negro, blanco, escala de grises y detalles dorados** (dorado como acento, no como fondo). Ejemplo de tokens: `--negro #0B0B0B`, `--blanco #FAFAFA`, grises `#1A1A1A #2B2B2B #8A8A8A #D9D9D9`, `--dorado #C9A24D`.
- Nueva línea visual: **naturaleza**. Fotos de producto y lifestyle en **pasto, cielo, luz natural** (temporada de buen clima). Usa imágenes placeholder coherentes con eso (pueden ser de Unsplash con temática básquet/zapatillas/cancha al aire libre) y deja todo reemplazable desde el panel.
- Referencias de inspiración (no copiar): **Nike** y tiendas de sneakers de estética editorial. Tipografía grande y condensada para titulares, sans limpia para texto.
- Animaciones sutiles y premium: aparición al hacer scroll, hover en tarjetas de producto, transiciones suaves. Respeta `prefers-reduced-motion`. Mobile first: la mayoría llegará desde Instagram en el celular.
- El diseñador debe poder **cambiar banners, textos del hero y fotos de portada desde el panel** sin tocar código.

## Ideas de UX móvil tomadas de referentes (inspiración, no regla)

Se revisaron tiendas como Nike, SNS, END., Kith y Aimé Leon Dore (detalle en `inspiracion-tiendas-mobile.md`). Toma estas ideas como punto de partida y usa tu criterio: la identidad de Basketline (sobria, dorado, naturaleza, cercana a Instagram) manda por sobre copiar a cualquiera.

- **Filtro "Mi talla"** en el catálogo: el cliente elige su talla una vez y ve solo lo que tiene stock en ella (se recuerda para la próxima visita).
- **Grilla de tallas en botones**: agotadas tachadas pero tocables para "Avísame cuando llegue"; poco stock con punto dorado y "Quedan 2"; barra fija abajo con precio y "Agregar" que se activa al elegir talla.
- **Guía de tallas** en hoja que sube desde abajo, con tabla US/EU/CM.
- **Lanzamientos (drops)**: página con cuenta regresiva y "Avísame", pensada para enlazar desde las historias de Instagram.
- **Navegación**: header mínimo que se esconde al bajar, menú a pantalla completa con categorías grandes, carrito en panel lateral.
- **Catálogo** en 2 columnas, alternando foto de producto con foto lifestyle en exterior.
- **Vara a superar:** la competencia local mambasport.cl (WooCommerce) no muestra stock ni tallas en el catálogo, no tiene buscador útil y deriva todo a WhatsApp. La demo debe verse claramente más pulida y resolver esos tres puntos.

## Stack sugerido

- **Next.js (App Router) + TypeScript + Tailwind CSS**.
- **Supabase** (Postgres) como base de datos desde el inicio, con **Prisma** como ORM. Sirve igual para la demo publicada en Vercel y para producción. Variables en `.env` (`DATABASE_URL`, `DIRECT_URL`, claves de Supabase) con un `.env.example`.
- Autenticación simple para el panel (email + contraseña con hash, sesión en cookie httpOnly). Roles: `admin` (Alexis) y `equipo` (sube fotos y gestiona stock, no ve finanzas).
- Imágenes en **Supabase Storage** (bucket público `productos`), detrás de una interfaz `StorageProvider`. Despliegue en **Vercel**.
- Correos con una interfaz `EmailProvider`; en la demo se guardan en una tabla y se ven en una "bandeja de correos enviados" dentro del panel (y opcionalmente en consola). Plantillas HTML con la marca.
- Seed con datos realistas: ~16 zapatillas (marcas y modelos de básquet, tallas US 7 a 13 con stock distinto por talla, algunas agotadas), ~8 mochilas (stock por unidad/color), ~25 pedidos en distintos estados, movimientos de stock y abonos bancarios de ejemplo.

## Parte 1: Tienda pública

1. **Home / landing:** hero con foto lifestyle (editable), destacados, "Lo nuevo", "Más vendidos", sección **Quiénes somos** (historia de la marca y el equipo), link a Instagram, preguntas frecuentes (envíos, cambios, cómo pagar).
2. **Catálogo** `/tienda`: filtros por categoría (zapatillas / mochilas), marca, talla disponible, precio; orden por novedad y precio. Cada tarjeta muestra si hay stock o "Agotado". Buscador.
3. **Ficha de producto:** galería de fotos, precio, **selector de talla que muestra stock por talla** (tallas sin stock deshabilitadas, "¡Quedan 2!" cuando hay poco), descripción, guía de tallas, botón "Avísame cuando llegue" que guarda el email si está agotado.
4. **Carrito** persistente (localStorage) y **checkout** en una sola página: nombre, RUT (validado con dígito verificador), email, teléfono, región/comuna (lista de Chile), dirección, método de entrega (envío a domicilio con costo por zona o retiro coordinado), notas. Resumen del pedido.
5. Al confirmar se crea el pedido en estado **Pendiente de pago**, se **reserva el stock** por un tiempo (configurable, ej. 24 h) y se muestra la **pantalla de pago por transferencia** (ver Pagos).
6. **Seguimiento de pedido** `/pedido/[codigo]`: el cliente ve el estado (Pendiente de pago → Pago en revisión → Pagado → Preparando → Enviado → Entregado) y el número de seguimiento.
7. Opcional para la demo: **asistente de compra** (chat simple) que recomienda zapatillas del catálogo según posición, tipo de juego, presupuesto y talla. Puede funcionar con reglas sobre los datos del catálogo; deja la interfaz preparada para conectar un modelo de IA después.

## Parte 2: Pagos por transferencia directa (sin intermediarios)

La plata va **directo de la cuenta del cliente a la cuenta de Basketline**. No uses ninguna pasarela. La automatización se arma así:

1. **Pantalla de pago:** muestra los datos bancarios de la tienda (banco, tipo de cuenta, número, RUT, nombre, email) con botón **copiar todo** y copiar por campo, el **monto exacto** a transferir y el **código del pedido** (ej. `BL-1042`) que el cliente debe poner en el comentario de la transferencia. Cuenta regresiva del tiempo de reserva.
2. **Monto único ("huella"):** para identificar cada pago solo por el monto, al total se le descuenta un valor de $1 a $99 que no tenga ningún otro pedido pendiente (ej. $45.990 → $45.937). Se muestra como "descuento por transferencia". Configurable on/off.
3. **Botón "Listo, ya transferí":** pasa el pedido a **Pago en revisión** y permite (opcional) subir foto o PDF del comprobante.
4. **Lectura de comprobante (OCR):** extrae monto, fecha, banco y nombre/RUT del emisor del comprobante subido (en la demo puede ser simulado con un parser que lea texto; deja una interfaz `ReceiptReader`). Si coincide con el pedido, sube la confianza del match.
5. **Notificaciones del banco por correo (lo más automático):** los bancos chilenos envían un correo por cada transferencia recibida ("Has recibido una transferencia…") con monto, nombre, RUT y comentario. Implementa un módulo `BankEmailIngest` con parsers por banco (al menos Banco de Chile, BancoEstado, Santander, BCI, Scotiabank, con formato configurable) que reciba esos correos (en producción vía IMAP o reenvío a un webhook de correo entrante; en la demo, un botón "Simular correo del banco" y un endpoint `POST /api/banco/correo-entrante`). Cada correo se convierte en un **abono**.
6. **Conciliación automática:** cada abono se cruza con los pedidos pendientes por **monto exacto + código en el comentario + RUT + fecha**. Reglas: coincidencia segura → el pedido pasa solo a **Pagado**, se descuenta el stock definitivo y se manda el correo de confirmación. Coincidencia dudosa → queda en una bandeja "Por revisar" con sugerencias. Abono sin pedido → bandeja "Abonos sin asignar".
7. **Carga de cartola:** respaldo. El admin sube la cartola del banco (Excel/CSV), el sistema la parsea, ignora abonos ya conciliados y concilia el resto con las mismas reglas.
8. **Aprobación manual con un clic** y posibilidad de rechazar (con motivo y correo al cliente).
9. **Expiración:** si un pedido no se paga en el tiempo de reserva se cancela y se libera el stock; se manda un correo de aviso antes de que expire.
10. Todo cambio de estado de pago queda en un **historial auditable** (quién, cuándo, por qué: automático o manual).

## Parte 3: Panel de administración `/admin`

1. **Dashboard:** ventas del día/semana/mes, pedidos por estado, pagos por revisar, productos con stock bajo, **ranking de lo más vendido** (por modelo y por talla), ticket promedio, gráfico de ventas en el tiempo. Accesos rápidos a lo urgente.
2. **Productos:** crear/editar/archivar zapatillas y mochilas; marca, modelo, categoría, precio, precio oferta, descripción, etiquetas (nuevo, destacado). **Variantes por talla/color con stock propio.** Subida de **varias fotos arrastrando** o desde la cámara del celular, reordenarlas y elegir portada (comprimir y redimensionar al subir).
3. **Inventario:** vista tipo planilla de stock por variante, edición rápida, **registro de movimientos** (ingreso de mercadería, venta, ajuste, devolución) con fecha y usuario, alerta de stock bajo configurable, lista de "avísame cuando llegue" por producto.
4. **Pedidos:** lista con filtros y búsqueda; detalle con datos del cliente, productos, pago, historial. Acciones: marcar preparando, **marcar enviado ingresando courier y número de seguimiento** (dispara el correo de despacho), marcar entregado, cancelar.
5. **Etiqueta de despacho:** botón **Imprimir etiqueta** (vista de impresión de 10x15 cm) con nombre, RUT, teléfono, dirección, comuna/región, código de pedido y código QR del pedido. Impresión masiva de las etiquetas del día.
6. **Pagos:** bandejas "Por revisar", "Abonos sin asignar" y "Conciliados"; subir cartola; simular correo del banco; ver comprobantes.
7. **Clientes:** listado generado de los pedidos, historial de compras por cliente, total gastado.
8. **Correos:** bandeja de correos enviados (demo) y edición de plantillas: confirmación de pedido con datos para transferir, pago confirmado, **"Hoy se envía tu pedido"** con seguimiento, recordatorio de pago, pedido expirado/cancelado.
9. **Contenido del sitio (para el diseñador):** editar hero, banners, textos de Quiénes somos, fotos del equipo y FAQ.
10. **Configuración:** datos bancarios, tiempo de reserva, costos de envío por zona, monto único on/off, stock bajo, usuarios y roles.

## Requisitos de calidad

- Responsive impecable en celular; el panel también debe ser usable desde el celular (Alexis sube fotos y marca envíos desde ahí).
- Validaciones en servidor; nunca confiar en el precio que manda el navegador.
- Control de stock a prueba de doble venta (transacción al reservar y al confirmar).
- Accesibilidad básica (contraste, foco visible, textos alternativos), SEO básico (metadatos, Open Graph para compartir productos en Instagram/WhatsApp).
- Código ordenado por módulos, con las interfaces `StorageProvider`, `EmailProvider`, `ReceiptReader`, `BankEmailIngest` para cambiar las implementaciones de demo por las reales.
- Un `README` en español con: cómo correrlo, usuarios de prueba, y un **guion de demo** paso a paso.

## Guion de demo que debe funcionar de punta a punta

1. Entro a la tienda desde el celular, veo el catálogo con stock por talla, elijo unas zapatillas talla 10.
2. Hago el checkout, aparece la pantalla de transferencia con el monto único y el código, aprieto "Listo, ya transferí".
3. En el panel aprieto "Simular correo del banco" con ese monto y código: el pedido pasa solo a **Pagado**, baja el stock y aparece el correo de confirmación en la bandeja.
4. Imprimo la etiqueta de despacho.
5. Marco el pedido como enviado con número de seguimiento: sale el correo "Hoy se envía tu pedido".
6. Subo una cartola de ejemplo y veo cómo se concilian otros pedidos y queda un abono sin asignar.
7. Veo el dashboard con lo más vendido y el stock bajo.

Construye el proyecto completo, corre el seed y verifica tú mismo el guion de demo antes de terminar.
