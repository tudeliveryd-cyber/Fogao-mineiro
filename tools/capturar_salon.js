// Telas do modo Salón (mesas/canchas) com fotos, para artes. Roda no GitHub Actions.
const { chromium } = require('playwright');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');
const OUT = path.join(ROOT, 'tools', 'telas', 'salon');
const DEMO = 'file://' + path.join(ROOT, 'araujo-tech-site', 'demo', 'index.html');
async function waitImages(p) {
  await p.waitForLoadState('networkidle').catch(() => {});
  await p.evaluate(async () => { document.querySelectorAll('img[loading]').forEach(i => (i.loading = 'eager'));
    await Promise.all([...document.images].map(i => (i.complete ? 0 : new Promise(r => { i.onload = i.onerror = r; setTimeout(r, 8000); })))); });
  await p.waitForTimeout(900);
}
const FAKE = () => { window.TDC_FAKE_CLOUD = new Proxy({ getShop: async () => null, listReviews: async () => [], placeOrder: async () => ({ id: 'o1', no: 1042 }), watchTrack: () => () => {} },
  { get: (t, k) => k === 'then' ? undefined : k in t ? t[k] : (() => Promise.resolve(null)) }); };
(async () => {
  const b = await chromium.launch();
  const mk = async () => { const c = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 3, isMobile: true, hasTouch: true }); return c; };
  // catálogo na quadra
  let ctx = await mk(); await ctx.addInitScript(FAKE); let p = await ctx.newPage();
  await p.goto(DEMO + '?ver=catalogo&mesa=3'); await p.evaluate(() => { pub.store.tables = 6; pub.store.tableWord = 'cancha'; pub.store.service = 'mozo'; render() });
  await waitImages(p); await p.screenshot({ path: path.join(OUT, 'cat-mesa.jpg'), quality: 92 });
  await p.evaluate(() => scrollTo(0, 520)); await waitImages(p); await p.screenshot({ path: path.join(OUT, 'cat-menu.jpg'), quality: 92 });
  // checkout
  await p.evaluate(() => { const ids = pub.products.filter(q => !(q.g && q.g.length) && q.on !== false).slice(0, 3).map(q => q.id); cart = ids.map((pid, i) => ({ pid, q: i ? 1 : 2, opts: {}, note: '' })); saveCart(); ck.name = 'Juan'; ck.pay = 'cash'; checkoutSheet() });
  await p.waitForTimeout(700); await p.screenshot({ path: path.join(OUT, 'cat-checkout.jpg'), quality: 92 });
  await p.evaluate(() => { acts.close(); scrollTo(0, 0); readyAlert({ mode: 'mesa', no: 1042, status: 'pronto' }) }); await p.waitForTimeout(700);
  await p.screenshot({ path: path.join(OUT, 'cat-listo.jpg'), quality: 92 });
  await ctx.close();
  // painel: salón e cozinha
  ctx = await mk(); p = await ctx.newPage(); p.on('dialog', d => d.accept());
  await p.goto(DEMO + '#painel'); await p.waitForTimeout(1200);
  await p.evaluate(() => {
    applyBoth(c => { c.store.tables = 6; c.store.tableWord = 'cancha'; c.store.tables2 = 10; c.store.tableWord2 = 'mesa'; c.store.service = 'mozo'; c.store.mozoPct = '5' }); S.set(K.auth, true);
    const P = pub.products.filter(q => q.on !== false).map(q => q.n.es || q.n.pt); const now = Date.now();
    const mk = (no, mesa, st, name, items, tot, mins, pay, chg, mozo) => ({ id: 'x' + no, no, date: new Date(now - mins * 60e3).toISOString(), mode: 'mesa', mesa, canal: 'mesa', name, lines: items.map(([q, i]) => ({ q, n: P[i % P.length], ex: [], note: '' })), items: [], total: tot, pay, change: chg || '', status: st, mozo });
    orders = [mk(1046, 'C3', 'aguardando', 'Juan', [[2, 0], [1, 5]], 98000, 1, 'cash'), mk(1045, 'M7', 'preparo', 'Laura', [[1, 2], [2, 7]], 76000, 6, 'transfer'), mk(1044, 'C1', 'preparo', 'Diego', [[3, 4]], 54000, 9, 'pix'),
      mk(1043, 'C3', 'pronto', 'Juan', [[4, 8], [2, 9]], 64000, 12, 'cash', '100000'), mk(1041, 'C5', 'pronto', 'Marcos', [[1, 1], [3, 9]], 87000, 14, 'transfer'),
      mk(1040, 'M2', 'retirado', 'Ana', [[2, 3]], 70000, 30, 'cash', '', 'pedro'), mk(1039, 'C2', 'retirado', '', [[6, 9]], 60000, 40, 'cash', '', 'juan')];
    CALLS = [{ id: 'c1', call: 'cuenta', mesa: 'C2', pay: 'transfer', name: 'Rodrigo', date: new Date(now - 2 * 60e3).toISOString(), status: 'aguardando' }];
    ui.view = 'admin'; ui.tab = 'salon'; render() });
  await waitImages(p); await p.screenshot({ path: path.join(OUT, 'salon.jpg'), quality: 92 });
  await p.evaluate(() => { const e = [...document.querySelectorAll('#tabBody .card h3')].find(h => /Listos/.test(h.textContent)); e && e.scrollIntoView() }); await p.waitForTimeout(400);
  await p.screenshot({ path: path.join(OUT, 'salon-listos.jpg'), quality: 92 });
  await p.evaluate(() => { ui.tab = 'cocina'; render(); scrollTo(0, 0) }); await p.waitForTimeout(500); await p.screenshot({ path: path.join(OUT, 'cocina.jpg'), quality: 92 });
  await p.setViewportSize({ width: 1280, height: 800 }); await p.evaluate(() => { ui.tab = 'salon'; ui.tv = true; render() }); await p.waitForTimeout(500);
  await p.screenshot({ path: path.join(OUT, 'tv.jpg'), quality: 92 });
  await b.close();
})();
