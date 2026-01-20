---
marp: true
theme: default
paginate: true
footer: 'Subagentsによる自動化'
style: |
  section {
    font-family: 'Noto Sans CJK JP', 'Noto Sans JP', sans-serif;
  }
---

# Subagentsによる自動化

3つのエージェントで品質を安定化

---

# アジェンダ

1. Subagentsとは
2. 3つのエージェント
3. ワークフロー
4. まとめ

---

# Subagentsとは

役割を分担した専門エージェント

- 自然言語でトリガー
- 各エージェントが専門タスクを実行
- 品質が安定する

---

# create-agent

スライド作成を担当

- 下書きを読み込み
- Marp形式に変換
- 構成を自動決定

**トリガー**: 「スライドを作成して」

---

# review-agent

品質チェックを担当

- 構文チェック
- 文字数検証（タイトル30文字以内など）
- 改善提案を出力

**トリガー**: 「スライドをレビューして」

---

# build-agent

ビルドを担当

- HTML出力
- PDF出力
- エラーハンドリング

**トリガー**: 「スライドをビルドして」

---

# ワークフロー

```
「スライドを作成して」
    ↓
create-agent: 1_input → 2_slides
    ↓
「スライドをレビューして」
    ↓
review-agent: 検証・改善提案
    ↓
「スライドをビルドして」
    ↓
build-agent: 2_slides → 3_output
```

---

# まとめ

- 3つのエージェントで役割分担
- 自然言語でトリガー
- 品質が安定する

---

# ご清聴ありがとうございました
