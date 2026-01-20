# 7_googleslides - Google Slides API連携

## 概要

Google Slides APIを使用してMarkdownからGoogleスライドを直接生成。

## ディレクトリ構成

```
7_googleslides/
├── 1_input/           # 入力Markdown
├── 2_slides/          # 変換用中間ファイル
├── 3_output/          # 生成されたスライドURL
├── scripts/
│   └── md_to_gslides.py   # 変換スクリプト
├── credentials/       # Google API認証情報（.gitignore）
├── .claude/
│   └── commands/
└── CLAUDE.md          # 本ファイル
```

## セットアップ

### 1. Google Cloud プロジェクト作成

1. [Google Cloud Console](https://console.cloud.google.com/) にアクセス
2. 新規プロジェクト作成
3. 「APIとサービス」→「APIを有効にする」
4. 「Google Slides API」を有効化
5. 「Google Drive API」を有効化

### 2. OAuth認証情報の作成

1. 「APIとサービス」→「認証情報」
2. 「認証情報を作成」→「OAuthクライアントID」
3. アプリケーションの種類：「デスクトップアプリ」
4. JSONファイルをダウンロード
5. `credentials/client_secret.json` として保存

### 3. Python依存関係インストール

```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

## 使い方

### 基本コマンド

```bash
python scripts/md_to_gslides.py 1_input/slides.md "プレゼンタイトル"
```

### 初回実行時

ブラウザが開いてGoogle認証を求められます。許可すると `credentials/token.json` が生成されます。

## Markdown形式

```markdown
# スライドタイトル

---

# スライド1のタイトル

- 箇条書き1
- 箇条書き2

---

# スライド2のタイトル

本文テキスト
```

## 制限事項

- 画像の埋め込みは別途処理が必要
- 複雑なレイアウトは非対応
- API利用制限あり（1日あたりのリクエスト数）

## 代替方法: PPTXインポート

より簡単な方法として、Marpで生成したPPTXをGoogleスライドにインポート：

1. Marpでスライド生成（アプローチ1-4）
2. `marp slides.md --pptx -o slides.pptx`
3. Google Driveにアップロード
4. 「Googleスライドで開く」を選択

## 依存

- Python 3.x
- google-api-python-client
- google-auth-oauthlib
