# scratch/gen_mindmap.py
# Generates the interactive Neural Mind Map page (mindmap.html)
# Features glowing neurons, pulsing synaptic energy packets, KaTeX pop-out equations, and memory cards.

import json
from mindmap_data import MINDMAP_DATA

def build_mindmap_html():
    data_json = json.dumps(MINDMAP_DATA)
    
    html = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>Neural Mind Map | KTU Engineering Exam Prep</title>
    
    <!-- Instant Anti-FOUC Theme Preload -->
    <script>
        (function() {{
            const savedTheme = localStorage.getItem('ktu_portal_theme') || 'dark';
            document.documentElement.setAttribute('data-theme', savedTheme);
            const savedLang = localStorage.getItem('ktu_portal_lang') || 'en';
            document.documentElement.setAttribute('data-lang', savedLang);
        }})();
    </script>

    <!-- KaTeX CDN for Clean Mathematical Formula Rendering -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
        onload="renderMathInElement(document.body, {{
            delimiters: [
                {{left: '$$', right: '$$', display: true}},
                {{left: '$', right: '$', display: false}}
            ],
            throwOnError: false
        }});"></script>

    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&family=Noto+Sans+Malayalam:wght@400;500;600;700&display=swap" rel="stylesheet">

    <style>
        :root, [data-theme="dark"] {{
            --bg-base: #0a0d14;
            --bg-surface: #101522;
            --bg-card: rgba(22, 28, 44, 0.88);
            --border-subtle: #222d42;
            --border-glow: #38bdf8;
            --text-main: #f1f5f9;
            --text-body: #cbd5e1;
            --text-muted: #8493a8;
            --header-bg: rgba(13, 17, 27, 0.92);
            --acs-color: #38bdf8;
            --acs-glow: rgba(56, 189, 248, 0.5);
            --drive-color: #f59e0b;
            --drive-glow: rgba(245, 158, 11, 0.5);
            --mobile-color: #ec4899;
            --mobile-glow: rgba(236, 72, 153, 0.5);
            --card-shadow: 0 20px 40px rgba(0, 0, 0, 0.7);
        }}
        [data-theme="warm"] {{
            --bg-base: #110f0d;
            --bg-surface: #1a1714;
            --bg-card: rgba(32, 28, 24, 0.9);
            --border-subtle: #302924;
            --border-glow: #fbbf24;
            --text-main: #faf4ed;
            --text-body: #ded4c7;
            --text-muted: #a19586;
            --header-bg: rgba(21, 18, 16, 0.94);
            --acs-color: #38bdf8;
            --acs-glow: rgba(56, 189, 248, 0.4);
            --drive-color: #f59e0b;
            --drive-glow: rgba(245, 158, 11, 0.4);
            --mobile-color: #f472b6;
            --mobile-glow: rgba(244, 114, 182, 0.4);
            --card-shadow: 0 20px 40px rgba(0, 0, 0, 0.8);
        }}
        [data-theme="forest"] {{
            --bg-base: #0b1411;
            --bg-surface: #111d19;
            --bg-card: rgba(22, 36, 31, 0.9);
            --border-subtle: #213a31;
            --border-glow: #34d399;
            --text-main: #ecfdf5;
            --text-body: #c7e5d8;
            --text-muted: #7ca895;
            --header-bg: rgba(13, 23, 20, 0.94);
            --acs-color: #38bdf8;
            --acs-glow: rgba(56, 189, 248, 0.4);
            --drive-color: #fbbf24;
            --drive-glow: rgba(251, 191, 36, 0.4);
            --mobile-color: #34d399;
            --mobile-glow: rgba(52, 211, 153, 0.4);
            --card-shadow: 0 20px 40px rgba(0, 0, 0, 0.8);
        }}
        [data-theme="oled"] {{
            --bg-base: #000000;
            --bg-surface: #0a0a0a;
            --bg-card: rgba(16, 16, 16, 0.95);
            --border-subtle: #222222;
            --border-glow: #ffffff;
            --text-main: #ffffff;
            --text-body: #d1d5db;
            --text-muted: #888888;
            --header-bg: rgba(0, 0, 0, 0.96);
            --acs-color: #38bdf8;
            --acs-glow: rgba(56, 189, 248, 0.6);
            --drive-color: #f59e0b;
            --drive-glow: rgba(245, 158, 11, 0.6);
            --mobile-color: #ec4899;
            --mobile-glow: rgba(236, 72, 153, 0.6);
            --card-shadow: 0 20px 40px rgba(0, 0, 0, 0.95);
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: var(--bg-base);
            color: var(--text-body);
            overflow: hidden;
            width: 100vw;
            height: 100vh;
            user-select: none;
        }}

        /* Header Navigation */
        .map-header {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            height: 64px;
            background: var(--header-bg);
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
            border-bottom: 1px solid var(--border-subtle);
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 1.25rem;
            z-index: 100;
        }}

        .brand-group {{
            display: flex;
            align-items: center;
            gap: 0.75rem;
            text-decoration: none;
            color: inherit;
        }}
        .brand-icon {{
            font-size: 1.5rem;
            filter: drop-shadow(0 0 10px rgba(56, 189, 248, 0.6));
        }}
        .brand-title {{
            font-size: 1.05rem;
            font-weight: 800;
            letter-spacing: -0.02em;
            color: var(--text-main);
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}
        .brand-badge {{
            font-size: 0.68rem;
            font-weight: 700;
            padding: 0.15rem 0.45rem;
            border-radius: 999px;
            background: linear-gradient(135deg, #38bdf8, #818cf8);
            color: #030712;
            letter-spacing: 0.05em;
            text-transform: uppercase;
        }}

        /* Navigation Links */
        .nav-links-cluster {{
            display: flex;
            align-items: center;
            gap: 0.4rem;
        }}
        .nav-pill {{
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            padding: 0.4rem 0.75rem;
            border-radius: 8px;
            font-size: 0.82rem;
            font-weight: 600;
            color: var(--text-body);
            text-decoration: none;
            border: 1px solid transparent;
            transition: all 0.2s ease;
        }}
        .nav-pill:hover {{
            color: var(--text-main);
            background: rgba(255, 255, 255, 0.06);
            border-color: var(--border-subtle);
        }}
        .nav-pill.active {{
            background: rgba(56, 189, 248, 0.12);
            color: #38bdf8;
            border-color: rgba(56, 189, 248, 0.35);
            box-shadow: 0 0 12px rgba(56, 189, 248, 0.2);
        }}

        /* Subject Filter Bar in Canvas */
        .map-subject-bar {{
            position: absolute;
            top: 76px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            align-items: center;
            gap: 0.35rem;
            background: var(--header-bg);
            border: 1px solid var(--border-subtle);
            border-radius: 999px;
            padding: 0.3rem 0.45rem;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
            z-index: 50;
        }}
        .filter-tab {{
            display: flex;
            align-items: center;
            gap: 0.35rem;
            padding: 0.35rem 0.85rem;
            border-radius: 999px;
            background: transparent;
            border: none;
            color: var(--text-muted);
            font-size: 0.8rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
        }}
        .filter-tab:hover {{
            color: var(--text-main);
        }}
        .filter-tab.active {{
            color: #ffffff;
            box-shadow: 0 0 14px currentColor;
        }}
        .filter-tab[data-sub="all"].active {{ background: #4f46e5; color: #fff; }}
        .filter-tab[data-sub="acs"].active {{ background: #0284c7; color: #fff; }}
        .filter-tab[data-sub="drive"].active {{ background: #d97706; color: #fff; }}
        .filter-tab[data-sub="mobile"].active {{ background: #db2777; color: #fff; }}

        /* Canvas Viewport */
        #neural-canvas {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            cursor: grab;
            background: radial-gradient(circle at center, rgba(14, 21, 37, 0.5) 0%, var(--bg-base) 100%);
        }}
        #neural-canvas:active {{
            cursor: grabbing;
        }}

        /* Search HUD */
        .search-hud {{
            position: absolute;
            bottom: 24px;
            left: 24px;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            background: var(--header-bg);
            border: 1px solid var(--border-subtle);
            border-radius: 12px;
            padding: 0.45rem 0.85rem;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
            backdrop-filter: blur(12px);
            z-index: 50;
        }}
        .search-hud input {{
            background: transparent;
            border: none;
            outline: none;
            color: var(--text-main);
            font-size: 0.86rem;
            width: 220px;
        }}
        .search-hud input::placeholder {{
            color: var(--text-muted);
        }}
        .search-icon {{
            color: var(--text-muted);
            font-size: 0.95rem;
        }}

        /* Canvas Controls HUD */
        .controls-hud {{
            position: absolute;
            bottom: 24px;
            right: 24px;
            display: flex;
            align-items: center;
            gap: 0.4rem;
            background: var(--header-bg);
            border: 1px solid var(--border-subtle);
            border-radius: 12px;
            padding: 0.35rem 0.5rem;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
            backdrop-filter: blur(12px);
            z-index: 50;
        }}
        .hud-btn {{
            background: transparent;
            border: 1px solid transparent;
            color: var(--text-body);
            width: 34px;
            height: 34px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1rem;
            cursor: pointer;
            transition: all 0.2s ease;
        }}
        .hud-btn:hover {{
            background: rgba(255, 255, 255, 0.08);
            color: var(--text-main);
            border-color: var(--border-subtle);
        }}

        /* Floating Holographic Pop-out Card */
        #node-card {{
            position: absolute;
            width: 360px;
            max-width: calc(100vw - 32px);
            background: var(--bg-card);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid var(--border-glow);
            border-radius: 16px;
            padding: 1.25rem;
            box-shadow: var(--card-shadow), 0 0 35px var(--node-glow-color, rgba(56, 189, 248, 0.3));
            color: var(--text-body);
            z-index: 90;
            display: none;
            animation: cardPop 0.25s cubic-bezier(0.16, 1, 0.3, 1);
            pointer-events: auto;
        }}
        @keyframes cardPop {{
            from {{ opacity: 0; transform: scale(0.92) translateY(10px); }}
            to {{ opacity: 1; transform: scale(1) translateY(0); }}
        }}

        .card-close-btn {{
            position: absolute;
            top: 10px;
            right: 12px;
            background: transparent;
            border: none;
            color: var(--text-muted);
            font-size: 1.2rem;
            cursor: pointer;
            line-height: 1;
            padding: 4px;
        }}
        .card-close-btn:hover {{
            color: var(--text-main);
        }}

        .card-badge-row {{
            display: flex;
            align-items: center;
            gap: 0.45rem;
            margin-bottom: 0.5rem;
        }}
        .node-category-tag {{
            font-size: 0.7rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            padding: 0.15rem 0.5rem;
            border-radius: 4px;
            background: rgba(255, 255, 255, 0.08);
            color: var(--node-accent-color, #38bdf8);
        }}

        .card-node-title {{
            font-size: 1.05rem;
            font-weight: 700;
            color: var(--text-main);
            line-height: 1.3;
            margin-bottom: 0.65rem;
        }}

        .card-eq-box {{
            background: rgba(0, 0, 0, 0.45);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-left: 3px solid var(--node-accent-color, #38bdf8);
            border-radius: 8px;
            padding: 0.6rem 0.75rem;
            margin-bottom: 0.75rem;
            overflow-x: auto;
            text-align: center;
        }}

        .card-summary-text {{
            font-size: 0.83rem;
            line-height: 1.45;
            color: var(--text-body);
            margin-bottom: 0.75rem;
        }}

        .card-byheart-box {{
            background: rgba(245, 158, 11, 0.09);
            border: 1px solid rgba(245, 158, 11, 0.25);
            border-radius: 8px;
            padding: 0.55rem 0.7rem;
            margin-bottom: 0.85rem;
            font-size: 0.78rem;
            line-height: 1.4;
            color: #fde68a;
        }}
        .card-byheart-box strong {{
            color: #fbbf24;
            display: block;
            margin-bottom: 0.15rem;
            font-size: 0.8rem;
        }}

        .card-actions {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding-top: 0.6rem;
            border-top: 1px solid var(--border-subtle);
        }}
        .card-jump-link {{
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            font-size: 0.8rem;
            font-weight: 600;
            color: var(--node-accent-color, #38bdf8);
            text-decoration: none;
            padding: 0.35rem 0.7rem;
            border-radius: 6px;
            background: rgba(56, 189, 248, 0.1);
            transition: all 0.2s ease;
        }}
        .card-jump-link:hover {{
            background: var(--node-accent-color, #38bdf8);
            color: #030712;
            box-shadow: 0 0 15px var(--node-glow-color, rgba(56, 189, 248, 0.5));
        }}

        /* Legend overlay */
        .legend-overlay {{
            position: absolute;
            top: 76px;
            left: 24px;
            background: var(--header-bg);
            border: 1px solid var(--border-subtle);
            border-radius: 12px;
            padding: 0.6rem 0.85rem;
            font-size: 0.75rem;
            color: var(--text-muted);
            backdrop-filter: blur(12px);
            z-index: 50;
            display: flex;
            flex-direction: column;
            gap: 0.35rem;
        }}
        .legend-item {{
            display: flex;
            align-items: center;
            gap: 0.45rem;
        }}
        .legend-dot {{
            width: 10px;
            height: 10px;
            border-radius: 50%;
            box-shadow: 0 0 8px currentColor;
        }}

        /* Mobile Adjustments */
        @media (max-width: 768px) {{
            .map-header {{
                padding: 0 0.75rem;
                height: 56px;
            }}
            .brand-subtext, .brand-badge {{
                display: none;
            }}
            .map-subject-bar {{
                top: 64px;
                width: 95vw;
                justify-content: center;
                overflow-x: auto;
            }}
            .legend-overlay {{
                display: none;
            }}
            .search-hud {{
                left: 12px;
                bottom: 12px;
                padding: 0.35rem 0.6rem;
            }}
            .search-hud input {{
                width: 140px;
            }}
            .controls-hud {{
                right: 12px;
                bottom: 12px;
            }}
            #node-card {{
                left: 16px !important;
                right: 16px !important;
                top: auto !important;
                bottom: 64px !important;
                width: auto;
            }}
        }}
    </style>
</head>
<body>

    <!-- Header Navigation -->
    <header class="map-header">
        <a href="index.html" class="brand-group">
            <span class="brand-icon">🧠</span>
            <div class="brand-text">
                <span class="brand-title">KTU Neural Mind Map <span class="brand-badge">Interactive</span></span>
            </div>
        </a>

        <nav class="nav-links-cluster">
            <a href="index.html" class="nav-pill">📚 Question Bank</a>
            <a href="mindmap.html" class="nav-pill active">🧠 Mind Map</a>
            <a href="activities.html" class="nav-pill">🎯 Focus Lab</a>
            <a href="animations.html" class="nav-pill">🎬 60fps Simulators</a>
        </nav>
    </header>

    <!-- Canvas Filter Bar -->
    <div class="map-subject-bar" role="tablist">
        <button class="filter-tab active" data-sub="all">🌌 Universe (All 3 Subjects)</button>
        <button class="filter-tab" data-sub="acs">⚡ ACS (Control Theory)</button>
        <button class="filter-tab" data-sub="drive">🏎️ Electric Drives</button>
        <button class="filter-tab" data-sub="mobile">📡 Mobile Computing</button>
    </div>

    <!-- Legend Overlay -->
    <div class="legend-overlay">
        <div class="legend-item"><span class="legend-dot" style="color: #38bdf8; background: #38bdf8;"></span> ACS: State Space &amp; Nonlinear</div>
        <div class="legend-item"><span class="legend-dot" style="color: #f59e0b; background: #f59e0b;"></span> Drives: Power Motors &amp; Inverters</div>
        <div class="legend-item"><span class="legend-dot" style="color: #ec4899; background: #ec4899;"></span> Mobile: Cellular &amp; Cryptography</div>
        <div class="legend-item"><span class="legend-dot" style="color: #818cf8; background: #818cf8;"></span> Cross-Domain Synapses</div>
    </div>

    <!-- Search HUD -->
    <div class="search-hud">
        <span class="search-icon">🔍</span>
        <input type="text" id="node-search" placeholder="Search 94+ neurons &amp; formulas..." autocomplete="off">
    </div>

    <!-- Controls HUD -->
    <div class="controls-hud">
        <button class="hud-btn" id="btn-zoom-in" title="Zoom In">➕</button>
        <button class="hud-btn" id="btn-zoom-out" title="Zoom Out">➖</button>
        <button class="hud-btn" id="btn-reset-view" title="Reset Camera">🎯</button>
        <button class="hud-btn" id="btn-toggle-flow" title="Pause / Resume Synaptic Flow">⚡</button>
    </div>

    <!-- Main HTML5 Canvas -->
    <canvas id="neural-canvas"></canvas>

    <!-- Floating Holographic Pop-out Card -->
    <div id="node-card">
        <button class="card-close-btn" onclick="closeNodeCard()">✕</button>
        <div class="card-badge-row">
            <span class="node-category-tag" id="card-category">Category</span>
        </div>
        <h3 class="card-node-title" id="card-title">Node Title</h3>
        <div class="card-eq-box" id="card-eq">$$\\dot{{x}} = Ax + Bu$$</div>
        <p class="card-summary-text" id="card-summary">Explanation</p>
        <div class="card-byheart-box" id="card-byheart">
            <strong>⚡ Key Exam Shortcut / Ormavekkan:</strong>
            <span id="card-byheart-text">Memory note text</span>
        </div>
        <div class="card-actions">
            <span style="font-size:0.75rem; color:var(--text-muted);" id="card-connected-count">3 Synapses</span>
            <a href="#" target="_blank" class="card-jump-link" id="card-jump-link">Open Exam Question ↗</a>
        </div>
    </div>

    <!-- Neural Engine Script -->
    <script>
        const GRAPH_DATA = {data_json};

        const canvas = document.getElementById('neural-canvas');
        const ctx = canvas.getContext('2d');
        const card = document.getElementById('node-card');

        let width, height;
        let activeSubject = 'all';
        let synapticPulseActive = true;

        // Camera transform
        let camera = {{
            x: 0,
            y: 0,
            scale: 0.9,
            targetX: 0,
            targetY: 0,
            targetScale: 0.9,
            isDragging: false,
            startX: 0,
            startY: 0
        }};

        // Synaptic particles
        const particles = [];
        const MAX_PARTICLES = 60;

        // Resize Canvas to Device Pixel Ratio
        function resize() {{
            const dpr = window.devicePixelRatio || 1;
            width = window.innerWidth;
            height = window.innerHeight;
            canvas.width = width * dpr;
            canvas.height = height * dpr;
            ctx.scale(dpr, dpr);
            if (camera.x === 0 && camera.y === 0) {{
                camera.x = width / 2;
                camera.y = height / 2;
                camera.targetX = width / 2;
                camera.targetY = height / 2;
            }}
        }}
        window.addEventListener('resize', resize);
        resize();

        // Nodes lookup & physics setup
        const nodeMap = {{}};
        GRAPH_DATA.nodes.forEach(n => {{
            n.vx = 0;
            n.vy = 0;
            n.pulse = Math.random() * Math.PI * 2;
            nodeMap[n.id] = n;
        }});

        // Generate initial synaptic particles
        GRAPH_DATA.edges.forEach((edge, i) => {{
            if (i % 2 === 0) {{
                particles.push({{
                    from: edge.from,
                    to: edge.to,
                    progress: Math.random(),
                    speed: 0.003 + Math.random() * 0.005,
                    color: nodeMap[edge.from]?.color || '#38bdf8'
                }});
            }}
        }});

        // Mouse & Touch interaction
        let hoveredNode = null;
        let selectedNode = null;

        function getCanvasCoords(e) {{
            const rect = canvas.getBoundingClientRect();
            const clientX = e.clientX ?? (e.touches ? e.touches[0].clientX : 0);
            const clientY = e.clientY ?? (e.touches ? e.touches[0].clientY : 0);
            return {{
                x: (clientX - camera.x) / camera.scale,
                y: (clientY - camera.y) / camera.scale,
                screenX: clientX,
                screenY: clientY
            }};
        }}

        canvas.addEventListener('mousedown', e => {{
            camera.isDragging = true;
            camera.startX = e.clientX - camera.x;
            camera.startY = e.clientY - camera.y;
        }});

        window.addEventListener('mousemove', e => {{
            if (camera.isDragging) {{
                camera.x = e.clientX - camera.startX;
                camera.y = e.clientY - camera.startY;
                camera.targetX = camera.x;
                camera.targetY = camera.y;
                return;
            }}

            const pos = getCanvasCoords(e);
            let found = null;
            for (const n of GRAPH_DATA.nodes) {{
                if (activeSubject !== 'all' && n.subject !== activeSubject && n.subject !== 'master') continue;
                const dx = pos.x - n.x;
                const dy = pos.y - n.y;
                if (Math.sqrt(dx * dx + dy * dy) <= (n.radius + 6)) {{
                    found = n;
                    break;
                }}
            }}
            hoveredNode = found;
            canvas.style.cursor = found ? 'pointer' : (camera.isDragging ? 'grabbing' : 'grab');
        }});

        window.addEventListener('mouseup', () => {{
            camera.isDragging = false;
        }});

        canvas.addEventListener('click', e => {{
            const pos = getCanvasCoords(e);
            for (const n of GRAPH_DATA.nodes) {{
                if (activeSubject !== 'all' && n.subject !== activeSubject && n.subject !== 'master') continue;
                const dx = pos.x - n.x;
                const dy = pos.y - n.y;
                if (Math.sqrt(dx * dx + dy * dy) <= (n.radius + 6)) {{
                    selectNode(n, pos.screenX, pos.screenY);
                    return;
                }}
            }}
        }});

        // Zoom with wheel
        canvas.addEventListener('wheel', e => {{
            e.preventDefault();
            const zoomFactor = e.deltaY < 0 ? 1.12 : 0.89;
            const newScale = Math.min(Math.max(camera.scale * zoomFactor, 0.35), 2.8);
            
            // Zoom towards mouse
            camera.x = e.clientX - (e.clientX - camera.x) * (newScale / camera.scale);
            camera.y = e.clientY - (e.clientY - camera.y) * (newScale / camera.scale);
            camera.scale = newScale;
            camera.targetX = camera.x;
            camera.targetY = camera.y;
            camera.targetScale = camera.scale;
        }}, {{ passive: false }});

        // Touch gesture pan & pinch
        let initialPinchDist = null;
        canvas.addEventListener('touchstart', e => {{
            if (e.touches.length === 1) {{
                camera.isDragging = true;
                camera.startX = e.touches[0].clientX - camera.x;
                camera.startY = e.touches[0].clientY - camera.y;
            }} else if (e.touches.length === 2) {{
                camera.isDragging = false;
                const dx = e.touches[0].clientX - e.touches[1].clientX;
                const dy = e.touches[0].clientY - e.touches[1].clientY;
                initialPinchDist = Math.sqrt(dx * dx + dy * dy);
            }}
        }});

        canvas.addEventListener('touchmove', e => {{
            if (e.touches.length === 1 && camera.isDragging) {{
                camera.x = e.touches[0].clientX - camera.startX;
                camera.y = e.touches[0].clientY - camera.startY;
                camera.targetX = camera.x;
                camera.targetY = camera.y;
            }} else if (e.touches.length === 2 && initialPinchDist) {{
                const dx = e.touches[0].clientX - e.touches[1].clientX;
                const dy = e.touches[0].clientY - e.touches[1].clientY;
                const dist = Math.sqrt(dx * dx + dy * dy);
                const factor = dist / initialPinchDist;
                camera.scale = Math.min(Math.max(camera.scale * factor, 0.35), 2.8);
                camera.targetScale = camera.scale;
                initialPinchDist = dist;
            }}
        }});

        canvas.addEventListener('touchend', () => {{
            camera.isDragging = false;
            initialPinchDist = null;
        }});

        // Select Node & Show Card
        function selectNode(n, screenX, screenY) {{
            selectedNode = n;
            card.style.setProperty('--node-accent-color', n.color);
            card.style.setProperty('--node-glow-color', n.color);
            
            document.getElementById('card-category').textContent = n.category || 'Core Concept';
            document.getElementById('card-title').textContent = n.title;
            document.getElementById('card-summary').textContent = n.summary;
            document.getElementById('card-byheart-text').textContent = n.byheart;
            
            const eqBox = document.getElementById('card-eq');
            eqBox.textContent = `$$${{n.eq}}$$`;
            if (window.renderMathInElement) {{
                window.renderMathInElement(eqBox, {{
                    delimiters: [{{left: '$$', right: '$$', display: true}}],
                    throwOnError: false
                }});
            }}

            // Count connected synapses
            const connected = GRAPH_DATA.edges.filter(e => e.from === n.id || e.to === n.id);
            document.getElementById('card-connected-count').textContent = `⚡ ${{connected.length}} Active Synapses`;

            const jumpLink = document.getElementById('card-jump-link');
            jumpLink.href = n.card_url || 'index.html';

            // Positioning
            card.style.display = 'block';
            if (window.innerWidth > 768) {{
                let left = screenX + 24;
                let top = screenY - 80;
                if (left + 380 > window.innerWidth) left = screenX - 390;
                if (top + 340 > window.innerHeight) top = window.innerHeight - 360;
                if (top < 70) top = 80;
                card.style.left = `${{left}}px`;
                card.style.top = `${{top}}px`;
            }}

            // Center camera smoothly
            camera.targetX = width / 2 - n.x * camera.scale;
            camera.targetY = height / 2 - n.y * camera.scale;
        }}

        function closeNodeCard() {{
            card.style.display = 'none';
            selectedNode = null;
        }}

        // Search feature with auto-fly camera
        const searchInput = document.getElementById('node-search');
        searchInput.addEventListener('input', e => {{
            const val = e.target.value.toLowerCase().trim();
            if (!val) return;
            const match = GRAPH_DATA.nodes.find(n => 
                n.title.toLowerCase().includes(val) || 
                n.summary.toLowerCase().includes(val) || 
                (n.eq && n.eq.toLowerCase().includes(val))
            );
            if (match) {{
                camera.targetX = width / 2 - match.x * camera.scale;
                camera.targetY = height / 2 - match.y * camera.scale;
                selectedNode = match;
            }}
        }});

        // Filter tabs
        document.querySelectorAll('.filter-tab').forEach(tab => {{
            tab.addEventListener('click', () => {{
                document.querySelectorAll('.filter-tab').forEach(t => t.classList.remove('active'));
                tab.classList.add('active');
                activeSubject = tab.getAttribute('data-sub');
                
                // Fly to subject hub
                const hubId = activeSubject === 'all' ? 'master-core' : `${{activeSubject}}-hub`;
                const hub = nodeMap[hubId];
                if (hub) {{
                    camera.targetX = width / 2 - hub.x * camera.scale;
                    camera.targetY = height / 2 - hub.y * camera.scale;
                }}
            }});
        }});

        // HUD Buttons
        document.getElementById('btn-zoom-in').addEventListener('click', () => {{
            camera.targetScale = Math.min(camera.scale * 1.3, 2.8);
        }});
        document.getElementById('btn-zoom-out').addEventListener('click', () => {{
            camera.targetScale = Math.max(camera.scale * 0.75, 0.35);
        }});
        document.getElementById('btn-reset-view').addEventListener('click', () => {{
            camera.targetX = width / 2;
            camera.targetY = height / 2;
            camera.targetScale = 0.9;
        }});
        document.getElementById('btn-toggle-flow').addEventListener('click', () => {{
            synapticPulseActive = !synapticPulseActive;
        }});

        // Main Animation Loop
        function animate() {{
            // Smooth camera lerp
            camera.x += (camera.targetX - camera.x) * 0.1;
            camera.y += (camera.targetY - camera.y) * 0.1;
            camera.scale += (camera.targetScale - camera.scale) * 0.1;

            ctx.clearRect(0, 0, width, height);
            ctx.save();
            ctx.translate(camera.x, camera.y);
            ctx.scale(camera.scale, camera.scale);

            // Draw Edges / Synapses
            ctx.lineWidth = 1.4;
            GRAPH_DATA.edges.forEach(edge => {{
                const u = nodeMap[edge.from];
                const v = nodeMap[edge.to];
                if (!u || !v) return;

                if (activeSubject !== 'all' && 
                    u.subject !== activeSubject && u.subject !== 'master' && 
                    v.subject !== activeSubject && v.subject !== 'master') {{
                    return;
                }}

                // Edge line gradient
                const grad = ctx.createLinearGradient(u.x, u.y, v.x, v.y);
                grad.addColorStop(0, u.color || '#38bdf8');
                grad.addColorStop(1, v.color || '#818cf8');
                
                ctx.strokeStyle = grad;
                ctx.globalAlpha = 0.28;
                ctx.beginPath();
                ctx.moveTo(u.x, u.y);
                ctx.lineTo(v.x, v.y);
                ctx.stroke();
            }});
            ctx.globalAlpha = 1.0;

            // Draw Synaptic Flowing Particles
            if (synapticPulseActive) {{
                particles.forEach(p => {{
                    const u = nodeMap[p.from];
                    const v = nodeMap[p.to];
                    if (!u || !v) return;
                    if (activeSubject !== 'all' && u.subject !== activeSubject && v.subject !== activeSubject) return;

                    p.progress += p.speed;
                    if (p.progress >= 1) p.progress = 0;

                    const px = u.x + (v.x - u.x) * p.progress;
                    const py = u.y + (v.y - u.y) * p.progress;

                    ctx.shadowBlur = 10;
                    ctx.shadowColor = p.color;
                    ctx.fillStyle = '#ffffff';
                    ctx.beginPath();
                    ctx.arc(px, py, 2.2, 0, Math.PI * 2);
                    ctx.fill();
                    ctx.shadowBlur = 0;
                }});
            }}

            // Draw Nodes
            GRAPH_DATA.nodes.forEach(n => {{
                if (activeSubject !== 'all' && n.subject !== activeSubject && n.subject !== 'master') return;

                n.pulse += 0.035;
                const isHovered = hoveredNode === n;
                const isSelected = selectedNode === n;
                const pulseR = n.radius + Math.sin(n.pulse) * 2.5;

                // Outer Glowing Aura
                const glowGrad = ctx.createRadialGradient(n.x, n.y, n.radius * 0.4, n.x, n.y, n.radius * 2.5);
                glowGrad.addColorStop(0, n.color);
                glowGrad.addColorStop(1, 'transparent');
                ctx.globalAlpha = isHovered || isSelected ? 0.75 : 0.32;
                ctx.fillStyle = glowGrad;
                ctx.beginPath();
                ctx.arc(n.x, n.y, n.radius * 2.4, 0, Math.PI * 2);
                ctx.fill();
                ctx.globalAlpha = 1.0;

                // Core Soma Circle
                ctx.shadowBlur = isHovered || isSelected ? 25 : 12;
                ctx.shadowColor = n.color;
                ctx.fillStyle = isSelected ? '#ffffff' : n.color;
                ctx.beginPath();
                ctx.arc(n.x, n.y, isHovered ? pulseR + 4 : pulseR, 0, Math.PI * 2);
                ctx.fill();
                ctx.shadowBlur = 0;

                // Inner core ring
                ctx.strokeStyle = '#ffffff';
                ctx.lineWidth = 1.8;
                ctx.beginPath();
                ctx.arc(n.x, n.y, n.radius * 0.55, 0, Math.PI * 2);
                ctx.stroke();

                // Node Title Label (rendered above/below node)
                if (camera.scale > 0.65 || n.radius >= 24 || isHovered || isSelected) {{
                    ctx.font = `${{isHovered || isSelected ? 'bold 12px' : '10.5px'}} 'Inter', sans-serif`;
                    ctx.textAlign = 'center';
                    ctx.fillStyle = isHovered || isSelected ? '#ffffff' : '#cbd5e1';
                    ctx.shadowBlur = 6;
                    ctx.shadowColor = '#000000';
                    ctx.fillText(n.title, n.x, n.y + n.radius + 15);
                    ctx.shadowBlur = 0;
                }}
            }});

            ctx.restore();
            requestAnimationFrame(animate);
        }}
        requestAnimationFrame(animate);
    </script>
</body>
</html>
"""
    return html

if __name__ == '__main__':
    content = build_mindmap_html()
    with open('mindmap.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Generated mindmap.html successfully ({} bytes)".format(len(content)))
