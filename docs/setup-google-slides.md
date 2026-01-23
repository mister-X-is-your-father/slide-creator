# Google Slides API セットアップ手順

## 1. Google Cloud Console でプロジェクト作成

1. [Google Cloud Console](https://console.cloud.google.com/) にアクセス
2. 新しいプロジェクトを作成（または既存のものを選択）

## 2. Google Slides API を有効化

1. 「APIとサービス」→「ライブラリ」
2. 「Google Slides API」を検索して有効化
3. 「Google Drive API」も有効化（ファイル作成に必要）

## 3. OAuth 2.0 認証情報を作成

1. 「APIとサービス」→「認証情報」
2. 「認証情報を作成」→「OAuth クライアント ID」
3. アプリケーションの種類: 「デスクトップアプリ」
4. 名前を入力して「作成」
5. JSONをダウンロード → `credentials.json` として保存

## 4. credentials.json を配置

```bash
# プロジェクトルートに配置
cp ~/Downloads/client_secret_xxx.json /path/to/slide-creator/credentials.json

# または .credentials/ ディレクトリに配置
mkdir -p /path/to/slide-creator/.credentials
cp ~/Downloads/client_secret_xxx.json /path/to/slide-creator/.credentials/credentials.json
```

## 5. 初回認証

```bash
# エクスポートスクリプトを実行
python3 scripts/export_gslides.py 2_create/sample_presentation.md --mode new

# ブラウザが開くので、Googleアカウントでログイン
# 「このアプリはGoogleで確認されていません」と表示されたら
# 「詳細」→「（安全ではないページ）に移動」で進む
```

## 6. トークンの保存場所

認証後、トークンは以下に保存されます：
```
~/.slide-creator/token.pickle
```

## トラブルシューティング

### 「credentials.json が見つかりません」エラー

```bash
# ファイルの存在確認
ls -la credentials.json

# パスを指定して実行
python3 scripts/export_gslides.py --credentials /path/to/credentials.json
```

### 「アクセスがブロックされました」エラー

1. Google Cloud Console で OAuth 同意画面を設定
2. テストユーザーに自分のメールを追加

### 認証をやり直したい場合

```bash
rm ~/.slide-creator/token.pickle
python3 scripts/export_gslides.py ...
```

## 必要なPythonパッケージ

```bash
pip install google-api-python-client google-auth-oauthlib google-auth-httplib2
```
