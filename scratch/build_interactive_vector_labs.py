# -*- coding: utf-8 -*-
"""
build_interactive_vector_labs.py
================================
Generates 100% interactive vector SVG muscle-memory drawing labs for:
  - draw_drives.html  (Electric Drives - EET413)
  - draw_acs.html     (Advanced Control Systems - EET401)
  - draw_mobile.html  (Mobile Computing - CST415)
"""

import sys, os, json, html

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vector_diagrams_drives import DRIVES_DIAGRAMS
from vector_diagrams_acs import ACS_DIAGRAMS
from vector_diagrams_mobile import MOBILE_DIAGRAMS

def generate_interactive_lab(subject_key, subject_name, course_code, accent_color, diagrams, output_filename):
    diagrams_json = json.dumps(diagrams)

    page_html = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>{html.escape(subject_name)} ({course_code}) | Interactive Muscle Memory Canvas</title>

    <!-- Theme & Preload -->
    <script>
        (function() {{
            const savedTheme = localStorage.getItem('ktu_portal_theme') || 'dark';
            document.documentElement.setAttribute('data-theme', savedTheme);
        }})();
    </script>

    <!-- KaTeX CDN -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>

    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">

    <style>
        :root, [data-theme="dark"] {{
            --bg-base: #080b11;
            --bg-surface: #0f1523;
            --bg-card: #151e32;
            --bg-card-hover: #1c2842;
            --border-subtle: #22304d;
            --border-focus: #38bdf8;
            --text-main: #f1f5f9;
            --text-body: #cbd5e1;
            --text-muted: #8292a8;
            --header-bg: rgba(13, 19, 29, 0.94);
            --accent-main: {accent_color};
            --accent-alpha: rgba(56, 189, 248, 0.2);
            --card-shadow: 0 12px 30px rgba(0, 0, 0, 0.6);
        }}

        [data-theme="light"] {{
            --bg-base: #f8fafc;
            --bg-surface: #ffffff;
            --bg-card: #f1f5f9;
            --bg-card-hover: #e2e8f0;
            --border-subtle: #cbd5e1;
            --border-focus: #0284c7;
            --text-main: #0f172a;
            --text-body: #334155;
            --text-muted: #64748b;
            --header-bg: rgba(255, 255, 255, 0.94);
            --accent-main: {accent_color};
            --accent-alpha: rgba(2, 132, 199, 0.15);
            --card-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            -webkit-tap-highlight-color: transparent;
        }}

        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background-color: var(--bg-base);
            color: var(--text-main);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            overflow-x: hidden;
            touch-action: pan-y;
        }}

        /* Header Navigation */
        .site-header {{
            position: sticky;
            top: 0;
            z-index: 100;
            background: var(--header-bg);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-bottom: 1px solid var(--border-subtle);
            padding: 0.65rem 1.25rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
        }}

        .brand-link {{
            display: flex;
            align-items: center;
            gap: 0.65rem;
            text-decoration: none;
            color: var(--text-main);
            font-weight: 800;
            font-size: 1.05rem;
            letter-spacing: -0.02em;
        }}

        .brand-badge {{
            font-size: 0.7rem;
            font-weight: 700;
            text-transform: uppercase;
            padding: 0.2rem 0.55rem;
            border-radius: 9999px;
            background: rgba(56, 189, 248, 0.15);
            color: var(--accent-main);
            border: 1px solid var(--accent-main);
        }}

        .nav-pills {{
            display: flex;
            align-items: center;
            gap: 0.45rem;
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
        }}

        .nav-pill {{
            font-size: 0.8rem;
            font-weight: 600;
            color: var(--text-muted);
            text-decoration: none;
            padding: 0.35rem 0.75rem;
            border-radius: 8px;
            white-space: nowrap;
            transition: all 0.2s ease;
        }}

        .nav-pill:hover {{
            color: var(--text-main);
            background: var(--bg-card);
        }}

        .nav-pill.active {{
            background: var(--bg-card);
            color: var(--accent-main);
            border: 1px solid var(--accent-main);
        }}

        /* Subject Switcher Bar */
        .subject-switcher-bar {{
            background: var(--bg-surface);
            border-bottom: 1px solid var(--border-subtle);
            padding: 0.5rem 1.25rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
            overflow-x: auto;
        }}

        .subject-tabs {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .subject-tab {{
            font-size: 0.78rem;
            font-weight: 700;
            color: var(--text-muted);
            text-decoration: none;
            padding: 0.32rem 0.75rem;
            border-radius: 9999px;
            border: 1px solid var(--border-subtle);
            transition: all 0.2s ease;
            white-space: nowrap;
        }}

        .subject-tab:hover {{
            color: var(--text-main);
            border-color: var(--border-focus);
        }}

        .subject-tab.active {{
            background: var(--accent-alpha);
            color: var(--accent-main);
            border-color: var(--accent-main);
            box-shadow: 0 0 10px var(--accent-alpha);
        }}

        /* Container */
        .lab-container {{
            max-width: 1280px;
            width: 100%;
            margin: 0 auto;
            padding: 1.25rem;
            display: flex;
            flex-direction: column;
            gap: 1.25rem;
            flex: 1;
        }}

        /* Diagram Carousel / Selector */
        .diagram-selector-card {{
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            border-radius: 14px;
            padding: 0.85rem 1rem;
            display: flex;
            flex-direction: column;
            gap: 0.65rem;
        }}

        .selector-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 0.75rem;
        }}

        .selector-title {{
            font-size: 0.82rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--text-muted);
            display: flex;
            align-items: center;
            gap: 0.4rem;
        }}

        .diagram-carousel {{
            display: flex;
            gap: 0.65rem;
            overflow-x: auto;
            padding-bottom: 0.35rem;
            scroll-snap-type: x mandatory;
            -webkit-overflow-scrolling: touch;
        }}

        .carousel-item {{
            flex: 0 0 240px;
            scroll-snap-align: start;
            background: var(--bg-card);
            border: 1px solid var(--border-subtle);
            border-radius: 10px;
            padding: 0.65rem 0.85rem;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            flex-direction: column;
            gap: 0.35rem;
            user-select: none;
        }}

        .carousel-item:hover {{
            border-color: var(--border-focus);
            transform: translateY(-2px);
        }}

        .carousel-item.active {{
            border-color: var(--accent-main);
            background: var(--bg-card-hover);
            box-shadow: 0 0 14px var(--accent-alpha);
        }}

        .carousel-item-top {{
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}

        .item-qid {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.7rem;
            font-weight: 700;
            color: var(--accent-main);
            background: rgba(15, 23, 42, 0.8);
            padding: 0.15rem 0.45rem;
            border-radius: 4px;
        }}

        .item-marks {{
            font-size: 0.68rem;
            font-weight: 700;
            color: #34d399;
        }}

        .item-title {{
            font-size: 0.82rem;
            font-weight: 700;
            color: var(--text-main);
            line-height: 1.3;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }}

        /* Banner */
        .activity-banner {{
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            border-radius: 16px;
            padding: 1.25rem 1.5rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1.5rem;
            flex-wrap: wrap;
            box-shadow: var(--card-shadow);
        }}

        .banner-content {{
            flex: 1;
            min-width: 280px;
        }}

        .banner-tags {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin-bottom: 0.5rem;
            flex-wrap: wrap;
        }}

        .tag-subject {{
            font-size: 0.74rem;
            font-weight: 800;
            text-transform: uppercase;
            padding: 0.2rem 0.65rem;
            border-radius: 6px;
            background: rgba(56, 189, 248, 0.15);
            color: var(--accent-main);
            border: 1px solid var(--accent-main);
        }}

        .tag-marks {{
            font-size: 0.74rem;
            font-weight: 800;
            padding: 0.2rem 0.65rem;
            border-radius: 6px;
            background: rgba(16, 185, 129, 0.15);
            color: #34d399;
            border: 1px solid rgba(16, 185, 129, 0.4);
        }}

        .tag-freq {{
            font-size: 0.74rem;
            font-weight: 700;
            color: #fbbf24;
        }}

        .activity-title {{
            font-size: 1.35rem;
            font-weight: 900;
            letter-spacing: -0.02em;
            color: var(--text-main);
            margin-bottom: 0.4rem;
            line-height: 1.25;
        }}

        .activity-desc {{
            font-size: 0.88rem;
            color: var(--text-body);
            line-height: 1.5;
            max-width: 820px;
        }}

        /* Progress Pill */
        .progress-stat-pill {{
            display: flex;
            align-items: center;
            gap: 0.85rem;
            background: var(--bg-card);
            border: 1px solid var(--border-subtle);
            border-radius: 12px;
            padding: 0.65rem 1.15rem;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        }}

        .progress-circle-wrap {{
            position: relative;
            width: 52px;
            height: 52px;
        }}

        .progress-circle-svg {{
            transform: rotate(-90deg);
        }}

        .circle-bg {{
            fill: none;
            stroke: var(--border-subtle);
            stroke-width: 5;
        }}

        .circle-bar {{
            fill: none;
            stroke: #10b981;
            stroke-width: 5;
            stroke-dasharray: 138;
            stroke-dashoffset: 138;
            stroke-linecap: round;
            transition: stroke-dashoffset 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }}

        .progress-pct-text {{
            position: absolute;
            inset: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.82rem;
            font-weight: 800;
            color: #34d399;
            font-family: 'JetBrains Mono', monospace;
        }}

        .progress-labels {{
            display: flex;
            flex-direction: column;
        }}

        .progress-count-text {{
            font-size: 1.05rem;
            font-weight: 800;
            color: var(--text-main);
            font-family: 'JetBrains Mono', monospace;
        }}

        .progress-subtext {{
            font-size: 0.72rem;
            color: var(--text-muted);
            text-transform: uppercase;
            font-weight: 600;
        }}

        /* Canvas Workspace Card */
        .canvas-card {{
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            border-radius: 18px;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            box-shadow: var(--card-shadow);
        }}

        .canvas-toolbar {{
            background: var(--bg-card);
            border-bottom: 1px solid var(--border-subtle);
            padding: 0.65rem 1.25rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 0.75rem;
            flex-wrap: wrap;
        }}

        .toolbar-group {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
            flex-wrap: wrap;
        }}

        .tool-btn {{
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            padding: 0.42rem 0.85rem;
            border-radius: 8px;
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            color: var(--text-main);
            font-size: 0.78rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
            user-select: none;
        }}

        .tool-btn:hover {{
            background: var(--bg-card-hover);
            border-color: var(--border-focus);
            transform: translateY(-1px);
        }}

        .tool-btn:active {{
            transform: translateY(0);
        }}

        .tool-btn.primary {{
            background: #0284c7;
            border-color: #38bdf8;
            color: #ffffff;
            box-shadow: 0 0 12px rgba(56, 189, 248, 0.3);
        }}

        .tool-btn.primary:hover {{
            filter: brightness(1.1);
        }}

        .tool-btn.amber {{
            background: #d97706;
            border-color: #fbbf24;
            color: #ffffff;
            box-shadow: 0 0 12px rgba(251, 191, 36, 0.3);
        }}

        .tool-btn.success {{
            background: #059669;
            border-color: #10b981;
            color: #ffffff;
        }}

        .ghost-slider-group {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            padding: 0.3rem 0.75rem;
            border-radius: 8px;
            font-size: 0.76rem;
            color: var(--text-muted);
            font-weight: 600;
        }}

        .ghost-slider-group input[type="range"] {{
            width: 80px;
            accent-color: var(--accent-main);
            cursor: pointer;
        }}

        /* Interactive Vector Stage */
        .stage-wrapper {{
            position: relative;
            width: 100%;
            height: 520px;
            background-color: #070912;
            background-image: 
                radial-gradient(rgba(56, 189, 248, 0.1) 1px, transparent 1px),
                linear-gradient(to right, rgba(255, 255, 255, 0.02) 1px, transparent 1px),
                linear-gradient(to bottom, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
            background-size: 24px 24px, 48px 48px, 48px 48px;
            overflow: hidden;
            touch-action: none;
            cursor: crosshair;
        }}

        @media (max-width: 768px) {{
            .stage-wrapper {{
                height: 420px;
            }}
        }}

        @media (max-width: 480px) {{
            .stage-wrapper {{
                height: 360px;
            }}
        }}

        .circuit-svg {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
        }}

        .ink-canvas {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            touch-action: none;
            z-index: 5;
        }}

        .particles-canvas {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 10;
        }}

        /* Ghost Blueprint Elements */
        .ghost-stroke {{
            stroke: #475569;
            stroke-width: 2;
            stroke-dasharray: 4, 4;
            fill: none;
            transition: opacity 0.25s ease;
        }}

        .ghost-fill {{
            fill: #1e293b;
            fill-opacity: 0.15;
            stroke: #475569;
            stroke-width: 1.5;
            stroke-dasharray: 4, 4;
        }}

        /* Snapped Active Components */
        .active-comp {{
            opacity: 0;
            transition: opacity 0.3s cubic-bezier(0.16, 1, 0.3, 1), transform 0.3s ease;
            transform-origin: center;
        }}

        .active-comp.snapped {{
            opacity: 1;
            animation: snapPop 0.4s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
        }}

        @keyframes snapPop {{
            0% {{
                opacity: 0;
                transform: scale(0.92);
                filter: drop-shadow(0 0 20px #fff);
            }}
            50% {{
                transform: scale(1.04);
            }}
            100% {{
                opacity: 1;
                transform: scale(1);
            }}
        }}

        .spotlight-pulse {{
            animation: spotlightPulse 0.6s infinite alternate !important;
            opacity: 0.85 !important;
        }}

        @keyframes spotlightPulse {{
            from {{ filter: drop-shadow(0 0 8px #fbbf24); }}
            to {{ filter: drop-shadow(0 0 24px #00f2fe); }}
        }}

        /* Floating Hint */
        .swipe-hint-pill {{
            position: absolute;
            bottom: 1rem;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(15, 23, 42, 0.88);
            backdrop-filter: blur(8px);
            border: 1px solid var(--accent-main);
            color: var(--accent-main);
            font-size: 0.78rem;
            font-weight: 700;
            padding: 0.4rem 1.15rem;
            border-radius: 9999px;
            pointer-events: none;
            z-index: 15;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
            white-space: nowrap;
        }}

        /* Checklist */
        .checklist-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
            gap: 0.65rem;
            padding: 1.25rem;
            background: var(--bg-card);
            border-top: 1px solid var(--border-subtle);
        }}

        .check-item {{
            display: flex;
            align-items: center;
            gap: 0.65rem;
            padding: 0.45rem 0.75rem;
            border-radius: 8px;
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            font-size: 0.78rem;
            color: var(--text-muted);
            transition: all 0.25s ease;
            user-select: none;
        }}

        .check-item.done {{
            border-color: #10b981;
            background: rgba(16, 185, 129, 0.08);
            color: var(--text-main);
            font-weight: 600;
        }}

        .check-icon {{
            font-size: 0.95rem;
            margin-left: auto;
        }}

        .check-item.done .check-icon {{
            color: #10b981;
        }}

        .color-dot {{
            width: 10px;
            height: 10px;
            border-radius: 50%;
            display: inline-block;
            flex-shrink: 0;
        }}

        /* Victory Modal Popup */
        .victory-overlay {{
            position: fixed;
            inset: 0;
            background: rgba(8, 11, 17, 0.85);
            backdrop-filter: blur(8px);
            z-index: 1000;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 1.5rem;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.35s ease;
        }}

        .victory-overlay.visible {{
            opacity: 1;
            pointer-events: auto;
        }}

        .victory-card {{
            background: linear-gradient(135deg, #151e32 0%, #0d1322 100%);
            border: 2px solid #10b981;
            border-radius: 20px;
            padding: 2.25rem;
            max-width: 540px;
            width: 100%;
            text-align: center;
            box-shadow: 0 20px 60px rgba(16, 185, 129, 0.3), 0 0 80px rgba(0, 0, 0, 0.8);
            transform: scale(0.85);
            transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        }}

        .victory-overlay.visible .victory-card {{
            transform: scale(1);
        }}

        .victory-badge {{
            font-size: 3.5rem;
            margin-bottom: 0.5rem;
            animation: bounce 1s infinite alternate;
        }}

        @keyframes bounce {{
            from {{ transform: translateY(0); }}
            to {{ transform: translateY(-8px); }}
        }}

        .victory-title {{
            font-size: 1.6rem;
            font-weight: 900;
            color: #34d399;
            margin-bottom: 0.5rem;
            letter-spacing: -0.01em;
        }}

        .victory-desc {{
            font-size: 0.92rem;
            color: var(--text-body);
            line-height: 1.5;
            margin-bottom: 1.5rem;
        }}

        .victory-stats-row {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 0.75rem;
            margin-bottom: 1.5rem;
        }}

        .victory-stat-box {{
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            border-radius: 10px;
            padding: 0.75rem 0.5rem;
        }}

        .stat-value {{
            font-size: 1.15rem;
            font-weight: 800;
            color: #fbbf24;
            font-family: 'JetBrains Mono', monospace;
        }}

        .stat-label-mini {{
            font-size: 0.68rem;
            color: var(--text-muted);
            text-transform: uppercase;
            font-weight: 700;
            margin-top: 0.2rem;
        }}

        .victory-btn-row {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.75rem;
            flex-wrap: wrap;
        }}

        /* Theory Guide Card */
        .theory-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-subtle);
            border-radius: 14px;
            padding: 1.25rem 1.5rem;
            display: flex;
            flex-direction: column;
            gap: 0.85rem;
        }}

        .theory-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 0.75rem;
            border-bottom: 1px solid var(--border-subtle);
            padding-bottom: 0.65rem;
        }}

        .theory-title {{
            font-size: 1rem;
            font-weight: 700;
            color: #fbbf24;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .theory-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1rem;
        }}

        .theory-item {{
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            border-radius: 10px;
            padding: 0.85rem 1rem;
        }}

        .theory-item h4 {{
            font-size: 0.85rem;
            font-weight: 700;
            color: #38bdf8;
            margin-bottom: 0.35rem;
        }}

        .theory-item p, .theory-item div {{
            font-size: 0.84rem;
            color: var(--text-body);
            line-height: 1.45;
        }}
    </style>
</head>
<body>

    <!-- Header Navigation -->
    <header class="site-header">
        <a href="index.html" class="brand-link">
            <span style="font-size:1.35rem;">⚡</span>
            <span>KTU Muscle Memory Lab</span>
            <span class="brand-badge">{html.escape(subject_name)}</span>
        </a>

        <nav class="nav-pills">
            <a href="index.html" class="nav-pill">📚 Question Bank</a>
            <a href="draw.html" class="nav-pill">🎨 Master Hub</a>
            <a href="draw_drives.html" class="nav-pill {'active' if subject_key == 'DRIVES' else ''}">⚡ Electric Drives</a>
            <a href="draw_acs.html" class="nav-pill {'active' if subject_key == 'ACS' else ''}">🌀 Control Systems</a>
            <a href="draw_mobile.html" class="nav-pill {'active' if subject_key == 'MOBILE' else ''}">📱 Mobile Computing</a>
            <a href="mindmap.html" class="nav-pill">🧠 Mind Map</a>
            <a href="activities.html" class="nav-pill">🎯 Focus Lab</a>
            <a href="animations.html" class="nav-pill">🎬 60fps Simulators</a>
        </nav>
    </header>

    <!-- Subject Switcher Bar -->
    <div class="subject-switcher-bar">
        <div class="subject-tabs">
            <a href="draw_drives.html" class="subject-tab {'active' if subject_key == 'DRIVES' else ''}">⚡ Electric Drives (EET413)</a>
            <a href="draw_acs.html" class="subject-tab {'active' if subject_key == 'ACS' else ''}">🌀 Advanced Control Systems (EET401)</a>
            <a href="draw_mobile.html" class="subject-tab {'active' if subject_key == 'MOBILE' else ''}">📱 Mobile Computing (CST415)</a>
        </div>
        <span style="font-size:0.75rem; color:var(--text-muted); font-weight:600;">{len(diagrams)} Interactive Vector Blueprints</span>
    </div>

    <main class="lab-container">

        <!-- Diagram Selector Carousel -->
        <section class="diagram-selector-card">
            <div class="selector-header">
                <span class="selector-title">📐 Select Exam Question to Draw:</span>
                <span style="font-size:0.75rem; color:var(--text-muted);">Swipe or click blueprint</span>
            </div>
            <div class="diagram-carousel" id="diagram-carousel">
                <!-- Dynamically populated via JS -->
            </div>
        </section>

        <!-- Activity Info Banner -->
        <section class="activity-banner">
            <div class="banner-content">
                <div class="banner-tags">
                    <span class="tag-subject" id="banner-subject-pill">EET413</span>
                    <span class="tag-marks" id="banner-marks-pill">7 Marks</span>
                    <span class="tag-freq" id="banner-qid-pill">QID</span>
                </div>
                <h1 class="activity-title" id="banner-title">Diagram Title</h1>
                <p class="activity-desc" id="banner-desc">
                    Swipe with your finger, stylus, or mouse near any circuit element. The <strong>magnetic tracer</strong> snaps the vector lines into vibrant glowing neon schematics!
                </p>
            </div>

            <!-- Progress Ring -->
            <div class="progress-stat-pill">
                <div class="progress-circle-wrap">
                    <svg class="progress-circle-svg" width="52" height="52" viewBox="0 0 52 52">
                        <circle class="circle-bg" cx="26" cy="26" r="22"></circle>
                        <circle class="circle-bar" id="progress-bar-circle" cx="26" cy="26" r="22"></circle>
                    </svg>
                    <div class="progress-pct-text" id="progress-pct-text">0%</div>
                </div>
                <div class="progress-labels">
                    <span class="progress-count-text" id="progress-count-text">0 / 0</span>
                    <span class="progress-subtext">Components Snapped</span>
                </div>
            </div>
        </section>

        <!-- Canvas Workspace Card -->
        <section class="canvas-card">
            <!-- Toolbar -->
            <div class="canvas-toolbar">
                <div class="toolbar-group">
                    <button class="tool-btn primary" id="btn-auto-draw" title="Watch full guided drawing demo">
                        <span>▶️</span> <span>Watch Demo</span>
                    </button>
                    <button class="tool-btn amber" id="btn-hint" title="Spotlight next stroke to draw">
                        <span>💡</span> <span>Next Hint</span>
                    </button>
                    <button class="tool-btn" id="btn-undo" title="Undo last snapped component">
                        <span>↩️</span> <span>Undo</span>
                    </button>
                    <button class="tool-btn" id="btn-reset" title="Reset canvas and start over">
                        <span>🔄</span> <span>Reset</span>
                    </button>
                </div>

                <div class="toolbar-group">
                    <!-- Ghost Opacity Slider -->
                    <div class="ghost-slider-group">
                        <span>👻 Guide Opacity:</span>
                        <input type="range" id="ghost-opacity-slider" min="0" max="100" value="25" title="Ghost guide transparency">
                        <span id="ghost-opacity-val">25%</span>
                    </div>

                    <!-- Audio Toggle -->
                    <button class="tool-btn" id="btn-sound-toggle" title="Toggle sound chimes">
                        <span id="sound-icon">🔊</span>
                    </button>
                </div>
            </div>

            <!-- Stage: Vector Circuit + Touch Canvas -->
            <div class="stage-wrapper" id="stage-wrapper">
                <!-- SVG Vector Circuit Stage -->
                <svg class="circuit-svg" id="circuit-svg" viewBox="0 0 1000 580" preserveAspectRatio="xMidYMid meet">
                    <defs>
                        <!-- Glow filters -->
                        <filter id="glow-gold" x="-20%" y="-20%" width="140%" height="140%">
                            <feGaussianBlur stdDeviation="3" result="blur" />
                            <feComposite in="SourceGraphic" in2="blur" operator="over" />
                        </filter>
                        <filter id="glow-cyan" x="-20%" y="-20%" width="140%" height="140%">
                            <feGaussianBlur stdDeviation="4" result="blur" />
                            <feComposite in="SourceGraphic" in2="blur" operator="over" />
                        </filter>
                        <filter id="glow-green" x="-20%" y="-20%" width="140%" height="140%">
                            <feGaussianBlur stdDeviation="4" result="blur" />
                            <feComposite in="SourceGraphic" in2="blur" operator="over" />
                        </filter>
                        <filter id="glow-pink" x="-20%" y="-20%" width="140%" height="140%">
                            <feGaussianBlur stdDeviation="5" result="blur" />
                            <feComposite in="SourceGraphic" in2="blur" operator="over" />
                        </filter>
                        <marker id="arrow-wire" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                            <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#38bdf8"/>
                        </marker>
                    </defs>

                    <!-- 1. GHOST BLUEPRINT UNDERLAY -->
                    <g id="ghost-blueprint-group" opacity="0.25">
                        <!-- Injected via JS -->
                    </g>

                    <!-- 2. ACTIVE SNAPPED COMPONENTS -->
                    <g id="active-components-group">
                        <!-- Injected via JS -->
                    </g>
                </svg>

                <!-- Freehand User Stroke Layer -->
                <canvas class="ink-canvas" id="ink-canvas"></canvas>

                <!-- Spark Particles Layer -->
                <canvas class="particles-canvas" id="particles-canvas"></canvas>

                <!-- Floating Swipe Hint -->
                <div class="swipe-hint-pill" id="swipe-hint-pill">
                    <span>✨ Swipe or trace near any dotted line to snap!</span>
                </div>
            </div>

            <!-- Real-time Component Checklist -->
            <div class="checklist-grid" id="checklist-grid">
                <!-- Injected via JS -->
            </div>
        </section>

        <!-- Governing Formula & Theory Guide Card -->
        <section class="theory-card">
            <div class="theory-header">
                <div class="theory-title">
                    <span>📐</span> <span id="theory-title-text">Exam Warfare &amp; Governing Equations</span>
                </div>
                <span style="font-size:0.75rem; color:#34d399; font-weight:700;">KTU 40/30/30 Scoring Protocol</span>
            </div>
            <div class="theory-grid">
                <div class="theory-item">
                    <h4>Governing Mathematical Formula</h4>
                    <div id="theory-formula-box"></div>
                </div>
                <div class="theory-item">
                    <h4>Examiner Marking Criteria</h4>
                    <p id="theory-marking-text"></p>
                </div>
            </div>
        </section>

    </main>

    <!-- Victory Modal Popup -->
    <div class="victory-overlay" id="victory-overlay">
        <div class="victory-card">
            <div class="victory-badge">🏆</div>
            <h2 class="victory-title">Blueprint Mastered!</h2>
            <p class="victory-desc">
                Full muscle memory locked in! You traced all components with exact spatial precision. Your neural motor pathways are now primed for full marks in the 3-hour university exam!
            </p>
            <div class="victory-stats-row">
                <div class="victory-stat-box">
                    <div class="stat-value" id="final-accuracy">100%</div>
                    <div class="stat-label-mini">Accuracy</div>
                </div>
                <div class="victory-stat-box">
                    <div class="stat-value" id="final-time">00:32</div>
                    <div class="stat-label-mini">Time Taken</div>
                </div>
                <div class="victory-stat-box">
                    <div class="stat-value" id="final-score">7 / 7</div>
                    <div class="stat-label-mini">Exam Marks</div>
                </div>
            </div>
            <div class="victory-btn-row">
                <button class="tool-btn amber" id="btn-practice-again">
                    <span>🔄</span> <span>Practice Again</span>
                </button>
                <button class="tool-btn primary" id="btn-next-diagram">
                    <span>▶️</span> <span>Next Diagram</span>
                </button>
            </div>
        </div>
    </div>

    <!-- Application Script -->
    <script>
        (function() {{
            const DIAGRAMS = {diagrams_json};
            let currentDiagramIdx = 0;
            let currentComponents = [];
            let snappedComponents = new Set();
            let historyStack = [];
            let isDrawing = false;
            let lastPoint = null;
            let startTime = null;
            let timerInterval = null;
            let soundEnabled = true;
            let isAutoDrawing = false;

            // DOM Elements
            const carousel = document.getElementById('diagram-carousel');
            const stageWrapper = document.getElementById('stage-wrapper');
            const circuitSvg = document.getElementById('circuit-svg');
            const ghostGroup = document.getElementById('ghost-blueprint-group');
            const activeGroup = document.getElementById('active-components-group');
            const inkCanvas = document.getElementById('ink-canvas');
            const particlesCanvas = document.getElementById('particles-canvas');
            const inkCtx = inkCanvas.getContext('2d');
            const partCtx = particlesCanvas.getContext('2d');

            const ghostSlider = document.getElementById('ghost-opacity-slider');
            const ghostValText = document.getElementById('ghost-opacity-val');
            const progressBarCircle = document.getElementById('progress-bar-circle');
            const progressPctText = document.getElementById('progress-pct-text');
            const progressCountText = document.getElementById('progress-count-text');
            const swipeHintText = document.getElementById('swipe-hint-pill');
            const checklistGrid = document.getElementById('checklist-grid');
            const victoryOverlay = document.getElementById('victory-overlay');
            const finalTimeText = document.getElementById('final-time');

            const bannerSubjectPill = document.getElementById('banner-subject-pill');
            const bannerMarksPill = document.getElementById('banner-marks-pill');
            const bannerQidPill = document.getElementById('banner-qid-pill');
            const bannerTitle = document.getElementById('banner-title');
            const bannerDesc = document.getElementById('banner-desc');
            const theoryFormulaBox = document.getElementById('theory-formula-box');
            const theoryMarkingText = document.getElementById('theory-marking-text');

            // Web Audio Synthesis
            let audioCtx = null;
            function playChime(freq = 587.33, type = 'sine', duration = 0.25) {{
                if (!soundEnabled) return;
                try {{
                    if (!audioCtx) {{
                        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                    }}
                    if (audioCtx.state === 'suspended') audioCtx.resume();
                    const osc = audioCtx.createOscillator();
                    const gain = audioCtx.createGain();
                    osc.type = type;
                    osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
                    gain.gain.setValueAtTime(0.2, audioCtx.currentTime);
                    gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration);
                    osc.connect(gain);
                    gain.connect(audioCtx.destination);
                    osc.start();
                    osc.stop(audioCtx.currentTime + duration);
                }} catch(e) {{}}
            }}

            function playVictoryChime() {{
                if (!soundEnabled) return;
                const notes = [523.25, 659.25, 783.99, 1046.50];
                notes.forEach((n, i) => {{
                    setTimeout(() => playChime(n, 'triangle', 0.4), i * 120);
                }});
            }}

            // Responsive Canvas Resize
            function resizeCanvases() {{
                const rect = stageWrapper.getBoundingClientRect();
                if (!rect || rect.width <= 0 || rect.height <= 0) return;
                const dpr = window.devicePixelRatio || 1;

                inkCanvas.width = rect.width * dpr;
                inkCanvas.height = rect.height * dpr;
                inkCanvas.style.width = rect.width + 'px';
                inkCanvas.style.height = rect.height + 'px';
                inkCtx.scale(dpr, dpr);

                particlesCanvas.width = rect.width * dpr;
                particlesCanvas.height = rect.height * dpr;
                particlesCanvas.style.width = rect.width + 'px';
                particlesCanvas.style.height = rect.height + 'px';
                partCtx.scale(dpr, dpr);
            }}

            window.addEventListener('resize', resizeCanvases);
            window.addEventListener('orientationchange', () => setTimeout(resizeCanvases, 150));
            setTimeout(resizeCanvases, 50);

            // Coordinates Normalization (SVG 1000x580 to Screen)
            const SVG_VIEW_WIDTH = 1000;
            const SVG_VIEW_HEIGHT = 580;

            function screenToSvgCoords(clientX, clientY) {{
                const rect = stageWrapper.getBoundingClientRect();
                const screenX = clientX - rect.left;
                const screenY = clientY - rect.top;

                const stageRatio = rect.width / rect.height;
                const svgRatio = SVG_VIEW_WIDTH / SVG_VIEW_HEIGHT;

                let renderedWidth, renderedHeight, offsetX, offsetY;
                if (stageRatio > svgRatio) {{
                    renderedHeight = rect.height;
                    renderedWidth = rect.height * svgRatio;
                    offsetX = (rect.width - renderedWidth) / 2;
                    offsetY = 0;
                }} else {{
                    renderedWidth = rect.width;
                    renderedHeight = rect.width / svgRatio;
                    offsetX = 0;
                    offsetY = (rect.height - renderedHeight) / 2;
                }}

                const normalizedX = (screenX - offsetX) * (SVG_VIEW_WIDTH / renderedWidth);
                const normalizedY = (screenY - offsetY) * (SVG_VIEW_HEIGHT / renderedHeight);
                return {{ x: normalizedX, y: normalizedY }};
            }}

            function svgToScreenCoords(svgX, svgY) {{
                const rect = stageWrapper.getBoundingClientRect();
                const stageRatio = rect.width / rect.height;
                const svgRatio = SVG_VIEW_WIDTH / SVG_VIEW_HEIGHT;

                let renderedWidth, renderedHeight, offsetX, offsetY;
                if (stageRatio > svgRatio) {{
                    renderedHeight = rect.height;
                    renderedWidth = rect.height * svgRatio;
                    offsetX = (rect.width - renderedWidth) / 2;
                    offsetY = 0;
                }} else {{
                    renderedWidth = rect.width;
                    renderedHeight = rect.width / svgRatio;
                    offsetX = 0;
                    offsetY = (rect.height - renderedHeight) / 2;
                }}

                const screenX = offsetX + (svgX * (renderedWidth / SVG_VIEW_WIDTH));
                const screenY = offsetY + (svgY * (renderedHeight / SVG_VIEW_HEIGHT));
                return {{ x: screenX, y: screenY }};
            }}

            // Render Carousel Items
            function renderCarousel() {{
                carousel.innerHTML = '';
                DIAGRAMS.forEach((d, idx) => {{
                    const item = document.createElement('div');
                    item.className = `carousel-item ${{idx === currentDiagramIdx ? 'active' : ''}}`;
                    item.setAttribute('data-index', idx);
                    item.innerHTML = `
                        <div class="carousel-item-top">
                            <span class="item-qid">${{d.qid.toUpperCase()}}</span>
                            <span class="item-marks">${{d.marks}}</span>
                        </div>
                        <div class="item-title">${{d.title}}</div>
                    `;
                    item.addEventListener('click', () => {{
                        loadDiagram(idx);
                    }});
                    carousel.appendChild(item);
                }});
            }}

            // Load and Initialize Diagram
            function loadDiagram(idx) {{
                if (idx < 0 || idx >= DIAGRAMS.length) return;
                currentDiagramIdx = idx;
                const d = DIAGRAMS[idx];

                // Update Info Banner
                bannerSubjectPill.textContent = `{course_code} • Mod ${{d.module}}`;
                bannerMarksPill.textContent = d.marks;
                bannerQidPill.textContent = `★ Question ${{d.qid.toUpperCase()}}`;
                bannerTitle.textContent = d.title;
                bannerDesc.textContent = d.desc;

                // Update Theory & Math
                theoryFormulaBox.innerHTML = `$$${{d.equation}}$$`;
                theoryMarkingText.textContent = d.marking_tip;
                if (window.renderMathInElement) {{
                    window.renderMathInElement(theoryFormulaBox, {{
                        delimiters: [
                            {{left: '$$', right: '$$', display: true}},
                            {{left: '$', right: '$', display: false}}
                        ],
                        throwOnError: false
                    }});
                }}

                // Inject SVG Vector Elements
                ghostGroup.innerHTML = d.ghost_svg;
                activeGroup.innerHTML = d.active_svg;
                currentComponents = d.components || [];

                // Reset State
                snappedComponents.clear();
                historyStack = [];
                startTime = null;
                clearInterval(timerInterval);
                isAutoDrawing = false;
                victoryOverlay.classList.remove('visible');

                // Clear Inks
                const rect = stageWrapper.getBoundingClientRect();
                inkCtx.clearRect(0, 0, rect.width, rect.height);
                partCtx.clearRect(0, 0, rect.width, rect.height);

                // Build Checklist
                checklistGrid.innerHTML = '';
                currentComponents.forEach(comp => {{
                    const el = document.createElement('div');
                    el.className = 'check-item';
                    el.id = `chk-${{comp.id}}`;
                    el.innerHTML = `
                        <span class="color-dot" style="background:${{comp.color}}; box-shadow: 0 0 6px ${{comp.color}};"></span>
                        <span class="check-title">${{comp.name}}</span>
                        <span class="check-icon">○</span>
                    `;
                    checklistGrid.appendChild(el);
                }});

                // Update Active Carousel Card
                document.querySelectorAll('.carousel-item').forEach(card => {{
                    const cIdx = parseInt(card.getAttribute('data-index') || -1);
                    card.classList.toggle('active', cIdx === idx);
                }});

                const activeCard = document.querySelector(`.carousel-item[data-index="${{idx}}"]`);
                if (activeCard && typeof activeCard.scrollIntoView === 'function') {{
                    activeCard.scrollIntoView({{ behavior: 'smooth', block: 'nearest', inline: 'center' }});
                }}

                // Update URL Hash
                if (window.history && window.history.replaceState && d.qid) {{
                    window.history.replaceState(null, '', '#' + d.qid);
                }}

                updateProgressUI();
                swipeHintText.textContent = '✨ Swipe or trace near any dotted line to snap!';
                playChime(523.25, 'triangle', 0.2);
            }}

            // Particles Engine
            let particles = [];
            function emitSparks(screenX, screenY, color = '#38bdf8') {{
                const count = 22;
                for (let i = 0; i < count; i++) {{
                    const angle = Math.random() * Math.PI * 2;
                    const speed = 1.5 + Math.random() * 4.5;
                    particles.push({{
                        x: screenX,
                        y: screenY,
                        vx: Math.cos(angle) * speed,
                        vy: Math.sin(angle) * speed - 0.5,
                        life: 1.0,
                        decay: 0.02 + Math.random() * 0.02,
                        size: 2.5 + Math.random() * 3.5,
                        color: color
                    }});
                }}
            }}

            function updateParticles() {{
                const rect = stageWrapper.getBoundingClientRect();
                partCtx.clearRect(0, 0, rect.width, rect.height);

                for (let i = particles.length - 1; i >= 0; i--) {{
                    const p = particles[i];
                    p.x += p.vx;
                    p.y += p.vy;
                    p.vy += 0.08;
                    p.life -= p.decay;

                    if (p.life <= 0) {{
                        particles.splice(i, 1);
                        continue;
                    }}

                    partCtx.save();
                    partCtx.globalAlpha = p.life;
                    partCtx.fillStyle = p.color;
                    partCtx.shadowColor = p.color;
                    partCtx.shadowBlur = 8;
                    partCtx.beginPath();
                    partCtx.arc(p.x, p.y, p.size * p.life, 0, Math.PI * 2);
                    partCtx.fill();
                    partCtx.restore();
                }}
                requestAnimationFrame(updateParticles);
            }}
            requestAnimationFrame(updateParticles);

            // Magnetic Snap Check
            const SNAP_DISTANCE_THRESHOLD = 45;

            function checkProximityAndSnap(svgPoint, screenPoint) {{
                if (snappedComponents.size === 0 && !startTime) {{
                    startTime = Date.now();
                    timerInterval = setInterval(updateTimerDisplay, 1000);
                }}

                for (const comp of currentComponents) {{
                    if (snappedComponents.has(comp.id)) continue;

                    const dxCenter = svgPoint.x - comp.center.x;
                    const dyCenter = svgPoint.y - comp.center.y;
                    const distCenter = Math.sqrt(dxCenter * dxCenter + dyCenter * dyCenter);

                    let isClose = distCenter < comp.radius;

                    if (!isClose && comp.points) {{
                        for (const pt of comp.points) {{
                            const d = Math.hypot(svgPoint.x - pt.x, svgPoint.y - pt.y);
                            if (d <= SNAP_DISTANCE_THRESHOLD) {{
                                isClose = true;
                                break;
                            }}
                        }}
                    }}

                    if (isClose) {{
                        snapComponent(comp, screenPoint);
                        break;
                    }}
                }}
            }}

            function snapComponent(comp, screenPoint) {{
                if (snappedComponents.has(comp.id)) return;

                snappedComponents.add(comp.id);
                historyStack.push(comp.id);

                const el = document.getElementById(comp.id);
                if (el) {{
                    el.classList.add('snapped');
                }}

                const chk = document.getElementById(`chk-${{comp.id}}`);
                if (chk) {{
                    chk.classList.add('done');
                    chk.querySelector('.check-icon').textContent = '●';
                }}

                const pt = screenPoint || svgToScreenCoords(comp.center.x, comp.center.y);
                emitSparks(pt.x, pt.y, comp.color);
                playChime(440 + snappedComponents.size * 55, 'triangle', 0.28);
                if (navigator.vibrate) navigator.vibrate(25);

                updateProgressUI();

                if (snappedComponents.size === currentComponents.length) {{
                    handleVictory();
                }} else {{
                    swipeHintText.textContent = `🎯 Snapped: ${{comp.name}}! Keep tracing!`;
                }}
            }}

            function updateProgressUI() {{
                const total = currentComponents.length;
                const count = snappedComponents.size;
                const pct = total > 0 ? Math.round((count / total) * 100) : 0;

                progressCountText.textContent = `${{count}} / ${{total}}`;
                progressPctText.textContent = `${{pct}}%`;

                const offset = 138 - (138 * (total > 0 ? count / total : 0));
                progressBarCircle.style.strokeDashoffset = offset;
            }}

            function updateTimerDisplay() {{
                if (!startTime) return;
                const sec = Math.floor((Date.now() - startTime) / 1000);
                const m = String(Math.floor(sec / 60)).padStart(2, '0');
                const s = String(sec % 60).padStart(2, '0');
                finalTimeText.textContent = `${{m}}:${{s}}`;
            }}

            function handleVictory() {{
                clearInterval(timerInterval);
                playVictoryChime();

                for (let i = 0; i < 5; i++) {{
                    setTimeout(() => {{
                        const rect = stageWrapper.getBoundingClientRect();
                        const rx = rect.width * (0.2 + Math.random() * 0.6);
                        const ry = rect.height * (0.2 + Math.random() * 0.6);
                        emitSparks(rx, ry, ['#fbbf24', '#00f2fe', '#10b981', '#f43f5e', '#c084fc'][i % 5]);
                    }}, i * 180);
                }}

                setTimeout(() => {{
                    victoryOverlay.classList.add('visible');
                }}, 800);
            }}

            // Pointer Drawing Engine
            function getPointerPos(e) {{
                const rect = stageWrapper.getBoundingClientRect();
                const clientX = e.clientX !== undefined ? e.clientX : (e.touches && e.touches[0] ? e.touches[0].clientX : 0);
                const clientY = e.clientY !== undefined ? e.clientY : (e.touches && e.touches[0] ? e.touches[0].clientY : 0);
                return {{
                    clientX,
                    clientY,
                    screenX: clientX - rect.left,
                    screenY: clientY - rect.top,
                    svg: screenToSvgCoords(clientX, clientY)
                }};
            }}

            function handlePointerDown(e) {{
                isDrawing = true;
                if (e.cancelable) e.preventDefault();
                if (e.target && e.target.setPointerCapture && e.pointerId !== undefined) {{
                    try {{ e.target.setPointerCapture(e.pointerId); }} catch(err) {{}}
                }}
                const pos = getPointerPos(e);
                lastPoint = {{ x: pos.screenX, y: pos.screenY }};
                checkProximityAndSnap(pos.svg, {{ x: pos.screenX, y: pos.screenY }});
            }}

            function handlePointerMove(e) {{
                if (!isDrawing) return;
                if (e.cancelable) e.preventDefault();

                const pos = getPointerPos(e);

                inkCtx.save();
                inkCtx.strokeStyle = 'rgba(56, 189, 248, 0.45)';
                inkCtx.lineWidth = 4;
                inkCtx.lineCap = 'round';
                inkCtx.lineJoin = 'round';
                inkCtx.shadowColor = '#00f2fe';
                inkCtx.shadowBlur = 6;
                inkCtx.beginPath();
                inkCtx.moveTo(lastPoint.x, lastPoint.y);
                inkCtx.lineTo(pos.screenX, pos.screenY);
                inkCtx.stroke();
                inkCtx.restore();

                lastPoint = {{ x: pos.screenX, y: pos.screenY }};
                checkProximityAndSnap(pos.svg, {{ x: pos.screenX, y: pos.screenY }});
            }}

            function handlePointerUp(e) {{
                isDrawing = false;
                if (e && e.target && e.target.releasePointerCapture && e.pointerId !== undefined) {{
                    try {{ e.target.releasePointerCapture(e.pointerId); }} catch(err) {{}}
                }}
            }}

            stageWrapper.addEventListener('pointerdown', handlePointerDown);
            window.addEventListener('pointermove', handlePointerMove, {{ passive: false }});
            window.addEventListener('pointerup', handlePointerUp);
            window.addEventListener('pointercancel', handlePointerUp);

            // Watch Demo Button
            document.getElementById('btn-auto-draw').addEventListener('click', function() {{
                if (isAutoDrawing) return;
                isAutoDrawing = true;
                this.classList.add('success');
                this.innerHTML = '<span>⏸️</span> <span>Playing...</span>';

                if (snappedComponents.size === currentComponents.length) {{
                    resetCanvas();
                }}

                let idx = 0;
                function drawNextStep() {{
                    if (idx < currentComponents.length) {{
                        const comp = currentComponents[idx];
                        if (!snappedComponents.has(comp.id)) {{
                            const pt = svgToScreenCoords(comp.center.x, comp.center.y);
                            snapComponent(comp, pt);
                        }}
                        idx++;
                        setTimeout(drawNextStep, 500);
                    }} else {{
                        isAutoDrawing = false;
                        document.getElementById('btn-auto-draw').classList.remove('success');
                        document.getElementById('btn-auto-draw').innerHTML = '<span>▶️</span> <span>Watch Demo</span>';
                    }}
                }}
                drawNextStep();
            }});

            // Next Hint Button
            document.getElementById('btn-hint').addEventListener('click', function() {{
                const nextComp = currentComponents.find(c => !snappedComponents.has(c.id));
                if (!nextComp) return;

                const pt = svgToScreenCoords(nextComp.center.x, nextComp.center.y);
                emitSparks(pt.x, pt.y, nextComp.color);
                playChime(659.25, 'sine', 0.2);
                swipeHintText.textContent = `👉 Hint: Swipe near ${{nextComp.name}}!`;

                const ghostEl = document.getElementById(nextComp.id);
                if (ghostEl) {{
                    ghostEl.classList.add('spotlight-pulse');
                    setTimeout(() => ghostEl.classList.remove('spotlight-pulse'), 1800);
                }}
            }});

            // Undo Button
            document.getElementById('btn-undo').addEventListener('click', function() {{
                if (historyStack.length === 0) return;
                const lastId = historyStack.pop();
                snappedComponents.delete(lastId);

                const el = document.getElementById(lastId);
                if (el) el.classList.remove('snapped');

                const chk = document.getElementById(`chk-${{lastId}}`);
                if (chk) {{
                    chk.classList.remove('done');
                    chk.querySelector('.check-icon').textContent = '○';
                }}

                updateProgressUI();
                swipeHintText.textContent = 'Undone. Swipe again to snap!';
            }});

            // Reset Button
            function resetCanvas() {{
                snappedComponents.clear();
                historyStack = [];
                startTime = null;
                clearInterval(timerInterval);

                currentComponents.forEach(c => {{
                    const el = document.getElementById(c.id);
                    if (el) el.classList.remove('snapped');
                    const chk = document.getElementById(`chk-${{c.id}}`);
                    if (chk) {{
                        chk.classList.remove('done');
                        chk.querySelector('.check-icon').textContent = '○';
                    }}
                }});

                const rect = stageWrapper.getBoundingClientRect();
                inkCtx.clearRect(0, 0, rect.width, rect.height);
                partCtx.clearRect(0, 0, rect.width, rect.height);
                victoryOverlay.classList.remove('visible');

                updateProgressUI();
                swipeHintText.textContent = 'Canvas reset! Swipe near any line to begin.';
            }}

            document.getElementById('btn-reset').addEventListener('click', resetCanvas);
            document.getElementById('btn-practice-again').addEventListener('click', resetCanvas);
            document.getElementById('btn-next-diagram').addEventListener('click', () => {{
                victoryOverlay.classList.remove('visible');
                loadDiagram((currentDiagramIdx + 1) % DIAGRAMS.length);
            }});

            // Ghost Opacity Slider
            ghostSlider.addEventListener('input', function() {{
                const val = this.value;
                ghostValText.textContent = `${{val}}%`;
                ghostGroup.setAttribute('opacity', (val / 100).toFixed(2));
            }});

            // Sound Toggle
            document.getElementById('btn-sound-toggle').addEventListener('click', function() {{
                soundEnabled = !soundEnabled;
                document.getElementById('sound-icon').textContent = soundEnabled ? '🔊' : '🔇';
            }});

            // Initial Launch & Hash Router
            renderCarousel();

            function selectFromHash() {{
                const hash = (window.location.hash || '').replace('#', '').trim().toLowerCase();
                if (hash) {{
                    let foundIdx = DIAGRAMS.findIndex(d => (d.qid || '').toLowerCase() === hash);
                    if (foundIdx === -1) {{
                        foundIdx = DIAGRAMS.findIndex(d => {{
                            const arr = (d.aliases || []);
                            return arr.some(a => a.toLowerCase() === hash);
                        }});
                    }}
                    if (foundIdx !== -1) {{
                        loadDiagram(foundIdx);
                        return true;
                    }}
                }}
                return false;
            }}

            if (!selectFromHash()) {{
                loadDiagram(0);
            }}

            window.addEventListener('hashchange', () => {{
                selectFromHash();
            }});

        }})();
    </script>
</body>
</html>"""

    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(page_html)
    print(f"Generated {output_filename} successfully ({len(diagrams)} interactive vector blueprints, {len(page_html)} bytes).")

def main():
    print("Building Interactive Vector Muscle Memory Labs...")
    generate_interactive_lab("DRIVES", "Electric Drives", "EET413", "#f59e0b", DRIVES_DIAGRAMS, "draw_drives.html")
    generate_interactive_lab("ACS", "Advanced Control Systems", "EET401", "#38bdf8", ACS_DIAGRAMS, "draw_acs.html")
    generate_interactive_lab("MOBILE", "Mobile Computing", "CST415", "#10b981", MOBILE_DIAGRAMS, "draw_mobile.html")

if __name__ == "__main__":
    main()
