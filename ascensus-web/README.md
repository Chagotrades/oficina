# Ascensus — web del estudio

Web corporativa basada en la dirección Editorial elegida por Mathias. La referencia está en `docs/referencia-visual.png`. La última indicación de Mathias, el 5 de noviembre de 2026, cambia el protagonismo del coral por **blanco marfil y negro**.

## Ver y editar

Requiere Node.js, sin instalar dependencias:

```powershell
cd ascensus-web
npm run dev
```

Abrir `http://127.0.0.1:4173`. También se puede abrir `index.html` directamente; la copia al portapapeles depende de los permisos del navegador.

```powershell
npm run check
```

## Dónde cambiar cada cosa

| Archivo | Contenido |
|---|---|
| `index.html` | Portada, estudio, proceso, contacto y metadatos. |
| `styles.css` | Paleta, tipografía, cascada de sitios, grilla y tamaños móviles. |
| `app.js` | Las seis demos, filtros, ventanas, vistas escritorio/celular y mensaje de contacto. |
| `assets/` | Fotos en dos resoluciones, fuentes locales, licencias, favicon y logo de la oficina. |
| `server.mjs` | Vista previa local; no es un servidor de producción. |
| `ESTADO.md` | Continuidad: qué está listo y qué queda por decidir. |
| `docs/VERIFICACION.md` | Pruebas, mediciones y límites. |
| `docs/FUENTES.md` | Origen de textos, imágenes y fuentes. |

## Qué incluye

- Portada editorial con una cascada diagonal de seis sitios seleccionables.
- Galería por Turismo, Servicios, Gastronomía y Salud.
- Seis exploraciones de marcas ficticias: Refugio del Sur, A Medida, Mesa, Cuidado Dental, Estudio Norte y Nexo Ingeniería.
- Demos navegables, con vista de escritorio y celular y enlace para consultar por una web similar.
- Presentación de Ascensus, sus principios y proceso de trabajo.
- Contacto: prepara un mensaje local y permite revisarlo, editarlo, copiarlo o continuar en WhatsApp con Mathias. **No envía mensajes automáticamente.**
- Navegación por teclado, cierre con Escape, foco en ventanas, adaptación móvil y respeto de movimiento reducido.
- Sin framework, instalación, backend, base de datos, analítica, cookies ni dependencias de producción. Las fuentes y fotos se sirven desde el propio proyecto.

## Compartir con Claude

En el repositorio `Chagotrades/oficina`, pedir:

> Continúa la web de Ascensus en `ascensus-web/`. Primero lee `CLAUDE.md` y `ESTADO.md` de esa carpeta y respeta el tablero `ENCARGOS.md`. Mantén la dirección blanco marfil y negro y la cascada de la referencia.

## Publicación

Esta entrega guarda el código en GitHub; **no habilita un dominio ni publica el sitio**. Para un alojamiento estático, la carpeta del sitio es `ascensus-web/`, con entrada `index.html`, sin comando de compilación. Los archivos `docs/`, `CLAUDE.md`, `ESTADO.md`, `README.md`, `package.json` y `server.mjs` son de trabajo y no necesitan publicarse. Elegir alojamiento y dominio con un socio antes de desplegar. No subir el repositorio completo: contiene información comercial ajena a la web.
