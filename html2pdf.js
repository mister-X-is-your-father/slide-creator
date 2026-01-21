const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 720 });
  
  const htmlPath = path.resolve(__dirname, process.argv[2]);
  console.log('Loading:', htmlPath);
  await page.goto('file://' + htmlPath, { waitUntil: 'networkidle0' });
  
  const outPath = path.resolve(__dirname, process.argv[3]);
  await page.pdf({
    path: outPath,
    width: '1280px',
    height: '720px',
    printBackground: true
  });
  
  await browser.close();
  console.log('PDF generated:', outPath);
})();
