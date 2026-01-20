# generate-image

スライド内のMermaid記法から画像を生成する。

## 手順

1. `2_slides/slides.md` を読み込む
2. Mermaid記法のブロックを抽出
3. 各Mermaidブロックに対して画像生成
4. `images/` に保存
5. スライド内の参照を更新

## コマンド例

```bash
cd 4_marp_ai_image

# 単一画像生成
python scripts/gemini_image.py \
  --prompt "プロフェッショナルなフローチャート、青系カラー" \
  --mermaid mermaid/flowchart.mmd \
  --output images/flowchart.png

# スライド内の画像参照を更新
# ```mermaid ... ``` を ![](images/xxx.png) に置換
```

## プロンプトテンプレート

### フローチャート用

```
以下のフローチャートをプレゼンテーション用の美しい図解として生成してください。

スタイル: ミニマル、プロフェッショナル
カラー: 青系グラデーション (#2563eb → #1d4ed8)
背景: 白
フォント: サンセリフ、読みやすい
```

### アーキテクチャ図用

```
以下のシステムアーキテクチャをプレゼンテーション用の図解として生成してください。

スタイル: モダン、クリーン
アイコン: シンプルな線画アイコン
接続線: 矢印付き、グレー
コンポーネント: 角丸四角形、影付き
```

### タイムライン用

```
以下のスケジュールをプレゼンテーション用のタイムライン図として生成してください。

スタイル: 水平タイムライン
マイルストーン: 丸いマーカー
期間: グラデーションバー
ラベル: 上下交互に配置
```

## 依存

- Python 3.x
- google-generativeai (`pip install google-generativeai`)
- GOOGLE_API_KEY 環境変数
