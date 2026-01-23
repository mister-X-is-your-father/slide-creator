/**
 * Handdrawn.js - Rough.js + roughViz ラッパー
 * テイストを選んで手書き風グラフィックを描画
 */

// ========================================
// テイスト（スタイル）プリセット
// ========================================
const HANDDRAWN_STYLES = {
  // 軽い手書き風（ビジネス向け）
  light: {
    roughness: 0.5,
    bowing: 0.5,
    strokeWidth: 1,
    fillStyle: 'hachure',
    fillWeight: 1,
    hachureGap: 4
  },

  // 標準的な手書き風
  normal: {
    roughness: 1,
    bowing: 1,
    strokeWidth: 1.5,
    fillStyle: 'hachure',
    fillWeight: 1.5,
    hachureGap: 4
  },

  // しっかり手書き風（絵本向け）
  sketchy: {
    roughness: 2,
    bowing: 1.5,
    strokeWidth: 2,
    fillStyle: 'zigzag',
    fillWeight: 2,
    hachureGap: 5
  },

  // 荒い手書き風（落書き風）
  rough: {
    roughness: 3,
    bowing: 2,
    strokeWidth: 2.5,
    fillStyle: 'cross-hatch',
    fillWeight: 2,
    hachureGap: 6
  },

  // クレヨン風
  crayon: {
    roughness: 2.5,
    bowing: 1.8,
    strokeWidth: 3,
    fillStyle: 'solid',
    fillWeight: 3,
    hachureGap: 3
  },

  // ペン風（細い線）
  pen: {
    roughness: 0.8,
    bowing: 0.3,
    strokeWidth: 1,
    fillStyle: 'hachure',
    fillWeight: 0.8,
    hachureGap: 3
  },

  // マーカー風
  marker: {
    roughness: 1.2,
    bowing: 0.8,
    strokeWidth: 2,
    fillStyle: 'solid',
    fillWeight: 2,
    hachureGap: 4
  }
};

// カラーパレット
const COLOR_PALETTES = {
  warm: ['#FF6B6B', '#FFE66D', '#4ECDC4', '#FF8C42', '#95E1D3'],
  cool: ['#74B9FF', '#A29BFE', '#81ECEC', '#6C5CE7', '#00CEC9'],
  pastel: ['#FFB3BA', '#FFDFBA', '#FFFFBA', '#BAFFC9', '#BAE1FF'],
  earth: ['#D4A574', '#8B7355', '#6B8E23', '#CD853F', '#DEB887'],
  mono: ['#2D3436', '#636E72', '#B2BEC3', '#DFE6E9', '#74B9FF'],
  picturebook: ['#FF9AA2', '#FFB7B2', '#FFDAC1', '#E2F0CB', '#B5EAD7', '#C7CEEA']
};

// ========================================
// Handdrawn クラス
// ========================================
class Handdrawn {
  constructor(options = {}) {
    this.style = options.style || 'normal';
    this.palette = options.palette || 'warm';
    this.roughInstance = null;

    // Rough.js の読み込み確認
    if (typeof rough === 'undefined') {
      console.warn('Rough.js not loaded. Please include: <script src="https://unpkg.com/roughjs@latest/bundled/rough.cjs.js"></script>');
    }
  }

  // スタイル設定を取得
  getStyleOptions(overrides = {}) {
    const baseStyle = HANDDRAWN_STYLES[this.style] || HANDDRAWN_STYLES.normal;
    return { ...baseStyle, ...overrides };
  }

  // カラーパレットを取得
  getColors() {
    return COLOR_PALETTES[this.palette] || COLOR_PALETTES.warm;
  }

  // Canvas に描画インスタンスを作成
  canvas(canvasElement) {
    if (typeof rough !== 'undefined') {
      this.roughInstance = rough.canvas(canvasElement);
      return this;
    }
    return null;
  }

  // SVG に描画インスタンスを作成
  svg(svgElement) {
    if (typeof rough !== 'undefined') {
      this.roughInstance = rough.svg(svgElement);
      return this;
    }
    return null;
  }

  // 四角形を描画
  rectangle(x, y, width, height, options = {}) {
    if (!this.roughInstance) return null;
    const opts = this.getStyleOptions(options);
    return this.roughInstance.rectangle(x, y, width, height, opts);
  }

  // 円を描画
  circle(x, y, diameter, options = {}) {
    if (!this.roughInstance) return null;
    const opts = this.getStyleOptions(options);
    return this.roughInstance.circle(x, y, diameter, opts);
  }

  // 楕円を描画
  ellipse(x, y, width, height, options = {}) {
    if (!this.roughInstance) return null;
    const opts = this.getStyleOptions(options);
    return this.roughInstance.ellipse(x, y, width, height, opts);
  }

  // 線を描画
  line(x1, y1, x2, y2, options = {}) {
    if (!this.roughInstance) return null;
    const opts = this.getStyleOptions(options);
    return this.roughInstance.line(x1, y1, x2, y2, opts);
  }

  // 多角形を描画
  polygon(vertices, options = {}) {
    if (!this.roughInstance) return null;
    const opts = this.getStyleOptions(options);
    return this.roughInstance.polygon(vertices, opts);
  }

  // パスを描画
  path(d, options = {}) {
    if (!this.roughInstance) return null;
    const opts = this.getStyleOptions(options);
    return this.roughInstance.path(d, opts);
  }

  // 矢印を描画
  arrow(x1, y1, x2, y2, options = {}) {
    if (!this.roughInstance) return null;
    const opts = this.getStyleOptions(options);

    // 矢印の本体
    const line = this.roughInstance.line(x1, y1, x2, y2, opts);

    // 矢印の先端（三角形）
    const angle = Math.atan2(y2 - y1, x2 - x1);
    const headLength = options.headLength || 15;
    const headAngle = Math.PI / 6;

    const head1X = x2 - headLength * Math.cos(angle - headAngle);
    const head1Y = y2 - headLength * Math.sin(angle - headAngle);
    const head2X = x2 - headLength * Math.cos(angle + headAngle);
    const head2Y = y2 - headLength * Math.sin(angle + headAngle);

    const head1 = this.roughInstance.line(x2, y2, head1X, head1Y, opts);
    const head2 = this.roughInstance.line(x2, y2, head2X, head2Y, opts);

    return { line, head1, head2 };
  }

  // ボックス（角丸四角形風）を描画
  box(x, y, width, height, options = {}) {
    if (!this.roughInstance) return null;
    const opts = this.getStyleOptions({
      fill: options.fill || this.getColors()[0],
      ...options
    });
    return this.roughInstance.rectangle(x, y, width, height, opts);
  }
}

// ========================================
// HanddrawnChart クラス（roughViz ラッパー）
// ========================================
class HanddrawnChart {
  constructor(options = {}) {
    this.style = options.style || 'normal';
    this.palette = options.palette || 'warm';
    this.font = options.font || 0; // 0: Gaegu, 1: Indie Flower

    // roughViz の読み込み確認
    if (typeof roughViz === 'undefined') {
      console.warn('roughViz not loaded. Please include: <script src="https://unpkg.com/rough-viz@2.0.5"></script>');
    }
  }

  // 共通オプションを取得
  getChartOptions(overrides = {}) {
    const stylePreset = HANDDRAWN_STYLES[this.style] || HANDDRAWN_STYLES.normal;
    const colors = COLOR_PALETTES[this.palette] || COLOR_PALETTES.warm;

    return {
      roughness: stylePreset.roughness,
      fillStyle: stylePreset.fillStyle,
      fillWeight: stylePreset.fillWeight,
      strokeWidth: stylePreset.strokeWidth,
      colors: colors,
      font: this.font,
      highlight: colors[0],
      ...overrides
    };
  }

  // 棒グラフ（縦）
  bar(element, data, options = {}) {
    if (typeof roughViz === 'undefined') return null;
    const opts = this.getChartOptions(options);
    return new roughViz.Bar({
      element,
      data,
      ...opts
    });
  }

  // 棒グラフ（横）
  barH(element, data, options = {}) {
    if (typeof roughViz === 'undefined') return null;
    const opts = this.getChartOptions(options);
    return new roughViz.BarH({
      element,
      data,
      ...opts
    });
  }

  // 円グラフ
  pie(element, data, options = {}) {
    if (typeof roughViz === 'undefined') return null;
    const opts = this.getChartOptions(options);
    return new roughViz.Pie({
      element,
      data,
      ...opts
    });
  }

  // ドーナツグラフ
  donut(element, data, options = {}) {
    if (typeof roughViz === 'undefined') return null;
    const opts = this.getChartOptions(options);
    return new roughViz.Donut({
      element,
      data,
      ...opts
    });
  }

  // 折れ線グラフ
  line(element, data, options = {}) {
    if (typeof roughViz === 'undefined') return null;
    const opts = this.getChartOptions(options);
    return new roughViz.Line({
      element,
      data,
      ...opts
    });
  }

  // 散布図
  scatter(element, data, options = {}) {
    if (typeof roughViz === 'undefined') return null;
    const opts = this.getChartOptions(options);
    return new roughViz.Scatter({
      element,
      data,
      ...opts
    });
  }

  // 積み上げ棒グラフ
  stackedBar(element, data, options = {}) {
    if (typeof roughViz === 'undefined') return null;
    const opts = this.getChartOptions(options);
    return new roughViz.StackedBar({
      element,
      data,
      ...opts
    });
  }
}

// ========================================
// ユーティリティ関数
// ========================================

// DOM要素を手書き風に変換
function makeHanddrawn(selector, options = {}) {
  const elements = document.querySelectorAll(selector);
  const hd = new Handdrawn(options);

  elements.forEach(el => {
    // SVGを作成して要素の背景として配置
    const rect = el.getBoundingClientRect();
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.setAttribute('width', rect.width);
    svg.setAttribute('height', rect.height);
    svg.style.position = 'absolute';
    svg.style.top = '0';
    svg.style.left = '0';
    svg.style.pointerEvents = 'none';
    svg.style.zIndex = '-1';

    hd.svg(svg);
    const border = hd.rectangle(2, 2, rect.width - 4, rect.height - 4, {
      stroke: options.stroke || '#333',
      fill: options.fill || 'transparent'
    });
    svg.appendChild(border);

    el.style.position = 'relative';
    el.appendChild(svg);
  });
}

// 自動初期化（data-handdrawn属性を持つ要素）
function initHanddrawnElements() {
  // data-handdrawn-box
  document.querySelectorAll('[data-handdrawn-box]').forEach(el => {
    const style = el.dataset.handdrawnBox || 'normal';
    makeHanddrawn(el, { style });
  });

  // data-handdrawn-chart
  document.querySelectorAll('[data-handdrawn-chart]').forEach(el => {
    const chartType = el.dataset.handdrawnChart;
    const style = el.dataset.style || 'normal';
    const palette = el.dataset.palette || 'warm';
    const dataAttr = el.dataset.chartData;

    if (chartType && dataAttr) {
      try {
        const data = JSON.parse(dataAttr);
        const chart = new HanddrawnChart({ style, palette });
        chart[chartType](`#${el.id}`, data);
      } catch (e) {
        console.error('Chart data parse error:', e);
      }
    }
  });
}

// DOMContentLoaded で自動初期化
if (typeof document !== 'undefined') {
  document.addEventListener('DOMContentLoaded', initHanddrawnElements);
}

// ========================================
// エクスポート
// ========================================
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    Handdrawn,
    HanddrawnChart,
    HANDDRAWN_STYLES,
    COLOR_PALETTES,
    makeHanddrawn,
    initHanddrawnElements
  };
}

// グローバルに公開
if (typeof window !== 'undefined') {
  window.Handdrawn = Handdrawn;
  window.HanddrawnChart = HanddrawnChart;
  window.HANDDRAWN_STYLES = HANDDRAWN_STYLES;
  window.COLOR_PALETTES = COLOR_PALETTES;
  window.makeHanddrawn = makeHanddrawn;
  window.initHanddrawnElements = initHanddrawnElements;
}
