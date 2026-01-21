#!/usr/bin/env python3
"""
Google Slides API service for creating and managing presentations
"""

import json
import os
from googleapiclient.discovery import build
from .auth import authenticate


def hex_to_rgb(hex_color):
    """Convert hex color to RGB dict for Google Slides API"""
    hex_color = hex_color.lstrip('#')
    return {
        'red': int(hex_color[0:2], 16) / 255.0,
        'green': int(hex_color[2:4], 16) / 255.0,
        'blue': int(hex_color[4:6], 16) / 255.0
    }


class GoogleSlidesService:
    """Service class for Google Slides API operations"""

    def __init__(self, credentials=None):
        """
        Initialize the service

        Args:
            credentials: Google credentials object. If None, will authenticate.
        """
        if credentials is None:
            credentials = authenticate()
        self.service = build('slides', 'v1', credentials=credentials)

    def create_presentation(self, title):
        """
        Create a new empty presentation

        Args:
            title: Presentation title

        Returns:
            Presentation ID
        """
        presentation = self.service.presentations().create(body={
            'title': title
        }).execute()
        return presentation['presentationId']

    def batch_update(self, presentation_id, requests):
        """
        Execute batch update requests

        Args:
            presentation_id: Target presentation ID
            requests: List of update requests
        """
        self.service.presentations().batchUpdate(
            presentationId=presentation_id,
            body={'requests': requests}
        ).execute()

    def get_presentation_url(self, presentation_id):
        """Get the URL for a presentation"""
        return f"https://docs.google.com/presentation/d/{presentation_id}"

    def create_slide(self, slide_id, layout='BLANK'):
        """
        Create a slide request

        Args:
            slide_id: Unique ID for the slide
            layout: Predefined layout type

        Returns:
            Request dict
        """
        return {
            'createSlide': {
                'objectId': slide_id,
                'slideLayoutReference': {'predefinedLayout': layout}
            }
        }

    def create_shape(self, object_id, page_id, shape_type, x, y, width, height):
        """
        Create a shape request

        Args:
            object_id: Unique ID for the shape
            page_id: Parent slide ID
            shape_type: RECTANGLE, ELLIPSE, TEXT_BOX, etc.
            x, y: Position in EMU
            width, height: Size in EMU

        Returns:
            Request dict
        """
        return {
            'createShape': {
                'objectId': object_id,
                'shapeType': shape_type,
                'elementProperties': {
                    'pageObjectId': page_id,
                    'size': {
                        'width': {'magnitude': width, 'unit': 'EMU'},
                        'height': {'magnitude': height, 'unit': 'EMU'}
                    },
                    'transform': {
                        'scaleX': 1, 'scaleY': 1,
                        'translateX': x,
                        'translateY': y,
                        'unit': 'EMU'
                    }
                }
            }
        }

    def insert_text(self, object_id, text):
        """
        Create an insert text request

        Args:
            object_id: Target text box ID
            text: Text to insert

        Returns:
            Request dict
        """
        return {
            'insertText': {
                'objectId': object_id,
                'text': text,
                'insertionIndex': 0
            }
        }

    def update_text_style(self, object_id, font_size, color_hex, bold=False):
        """
        Create a text style update request

        Args:
            object_id: Target text box ID
            font_size: Font size in PT
            color_hex: Text color in hex format
            bold: Whether text is bold

        Returns:
            Request dict
        """
        rgb = hex_to_rgb(color_hex)
        return {
            'updateTextStyle': {
                'objectId': object_id,
                'style': {
                    'bold': bold,
                    'fontSize': {'magnitude': font_size, 'unit': 'PT'},
                    'foregroundColor': {'opaqueColor': {'rgbColor': rgb}}
                },
                'fields': 'bold,fontSize,foregroundColor'
            }
        }

    def update_paragraph_style(self, object_id, alignment='START'):
        """
        Create a paragraph style update request

        Args:
            object_id: Target text box ID
            alignment: START, CENTER, END, JUSTIFIED

        Returns:
            Request dict
        """
        return {
            'updateParagraphStyle': {
                'objectId': object_id,
                'style': {'alignment': alignment},
                'fields': 'alignment'
            }
        }

    def update_shape_background(self, object_id, color_hex, alpha=1.0):
        """
        Create a shape background update request

        Args:
            object_id: Target shape ID
            color_hex: Background color in hex format
            alpha: Opacity (0.0 - 1.0)

        Returns:
            Request dict
        """
        rgb = hex_to_rgb(color_hex)
        return {
            'updateShapeProperties': {
                'objectId': object_id,
                'shapeProperties': {
                    'shapeBackgroundFill': {
                        'solidFill': {'color': {'rgbColor': rgb}, 'alpha': alpha}
                    },
                    'outline': {'outlineFill': {'solidFill': {'color': {'rgbColor': rgb}}}}
                },
                'fields': 'shapeBackgroundFill,outline'
            }
        }


def load_template(template_name, templates_dir='templates/slides'):
    """
    Load template configuration from JSON file

    Args:
        template_name: Template name (without .json extension)
        templates_dir: Directory containing template files

    Returns:
        Template config dict
    """
    template_path = os.path.join(templates_dir, f'{template_name}.json')
    with open(template_path, 'r', encoding='utf-8') as f:
        return json.load(f)
