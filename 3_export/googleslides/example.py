#!/usr/bin/env python3
"""
Example: Create a Google Slides presentation

Usage:
    python -m googleslides.example

Prerequisites:
    1. Place credentials.json in project root (from Google Cloud Console)
    2. pip install google-auth google-auth-oauthlib google-api-python-client
"""

import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from googleslides import PresentationBuilder


def main():
    print("=" * 60)
    print("Google Slides プレゼンテーション作成")
    print("=" * 60)

    # Get user input
    print("\n📝 情報を入力してください:")
    title = input("タイトル: ").strip() or "サンプルプレゼンテーション"
    subtitle = input("サブタイトル (省略可): ").strip() or None

    # Template selection
    print("\n📋 テンプレート:")
    print("  1. default (シンプル)")
    print("  2. business-proposal (ビジネス)")
    print("  3. modern (モダン)")
    print("  4. academic (アカデミック)")
    choice = input("選択 (1-4, デフォルト: 1): ").strip() or "1"

    template_map = {
        "1": "default",
        "2": "business-proposal",
        "3": "modern",
        "4": "academic"
    }
    template_name = template_map.get(choice, "default")

    # Find templates directory
    templates_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'illustrated-curriculum-creator', 'templates', 'slides'
    )

    if not os.path.exists(templates_dir):
        print(f"❌ テンプレートディレクトリが見つかりません: {templates_dir}")
        return

    print(f"\n🔧 テンプレート: {template_name}")
    print("🔐 Google 認証中...")

    try:
        # Build presentation
        builder = PresentationBuilder(template_name=template_name, templates_dir=templates_dir)

        builder.add_title_slide(title, subtitle)
        builder.add_section_slide("01", "はじめに", "このプレゼンテーションの概要")
        builder.add_content_slide("背景", [
            "現状の課題",
            "解決すべき問題点",
            "期待される効果"
        ])
        builder.add_section_slide("02", "提案内容", "具体的な提案")
        builder.add_content_slide("アプローチ", [
            "ステップ1: 調査・分析",
            "ステップ2: 設計・開発",
            "ステップ3: テスト・検証",
            "ステップ4: 展開・運用"
        ])
        builder.add_section_slide("03", "まとめ", "結論と次のステップ")

        print("📊 プレゼンテーション作成中...")
        presentation_id, url = builder.build(title)

        print("\n✅ 完成！")
        print(f"🔗 URL: {url}")
        print(f"\n📐 スライド数: {builder.slide_count}枚")

    except FileNotFoundError as e:
        print(f"\n❌ エラー: {e}")
        print("\n💡 ヒント:")
        print("   1. Google Cloud Console で OAuth 2.0 クライアント ID を作成")
        print("   2. credentials.json をダウンロードしてプロジェクトルートに配置")
    except Exception as e:
        print(f"\n❌ エラー: {e}")
        raise


if __name__ == '__main__':
    main()
