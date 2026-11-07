// Tira as telas das demos COM as fotos (roda no GitHub Actions, que tem internet).
// Saída: araujo-tech-site/img/sistemas/{catalogo,farmacia}-{pc,cel}.jpg e tools/telas/*.png (para artes)
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const ROOT = path.resolve(__dirname, '..');
const OUT = path.join(ROOT, 'araujo-tech-site', 'img', 'sistemas');
const RAW = path.join(ROOT, 'tools', 'telas');
fs.mkdirSync(RAW, { recursive: true });

const DEMOS = [
  { id: 'catalogo', file: 'araujo-tech-site/demo/index.html' },
  { id: 'farmacia', file: 'araujo-tech-site/demo-farmacia/index.html' },
];

async function waitImages(p) {
  await p.waitForLoadState('networkidle').catch(() => {});
  await p.evaluate(async () => {
    document.querySelectorAll('img[loading]').forEach(i => (i.loading = 'eager'));
    const imgs = [...document.images];
    await Promise.all(imgs.map(i => (i.complete ? 0 : new Promise(r => { i.onload = i.onerror = r; setTimeout(r, 8000); }))));
  });
  await p.waitForTimeout(800);
}

(async () => {
  const b = await chromium.launch();
  for (const d of DEMOS) {
    const url = 'file://' + path.join(ROOT, d.file);
    // computador
    let p = await (await b.newContext({ viewport: { width: 1280, height: 800 }, deviceScaleFactor: 1 })).newPage();
    await p.goto(url); await p.addStyleTag({ content: '#top{display:none!important}' });
    await waitImages(p);
    await p.screenshot({ path: path.join(OUT, d.id + '-pc.jpg'), type: 'jpeg', quality: 84 });
    await p.context().close();
    p = await (await b.newContext({ viewport: { width: 1280, height: 800 }, deviceScaleFactor: 2 })).newPage();
    await p.goto(url); await p.addStyleTag({ content: '#top{display:none!important}' });
    await waitImages(p);
    await p.screenshot({ path: path.join(RAW, d.id + '-pc.png') });
    await p.context().close();
    // celular
    p = await (await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 600 / 390, isMobile: true, hasTouch: true })).newPage();
    await p.goto(url); await p.addStyleTag({ content: '#top{display:none!important}' });
    await waitImages(p);
    await p.screenshot({ path: path.join(OUT, d.id + '-cel.jpg'), type: 'jpeg', quality: 84 });
    await p.context().close();
    p = await (await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 3, isMobile: true, hasTouch: true })).newPage();
    await p.goto(url); await p.addStyleTag({ content: '#top{display:none!important}' });
    await waitImages(p);
    await p.screenshot({ path: path.join(RAW, d.id + '-cel.png') });
    // celular rolado até os produtos (para artes)
    await p.evaluate(() => { const s = document.querySelector('.cbody'); window.scrollTo(0, (s ? s.getBoundingClientRect().top + scrollY : 500) + 380); });
    await p.waitForTimeout(600);
    await p.screenshot({ path: path.join(RAW, d.id + '-cel-produtos.png') });
    await p.context().close();
    console.log('ok', d.id);
  }
  // Todas as demos por ramo: tela do celular (para o manual) + lista de fotos que não carregaram
  const RUB = path.join(RAW, 'rubros'); fs.mkdirSync(RUB, { recursive: true });
  const broken = [];
  const all = fs.readdirSync(path.join(ROOT, 'araujo-tech-site')).filter(x => x.startsWith('demo')).sort();
  for (const dir of all) {
    const p = await (await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true })).newPage();
    await p.goto('file://' + path.join(ROOT, 'araujo-tech-site', dir, 'index.html'));
    await p.addStyleTag({ content: '#top{display:none!important}' });
    await waitImages(p);
    await p.screenshot({ path: path.join(RUB, dir + '.jpg'), type: 'jpeg', quality: 82 });
    await p.evaluate(() => { const s = document.querySelector('.cbody'); window.scrollTo(0, (s ? s.getBoundingClientRect().top + scrollY : 500) + 380); });
    await p.waitForTimeout(400); await waitImages(p);
    await p.screenshot({ path: path.join(RUB, dir + '-produtos.jpg'), type: 'jpeg', quality: 82 });
    // percorre a página inteira para carregar todas as fotos e testa cada uma
    const bad = await p.evaluate(async () => {
      for (let y = 0; y < document.body.scrollHeight; y += 600) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 150)); }
      document.querySelectorAll('img').forEach(i => (i.loading = 'eager'));
      await Promise.all([...document.images].map(i => (i.complete ? 0 : new Promise(r => { i.onload = i.onerror = r; setTimeout(r, 8000); }))));
      return [...document.images].filter(i => /unsplash/.test(i.src) && i.naturalWidth === 0).map(i => i.src.split('?')[0]);
    });
    bad.forEach(u => broken.push(dir + ' ' + u));
    await p.context().close();
    console.log('ok', dir, bad.length, 'fotos com erro');
  }
  fs.writeFileSync(path.join(RUB, 'fotos-com-erro.txt'), broken.join('\n') + '\n');
  await b.close();
})();
