# 1_marp_basic - 基本Marpアプローチ

## 概要

VSCode + Marp拡張機能を使用したシンプルなスライド生成。

## ディレクトリ構成

```
1_marp_basic/
├── 1_input/       # 下書き・アイデア
├── 2_slides/      # Marp形式スライド
├── 3_output/      # HTML/PDF出力
└── CLAUDE.md      # 本ファイル
```

## ワークフロー

1. `1_input/draft.md` に内容を記述
2. Claudeに変換を依頼 → `2_slides/slides.md`
3. VSCode Marp拡張でプレビュー・調整
4. エクスポート → `3_output/`

## Marp基本構文

```markdown
---
marp: true
theme: default
paginate: true
header: 'タイトル'
footer: '発表者名 | 日付'
---

# スライドタイトル

内容

---

# 次のスライド

- 箇条書き1
- 箇条書き2
```

## スライドルール

- タイトル: 最大30文字
- リード文: 最大2行
- 箇条書き: 1項目25文字以内、最大5項目
- 1スライド1メッセージ

## 依存ツール

- VSCode
- Marp for VS Code拡張機能
