# コンテンツ詳細化プロンプト

以下のページについて、詳細な本文とイラスト指示を作成してください。

## ページ情報
- ページ番号: {page_number}
- タイプ: {type}
- セクション: {section}
- 概要: {summary}

## 要件
1. 本文は指定文字数に収める
2. 会話がある場合は自然なやり取りに
3. イラスト指示は具体的に（位置、表情、動作）
4. 感情の動きを明確に表現

## 出力形式
以下のJSON形式で出力してください:

```json
{
  "page_number": 1,
  "text": "本文テキスト",
  "dialogue": [
    {
      "character": "キャラ名",
      "text": "セリフ"
    }
  ],
  "illustration": {
    "description": "全体説明",
    "characters": [
      {
        "name": "キャラ名",
        "position": "left/center/right",
        "expression": "表情",
        "action": "動作"
      }
    ],
    "background": "背景詳細"
  },
  "emphasis": ["強調するテキスト"]
}
```
