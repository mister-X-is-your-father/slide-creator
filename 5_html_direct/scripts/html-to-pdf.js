#!/usr/bin/env node
/**
 * HTML to PDF 変換スクリプト
 *
 * 使用方法:
 *   node html-to-pdf.js input.html output.pdf
 *
 * 依存:
 *   npm install puppeteer
 */

const puppeteer = require("puppeteer");
const path = require("path");
const fs = require("fs");

async function htmlToPdf(inputPath, outputPath) {
  // 入力ファイルの存在確認
  if (!fs.existsSync(inputPath)) {
    console.error(`Error: ${inputPath} が見つかりません`);
    process.exit(1);
  }

  // 絶対パスに変換
  const absoluteInputPath = path.resolve(inputPath);
  const absoluteOutputPath = path.resolve(outputPath);

  console.log(`変換中: ${absoluteInputPath} → ${absoluteOutputPath}`);

  const browser = await puppeteer.launch({
    headless: "new",
    args: ["--no-sandbox", "--disable-setuid-sandbox"],
  });

  try {
    const page = await browser.newPage();

    // HTMLファイルを読み込み
    await page.goto(`file://${absoluteInputPath}`, {
      waitUntil: "networkidle0",
    });

    // PDF設定
    await page.pdf({
      path: absoluteOutputPath,
      format: "A4",
      landscape: true, // 横向き（16:9に近い）
      printBackground: true,
      margin: {
        top: "0",
        right: "0",
        bottom: "0",
        left: "0",
      },
    });

    console.log(`完了: ${absoluteOutputPath}`);
  } finally {
    await browser.close();
  }
}

// メイン処理
const args = process.argv.slice(2);

if (args.length < 2) {
  console.log("使用方法: node html-to-pdf.js <input.html> <output.pdf>");
  console.log("例: node html-to-pdf.js 2_artifacts/slides.html 3_output/slides.pdf");
  process.exit(1);
}

const [inputPath, outputPath] = args;

htmlToPdf(inputPath, outputPath).catch((error) => {
  console.error("Error:", error);
  process.exit(1);
});
