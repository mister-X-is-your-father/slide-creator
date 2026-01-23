#!/usr/bin/env python3
"""
google_auth_playwright.py - PlaywrightでGoogle OAuth認証を自動化

OAuth認証フローをブラウザで自動/半自動で実行し、
Google Slides APIのトークンを取得する。

使い方:
    # 初回認証（ブラウザが開いてログインを促す）
    python google_auth_playwright.py auth

    # 保存済み認証でトークン取得
    python google_auth_playwright.py token

    # Google Cloud Consoleで認証情報を作成（半自動）
    python google_auth_playwright.py setup-credentials
"""

import argparse
import asyncio
import json
import os
import pickle
import sys
from pathlib import Path
from urllib.parse import urlparse, parse_qs

from playwright.async_api import async_playwright

# 設定
PROJECT_ROOT = Path(__file__).parent.parent
CREDENTIALS_FILE = PROJECT_ROOT / "credentials.json"
TOKEN_FILE = Path.home() / ".slide-creator" / "token.pickle"
BROWSER_DATA_DIR = PROJECT_ROOT / ".playwright-data"

# OAuth設定
SCOPES = [
    'https://www.googleapis.com/auth/presentations',
    'https://www.googleapis.com/auth/drive.file'
]


async def setup_credentials():
    """
    Google Cloud ConsoleでOAuth認証情報を作成（半自動ガイド）
    """
    print("=" * 60)
    print("Google Cloud Console で認証情報を作成します")
    print("=" * 60)

    playwright = await async_playwright().start()
    BROWSER_DATA_DIR.mkdir(parents=True, exist_ok=True)

    browser = await playwright.chromium.launch_persistent_context(
        user_data_dir=str(BROWSER_DATA_DIR),
        headless=False,
        viewport={"width": 1400, "height": 900}
    )

    page = await browser.new_page()

    # ステップ1: Google Cloud Console
    print("\n[Step 1] Google Cloud Console にアクセス")
    await page.goto("https://console.cloud.google.com/apis/credentials")
    await page.wait_for_load_state("networkidle")

    input("\n→ Googleアカウントでログインしてください。完了したらEnterを押してください...")

    # ステップ2: プロジェクト確認
    print("\n[Step 2] プロジェクトを選択または作成")
    print("   - 画面上部のプロジェクトセレクタで選択")
    print("   - なければ「新しいプロジェクト」で作成")

    input("\n→ プロジェクト選択が完了したらEnterを押してください...")

    # ステップ3: API有効化
    print("\n[Step 3] APIを有効化")
    await page.goto("https://console.cloud.google.com/apis/library/slides.googleapis.com")
    await page.wait_for_load_state("networkidle")
    print("   - 「有効にする」ボタンをクリック")

    input("\n→ Google Slides API を有効にしたらEnterを押してください...")

    await page.goto("https://console.cloud.google.com/apis/library/drive.googleapis.com")
    await page.wait_for_load_state("networkidle")
    print("   - Google Drive API も「有効にする」")

    input("\n→ Google Drive API を有効にしたらEnterを押してください...")

    # ステップ4: OAuth同意画面
    print("\n[Step 4] OAuth同意画面を設定")
    await page.goto("https://console.cloud.google.com/apis/credentials/consent")
    await page.wait_for_load_state("networkidle")
    print("   - User Type: 「外部」を選択して「作成」")
    print("   - アプリ名、ユーザーサポートメール、デベロッパー連絡先を入力")
    print("   - スコープは追加せずに進める")
    print("   - テストユーザーに自分のメールを追加")

    input("\n→ OAuth同意画面の設定が完了したらEnterを押してください...")

    # ステップ5: 認証情報作成
    print("\n[Step 5] OAuth クライアントIDを作成")
    await page.goto("https://console.cloud.google.com/apis/credentials")
    await page.wait_for_load_state("networkidle")
    print("   - 「+ 認証情報を作成」→「OAuth クライアント ID」")
    print("   - アプリケーションの種類: 「デスクトップアプリ」")
    print("   - 名前: 任意（例: slide-creator）")
    print("   - 「作成」をクリック")

    input("\n→ OAuth クライアントIDを作成したらEnterを押してください...")

    # ステップ6: JSONダウンロード
    print("\n[Step 6] 認証情報をダウンロード")
    print("   - 作成したOAuthクライアントの右側「⬇」ボタンをクリック")
    print("   - JSONファイルがダウンロードされます")
    print(f"\n   ダウンロード後、以下にコピーしてください:")
    print(f"   → {CREDENTIALS_FILE}")

    input("\n→ JSONをダウンロードしたらEnterを押してください...")

    # 確認
    await browser.close()
    await playwright.stop()

    if CREDENTIALS_FILE.exists():
        print(f"\n✓ credentials.json を検出しました！")
        print("次のコマンドで認証を完了してください:")
        print(f"  python {__file__} auth")
    else:
        print(f"\n⚠ credentials.json が見つかりません")
        print(f"ダウンロードしたJSONを {CREDENTIALS_FILE} にコピーしてください")


async def authenticate():
    """
    OAuth認証フローを実行してトークンを取得
    """
    if not CREDENTIALS_FILE.exists():
        print(f"エラー: {CREDENTIALS_FILE} が見つかりません")
        print("先に 'python google_auth_playwright.py setup-credentials' を実行してください")
        return False

    # credentials.json読み込み
    with open(CREDENTIALS_FILE, "r") as f:
        creds_data = json.load(f)

    client_id = creds_data.get("installed", {}).get("client_id")
    client_secret = creds_data.get("installed", {}).get("client_secret")
    redirect_uri = "http://localhost:8080/"

    if not client_id:
        print("エラー: credentials.json の形式が不正です")
        return False

    # OAuth URLを構築
    scope = " ".join(SCOPES)
    auth_url = (
        f"https://accounts.google.com/o/oauth2/auth?"
        f"client_id={client_id}&"
        f"redirect_uri={redirect_uri}&"
        f"scope={scope}&"
        f"response_type=code&"
        f"access_type=offline&"
        f"prompt=consent"
    )

    print("=" * 60)
    print("Google OAuth 認証")
    print("=" * 60)
    print("\nブラウザが開きます。Googleアカウントでログインしてください。")

    playwright = await async_playwright().start()
    BROWSER_DATA_DIR.mkdir(parents=True, exist_ok=True)

    browser = await playwright.chromium.launch_persistent_context(
        user_data_dir=str(BROWSER_DATA_DIR),
        headless=False,
        viewport={"width": 1000, "height": 700}
    )

    page = await browser.new_page()
    await page.goto(auth_url)

    print("\nGoogleアカウントでログインし、アクセスを許可してください。")
    print("「このアプリはGoogleで確認されていません」と表示されたら:")
    print("  → 「詳細」→「（安全ではないページ）に移動」")

    # リダイレクト待ち（localhost:8080 にリダイレクトされるのを待つ）
    auth_code = None
    while True:
        await asyncio.sleep(1)
        current_url = page.url

        if current_url.startswith("http://localhost:8080"):
            parsed = urlparse(current_url)
            params = parse_qs(parsed.query)
            if "code" in params:
                auth_code = params["code"][0]
                break
            elif "error" in params:
                print(f"\nエラー: {params.get('error_description', params['error'])}")
                await browser.close()
                await playwright.stop()
                return False

    await browser.close()
    await playwright.stop()

    if not auth_code:
        print("認証コードの取得に失敗しました")
        return False

    print("\n✓ 認証コードを取得しました")

    # トークン交換
    import urllib.request
    import urllib.parse

    token_url = "https://oauth2.googleapis.com/token"
    token_data = urllib.parse.urlencode({
        "code": auth_code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code"
    }).encode()

    req = urllib.request.Request(token_url, data=token_data, method="POST")
    try:
        with urllib.request.urlopen(req) as response:
            token_response = json.loads(response.read().decode())
    except Exception as e:
        print(f"トークン交換エラー: {e}")
        return False

    # トークンを保存
    TOKEN_FILE.parent.mkdir(parents=True, exist_ok=True)

    # google.oauth2.credentials.Credentials 互換形式で保存
    from google.oauth2.credentials import Credentials

    creds = Credentials(
        token=token_response["access_token"],
        refresh_token=token_response.get("refresh_token"),
        token_uri="https://oauth2.googleapis.com/token",
        client_id=client_id,
        client_secret=client_secret,
        scopes=SCOPES
    )

    with open(TOKEN_FILE, "wb") as f:
        pickle.dump(creds, f)

    os.chmod(TOKEN_FILE, 0o600)

    print(f"\n✓ トークンを保存しました: {TOKEN_FILE}")
    print("\nGoogle Slides API を使用する準備が整いました！")
    print("以下のコマンドでテストできます:")
    print(f"  python scripts/export_gslides.py 2_create/sample_presentation.md --mode new")

    return True


async def check_token():
    """保存済みトークンの状態を確認"""
    if not TOKEN_FILE.exists():
        print(f"トークンファイルがありません: {TOKEN_FILE}")
        print("'python google_auth_playwright.py auth' で認証してください")
        return

    with open(TOKEN_FILE, "rb") as f:
        creds = pickle.load(f)

    print(f"トークンファイル: {TOKEN_FILE}")
    print(f"有効: {creds.valid}")
    print(f"期限切れ: {creds.expired}")
    print(f"スコープ: {creds.scopes}")

    if creds.expired and creds.refresh_token:
        print("\nトークンが期限切れです。リフレッシュしています...")
        from google.auth.transport.requests import Request
        creds.refresh(Request())

        with open(TOKEN_FILE, "wb") as f:
            pickle.dump(creds, f)
        print("✓ トークンをリフレッシュしました")


def main():
    parser = argparse.ArgumentParser(
        description="PlaywrightでGoogle OAuth認証を自動化"
    )
    subparsers = parser.add_subparsers(dest="command", help="コマンド")

    subparsers.add_parser("setup-credentials", help="Google Cloud Consoleで認証情報を作成（ガイド付き）")
    subparsers.add_parser("auth", help="OAuth認証を実行してトークンを取得")
    subparsers.add_parser("token", help="保存済みトークンの状態を確認")

    args = parser.parse_args()

    if args.command == "setup-credentials":
        asyncio.run(setup_credentials())
    elif args.command == "auth":
        asyncio.run(authenticate())
    elif args.command == "token":
        asyncio.run(check_token())
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
