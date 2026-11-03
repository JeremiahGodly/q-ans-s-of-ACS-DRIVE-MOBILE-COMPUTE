# scratch/gen_activities.py
# Generates the gamified Focus Lab & Interactive Activities page (activities.html)
# Features 5 interactive mini-games, Web Audio sound effects, Nano Banana visual portals,
# and the expanded Speed Drill: Formula Lightning Rush separated by 3 subjects with 39+ high-weightage formulas.

def build_activities_html():
    html = r"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>Focus Lab & Engineering Challenges | KTU Mastery Portal</title>
    
    <!-- Instant Anti-FOUC Theme Preload -->
    <script>
        (function() {
            const savedTheme = localStorage.getItem('ktu_portal_theme') || 'dark';
            document.documentElement.setAttribute('data-theme', savedTheme);
            const savedLang = localStorage.getItem('ktu_portal_lang') || 'en';
            document.documentElement.setAttribute('data-lang', savedLang);
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

    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&family=Noto+Sans+Malayalam:wght@400;500;600;700&display=swap" rel="stylesheet">

    <style>
        :root, [data-theme="dark"] {
            --bg-base: #0c1017;
            --bg-surface: #121824;
            --bg-card: #182232;
            --bg-card-hover: #1f2c40;
            --border-subtle: #25334a;
            --border-focus: #38bdf8;
            --text-main: #f1f5f9;
            --text-body: #cbd5e1;
            --text-muted: #8393a8;
            --header-bg: rgba(15, 21, 32, 0.94);
            --acs-color: #38bdf8;
            --drive-color: #f59e0b;
            --mobile-color: #ec4899;
            --card-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
        }
        [data-theme="warm"] {
            --bg-base: #14110e;
            --bg-surface: #1d1814;
            --bg-card: #27211b;
            --bg-card-hover: #332b24;
            --border-subtle: #3d332a;
            --border-focus: #fbbf24;
            --text-main: #faf4ed;
            --text-body: #ded4c7;
            --text-muted: #a69888;
            --header-bg: rgba(23, 19, 16, 0.94);
            --acs-color: #38bdf8;
            --drive-color: #f59e0b;
            --mobile-color: #f472b6;
            --card-shadow: 0 10px 25px rgba(0, 0, 0, 0.6);
        }
        [data-theme="forest"] {
            --bg-base: #0c1512;
            --bg-surface: #121f1a;
            --bg-card: #192b24;
            --bg-card-hover: #21382f;
            --border-subtle: #29453a;
            --border-focus: #34d399;
            --text-main: #ecfdf5;
            --text-body: #c7e5d8;
            --text-muted: #7fa896;
            --header-bg: rgba(14, 25, 21, 0.94);
            --acs-color: #38bdf8;
            --drive-color: #fbbf24;
            --mobile-color: #34d399;
            --card-shadow: 0 10px 25px rgba(0, 0, 0, 0.6);
        }
        [data-theme="oled"] {
            --bg-base: #000000;
            --bg-surface: #0a0a0a;
            --bg-card: #141414;
            --bg-card-hover: #1f1f1f;
            --border-subtle: #242424;
            --border-focus: #ffffff;
            --text-main: #ffffff;
            --text-body: #d1d5db;
            --text-muted: #888888;
            --header-bg: rgba(0, 0, 0, 0.96);
            --acs-color: #38bdf8;
            --drive-color: #f59e0b;
            --mobile-color: #ec4899;
            --card-shadow: 0 10px 25px rgba(0, 0, 0, 0.85);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: var(--bg-base);
            color: var(--text-body);
            min-height: 100vh;
            line-height: 1.5;
            padding-bottom: 5rem;
        }

        /* Header */
        .site-header {
            position: sticky;
            top: 0;
            background: var(--header-bg);
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
            border-bottom: 1px solid var(--border-subtle);
            padding: 0.75rem 1.5rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            z-index: 100;
        }
        .brand-link {
            display: flex;
            align-items: center;
            gap: 0.65rem;
            text-decoration: none;
            color: inherit;
        }
        .brand-title {
            font-size: 1.1rem;
            font-weight: 800;
            color: var(--text-main);
            letter-spacing: -0.02em;
        }
        .nav-pills {
            display: flex;
            align-items: center;
            gap: 0.4rem;
        }
        .nav-pill {
            padding: 0.4rem 0.8rem;
            border-radius: 8px;
            font-size: 0.83rem;
            font-weight: 600;
            color: var(--text-body);
            text-decoration: none;
            border: 1px solid transparent;
            transition: all 0.2s ease;
        }
        .nav-pill:hover {
            color: var(--text-main);
            background: rgba(255, 255, 255, 0.06);
            border-color: var(--border-subtle);
        }
        .nav-pill.active {
            background: rgba(56, 189, 248, 0.12);
            color: #38bdf8;
            border-color: rgba(56, 189, 248, 0.35);
        }

        /* Layout Container */
        .page-container {
            max-width: 1240px;
            margin: 0 auto;
            padding: 1.75rem 1.25rem;
        }

        /* Hero Banner with Nano Banana Visual */
        .focus-hero-card {
            position: relative;
            background: linear-gradient(135deg, rgba(30, 41, 59, 0.7) 0%, rgba(15, 23, 42, 0.95) 100%);
            border: 1px solid var(--border-subtle);
            border-radius: 20px;
            overflow: hidden;
            display: grid;
            grid-template-columns: 1fr 340px;
            gap: 1.5rem;
            padding: 2rem;
            margin-bottom: 2.5rem;
            box-shadow: 0 20px 45px rgba(0, 0, 0, 0.4);
        }
        .focus-hero-content {
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        .hero-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: #38bdf8;
            background: rgba(56, 189, 248, 0.15);
            padding: 0.25rem 0.65rem;
            border-radius: 999px;
            width: fit-content;
            margin-bottom: 0.85rem;
        }
        .hero-title {
            font-size: 2rem;
            font-weight: 800;
            color: var(--text-main);
            letter-spacing: -0.03em;
            line-height: 1.2;
            margin-bottom: 0.75rem;
        }
        .hero-desc {
            font-size: 0.95rem;
            color: var(--text-body);
            line-height: 1.6;
            margin-bottom: 1.25rem;
        }
        .hero-stats-row {
            display: flex;
            align-items: center;
            gap: 1.5rem;
        }
        .stat-badge {
            display: flex;
            flex-direction: column;
            gap: 0.15rem;
        }
        .stat-num {
            font-size: 1.4rem;
            font-weight: 800;
            color: #fbbf24;
            font-family: 'JetBrains Mono', monospace;
        }
        .stat-label {
            font-size: 0.75rem;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        .hero-img-wrap {
            border-radius: 14px;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.1);
            height: 100%;
            min-height: 200px;
        }
        .hero-img-wrap img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }

        /* Nano Banana Visual Portals Grid */
        .section-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 1.25rem;
        }
        .section-title {
            font-size: 1.35rem;
            font-weight: 800;
            color: var(--text-main);
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        .visual-portals-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1.25rem;
            margin-bottom: 3rem;
        }
        .portal-card {
            background: var(--bg-card);
            border: 1px solid var(--border-subtle);
            border-radius: 16px;
            overflow: hidden;
            transition: all 0.25s ease;
            box-shadow: var(--card-shadow);
            display: flex;
            flex-direction: column;
        }
        .portal-card:hover {
            transform: translateY(-4px);
            border-color: var(--portal-color, #38bdf8);
            box-shadow: 0 16px 32px rgba(0, 0, 0, 0.6), 0 0 20px var(--portal-glow, rgba(56, 189, 248, 0.3));
        }
        .portal-img-wrap {
            height: 160px;
            overflow: hidden;
            position: relative;
        }
        .portal-img-wrap img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.4s ease;
        }
        .portal-card:hover .portal-img-wrap img {
            transform: scale(1.05);
        }
        .portal-badge {
            position: absolute;
            top: 10px;
            left: 10px;
            font-size: 0.7rem;
            font-weight: 700;
            text-transform: uppercase;
            padding: 0.2rem 0.5rem;
            border-radius: 6px;
            background: rgba(0, 0, 0, 0.7);
            color: #ffffff;
            backdrop-filter: blur(8px);
        }
        .portal-content {
            padding: 1.15rem;
            display: flex;
            flex-direction: column;
            flex-grow: 1;
        }
        .portal-title {
            font-size: 1.05rem;
            font-weight: 700;
            color: var(--text-main);
            margin-bottom: 0.4rem;
        }
        .portal-desc {
            font-size: 0.82rem;
            color: var(--text-muted);
            line-height: 1.45;
            margin-bottom: 0.85rem;
            flex-grow: 1;
        }
        .portal-link {
            font-size: 0.8rem;
            font-weight: 600;
            color: var(--portal-color, #38bdf8);
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
        }
        .portal-link:hover {
            text-decoration: underline;
        }

        /* Activity Cards Grid */
        .activities-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 2rem;
        }

        .game-panel {
            background: var(--bg-card);
            border: 1px solid var(--border-subtle);
            border-radius: 20px;
            padding: 1.5rem;
            box-shadow: var(--card-shadow);
        }
        .game-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 1.25rem;
            padding-bottom: 0.85rem;
            border-bottom: 1px solid var(--border-subtle);
        }
        .game-title-group {
            display: flex;
            align-items: center;
            gap: 0.65rem;
        }
        .game-icon {
            font-size: 1.5rem;
        }
        .game-title {
            font-size: 1.2rem;
            font-weight: 800;
            color: var(--text-main);
        }
        .game-score-badge {
            background: rgba(245, 158, 11, 0.15);
            border: 1px solid rgba(245, 158, 11, 0.3);
            color: #fbbf24;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.85rem;
            font-weight: 700;
            padding: 0.3rem 0.75rem;
            border-radius: 999px;
        }

        /* Activity 1: Pole Hunter */
        .pole-hunter-layout {
            display: grid;
            grid-template-columns: 1fr 280px;
            gap: 1.25rem;
        }
        .splane-canvas-wrap {
            position: relative;
            background: #080b12;
            border: 1px solid var(--border-subtle);
            border-radius: 14px;
            overflow: hidden;
            height: 320px;
        }
        #splane-canvas {
            width: 100%;
            height: 100%;
            display: block;
        }
        .oscilloscope-panel {
            background: #080b12;
            border: 1px solid var(--border-subtle);
            border-radius: 14px;
            padding: 1rem;
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
        }
        .scope-header {
            font-size: 0.78rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: #38bdf8;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        #scope-canvas {
            width: 100%;
            height: 120px;
            background: #04060a;
            border-radius: 8px;
            border: 1px solid rgba(56, 189, 248, 0.2);
        }
        .game-controls-row {
            margin-top: 1rem;
            display: flex;
            align-items: center;
            gap: 1rem;
            background: var(--bg-surface);
            padding: 0.75rem 1rem;
            border-radius: 12px;
            border: 1px solid var(--border-subtle);
        }
        .slider-label {
            font-size: 0.82rem;
            font-weight: 600;
            color: var(--text-main);
            min-width: 140px;
        }
        .custom-slider {
            flex-grow: 1;
            accent-color: #38bdf8;
            cursor: pointer;
        }
        .status-pill {
            font-size: 0.78rem;
            font-weight: 700;
            padding: 0.25rem 0.65rem;
            border-radius: 6px;
        }
        .status-stable {
            background: rgba(16, 185, 129, 0.2);
            color: #34d399;
            border: 1px solid rgba(16, 185, 129, 0.4);
        }
        .status-unstable {
            background: rgba(239, 68, 68, 0.2);
            color: #f87171;
            border: 1px solid rgba(239, 68, 68, 0.4);
        }

        /* Activity 2: 4-Quadrant Chopper EV */
        .chopper-layout {
            display: grid;
            grid-template-columns: 1fr 300px;
            gap: 1.25rem;
        }
        .ev-track-canvas-wrap {
            background: #080b12;
            border: 1px solid var(--border-subtle);
            border-radius: 14px;
            height: 320px;
            position: relative;
            overflow: hidden;
        }
        #ev-canvas {
            width: 100%;
            height: 100%;
            display: block;
        }
        .quadrant-hud {
            background: #080b12;
            border: 1px solid var(--border-subtle);
            border-radius: 14px;
            padding: 1rem;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 0.5rem;
            height: 320px;
        }
        .quadrant-box {
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 8px;
            padding: 0.6rem;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            background: rgba(255, 255, 255, 0.02);
            transition: all 0.2s ease;
        }
        .quadrant-box.active {
            border-color: #f59e0b;
            background: rgba(245, 158, 11, 0.15);
            box-shadow: 0 0 15px rgba(245, 158, 11, 0.3);
        }
        .q-name {
            font-size: 0.72rem;
            font-weight: 700;
            color: var(--text-muted);
            text-transform: uppercase;
        }
        .quadrant-box.active .q-name {
            color: #fbbf24;
        }
        .q-mode {
            font-size: 0.8rem;
            font-weight: 700;
            color: var(--text-main);
            margin: 0.2rem 0;
        }
        .q-signs {
            font-size: 0.7rem;
            font-family: 'JetBrains Mono', monospace;
            color: var(--text-muted);
        }

        /* Activity 3: Lightning Formula Rush */
        .rush-panel-header {
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
            margin-bottom: 1rem;
        }
        .rush-subject-tabs {
            display: flex;
            align-items: center;
            gap: 0.4rem;
            background: var(--bg-surface);
            padding: 0.3rem;
            border-radius: 10px;
            border: 1px solid var(--border-subtle);
            overflow-x: auto;
            scrollbar-width: none;
        }
        .rush-subject-tabs::-webkit-scrollbar {
            display: none;
        }
        .rush-tab {
            background: transparent;
            border: 1px solid transparent;
            color: var(--text-muted);
            font-size: 0.82rem;
            font-weight: 600;
            padding: 0.45rem 0.9rem;
            border-radius: 8px;
            cursor: pointer;
            white-space: nowrap;
            transition: all 0.2s ease;
        }
        .rush-tab:hover {
            color: var(--text-main);
            background: rgba(255, 255, 255, 0.06);
        }
        .rush-tab.active {
            color: #ffffff;
            font-weight: 700;
        }
        .rush-tab[data-subject="all"].active {
            background: #6366f1;
            box-shadow: 0 0 14px rgba(99, 102, 241, 0.4);
        }
        .rush-tab[data-subject="acs"].active {
            background: #0284c7;
            box-shadow: 0 0 14px rgba(2, 132, 199, 0.4);
        }
        .rush-tab[data-subject="drive"].active {
            background: #d97706;
            box-shadow: 0 0 14px rgba(217, 119, 6, 0.4);
        }
        .rush-tab[data-subject="mobile"].active {
            background: #db2777;
            box-shadow: 0 0 14px rgba(219, 39, 119, 0.4);
        }

        .rush-container {
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            border-radius: 16px;
            padding: 1.5rem;
            text-align: center;
            box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.2);
        }
        .rush-timer-bar {
            height: 6px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 999px;
            overflow: hidden;
            margin-bottom: 1.25rem;
        }
        .rush-timer-fill {
            height: 100%;
            background: linear-gradient(90deg, #ec4899, #f59e0b, #38bdf8);
            width: 100%;
            transition: width 0.1s linear;
        }

        .rush-card-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 0.75rem;
        }
        .rush-subject-pill {
            font-size: 0.72rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            padding: 0.2rem 0.6rem;
            border-radius: 6px;
            background: rgba(56, 189, 248, 0.15);
            color: #38bdf8;
            border: 1px solid rgba(56, 189, 248, 0.3);
        }
        .rush-index-pill {
            font-size: 0.75rem;
            font-family: 'JetBrains Mono', monospace;
            color: var(--text-muted);
        }

        .rush-formula-card {
            background: rgba(0, 0, 0, 0.45);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 14px;
            padding: 1.75rem 1rem;
            font-size: 1.45rem;
            margin-bottom: 1.5rem;
            min-height: 105px;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow-x: auto;
            box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.5);
            transition: border-color 0.25s ease;
        }
        .rush-options-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 0.85rem;
            margin-bottom: 1rem;
        }
        .rush-btn {
            background: var(--bg-card);
            border: 1px solid var(--border-subtle);
            border-radius: 12px;
            padding: 0.9rem 1.15rem;
            font-size: 0.88rem;
            font-weight: 600;
            color: var(--text-body);
            cursor: pointer;
            transition: all 0.2s ease;
            text-align: left;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            line-height: 1.4;
        }
        .rush-btn:hover {
            border-color: #38bdf8;
            color: var(--text-main);
            background: rgba(56, 189, 248, 0.08);
            transform: translateY(-2px);
        }
        .rush-btn.correct {
            background: rgba(16, 185, 129, 0.25) !important;
            border-color: #34d399 !important;
            color: #ffffff !important;
            box-shadow: 0 0 16px rgba(16, 185, 129, 0.35);
        }
        .rush-btn.wrong {
            background: rgba(239, 68, 68, 0.25) !important;
            border-color: #f87171 !important;
            color: #ffffff !important;
            box-shadow: 0 0 16px rgba(239, 68, 68, 0.35);
        }

        .rush-bottom-bar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding-top: 0.85rem;
            border-top: 1px solid var(--border-subtle);
            font-size: 0.8rem;
            color: var(--text-muted);
        }
        .btn-skip-rush {
            background: transparent;
            border: 1px solid var(--border-subtle);
            color: var(--text-muted);
            padding: 0.35rem 0.75rem;
            border-radius: 6px;
            cursor: pointer;
            font-size: 0.78rem;
            font-weight: 600;
            transition: all 0.2s ease;
        }
        .btn-skip-rush:hover {
            color: var(--text-main);
            border-color: var(--border-focus);
        }

        /* Responsive Mobile Styles */
        @media (max-width: 900px) {
            .focus-hero-card {
                grid-template-columns: 1fr;
            }
            .hero-img-wrap {
                height: 180px;
            }
            .visual-portals-grid {
                grid-template-columns: 1fr;
            }
            .pole-hunter-layout, .chopper-layout {
                grid-template-columns: 1fr;
            }
            .rush-options-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>

    <!-- Header Navigation -->
    <header class="site-header">
        <a href="index.html" class="brand-link">
            <span style="font-size:1.5rem;">⚡</span>
            <span class="brand-title">KTU Focus Lab &amp; Challenges</span>
        </a>

        <nav class="nav-pills">
            <a href="index.html" class="nav-pill">📚 Question Bank</a>
            <a href="mindmap.html" class="nav-pill">🧠 Mind Map</a>
            <a href="activities.html" class="nav-pill active">🎯 Focus Lab</a>
            <a href="animations.html" class="nav-pill">🎬 60fps Simulators</a>
        </nav>
    </header>

    <main class="page-container">

        <!-- Hero Card with Nano Banana Arcade Visual -->
        <section class="focus-hero-card">
            <div class="focus-hero-content">
                <span class="hero-badge">⚡ Interactive Engineering Playground</span>
                <h1 class="hero-title">Stay Laser-Focused On Complex Engineering</h1>
                <p class="hero-desc">
                    Transform abstract differential equations, electromagnetic torque curves, and wireless MAC protocols into tactile, playable challenges. Earn study streaks and test your intuition before exam day!
                </p>
                <div class="hero-stats-row">
                    <div class="stat-badge">
                        <span class="stat-num" id="total-xp">3,450 XP</span>
                        <span class="stat-label">Engineering Score</span>
                    </div>
                    <div class="stat-badge">
                        <span class="stat-num" id="streak-counter">🔥 7 Days</span>
                        <span class="stat-label">Focus Streak</span>
                    </div>
                    <div class="stat-badge">
                        <span class="stat-num">94 / 94</span>
                        <span class="stat-label">Syllabus Covered</span>
                    </div>
                </div>
            </div>
            <div class="hero-img-wrap">
                <img src="images/visuals/focus_arcade_hero.jpg" alt="3D Neon Arcade Machine for Engineering Focus" loading="lazy">
            </div>
        </section>

        <!-- Visual Portals Gallery (Nano Banana Visuals) -->
        <div class="section-header">
            <h2 class="section-title"><span>🌟</span> Subject Visual Portals</h2>
            <span style="font-size:0.82rem; color:var(--text-muted);">High-resolution immersive study worlds</span>
        </div>

        <div class="visual-portals-grid">
            <!-- ACS Portal -->
            <div class="portal-card" style="--portal-color:#38bdf8; --portal-glow:rgba(56, 189, 248, 0.35);">
                <div class="portal-img-wrap">
                    <span class="portal-badge">ACS • EET401</span>
                    <img src="images/visuals/acs_cyber_core.jpg" alt="Advanced Control Systems Cybernetic Core" loading="lazy">
                </div>
                <div class="portal-content">
                    <h3 class="portal-title">Cybernetic State-Space Core</h3>
                    <p class="portal-desc">Holographic state vectors, phase trajectories, limit cycles, and Liapunov energy basins rendered in luminous cybernetic detail.</p>
                    <a href="acs.html" class="portal-link">Explore 29 ACS Questions &rarr;</a>
                </div>
            </div>

            <!-- Drives Portal -->
            <div class="portal-card" style="--portal-color:#f59e0b; --portal-glow:rgba(245, 158, 11, 0.35);">
                <div class="portal-img-wrap">
                    <span class="portal-badge">Drives • EET413</span>
                    <img src="images/visuals/electric_drives_flux.jpg" alt="Electric Drives Electromagnetic Flux Stator" loading="lazy">
                </div>
                <div class="portal-content">
                    <h3 class="portal-title">Electromagnetic Powertrain</h3>
                    <p class="portal-desc">High-voltage induction motor cutaways with pulsing flux lines, inverter semiconductor switching, and 4-quadrant EV torque dynamics.</p>
                    <a href="drives.html" class="portal-link">Explore 27 Drives Questions &rarr;</a>
                </div>
            </div>

            <!-- Mobile Portal -->
            <div class="portal-card" style="--portal-color:#ec4899; --portal-glow:rgba(236, 72, 153, 0.35);">
                <div class="portal-img-wrap">
                    <span class="portal-badge">Mobile • CST415</span>
                    <img src="images/visuals/mobile_cellular_grid.jpg" alt="Mobile Computing Cellular Grid and Satellite Downlinks" loading="lazy">
                </div>
                <div class="portal-content">
                    <h3 class="portal-title">Orbital Cellular Mesh</h3>
                    <p class="portal-desc">Hexagonal frequency reuse clusters, GSM TDMA frame hierarchies, satellite laser downlinks, and RSA/Diffie-Hellman cryptographic ciphers.</p>
                    <a href="mobile_computing.html" class="portal-link">Explore 38 Mobile Questions &rarr;</a>
                </div>
            </div>
        </div>

        <!-- Interactive Activities & Challenges -->
        <div class="section-header">
            <h2 class="section-title"><span>🎮</span> Focus Drills &amp; Simulators</h2>
        </div>

        <div class="activities-grid">

            <!-- Activity 1: Pole Hunter (ACS) -->
            <div class="game-panel">
                <div class="game-header">
                    <div class="game-title-group">
                        <span class="game-icon">🎯</span>
                        <div>
                            <h3 class="game-title">ACS Challenge: Stability Pole Hunter</h3>
                            <p style="font-size:0.8rem; color:var(--text-muted);">Adjust feedback gain $K$ to pull unstable poles from RHP back into the stable Left-Half Plane!</p>
                        </div>
                    </div>
                    <span class="game-score-badge" id="pole-score">LHP Stabilized: +150 XP</span>
                </div>

                <div class="pole-hunter-layout">
                    <div class="splane-canvas-wrap">
                        <canvas id="splane-canvas"></canvas>
                    </div>
                    <div class="oscilloscope-panel">
                        <div class="scope-header">
                            <span>Step Response Oscilloscope</span>
                            <span class="status-pill status-stable" id="system-status-pill">STABLE (LHP)</span>
                        </div>
                        <canvas id="scope-canvas"></canvas>
                        <p style="font-size:0.75rem; color:var(--text-muted); line-height:1.4;">
                            When closed-loop poles cross the imaginary $j\omega$ axis into the Right Half Plane, the time-domain output explodes exponentially ($e^{+\sigma t}\sin(\omega t)$).
                        </p>
                    </div>
                </div>

                <div class="game-controls-row">
                    <label class="slider-label" for="gain-slider">Feedback Gain $K$: <span id="gain-val" style="color:#38bdf8; font-family:'JetBrains Mono';">2.4</span></label>
                    <input type="range" id="gain-slider" class="custom-slider" min="0.2" max="6.0" step="0.1" value="2.4">
                    <button type="button" class="nav-pill" onclick="resetPoles()" style="cursor:pointer; background:rgba(255,255,255,0.08);">🔄 Reset Poles</button>
                </div>
            </div>

            <!-- Activity 2: 4-Quadrant Chopper EV Racer (Drives) -->
            <div class="game-panel">
                <div class="game-header">
                    <div class="game-title-group">
                        <span class="game-icon">🏎️</span>
                        <div>
                            <h3 class="game-title">Electric Drives: 4-Quadrant Chopper Racer</h3>
                            <p style="font-size:0.8rem; color:var(--text-muted);">Navigate an EV through all 4 quadrants. Regenerate downhill to recharge the battery!</p>
                        </div>
                    </div>
                    <span class="game-score-badge" id="battery-gauge">⚡ Battery: 78% (Regen Active)</span>
                </div>

                <div class="chopper-layout">
                    <div class="ev-track-canvas-wrap">
                        <canvas id="ev-canvas"></canvas>
                    </div>
                    <div class="quadrant-hud">
                        <div class="quadrant-box" id="q2-box">
                            <span class="q-name">Quadrant II</span>
                            <span class="q-mode">Forward Braking</span>
                            <span class="q-signs">$-T_e, +\omega_m$ (Regen)</span>
                        </div>
                        <div class="quadrant-box active" id="q1-box">
                            <span class="q-name">Quadrant I</span>
                            <span class="q-mode">Forward Motoring</span>
                            <span class="q-signs">$+T_e, +\omega_m$</span>
                        </div>
                        <div class="quadrant-box" id="q3-box">
                            <span class="q-name">Quadrant III</span>
                            <span class="q-mode">Reverse Motoring</span>
                            <span class="q-signs">$-T_e, -\omega_m$</span>
                        </div>
                        <div class="quadrant-box" id="q4-box">
                            <span class="q-name">Quadrant IV</span>
                            <span class="q-mode">Reverse Braking</span>
                            <span class="q-signs">$+T_e, -\omega_m$ (Regen)</span>
                        </div>
                    </div>
                </div>

                <div class="game-controls-row">
                    <label class="slider-label" for="duty-slider">Duty Ratio $\alpha = T_{on}/T$: <span id="duty-val" style="color:#f59e0b; font-family:'JetBrains Mono';">0.65</span></label>
                    <input type="range" id="duty-slider" class="custom-slider" min="0.05" max="0.95" step="0.05" value="0.65" style="accent-color:#f59e0b;">
                    <button type="button" class="nav-pill" id="btn-reverse" onclick="toggleDriveDir()" style="cursor:pointer; background:rgba(255,255,255,0.08);">🔁 Reverse Direction</button>
                    <button type="button" class="nav-pill" id="btn-brake" onmousedown="applyRegenBrake(true)" onmouseup="applyRegenBrake(false)" style="cursor:pointer; background:rgba(239, 68, 68, 0.2); color:#f87171;">🛑 Hold Brake</button>
                </div>
            </div>

            <!-- Activity 3: Lightning Formula Rush (Separated by 3 Subjects + All) -->
            <div class="game-panel">
                <div class="game-header">
                    <div class="game-title-group">
                        <span class="game-icon">⚡</span>
                        <div>
                            <h3 class="game-title">Speed Drill: Formula Lightning Rush</h3>
                            <p style="font-size:0.8rem; color:var(--text-muted);">Match high-weightage KTU equations to their physical meaning before time runs out!</p>
                        </div>
                    </div>
                    <span class="game-score-badge" id="rush-score">Score: 0 | Streak: 0x</span>
                </div>

                <div class="rush-panel-header">
                    <!-- Subject Filter Tabs for Rush Drill -->
                    <div class="rush-subject-tabs" role="tablist">
                        <button class="rush-tab active" data-subject="all">🌟 All Subjects (39 Formulas)</button>
                        <button class="rush-tab" data-subject="acs">⚡ ACS (13 Formulas)</button>
                        <button class="rush-tab" data-subject="drive">🏎️ Electric Drives (13 Formulas)</button>
                        <button class="rush-tab" data-subject="mobile">📡 Mobile Computing (13 Formulas)</button>
                    </div>
                </div>

                <div class="rush-container">
                    <div class="rush-timer-bar">
                        <div class="rush-timer-fill" id="rush-timer"></div>
                    </div>

                    <div class="rush-card-header">
                        <span class="rush-subject-pill" id="rush-subject-pill">⚡ ACS</span>
                        <span class="rush-index-pill" id="rush-index-pill">Formula 1 of 39</span>
                    </div>

                    <div class="rush-formula-card" id="rush-eq-display">
                        $$\dot{\mathbf{x}} = A\mathbf{x} + B\mathbf{u}$$
                    </div>

                    <div class="rush-options-grid" id="rush-options">
                        <!-- Options generated dynamically -->
                    </div>

                    <div class="rush-bottom-bar">
                        <span id="rush-accuracy-text">Accuracy: 100% | High Score: 0</span>
                        <button type="button" class="btn-skip-rush" onclick="skipRush()">Skip Formula ⏭️</button>
                    </div>
                </div>
            </div>

        </div>

    </main>

    <!-- Interactive Canvas Game Scripts -->
    <script>
        // Web Audio Synthesizer for high-energy gamified feedback
        let audioCtx = null;
        function playChime(freq = 520, type = 'sine', duration = 0.15) {
            try {
                if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                if (audioCtx.state === 'suspended') audioCtx.resume();
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.type = type;
                osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
                gain.gain.setValueAtTime(0.12, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration);
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                osc.start();
                osc.stop(audioCtx.currentTime + duration);
            } catch(e) {}
        }

        // =========================================================================
        // POLE HUNTER (ACS)
        // =========================================================================
        const splaneCanvas = document.getElementById('splane-canvas');
        const sCtx = splaneCanvas.getContext('2d');
        const scopeCanvas = document.getElementById('scope-canvas');
        const scCtx = scopeCanvas.getContext('2d');
        const gainSlider = document.getElementById('gain-slider');
        const gainVal = document.getElementById('gain-val');
        const statusPill = document.getElementById('system-status-pill');

        let gainK = 2.4;
        let isStable = true;
        let scopeTime = 0;

        function resizePoles() {
            splaneCanvas.width = splaneCanvas.parentElement.clientWidth;
            splaneCanvas.height = 320;
            scopeCanvas.width = scopeCanvas.parentElement.clientWidth;
            scopeCanvas.height = 120;
        }
        window.addEventListener('resize', resizePoles);
        resizePoles();

        gainSlider.addEventListener('input', e => {
            gainK = parseFloat(e.target.value);
            gainVal.textContent = gainK.toFixed(1);
            // System stable if K between 1.0 and 4.8
            isStable = (gainK >= 1.0 && gainK <= 4.8);
            if (isStable) {
                statusPill.className = 'status-pill status-stable';
                statusPill.textContent = 'STABLE (LHP)';
            } else {
                statusPill.className = 'status-pill status-unstable';
                statusPill.textContent = 'UNSTABLE (RHP OSCILLATION)';
                playChime(220, 'sawtooth', 0.12);
            }
        });

        function resetPoles() {
            gainSlider.value = 2.4;
            gainK = 2.4;
            gainVal.textContent = '2.4';
            isStable = true;
            statusPill.className = 'status-pill status-stable';
            statusPill.textContent = 'STABLE (LHP)';
            playChime(660, 'sine', 0.2);
        }

        function drawSPlane() {
            const w = splaneCanvas.width;
            const h = splaneCanvas.height;
            sCtx.clearRect(0, 0, w, h);

            const cx = w * 0.65; // Imaginary axis
            const cy = h / 2;    // Real axis

            // Background LHP & RHP tint
            sCtx.fillStyle = 'rgba(16, 185, 129, 0.05)';
            sCtx.fillRect(0, 0, cx, h);
            sCtx.fillStyle = 'rgba(239, 68, 68, 0.08)';
            sCtx.fillRect(cx, 0, w - cx, h);

            // Axes
            sCtx.strokeStyle = 'rgba(255, 255, 255, 0.15)';
            sCtx.lineWidth = 1.2;
            sCtx.beginPath();
            sCtx.moveTo(0, cy);
            sCtx.lineTo(w, cy);
            sCtx.moveTo(cx, 0);
            sCtx.lineTo(cx, h);
            sCtx.stroke();

            // Imaginary Axis Red Alert Line
            sCtx.strokeStyle = '#f87171';
            sCtx.lineWidth = 1.8;
            sCtx.beginPath();
            sCtx.moveTo(cx, 0);
            sCtx.lineTo(cx, h);
            sCtx.stroke();

            // Axis Labels
            sCtx.fillStyle = '#8393a8';
            sCtx.font = '11px Inter';
            sCtx.fillText('j\u03c9 (Imaginary)', cx + 8, 20);
            sCtx.fillText('\u03c3 (Real)', w - 50, cy - 8);
            sCtx.fillText('Stable LHP', 20, 25);
            sCtx.fillText('Unstable RHP', cx + 20, 25);

            // Compute pole positions based on gain K
            const sigma = (gainK - 3.2) * 45; // When K=3.2, on jw axis
            const omega = 65 + Math.sin(Date.now() * 0.003) * 5;

            // Draw Complex Conjugate Poles (Crosses)
            const poles = [
                { x: cx + sigma, y: cy - omega },
                { x: cx + sigma, y: cy + omega }
            ];

            poles.forEach(p => {
                sCtx.strokeStyle = isStable ? '#38bdf8' : '#f87171';
                sCtx.lineWidth = 3;
                const size = 8;
                sCtx.beginPath();
                sCtx.moveTo(p.x - size, p.y - size);
                sCtx.lineTo(p.x + size, p.y + size);
                sCtx.moveTo(p.x + size, p.y - size);
                sCtx.lineTo(p.x - size, p.y + size);
                sCtx.stroke();

                // Glow ring
                sCtx.strokeStyle = isStable ? 'rgba(56, 189, 248, 0.3)' : 'rgba(239, 68, 68, 0.4)';
                sCtx.lineWidth = 1;
                sCtx.beginPath();
                sCtx.arc(p.x, p.y, 14, 0, Math.PI * 2);
                sCtx.stroke();
            });

            // Draw Oscilloscope Step Response
            drawScope();

            requestAnimationFrame(drawSPlane);
        }

        function drawScope() {
            const sw = scopeCanvas.width;
            const sh = scopeCanvas.height;
            scCtx.fillStyle = '#05080f';
            scCtx.fillRect(0, 0, sw, sh);

            // Grid lines
            scCtx.strokeStyle = 'rgba(56, 189, 248, 0.1)';
            scCtx.lineWidth = 1;
            for (let x = 0; x < sw; x += 30) {
                scCtx.beginPath();
                scCtx.moveTo(x, 0);
                scCtx.lineTo(x, sh);
                scCtx.stroke();
            }
            for (let y = 0; y < sh; y += 30) {
                scCtx.beginPath();
                scCtx.moveTo(0, y);
                scCtx.lineTo(sw, y);
                scCtx.stroke();
            }

            scopeTime += 0.04;
            scCtx.strokeStyle = isStable ? '#34d399' : '#f87171';
            scCtx.lineWidth = 2;
            scCtx.beginPath();

            const decay = isStable ? 0.03 : -0.015;
            for (let x = 0; x < sw; x++) {
                const t = (x * 0.04) + scopeTime;
                let amp = Math.sin(t * 3.5);
                if (isStable) {
                    amp = amp * Math.exp(-decay * (x % 140));
                } else {
                    amp = amp * Math.exp(-decay * (x % 140)) * 1.5;
                }
                const y = (sh / 2) - amp * 28;
                if (x === 0) scCtx.moveTo(x, y);
                else scCtx.lineTo(x, y);
            }
            scCtx.stroke();
        }
        requestAnimationFrame(drawSPlane);

        // =========================================================================
        // 4-QUADRANT EV RACER (DRIVES)
        // =========================================================================
        const evCanvas = document.getElementById('ev-canvas');
        const evCtx = evCanvas.getContext('2d');
        const dutySlider = document.getElementById('duty-slider');
        const dutyVal = document.getElementById('duty-val');
        const batteryGauge = document.getElementById('battery-gauge');

        let carX = 100;
        let carSpeed = 2.0;
        let isReversed = false;
        let isBraking = false;
        let batteryPct = 78;

        function resizeEV() {
            evCanvas.width = evCanvas.parentElement.clientWidth;
            evCanvas.height = 320;
        }
        window.addEventListener('resize', resizeEV);
        resizeEV();

        dutySlider.addEventListener('input', e => {
            const a = parseFloat(e.target.value);
            dutyVal.textContent = a.toFixed(2);
        });

        function toggleDriveDir() {
            isReversed = !isReversed;
            document.getElementById('btn-reverse').textContent = isReversed ? '◀️ Reverse Gear' : '▶️ Forward Gear';
            playChime(440, 'triangle', 0.15);
        }

        function applyRegenBrake(active) {
            isBraking = active;
            if (active) playChime(320, 'sine', 0.2);
        }

        function drawEV() {
            const w = evCanvas.width;
            const h = evCanvas.height;
            evCtx.clearRect(0, 0, w, h);

            // Ground & Hill profile
            evCtx.strokeStyle = '#29334a';
            evCtx.lineWidth = 3;
            evCtx.beginPath();
            evCtx.moveTo(0, h - 80);
            evCtx.quadraticCurveTo(w * 0.4, h - 160, w, h - 90);
            evCtx.stroke();

            // Calculate active quadrant
            let activeQ = 1;
            const duty = parseFloat(dutySlider.value);
            if (!isReversed && !isBraking) {
                activeQ = 1; // Q1: Forward Motoring
                carSpeed = duty * 4.5;
                batteryPct = Math.max(batteryPct - 0.005, 5);
            } else if (!isReversed && isBraking) {
                activeQ = 2; // Q2: Forward Braking (Regen)
                carSpeed = Math.max(carSpeed - 0.08, 0.4);
                batteryPct = Math.min(batteryPct + 0.015, 100);
            } else if (isReversed && !isBraking) {
                activeQ = 3; // Q3: Reverse Motoring
                carSpeed = -duty * 3.5;
                batteryPct = Math.max(batteryPct - 0.005, 5);
            } else if (isReversed && isBraking) {
                activeQ = 4; // Q4: Reverse Braking (Regen)
                carSpeed = Math.min(carSpeed + 0.08, -0.4);
                batteryPct = Math.min(batteryPct + 0.015, 100);
            }

            // Update Battery HUD
            const regenTag = isBraking ? ' (⚡ Regen Charging)' : ' (⚡ Motor Consuming)';
            batteryGauge.textContent = `Battery: ${batteryPct.toFixed(1)}%${regenTag}`;

            // Update Quadrant Highlight Box
            ['q1', 'q2', 'q3', 'q4'].forEach((q, idx) => {
                const el = document.getElementById(`${q}-box`);
                if (idx + 1 === activeQ) el.classList.add('active');
                else el.classList.remove('active');
            });

            // Move Car
            carX += carSpeed;
            if (carX > w + 40) carX = -40;
            if (carX < -40) carX = w + 40;

            // Compute Y position on hill
            const normX = Math.max(0, Math.min(carX / w, 1));
            const carY = (h - 80) - Math.sin(normX * Math.PI) * 55;

            // Draw Stylized Cyber EV Car
            evCtx.save();
            evCtx.translate(carX, carY);
            if (isReversed) evCtx.scale(-1, 1);

            // Car Body
            evCtx.fillStyle = isBraking ? '#f87171' : '#f59e0b';
            evCtx.beginPath();
            evCtx.roundRect(-30, -22, 60, 16, 6);
            evCtx.fill();

            // Windshield
            evCtx.fillStyle = '#0f172a';
            evCtx.beginPath();
            evCtx.roundRect(-10, -32, 28, 12, 4);
            evCtx.fill();

            // Wheels
            evCtx.fillStyle = '#334155';
            evCtx.beginPath();
            evCtx.arc(-18, -4, 7, 0, Math.PI * 2);
            evCtx.arc(18, -4, 7, 0, Math.PI * 2);
            evCtx.fill();

            // Headlight beam
            evCtx.fillStyle = isBraking ? 'rgba(239, 68, 68, 0.3)' : 'rgba(245, 158, 11, 0.3)';
            evCtx.beginPath();
            evCtx.moveTo(30, -18);
            evCtx.lineTo(65, -28);
            evCtx.lineTo(65, -8);
            evCtx.closePath();
            evCtx.fill();

            evCtx.restore();

            requestAnimationFrame(drawEV);
        }
        requestAnimationFrame(drawEV);

        // =========================================================================
        // EXPANDED FORMULA LIGHTNING RUSH (SEPARATED BY 3 SUBJECTS + ALL)
        // =========================================================================
        const ALL_RUSH_FORMULAS = [
            // ---------------------------------------------------------------------
            // ACS FORMULAS (13)
            // ---------------------------------------------------------------------
            {
                subject: 'acs',
                subjectName: '⚡ ACS • Control Theory',
                color: '#38bdf8',
                eq: "e^{At} = \\mathcal{L}^{-1}\\{(sI - A)^{-1}\\}",
                options: [
                    { text: "State Transition Matrix (STM) Resolvent Computation", correct: true },
                    { text: "Kalman Controllability Test Matrix", correct: false },
                    { text: "PWM Inverter Duty Modulation Ratio", correct: false },
                    { text: "GSM Normal Burst Duration Formula", correct: false }
                ]
            },
            {
                subject: 'acs',
                subjectName: '⚡ ACS • Control Theory',
                color: '#38bdf8',
                eq: "G(s) = C(sI - A)^{-1}B + D",
                options: [
                    { text: "Transfer Function Formulation from State-Space Model", correct: true },
                    { text: "Liapunov Direct Asymptotic Energy Function", correct: false },
                    { text: "Stator Air-Gap Flux Constant Ratio", correct: false },
                    { text: "Diffie-Hellman Discrete Logarithm Formula", correct: false }
                ]
            },
            {
                subject: 'acs',
                subjectName: '⚡ ACS • Control Theory',
                color: '#38bdf8',
                eq: "Q_c = \\begin{bmatrix} B & AB & A^2B & \\dots & A^{n-1}B \\end{bmatrix}",
                options: [
                    { text: "Kalman Controllability Test Matrix (Rank must equal n)", correct: true },
                    { text: "Ackermann's State Observer Gain Vector", correct: false },
                    { text: "Clarke Transformation Stationary Stator Current", correct: false },
                    { text: "RSA Modular Exponentiation Cipher Formula", correct: false }
                ]
            },
            {
                subject: 'acs',
                subjectName: '⚡ ACS • Control Theory',
                color: '#38bdf8',
                eq: "Q_o = \\begin{bmatrix} C \\\\ CA \\\\ CA^2 \\\\ \\vdots \\\\ CA^{n-1} \\end{bmatrix}",
                options: [
                    { text: "Kalman Observability Test Matrix (Rank must equal n)", correct: true },
                    { text: "Jordan Canonical Block Matrix with Superdiagonal 1s", correct: false },
                    { text: "Steady-State Motor Load Torque Slope Stability", correct: false },
                    { text: "GSM TDMA Frame Timing Calculation", correct: false }
                ]
            },
            {
                subject: 'acs',
                subjectName: '⚡ ACS • Control Theory',
                color: '#38bdf8',
                eq: "K = \\begin{bmatrix} 0 & \\dots & 0 & 1 \\end{bmatrix} Q_c^{-1} \\phi_d(A)",
                options: [
                    { text: "Ackermann's Formula for State Feedback Pole Placement", correct: true },
                    { text: "Krasovskii Jacobian Energy Dissipation Matrix", correct: false },
                    { text: "Chopper Four-Quadrant Class E H-Bridge Switch", correct: false },
                    { text: "Wi-Fi 802.11 SIFS Inter-Frame Priority Gap", correct: false }
                ]
            },
            {
                subject: 'acs',
                subjectName: '⚡ ACS • Control Theory',
                color: '#38bdf8',
                eq: "\\dot{\\mathbf{e}} = (A - LC)\\mathbf{e}",
                options: [
                    { text: "Full-Order Luenberger State Observer Error Dynamics", correct: true },
                    { text: "Isocline Trajectory Slope Method Differential", correct: false },
                    { text: "Static Scherbius Cycloconverter Slip Power Flow", correct: false },
                    { text: "Co-Channel Carrier-to-Interference Ratio Bound", correct: false }
                ]
            },
            {
                subject: 'acs',
                subjectName: '⚡ ACS • Control Theory',
                color: '#38bdf8',
                eq: "N(X) = \\frac{4M}{\\pi X} \\angle 0^\\circ",
                options: [
                    { text: "Describing Function of Ideal Two-Position (On-Off) Relay", correct: true },
                    { text: "Describing Function of Saturation with Dead-Zone", correct: false },
                    { text: "Single-Phase Converter DC Output Voltage", correct: false },
                    { text: "GSM A3 Authentication Challenge Algorithm", correct: false }
                ]
            },
            {
                subject: 'acs',
                subjectName: '⚡ ACS • Control Theory',
                color: '#38bdf8',
                eq: "G(j\\omega) = -\\frac{1}{N(X)}",
                options: [
                    { text: "Limit Cycle Stability Criterion via Nyquist DF Locus", correct: true },
                    { text: "Gilbert's Diagonal Controllability Rank Test", correct: false },
                    { text: "Dual Converter Circulating Current Firing Angle", correct: false },
                    { text: "Cellular Cluster Size Integer Tessellation Rule", correct: false }
                ]
            },
            {
                subject: 'acs',
                subjectName: '⚡ ACS • Control Theory',
                color: '#38bdf8',
                eq: "V(\\mathbf{x}) > 0, \\quad \\dot{V}(\\mathbf{x}) = \\nabla V \\cdot \\mathbf{f}(\\mathbf{x}) \\le 0",
                options: [
                    { text: "Liapunov Direct Method for Energy-Based Stability", correct: true },
                    { text: "Ackermann's Desired Characteristic Polynomial", correct: false },
                    { text: "Vector Control Rotor Flux Dynamic Orientation", correct: false },
                    { text: "Diffie-Hellman Discrete Exponentiation Module", correct: false }
                ]
            },
            {
                subject: 'acs',
                subjectName: '⚡ ACS • Control Theory',
                color: '#38bdf8',
                eq: "V = \\mathbf{f}^T \\mathbf{f}, \\quad \\dot{V} = \\mathbf{f}^T (J + J^T) \\mathbf{f}",
                options: [
                    { text: "Krasovskii Method for Liapunov Function Construction", correct: true },
                    { text: "Cayley-Hamilton Matrix Series Expansion for STM", correct: false },
                    { text: "Three-Phase Converter Line-Commutated Inversion", correct: false },
                    { text: "GSM Normal Burst Guard Period Duration", correct: false }
                ]
            },
            {
                subject: 'acs',
                subjectName: '⚡ ACS • Control Theory',
                color: '#38bdf8',
                eq: "\\frac{dx_2}{dx_1} = m = \\text{constant} \\implies f(x_1, x_2) = m",
                options: [
                    { text: "Isocline Method for Phase Trajectory Construction", correct: true },
                    { text: "Saddle Point Eigenvalue Asymptotic Separation", correct: false },
                    { text: "Scalar V/f Maximum Breakdown Torque Equation", correct: false },
                    { text: "Handover Hysteresis Margin Margin Threshold", correct: false }
                ]
            },
            {
                subject: 'acs',
                subjectName: '⚡ ACS • Control Theory',
                color: '#38bdf8',
                eq: "\\Lambda = M^{-1} A M = \\text{diag}(\\lambda_1, \\lambda_2, \\dots, \\lambda_n)",
                options: [
                    { text: "Modal Decoupling Matrix Diagonalization Transformation", correct: true },
                    { text: "Jordan Canonical Block Matrix with Deficiency", correct: false },
                    { text: "CSI DC-Link Inductor Regenerative Braking State", correct: false },
                    { text: "IEEE 802.11 Exponential Random Backoff Slot", correct: false }
                ]
            },
            {
                subject: 'acs',
                subjectName: '⚡ ACS • Control Theory',
                color: '#38bdf8',
                eq: "\\begin{bmatrix} \\dot{x}_1 \\\\ \\dot{x}_2 \\\\ \\vdots \\\\ \\dot{x}_n \\end{bmatrix} = \\begin{bmatrix} 0 & 1 & \\dots & 0 \\\\ \\vdots & \\vdots & \\ddots & 1 \\\\ -a_0 & -a_1 & \\dots & -a_{n-1} \\end{bmatrix}\\mathbf{x}",
                options: [
                    { text: "Phase Variable State-Space Model in Companion Canonical Form", correct: true },
                    { text: "Full Observer Feedback Error Estimator Matrix", correct: false },
                    { text: "Static Kramer Rotor Power Recovery Rectifier", correct: false },
                    { text: "GSM Superframe Multiframe Timing Hierarchy", correct: false }
                ]
            },

            // ---------------------------------------------------------------------
            // ELECTRIC DRIVES FORMULAS (13)
            // ---------------------------------------------------------------------
            {
                subject: 'drive',
                subjectName: '🏎️ Drives • Power Electronics',
                color: '#f59e0b',
                eq: "T_e - T_L = J\\frac{d\\omega_m}{dt} + B\\omega_m",
                options: [
                    { text: "Fundamental Motor-Load Dynamic Torque Balance Equation", correct: true },
                    { text: "Steady-State Induction Motor Synchronous Speed", correct: false },
                    { text: "Kalman State Space Controllability Condition", correct: false },
                    { text: "Cellular Co-Channel Frequency Reuse Separation", correct: false }
                ]
            },
            {
                subject: 'drive',
                subjectName: '🏎️ Drives • Power Electronics',
                color: '#f59e0b',
                eq: "\\frac{dT_L}{d\\omega_m} - \\frac{dT_e}{d\\omega_m} > 0",
                options: [
                    { text: "Steady-State Stability Criterion of Drive Operating Point", correct: true },
                    { text: "Regenerative Braking Counter-EMF Threshold", correct: false },
                    { text: "Ackermann's Pole Placement Desired Polynomial", correct: false },
                    { text: "Diffie-Hellman Shared Secret Modulo Power", correct: false }
                ]
            },
            {
                subject: 'drive',
                subjectName: '🏎️ Drives • Power Electronics',
                color: '#f59e0b',
                eq: "P = T_e \\cdot \\omega_m \\implies \\text{Q1, Q3 } (P>0), \\quad \\text{Q2, Q4 } (P<0)",
                options: [
                    { text: "Four-Quadrant Operation Power Flow (Motoring vs Braking)", correct: true },
                    { text: "Dual Converter Circulating Current Zero Ripple", correct: false },
                    { text: "Liapunov Energy Function Derivative Decay", correct: false },
                    { text: "GSM Time Slot Bit Duration Division", correct: false }
                ]
            },
            {
                subject: 'drive',
                subjectName: '🏎️ Drives • Power Electronics',
                color: '#f59e0b',
                eq: "V_0 = \\frac{2V_m}{\\pi}\\cos\\alpha",
                options: [
                    { text: "1-Phase Fully Controlled Converter Fed DC Motor Terminal Voltage", correct: true },
                    { text: "3-Phase Converter AC Supply Displacement Factor", correct: false },
                    { text: "Describing Function of Saturated Plant Element", correct: false },
                    { text: "RSA Public Encryption Exponent Product", correct: false }
                ]
            },
            {
                subject: 'drive',
                subjectName: '🏎️ Drives • Power Electronics',
                color: '#f59e0b',
                eq: "V_0 = \\frac{3\\sqrt{2}V_L}{\\pi}\\cos\\alpha = \\frac{3V_{ml}}{\\pi}\\cos\\alpha",
                options: [
                    { text: "3-Phase Fully Controlled Converter Fed DC Motor Average Voltage", correct: true },
                    { text: "Induction Motor Rotor Stator Resistance Ratio", correct: false },
                    { text: "Kalman Observability Output Matrix Product", correct: false },
                    { text: "Cellular Handover RSSI Received Signal Floor", correct: false }
                ]
            },
            {
                subject: 'drive',
                subjectName: '🏎️ Drives • Power Electronics',
                color: '#f59e0b',
                eq: "\\alpha_1 + \\alpha_2 = 180^\\circ \\implies V_{01} = -V_{02}",
                options: [
                    { text: "Dual Converter Firing Angle Constraint for 4-Quadrant DC Drives", correct: true },
                    { text: "Chopper Duty Ratio Upper Conduction Limit", correct: false },
                    { text: "Phase Portrait Saddle Point Angle Condition", correct: false },
                    { text: "GSM Normal Burst Training Sequence Correlation", correct: false }
                ]
            },
            {
                subject: 'drive',
                subjectName: '🏎️ Drives • Power Electronics',
                color: '#f59e0b',
                eq: "V_0 = \\alpha V_{dc} \\quad (\\alpha = T_{on}/T)",
                options: [
                    { text: "Class A Chopper Output Terminal Voltage (Step-Down Buck)", correct: true },
                    { text: "Inverter DC-Link Resonant Frequency Tank", correct: false },
                    { text: "State Transition Resolvent Inverse Matrix", correct: false },
                    { text: "Wi-Fi RTS/CTS NAV Timer Reservation Length", correct: false }
                ]
            },
            {
                subject: 'drive',
                subjectName: '🏎️ Drives • Power Electronics',
                color: '#f59e0b',
                eq: "T_e \\propto V_s^2, \\quad T_{max} \\propto V_s^2 \\quad (s_m = \\text{constant})",
                options: [
                    { text: "Induction Motor Stator Voltage Control Torque-Speed Characteristic", correct: true },
                    { text: "Scalar Constant Frequency Overflux Saturation", correct: false },
                    { text: "Ideal Relay Fundamental Harmonic Gain", correct: false },
                    { text: "Mobile IP Care-of Address Foreign Agent Tunnel", correct: false }
                ]
            },
            {
                subject: 'drive',
                subjectName: '🏎️ Drives • Power Electronics',
                color: '#f59e0b',
                eq: "\\frac{V_s}{f} = \\text{constant} \\implies \\Phi_m \\approx \\frac{V_s}{4.44 f N_s} = \\text{constant}",
                options: [
                    { text: "Scalar V/f Control: Maintaining Constant Air-Gap Magnetic Flux", correct: true },
                    { text: "Slip Energy Inverter Recovery Factor", correct: false },
                    { text: "Liapunov Asymptotic Stability Gradient Matrix", correct: false },
                    { text: "GSM Authentication SRES Cryptographic Triplet", correct: false }
                ]
            },
            {
                subject: 'drive',
                subjectName: '🏎️ Drives • Power Electronics',
                color: '#f59e0b',
                eq: "P_{slip} = s P_g \\implies \\text{Rotor Diode Bridge} \\to \\text{Inverter} \\to \\text{AC Mains}",
                options: [
                    { text: "Static Kramer Drive: Sub-Synchronous Slip Power Recovery", correct: true },
                    { text: "Static Scherbius Super-Synchronous Cycloconverter Drive", correct: false },
                    { text: "Ackermann Closed-Loop Eigenvalue Shift Formula", correct: false },
                    { text: "Cellular Cluster Geometry Distance Formula", correct: false }
                ]
            },
            {
                subject: 'drive',
                subjectName: '🏎️ Drives • Power Electronics',
                color: '#f59e0b',
                eq: "T_e = \\frac{3}{2} P \\frac{L_m^2}{L_r} i_{ds} i_{qs}",
                options: [
                    { text: "Field-Oriented Vector Control Decoupled Torque Equation", correct: true },
                    { text: "CSI Motor Armature Reactance Dynamic Current", correct: false },
                    { text: "Isocline Method Limit Cycle Envelope", correct: false },
                    { text: "Diffie-Hellman Modular Primitive Root Generator", correct: false }
                ]
            },
            {
                subject: 'drive',
                subjectName: '🏎️ Drives • Power Electronics',
                color: '#f59e0b',
                eq: "[a, b, c] \\xrightarrow{\\text{Clarke}} [\\alpha, \\beta, 0] \\xrightarrow{\\text{Park}} [d, q, 0]",
                options: [
                    { text: "Clarke & Park Transformations: Converting 3-Phase AC to 2-Phase DC", correct: true },
                    { text: "Static Scherbius Bidirectional Inverter Bridge", correct: false },
                    { text: "Full-Order Observer Error Decay Convergence", correct: false },
                    { text: "IEEE 802.11 CSMA/CA Backoff Timer Decrement", correct: false }
                ]
            },
            {
                subject: 'drive',
                subjectName: '🏎️ Drives • Power Electronics',
                color: '#f59e0b',
                eq: "E_b > V_t \\implies I_a = \\frac{V_t - E_b}{R_a} < 0",
                options: [
                    { text: "DC Motor Regenerative Braking Electrical Condition", correct: true },
                    { text: "Plugging Dynamic Reversal Voltage Threshold", correct: false },
                    { text: "Van der Pol Nonlinear Limit Cycle Damping Limit", correct: false },
                    { text: "GSM Hyperframe Superframe Bit Duration", correct: false }
                ]
            },

            // ---------------------------------------------------------------------
            // MOBILE COMPUTING FORMULAS (13)
            // ---------------------------------------------------------------------
            {
                subject: 'mobile',
                subjectName: '📡 Mobile • Wireless Networks',
                color: '#ec4899',
                eq: "D = R\\sqrt{3N}",
                options: [
                    { text: "Cellular Co-Channel Reuse Distance as a Function of Cluster Size N", correct: true },
                    { text: "Free Space Path Loss Friis Attenuation Formula", correct: false },
                    { text: "Clarke Transformation Stationary Current Angle", correct: false },
                    { text: "Kalman State Space Controllability Dimension", correct: false }
                ]
            },
            {
                subject: 'mobile',
                subjectName: '📡 Mobile • Wireless Networks',
                color: '#ec4899',
                eq: "N = i^2 + ij + j^2 \\quad (N \\in \\{3, 4, 7, 12, 19\\})",
                options: [
                    { text: "Hexagonal Cellular Network Geometry Valid Cluster Size Formula", correct: true },
                    { text: "TDMA Time Slot Modulation Phase Offset", correct: false },
                    { text: "PWM Inverter Carrier Frequency Harmonic Ratio", correct: false },
                    { text: "Liapunov Positive Definite Energy Quadratic Form", correct: false }
                ]
            },
            {
                subject: 'mobile',
                subjectName: '📡 Mobile • Wireless Networks',
                color: '#ec4899',
                eq: "\\frac{S}{I} = \\frac{(\\sqrt{3N})^n}{i_0} \\ge 18\\text{ dB in GSM}",
                options: [
                    { text: "Worst-Case Co-Channel Carrier-to-Interference Ratio in Cellular Systems", correct: true },
                    { text: "Adjacent Channel Filter Bleed-Through Ratio", correct: false },
                    { text: "Induction Motor Air-Gap Flux Density Limit", correct: false },
                    { text: "Ackermann Matrix Eigenvalue Shift Constraint", correct: false }
                ]
            },
            {
                subject: 'mobile',
                subjectName: '📡 Mobile • Wireless Networks',
                color: '#ec4899',
                eq: "\\Delta = P_{ho} - P_{min} \\quad (\\text{Hysteresis Margin})",
                options: [
                    { text: "Cellular Handover Hysteresis Margin for Ping-Pong Avoidance", correct: true },
                    { text: "Cell Splitting Microcell Transmit Power Floor", correct: false },
                    { text: "Chopper DC Drive Duty Ratio Minimum Threshold", correct: false },
                    { text: "Relay Dead Zone Hysteresis Output Magnitude", correct: false }
                ]
            },
            {
                subject: 'mobile',
                subjectName: '📡 Mobile • Wireless Networks',
                color: '#ec4899',
                eq: "1\\text{ Time Slot} = 0.577\\text{ ms} = 156.25\\text{ bit periods}",
                options: [
                    { text: "GSM TDMA Basic Air Interface Time Slot Physical Duration", correct: true },
                    { text: "GPRS Packet Data Protocol Frame Duration", correct: false },
                    { text: "Scalar V/f Minimum Switching Inverter Period", correct: false },
                    { text: "State Transition Matrix Fundamental Oscillation Period", correct: false }
                ]
            },
            {
                subject: 'mobile',
                subjectName: '📡 Mobile • Wireless Networks',
                color: '#ec4899',
                eq: "1\\text{ TDMA Frame} = 8\\text{ Time Slots} = 4.615\\text{ ms}",
                options: [
                    { text: "GSM TDMA Full Air Interface Frame Timing Duration", correct: true },
                    { text: "GSM Superframe Traffic Multiframe Cycle", correct: false },
                    { text: "Three-Phase Converter 6-Pulse Ripple Duration", correct: false },
                    { text: "Observer Error Dynamics Convergence Window", correct: false }
                ]
            },
            {
                subject: 'mobile',
                subjectName: '📡 Mobile • Wireless Networks',
                color: '#ec4899',
                eq: "3\\text{T} + 57\\text{D} + 1\\text{S} + 26\\text{Tr} + 1\\text{S} + 57\\text{D} + 3\\text{T} + 8.25\\text{G} = 156.25\\text{ bits}",
                options: [
                    { text: "GSM Normal Burst Complete Bit Structure & Allocation", correct: true },
                    { text: "GSM Frequency Correction Burst Sine Wave Bit Allocation", correct: false },
                    { text: "Vector Control Coordinate Transformation Stator Matrix", correct: false },
                    { text: "Krasovskii Symmetric Jacobian Determinant Formula", correct: false }
                ]
            },
            {
                subject: 'mobile',
                subjectName: '📡 Mobile • Wireless Networks',
                color: '#ec4899',
                eq: "\\text{RTS} \\to \\text{SIFS} \\to \\text{CTS} \\to \\text{SIFS} \\to \\text{DATA} \\to \\text{SIFS} \\to \\text{ACK}",
                options: [
                    { text: "IEEE 802.11 CSMA/CA Virtual Carrier Sensing MAC Handshake", correct: true },
                    { text: "GSM Call Setup Signaling Sequence over PSTN", correct: false },
                    { text: "Dual Converter 4-Quadrant Thyristor Firing Pipeline", correct: false },
                    { text: "Liapunov Asymptotic Stability Vector Gradient Order", correct: false }
                ]
            },
            {
                subject: 'mobile',
                subjectName: '📡 Mobile • Wireless Networks',
                color: '#ec4899',
                eq: "K = B^a \\equiv A^b \\equiv g^{ab} \\pmod p",
                options: [
                    { text: "Diffie-Hellman Key Exchange Shared Secret Computation", correct: true },
                    { text: "RSA Public Encryption Modular Exponentiation", correct: false },
                    { text: "GSM A5 Stream Cipher Pseudo-Random Output", correct: false },
                    { text: "Kalman State Space Observability Matrix Modulo", correct: false }
                ]
            },
            {
                subject: 'mobile',
                subjectName: '📡 Mobile • Wireless Networks',
                color: '#ec4899',
                eq: "n = p \\cdot q, \\quad e \\cdot d \\equiv 1 \\pmod{\\phi(n)}, \\quad \\phi(n) = (p-1)(q-1)",
                options: [
                    { text: "RSA Asymmetric Cryptography Key Pair Generation Formula", correct: true },
                    { text: "Diffie-Hellman Prime Root Modular Exponentiation", correct: false },
                    { text: "Chopper Continuous Conduction Angle Boundary", correct: false },
                    { text: "Phase Plane Singular Point Saddle Eigenvalues", correct: false }
                ]
            },
            {
                subject: 'mobile',
                subjectName: '📡 Mobile • Wireless Networks',
                color: '#ec4899',
                eq: "c = m^e \\pmod n, \\quad m = c^d \\pmod n",
                options: [
                    { text: "RSA Public Encryption (c) and Private Decryption (m) Formulas", correct: true },
                    { text: "GSM A3 Authentication Challenge Response SRES", correct: false },
                    { text: "Clarke Transformation Stationary Alpha-Beta Conversion", correct: false },
                    { text: "Ackermann Observer Desired Polynomial Expression", correct: false }
                ]
            },
            {
                subject: 'mobile',
                subjectName: '📡 Mobile • Wireless Networks',
                color: '#ec4899',
                eq: "\\text{AUC} \\xrightarrow{\\text{Ki}} \\text{RAND} \\xrightarrow{\\text{A3}} \\text{SRES}, \\quad \\text{RAND} \\xrightarrow{\\text{A8}} K_c",
                options: [
                    { text: "GSM Subscriber Authentication & Cipher Key Generation Triplet", correct: true },
                    { text: "Mobile IP Home Agent Registration Tunneling Protocol", correct: false },
                    { text: "Static Kramer Rotor Slip Power Inversion Balance", correct: false },
                    { text: "Describing Function of Ideal Two-Position Relay", correct: false }
                ]
            },
            {
                subject: 'mobile',
                subjectName: '📡 Mobile • Wireless Networks',
                color: '#ec4899',
                eq: "\\text{NAV (Network Allocation Vector)} \\implies \\text{Virtual Carrier Sensing}",
                options: [
                    { text: "Virtual Medium Reservation Timer preventing Hidden Terminal Collisions", correct: true },
                    { text: "Physical Carrier Sensing Energy Detection Threshold", correct: false },
                    { text: "Inverter Dead-Time Interlock Protection Window", correct: false },
                    { text: "Cayley-Hamilton Characteristic Polynomial Remainder", correct: false }
                ]
            }
        ];

        let currentSubjectFilter = 'all';
        let filteredRushPool = [...ALL_RUSH_FORMULAS];
        let currentRushIdx = 0;
        let rushScore = 0;
        let rushStreak = 0;
        let rushTotalAnswers = 0;
        let rushCorrectAnswers = 0;
        let rushTimerTimeout = null;

        const STORAGE_KEY_HIGHSCORE = 'ktu_rush_highscore_';

        function initRushSubjectTabs() {
            const tabs = document.querySelectorAll('.rush-tab');
            tabs.forEach(tab => {
                tab.addEventListener('click', () => {
                    tabs.forEach(t => t.classList.remove('active'));
                    tab.classList.add('active');
                    const sub = tab.getAttribute('data-subject');
                    setRushSubject(sub);
                    playChime(580, 'sine', 0.15);
                });
            });
        }

        function setRushSubject(sub) {
            currentSubjectFilter = sub;
            if (sub === 'all') {
                filteredRushPool = [...ALL_RUSH_FORMULAS];
            } else {
                filteredRushPool = ALL_RUSH_FORMULAS.filter(q => q.subject === sub);
            }
            // Shuffle pool
            filteredRushPool.sort(() => Math.random() - 0.5);
            currentRushIdx = 0;
            updateRushHUD();
            loadRushQuestion();
        }

        function loadRushQuestion() {
            if (filteredRushPool.length === 0) return;
            const q = filteredRushPool[currentRushIdx];

            // Update Subject Pill on card
            const pill = document.getElementById('rush-subject-pill');
            pill.textContent = q.subjectName;
            pill.style.color = q.color;
            pill.style.borderColor = q.color;
            pill.style.background = `${q.color}22`;

            // Update Index Pill
            document.getElementById('rush-index-pill').textContent = `Formula ${currentRushIdx + 1} of ${filteredRushPool.length}`;

            // Display Formula
            const display = document.getElementById('rush-eq-display');
            display.style.borderColor = q.color;
            display.textContent = `$$${q.eq}$$`;
            if (window.renderMathInElement) {
                window.renderMathInElement(display, {
                    delimiters: [{left: '$$', right: '$$', display: true}],
                    throwOnError: false
                });
            }

            // Render Options
            const optGrid = document.getElementById('rush-options');
            optGrid.innerHTML = '';
            const shuffled = [...q.options].sort(() => Math.random() - 0.5);
            shuffled.forEach(opt => {
                const btn = document.createElement('button');
                btn.className = 'rush-btn';
                btn.innerHTML = `<span style="color:${q.color}; font-size:1.1rem; line-height:1;">⚡</span> <span>${opt.text}</span>`;
                btn.onclick = () => answerRush(opt.correct, btn);
                optGrid.appendChild(btn);
            });

            // Start Timer Bar (10 seconds)
            const bar = document.getElementById('rush-timer');
            bar.style.transition = 'none';
            bar.style.width = '100%';
            setTimeout(() => {
                bar.style.transition = 'width 10s linear';
                bar.style.width = '0%';
            }, 50);

            clearTimeout(rushTimerTimeout);
            rushTimerTimeout = setTimeout(() => {
                // Time Up
                rushStreak = 0;
                rushTotalAnswers++;
                playChime(190, 'sawtooth', 0.25);
                updateRushHUD();
                nextRush();
            }, 10000);
        }

        function answerRush(isCorrect, btn) {
            clearTimeout(rushTimerTimeout);
            rushTotalAnswers++;
            if (isCorrect) {
                btn.classList.add('correct');
                rushStreak++;
                rushCorrectAnswers++;
                rushScore += 100 * rushStreak;
                playChime(880, 'sine', 0.18);
                // Save high score
                const curBest = parseInt(localStorage.getItem(STORAGE_KEY_HIGHSCORE + currentSubjectFilter) || '0', 10);
                if (rushScore > curBest) {
                    localStorage.setItem(STORAGE_KEY_HIGHSCORE + currentSubjectFilter, rushScore);
                }
            } else {
                btn.classList.add('wrong');
                rushStreak = 0;
                playChime(180, 'sawtooth', 0.25);
            }
            updateRushHUD();
            setTimeout(nextRush, 850);
        }

        function skipRush() {
            clearTimeout(rushTimerTimeout);
            playChime(360, 'sine', 0.12);
            nextRush();
        }

        function updateRushHUD() {
            document.getElementById('rush-score').textContent = `Score: ${rushScore} | Streak: ${rushStreak}x 🔥`;
            document.getElementById('total-xp').textContent = `${(3450 + rushScore).toLocaleString()} XP`;

            const accuracy = rushTotalAnswers > 0 ? Math.round((rushCorrectAnswers / rushTotalAnswers) * 100) : 100;
            const highscore = localStorage.getItem(STORAGE_KEY_HIGHSCORE + currentSubjectFilter) || '0';
            document.getElementById('rush-accuracy-text').textContent = `Accuracy: ${accuracy}% | High Score: ${highscore}`;
        }

        function nextRush() {
            currentRushIdx = (currentRushIdx + 1) % filteredRushPool.length;
            loadRushQuestion();
        }

        // Initialize tabs and load first question
        initRushSubjectTabs();
        setRushSubject('all');
    </script>
</body>
</html>
"""
    return html

if __name__ == '__main__':
    content = build_activities_html()
    with open('activities.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Generated activities.html successfully ({} bytes)".format(len(content)))
