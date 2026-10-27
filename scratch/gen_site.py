# -*- coding: utf-8 -*-
"""
Master Website Generator: Creates index.html (3-in-1 unified portal) and standalone pages.
Features:
- 3 Ergonomic Study & Reading Themes:
  1. Deep Charcoal & Warm Ivory (Night Mode) - 🌙
  2. Warm Slate & Off-White (Day Mode) - ☀️
  3. Sage & Soft Olive (Cool Focus Mode) - 🍃
- Theme switcher buttons with icons and LocalStorage persistence
- KaTeX math support via CDN auto-render
- 3 web pages integrated into one index page with smooth tab switching
- Module filters and live search bar
- Paragraph-style elaborated answers (3 marks: half page+, 7 marks: full page+)
- Image placeholders with explicit paths
- YouTube problem-solving link buttons
- Compact non-sticky header and floating Back to Top button
"""

import sys, os, html
from gen_acs import ACS_MODULES
from gen_drive import DRIVE_MODULES
from gen_mobile import MOBILE_SYLLABUS, MOBILE_MODULES
from byheart_data import get_byheart_card_html
from exam_questions import EXAM_QUESTIONS_MAP

def render_image_box(img_path, img_caption):
    exists = os.path.exists(img_path)
    real_class = 'has-real-image' if exists else 'missing-image'
    return f"""
    <div class="image-placeholder-container {real_class}">
        <div class="image-wrapper">
            <img src="{img_path}" alt="{html.escape(img_caption)}" class="diagram-img" onerror="this.closest('.image-placeholder-container').classList.remove('has-real-image'); this.closest('.image-placeholder-container').classList.add('missing-image');">
            <div class="placeholder-fallback">
                <div class="ph-icon">🖼️</div>
                <div class="ph-title">Diagram / Schematic Placeholder</div>
                <div class="ph-desc">{html.escape(img_caption)}</div>
                <div class="ph-path-badge"><code>{html.escape(img_path)}</code></div>
                <div class="ph-note">Place your image file at this exact location to display it here.</div>
            </div>
        </div>
        <p class="diagram-caption"><strong>Figure Caption:</strong> {html.escape(img_caption)} <span class="file-path-tag">[{html.escape(img_path)}]</span></p>
    </div>
    """

def render_youtube_btn(query, title):
    encoded_query = html.escape(query.replace(' ', '+'))
    return f"""
    <a href="https://www.youtube.com/results?search_query={encoded_query}" target="_blank" rel="noopener noreferrer" class="yt-button" title="Watch video solution on YouTube">
        <svg class="yt-icon" viewBox="0 0 24 24" width="20" height="20" fill="currentColor">
            <path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/>
        </svg>
        <span>Watch Video Solution</span>
    </a>
    """

def format_paragraphs(text):
    paragraphs = [p.strip() for p in text.strip().split('\n\n') if p.strip()]
    formatted = []
    for p in paragraphs:
        if p.startswith('$$') and p.endswith('$$'):
            formatted.append(f'<div class="katex-display-block">{p}</div>')
        else:
            formatted.append(f'<p class="answer-para">{p}</p>')
    return '\n'.join(formatted)

def render_question_card(q, subject_class):
    actual_question = EXAM_QUESTIONS_MAP.get(q["qid"], q["title"])
    marks_badge = f'<span class="badge badge-3m">3 Marks (Short Answer)</span>' if q["marks"] == 3 else f'<span class="badge badge-7m">7/14 Marks (Long Essay / Derivation)</span>'
    duration_sec = 300 if q["marks"] == 3 else 720
    duration_str = "05:00" if q["marks"] == 3 else "12:00"
    timer_widget = f'''<div class="card-timer-widget" id="timer-{q['qid']}" data-duration="{duration_sec}" data-qid="{q['qid']}">
                <button class="timer-btn timer-toggle-btn" onclick="toggleCardTimer('{q['qid']}')" title="Start exam practice countdown">
                    <span class="timer-icon">⏱️</span>
                    <span class="timer-display">{duration_str}</span>
                    <span class="timer-action">Start</span>
                </button>
                <button class="timer-btn timer-reset-btn" onclick="resetCardTimer('{q['qid']}')" title="Reset timer" style="display:none;">🔄</button>
            </div>'''
    type_badge = f'<span class="badge badge-type">{q["type"]}</span>'
    yt_btn = render_youtube_btn(q["yt_query"], actual_question)
    img_box = render_image_box(q["img_path"], q["img_caption"])
    content_html = format_paragraphs(q["answer"])
    byheart_box = get_byheart_card_html(q["qid"], q["marks"])

    return f"""
    <article class="question-card {subject_class}" id="{q['qid']}" data-marks="{q['marks']}" data-title="{html.escape(actual_question.lower())}">
        <header class="card-header">
            <div class="card-badges">
                {marks_badge}
                {timer_widget}
                {type_badge}
                <span class="badge badge-qid">ID: {q['qid'].upper()}</span>
            </div>
            <h3 class="card-title">{actual_question}</h3>
            <div class="card-action-bar">
                {yt_btn}
                <button class="btn-toggle-answer" onclick="toggleAnswerCard('{q['qid']}')" title="Toggle answer visibility">
                    <span class="toggle-icon">▲</span>
                    <span class="toggle-text">Hide Answer</span>
                </button>
            </div>
        </header>
        <div class="card-body">
            {byheart_box}
            <div class="answer-section">
                <h4 class="answer-heading">Elaborated Conceptual Solution:</h4>
                {content_html}
            </div>
            {img_box}
        </div>
    </article>
    """

def render_module_section(mod, subject_class):
    q_cards = '\n'.join([render_question_card(q, subject_class) for q in mod["questions"]])
    return f"""
    <section class="module-section" id="{mod['module_id']}">
        <div class="module-header">
            <span class="module-tag">{mod['module_num']}</span>
            <h2 class="module-title">{mod['module_title']}</h2>
            <p class="module-count">{len(mod['questions'])} Elaborated University Questions & Answers</p>
        </div>
        <div class="questions-grid">
            {q_cards}
        </div>
    </section>
    """

def render_mobile_syllabus_section():
    s = MOBILE_SYLLABUS
    modules_html = []
    for m in s["modules"]:
        modules_html.append(f"""
        <div class="syllabus-module-card">
            <div class="syl-mod-badge">{m['num']}</div>
            <div class="syl-mod-content">
                <h4 class="syl-mod-title">{m['title']}</h4>
                <p class="syl-mod-desc">{m['contents']}</p>
            </div>
        </div>
        """)
    all_mods_str = '\n'.join(modules_html)

    return f"""
    <section class="syllabus-overview-card" id="cst415-syllabus">
        <div class="syllabus-header">
            <span class="badge badge-type">Official KTU Curriculum Blueprint</span>
            <h2>{s['course_code']}: {s['course_name']}</h2>
            <div class="syllabus-meta">
                <span><strong>Scheme:</strong> {s['scheme']}</span>
                <span><strong>Credits:</strong> {s['credits']}</span>
            </div>
            <p class="syllabus-preamble">{s['preamble']}</p>
        </div>
        <h3 class="syllabus-modules-heading">Complete 5-Module Syllabus Breakdown:</h3>
        <div class="syllabus-grid">
            {all_mods_str}
        </div>
    </section>
    """

CSS_STYLES = """
/* ==========================================================================
   THEME PALETTE 1: Soft Charcoal & Warm Slate (Refined Dark Mode)
   - Background: Soft Neutral Dark Charcoal (#10141c)
   - Surface / Cards: Dark Slate Inset (#161c27 / #1d2432)
   - Primary Text: Soft Warm Ivory / Silver (#e5eaf2 / #cbd3de)
   - Reduced blue tint, low-glare borders, comfortable contrast (12.6:1)
   ========================================================================== */
:root, [data-theme="dark"] {
    --theme-name: "Soft Charcoal";
    --bg-base: #10141c;
    --bg-surface: #161c27;
    --bg-card: #1d2432;
    --bg-card-hover: #242d3e;
    --bg-accent: #2a3548;
    
    --border-subtle: #293448;
    --border-focus: #38bdf8;
    
    --text-main: #e5eaf2;
    --text-body: #cbd3de;
    --text-muted: #919db0;
    --text-faint: #64748b;
    
    --header-bg: #131822;
    --card-shadow: rgba(0, 0, 0, 0.4);
    --display-block-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.35);

    --brand-text-grad: linear-gradient(90deg, #f8fafc, #93c5fd);

    /* Subject Themes */
    --acs-color: #38bdf8;
    --acs-glow: rgba(56, 189, 248, 0.25);
    --acs-gradient: linear-gradient(135deg, #0284c7 0%, #38bdf8 100%);
    
    --drive-color: #f59e0b;
    --drive-glow: rgba(245, 158, 11, 0.25);
    --drive-gradient: linear-gradient(135deg, #d97706 0%, #fbbf24 100%);
    
    --mobile-color: #10b981;
    --mobile-glow: rgba(16, 185, 129, 0.25);
    --mobile-gradient: linear-gradient(135deg, #059669 0%, #34d399 100%);
    
    --hero-acs-grad: radial-gradient(circle at top right, rgba(56, 189, 248, 0.15), transparent 70%);
    --hero-drive-grad: radial-gradient(circle at top right, rgba(245, 158, 11, 0.15), transparent 70%);
    --hero-mobile-grad: radial-gradient(circle at top right, rgba(16, 185, 129, 0.15), transparent 70%);

    --badge-3m-bg: rgba(56, 189, 248, 0.15);
    --badge-3m-color: #38bdf8;
    --badge-7m-bg: rgba(245, 158, 11, 0.15);
    --badge-7m-color: #fbbf24;
    --badge-type-bg: rgba(16, 185, 129, 0.15);
    --badge-type-color: #34d399;

    --placeholder-bg: rgba(0, 0, 0, 0.25);
    --placeholder-border: rgba(255, 255, 255, 0.15);

    --top-btn-grad: linear-gradient(135deg, #38bdf8, #6366f1);
}

/* ==========================================================================
   THEME PALETTE 2: Warm Espresso / Sepia Dark (Kindle-Style Comfort)
   - Background: Deep Warm Roasted Earth Charcoal (#151311)
   - Surface / Cards: Warm Amber-Black (#1d1a17 / #24201c)
   - Primary Text: Antique Warm Cream & Oatmeal (#ede5da / #d6cdbf)
   - Zero blue-light emission, maximum optical relaxation in the dark
   ========================================================================== */
[data-theme="warm"] {
    --theme-name: "Warm Espresso";
    --bg-base: #151311;
    --bg-surface: #1d1a17;
    --bg-card: #24201c;
    --bg-card-hover: #2c2723;
    --bg-accent: #332d28;
    
    --border-subtle: #3a332a;
    --border-focus: #f59e0b;
    
    --text-main: #ede5da;
    --text-body: #d6cdbf;
    --text-muted: #a39888;
    --text-faint: #706758;
    
    --header-bg: #1a1714;
    --card-shadow: rgba(0, 0, 0, 0.45);
    --display-block-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.4);

    --brand-text-grad: linear-gradient(90deg, #fef3c7, #f59e0b);

    /* Subject Themes - Warm Harmonized */
    --acs-color: #38bdf8;
    --acs-glow: rgba(56, 189, 248, 0.2);
    --acs-gradient: linear-gradient(135deg, #0284c7 0%, #38bdf8 100%);
    
    --drive-color: #f59e0b;
    --drive-glow: rgba(245, 158, 11, 0.25);
    --drive-gradient: linear-gradient(135deg, #d97706 0%, #fbbf24 100%);
    
    --mobile-color: #34d399;
    --mobile-glow: rgba(52, 211, 153, 0.2);
    --mobile-gradient: linear-gradient(135deg, #059669 0%, #34d399 100%);
    
    --hero-acs-grad: radial-gradient(circle at top right, rgba(56, 189, 248, 0.12), transparent 70%);
    --hero-drive-grad: radial-gradient(circle at top right, rgba(245, 158, 11, 0.15), transparent 70%);
    --hero-mobile-grad: radial-gradient(circle at top right, rgba(52, 211, 153, 0.12), transparent 70%);

    --badge-3m-bg: rgba(56, 189, 248, 0.15);
    --badge-3m-color: #7dd3fc;
    --badge-7m-bg: rgba(245, 158, 11, 0.18);
    --badge-7m-color: #fcd34d;
    --badge-type-bg: rgba(52, 211, 153, 0.15);
    --badge-type-color: #6ee7b7;

    --placeholder-bg: rgba(0, 0, 0, 0.3);
    --placeholder-border: rgba(245, 158, 11, 0.2);

    --top-btn-grad: linear-gradient(135deg, #d97706, #b45309);
}

/* ==========================================================================
   THEME PALETTE 3: Forest Night (Deep Pine & Soft Mint)
   - Background: Deep Evergreen Botanical Slate (#0b1311)
   - Surface / Cards: Dark Pine Inset (#121c19 / #182622)
   - Primary Text: Soft Mint Ivory & Muted Sage (#e2ece8 / #c4d6ce)
   - Green wavelengths (555nm) produce the lowest optical accommodation strain
   ========================================================================== */
[data-theme="forest"] {
    --theme-name: "Forest Night";
    --bg-base: #0b1311;
    --bg-surface: #121c19;
    --bg-card: #182622;
    --bg-card-hover: #1f312c;
    --bg-accent: #263c36;
    
    --border-subtle: #29423b;
    --border-focus: #34d399;
    
    --text-main: #e2ece8;
    --text-body: #c4d6ce;
    --text-muted: #8ea89f;
    --text-faint: #5d756d;
    
    --header-bg: #0f1815;
    --card-shadow: rgba(0, 0, 0, 0.45);
    --display-block-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.4);

    --brand-text-grad: linear-gradient(90deg, #d1fae5, #34d399);

    /* Subject Themes - Forest Harmonized */
    --acs-color: #38bdf8;
    --acs-glow: rgba(56, 189, 248, 0.2);
    --acs-gradient: linear-gradient(135deg, #0284c7 0%, #38bdf8 100%);
    
    --drive-color: #fbbf24;
    --drive-glow: rgba(251, 191, 36, 0.2);
    --drive-gradient: linear-gradient(135deg, #d97706 0%, #fbbf24 100%);
    
    --mobile-color: #10b981;
    --mobile-glow: rgba(16, 185, 129, 0.25);
    --mobile-gradient: linear-gradient(135deg, #059669 0%, #34d399 100%);
    
    --hero-acs-grad: radial-gradient(circle at top right, rgba(56, 189, 248, 0.12), transparent 70%);
    --hero-drive-grad: radial-gradient(circle at top right, rgba(251, 191, 36, 0.12), transparent 70%);
    --hero-mobile-grad: radial-gradient(circle at top right, rgba(16, 185, 129, 0.15), transparent 70%);

    --badge-3m-bg: rgba(56, 189, 248, 0.15);
    --badge-3m-color: #7dd3fc;
    --badge-7m-bg: rgba(251, 191, 36, 0.15);
    --badge-7m-color: #fde68a;
    --badge-type-bg: rgba(16, 185, 129, 0.15);
    --badge-type-color: #6ee7b7;

    --placeholder-bg: rgba(0, 0, 0, 0.3);
    --placeholder-border: rgba(52, 211, 153, 0.2);

    --top-btn-grad: linear-gradient(135deg, #10b981, #059669);
}

/* ==========================================================================
   THEME PALETTE 4: Midnight OLED (Minimalist True Black)
   - Background: Pure Deep Black (#060709)
   - Surface / Cards: Dark Graphite Inset (#0f1115 / #15181f)
   - Primary Text: Moonlight Silver (#e6e8ee / #c1c5ce)
   - Prevents high-contrast blooming while achieving zero OLED light emission
   ========================================================================== */
[data-theme="oled"] {
    --theme-name: "Midnight OLED";
    --bg-base: #060709;
    --bg-surface: #0f1115;
    --bg-card: #15181f;
    --bg-card-hover: #1c202a;
    --bg-accent: #232835;
    
    --border-subtle: #242935;
    --border-focus: #60a5fa;
    
    --text-main: #e6e8ee;
    --text-body: #c1c5ce;
    --text-muted: #818796;
    --text-faint: #555b68;
    
    --header-bg: #090b0e;
    --card-shadow: rgba(0, 0, 0, 0.7);
    --display-block-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.6);

    --brand-text-grad: linear-gradient(90deg, #f8fafc, #60a5fa);

    /* Subject Themes */
    --acs-color: #60a5fa;
    --acs-glow: rgba(96, 165, 250, 0.2);
    --acs-gradient: linear-gradient(135deg, #2563eb 0%, #60a5fa 100%);
    
    --drive-color: #f59e0b;
    --drive-glow: rgba(245, 158, 11, 0.2);
    --drive-gradient: linear-gradient(135deg, #d97706 0%, #fbbf24 100%);
    
    --mobile-color: #34d399;
    --mobile-glow: rgba(52, 211, 153, 0.2);
    --mobile-gradient: linear-gradient(135deg, #059669 0%, #34d399 100%);
    
    --hero-acs-grad: radial-gradient(circle at top right, rgba(96, 165, 250, 0.12), transparent 70%);
    --hero-drive-grad: radial-gradient(circle at top right, rgba(245, 158, 11, 0.12), transparent 70%);
    --hero-mobile-grad: radial-gradient(circle at top right, rgba(52, 211, 153, 0.12), transparent 70%);

    --badge-3m-bg: rgba(96, 165, 250, 0.15);
    --badge-3m-color: #93c5fd;
    --badge-7m-bg: rgba(245, 158, 11, 0.15);
    --badge-7m-color: #fcd34d;
    --badge-type-bg: rgba(52, 211, 153, 0.15);
    --badge-type-color: #6ee7b7;

    --placeholder-bg: #0b0c10;
    --placeholder-border: #242935;

    --top-btn-grad: linear-gradient(135deg, #3b82f6, #1d4ed8);
}

/* ==========================================================================
   THEME PALETTE 5: Warm Slate & Off-White (Day / Reading Mode)
   - Background: Soft Warm Off-White / Cream Paper (#f4f4f0)
   - Primary Text: Dark Slate Gray (#0f172a / #1e293b) — No pure black on white
   - Meets WCAG AAA 11.5:1 contrast, paper-like low-glare reading
   ========================================================================== */
[data-theme="light"] {
    --theme-name: "Day Mode";
    --bg-base: #f4f4f0;
    --bg-surface: #ffffff;
    --bg-card: #f8fafc;
    --bg-card-hover: #f1f5f9;
    --bg-accent: #e2e8f0;
    
    --border-subtle: #cbd5e1;
    --border-focus: #0284c7;
    
    --text-main: #0f172a;
    --text-body: #1e293b;
    --text-muted: #475569;
    --text-faint: #64748b;
    
    --header-bg: #ffffff;
    --card-shadow: rgba(15, 23, 42, 0.08);
    --display-block-shadow: inset 0 1px 4px rgba(15, 23, 42, 0.06);

    --brand-text-grad: linear-gradient(90deg, #0f172a, #0284c7);

    /* Subject Themes */
    --acs-color: #0284c7;
    --acs-glow: rgba(2, 132, 199, 0.2);
    --acs-gradient: linear-gradient(135deg, #0284c7 0%, #38bdf8 100%);
    
    --drive-color: #d97706;
    --drive-glow: rgba(217, 119, 6, 0.2);
    --drive-gradient: linear-gradient(135deg, #b45309 0%, #f59e0b 100%);
    
    --mobile-color: #0d9488;
    --mobile-glow: rgba(13, 148, 136, 0.2);
    --mobile-gradient: linear-gradient(135deg, #0f766e 0%, #14b8a6 100%);
    
    --hero-acs-grad: radial-gradient(circle at top right, rgba(2, 132, 199, 0.12), transparent 70%);
    --hero-drive-grad: radial-gradient(circle at top right, rgba(217, 119, 6, 0.12), transparent 70%);
    --hero-mobile-grad: radial-gradient(circle at top right, rgba(13, 148, 136, 0.12), transparent 70%);

    --badge-3m-bg: rgba(2, 132, 199, 0.12);
    --badge-3m-color: #0369a1;
    --badge-7m-bg: rgba(217, 119, 6, 0.12);
    --badge-7m-color: #92400e;
    --badge-type-bg: rgba(13, 148, 136, 0.12);
    --badge-type-color: #0f766e;

    --placeholder-bg: #f8fafc;
    --placeholder-border: #cbd5e1;

    --top-btn-grad: linear-gradient(135deg, #0284c7, #4f46e5);
}

/* ==========================================================================
   THEME PALETTE 6: Sage & Soft Olive (Cool Focus Palette / Eye Comfort)
   - Background: Pale Sage / Muted Mint Tint (#ebf3f1)
   - Primary Text: Deep Forest / Dark Charcoal (#1c2a26 / #233530)
   - Cool, muted greens and blues promote sustained focus and lower fatigue
   ========================================================================== */
[data-theme="sage"] {
    --theme-name: "Sage Focus Mode";
    --bg-base: #ebf3f1;
    --bg-surface: #f4faf8;
    --bg-card: #e2edea;
    --bg-card-hover: #d5e4df;
    --bg-accent: #cadbd5;
    
    --border-subtle: #b6cec5;
    --border-focus: #059669;
    
    --text-main: #1c2a26;
    --text-body: #233530;
    --text-muted: #3d534c;
    --text-faint: #5c746d;
    
    --header-bg: #f4faf8;
    --card-shadow: rgba(28, 42, 38, 0.08);
    --display-block-shadow: inset 0 1px 4px rgba(28, 42, 38, 0.06);

    --brand-text-grad: linear-gradient(90deg, #1c2a26, #047857);

    /* Subject Themes */
    --acs-color: #0e7490;
    --acs-glow: rgba(14, 116, 144, 0.2);
    --acs-gradient: linear-gradient(135deg, #0e7490 0%, #06b6d4 100%);
    
    --drive-color: #b45309;
    --drive-glow: rgba(180, 83, 9, 0.2);
    --drive-gradient: linear-gradient(135deg, #92400e 0%, #d97706 100%);
    
    --mobile-color: #047857;
    --mobile-glow: rgba(4, 120, 87, 0.2);
    --mobile-gradient: linear-gradient(135deg, #065f46 0%, #10b981 100%);
    
    --hero-acs-grad: radial-gradient(circle at top right, rgba(14, 116, 144, 0.12), transparent 70%);
    --hero-drive-grad: radial-gradient(circle at top right, rgba(180, 83, 9, 0.12), transparent 70%);
    --hero-mobile-grad: radial-gradient(circle at top right, rgba(4, 120, 87, 0.12), transparent 70%);

    --badge-3m-bg: rgba(14, 116, 144, 0.12);
    --badge-3m-color: #0e7490;
    --badge-7m-bg: rgba(180, 83, 9, 0.12);
    --badge-7m-color: #78350f;
    --badge-type-bg: rgba(4, 120, 87, 0.12);
    --badge-type-color: #065f46;

    --placeholder-bg: #e2edea;
    --placeholder-border: #b6cec5;

    --top-btn-grad: linear-gradient(135deg, #047857, #4f46e5);
}

:root {
    --yt-red: #ef4444;
    --yt-gradient: linear-gradient(135deg, #dc2626 0%, #ef4444 100%);
    --font-main: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    --font-mono: 'JetBrains Mono', Consolas, Monaco, monospace;
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    background-color: var(--bg-base);
    color: var(--text-main);
    font-family: var(--font-main);
    line-height: 1.75;
    font-size: 16px;
    overflow-x: hidden;
    -webkit-font-smoothing: antialiased;
    transition: background-color 0.25s ease, color 0.25s ease;
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 10px;
    height: 10px;
}
::-webkit-scrollbar-track {
    background: var(--bg-base);
}
::-webkit-scrollbar-thumb {
    background: var(--bg-accent);
    border-radius: 5px;
    border: 2px solid var(--bg-base);
}
::-webkit-scrollbar-thumb:hover {
    background: var(--text-faint);
}

/* Header & Navigation Bar - Stuck at Top of Page, Does NOT Follow Scroll */
header.site-header {
    position: relative; /* Positioned at top of document; does NOT follow scroll */
    z-index: 10;
    background: var(--header-bg);
    border-bottom: 1px solid var(--border-subtle);
    padding: 0.65rem 1.75rem;
    display: flex;
    flex-direction: column;
    gap: 0.55rem;
    box-shadow: 0 4px 20px var(--card-shadow);
    transition: background-color 0.25s ease, border-color 0.25s ease;
}

.header-top-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 0.75rem;
}

.brand-container {
    display: flex;
    align-items: center;
    gap: 0.65rem;
}

.brand-logo-icon {
    width: 36px;
    height: 36px;
    background: linear-gradient(135deg, #6366f1, #38bdf8);
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.15rem;
    box-shadow: 0 3px 12px rgba(99, 102, 241, 0.35);
}

.brand-text h1 {
    font-size: 1.15rem;
    font-weight: 700;
    letter-spacing: -0.02em;
    background: var(--brand-text-grad);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.brand-text p {
    font-size: 0.72rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

/* Subject Tab Switcher (3 Pages in One) */
.subject-tabs {
    display: flex;
    background: var(--bg-base);
    padding: 0.25rem;
    border-radius: 10px;
    border: 1px solid var(--border-subtle);
    gap: 0.25rem;
}

.tab-btn {
    background: transparent;
    border: none;
    color: var(--text-muted);
    font-family: var(--font-main);
    font-size: 0.85rem;
    font-weight: 600;
    padding: 0.45rem 1rem;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.2s ease;
    display: flex;
    align-items: center;
    gap: 0.4rem;
    white-space: nowrap;
}

.tab-btn:hover {
    color: var(--text-main);
    background: var(--bg-card-hover);
}

.tab-btn.active.tab-acs {
    background: var(--acs-gradient);
    color: #ffffff;
    font-weight: 700;
    box-shadow: 0 4px 18px var(--acs-glow);
}

.tab-btn.active.tab-drive {
    background: var(--drive-gradient);
    color: #ffffff;
    font-weight: 700;
    box-shadow: 0 4px 18px var(--drive-glow);
}

.tab-btn.active.tab-mobile {
    background: var(--mobile-gradient);
    color: #ffffff;
    font-weight: 700;
    box-shadow: 0 4px 18px var(--mobile-glow);
}

/* Theme Switcher Controls */
/* Theme Switcher Controls */
.theme-switcher-wrapper {
    display: flex;
    align-items: center;
    background: var(--bg-surface);
    border: 1px solid var(--border-subtle);
    border-radius: 9px;
    padding: 0.18rem;
    gap: 0.15rem;
    box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1);
}

.theme-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.28rem;
    background: transparent;
    border: 1px solid transparent;
    color: var(--text-muted);
    font-family: var(--font-main);
    font-size: 0.76rem;
    font-weight: 600;
    padding: 0.28rem 0.52rem;
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.2s ease;
    white-space: nowrap;
}

.theme-btn:hover {
    color: var(--text-main);
    background: var(--bg-card-hover);
}

.theme-btn.active {
    background: var(--bg-card);
    color: var(--text-main);
    border-color: var(--border-focus);
    box-shadow: 0 1px 5px var(--card-shadow);
}

.theme-btn .theme-icon {
    font-size: 0.88rem;
    line-height: 1;
}

@media (max-width: 960px) {
    .theme-btn .theme-name {
        display: none;
    }
    .theme-btn {
        padding: 0.32rem 0.45rem;
    }
}

.theme-btn .theme-icon {
    font-size: 0.95rem;
    line-height: 1;
}

/* Controls: Search and Dynamic Filtering */
.controls-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 0.5rem;
}

.search-box-wrapper {
    position: relative;
    flex: 1;
    min-width: 240px;
    max-width: 420px;
}

.search-input {
    width: 100%;
    background: var(--bg-base);
    border: 1px solid var(--border-subtle);
    color: var(--text-main);
    padding: 0.45rem 0.85rem 0.45rem 2.2rem;
    border-radius: 8px;
    font-family: var(--font-main);
    font-size: 0.85rem;
    outline: none;
    transition: border-color 0.2s, box-shadow 0.2s;
}

.search-input:focus {
    border-color: var(--border-focus);
    box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.15);
}

.search-icon {
    position: absolute;
    left: 0.75rem;
    top: 50%;
    transform: translateY(-50%);
    font-size: 0.85rem;
    color: var(--text-faint);
    pointer-events: none;
}

.filter-buttons {
    display: flex;
    align-items: center;
    gap: 0.4rem;
    overflow-x: auto;
    padding-bottom: 2px;
}

.filter-btn {
    background: var(--bg-card);
    border: 1px solid var(--border-subtle);
    color: var(--text-muted);
    padding: 0.35rem 0.75rem;
    border-radius: 7px;
    font-size: 0.8rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s ease;
    white-space: nowrap;
}

.filter-btn:hover, .filter-btn.active {
    color: var(--text-main);
    background: var(--bg-accent);
    border-color: var(--border-focus);
}

.standalone-back-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    background: var(--bg-card);
    border: 1px solid var(--border-subtle);
    color: var(--text-main);
    padding: 0.35rem 0.75rem;
    border-radius: 7px;
    font-size: 0.8rem;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.2s ease;
    white-space: nowrap;
}
.standalone-back-btn:hover {
    background: var(--bg-accent);
    border-color: var(--border-focus);
}

.stats-badge {
    background: var(--bg-accent);
    border: 1px solid var(--border-subtle);
    color: var(--text-muted);
    padding: 0.35rem 0.75rem;
    border-radius: 7px;
    font-size: 0.75rem;
    font-weight: 600;
}

/* Main Container */
main.content-container {
    max-width: 1350px;
    margin: 0 auto;
    padding: 2.5rem 1.5rem;
}

/* Subject Views */
.subject-view {
    display: none;
    animation: fadeIn 0.3s ease;
}

.subject-view.active {
    display: block;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(6px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Hero Banner */
.subject-hero {
    padding: 2.5rem;
    border-radius: 20px;
    margin-bottom: 2.5rem;
    position: relative;
    overflow: hidden;
    box-shadow: 0 15px 35px var(--card-shadow);
}

.hero-acs {
    background: var(--hero-acs-grad), var(--bg-surface);
    border: 1px solid var(--border-subtle);
}

.hero-drive {
    background: var(--hero-drive-grad), var(--bg-surface);
    border: 1px solid var(--border-subtle);
}

.hero-mobile {
    background: var(--hero-mobile-grad), var(--bg-surface);
    border: 1px solid var(--border-subtle);
}

.hero-badge {
    display: inline-block;
    font-size: 0.8rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    padding: 0.3rem 0.85rem;
    border-radius: 6px;
    margin-bottom: 0.8rem;
}

.hero-acs .hero-badge { background: var(--badge-3m-bg); color: var(--acs-color); }
.hero-drive .hero-badge { background: var(--badge-7m-bg); color: var(--drive-color); }
.hero-mobile .hero-badge { background: var(--badge-type-bg); color: var(--mobile-color); }

.subject-hero h2 {
    font-size: 2.2rem;
    font-weight: 800;
    letter-spacing: -0.02em;
    margin-bottom: 0.6rem;
    color: var(--text-main);
}

.subject-hero p {
    color: var(--text-muted);
    font-size: 1.05rem;
    max-width: 900px;
    line-height: 1.7;
}

/* 3-Hour Exam Writing Strategy Banner */
.exam-strategy-banner {
    display: flex;
    align-items: flex-start;
    gap: 1.15rem;
    background: linear-gradient(135deg, rgba(56, 189, 248, 0.08) 0%, rgba(16, 185, 129, 0.08) 100%);
    border: 1px solid rgba(56, 189, 248, 0.3);
    border-left: 5px solid #38bdf8;
    border-radius: 12px;
    padding: 1.1rem 1.4rem;
    margin-bottom: 2.25rem;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
}

[data-theme="light"] .exam-strategy-banner {
    background: linear-gradient(135deg, #f0f9ff 0%, #f0fdf4 100%);
    border-color: #bae6fd;
    border-left-color: #0284c7;
}

[data-theme="warm"] .exam-strategy-banner {
    background: linear-gradient(135deg, rgba(245, 158, 11, 0.1) 0%, rgba(180, 83, 9, 0.05) 100%);
    border-color: rgba(245, 158, 11, 0.35);
    border-left-color: #f59e0b;
}

[data-theme="forest"] .exam-strategy-banner {
    background: linear-gradient(135deg, rgba(52, 211, 153, 0.1) 0%, rgba(16, 185, 129, 0.05) 100%);
    border-color: rgba(52, 211, 153, 0.35);
    border-left-color: #10b981;
}

[data-theme="sage"] .exam-strategy-banner {
    background: linear-gradient(135deg, #f0fdfa 0%, #f4f8f6 100%);
    border-color: #99f6e4;
    border-left-color: #0d9488;
}

[data-theme="oled"] .exam-strategy-banner {
    background: #080808;
    border-color: #1e293b;
    border-left-color: #38bdf8;
}

.strategy-icon {
    font-size: 1.85rem;
    line-height: 1;
    flex-shrink: 0;
    margin-top: 0.1rem;
}

.strategy-content h4 {
    font-size: 1.05rem;
    font-weight: 700;
    color: var(--text-main);
    margin: 0 0 0.4rem 0;
    letter-spacing: -0.01em;
}

.strategy-content p {
    font-size: 0.94rem;
    line-height: 1.65;
    color: var(--text-body);
    margin: 0;
}

.strategy-content strong {
    color: var(--text-main);
}

@media (max-width: 640px) {
    .exam-strategy-banner {
        padding: 0.85rem 1rem;
        gap: 0.75rem;
        margin-bottom: 1.25rem;
    }
    .strategy-icon {
        font-size: 1.4rem;
    }
    .strategy-content h4 {
        font-size: 0.94rem;
    }
    .strategy-content p {
        font-size: 0.86rem;
        line-height: 1.55;
    }
}

/* Module Sections */
.module-section {
    margin-bottom: 3.5rem;
}

.module-header {
    margin-bottom: 1.8rem;
    border-bottom: 1px solid var(--border-subtle);
    padding-bottom: 0.85rem;
    display: flex;
    align-items: baseline;
    gap: 1rem;
    flex-wrap: wrap;
}

.module-tag {
    font-family: var(--font-mono);
    font-size: 0.85rem;
    font-weight: 700;
    background: var(--bg-accent);
    color: var(--text-main);
    padding: 0.25rem 0.75rem;
    border-radius: 6px;
}

.module-title {
    font-size: 1.55rem;
    font-weight: 700;
    letter-spacing: -0.01em;
    color: var(--text-main);
}

.module-count {
    color: var(--text-faint);
    font-size: 0.9rem;
    margin-left: auto;
}

/* Questions Grid */
.questions-grid {
    display: flex;
    flex-direction: column;
    gap: 2.2rem;
}

/* Question Card */
.question-card {
    background: var(--bg-surface);
    border: 1px solid var(--border-subtle);
    border-radius: 18px;
    padding: 2.2rem;
    box-shadow: 0 4px 16px var(--card-shadow);
    transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease, background-color 0.25s ease;
    position: relative;
}

.question-card:hover {
    border-color: var(--border-focus);
    box-shadow: 0 10px 30px var(--card-shadow);
}

.question-card.subject-acs {
    border-left: 5px solid var(--acs-color);
}

.question-card.subject-drive {
    border-left: 5px solid var(--drive-color);
}

.question-card.subject-mobile {
    border-left: 5px solid var(--mobile-color);
}

.card-header {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    margin-bottom: 1.5rem;
    border-bottom: 1px solid var(--border-subtle);
    padding-bottom: 1.2rem;
}

.card-badges {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    flex-wrap: wrap;
}

.badge {
    font-size: 0.75rem;
    font-weight: 700;
    padding: 0.25rem 0.65rem;
    border-radius: 6px;
    text-transform: uppercase;
    letter-spacing: 0.04em;
}

.badge-3m {
    background: var(--badge-3m-bg);
    color: var(--badge-3m-color);
    border: 1px solid var(--badge-3m-color);
}

.badge-7m {
    background: var(--badge-7m-bg);
    color: var(--badge-7m-color);
    border: 1px solid var(--badge-7m-color);
}

.badge-type {
    background: var(--badge-type-bg);
    color: var(--badge-type-color);
}

.badge-qid {
    background: var(--bg-base);
    color: var(--text-faint);
    font-family: var(--font-mono);
    font-size: 0.75rem;
    border: 1px solid var(--border-subtle);
}

.badge-time {
    background: rgba(16, 185, 129, 0.15);
    color: #10b981;
    border: 1px solid rgba(16, 185, 129, 0.4);
    font-weight: 700;
    display: inline-flex;
    align-items: center;
    gap: 0.25rem;
}

[data-theme="light"] .badge-time {
    background: #ecfdf5;
    color: #047857;
    border-color: #6ee7b7;
}

[data-theme="sage"] .badge-time {
    background: #e6f4f1;
    color: #0f766e;
    border-color: #99f6e4;
}

[data-theme="oled"] .badge-time {
    background: #002b1c;
    color: #34d399;
    border-color: #059669;
}

.card-title {
    font-size: 1.35rem;
    font-weight: 700;
    color: var(--text-main);
    line-height: 1.45;
}

.card-action-bar {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    gap: 0.75rem;
    margin-top: 0.25rem;
    flex-wrap: wrap;
}

/* Hide/Show Answer Toggle Button */
.btn-toggle-answer {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.52rem 0.95rem;
    font-size: 0.82rem;
    font-weight: 700;
    font-family: var(--font-main);
    color: var(--text-main);
    background: var(--bg-surface);
    border: 1px solid var(--border-subtle);
    border-radius: 9px;
    cursor: pointer;
    transition: all 0.2s ease;
    box-shadow: 0 2px 6px var(--card-shadow);
}

.btn-toggle-answer:hover {
    color: var(--text-main);
    background: var(--bg-card-hover);
    border-color: var(--border-focus);
    transform: translateY(-1px);
}

.question-card.answer-collapsed {
    padding-bottom: 0.85rem;
}

.question-card.answer-collapsed .card-header {
    border-bottom: none;
    margin-bottom: 0;
    padding-bottom: 0;
}

.question-card.answer-collapsed .card-body {
    display: none !important;
}

/* Card Interactive Timer Widget */
.card-timer-widget {
    display: inline-flex;
    align-items: center;
    gap: 0.25rem;
    background: var(--bg-surface);
    border: 1px solid rgba(16, 185, 129, 0.4);
    border-radius: 6px;
    padding: 0.15rem 0.35rem;
    transition: all 0.25s ease;
}

.timer-btn {
    border: none;
    background: transparent;
    cursor: pointer;
    font-family: var(--font-mono);
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    color: #10b981;
    font-size: 0.76rem;
    font-weight: 700;
    padding: 0.2rem 0.4rem;
    border-radius: 4px;
    transition: background 0.2s ease, color 0.2s ease;
}

.timer-toggle-btn:hover {
    background: rgba(16, 185, 129, 0.15);
}

.timer-reset-btn {
    font-size: 0.75rem;
    padding: 0.2rem 0.35rem;
    color: var(--text-muted);
}
.timer-reset-btn:hover {
    color: var(--text-main);
    background: var(--bg-card-hover);
}

.timer-action {
    font-family: var(--font-main);
    font-size: 0.68rem;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    background: rgba(16, 185, 129, 0.2);
    padding: 0.1rem 0.38rem;
    border-radius: 4px;
}

/* Timer State: Running */
.card-timer-widget.timer-running {
    border-color: #10b981;
    box-shadow: 0 0 10px rgba(16, 185, 129, 0.35);
    background: rgba(16, 185, 129, 0.12);
    animation: timerPulse 2s infinite ease-in-out;
}

.card-timer-widget.timer-running .timer-action {
    background: #10b981;
    color: #064e3b;
    font-weight: 800;
}

/* Timer State: Paused */
.card-timer-widget.timer-paused {
    border-color: #f59e0b;
    background: rgba(245, 158, 11, 0.1);
}
.card-timer-widget.timer-paused .timer-btn {
    color: #f59e0b;
}
.card-timer-widget.timer-paused .timer-action {
    background: #f59e0b;
    color: #451a03;
}

/* Timer State: Warning (< 1 min) */
.card-timer-widget.timer-warning {
    border-color: #f59e0b;
    box-shadow: 0 0 12px rgba(245, 158, 11, 0.45);
    background: rgba(245, 158, 11, 0.15);
}
.card-timer-widget.timer-warning .timer-btn {
    color: #fbbf24;
}
.card-timer-widget.timer-warning .timer-action {
    background: #f59e0b;
    color: #451a03;
}

/* Timer State: Expired (Time's Up) */
.card-timer-widget.timer-expired {
    border-color: #ef4444;
    box-shadow: 0 0 14px rgba(239, 68, 68, 0.5);
    background: rgba(239, 68, 68, 0.18);
    animation: expiredFlash 1s infinite alternate;
}
.card-timer-widget.timer-expired .timer-btn {
    color: #f87171;
}
.card-timer-widget.timer-expired .timer-action {
    background: #ef4444;
    color: #ffffff;
    font-weight: 800;
}

@keyframes timerPulse {
    0%, 100% { box-shadow: 0 0 8px rgba(16, 185, 129, 0.25); }
    50% { box-shadow: 0 0 14px rgba(16, 185, 129, 0.5); }
}

@keyframes expiredFlash {
    from { opacity: 1; }
    to { opacity: 0.65; }
}

/* Global Collapse All Button */
.global-collapse-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
}
.global-collapse-btn.active-collapsed {
    border-color: var(--border-focus);
    background: var(--bg-card);
    color: var(--text-main);
}

/* YouTube Link Button */
.yt-button {
    display: inline-flex;
    align-items: center;
    gap: 0.55rem;
    background: var(--yt-gradient);
    color: #ffffff;
    font-size: 0.85rem;
    font-weight: 700;
    padding: 0.55rem 1.15rem;
    border-radius: 10px;
    text-decoration: none;
    transition: all 0.2s ease;
    box-shadow: 0 4px 14px rgba(239, 68, 68, 0.35);
}

.yt-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(239, 68, 68, 0.5);
    filter: brightness(1.1);
}

.yt-icon {
    flex-shrink: 0;
}

/* =========================================================================
   Sentence / (Equation) to Byhart Card - High Mark Weightage Exam Memo Box
   ========================================================================= */
.byheart-card {
    background: linear-gradient(135deg, rgba(245, 158, 11, 0.08) 0%, rgba(56, 189, 248, 0.04) 100%);
    border: 1px solid rgba(245, 158, 11, 0.35);
    border-left: 5px solid #f59e0b;
    border-radius: 10px;
    padding: 1.1rem 1.35rem;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
    position: relative;
    transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
}

.byheart-card:hover {
    border-color: #fbbf24;
    box-shadow: 0 6px 20px rgba(245, 158, 11, 0.22);
}

[data-theme="light"] .byheart-card {
    background: linear-gradient(135deg, #fffdf5 0%, #fef9c3 100%);
    border: 1px solid #fde047;
    border-left: 5px solid #d97706;
    box-shadow: 0 3px 12px rgba(217, 119, 6, 0.1);
}

[data-theme="warm"] .byheart-card {
    background: linear-gradient(135deg, rgba(245, 158, 11, 0.1) 0%, rgba(180, 83, 9, 0.06) 100%);
    border: 1px solid rgba(245, 158, 11, 0.38);
    border-left: 5px solid #f59e0b;
}

[data-theme="forest"] .byheart-card {
    background: linear-gradient(135deg, rgba(52, 211, 153, 0.09) 0%, rgba(245, 158, 11, 0.05) 100%);
    border: 1px solid rgba(52, 211, 153, 0.35);
    border-left: 5px solid #10b981;
}

[data-theme="oled"] .byheart-card {
    background: #080808;
    border: 1px solid #3d2f0a;
    border-left: 5px solid #f59e0b;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.8);
}

[data-theme="sage"] .byheart-card {
    background: linear-gradient(135deg, #f4f8f6 0%, #e6f0ec 100%);
    border: 1px solid #99c7b9;
    border-left: 5px solid #0d9488;
    box-shadow: 0 3px 12px rgba(13, 148, 136, 0.1);
}

.byheart-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 0.6rem;
    margin-bottom: 0.75rem;
    padding-bottom: 0.55rem;
    border-bottom: 1px dashed rgba(245, 158, 11, 0.3);
}

[data-theme="forest"] .byheart-header {
    border-bottom-color: rgba(52, 211, 153, 0.3);
}

[data-theme="sage"] .byheart-header {
    border-bottom-color: rgba(13, 148, 136, 0.3);
}

.byheart-title-group {
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.byheart-icon {
    font-size: 1.15rem;
    line-height: 1;
}

.byheart-title {
    font-size: 0.88rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.07em;
    color: #f59e0b;
}

[data-theme="light"] .byheart-title {
    color: #b45309;
}

[data-theme="forest"] .byheart-title {
    color: #34d399;
}

[data-theme="sage"] .byheart-title {
    color: #0f766e;
}

.byheart-badge {
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    background: rgba(245, 158, 11, 0.18);
    color: #fbbf24;
    padding: 0.22rem 0.65rem;
    border-radius: 9999px;
    border: 1px solid rgba(245, 158, 11, 0.35);
}

[data-theme="light"] .byheart-badge {
    background: #fef08a;
    color: #854d0e;
    border-color: #facc15;
}

[data-theme="forest"] .byheart-badge {
    background: rgba(16, 185, 129, 0.18);
    color: #6ee7b7;
    border-color: rgba(16, 185, 129, 0.35);
}

[data-theme="sage"] .byheart-badge {
    background: #ccfbf1;
    color: #115e59;
    border-color: #5eead4;
}

.byheart-badges-group {
    display: flex;
    align-items: center;
    gap: 0.45rem;
    flex-wrap: wrap;
}

.byheart-time-badge {
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    background: rgba(56, 189, 248, 0.15);
    color: #38bdf8;
    padding: 0.22rem 0.6rem;
    border-radius: 9999px;
    border: 1px solid rgba(56, 189, 248, 0.35);
    display: inline-flex;
    align-items: center;
    gap: 0.2rem;
}

[data-theme="light"] .byheart-time-badge {
    background: #e0f2fe;
    color: #0284c7;
    border-color: #7dd3fc;
}

[data-theme="forest"] .byheart-time-badge {
    background: rgba(52, 211, 153, 0.15);
    color: #34d399;
    border-color: rgba(52, 211, 153, 0.35);
}

[data-theme="sage"] .byheart-time-badge {
    background: #ccfbf1;
    color: #0f766e;
    border-color: #5eead4;
}

[data-theme="oled"] .byheart-time-badge {
    background: #001f33;
    color: #38bdf8;
    border-color: #0284c7;
}

.byheart-body {
    display: flex;
    flex-direction: column;
    gap: 0.65rem;
}

.byheart-eq {
    background: rgba(0, 0, 0, 0.3);
    padding: 0.6rem 0.9rem;
    border-radius: 8px;
    border: 1px solid rgba(255, 255, 255, 0.07);
    overflow-x: auto;
    font-size: 1.02rem;
    text-align: center;
}

[data-theme="light"] .byheart-eq {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.04);
}

[data-theme="sage"] .byheart-eq {
    background: #ffffff;
    border: 1px solid #cbd5e1;
}

[data-theme="oled"] .byheart-eq {
    background: #000000;
    border-color: #222222;
}

.byheart-text {
    font-size: 0.98rem;
    line-height: 1.75;
    color: var(--text-main);
    margin: 0;
}

.byheart-text strong {
    color: #fbbf24;
    font-weight: 700;
}

[data-theme="light"] .byheart-text strong {
    color: #b45309;
}

[data-theme="forest"] .byheart-text strong {
    color: #34d399;
}

[data-theme="sage"] .byheart-text strong {
    color: #0f766e;
}

/* Card Body & Paragraph Styling */
.card-body {
    display: flex;
    flex-direction: column;
    gap: 1.8rem;
}

.answer-section {
    display: flex;
    flex-direction: column;
    gap: 1.15rem;
}

.answer-heading {
    font-size: 0.95rem;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: var(--text-muted);
    font-weight: 700;
    margin-bottom: 0.25rem;
}

.answer-para {
    font-size: 1.02rem;
    line-height: 1.85;
    color: var(--text-body);
    text-align: justify;
}

/* KaTeX Math Blocks */
.katex-display-block {
    margin: 1.25rem 0;
    padding: 1.2rem 1.5rem;
    background: var(--bg-card);
    border: 1px solid var(--border-subtle);
    border-radius: 12px;
    overflow-x: auto;
    text-align: center;
    box-shadow: var(--display-block-shadow);
    color: var(--text-main);
}

.katex-display {
    margin: 0 !important;
}

/* Image Placeholder Box */
.image-placeholder-container {
    margin-top: 1.2rem;
    background: var(--bg-card);
    border: 1px solid var(--border-subtle);
    border-radius: 14px;
    padding: 1.5rem;
    display: flex;
    flex-direction: column;
    gap: 0.85rem;
}

.image-placeholder-container.missing-image .diagram-img {
    display: none;
}

.image-placeholder-container.has-real-image .placeholder-fallback {
    display: none;
}

.image-placeholder-container.has-real-image .diagram-img {
    display: block;
    max-width: 100%;
    height: auto;
    border-radius: 10px;
    border: 1px solid var(--border-subtle);
    margin: 0 auto;
    background: #ffffff;
    box-shadow: 0 4px 20px var(--card-shadow);
}

.placeholder-fallback {
    border: 2px dashed var(--placeholder-border);
    border-radius: 12px;
    padding: 2.2rem 1.5rem;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.65rem;
    background: var(--placeholder-bg);
}

.ph-icon {
    font-size: 2.2rem;
    opacity: 0.8;
}

.ph-title {
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--text-main);
}

.ph-desc {
    color: var(--text-muted);
    font-size: 0.95rem;
    max-width: 600px;
}

.ph-path-badge code {
    background: var(--bg-base);
    color: var(--text-main);
    padding: 0.35rem 0.85rem;
    border-radius: 6px;
    font-family: var(--font-mono);
    font-size: 0.82rem;
    border: 1px solid var(--border-subtle);
}

.ph-note {
    font-size: 0.8rem;
    color: var(--text-faint);
    font-style: italic;
}

.diagram-caption {
    font-size: 0.9rem;
    color: var(--text-muted);
    border-top: 1px solid var(--border-subtle);
    padding-top: 0.75rem;
}

.file-path-tag {
    font-family: var(--font-mono);
    font-size: 0.78rem;
    color: var(--text-faint);
    margin-left: 0.5rem;
}

/* Syllabus Blueprint Section */
.syllabus-overview-card {
    background: var(--bg-surface);
    border: 1px solid var(--border-subtle);
    border-radius: 20px;
    padding: 2.5rem;
    margin-bottom: 3rem;
    box-shadow: 0 10px 30px var(--card-shadow);
}

.syllabus-header h2 {
    font-size: 1.85rem;
    font-weight: 800;
    margin: 0.75rem 0 0.5rem 0;
    color: var(--text-main);
}

.syllabus-meta {
    display: flex;
    gap: 1.5rem;
    font-size: 0.9rem;
    color: var(--text-muted);
    margin-bottom: 1rem;
}

.syllabus-preamble {
    color: var(--text-muted);
    line-height: 1.7;
    margin-bottom: 1.8rem;
    font-size: 0.98rem;
    border-left: 3px solid var(--mobile-color);
    padding-left: 1rem;
}

.syllabus-modules-heading {
    font-size: 1.2rem;
    font-weight: 700;
    color: var(--text-main);
    margin-bottom: 1.2rem;
}

.syllabus-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.25rem;
}

.syllabus-module-card {
    background: var(--bg-card);
    border: 1px solid var(--border-subtle);
    border-radius: 12px;
    padding: 1.25rem;
    display: flex;
    flex-direction: column;
    gap: 0.65rem;
}

.syl-mod-badge {
    align-self: flex-start;
    font-family: var(--font-mono);
    font-size: 0.75rem;
    font-weight: 700;
    background: var(--bg-accent);
    color: var(--mobile-color);
    padding: 0.2rem 0.6rem;
    border-radius: 5px;
    border: 1px solid var(--border-subtle);
}

.syl-mod-title {
    font-size: 1.05rem;
    font-weight: 700;
    color: var(--text-main);
}

.syl-mod-desc {
    font-size: 0.88rem;
    color: var(--text-muted);
    line-height: 1.6;
}

/* Floating Back to Top Button */
.back-to-top-btn {
    position: fixed;
    bottom: 2rem;
    right: 2rem;
    z-index: 999;
    background: var(--top-btn-grad);
    color: #ffffff;
    border: none;
    border-radius: 30px;
    padding: 0.55rem 1.1rem;
    font-family: var(--font-main);
    font-size: 0.85rem;
    font-weight: 700;
    cursor: pointer;
    box-shadow: 0 6px 20px rgba(56, 189, 248, 0.35);
    display: flex;
    align-items: center;
    gap: 0.4rem;
    opacity: 0;
    visibility: hidden;
    transform: translateY(12px);
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.back-to-top-btn.visible {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
}

.back-to-top-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 28px rgba(56, 189, 248, 0.55);
}

/* Footer */
footer.site-footer {
    border-top: 1px solid var(--border-subtle);
    background: var(--bg-surface);
    padding: 3rem 1.5rem;
    text-align: center;
    color: var(--text-faint);
    font-size: 0.9rem;
    margin-top: 4rem;
}

.footer-content {
    max-width: 900px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.footer-links {
    display: flex;
    justify-content: center;
    gap: 1.5rem;
    flex-wrap: wrap;
}

.footer-links a {
    color: var(--text-muted);
    text-decoration: none;
    font-weight: 600;
    transition: color 0.2s;
}

.footer-links a:hover {
    color: var(--border-focus);
}

/* ==========================================================================
   ADVANCED MOBILE-FRIENDLY & SPACE-EFFICIENT RESPONSIVE SUITE
   - Fluid typography & touch targets
   - Zero horizontal overflow
   - Safe-area insets for notches / dynamic islands
   - Highly compact, space-saving headers and cards for phones
   ========================================================================== */

/* Responsive label toggling */
.tab-text-short {
    display: none;
}

/* Touch action optimization on all interactive elements */
button, input, a, .tab-btn, .theme-btn, .filter-btn {
    touch-action: manipulation;
}

/* Base Body Font Scaling & Text Adjustments */
body {
    -webkit-text-size-adjust: 100%;
    text-rendering: optimizeLegibility;
}

/* Fluid display resolution handling for tablets (<= 1024px) */
@media (max-width: 1024px) {
    main.content-container {
        padding: 1.8rem 1.2rem;
    }
    .question-card {
        padding: 1.8rem 1.4rem;
        border-radius: 16px;
    }
    .card-title {
        font-size: 1.22rem;
    }
}

/* Responsive adjustment for tablets & large phones (<= 860px) */
@media (max-width: 860px) {
    header.site-header {
        padding: 0.5rem 1rem;
        gap: 0.45rem;
    }

    .header-top-row {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 0.4rem;
    }

    .brand-container {
        gap: 0.5rem;
    }
    .brand-logo-icon {
        width: 32px;
        height: 32px;
        font-size: 1rem;
        border-radius: 8px;
    }
    .brand-text h1 {
        font-size: 1.02rem;
    }
    .brand-subtext {
        font-size: 0.65rem;
    }

    /* Tabs become compact and switch to shortened label */
    .tab-text-full {
        display: none;
    }
    .tab-text-short {
        display: inline;
    }
    .subject-tabs {
        order: 3;
        width: 100%;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
        scrollbar-width: none;
        padding: 0.2rem;
        border-radius: 8px;
    }
    .subject-tabs::-webkit-scrollbar {
        display: none;
    }
    .tab-btn {
        padding: 0.38rem 0.75rem;
        font-size: 0.78rem;
        border-radius: 6px;
        flex-shrink: 0;
    }

    /* Theme switcher sits neatly in top row beside brand */
    .theme-switcher-wrapper {
        order: 2;
        margin-left: auto;
        padding: 0.15rem;
        gap: 0.12rem;
        border-radius: 8px;
    }
    .theme-btn {
        padding: 0.28rem 0.48rem;
    }
    .theme-btn .theme-name {
        display: none;
    }
    .theme-btn .theme-icon {
        font-size: 0.88rem;
    }

    /* Controls Row */
    .controls-row {
        gap: 0.4rem;
    }
    .search-box-wrapper {
        min-width: 100%;
        max-width: 100%;
        width: 100%;
    }
    .search-input {
        padding: 0.38rem 0.75rem 0.38rem 2rem;
        font-size: 0.82rem;
    }
    .filter-buttons {
        width: 100%;
        display: flex;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
        scrollbar-width: none;
        padding-bottom: 2px;
    }
    .filter-buttons::-webkit-scrollbar {
        display: none;
    }
    .filter-btn {
        padding: 0.28rem 0.65rem;
        font-size: 0.75rem;
        flex-shrink: 0;
    }
    .stats-badge {
        font-size: 0.7rem;
        padding: 0.28rem 0.55rem;
        flex-shrink: 0;
        margin-left: auto;
    }

    .subject-hero {
        padding: 1.5rem 1.2rem;
        border-radius: 14px;
        margin-bottom: 1.5rem;
    }
    .subject-hero h2 {
        font-size: 1.45rem;
    }
}

/* Smartphone Portrait Viewport (<= 640px) */
@media (max-width: 640px) {
    /* Maximum Space Efficiency: Slim Header */
    header.site-header {
        padding: 0.45rem 0.65rem;
        gap: 0.35rem;
    }

    /* Container: minimal side gutters to maximize reading width */
    main.content-container {
        padding: 0.85rem 0.55rem;
    }

    /* Question Cards: compact padding, high space utilization */
    .questions-grid {
        gap: 1.15rem;
    }
    .question-card {
        padding: 1.15rem 0.85rem;
        border-radius: 12px;
        border-left-width: 4px;
        box-shadow: 0 2px 10px var(--card-shadow);
    }
    .card-header {
        gap: 0.5rem;
        margin-bottom: 1rem;
        padding-bottom: 0.75rem;
    }

    /* Badges */
    .card-badges {
        gap: 0.3rem;
    }
    .badge {
        font-size: 0.68rem;
        padding: 0.18rem 0.48rem;
        border-radius: 4px;
    }

    /* Title: Clamped readable scale */
    .card-title {
        font-size: 1.12rem;
        line-height: 1.4;
        letter-spacing: -0.01em;
    }

    /* Answer Typography: Left-aligned for mobile, no rivers of white space */
    .card-body {
        gap: 1.25rem;
    }
    .answer-section {
        gap: 0.85rem;
    }
    .answer-heading {
        font-size: 0.88rem;
        letter-spacing: 0.04em;
    }
    .answer-para {
        font-size: 0.94rem;
        line-height: 1.7;
        text-align: left;
        hyphens: auto;
        word-break: break-word;
    }

    /* Byheart Memo Card Mobile Optimization */
    .byheart-card {
        padding: 0.85rem 0.95rem;
        border-radius: 8px;
        border-left-width: 4px;
    }
    .byheart-header {
        gap: 0.4rem;
        margin-bottom: 0.6rem;
        padding-bottom: 0.45rem;
    }
    .byheart-title {
        font-size: 0.8rem;
    }
    .byheart-badge {
        font-size: 0.65rem;
        padding: 0.15rem 0.48rem;
    }
    .byheart-text {
        font-size: 0.92rem;
        line-height: 1.65;
        text-align: left;
    }
    .byheart-eq {
        padding: 0.45rem 0.55rem;
        font-size: 0.9rem;
        -webkit-overflow-scrolling: touch;
    }

    /* KaTeX Equations: smooth horizontal swipe without document overflow */
    .katex-display-block {
        margin: 0.85rem 0;
        padding: 0.75rem 0.6rem;
        border-radius: 8px;
        font-size: 0.86rem;
        -webkit-overflow-scrolling: touch;
        scrollbar-width: thin;
    }

    /* Images: full responsive scaling */
    .image-placeholder-container {
        margin-top: 0.85rem;
        padding: 0.6rem;
        border-radius: 10px;
        gap: 0.5rem;
    }
    .image-placeholder-container.has-real-image .diagram-img {
        border-radius: 7px;
        max-width: 100%;
        height: auto;
        object-fit: contain;
    }
    .image-caption {
        font-size: 0.76rem;
        line-height: 1.35;
        padding: 0 0.2rem;
    }

    /* YouTube Button: Full width touch target */
    .card-action-bar {
        width: 100%;
    }
    .yt-button {
        width: 100%;
        justify-content: center;
        padding: 0.55rem 0.85rem;
        font-size: 0.82rem;
        border-radius: 8px;
    }

    /* Module Headers */
    .module-header {
        margin-bottom: 0.9rem;
        padding-bottom: 0.5rem;
        gap: 0.4rem;
    }
    .module-tag {
        font-size: 0.72rem;
        padding: 0.18rem 0.5rem;
    }
    .module-title {
        font-size: 1.18rem;
    }
    .module-count {
        font-size: 0.75rem;
    }

    /* Subject Hero: Ultra compact */
    .subject-hero {
        padding: 1.15rem 0.9rem;
        border-radius: 12px;
        margin-bottom: 1.15rem;
    }
    .subject-hero h2 {
        font-size: 1.25rem;
        margin: 0.35rem 0 0.45rem 0;
    }
    .subject-hero p {
        font-size: 0.82rem;
        line-height: 1.5;
    }
    .hero-badge {
        font-size: 0.68rem;
        padding: 0.18rem 0.5rem;
    }

    /* Mobile Floating Top Button */
    .back-to-top-btn {
        bottom: calc(0.85rem + env(safe-area-inset-bottom));
        right: 0.85rem;
        padding: 0.42rem 0.7rem;
        font-size: 0.74rem;
        border-radius: 20px;
    }
}

/* Compact Phones (<= 400px - e.g. iPhone SE, Galaxy A series) */
@media (max-width: 400px) {
    header.site-header {
        padding: 0.4rem 0.5rem;
    }
    main.content-container {
        padding: 0.7rem 0.4rem;
    }
    .question-card {
        padding: 0.95rem 0.7rem;
        border-radius: 10px;
    }
    .card-title {
        font-size: 1.04rem;
    }
    .answer-para {
        font-size: 0.91rem;
        line-height: 1.65;
    }
    .katex-display-block {
        font-size: 0.82rem;
        padding: 0.6rem 0.4rem;
    }
    .brand-text h1 {
        font-size: 0.94rem;
    }
    .brand-subtext {
        display: none;
    }
    .theme-btn {
        padding: 0.25rem 0.38rem;
    }
}
"""

JS_SCRIPT = """
// Tab Switching for 3 Web Pages in One Index Page
const tabBtns = document.querySelectorAll('.tab-btn');
const subjectViews = document.querySelectorAll('.subject-view');

function switchTab(targetId) {
    tabBtns.forEach(btn => {
        if (btn.getAttribute('data-target') === targetId) {
            btn.classList.add('active');
            btn.setAttribute('aria-selected', 'true');
        } else {
            btn.classList.remove('active');
            btn.setAttribute('aria-selected', 'false');
        }
    });

    subjectViews.forEach(view => {
        if (view.id === targetId) {
            view.classList.add('active');
        } else {
            view.classList.remove('active');
        }
    });

    if (window.renderMathInElement) {
        renderMathInElement(document.getElementById(targetId), {
            delimiters: [
                {left: '$$', right: '$$', display: true},
                {left: '$', right: '$', display: false}
            ],
            throwOnError: false
        });
    }

    applyFilters();
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        const targetId = btn.getAttribute('data-target');
        switchTab(targetId);
    });
});

// Filter Questions (All, 3 Marks, 7 Marks)
const filterBtns = document.querySelectorAll('.filter-btn');
filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        applyFilters();
    });
});

// Live Search Input
const searchInput = document.getElementById('global-search');
searchInput.addEventListener('input', () => {
    applyFilters();
});

function applyFilters() {
    const query = searchInput.value.toLowerCase().trim();
    const activeFilterBtn = document.querySelector('.filter-btn.active');
    const filterType = activeFilterBtn ? activeFilterBtn.getAttribute('data-filter') : 'all';

    const activeView = document.querySelector('.subject-view.active');
    if (!activeView) return;

    const cards = activeView.querySelectorAll('.question-card');
    let visibleCount = 0;

    cards.forEach(card => {
        const marks = card.getAttribute('data-marks');
        const title = card.getAttribute('data-title') || '';
        const cardText = card.innerText.toLowerCase();

        let matchesMarks = true;
        if (filterType === '3m' && marks !== '3') matchesMarks = false;
        if (filterType === '7m' && marks === '3') matchesMarks = false;

        let matchesSearch = true;
        if (query.length > 0) {
            matchesSearch = cardText.includes(query) || title.includes(query);
        }

        if (matchesMarks && matchesSearch) {
            card.style.display = 'block';
            visibleCount++;
        } else {
            card.style.display = 'none';
        }
    });

    const statsPill = document.getElementById('stats-pill');
    if (statsPill) {
        statsPill.innerText = `${visibleCount} Questions Displayed`;
    }
}

// Back to Top Scroll Behavior
window.addEventListener('scroll', () => {
    const topBtn = document.getElementById('back-to-top');
    if (topBtn) {
        if (window.scrollY > 350) {
            topBtn.classList.add('visible');
        } else {
            topBtn.classList.remove('visible');
        }
    }
});

function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// ==========================================================================
// Theme Switching Logic with LocalStorage Persistence
// Ergonomic Palettes:
// 1. 'dark'   : Soft Charcoal & Warm Slate (Refined Neutral Dark)
// 2. 'warm'   : Warm Espresso (Kindle-Style Sepia Dark - Zero Blue Light)
// 3. 'forest' : Forest Night (Deep Pine & Soft Mint - Lowest Eye Strain)
// 4. 'oled'   : Midnight OLED (Minimalist True Black)
// 5. 'light'  : Warm Slate & Off-White Paper (Day Mode)
// 6. 'sage'   : Sage & Soft Olive (Cool Focus Mode)
// ==========================================================================
const THEME_STORAGE_KEY = 'ktu_portal_theme';
const VALID_THEMES = ['dark', 'warm', 'forest', 'oled', 'light', 'sage'];

function setTheme(themeName) {
    if (!VALID_THEMES.includes(themeName)) {
        themeName = 'dark';
    }
    document.documentElement.setAttribute('data-theme', themeName);
    try {
        localStorage.setItem(THEME_STORAGE_KEY, themeName);
    } catch (e) {}

    const themeButtons = document.querySelectorAll('.theme-btn');
    themeButtons.forEach(btn => {
        const val = btn.getAttribute('data-theme-value');
        if (val === themeName) {
            btn.classList.add('active');
            btn.setAttribute('aria-checked', 'true');
        } else {
            btn.classList.remove('active');
            btn.setAttribute('aria-checked', 'false');
        }
    });
}

function initThemeSwitcher() {
    const themeButtons = document.querySelectorAll('.theme-btn');
    themeButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const chosenTheme = btn.getAttribute('data-theme-value');
            setTheme(chosenTheme);
        });
    });

    const savedTheme = localStorage.getItem(THEME_STORAGE_KEY) || 'dark';
    setTheme(savedTheme);
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initThemeSwitcher);
} else {
    initThemeSwitcher();
}

// =========================================================================
// Interactive Exam Countdown Timers
// =========================================================================
const cardTimers = {};

function formatTimerMMSS(seconds) {
    const m = Math.floor(seconds / 60);
    const s = seconds % 60;
    return (m < 10 ? '0' : '') + m + ':' + (s < 10 ? '0' : '') + s;
}

function toggleCardTimer(qid) {
    const widget = document.getElementById('timer-' + qid);
    if (!widget) return;
    const duration = parseInt(widget.getAttribute('data-duration') || '300', 10);
    
    if (!cardTimers[qid]) {
        cardTimers[qid] = {
            duration: duration,
            remaining: duration,
            intervalId: null,
            state: 'idle'
        };
    }
    
    const timer = cardTimers[qid];
    const displaySpan = widget.querySelector('.timer-display');
    const actionSpan = widget.querySelector('.timer-action');
    const resetBtn = widget.querySelector('.timer-reset-btn');

    if (timer.state === 'running') {
        // Pause
        clearInterval(timer.intervalId);
        timer.intervalId = null;
        timer.state = 'paused';
        actionSpan.textContent = 'Resume';
        widget.classList.remove('timer-running');
        widget.classList.add('timer-paused');
    } else {
        // Start or Resume
        if (timer.state === 'expired') {
            timer.remaining = timer.duration;
            widget.classList.remove('timer-expired');
        }
        timer.state = 'running';
        actionSpan.textContent = 'Pause';
        if (resetBtn) resetBtn.style.display = 'inline-flex';
        widget.classList.remove('timer-paused');
        widget.classList.add('timer-running');

        timer.intervalId = setInterval(() => {
            timer.remaining--;
            displaySpan.textContent = formatTimerMMSS(timer.remaining);

            if (timer.remaining <= 60 && timer.remaining > 0) {
                widget.classList.add('timer-warning');
            }

            if (timer.remaining <= 0) {
                clearInterval(timer.intervalId);
                timer.intervalId = null;
                timer.state = 'expired';
                displaySpan.textContent = '00:00';
                actionSpan.textContent = "Time's Up!";
                widget.classList.remove('timer-running', 'timer-warning');
                widget.classList.add('timer-expired');
            }
        }, 1000);
    }
}

function resetCardTimer(qid) {
    const widget = document.getElementById('timer-' + qid);
    if (!widget || !cardTimers[qid]) return;
    const timer = cardTimers[qid];
    if (timer.intervalId) {
        clearInterval(timer.intervalId);
        timer.intervalId = null;
    }
    timer.remaining = timer.duration;
    timer.state = 'idle';

    const displaySpan = widget.querySelector('.timer-display');
    const actionSpan = widget.querySelector('.timer-action');
    const resetBtn = widget.querySelector('.timer-reset-btn');

    displaySpan.textContent = formatTimerMMSS(timer.duration);
    actionSpan.textContent = 'Start';
    if (resetBtn) resetBtn.style.display = 'none';
    widget.classList.remove('timer-running', 'timer-paused', 'timer-warning', 'timer-expired');
}

// =========================================================================
// Answer Collapse / Expand Toggle
// =========================================================================
function toggleAnswerCard(qid) {
    const card = document.getElementById(qid);
    if (!card) return;
    const isCollapsed = card.classList.toggle('answer-collapsed');
    const toggleBtn = card.querySelector('.btn-toggle-answer');
    if (toggleBtn) {
        if (isCollapsed) {
            toggleBtn.innerHTML = '<span class="toggle-icon">▼</span> <span class="toggle-text">Show Answer</span>';
            toggleBtn.setAttribute('title', 'Show elaborated answer');
        } else {
            toggleBtn.innerHTML = '<span class="toggle-icon">▲</span> <span class="toggle-text">Hide Answer</span>';
            toggleBtn.setAttribute('title', 'Hide elaborated answer');
        }
    }
}

let allAnswersCollapsed = false;
function toggleAllAnswers() {
    allAnswersCollapsed = !allAnswersCollapsed;
    const cards = document.querySelectorAll('.question-card');
    const globalBtns = document.querySelectorAll('.global-collapse-btn');
    
    cards.forEach(card => {
        const toggleBtn = card.querySelector('.btn-toggle-answer');
        if (allAnswersCollapsed) {
            card.classList.add('answer-collapsed');
            if (toggleBtn) {
                toggleBtn.innerHTML = '<span class="toggle-icon">▼</span> <span class="toggle-text">Show Answer</span>';
                toggleBtn.setAttribute('title', 'Show elaborated answer');
            }
        } else {
            card.classList.remove('answer-collapsed');
            if (toggleBtn) {
                toggleBtn.innerHTML = '<span class="toggle-icon">▲</span> <span class="toggle-text">Hide Answer</span>';
                toggleBtn.setAttribute('title', 'Hide elaborated answer');
            }
        }
    });

    globalBtns.forEach(btn => {
        if (allAnswersCollapsed) {
            btn.innerHTML = '<span class="btn-icon">📖</span> <span class="btn-text">Expand All Answers</span>';
            btn.classList.add('active-collapsed');
        } else {
            btn.innerHTML = '<span class="btn-icon">👁️</span> <span class="btn-text">Collapse All Answers</span>';
            btn.classList.remove('active-collapsed');
        }
    });
}
"""

INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>KTU Engineering Exam Portal | ACS, Electric Drives, Mobile Computing</title>
    
    <!-- Instant Anti-FOUC Theme Preload Script -->
    <script>
        (function() {
            const savedTheme = localStorage.getItem('ktu_portal_theme') || 'dark';
            document.documentElement.setAttribute('data-theme', savedTheme);
        })();
    </script>

    <!-- KaTeX CDN for Clean Mathematical Formula Rendering -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
        onload="renderMathInElement(document.body, {
            delimiters: [
                {left: '$$', right: '$$', display: true},
                {left: '$', right: '$', display: false}
            ],
            throwOnError: false
        });"></script>

    <!-- Google Fonts: Inter & JetBrains Mono -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">

    <style>
        {{CSS_BLOCK}}
    </style>
</head>
<body>

    <!-- Header & Navigation Bar (Stuck at Top of Page, Does NOT Follow Scroll) -->
    <header class="site-header">
        <div class="header-top-row">
            <div class="brand-container">
                <div class="brand-logo-icon" aria-hidden="true">⚡</div>
                <div class="brand-text">
                    <h1>KTU Mastery Portal</h1>
                    <p class="brand-subtext">7th Sem B.Tech Question Bank</p>
                </div>
            </div>

            <!-- Subject Switcher Tabs (3 Web Pages in One Index Page) -->
            <nav class="subject-tabs" role="tablist" aria-label="Subject Selection Tabs">
                <button class="tab-btn active tab-acs" data-target="view-acs" role="tab" aria-selected="true">
                    <span class="tab-icon">📘</span>
                    <span class="tab-text-full">Advanced Control Systems (EET401)</span>
                    <span class="tab-text-short">ACS (EET401)</span>
                </button>
                <button class="tab-btn tab-drive" data-target="view-drive" role="tab" aria-selected="false">
                    <span class="tab-icon">⚡</span>
                    <span class="tab-text-full">Electric Drives (EET413)</span>
                    <span class="tab-text-short">Drives (EET413)</span>
                </button>
                <button class="tab-btn tab-mobile" data-target="view-mobile" role="tab" aria-selected="false">
                    <span class="tab-icon">📱</span>
                    <span class="tab-text-full">Mobile Computing (CST415)</span>
                    <span class="tab-text-short">Mobile (CST415)</span>
                </button>
            </nav>

            <!-- Theme Switcher Controls (Night, Day, Sage) -->
            <div class="theme-switcher-wrapper" role="radiogroup" aria-label="Reading &amp; Study Theme Selector">
                <button class="theme-btn active" data-theme-value="dark" title="Soft Charcoal: Neutral Soft Slate (Balanced Reading Contrast)">
                    <span class="theme-icon">🌙</span>
                    <span class="theme-name">Charcoal</span>
                </button>
                <button class="theme-btn" data-theme-value="warm" title="Warm Espresso: Kindle-Style Sepia Dark (Zero Blue Light, Maximum Eye Comfort)">
                    <span class="theme-icon">☕</span>
                    <span class="theme-name">Espresso</span>
                </button>
                <button class="theme-btn" data-theme-value="forest" title="Forest Night: Calming Deep Pine &amp; Soft Mint (Lowest Eye Strain)">
                    <span class="theme-icon">🌲</span>
                    <span class="theme-name">Forest</span>
                </button>
                <button class="theme-btn" data-theme-value="oled" title="Midnight OLED: Minimalist True Black (Zero Light Bleed)">
                    <span class="theme-icon">🌑</span>
                    <span class="theme-name">OLED</span>
                </button>
                <button class="theme-btn" data-theme-value="light" title="Day Mode: Warm Slate &amp; Off-White Paper (Ergonomic Daylight Reading)">
                    <span class="theme-icon">☀️</span>
                    <span class="theme-name">Day</span>
                </button>
                <button class="theme-btn" data-theme-value="sage" title="Cool Focus Mode: Pale Sage &amp; Deep Forest (Reduced Eye Fatigue)">
                    <span class="theme-icon">🍃</span>
                    <span class="theme-name">Sage</span>
                </button>
            </div>
        </div>

        <!-- Controls: Search and Dynamic Filtering -->
        <div class="controls-row">
            <div class="search-box-wrapper">
                <span class="search-icon">🔍</span>
                <input type="text" id="global-search" class="search-input" placeholder="Search questions, derivations, equations, concepts...">
            </div>

            <div class="filter-buttons">
                <button class="filter-btn active" data-filter="all">All Questions</button>
                <button class="filter-btn" data-filter="3m">3 Marks Only</button>
                <button class="filter-btn" data-filter="7m">7/14 Marks Only</button>
                <button class="filter-btn global-collapse-btn" id="btn-toggle-all-answers" onclick="toggleAllAnswers()" title="Collapse all answers for Self-Test / Flashcard Exam Practice">
                    <span class="btn-icon">👁️</span>
                    <span class="btn-text">Collapse All Answers</span>
                </button>
                <span class="stats-badge" id="stats-pill">{{GRAND_TOTAL}} Master Answers Available</span>
            </div>
        </div>
    </header>

    <!-- Main Content Container containing 3 Integrated Views -->
    <main class="content-container">

        <!-- 3-Hour Exam Writing Strategy Banner -->
        <section class="exam-strategy-banner" aria-label="3-Hour Exam Time Budget">
            <div class="strategy-icon" aria-hidden="true">⏱️</div>
            <div class="strategy-content">
                <h4>3-Hour Exam Time Budget (20 Questions / 100 Marks Strategy)</h4>
                <p><strong>Part A (10 Short Answers &times; 3 Marks = 30M):</strong> Allocate <strong>5 mins per answer</strong> (50 mins total) &mdash; target &frac12; to 1 page highlighting the key formula and core definition.<br>
                <strong>Part B (10 Essay Answers &times; 7 Marks = 70M):</strong> Allocate <strong>12 mins per answer</strong> (120 mins total) &mdash; target 1.5 to 2 pages with schematic circuit/block diagrams and step-by-step derivations.<br>
                <strong>Strategy &amp; Review Buffer (10 mins):</strong> 5 mins at start for question choice planning + 5 mins at end for question numbering and equation verification.</p>
            </div>
        </section>

        <!-- VIEW 1: Advanced Control Systems (EET401) -->
        <div id="view-acs" class="subject-view active">
            <div class="subject-hero hero-acs">
                <span class="hero-badge">Course Code: EET401</span>
                <h2>Advanced Control Systems</h2>
                <p>Complete university previous year questions, continuous LTI and non-linear system state models, solution of state equations, Cayley-Hamilton state transition matrices, Kalman controllability/observability, Ackermann state feedback pole placement, Luenberger observers, describing functions for non-linear saturation, phase plane singular point analysis, and Lyapunov stability theorems.</p>
            </div>
            {{ACS_CONTENT}}
        </div>

        <!-- VIEW 2: Electric Drives (EET413) -->
        <div id="view-drive" class="subject-view">
            <div class="subject-hero hero-drive">
                <span class="hero-badge">Course Code: EET413</span>
                <h2>Electric Drives</h2>
                <p>Exhaustive coverage of drive dynamics, fundamental dynamic torque equation derivations, four-quadrant hoist operations, steady-state stability criteria, phase-controlled converter DC drives with firing angle problem solving, chopper-controlled two-quadrant drives, closed-loop cascade speed control, induction motor stator voltage and V/f speed control, static rotor resistance chopper drives, synchronous motor drives, Space Vector PWM, Clarke/Park reference frame transformations, and Field-Oriented Control (FOC).</p>
            </div>
            {{DRIVE_CONTENT}}
        </div>

        <!-- VIEW 3: Introduction to Mobile Computing (CST415) -->
        <div id="view-mobile" class="subject-view">
            <div class="subject-hero hero-mobile">
                <span class="hero-badge">Course Code: CST415</span>
                <h2>Introduction to Mobile Computing</h2>
                <p>Comprehensive curriculum guide and university question bank encompassing the official CST415 syllabus, three-tier mobile computing architecture, client context and adaptability management, cellular multiple access (FDMA, TDMA, CDMA, SDMA), GEO/LEO/MEO satellites, full GSM network architecture with A3/A8/A5 security algorithms, SMS/GPRS architecture and packet workflows, IEEE 802.11 WLAN with hidden/exposed terminal RTS/CTS mechanics, Wireless Local Loop (WLL), Public Key RSA cryptosystem numerical problem solving, Diffie-Hellman key exchange, TLS/SSL protocols, and Orthogonal Frequency Division Multiplexing (OFDM).</p>
            </div>
            {{MOBILE_SYLLABUS_CONTENT}}
            {{MOBILE_CONTENT}}
        </div>

    </main>

    <!-- Floating Back to Top Button -->
    <button class="back-to-top-btn" id="back-to-top" onclick="scrollToTop()" title="Scroll to top of page">
        <span>↑</span> Top
    </button>

    <!-- Footer -->
    <footer class="site-footer">
        <div class="footer-content">
            <div class="footer-links">
                <a href="#view-acs" onclick="switchTab('view-acs')">Advanced Control Systems</a>
                <a href="#view-drive" onclick="switchTab('view-drive')">Electric Drives</a>
                <a href="#view-mobile" onclick="switchTab('view-mobile')">Mobile Computing</a>
            </div>
            <p>Designed for APJ Abdul Kalam Technological University (KTU) Engineering Students. Formatted with rigorous paragraph-style academic answers, step-by-step mathematical derivations with KaTeX, explicit image placeholders, and targeted YouTube problem-solving video links.</p>
            <p>&copy; 2026 Academic Engineering Portal. All rights reserved.</p>
        </div>
    </footer>

    <!-- Interactive Client-Side JavaScript -->
    <script>
        {{JS_BLOCK}}
    </script>
</body>
</html>
"""

def generate_standalone_page(subject_key, subject_title, subject_code, subject_color, subject_view_id, inner_html):
    template = """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>{{SUBJECT_TITLE}} ({{SUBJECT_CODE}}) | KTU Exam Portal</title>
    
    <!-- Instant Anti-FOUC Theme Preload Script -->
    <script>
        (function() {
            const savedTheme = localStorage.getItem('ktu_portal_theme') || 'dark';
            document.documentElement.setAttribute('data-theme', savedTheme);
        })();
    </script>

    <!-- KaTeX CDN -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
        onload="renderMathInElement(document.body, {
            delimiters: [
                {left: '$$', right: '$$', display: true},
                {left: '$', right: '$', display: false}
            ],
            throwOnError: false
        });"></script>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">

    <style>
        {{CSS_BLOCK}}
    </style>
</head>
<body>
    <header class="site-header">
        <div class="header-top-row">
            <div class="brand-container">
                <div class="brand-logo-icon">⚡</div>
                <div class="brand-text">
                    <h1>{{SUBJECT_TITLE}} ({{SUBJECT_CODE}})</h1>
                    <p>KTU Engineering B.Tech Examination Preparation</p>
                </div>
            </div>

            <!-- Theme Switcher Controls (Night, Day, Sage) -->
            <div class="theme-switcher-wrapper" role="radiogroup" aria-label="Reading &amp; Study Theme Selector">
                <button class="theme-btn active" data-theme-value="dark" title="Soft Charcoal: Neutral Soft Slate (Balanced Reading Contrast)">
                    <span class="theme-icon">🌙</span>
                    <span class="theme-name">Charcoal</span>
                </button>
                <button class="theme-btn" data-theme-value="warm" title="Warm Espresso: Kindle-Style Sepia Dark (Zero Blue Light, Maximum Eye Comfort)">
                    <span class="theme-icon">☕</span>
                    <span class="theme-name">Espresso</span>
                </button>
                <button class="theme-btn" data-theme-value="forest" title="Forest Night: Calming Deep Pine &amp; Soft Mint (Lowest Eye Strain)">
                    <span class="theme-icon">🌲</span>
                    <span class="theme-name">Forest</span>
                </button>
                <button class="theme-btn" data-theme-value="oled" title="Midnight OLED: Minimalist True Black (Zero Light Bleed)">
                    <span class="theme-icon">🌑</span>
                    <span class="theme-name">OLED</span>
                </button>
                <button class="theme-btn" data-theme-value="light" title="Day Mode: Warm Slate &amp; Off-White Paper (Ergonomic Daylight Reading)">
                    <span class="theme-icon">☀️</span>
                    <span class="theme-name">Day</span>
                </button>
                <button class="theme-btn" data-theme-value="sage" title="Cool Focus Mode: Pale Sage &amp; Deep Forest (Reduced Eye Fatigue)">
                    <span class="theme-icon">🍃</span>
                    <span class="theme-name">Sage</span>
                </button>
            </div>

            <div style="display:flex; align-items:center; gap:0.5rem; flex-wrap:wrap;">
                <button class="filter-btn global-collapse-btn" id="btn-toggle-all-answers" onclick="toggleAllAnswers()" title="Collapse all answers for Self-Test / Flashcard Exam Practice">
                    <span class="btn-icon">👁️</span>
                    <span class="btn-text">Collapse All Answers</span>
                </button>
                <a href="index.html" class="standalone-back-btn" title="Return to Master Portal">← 3-in-1 Portal</a>
            </div>
        </div>
    </header>

    <main class="content-container">
        <!-- 3-Hour Exam Writing Strategy Banner -->
        <section class="exam-strategy-banner" aria-label="3-Hour Exam Time Budget">
            <div class="strategy-icon" aria-hidden="true">⏱️</div>
            <div class="strategy-content">
                <h4>3-Hour Exam Time Budget (20 Questions / 100 Marks Strategy)</h4>
                <p><strong>Part A (10 Short Answers &times; 3 Marks = 30M):</strong> Allocate <strong>5 mins per answer</strong> (50 mins total) &mdash; target &frac12; to 1 page highlighting the key formula and core definition.<br>
                <strong>Part B (10 Essay Answers &times; 7 Marks = 70M):</strong> Allocate <strong>12 mins per answer</strong> (120 mins total) &mdash; target 1.5 to 2 pages with schematic circuit/block diagrams and step-by-step derivations.<br>
                <strong>Strategy &amp; Review Buffer (10 mins):</strong> 5 mins at start for question choice planning + 5 mins at end for question numbering and equation verification.</p>
            </div>
        </section>
        {{INNER_HTML}}
    </main>

    <button class="back-to-top-btn" id="back-to-top" onclick="window.scrollTo({top: 0, behavior: 'smooth'})" title="Scroll to top of page">
        <span>↑</span> Top
    </button>
    <script>
        window.addEventListener('scroll', () => {
            const topBtn = document.getElementById('back-to-top');
            if (topBtn) {
                if (window.scrollY > 350) topBtn.classList.add('visible');
                else topBtn.classList.remove('visible');
            }
        });

        // Theme Switcher for Standalone Pages
        const THEME_STORAGE_KEY = 'ktu_portal_theme';
        const VALID_THEMES = ['dark', 'warm', 'forest', 'oled', 'light', 'sage'];
        function setTheme(themeName) {
            if (!VALID_THEMES.includes(themeName)) themeName = 'dark';
            document.documentElement.setAttribute('data-theme', themeName);
            try { localStorage.setItem(THEME_STORAGE_KEY, themeName); } catch (e) {}
            const btns = document.querySelectorAll('.theme-btn');
            btns.forEach(btn => {
                if (btn.getAttribute('data-theme-value') === themeName) {
                    btn.classList.add('active');
                    btn.setAttribute('aria-checked', 'true');
                } else {
                    btn.classList.remove('active');
                    btn.setAttribute('aria-checked', 'false');
                }
            });
        }
        document.querySelectorAll('.theme-btn').forEach(btn => {
            btn.addEventListener('click', () => setTheme(btn.getAttribute('data-theme-value')));
        });
        setTheme(localStorage.getItem(THEME_STORAGE_KEY) || 'dark');

        // Interactive Exam Countdown Timers
        const cardTimers = {};

        function formatTimerMMSS(seconds) {
            const m = Math.floor(seconds / 60);
            const s = seconds % 60;
            return (m < 10 ? '0' : '') + m + ':' + (s < 10 ? '0' : '') + s;
        }

        function toggleCardTimer(qid) {
            const widget = document.getElementById('timer-' + qid);
            if (!widget) return;
            const duration = parseInt(widget.getAttribute('data-duration') || '300', 10);
            
            if (!cardTimers[qid]) {
                cardTimers[qid] = {
                    duration: duration,
                    remaining: duration,
                    intervalId: null,
                    state: 'idle'
                };
            }
            
            const timer = cardTimers[qid];
            const displaySpan = widget.querySelector('.timer-display');
            const actionSpan = widget.querySelector('.timer-action');
            const resetBtn = widget.querySelector('.timer-reset-btn');

            if (timer.state === 'running') {
                clearInterval(timer.intervalId);
                timer.intervalId = null;
                timer.state = 'paused';
                actionSpan.textContent = 'Resume';
                widget.classList.remove('timer-running');
                widget.classList.add('timer-paused');
            } else {
                if (timer.state === 'expired') {
                    timer.remaining = timer.duration;
                    widget.classList.remove('timer-expired');
                }
                timer.state = 'running';
                actionSpan.textContent = 'Pause';
                if (resetBtn) resetBtn.style.display = 'inline-flex';
                widget.classList.remove('timer-paused');
                widget.classList.add('timer-running');

                timer.intervalId = setInterval(() => {
                    timer.remaining--;
                    displaySpan.textContent = formatTimerMMSS(timer.remaining);

                    if (timer.remaining <= 60 && timer.remaining > 0) {
                        widget.classList.add('timer-warning');
                    }

                    if (timer.remaining <= 0) {
                        clearInterval(timer.intervalId);
                        timer.intervalId = null;
                        timer.state = 'expired';
                        displaySpan.textContent = '00:00';
                        actionSpan.textContent = "Time's Up!";
                        widget.classList.remove('timer-running', 'timer-warning');
                        widget.classList.add('timer-expired');
                    }
                }, 1000);
            }
        }

        function resetCardTimer(qid) {
            const widget = document.getElementById('timer-' + qid);
            if (!widget || !cardTimers[qid]) return;
            const timer = cardTimers[qid];
            if (timer.intervalId) {
                clearInterval(timer.intervalId);
                timer.intervalId = null;
            }
            timer.remaining = timer.duration;
            timer.state = 'idle';

            const displaySpan = widget.querySelector('.timer-display');
            const actionSpan = widget.querySelector('.timer-action');
            const resetBtn = widget.querySelector('.timer-reset-btn');

            displaySpan.textContent = formatTimerMMSS(timer.duration);
            actionSpan.textContent = 'Start';
            if (resetBtn) resetBtn.style.display = 'none';
            widget.classList.remove('timer-running', 'timer-paused', 'timer-warning', 'timer-expired');
        }

        // Answer Collapse / Expand Toggle
        function toggleAnswerCard(qid) {
            const card = document.getElementById(qid);
            if (!card) return;
            const isCollapsed = card.classList.toggle('answer-collapsed');
            const toggleBtn = card.querySelector('.btn-toggle-answer');
            if (toggleBtn) {
                if (isCollapsed) {
                    toggleBtn.innerHTML = '<span class="toggle-icon">▼</span> <span class="toggle-text">Show Answer</span>';
                    toggleBtn.setAttribute('title', 'Show elaborated answer');
                } else {
                    toggleBtn.innerHTML = '<span class="toggle-icon">▲</span> <span class="toggle-text">Hide Answer</span>';
                    toggleBtn.setAttribute('title', 'Hide elaborated answer');
                }
            }
        }

        let allAnswersCollapsed = false;
        function toggleAllAnswers() {
            allAnswersCollapsed = !allAnswersCollapsed;
            const cards = document.querySelectorAll('.question-card');
            const globalBtns = document.querySelectorAll('.global-collapse-btn');
            
            cards.forEach(card => {
                const toggleBtn = card.querySelector('.btn-toggle-answer');
                if (allAnswersCollapsed) {
                    card.classList.add('answer-collapsed');
                    if (toggleBtn) {
                        toggleBtn.innerHTML = '<span class="toggle-icon">▼</span> <span class="toggle-text">Show Answer</span>';
                        toggleBtn.setAttribute('title', 'Show elaborated answer');
                    }
                } else {
                    card.classList.remove('answer-collapsed');
                    if (toggleBtn) {
                        toggleBtn.innerHTML = '<span class="toggle-icon">▲</span> <span class="toggle-text">Hide Answer</span>';
                        toggleBtn.setAttribute('title', 'Hide elaborated answer');
                    }
                }
            });

            globalBtns.forEach(btn => {
                if (allAnswersCollapsed) {
                    btn.innerHTML = '<span class="btn-icon">📖</span> <span class="btn-text">Expand All Answers</span>';
                    btn.classList.add('active-collapsed');
                } else {
                    btn.innerHTML = '<span class="btn-icon">👁️</span> <span class="btn-text">Collapse All Answers</span>';
                    btn.classList.remove('active-collapsed');
                }
            });
        }
    </script>

    <footer class="site-footer">
        <p>&copy; 2026 Academic Engineering Portal. Standalone Edition.</p>
    </footer>
</body>
</html>
"""
    return (template
        .replace("{{SUBJECT_TITLE}}", subject_title)
        .replace("{{SUBJECT_CODE}}", subject_code)
        .replace("{{CSS_BLOCK}}", CSS_STYLES)
        .replace("{{INNER_HTML}}", inner_html)
    )

def main():
    print("Generating comprehensive website portal with ergonomic themes...")

    acs_html = '\n'.join([render_module_section(m, "subject-acs") for m in ACS_MODULES])
    drive_html = '\n'.join([render_module_section(m, "subject-drive") for m in DRIVE_MODULES])
    mobile_syl_html = render_mobile_syllabus_section()
    mobile_qs_html = '\n'.join([render_module_section(m, "subject-mobile") for m in MOBILE_MODULES])

    total_acs_q = sum(len(m["questions"]) for m in ACS_MODULES)
    total_drive_q = sum(len(m["questions"]) for m in DRIVE_MODULES)
    total_mobile_q = sum(len(m["questions"]) for m in MOBILE_MODULES)
    grand_total = total_acs_q + total_drive_q + total_mobile_q

    # 1. Generate index.html
    full_html = (INDEX_TEMPLATE
        .replace("{{CSS_BLOCK}}", CSS_STYLES)
        .replace("{{JS_BLOCK}}", JS_SCRIPT)
        .replace("{{GRAND_TOTAL}}", str(grand_total))
        .replace("{{ACS_CONTENT}}", acs_html)
        .replace("{{DRIVE_CONTENT}}", drive_html)
        .replace("{{MOBILE_SYLLABUS_CONTENT}}", mobile_syl_html)
        .replace("{{MOBILE_CONTENT}}", mobile_qs_html)
    )

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Generated index.html successfully ({len(full_html)} bytes, {grand_total} questions).")

    # 2. Generate acs.html
    acs_inner = f"""
    <div class="subject-hero hero-acs">
        <span class="hero-badge">Course Code: EET401</span>
        <h2>Advanced Control Systems</h2>
        <p>Complete university previous year questions, continuous LTI and non-linear system state models, solution of state equations, Cayley-Hamilton state transition matrices, Kalman controllability/observability, Ackermann state feedback pole placement, Luenberger observers, describing functions for non-linear saturation, phase plane singular point analysis, and Lyapunov stability theorems.</p>
    </div>
    """ + acs_html
    acs_page = generate_standalone_page("acs", "Advanced Control Systems", "EET401", "#38bdf8", "view-acs", acs_inner)
    with open("acs.html", "w", encoding="utf-8") as f:
        f.write(acs_page)
    print("Generated acs.html successfully.")

    # 3. Generate drives.html
    drive_inner = f"""
    <div class="subject-hero hero-drive">
        <span class="hero-badge">Course Code: EET413</span>
        <h2>Electric Drives</h2>
        <p>Exhaustive coverage of drive dynamics, fundamental dynamic torque equation derivations, four-quadrant hoist operations, steady-state stability criteria, phase-controlled converter DC drives with firing angle problem solving, chopper-controlled two-quadrant drives, closed-loop cascade speed control, induction motor stator voltage and V/f speed control, static rotor resistance chopper drives, synchronous motor drives, Space Vector PWM, Clarke/Park reference frame transformations, and Field-Oriented Control (FOC).</p>
    </div>
    """ + drive_html
    drive_page = generate_standalone_page("drive", "Electric Drives", "EET413", "#f59e0b", "view-drive", drive_inner)
    with open("drives.html", "w", encoding="utf-8") as f:
        f.write(drive_page)
    print("Generated drives.html successfully.")

    # 4. Generate mobile_computing.html
    mobile_inner = f"""
    <div class="subject-hero hero-mobile">
        <span class="hero-badge">Course Code: CST415</span>
        <h2>Introduction to Mobile Computing</h2>
        <p>Comprehensive curriculum guide and university question bank encompassing the official CST415 syllabus, three-tier mobile computing architecture, client context and adaptability management, cellular multiple access (FDMA, TDMA, CDMA, SDMA), GEO/LEO/MEO satellites, full GSM network architecture with A3/A8/A5 security algorithms, SMS/GPRS architecture and packet workflows, IEEE 802.11 WLAN with hidden/exposed terminal RTS/CTS mechanics, Wireless Local Loop (WLL), Public Key RSA cryptosystem numerical problem solving, Diffie-Hellman key exchange, TLS/SSL protocols, and Orthogonal Frequency Division Multiplexing (OFDM).</p>
    </div>
    """ + mobile_syl_html + mobile_qs_html
    mobile_page = generate_standalone_page("mobile", "Introduction to Mobile Computing", "CST415", "#10b981", "view-mobile", mobile_inner)
    with open("mobile_computing.html", "w", encoding="utf-8") as f:
        f.write(mobile_page)
    print("Generated mobile_computing.html successfully.")

if __name__ == "__main__":
    main()
