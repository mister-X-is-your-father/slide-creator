# create-slide（作成エージェント）

1_input/draft.md の内容をMarp形式のスライドに変換する。

## 手順

1. `1_input/draft.md` を読み込む
2. `.claude/skills/marp/skill.md` を参照
3. 内容を分析し、適切なスライド構成を決定
4. Marp形式で `2_slides/slides.md` に出力

## 出力フォーマット

```markdown
---
marp: true
theme: default
paginate: true
header: ''
footer: ''
---

# タイトル

（内容）

---

（以降のスライド）
```

## チェックリスト

- [ ] タイトルスライドがある
- [ ] アジェンダがある
- [ ] 1スライド1メッセージ
- [ ] 文字数制限を守っている
- [ ] まとめスライドがある
