# Estado — Basketline

Actualizado: 2026-11-03.

## Dónde estamos
- **Etapa 1 (tienda y stock por talla): construida.** Inicio con mochila 3D, catálogo por categoría, ficha de producto con tallas, página de lanzamientos con cuenta regresiva, "Avísame cuando llegue", carrito en panel lateral, botones flotantes y animaciones. Seed con fotos reales desde `demo/fotos/`.
- **Publicada** en https://basketline.vercel.app (Santiago la subió el 2026-11-03).
- **Etapa 2 (checkout y pago por transferencia): por hacer.** Checkout, seguimiento de pedido, monto único, "Listo, ya transferí", comprobante, correos del banco, conciliación, cartola, expiración y correos.
- **Etapa 3 (panel de administración): por hacer.** Login y roles, dashboard, productos con fotos desde el celular, inventario, pedidos, etiqueta 10x15, pagos, clientes, correos, contenido y configuración.
- La etapa 1 no ha pasado por la revisión de seguridad ni por `CALIDAD.md`.

## Próximo paso
1. Revisión de la etapa 1 con `revisor-seguridad` (es también la primera prueba del especialista).
2. Etapa 2. Es la más delicada: maneja plata y datos personales. Ojo con dos puntos del diseño: el endpoint de correo entrante del banco tiene que exigir autenticación (si no, cualquiera marca su pedido como pagado), y Alexis vende muchos pares únicos (una talla por modelo): la tienda ya los muestra, pero la reserva y la confirmación de stock tienen que resistir dos compras simultáneas del mismo par.
3. Antes de etapa 2, resolver con Alexis las preguntas 1 a 4 de PREGUNTAS_CLIENTE.md.

## Historial
Lo más nuevo arriba. Por cada bloque: fecha, qué cambió, cómo se comprobó y si está publicado o no.

- 2026-11-03: proyecto trasladado desde el Escritorio a la oficina (`clientes/basketline/`). Documentos movidos a `docs/`. El código se copió (la carpeta original estaba en uso) y se verificó idéntico: 25.432 archivos y 882.556.750 bytes, mismo commit (8c5a786), mismas huellas de `.env`, `schema.prisma`, `package.json` y `db.ts`. Levantado desde la nueva ubicación: la tienda carga los 38 productos desde Supabase. `C:\Users\cristobal\Desktop\basketline\demo` queda como respaldo hasta que Santiago lo borre.
- Visto al probar (no es del traslado): el 3D de la portada pide `/modelos/mochila-elite.glb`, que no existe (404) y usa su versión de respaldo; la tarjeta dice "¡Quedan 1!" en vez de "¡Queda 1!". Los pares únicos ya se muestran como "Par único · EUR 37.5".
- 2026-11-03: código subido a GitHub (`Chagotrades/basketline`) y publicado en Vercel.
- 2026-10-30: etapa 1 construida.
- 2026-10-29: especificación (`docs/SPEC.md`) armada desde los audios de Alexis y su diseñador, su Instagram y referentes de tiendas.
