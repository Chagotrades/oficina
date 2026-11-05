'use strict';

// Concept brands only. Do not replace these with client work without permission.
const demos = [
  { id: 'refugio', name: 'Refugio del Sur', short: 'Refugio', category: 'Turismo', title: 'Cabañas en el bosque patagónico', subtitle: 'Descanso, naturaleza y conexión en el sur de Chile.', action: 'Explorar estadías', nav: ['Cabañas', 'Experiencias', 'Entorno'], serif: false, light: false, position: 'center 58%', intro: 'Un lugar para bajar el ritmo.', description: 'Una propuesta para alojamientos que quieren transmitir la experiencia antes de la primera reserva.', features: [['El refugio', 'Espacios cálidos, rodeados de naturaleza. Una presentación que invita a imaginar la estadía.'], ['La experiencia', 'Rutas, paisajes y momentos para descubrir el entorno sin apuro.'], ['Tu próxima escapada', 'Información clara para elegir y dar el siguiente paso hacia una reserva.']] },
  { id: 'amedida', name: 'A MEDIDA', short: 'A medida', category: 'Servicios', title: 'Sastrería con carácter', subtitle: 'Vestuario a tu medida, hecho en Chile.', action: 'Conocer el oficio', nav: ['Sastrería', 'Camisas', 'Accesorios'], serif: true, light: false, position: 'center 40%', intro: 'El detalle hace la diferencia.', description: 'Una dirección editorial para negocios donde el oficio, los materiales y la atención personal son protagonistas.', features: [['Hecho para ti', 'Un recorrido que explica el servicio y ayuda a elegir con confianza.'], ['Materiales y oficio', 'Texturas y detalles que cuentan lo que hace distinto a un trabajo a medida.'], ['Atención personal', 'Un siguiente paso claro para conversar sobre una prenda o agendar una visita.']] },
  { id: 'mesa', name: 'Mesa', short: 'Mesa', category: 'Gastronomía', title: 'Cocina de estación', subtitle: 'Productos locales y sabor de origen.', action: 'Descubrir la carta', nav: ['Carta', 'El restaurante', 'Reservas'], serif: true, light: false, position: 'center 58%', intro: 'Del origen a la mesa.', description: 'Una experiencia para restaurantes que quieren abrir el apetito, contar su cocina y facilitar la visita.', features: [['De temporada', 'Una carta fácil de recorrer, con espacio para destacar los ingredientes y el origen.'], ['El encuentro', 'Una atmósfera cercana que muestra cómo se vive el restaurante.'], ['Una mesa para ti', 'Horarios, ubicación y contacto en un recorrido pensado para el celular.']] },
  { id: 'cuidado', name: 'Cuidado Dental', short: 'Cuidado', category: 'Salud', title: 'Salud dental para tu día a día', subtitle: 'Prevención, tratamiento y una atención cercana.', action: 'Ver tratamientos', nav: ['Tratamientos', 'Equipo', 'Clínica'], serif: false, light: true, position: '70% center', intro: 'Sentirse bien también es confiar.', description: 'Una propuesta para clínicas que necesitan explicar con claridad y acercar la atención a las personas.', features: [['Prevención', 'Contenido simple para conocer los controles y cuidar tu salud bucal.'], ['Tratamientos', 'Información organizada que ayuda a entender las alternativas antes de consultar.'], ['Atención cercana', 'Una presentación del equipo y un camino claro para solicitar una hora.']] },
  { id: 'norte', name: 'Estudio Norte', short: 'Norte', category: 'Servicios', title: 'Arquitectura que conecta personas y lugar', subtitle: 'Espacios pensados para la forma en que vivimos.', action: 'Explorar el estudio', nav: ['Proyectos', 'Estudio', 'Contacto'], serif: false, light: true, position: '65% center', intro: 'Habitar una idea.', description: 'Una propuesta para estudios que quieren dar espacio a sus proyectos y explicar su mirada de diseño.', features: [['Una mirada propia', 'Una introducción al estudio, sus criterios y su manera de entender cada lugar.'], ['Proyectos con contexto', 'Imágenes y relatos breves que explican las decisiones detrás de cada espacio.'], ['El próximo proyecto', 'Un punto de encuentro para conversar sobre una idea y sus posibilidades.']] },
  { id: 'nexo', name: 'Nexo Ingeniería', short: 'Nexo', category: 'Servicios', title: 'Soluciones de ingeniería para proyectos reales', subtitle: 'Experiencia técnica. Un objetivo en común.', action: 'Conocer especialidades', nav: ['Ingeniería', 'Proyectos', 'Especialidades'], serif: false, light: false, position: 'center 50%', intro: 'Claridad para construir confianza.', description: 'Una dirección para empresas técnicas que necesitan comunicar lo que hacen sin perderse en explicaciones complejas.', features: [['Especialidades', 'Servicios explicados con precisión y un lenguaje que facilita la consulta.'], ['Trabajo en terreno', 'Espacio para mostrar procesos, equipo y capacidades con evidencia.'], ['Hablemos del proyecto', 'Una invitación concreta para recibir el contexto y entender el requerimiento.']] }
];

const grid = document.querySelector('#demo-grid');
const collage = document.querySelector('#hero-collage');
const demoDialog = document.querySelector('#demo-dialog');
const contactDialog = document.querySelector('#contact-dialog');
const contactForm = document.querySelector('#contact-form');
let currentDemo = null;
let preparedMessage = '';
let returnFocus = null;

function preview(demo, eager = false) {
  return `<div class="site-preview ${demo.serif ? 'serif' : ''} ${demo.light ? 'light-preview' : ''} ${['norte', 'nexo'].includes(demo.id) ? 'long-copy' : ''}">
    <img class="preview-image" src="assets/${demo.id}-small.jpg" ${eager ? 'fetchpriority="high"' : 'loading="lazy"'} decoding="async" width="580" height="387" alt="" style="object-position:${demo.position}">
    <div class="mini-nav"><span class="mini-brand">${demo.name}</span><span class="mini-links" aria-hidden="true">${demo.nav.map(item => `<span>${item}</span>`).join('')}</span></div>
    <div class="mini-copy"><h3>${demo.title}</h3><p>${demo.subtitle}</p><span class="mini-cta" aria-hidden="true">${demo.action} ↗</span></div>
  </div>`;
}

function renderGallery() {
  grid.innerHTML = demos.map(demo => `<article class="demo-card" data-category="${demo.category}">
    <button class="demo-preview-button" data-demo="${demo.id}" aria-label="Abrir demo conceptual de ${demo.name}">${preview(demo)}</button>
    <div class="card-details"><div><p class="eyebrow">Demo conceptual</p><h3>${demo.short} / ${demo.category}</h3></div><button class="view-demo" data-demo="${demo.id}" aria-label="Ver demo de ${demo.name}"><span>Ver demo</span><span aria-hidden="true">↗</span></button></div>
  </article>`).join('');
  const cascadeOrder = ['norte', 'cuidado', 'mesa', 'nexo', 'amedida', 'refugio'];
  collage.innerHTML = cascadeOrder.map(id => {
    const demo = demos.find(item => item.id === id);
    return `<button class="hero-card" data-demo="${id}" aria-label="Explorar propuesta conceptual ${demo.name}">${preview(demo, true)}</button>`;
  }).join('');
}

function setMenu(open) {
  document.querySelector('.menu-toggle').setAttribute('aria-expanded', String(open));
  document.querySelector('.menu-toggle').setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
  document.querySelector('#mobile-nav').hidden = !open;
}

function updateBodyLock() {
  document.body.classList.toggle('modal-open', demoDialog.open || contactDialog.open);
}

function openContact(suggestion = '') {
  if (!demoDialog.open) returnFocus = document.activeElement;
  if (demoDialog.open) demoDialog.close();
  setMenu(false);
  contactForm.hidden = false;
  document.querySelector('#contact-result').hidden = true;
  if (suggestion) contactForm.elements.idea.value = suggestion;
  contactDialog.showModal();
  updateBodyLock();
}

function openDemo(id) {
  currentDemo = demos.find(demo => demo.id === id);
  if (!currentDemo) return;
  returnFocus = document.activeElement;
  const d = currentDemo;
  document.querySelector('#demo-dialog-title').textContent = `${d.short} / ${d.category}`;
  document.querySelector('#demo-page').innerHTML = `
    <div class="full-demo-nav"><strong>${d.name}</strong><a href="#demo-details">${d.nav[0]} ↓</a></div>
    <section class="full-demo-hero ${d.serif ? 'full-demo-seriffed' : ''}">
      <img src="assets/${d.id}.jpg" srcset="assets/${d.id}-small.jpg 580w, assets/${d.id}.jpg 1100w" sizes="(max-width:640px) 90vw, 1000px" width="1100" height="733" alt="Fotografía de referencia para la propuesta ${d.name}" style="object-position:${d.position}">
      <div><p class="eyebrow">${d.category} · Una propuesta de Ascensus</p><h3>${d.title}</h3><p>${d.subtitle}</p><a class="button" href="#demo-details">${d.action} ↓</a></div>
    </section>
    <section class="full-demo-body" id="demo-details"><p class="eyebrow">El concepto</p><h4>${d.intro}</h4><div class="demo-feature-grid">${d.features.map((feature, i) => `<div class="demo-feature"><span>0${i + 1}</span><h5>${feature[0]}</h5><p>${feature[1]}</p></div>`).join('')}</div><div class="demo-inquiry"><h5>¿Te imaginas algo así para tu negocio?</h5><p>${d.description}</p><button class="button button-dark" data-similar>Conversemos sobre una web así ↗</button></div><p class="concept-note">Esta es una exploración visual de Ascensus. ${d.name} es una marca ficticia. Las imágenes son de referencia; no representa un cliente real ni permite realizar reservas, compras o solicitar atención.</p></section>`;
  setDemoView('desktop');
  demoDialog.showModal();
  document.querySelector('#demo-viewport').scrollTop = 0;
  updateBodyLock();
}

function setDemoView(view) {
  document.querySelector('#demo-viewport').classList.toggle('mobile', view === 'mobile');
  document.querySelectorAll('[data-view]').forEach(button => {
    const active = button.dataset.view === view;
    button.classList.toggle('active', active);
    button.setAttribute('aria-pressed', String(active));
  });
}

document.querySelectorAll('[data-filter]').forEach(button => button.addEventListener('click', () => {
  const filter = button.dataset.filter;
  let count = 0;
  document.querySelectorAll('[data-filter]').forEach(item => {
    const active = item === button;
    item.classList.toggle('active', active);
    item.setAttribute('aria-pressed', String(active));
  });
  document.querySelectorAll('.demo-card').forEach(card => {
    card.hidden = filter !== 'Todos' && card.dataset.category !== filter;
    if (!card.hidden) count++;
  });
  document.querySelector('#filter-status').textContent = `${count} ${count === 1 ? 'demo conceptual' : 'demos conceptuales'}${filter === 'Todos' ? '' : ` de ${filter}`}`;
}));

document.addEventListener('click', event => {
  const trigger = event.target.closest('[data-demo]');
  if (trigger) openDemo(trigger.dataset.demo);
  if (event.target.closest('[data-contact]')) openContact();
  if (event.target.closest('[data-similar], #similar-project')) {
    openContact(currentDemo ? `Me gustó la propuesta ${currentDemo.name}. Quiero conversar sobre una web con esa dirección para mi negocio.` : 'Quiero conversar sobre una web para mi negocio.');
  }
});
document.querySelectorAll('[data-view]').forEach(button => button.addEventListener('click', () => setDemoView(button.dataset.view)));
document.querySelector('[data-close-demo]').addEventListener('click', () => demoDialog.close());
document.querySelector('[data-close-contact]').addEventListener('click', () => contactDialog.close());
document.querySelector('.menu-toggle').addEventListener('click', event => setMenu(event.currentTarget.getAttribute('aria-expanded') !== 'true'));
document.querySelectorAll('#mobile-nav a').forEach(link => link.addEventListener('click', () => setMenu(false)));
document.addEventListener('keydown', event => { if (event.key === 'Escape') setMenu(false); });

for (const dialog of [demoDialog, contactDialog]) {
  dialog.addEventListener('close', () => { updateBodyLock(); if (!demoDialog.open && !contactDialog.open && returnFocus?.isConnected) returnFocus.focus({ preventScroll: true }); });
  dialog.addEventListener('click', event => {
    if (event.target !== dialog) return;
    const box = dialog.getBoundingClientRect();
    if (event.clientX < box.left || event.clientX > box.right || event.clientY < box.top || event.clientY > box.bottom) dialog.close();
  });
}

// This form has no backend. No information leaves the browser until the visitor
// follows the WhatsApp link, reviews the message there, and chooses to send it.
contactForm.addEventListener('submit', event => {
  event.preventDefault();
  if (!contactForm.reportValidity()) return;
  const data = new FormData(contactForm);
  const name = String(data.get('name') || '').trim();
  const business = String(data.get('business') || '').trim();
  const idea = String(data.get('idea') || '').trim();
  const fields = [[contactForm.elements.name, name], [contactForm.elements.business, business], [contactForm.elements.idea, idea]];
  for (const [field, value] of fields) {
    field.setCustomValidity(value ? '' : 'Escribe al menos una palabra.');
    if (!value) { field.reportValidity(); return; }
  }
  preparedMessage = `Hola, Mathias. Soy ${name}, de ${business}. Vi la web de Ascensus y me gustaría conversar.\n\n${idea}`;
  document.querySelector('#message-preview').textContent = preparedMessage;
  // Published commercial contact in ventas/empresa/RESUMEN_PARA_CODEX.md.
  document.querySelector('#whatsapp-link').href = `https://wa.me/56949311482?text=${encodeURIComponent(preparedMessage)}`;
  contactForm.hidden = true;
  document.querySelector('#contact-result').hidden = false;
  document.querySelector('#copy-status').textContent = '';
  document.querySelector('#whatsapp-link').focus();
});
contactForm.addEventListener('input', event => event.target.setCustomValidity?.(''));
document.querySelector('#edit-message').addEventListener('click', () => {
  document.querySelector('#contact-result').hidden = true;
  contactForm.hidden = false;
  contactForm.elements.idea.focus();
});
document.querySelector('#copy-message').addEventListener('click', async () => {
  const status = document.querySelector('#copy-status');
  try { await navigator.clipboard.writeText(preparedMessage); status.textContent = 'Mensaje copiado. Puedes pegarlo en tu conversación.'; }
  catch { status.textContent = 'No pudimos copiarlo automáticamente. Puedes seleccionar y copiar el mensaje de arriba.'; }
});
document.querySelector('.toolbar-brand').addEventListener('click', () => demoDialog.close());
document.querySelector('#year').textContent = new Date().getFullYear();
renderGallery();
