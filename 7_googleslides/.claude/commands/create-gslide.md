# create-gslide

MarkdownからGoogleスライドを生成する。

## 前提条件

1. `credentials/client_secret.json` が存在すること
2. Python依存関係がインストール済みであること

## 手順

1. `1_input/slides.md` を読み込む
2. `scripts/md_to_gslides.py` を実行
3. 生成されたURLを `3_output/slides_url.txt` に保存

## コマンド

```bash
cd 7_googleslides
python scripts/md_to_gslides.py 1_input/slides.md "プレゼンタイトル"
```

## 初回実行時

ブラウザが開いてGoogle認証を求められます：

1. Googleアカウントでログイン
2. アプリへのアクセスを許可
3. `credentials/token.json` が自動生成される

## 出力

- GoogleスライドのURL: `3_output/slides_url.txt`
