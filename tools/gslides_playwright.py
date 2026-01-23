#!/usr/bin/env python3
"""
gslides_playwright.py - PlaywrightでGoogle Slidesを操作

スキル外のユーティリティ。ブラウザ自動化でGoogle Slidesを直接操作する。
APIより柔軟だが、UIの変更に影響を受ける可能性がある。

使い方:
    python gslides_playwright.py login          # Googleログイン（初回）
    python gslides_playwright.py create "タイトル"  # 新規作成
    python gslides_playwright.py open URL       # 既存を開く
"""

import argparse
import asyncio
import json
import os
import sys
from pathlib import Path
from playwright.async_api import async_playwright, Page, Browser

# 設定
PROJECT_ROOT = Path(__file__).parent.parent
USER_DATA_DIR = PROJECT_ROOT / ".playwright-data"
STATE_FILE = USER_DATA_DIR / "state.json"


async def get_browser(headless: bool = False):
    """ブラウザインスタンスを取得"""
    playwright = await async_playwright().start()

    # ユーザーデータを永続化（ログイン状態を保持）
    USER_DATA_DIR.mkdir(parents=True, exist_ok=True)

    browser = await playwright.chromium.launch_persistent_context(
        user_data_dir=str(USER_DATA_DIR),
        headless=headless,
        viewport={"width": 1280, "height": 800},
        locale="ja-JP"
    )

    return playwright, browser


async def login():
    """Googleにログイン（ブラウザで手動操作）"""
    print("Googleログインを開始します...")
    print("ブラウザが開きます。Googleアカウントでログインしてください。")
    print("ログイン完了後、このターミナルでEnterを押してください。")

    playwright, browser = await get_browser(headless=False)

    page = await browser.new_page()
    await page.goto("https://accounts.google.com/")

    # ユーザーがログインするのを待つ
    input("\nログイン完了後、Enterを押してください...")

    # 状態を保存
    storage_state = await browser.storage_state()
    with open(STATE_FILE, "w") as f:
        json.dump(storage_state, f)

    print(f"✓ ログイン状態を保存しました: {STATE_FILE}")

    await browser.close()
    await playwright.stop()


async def create_presentation(title: str):
    """新規プレゼンテーションを作成"""
    print(f"新規プレゼンテーション作成: {title}")

    playwright, browser = await get_browser(headless=False)

    page = await browser.new_page()

    # Google Slidesにアクセス
    await page.goto("https://docs.google.com/presentation/create")

    # ページ読み込み待ち
    await page.wait_for_load_state("networkidle")

    # タイトルを設定（タイトルボックスをクリック）
    try:
        # タイトル入力欄を探す
        title_input = page.locator('[aria-label="ドキュメントのタイトル変更"]')
        if await title_input.count() > 0:
            await title_input.click()
            await page.keyboard.type(title)
            await page.keyboard.press("Enter")
        else:
            # 別の方法で試す
            await page.keyboard.press("Control+Shift+T")  # タイトル編集ショートカット
            await page.keyboard.type(title)
            await page.keyboard.press("Enter")
    except Exception as e:
        print(f"タイトル設定に失敗（手動で設定してください）: {e}")

    url = page.url
    print(f"\n✓ プレゼンテーションを作成しました")
    print(f"  URL: {url}")

    input("\n操作が完了したらEnterを押してください...")

    await browser.close()
    await playwright.stop()

    return url


async def open_presentation(url: str):
    """既存のプレゼンテーションを開く"""
    print(f"プレゼンテーションを開きます: {url}")

    playwright, browser = await get_browser(headless=False)

    page = await browser.new_page()
    await page.goto(url)
    await page.wait_for_load_state("networkidle")

    print("\n✓ プレゼンテーションを開きました")
    print("ブラウザで操作してください。")

    input("\n操作が完了したらEnterを押してください...")

    await browser.close()
    await playwright.stop()


async def add_slide(page: Page, layout: str = "blank"):
    """スライドを追加"""
    # Ctrl+M で新規スライド追加
    await page.keyboard.press("Control+m")
    await page.wait_for_timeout(500)


async def add_text_box(page: Page, text: str, x: int = 100, y: int = 100):
    """テキストボックスを追加"""
    # 挿入メニュー → テキストボックス
    await page.keyboard.press("Alt+i")  # 挿入メニュー
    await page.wait_for_timeout(200)
    await page.keyboard.press("t")  # テキストボックス
    await page.wait_for_timeout(200)

    # クリックして配置
    await page.mouse.click(x, y)
    await page.wait_for_timeout(200)

    # テキスト入力
    await page.keyboard.type(text)


async def import_from_marp(marp_file: Path):
    """Marpファイルからスライドを作成（実験的）"""
    import re

    print(f"Marpファイルをインポート: {marp_file}")

    # Marpファイル読み込み
    with open(marp_file, "r", encoding="utf-8") as f:
        content = f.read()

    # フロントマター除去
    content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)

    # スライド分割
    slides = re.split(r'\n---\n', content)

    playwright, browser = await get_browser(headless=False)
    page = await browser.new_page()

    # 新規作成
    await page.goto("https://docs.google.com/presentation/create")
    await page.wait_for_load_state("networkidle")
    await page.wait_for_timeout(2000)

    for i, slide_content in enumerate(slides):
        slide_content = slide_content.strip()
        if not slide_content:
            continue

        if i > 0:
            # 新しいスライドを追加
            await add_slide(page)

        # タイトル抽出
        title_match = re.search(r'^##?\s+(.+)$', slide_content, re.MULTILINE)
        if title_match:
            title = title_match.group(1)
            # タイトルエリアにフォーカス（クリック）
            await page.mouse.click(640, 200)
            await page.wait_for_timeout(200)
            await page.keyboard.type(title)

        # 本文抽出
        body_lines = []
        for line in slide_content.split('\n'):
            line = line.strip()
            if line.startswith('- ') or line.startswith('* '):
                body_lines.append(line[2:])
            elif line and not line.startswith('#') and not line.startswith('<'):
                body_lines.append(line)

        if body_lines:
            # 本文エリアにフォーカス
            await page.mouse.click(640, 400)
            await page.wait_for_timeout(200)
            for line in body_lines:
                await page.keyboard.type(f"• {line}")
                await page.keyboard.press("Enter")

        await page.wait_for_timeout(500)

    url = page.url
    print(f"\n✓ インポート完了")
    print(f"  URL: {url}")
    print(f"  スライド数: {len([s for s in slides if s.strip()])}")

    input("\n確認が完了したらEnterを押してください...")

    await browser.close()
    await playwright.stop()

    return url


def main():
    parser = argparse.ArgumentParser(
        description="PlaywrightでGoogle Slidesを操作"
    )
    subparsers = parser.add_subparsers(dest="command", help="コマンド")

    # login
    subparsers.add_parser("login", help="Googleにログイン")

    # create
    create_parser = subparsers.add_parser("create", help="新規プレゼンテーション作成")
    create_parser.add_argument("title", help="プレゼンテーションのタイトル")

    # open
    open_parser = subparsers.add_parser("open", help="既存のプレゼンテーションを開く")
    open_parser.add_argument("url", help="プレゼンテーションのURL")

    # import
    import_parser = subparsers.add_parser("import", help="MarpファイルをGoogle Slidesにインポート")
    import_parser.add_argument("file", help="Marpファイルパス")

    args = parser.parse_args()

    if args.command == "login":
        asyncio.run(login())
    elif args.command == "create":
        asyncio.run(create_presentation(args.title))
    elif args.command == "open":
        asyncio.run(open_presentation(args.url))
    elif args.command == "import":
        asyncio.run(import_from_marp(Path(args.file)))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
