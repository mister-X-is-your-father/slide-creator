# create-slide

1_input/draft.md の内容を読み取り、Marp形式のスライドを 2_slides/slides.md に生成する。

## 手順

1. `1_input/draft.md` を読み込む
2. 内容を分析し、適切なスライド構成を決定
3. `theme/components.css` のコンポーネントを活用
4. `.claude/slide_rules.mdc` のルールに従う
5. `2_slides/slides.md` に出力

## 出力フォーマット

```markdown
---
marp: true
theme: custom
paginate: true
header: 'ヘッダー'
footer: 'フッター'
style: |
  @import './theme/theme.css';
  @import './theme/components.css';
---

（スライド内容）
```

## 制約

- タイトル: 最大30文字
- リード文: 最大2行
- 箇条書き: 1項目25文字以内、最大5項目
- 1スライド1メッセージ
