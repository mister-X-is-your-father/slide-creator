"""
Google Slides API integration for slide-creator

Usage:
    from googleslides import PresentationBuilder

    # Create presentation using template
    builder = PresentationBuilder(template_name='business-proposal')
    builder.add_title_slide("プロジェクト提案", "2025年度")
    builder.add_section_slide("01", "はじめに", "概要説明")
    builder.add_content_slide("背景", ["課題1", "課題2", "課題3"])

    # Build and get URL
    presentation_id, url = builder.build("My Presentation")
    print(f"Created: {url}")
"""

from .auth import authenticate
from .slides_service import GoogleSlidesService, load_template, hex_to_rgb
from .presentation_builder import PresentationBuilder

__all__ = [
    'authenticate',
    'GoogleSlidesService',
    'PresentationBuilder',
    'load_template',
    'hex_to_rgb',
]
