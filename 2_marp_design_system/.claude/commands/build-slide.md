# build-slide

2_slides/slides.md をHTML/PDFに変換して 3_output/ に出力する。

## 手順

1. Marp CLIがインストールされているか確認
2. `2_slides/slides.md` を読み込む
3. HTML形式で出力: `3_output/slides.html`
4. PDF形式で出力: `3_output/slides.pdf`

## コマンド例

```bash
# HTML出力
marp 2_slides/slides.md -o 3_output/slides.html

# PDF出力
marp 2_slides/slides.md --pdf -o 3_output/slides.pdf

# PPTX出力
marp 2_slides/slides.md --pptx -o 3_output/slides.pptx
```

## 依存

- Marp CLI (`npm install -g @marp-team/marp-cli`)
