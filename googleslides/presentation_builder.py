#!/usr/bin/env python3
"""
Presentation builder for creating Google Slides from templates
"""

from .slides_service import GoogleSlidesService, hex_to_rgb, load_template


class PresentationBuilder:
    """Builder class for creating Google Slides presentations"""

    # Default page size (16:9 widescreen, 2x scale)
    DEFAULT_PAGE_WIDTH = 18288000  # EMU
    DEFAULT_PAGE_HEIGHT = 10287000  # EMU

    def __init__(self, template_name='default', templates_dir='templates/slides'):
        """
        Initialize builder with template

        Args:
            template_name: Template name to use
            templates_dir: Directory containing template files
        """
        self.template = load_template(template_name, templates_dir)
        self.config = self.template.get('config', {})
        self.page_size = self.template.get('page_size', {})
        self.page_width = self.page_size.get('width_emu', self.DEFAULT_PAGE_WIDTH)
        self.page_height = self.page_size.get('height_emu', self.DEFAULT_PAGE_HEIGHT)
        self.requests = []
        self.slide_count = 0

    def _get_color(self, key, default='#000000'):
        """Get color from config"""
        return self.config.get(key, default)

    def add_title_slide(self, title, subtitle=None):
        """
        Add a title slide

        Args:
            title: Main title text
            subtitle: Optional subtitle text

        Returns:
            self for chaining
        """
        self.slide_count += 1
        slide_id = f'slide_{self.slide_count}'

        primary_color = self._get_color('primary_color', '#D63031')
        bg_color = self._get_color('background_color', '#FFFFFF')
        text_color = self._get_color('text_color', '#000000')
        title_font_size = self.config.get('title_font_size', 48)
        header_font_size = self.config.get('header_font_size', 36)

        # Create slide
        self.requests.append({
            'createSlide': {
                'objectId': slide_id,
                'slideLayoutReference': {'predefinedLayout': 'BLANK'}
            }
        })

        # Background
        self._add_background(slide_id, bg_color)

        # Decorative shapes
        self._add_decorative_shapes(slide_id, primary_color)

        # Title
        title_id = f'{slide_id}_title'
        self.requests.append({
            'createShape': {
                'objectId': title_id,
                'shapeType': 'TEXT_BOX',
                'elementProperties': {
                    'pageObjectId': slide_id,
                    'size': {
                        'width': {'magnitude': self.page_width * 0.7, 'unit': 'EMU'},
                        'height': {'magnitude': 2000000, 'unit': 'EMU'}
                    },
                    'transform': {
                        'scaleX': 1, 'scaleY': 1,
                        'translateX': self.page_width * 0.15,
                        'translateY': self.page_height * 0.35,
                        'unit': 'EMU'
                    }
                }
            }
        })
        self.requests.append({'insertText': {'objectId': title_id, 'text': title, 'insertionIndex': 0}})
        self.requests.append({
            'updateTextStyle': {
                'objectId': title_id,
                'style': {
                    'bold': True,
                    'fontSize': {'magnitude': title_font_size, 'unit': 'PT'},
                    'foregroundColor': {'opaqueColor': {'rgbColor': hex_to_rgb(primary_color)}}
                },
                'fields': 'bold,fontSize,foregroundColor'
            }
        })
        self.requests.append({
            'updateParagraphStyle': {
                'objectId': title_id,
                'style': {'alignment': 'CENTER'},
                'fields': 'alignment'
            }
        })

        # Subtitle
        if subtitle:
            subtitle_id = f'{slide_id}_subtitle'
            self.requests.append({
                'createShape': {
                    'objectId': subtitle_id,
                    'shapeType': 'TEXT_BOX',
                    'elementProperties': {
                        'pageObjectId': slide_id,
                        'size': {
                            'width': {'magnitude': self.page_width * 0.6, 'unit': 'EMU'},
                            'height': {'magnitude': 1000000, 'unit': 'EMU'}
                        },
                        'transform': {
                            'scaleX': 1, 'scaleY': 1,
                            'translateX': self.page_width * 0.2,
                            'translateY': self.page_height * 0.55,
                            'unit': 'EMU'
                        }
                    }
                }
            })
            self.requests.append({'insertText': {'objectId': subtitle_id, 'text': subtitle, 'insertionIndex': 0}})
            self.requests.append({
                'updateTextStyle': {
                    'objectId': subtitle_id,
                    'style': {
                        'fontSize': {'magnitude': header_font_size, 'unit': 'PT'},
                        'foregroundColor': {'opaqueColor': {'rgbColor': hex_to_rgb(text_color)}}
                    },
                    'fields': 'fontSize,foregroundColor'
                }
            })
            self.requests.append({
                'updateParagraphStyle': {
                    'objectId': subtitle_id,
                    'style': {'alignment': 'CENTER'},
                    'fields': 'alignment'
                }
            })

        return self

    def add_section_slide(self, section_number, section_title, description=None):
        """
        Add a section divider slide

        Args:
            section_number: Section number (e.g., "01", "02")
            section_title: Section title
            description: Optional description text

        Returns:
            self for chaining
        """
        self.slide_count += 1
        slide_id = f'slide_{self.slide_count}'

        primary_color = self._get_color('primary_color', '#D63031')
        bg_color = self._get_color('background_color', '#FFFFFF')
        text_color = self._get_color('text_color', '#000000')
        header_font_size = self.config.get('header_font_size', 36)
        body_font_size = self.config.get('body_font_size', 18)

        # Create slide
        self.requests.append({
            'createSlide': {
                'objectId': slide_id,
                'slideLayoutReference': {'predefinedLayout': 'BLANK'}
            }
        })

        # Background
        self._add_background(slide_id, bg_color)

        # Large section number
        number_id = f'{slide_id}_number'
        self.requests.append({
            'createShape': {
                'objectId': number_id,
                'shapeType': 'TEXT_BOX',
                'elementProperties': {
                    'pageObjectId': slide_id,
                    'size': {
                        'width': {'magnitude': 3000000, 'unit': 'EMU'},
                        'height': {'magnitude': 2000000, 'unit': 'EMU'}
                    },
                    'transform': {
                        'scaleX': 1, 'scaleY': 1,
                        'translateX': self.page_width * 0.1,
                        'translateY': self.page_height * 0.15,
                        'unit': 'EMU'
                    }
                }
            }
        })
        self.requests.append({'insertText': {'objectId': number_id, 'text': section_number, 'insertionIndex': 0}})
        self.requests.append({
            'updateTextStyle': {
                'objectId': number_id,
                'style': {
                    'bold': True,
                    'fontSize': {'magnitude': 72, 'unit': 'PT'},
                    'foregroundColor': {'opaqueColor': {'rgbColor': hex_to_rgb(primary_color)}}
                },
                'fields': 'bold,fontSize,foregroundColor'
            }
        })

        # Section title
        title_id = f'{slide_id}_title'
        self.requests.append({
            'createShape': {
                'objectId': title_id,
                'shapeType': 'TEXT_BOX',
                'elementProperties': {
                    'pageObjectId': slide_id,
                    'size': {
                        'width': {'magnitude': self.page_width * 0.7, 'unit': 'EMU'},
                        'height': {'magnitude': 1500000, 'unit': 'EMU'}
                    },
                    'transform': {
                        'scaleX': 1, 'scaleY': 1,
                        'translateX': self.page_width * 0.1,
                        'translateY': self.page_height * 0.4,
                        'unit': 'EMU'
                    }
                }
            }
        })
        self.requests.append({'insertText': {'objectId': title_id, 'text': section_title, 'insertionIndex': 0}})
        self.requests.append({
            'updateTextStyle': {
                'objectId': title_id,
                'style': {
                    'bold': True,
                    'fontSize': {'magnitude': header_font_size, 'unit': 'PT'},
                    'foregroundColor': {'opaqueColor': {'rgbColor': hex_to_rgb(text_color)}}
                },
                'fields': 'bold,fontSize,foregroundColor'
            }
        })

        # Description
        if description:
            desc_id = f'{slide_id}_desc'
            self.requests.append({
                'createShape': {
                    'objectId': desc_id,
                    'shapeType': 'TEXT_BOX',
                    'elementProperties': {
                        'pageObjectId': slide_id,
                        'size': {
                            'width': {'magnitude': self.page_width * 0.6, 'unit': 'EMU'},
                            'height': {'magnitude': 1000000, 'unit': 'EMU'}
                        },
                        'transform': {
                            'scaleX': 1, 'scaleY': 1,
                            'translateX': self.page_width * 0.1,
                            'translateY': self.page_height * 0.6,
                            'unit': 'EMU'
                        }
                    }
                }
            })
            self.requests.append({'insertText': {'objectId': desc_id, 'text': description, 'insertionIndex': 0}})
            self.requests.append({
                'updateTextStyle': {
                    'objectId': desc_id,
                    'style': {
                        'fontSize': {'magnitude': body_font_size, 'unit': 'PT'},
                        'foregroundColor': {'opaqueColor': {'rgbColor': hex_to_rgb(text_color)}}
                    },
                    'fields': 'fontSize,foregroundColor'
                }
            })

        return self

    def add_content_slide(self, title, content_lines):
        """
        Add a content slide with bullet points

        Args:
            title: Slide title
            content_lines: List of content lines

        Returns:
            self for chaining
        """
        self.slide_count += 1
        slide_id = f'slide_{self.slide_count}'

        primary_color = self._get_color('primary_color', '#D63031')
        bg_color = self._get_color('background_color', '#FFFFFF')
        text_color = self._get_color('text_color', '#000000')
        header_font_size = self.config.get('header_font_size', 36)
        body_font_size = self.config.get('body_font_size', 18)

        # Create slide
        self.requests.append({
            'createSlide': {
                'objectId': slide_id,
                'slideLayoutReference': {'predefinedLayout': 'BLANK'}
            }
        })

        # Background
        self._add_background(slide_id, bg_color)

        # Title
        title_id = f'{slide_id}_title'
        self.requests.append({
            'createShape': {
                'objectId': title_id,
                'shapeType': 'TEXT_BOX',
                'elementProperties': {
                    'pageObjectId': slide_id,
                    'size': {
                        'width': {'magnitude': self.page_width * 0.8, 'unit': 'EMU'},
                        'height': {'magnitude': 1200000, 'unit': 'EMU'}
                    },
                    'transform': {
                        'scaleX': 1, 'scaleY': 1,
                        'translateX': self.page_width * 0.1,
                        'translateY': self.page_height * 0.08,
                        'unit': 'EMU'
                    }
                }
            }
        })
        self.requests.append({'insertText': {'objectId': title_id, 'text': title, 'insertionIndex': 0}})
        self.requests.append({
            'updateTextStyle': {
                'objectId': title_id,
                'style': {
                    'bold': True,
                    'fontSize': {'magnitude': header_font_size, 'unit': 'PT'},
                    'foregroundColor': {'opaqueColor': {'rgbColor': hex_to_rgb(primary_color)}}
                },
                'fields': 'bold,fontSize,foregroundColor'
            }
        })

        # Content
        content_id = f'{slide_id}_content'
        content_text = '\n'.join([f'• {line}' for line in content_lines])
        self.requests.append({
            'createShape': {
                'objectId': content_id,
                'shapeType': 'TEXT_BOX',
                'elementProperties': {
                    'pageObjectId': slide_id,
                    'size': {
                        'width': {'magnitude': self.page_width * 0.8, 'unit': 'EMU'},
                        'height': {'magnitude': self.page_height * 0.6, 'unit': 'EMU'}
                    },
                    'transform': {
                        'scaleX': 1, 'scaleY': 1,
                        'translateX': self.page_width * 0.1,
                        'translateY': self.page_height * 0.25,
                        'unit': 'EMU'
                    }
                }
            }
        })
        self.requests.append({'insertText': {'objectId': content_id, 'text': content_text, 'insertionIndex': 0}})
        self.requests.append({
            'updateTextStyle': {
                'objectId': content_id,
                'style': {
                    'fontSize': {'magnitude': body_font_size, 'unit': 'PT'},
                    'foregroundColor': {'opaqueColor': {'rgbColor': hex_to_rgb(text_color)}}
                },
                'fields': 'fontSize,foregroundColor'
            }
        })

        return self

    def _add_background(self, slide_id, color_hex):
        """Add background rectangle to slide"""
        bg_id = f'{slide_id}_bg'
        self.requests.append({
            'createShape': {
                'objectId': bg_id,
                'shapeType': 'RECTANGLE',
                'elementProperties': {
                    'pageObjectId': slide_id,
                    'size': {
                        'width': {'magnitude': self.page_width, 'unit': 'EMU'},
                        'height': {'magnitude': self.page_height, 'unit': 'EMU'}
                    },
                    'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': 0, 'translateY': 0, 'unit': 'EMU'}
                }
            }
        })
        self.requests.append({
            'updateShapeProperties': {
                'objectId': bg_id,
                'shapeProperties': {
                    'shapeBackgroundFill': {'solidFill': {'color': {'rgbColor': hex_to_rgb(color_hex)}}},
                    'outline': {'outlineFill': {'solidFill': {'color': {'rgbColor': hex_to_rgb(color_hex)}}}}
                },
                'fields': 'shapeBackgroundFill,outline'
            }
        })

    def _add_decorative_shapes(self, slide_id, color_hex):
        """Add decorative geometric shapes to slide"""
        shapes = [
            {'type': 'RECTANGLE', 'x': 1000000, 'y': 1000000, 'w': 3000000, 'h': 3000000},
            {'type': 'ELLIPSE', 'x': 14000000, 'y': 7000000, 'w': 2500000, 'h': 2500000},
        ]

        for i, shape in enumerate(shapes):
            deco_id = f'{slide_id}_deco_{i}'
            self.requests.append({
                'createShape': {
                    'objectId': deco_id,
                    'shapeType': shape['type'],
                    'elementProperties': {
                        'pageObjectId': slide_id,
                        'size': {
                            'width': {'magnitude': shape['w'], 'unit': 'EMU'},
                            'height': {'magnitude': shape['h'], 'unit': 'EMU'}
                        },
                        'transform': {
                            'scaleX': 1, 'scaleY': 1,
                            'translateX': shape['x'],
                            'translateY': shape['y'],
                            'unit': 'EMU'
                        }
                    }
                }
            })
            self.requests.append({
                'updateShapeProperties': {
                    'objectId': deco_id,
                    'shapeProperties': {
                        'shapeBackgroundFill': {
                            'solidFill': {'color': {'rgbColor': hex_to_rgb(color_hex)}, 'alpha': 0.3}
                        },
                        'outline': {'outlineFill': {'solidFill': {'color': {'rgbColor': hex_to_rgb(color_hex)}}}}
                    },
                    'fields': 'shapeBackgroundFill,outline'
                }
            })

    def build(self, title):
        """
        Build and create the presentation

        Args:
            title: Presentation title

        Returns:
            Tuple of (presentation_id, presentation_url)
        """
        service = GoogleSlidesService()
        presentation_id = service.create_presentation(title)
        service.batch_update(presentation_id, self.requests)
        url = service.get_presentation_url(presentation_id)
        return presentation_id, url
