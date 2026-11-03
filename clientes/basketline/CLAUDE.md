# Basketline

Tienda chilena de básquet (Nike: zapatillas, mochilas y calcetas) de Alexis, en Osorno y Temuco, con unos 13 mil seguidores en Instagram (@basketline.cl). Hoy vende solo por DM y WhatsApp, con pago por transferencia. Le estamos haciendo una tienda web con stock por talla y un panel que sea "una ayuda para el negocio". Proyecto de Santiago con un socio; Santiago desarrolla casi todo. Se vendió en $300.000.

## Leer al retomar
- ESTADO.md: qué etapa está hecha, qué está publicado y el próximo paso.
- PREGUNTAS_CLIENTE.md: lo que Alexis aprobó, lo que no quiere y lo que falta preguntarle. Consultar antes de cambiar algo que él haya definido.
- `docs/SPEC.md`: la especificación completa. Es la fuente de qué se construye.
- `docs/prompts-por-etapas.md`: las 3 etapas y qué entra en cada una.
- Solo si hace falta: `docs/transcripciones.md` (audios de Alexis y su diseñador; transcripción automática con errores), `docs/info-instagram.md`, `docs/inspiracion-tiendas-mobile.md`, `docs/investigacion-pagos-transferencia.md`.

## Estructura
- `demo/`: el código (Next.js 15 + TypeScript + Tailwind + Prisma + Supabase). Tiene su propio git, conectado a GitHub (`Chagotrades/basketline`). Los commits del código se hacen dentro de `demo/`.
- `docs/`: especificación, investigación y material del cliente. `docs/instagram/` tiene las fotos sacadas de su Instagram.

## Límites
- **Pagos solo por transferencia directa a la cuenta de la tienda.** Nada de pasarelas ni intermediarios (Webpay, Khipu, Fintoc, Mercado Pago): es decisión de Alexis por los reportes al SII.
- **Sin cambios ni devoluciones:** debe quedar claro en la ficha, el checkout y las preguntas frecuentes.
- **Dirección de arte del diseñador:** sobria y minimalista; negro, blanco, grises y dorado solo como acento; línea visual de naturaleza (pasto, cielo, luz natural). No se cambia sin preguntar.
- **Mobile first:** casi todos llegan desde Instagram en el celular. Revisar siempre a 390 px.
- **Nunca confiar en el precio ni en el stock que manda el navegador.** Stock a prueba de doble venta.
- Datos de prueba siempre marcados como tales. Los precios y productos reales salen de `docs/info-instagram.md`.
- No conectar el correo real del banco, la casilla de correos ni datos bancarios reales sin autorización de Santiago.

## Cómo se prueba y se publica
- Probar: `npm --prefix demo run dev` y abrir http://localhost:3000 (escucha en 0.0.0.0, así que también se puede ver desde el celular en la misma red). Base de datos: `npm --prefix demo run db:push` y `npm --prefix demo run db:seed`.
- Las claves de Supabase están en `demo/.env`: no se leen ni se copian. Las variables que existen están en `demo/.env.example`.
- **Antes de mostrar o publicar una etapa que toque pagos, login o datos de clientes:** revisión con el especialista `revisor-seguridad`.
- Publicar: la demo está en https://basketline.vercel.app y se publica con `npx vercel deploy --prod` desde `demo/`. **Solo lo hace Santiago.** En la oficina ese comando está bloqueado.
