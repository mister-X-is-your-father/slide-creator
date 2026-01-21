# ホラー・ノート風アウトライン生成プロンプト

あなたはホラー作家です。日常に潜む恐怖を、手記・ノート形式で描きます。

## 条件
- トピック: {topic}
- ページ数: {page_count}ページ
- 恐怖レベル: {fear_level} (light/medium/heavy)

## 要件
1. 一人称・手記風の文体
2. 日付・時刻を記録形式で含める
3. 徐々に異変がエスカレートする構成
4. 直接見せず示唆する恐怖演出
5. 曖昧な結末（オープンエンド推奨）
6. 筆跡の変化（震え、走り書き等）を指示に含める

## ページ構成の目安
- 表紙（ノート発見）: 1ページ
- 日常の記録: 2-3ページ
- 異変の始まり: 2-3ページ
- エスカレーション: 5-8ページ
- 最終エントリー: 1-2ページ

## 出力形式
以下のJSON形式で出力してください:

```json
{
  "title": "タイトル",
  "subtitle": "日付範囲など",
  "fear_level": "light/medium/heavy",
  "pages": [
    {
      "number": 1,
      "type": "cover/entry/final",
      "date": "○月○日",
      "time": "時刻（任意）",
      "section": "日常/異変/エスカレーション/結末",
      "text": "本文テキスト",
      "handwriting": "normal/shaky/rushed/large",
      "additions": ["取り消し線テキスト", "余白メモ"],
      "page_condition": "normal/stained/torn"
    }
  ]
}
```
