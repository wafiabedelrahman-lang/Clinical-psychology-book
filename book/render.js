// Render book/build/book.html to PDF with headless Chromium via Playwright.
// Served over a local HTTP server so fonts and styles load like a normal web page.
const { chromium } = require('playwright');
const http = require('http');
const fs = require('fs');
const path = require('path');

const TYPES = { '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.js': 'text/javascript',
  '.woff2': 'font/woff2', '.svg': 'image/svg+xml', '.png': 'image/png' };

(async () => {
  const [,, inHtml, outPdf] = process.argv;
  const root = path.resolve(path.dirname(inHtml), '..');
  const server = http.createServer((req, res) => {
    const p = path.join(root, decodeURIComponent(req.url.split('?')[0]));
    if (!p.startsWith(root) || !fs.existsSync(p)) { res.writeHead(404); return res.end(); }
    res.writeHead(200, { 'Content-Type': TYPES[path.extname(p)] || 'application/octet-stream' });
    fs.createReadStream(p).pipe(res);
  });
  await new Promise(r => server.listen(0, '127.0.0.1', r));
  const url = `http://127.0.0.1:${server.address().port}/${path.relative(root, inHtml)}`;
  const browser = await chromium.launch();
  const page = await browser.newPage();
  page.on('pageerror', e => console.error('page error:', e.message));
  await page.goto(url, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({ path: outPdf, preferCSSPageSize: true, printBackground: true, outline: true, tagged: true });
  await browser.close();
  server.close();
})().catch(e => { console.error(e); process.exit(1); });
