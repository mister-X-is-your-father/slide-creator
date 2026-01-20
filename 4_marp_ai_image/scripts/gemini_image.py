#!/usr/bin/env python3
"""
Gemini API を使用した画像生成スクリプト

使用方法:
    python gemini_image.py --prompt "画像の説明" --output images/output.png

環境変数:
    GOOGLE_API_KEY: Gemini API キー
"""

import argparse
import os
import sys

try:
    import google.generativeai as genai
except ImportError:
    print("Error: google-generativeai がインストールされていません")
    print("pip install google-generativeai を実行してください")
    sys.exit(1)


def generate_image(prompt: str, output_path: str) -> bool:
    """
    Gemini API で画像を生成

    Args:
        prompt: 画像生成プロンプト
        output_path: 出力ファイルパス

    Returns:
        成功した場合 True
    """
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY 環境変数を設定してください")
        return False

    genai.configure(api_key=api_key)

    # Imagen モデルを使用
    # 注: 実際のモデル名は API バージョンによって異なる場合があります
    try:
        model = genai.ImageGenerationModel("imagen-3.0-generate-001")
        result = model.generate_images(
            prompt=prompt,
            number_of_images=1,
            aspect_ratio="16:9",  # プレゼン用
        )

        # 画像を保存
        if result.images:
            image = result.images[0]
            image.save(output_path)
            print(f"画像を保存しました: {output_path}")
            return True
        else:
            print("Error: 画像が生成されませんでした")
            return False

    except Exception as e:
        print(f"Error: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Gemini API で画像を生成")
    parser.add_argument("--prompt", "-p", required=True, help="画像生成プロンプト")
    parser.add_argument("--output", "-o", required=True, help="出力ファイルパス")
    parser.add_argument("--mermaid", "-m", help="Mermaidコードファイル（プロンプトに追加）")

    args = parser.parse_args()

    prompt = args.prompt

    # Mermaidコードがあれば追加
    if args.mermaid and os.path.exists(args.mermaid):
        with open(args.mermaid, "r") as f:
            mermaid_code = f.read()
        prompt = f"{prompt}\n\n以下の構造を参考にしてください:\n```mermaid\n{mermaid_code}\n```"

    success = generate_image(prompt, args.output)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
