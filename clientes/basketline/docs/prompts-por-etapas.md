# Basketline: construir la demo en 3 etapas

**Antes de empezar**
1. Crea una carpeta vacía para el código (ej. `Desktop\basketline\demo`) y copia dentro `prompt-demo-basketline.md` con el nombre `SPEC.md`. Es la especificación completa; cada etapa la cita.
2. (Opcional, muy recomendado) Crea `demo\fotos\` con las fotos reales de Basketline, una carpeta por producto:
   `fotos\nike-giannis-freak-6__89990\1.jpg, 2.jpg...` (nombre del producto, dos guiones bajos, precio sin puntos). Si no hay fotos, la demo usa placeholders.
3. Crea un proyecto gratis en supabase.com y ten a mano la URL de conexión y las claves (Project Settings → Database y API). Claude Code te las pedirá para el `.env`.
4. Abre Claude Code en esa carpeta y pega las etapas una por una. No pases a la siguiente hasta revisar la anterior en el celular.

---

## Etapa 1: Tienda y stock por talla

```
Lee SPEC.md completo: es la especificación de la demo de Basketline. En esta etapa construye SOLO la base y la tienda pública:
- Proyecto Next.js + TypeScript + Tailwind + Prisma/Supabase según "Stack sugerido".
- Modelo de datos completo (productos, variantes por talla con stock, pedidos, pagos, movimientos de stock, usuarios), aunque aquí solo uses una parte.
- Seed: si existe la carpeta ./fotos, crea un producto por subcarpeta (nombre y precio desde "nombre__precio", fotos en orden) con tallas US 7-13 y stock aleatorio; completa con productos de ejemplo hasta tener ~16 zapatillas y ~8 mochilas. Si no hay fotos, usa placeholders coherentes con la "Dirección de arte".
- Home, catálogo y ficha de producto (Parte 1, puntos 1 a 3) con TODAS las ideas de "Ideas de UX móvil": filtro "Mi talla", grilla de tallas con stock, barra fija abajo, guía de tallas en hoja inferior, página de lanzamientos.
- Carrito en panel lateral (todavía sin checkout).
Usa las skills animaciones y efectos-interactivos para los movimientos, con prefers-reduced-motion. Diseña mobile first y revisa a 390 px de ancho. Al terminar, corre el seed, levanta el sitio y dime cómo verlo en mi celular.
```

## Etapa 2: Checkout y pago por transferencia

```
Sigue con SPEC.md. Ya está la tienda (etapa 1). Ahora construye:
- Checkout en una página y seguimiento de pedido (Parte 1, puntos 4 a 6), con reserva de stock en transacción.
- Toda la "Parte 2: Pagos por transferencia directa": pantalla de pago con monto único y código, "Listo, ya transferí", subida de comprobante, BankEmailIngest con "Simular correo del banco", conciliación automática, carga de cartola, expiración e historial.
- EmailProvider de demo con bandeja de correos y las plantillas (confirmación, pago confirmado, recordatorio, expirado).
Prueba de punta a punta: compro desde la tienda, simulo el correo del banco y el pedido queda Pagado solo, con el stock descontado. Muéstrame el resultado.
```

## Etapa 3: Panel de administración y cierre

```
Sigue con SPEC.md. Ya están la tienda y los pagos. Ahora construye toda la "Parte 3: Panel de administración" (/admin) con login y roles: dashboard, productos con subida de fotos desde el celular, inventario con movimientos, pedidos, etiqueta de despacho 10x15 con QR, pagos, clientes, correos, contenido del sitio y configuración. El panel también debe ser cómodo en el celular.
Después revisa "Requisitos de calidad", escribe el README en español y corre el "Guion de demo" completo, arreglando lo que falle. Dime qué pasos funcionaron.
```
