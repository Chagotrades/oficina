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
2. Etapa 2. Es la más delicada: maneja plata y datos personales. Ojo con dos puntos del diseño: el endpoint de correo entrante del banco tiene que exigir autenticación (si no, cualquiera marca su pedido como pagado), y Alexis vende muchos pares únicos (una talla por modelo), así que el stock por variante debe funcionar bien con cantidad 1.
3. Antes de etapa 2, resolver con Alexis las preguntas 1 a 4 de PREGUNTAS_CLIENTE.md.

## Historial
Lo más nuevo arriba. Por cada bloque: fecha, qué cambió, cómo se comprobó y si está publicado o no.

- 2026-11-03: proyecto movido desde el Escritorio a la oficina (`clientes/basketline/`). Código en `demo/`, documentos en `docs/`.
- 2026-11-03: código subido a GitHub (`Chagotrades/basketline`) y publicado en Vercel.
- 2026-10-30: etapa 1 construida.
- 2026-10-29: especificación (`docs/SPEC.md`) armada desde los audios de Alexis y su diseñador, su Instagram y referentes de tiendas.
