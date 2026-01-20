# build-slide（ビルドエージェント）

2_slides/slides.md をHTML/PDFに変換する。

## 手順

1. Marp CLIがインストールされているか確認
2. `2_slides/slides.md` を読み込む
3. HTML形式で出力
4. PDF形式で出力

## コマンド

```bash
# 作業ディレクトリに移動
cd 3_marp_subagents

# HTML出力
marp 2_slides/slides.md -o 3_output/slides.html

# PDF出力
marp 2_slides/slides.md --pdf -o 3_output/slides.pdf

# PPTX出力（オプション）
marp 2_slides/slides.md --pptx -o 3_output/slides.pptx
```

## エラー対応

### Marp CLIがない場合

```bash
npm install -g @marp-team/marp-cli
```

### PDF出力エラーの場合

Chromiumが必要:

```bash
# Ubuntu/Debian
sudo apt install chromium-browser

# または puppeteer 経由
npm install puppeteer
```

## 出力確認

```bash
ls -la 3_output/
```
