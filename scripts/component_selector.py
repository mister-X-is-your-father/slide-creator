#!/usr/bin/env python3
"""
component_selector.py - テキスト内容からコンポーネントを自動選択

キーワードや構造を分析して、最適な図解コンポーネントを提案する。
"""

import re
from typing import Dict, List, Tuple

# キーワードとコンポーネントのマッピング
KEYWORD_PATTERNS = {
    # 時系列・プロセス系
    'timeline': {
        'keywords': ['フェーズ', 'ステップ', '段階', '手順', '流れ', 'プロセス', '工程',
                     'phase', 'step', 'stage', 'process', 'flow', 'schedule', 'スケジュール'],
        'components': ['timeline', 'steps', 'roadmap', 'gantt'],
        'numbered': True  # 番号付きリストの場合に優先
    },

    # 比較系
    'comparison': {
        'keywords': ['比較', '対比', 'vs', 'VS', '違い', '差', 'メリット', 'デメリット',
                     'compare', 'versus', 'difference', 'pros', 'cons', '長所', '短所'],
        'components': ['comparison-table', 'vs-comparison', 'pros-cons', 'before-after'],
        'numbered': False
    },

    # 階層・組織系
    'hierarchy': {
        'keywords': ['組織', '構造', '階層', 'レイヤー', 'チーム', '部門',
                     'organization', 'structure', 'layer', 'team', 'department'],
        'components': ['org-chart', 'hierarchy', 'layers', 'pyramid'],
        'numbered': False
    },

    # 数値・KPI系
    'metrics': {
        'keywords': ['%', '％', '倍', '件', '人', '円', '万', '億', 'KPI', '目標', '達成',
                     '増加', '減少', '改善', '向上', 'percent', 'increase', 'decrease'],
        'components': ['metric-card', 'big-number', 'progress-bar', 'counter-grid'],
        'numbered': False
    },

    # フロー・分岐系
    'flow': {
        'keywords': ['フロー', '流れ', '経路', '分岐', '判断', '条件', 'もし', 'なら',
                     'flow', 'branch', 'decision', 'if', 'then', 'path'],
        'components': ['flow-horizontal', 'flow-vertical', 'flow-branch'],
        'numbered': False
    },

    # サイクル・循環系
    'cycle': {
        'keywords': ['サイクル', '循環', 'PDCA', 'ループ', '繰り返し', '反復',
                     'cycle', 'loop', 'iteration', 'recurring'],
        'components': ['cycle', 'cycle-4'],
        'numbered': False
    },

    # 分析・マトリクス系
    'matrix': {
        'keywords': ['SWOT', 'マトリクス', '4象限', '分析', '評価', 'matrix',
                     'analysis', 'quadrant', '優先度', 'priority'],
        'components': ['swot', 'matrix-2x2'],
        'numbered': False
    },

    # グラフ・チャート系
    'chart': {
        'keywords': ['グラフ', 'チャート', '推移', '割合', 'シェア', '分布',
                     'graph', 'chart', 'trend', 'share', 'distribution', 'データ'],
        'components': ['bar-chart', 'pie-chart', 'donut-chart', 'radar-chart'],
        'numbered': False
    },

    # リスト・列挙系
    'list': {
        'keywords': ['一覧', 'リスト', '項目', '要素', '機能', '特徴', 'ポイント',
                     'list', 'items', 'features', 'points', '例'],
        'components': ['icon-list', 'checklist', 'card-grid', 'feature-card'],
        'numbered': False
    },

    # 引用・強調系
    'quote': {
        'keywords': ['名言', '格言', '引用', '言葉', 'メッセージ', '一言',
                     'quote', 'message', 'saying'],
        'components': ['quote-box', 'big-quote', 'highlight-box'],
        'numbered': False
    },

    # FAQ・Q&A系
    'faq': {
        'keywords': ['質問', '回答', 'Q&A', 'FAQ', 'なぜ', 'どう', '?', '？',
                     'question', 'answer', 'why', 'how', 'what'],
        'components': ['faq'],
        'numbered': False
    },

    # 価格・プラン系
    'pricing': {
        'keywords': ['価格', '料金', 'プラン', 'コース', '月額', '年額',
                     'price', 'pricing', 'plan', 'tier', 'subscription'],
        'components': ['pricing'],
        'numbered': False
    },
}

# 構造パターン
STRUCTURE_PATTERNS = {
    'numbered_list': {
        'pattern': r'^\d+\.',
        'components': ['steps', 'numbered-list', 'timeline', 'process-steps']
    },
    'bullet_list': {
        'pattern': r'^[-*]',
        'components': ['icon-list', 'bullet-points', 'checklist']
    },
    'before_after': {
        'pattern': r'(before|after|以前|以後|前|後|ビフォー|アフター)',
        'components': ['before-after']
    },
    'two_items': {
        'count': 2,
        'components': ['two-column', 'vs-comparison']
    },
    'three_items': {
        'count': 3,
        'components': ['three-column', 'steps']
    },
    'four_items': {
        'count': 4,
        'components': ['four-column', 'steps', 'cycle-4']
    },
    'many_items': {
        'count_min': 5,
        'components': ['card-grid', 'timeline', 'checklist']
    }
}


def analyze_keywords(text: str) -> Dict[str, float]:
    """テキスト内のキーワードを分析してスコアを返す"""
    text_lower = text.lower()
    scores = {}

    for category, data in KEYWORD_PATTERNS.items():
        score = 0
        for keyword in data['keywords']:
            if keyword.lower() in text_lower:
                score += 1
        if score > 0:
            scores[category] = score

    return scores


def analyze_structure(content: List[Dict]) -> Dict[str, any]:
    """コンテンツの構造を分析"""
    result = {
        'item_count': len(content),
        'has_numbers': False,
        'has_bullets': False,
        'avg_text_length': 0,
        'has_metrics': False
    }

    total_length = 0
    for item in content:
        text = item.get('text', '')
        total_length += len(text)

        if item.get('type') == 'numbered_item':
            result['has_numbers'] = True
        elif item.get('type') == 'list_item':
            result['has_bullets'] = True

        # 数値を含むか
        if re.search(r'\d+[%％倍件人円万億]', text):
            result['has_metrics'] = True

    if content:
        result['avg_text_length'] = total_length / len(content)

    return result


def select_component(section: Dict, style_category: str = 'business') -> Tuple[str, float]:
    """
    セクションに最適なコンポーネントを選択

    Args:
        section: セクション情報
        style_category: スタイルカテゴリ（business/handdrawn/picturebook）

    Returns:
        (component_name, confidence_score)
    """
    title = section.get('title', '')
    content = section.get('content', [])
    section_type = section.get('type', '')

    # 特殊なセクションタイプ
    if section_type == 'title':
        return 'title-slide', 1.0
    if section_type == 'section' and not content:
        return 'section-header', 1.0

    # テキストを結合
    all_text = title + ' ' + ' '.join([c.get('text', '') for c in content])

    # キーワード分析
    keyword_scores = analyze_keywords(all_text)

    # 構造分析
    structure = analyze_structure(content)

    # スコアリング
    candidates = []

    # キーワードベースの候補
    for category, score in keyword_scores.items():
        pattern_data = KEYWORD_PATTERNS[category]
        for component in pattern_data['components']:
            # 番号付きリストとの相性
            if pattern_data['numbered'] and structure['has_numbers']:
                score += 0.5
            candidates.append((component, score))

    # 構造ベースの候補
    item_count = structure['item_count']

    if structure['has_numbers']:
        if item_count <= 4:
            candidates.append(('steps', 0.8))
        else:
            candidates.append(('timeline', 0.7))
            candidates.append(('numbered-list', 0.6))

    if structure['has_bullets']:
        if item_count <= 3:
            candidates.append(('icon-list', 0.7))
        elif item_count <= 5:
            candidates.append(('bullet-points', 0.6))
        else:
            candidates.append(('checklist', 0.5))

    if structure['has_metrics']:
        candidates.append(('metric-card', 0.8))
        candidates.append(('big-number', 0.6))

    # アイテム数による調整
    if item_count == 2:
        candidates.append(('two-column', 0.5))
    elif item_count == 3:
        candidates.append(('three-column', 0.5))

    # スタイルカテゴリによる調整
    if style_category == 'handdrawn':
        # 手書き風では複雑な図解より、シンプルなものを優先
        for i, (comp, score) in enumerate(candidates):
            if comp in ['icon-list', 'steps', 'bullet-points']:
                candidates[i] = (comp, score + 0.2)
    elif style_category == 'picturebook':
        # 絵本風ではシンプルな構造を優先
        for i, (comp, score) in enumerate(candidates):
            if comp in ['icon-list', 'two-column']:
                candidates[i] = (comp, score + 0.3)

    # 最高スコアを選択
    if candidates:
        candidates.sort(key=lambda x: x[1], reverse=True)
        return candidates[0]

    # デフォルト
    if structure['has_bullets'] or structure['has_numbers']:
        return 'bullet-points', 0.3
    return 'default', 0.1


def suggest_components(section: Dict, style_category: str = 'business', top_n: int = 3) -> List[Tuple[str, float]]:
    """
    複数のコンポーネント候補を提案

    Args:
        section: セクション情報
        style_category: スタイルカテゴリ
        top_n: 返す候補数

    Returns:
        [(component_name, confidence_score), ...]
    """
    title = section.get('title', '')
    content = section.get('content', [])

    all_text = title + ' ' + ' '.join([c.get('text', '') for c in content])
    keyword_scores = analyze_keywords(all_text)
    structure = analyze_structure(content)

    candidates = []

    # 全カテゴリからの候補を収集
    for category, score in keyword_scores.items():
        pattern_data = KEYWORD_PATTERNS[category]
        for component in pattern_data['components']:
            adjusted_score = score
            if pattern_data['numbered'] and structure['has_numbers']:
                adjusted_score += 0.5
            candidates.append((component, adjusted_score))

    # 構造ベース
    if structure['has_numbers']:
        candidates.extend([('steps', 0.8), ('timeline', 0.7), ('numbered-list', 0.6)])
    if structure['has_bullets']:
        candidates.extend([('icon-list', 0.7), ('bullet-points', 0.6)])
    if structure['has_metrics']:
        candidates.extend([('metric-card', 0.8), ('big-number', 0.6)])

    # 重複を除去してスコア順にソート
    seen = set()
    unique_candidates = []
    for comp, score in sorted(candidates, key=lambda x: x[1], reverse=True):
        if comp not in seen:
            seen.add(comp)
            unique_candidates.append((comp, score))

    return unique_candidates[:top_n]


# テスト
if __name__ == '__main__':
    # テストケース
    test_sections = [
        {
            'title': 'プロジェクトスケジュール',
            'content': [
                {'type': 'numbered_item', 'text': '要件定義フェーズ'},
                {'type': 'numbered_item', 'text': '設計フェーズ'},
                {'type': 'numbered_item', 'text': '開発フェーズ'},
                {'type': 'numbered_item', 'text': 'テストフェーズ'},
            ]
        },
        {
            'title': '売上推移',
            'content': [
                {'type': 'paragraph', 'text': '前年比120%の成長'},
                {'type': 'paragraph', 'text': '月間売上1000万円達成'},
            ]
        },
        {
            'title': 'メリット・デメリット',
            'content': [
                {'type': 'list_item', 'text': 'コスト削減'},
                {'type': 'list_item', 'text': '効率向上'},
                {'type': 'list_item', 'text': '初期投資が必要'},
            ]
        },
    ]

    print("コンポーネント自動選択テスト\n")
    for section in test_sections:
        print(f"タイトル: {section['title']}")
        component, score = select_component(section)
        print(f"  選択: {component} (スコア: {score:.2f})")
        suggestions = suggest_components(section)
        print(f"  候補: {suggestions}")
        print()
