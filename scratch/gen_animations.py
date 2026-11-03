# scratch/gen_animations.py
# Generates the 60fps Interactive Motion Graphics & Engineering Simulators page (animations.html)
# Features 6 real-time Canvas simulators divided by subject tabs with slider bars and mathematical accuracy.

def build_animations_html():
    html = r"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>60fps Motion Graphics & Interactive Simulators | KTU Mastery Portal</title>
    
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
            --bg-base: #0a0d14;
            --bg-surface: #101622;
            --bg-card: #162030;
            --bg-card-hover: #1d2b40;
            --border-subtle: #24344d;
            --border-focus: #38bdf8;
            --text-main: #f1f5f9;
            --text-body: #cbd5e1;
            --text-muted: #8292a8;
            --header-bg: rgba(13, 19, 29, 0.94);
            --acs-color: #38bdf8;
            --drive-color: #f59e0b;
            --mobile-color: #ec4899;
            --card-shadow: 0 12px 30px rgba(0, 0, 0, 0.5);
        }
        [data-theme="warm"] {
            --bg-base: #120f0d;
            --bg-surface: #1c1713;
            --bg-card: #261f1a;
            --bg-card-hover: #332a23;
            --border-subtle: #3d3129;
            --border-focus: #fbbf24;
            --text-main: #faf4ed;
            --text-body: #ded4c7;
            --text-muted: #a69888;
            --header-bg: rgba(22, 18, 15, 0.94);
            --acs-color: #38bdf8;
            --drive-color: #f59e0b;
            --mobile-color: #f472b6;
            --card-shadow: 0 12px 30px rgba(0, 0, 0, 0.6);
        }
        [data-theme="forest"] {
            --bg-base: #0b1411;
            --bg-surface: #111e19;
            --bg-card: #182a23;
            --bg-card-hover: #20382f;
            --border-subtle: #284438;
            --border-focus: #34d399;
            --text-main: #ecfdf5;
            --text-body: #c7e5d8;
            --text-muted: #7fa896;
            --header-bg: rgba(14, 25, 21, 0.94);
            --acs-color: #38bdf8;
            --drive-color: #fbbf24;
            --mobile-color: #34d399;
            --card-shadow: 0 12px 30px rgba(0, 0, 0, 0.6);
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
            --card-shadow: 0 12px 30px rgba(0, 0, 0, 0.85);
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

        /* Header Navigation */
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

        /* Container */
        .page-container {
            max-width: 1240px;
            margin: 0 auto;
            padding: 2rem 1.25rem;
        }

        .hero-section {
            text-align: center;
            margin-bottom: 2rem;
        }
        .hero-tag {
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: #38bdf8;
            background: rgba(56, 189, 248, 0.15);
            padding: 0.25rem 0.75rem;
            border-radius: 999px;
            margin-bottom: 0.75rem;
        }
        .hero-title {
            font-size: 2.2rem;
            font-weight: 800;
            color: var(--text-main);
            letter-spacing: -0.03em;
            line-height: 1.2;
            margin-bottom: 0.65rem;
        }
        .hero-subtitle {
            font-size: 0.95rem;
            color: var(--text-muted);
            max-width: 720px;
            margin: 0 auto;
        }

        /* Subject Tab Filter Bar for Simulators */
        .subject-filter-wrapper {
            display: flex;
            justify-content: center;
            margin-bottom: 2.5rem;
        }
        .subject-filter-bar {
            display: flex;
            align-items: center;
            gap: 0.35rem;
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            border-radius: 12px;
            padding: 0.35rem;
            overflow-x: auto;
            max-width: 100%;
            scrollbar-width: none;
        }
        .subject-filter-bar::-webkit-scrollbar {
            display: none;
        }
        .sub-filter-tab {
            background: transparent;
            border: 1px solid transparent;
            color: var(--text-muted);
            font-size: 0.83rem;
            font-weight: 600;
            padding: 0.45rem 1rem;
            border-radius: 8px;
            cursor: pointer;
            white-space: nowrap;
            transition: all 0.2s ease;
        }
        .sub-filter-tab:hover {
            color: var(--text-main);
            background: rgba(255, 255, 255, 0.05);
        }
        .sub-filter-tab.active {
            color: #ffffff;
            font-weight: 700;
        }
        .sub-filter-tab[data-subject="all"].active {
            background: #6366f1;
            box-shadow: 0 0 14px rgba(99, 102, 241, 0.4);
        }
        .sub-filter-tab[data-subject="acs"].active {
            background: #0284c7;
            box-shadow: 0 0 14px rgba(2, 132, 199, 0.4);
        }
        .sub-filter-tab[data-subject="drive"].active {
            background: #d97706;
            box-shadow: 0 0 14px rgba(217, 119, 6, 0.4);
        }
        .sub-filter-tab[data-subject="mobile"].active {
            background: #db2777;
            box-shadow: 0 0 14px rgba(219, 39, 119, 0.4);
        }

        /* Simulators Grid */
        .sim-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 2.5rem;
        }

        .sim-card {
            background: var(--bg-card);
            border: 1px solid var(--border-subtle);
            border-radius: 20px;
            overflow: hidden;
            box-shadow: var(--card-shadow);
            transition: border-color 0.25s ease;
        }
        .sim-card:hover {
            border-color: var(--card-focus-color, #38bdf8);
        }

        .sim-header {
            padding: 1.25rem 1.5rem;
            background: var(--bg-surface);
            border-bottom: 1px solid var(--border-subtle);
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .sim-title-group {
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }
        .sim-icon {
            font-size: 1.4rem;
        }
        .sim-title {
            font-size: 1.15rem;
            font-weight: 800;
            color: var(--text-main);
        }
        .sim-badge {
            font-size: 0.72rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            padding: 0.2rem 0.6rem;
            border-radius: 6px;
            background: rgba(255, 255, 255, 0.08);
            color: var(--card-focus-color, #38bdf8);
        }

        .sim-body {
            padding: 1.5rem;
        }

        .canvas-viewport {
            background: #060910;
            border: 1px solid var(--border-subtle);
            border-radius: 14px;
            position: relative;
            overflow: hidden;
            height: 380px;
            margin-bottom: 1.25rem;
        }
        .canvas-viewport canvas {
            width: 100%;
            height: 100%;
            display: block;
        }

        .sim-controls-panel {
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            border-radius: 12px;
            padding: 1rem 1.25rem;
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            gap: 1.25rem;
        }
        .control-group {
            display: flex;
            align-items: center;
            gap: 0.65rem;
        }
        .control-label {
            font-size: 0.82rem;
            font-weight: 600;
            color: var(--text-main);
        }
        .control-val {
            font-size: 0.82rem;
            font-family: 'JetBrains Mono', monospace;
            color: var(--card-focus-color, #38bdf8);
            min-width: 45px;
        }
        .sim-slider {
            width: 130px;
            accent-color: var(--card-focus-color, #38bdf8);
            cursor: pointer;
        }

        .action-btn {
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid var(--border-subtle);
            color: var(--text-main);
            padding: 0.4rem 0.8rem;
            border-radius: 8px;
            font-size: 0.82rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            white-space: nowrap;
        }
        .action-btn:hover {
            background: rgba(255, 255, 255, 0.15);
            border-color: var(--card-focus-color, #38bdf8);
        }

        .explanation-drawer {
            margin-top: 1rem;
            background: rgba(0, 0, 0, 0.25);
            border-left: 3px solid var(--card-focus-color, #38bdf8);
            border-radius: 0 8px 8px 0;
            padding: 0.75rem 1rem;
            font-size: 0.85rem;
            line-height: 1.5;
            color: var(--text-body);
        }
        .explanation-drawer strong {
            color: var(--text-main);
        }

        .dual-canvas-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
            margin-bottom: 1.25rem;
        }
        .sub-canvas-card {
            background: #060910;
            border: 1px solid var(--border-subtle);
            border-radius: 12px;
            padding: 0.75rem;
            display: flex;
            flex-direction: column;
        }
        .sub-canvas-title {
            font-size: 0.78rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--text-muted);
            margin-bottom: 0.4rem;
        }
        .sub-canvas-card canvas {
            width: 100%;
            height: 260px;
            display: block;
            border-radius: 6px;
        }

        @media (max-width: 850px) {
            .dual-canvas-grid {
                grid-template-columns: 1fr;
            }
            .canvas-viewport {
                height: 280px;
            }
            .sub-canvas-card canvas {
                height: 220px;
            }
            .sim-controls-panel {
                gap: 0.75rem;
            }
        }
    </style>
</head>
<body>

    <!-- Header Navigation -->
    <header class="site-header">
        <a href="index.html" class="brand-link">
            <span style="font-size:1.5rem;">🎬</span>
            <span class="brand-title">KTU 60fps Interactive Simulators</span>
        </a>

        <nav class="nav-pills">
            <a href="index.html" class="nav-pill">📚 Question Bank</a>
            <a href="mindmap.html" class="nav-pill">🧠 Mind Map</a>
            <a href="activities.html" class="nav-pill">🎯 Focus Lab</a>
            <a href="animations.html" class="nav-pill active">🎬 60fps Simulators</a>
        </nav>
    </header>

    <main class="page-container">

        <section class="hero-section">
            <span class="hero-tag">⚡ Live Physics &amp; Signal Oscilloscopes</span>
            <h1 class="hero-title">Visual Motion Graphics for Engineering Mastery</h1>
            <p class="hero-subtitle">
                Interact in real time with non-linear limit cycles, inverter SPWM synthesis, converter firing angles, and cellular handover thresholds. Use the slider bars to tune parameters dynamically.
            </p>
        </section>

        <!-- Subject Tab Filter Bar -->
        <div class="subject-filter-wrapper">
            <div class="subject-filter-bar" role="tablist">
                <button class="sub-filter-tab active" data-subject="all" onclick="filterSimSubject('all')">🌟 All Simulators (6 Lab Stations)</button>
                <button class="sub-filter-tab" data-subject="acs" onclick="filterSimSubject('acs')">⚡ ACS Simulators</button>
                <button class="sub-filter-tab" data-subject="drive" onclick="filterSimSubject('drive')">🏎️ Electric Drives Simulators</button>
                <button class="sub-filter-tab" data-subject="mobile" onclick="filterSimSubject('mobile')">📡 Mobile Computing Simulators</button>
            </div>
        </div>

        <div class="sim-grid">

            <!-- SIMULATION 1: ACS Phase Plane & Limit Cycle Studio -->
            <article class="sim-card sim-item-acs" style="--card-focus-color:#38bdf8;">
                <div class="sim-header">
                    <div class="sim-title-group">
                        <span class="sim-icon">🌀</span>
                        <div>
                            <h2 class="sim-title">ACS: Non-Linear Phase Plane &amp; Limit Cycle Studio</h2>
                        </div>
                    </div>
                    <span class="sim-badge">ACS Module 3 &amp; 4</span>
                </div>
                <div class="sim-body">
                    <div class="canvas-viewport" id="viewport-phase">
                        <canvas id="canvas-phase"></canvas>
                    </div>

                    <div class="sim-controls-panel">
                        <div class="control-group">
                            <label class="control-label" for="select-system">Nonlinear System:</label>
                            <select id="select-system" class="action-btn" style="background:var(--bg-card);">
                                <option value="vanderpol">Van der Pol Oscillator (Self-Sustained Limit Cycle)</option>
                                <option value="relay">Relay with Dead Zone (Bang-Bang Chatter)</option>
                                <option value="saddle">Unstable Saddle Point System</option>
                                <option value="harmonic">Undamped Center (Concentric Ellipses)</option>
                            </select>
                        </div>
                        <div class="control-group">
                            <label class="control-label" for="slider-mu">Damping $\mu$:</label>
                            <input type="range" id="slider-mu" class="sim-slider" min="0.1" max="2.5" step="0.1" value="0.8">
                            <span class="control-val" id="val-mu">0.8</span>
                        </div>
                        <button type="button" class="action-btn" onclick="clearPhaseTrajectories()">🧹 Clear Paths</button>
                        <span style="font-size:0.78rem; color:var(--text-muted);">💡 <em>Click anywhere inside grid to spawn custom state trajectories!</em></span>
                    </div>

                    <div class="explanation-drawer">
                        <strong>KTU Exam Core Concept:</strong> A <strong>limit cycle</strong> is an isolated closed trajectory in phase space. In the Van der Pol oscillator $\ddot{x} - \mu(1 - x^2)\dot{x} + x = 0$, trajectories starting inside spiral outward, while trajectories starting outside spiral inward, converging onto the exact same stable periodic orbit.
                    </div>
                </div>
            </article>

            <!-- SIMULATION 2: ACS Closed-Loop Pole Placement & Transient Response -->
            <article class="sim-card sim-item-acs" style="--card-focus-color:#38bdf8;">
                <div class="sim-header">
                    <div class="sim-title-group">
                        <span class="sim-icon">🎯</span>
                        <div>
                            <h2 class="sim-title">ACS: State Feedback Pole Placement &amp; Transient Response</h2>
                        </div>
                    </div>
                    <span class="sim-badge">ACS Module 2: Pole Placement</span>
                </div>
                <div class="sim-body">
                    <div class="dual-canvas-grid">
                        <div class="sub-canvas-card">
                            <div class="sub-canvas-title">Time Domain Step Response $x_1(t)$ &amp; Velocity $x_2(t)$</div>
                            <canvas id="anim-transient-canvas"></canvas>
                        </div>
                        <div class="sub-canvas-card">
                            <div class="sub-canvas-title">Complex $s$-Plane Closed-Loop Poles $s = -\zeta\omega_n \pm j\omega_d$</div>
                            <canvas id="anim-splane-canvas"></canvas>
                        </div>
                    </div>

                    <div class="sim-controls-panel">
                        <div class="control-group">
                            <label class="control-label" for="anim-slider-wn">Natural Frequency $\omega_n$:</label>
                            <input type="range" id="anim-slider-wn" class="sim-slider" min="1.0" max="6.0" step="0.2" value="3.0">
                            <span class="control-val" id="anim-val-wn">3.0 rad/s</span>
                        </div>
                        <div class="control-group">
                            <label class="control-label" for="anim-slider-zeta">Damping Ratio $\zeta$:</label>
                            <input type="range" id="anim-slider-zeta" class="sim-slider" min="0.05" max="1.8" step="0.05" value="0.45">
                            <span class="control-val" id="anim-val-zeta">0.45</span>
                        </div>
                        <button type="button" class="action-btn" onclick="injectAnimStep()">⚡ Step Input</button>
                    </div>

                    <div class="explanation-drawer">
                        <strong>KTU Exam Core Concept (Ackermann's Formula):</strong> For state feedback $u = -K\mathbf{x}$, tuning gain vector $K = [0 \dots 1]Q_c^{-1}\phi_d(A)$ shifts closed-loop eigenvalues arbitrarily. Setting $\zeta = 0.707$ achieves the optimal balance of minimal rise time with less than 4.3% overshoot.
                    </div>
                </div>
            </article>

            <!-- SIMULATION 3: Electric Drives Inverter PWM Sine-Triangle Synthesizer -->
            <article class="sim-card sim-item-drive" style="--card-focus-color:#f59e0b;">
                <div class="sim-header">
                    <div class="sim-title-group">
                        <span class="sim-icon">⚡</span>
                        <div>
                            <h2 class="sim-title">Electric Drives: SPWM Inverter Sine-Triangle Synthesizer</h2>
                        </div>
                    </div>
                    <span class="sim-badge">Drives Module 3 &amp; 4</span>
                </div>
                <div class="sim-body">
                    <div class="canvas-viewport">
                        <canvas id="canvas-pwm"></canvas>
                    </div>

                    <div class="sim-controls-panel">
                        <div class="control-group">
                            <label class="control-label" for="slider-ma">Modulation Index $m_a = V_m/V_c$:</label>
                            <input type="range" id="slider-ma" class="sim-slider" min="0.2" max="1.4" step="0.05" value="0.85" style="accent-color:#f59e0b;">
                            <span class="control-val" id="val-ma" style="color:#f59e0b;">0.85</span>
                        </div>
                        <div class="control-group">
                            <label class="control-label" for="slider-mf">Carrier Ratio $m_f = f_c/f_m$:</label>
                            <input type="range" id="slider-mf" class="sim-slider" min="9" max="27" step="2" value="15" style="accent-color:#f59e0b;">
                            <span class="control-val" id="val-mf" style="color:#f59e0b;">15</span>
                        </div>
                        <button type="button" class="action-btn" id="btn-pwm-pause" onclick="togglePWMPause()">⏸️ Pause</button>
                    </div>

                    <div class="explanation-drawer" style="border-left-color:#f59e0b;">
                        <strong>KTU Exam Core Concept:</strong> In Sinusoidal PWM (SPWM), the comparator generates IGBT gate pulses whenever sinusoidal modulating wave $v_{ref} > v_{carrier}$. For $m_a \le 1.0$, output fundamental voltage is linear $V_{AO1} = m_a \frac{V_{dc}}{2}$. For $m_a > 1.0$ (Overmodulation), pulses merge into square-wave conduction.
                    </div>
                </div>
            </article>

            <!-- SIMULATION 4: Electric Drives Converter DC Drive & Firing Angle -->
            <article class="sim-card sim-item-drive" style="--card-focus-color:#f59e0b;">
                <div class="sim-header">
                    <div class="sim-title-group">
                        <span class="sim-icon">🏎️</span>
                        <div>
                            <h2 class="sim-title">Electric Drives: Converter DC Drive Firing Angle &amp; Conduction Mode</h2>
                        </div>
                    </div>
                    <span class="sim-badge">Drives Module 2: Converter Drives</span>
                </div>
                <div class="sim-body">
                    <div class="dual-canvas-grid">
                        <div class="sub-canvas-card">
                            <div class="sub-canvas-title">Armature Current Waveform $i_a(t)$</div>
                            <canvas id="anim-converter-canvas"></canvas>
                        </div>
                        <div class="sub-canvas-card">
                            <div class="sub-canvas-title">Torque-Speed Characteristic Curve $(T_e, \omega_m)$</div>
                            <canvas id="anim-speedtorque-canvas"></canvas>
                        </div>
                    </div>

                    <div class="sim-controls-panel">
                        <div class="control-group">
                            <label class="control-label" for="anim-slider-alpha">Firing Angle $\alpha$:</label>
                            <input type="range" id="anim-slider-alpha" class="sim-slider" min="0" max="150" step="5" value="45" style="accent-color:#f59e0b;">
                            <span class="control-val" id="anim-val-alpha" style="color:#f59e0b;">45&deg;</span>
                        </div>
                        <div class="control-group">
                            <label class="control-label" for="anim-slider-torque">Load Torque $T_L$:</label>
                            <input type="range" id="anim-slider-torque" class="sim-slider" min="0.1" max="2.0" step="0.1" value="1.0" style="accent-color:#f59e0b;">
                            <span class="control-val" id="anim-val-torque" style="color:#f59e0b;">1.0 p.u.</span>
                        </div>
                        <div class="control-group">
                            <label class="control-label" for="anim-slider-induct">Armature Inductance $L_a$:</label>
                            <input type="range" id="anim-slider-induct" class="sim-slider" min="1" max="3" step="1" value="2" style="accent-color:#f59e0b;">
                            <span class="control-val" id="anim-val-induct" style="color:#f59e0b;">Medium</span>
                        </div>
                    </div>

                    <div class="explanation-drawer" style="border-left-color:#f59e0b;">
                        <strong>KTU Exam Core Concept:</strong> In 1-phase full converters, $V_0 = \frac{2V_m}{\pi}\cos\alpha$. In Discontinuous Conduction Mode (DCM), current falls to zero before the next thyristor fires, causing severe no-load speed surges and poor regulation. Adding series inductance $L_a$ restores linear Continuous Conduction Mode (CCM).
                    </div>
                </div>
            </article>

            <!-- SIMULATION 5: Mobile Computing Cellular Handover & RSSI -->
            <article class="sim-card sim-item-mobile" style="--card-focus-color:#ec4899;">
                <div class="sim-header">
                    <div class="sim-title-group">
                        <span class="sim-icon">📶</span>
                        <div>
                            <h2 class="sim-title">Mobile Computing: Cellular Handover &amp; Hysteresis Margin</h2>
                        </div>
                    </div>
                    <span class="sim-badge">Mobile Module 1: Mobility Management</span>
                </div>
                <div class="sim-body">
                    <div class="dual-canvas-grid">
                        <div class="sub-canvas-card">
                            <div class="sub-canvas-title">Cellular Hexagonal Grid &amp; Active Vehicle Link</div>
                            <canvas id="anim-hex-canvas"></canvas>
                        </div>
                        <div class="sub-canvas-card">
                            <div class="sub-canvas-title">Received Signal Strength (RSSI) &amp; Margin $\Delta$</div>
                            <canvas id="anim-rssi-canvas"></canvas>
                        </div>
                    </div>

                    <div class="sim-controls-panel">
                        <div class="control-group">
                            <label class="control-label" for="anim-slider-speed">Vehicle Speed $v$:</label>
                            <input type="range" id="anim-slider-speed" class="sim-slider" min="20" max="120" step="10" value="50" style="accent-color:#ec4899;">
                            <span class="control-val" id="anim-val-speed" style="color:#ec4899;">50 km/h</span>
                        </div>
                        <div class="control-group">
                            <label class="control-label" for="anim-slider-margin">Hysteresis Margin $\Delta$:</label>
                            <input type="range" id="anim-slider-margin" class="sim-slider" min="1" max="14" step="1" value="6" style="accent-color:#ec4899;">
                            <span class="control-val" id="anim-val-margin" style="color:#ec4899;">6 dB</span>
                        </div>
                        <button type="button" class="action-btn" onclick="restartAnimVehicle()">🚗 Restart Vehicle</button>
                    </div>

                    <div class="explanation-drawer" style="border-left-color:#ec4899;">
                        <strong>KTU Exam Core Concept:</strong> Handovers are triggered when the target base station signal exceeds the serving base station signal by hysteresis threshold $\Delta = P_{ho} - P_{min}$. If $\Delta$ is too small, shadow fading causes ping-pong switching; if too large, the call drops before handover completion.
                    </div>
                </div>
            </article>

            <!-- SIMULATION 6: Mobile Computing CSMA/CA & Hidden Terminal Handshake -->
            <article class="sim-card sim-item-mobile" style="--card-focus-color:#ec4899;">
                <div class="sim-header">
                    <div class="sim-title-group">
                        <span class="sim-icon">📡</span>
                        <div>
                            <h2 class="sim-title">Mobile Computing: CSMA/CA RTS/CTS &amp; Hidden Terminal</h2>
                        </div>
                    </div>
                    <span class="sim-badge">Mobile Module 3: MAC</span>
                </div>
                <div class="sim-body">
                    <div class="canvas-viewport">
                        <canvas id="canvas-mac"></canvas>
                    </div>

                    <div class="sim-controls-panel">
                        <button type="button" class="action-btn" id="btn-toggle-rts" onclick="toggleRTSMode()">Mode: With RTS/CTS (Collision Free)</button>
                        <button type="button" class="action-btn" onclick="triggerMACTransmit()">🚀 Trigger Transmission</button>
                        <span id="mac-status-text" style="font-size:0.82rem; font-weight:700; color:#34d399;">Medium Status: Idle</span>
                    </div>

                    <div class="explanation-drawer" style="border-left-color:#ec4899;">
                        <strong>KTU Exam Core Concept:</strong> The <strong>Hidden Terminal Problem</strong> occurs when Node A and Node C cannot hear each other, causing collisions at the Access Point (AP). IEEE 802.11 solves this using virtual carrier sensing: Node A sends Request-to-Send (RTS) $\to$ AP replies with Clear-to-Send (CTS) containing the duration field $\to$ Node C overhears CTS and freezes its transmission via Network Allocation Vector (NAV).
                    </div>
                </div>
            </article>

        </div>

    </main>

    <!-- Canvas Simulation Scripts -->
    <script>
        // Filter simulators by subject tab
        function filterSimSubject(subject) {
            document.querySelectorAll('.sub-filter-tab').forEach(tab => {
                if (tab.getAttribute('data-subject') === subject) tab.classList.add('active');
                else tab.classList.remove('active');
            });

            document.querySelectorAll('.sim-card').forEach(card => {
                if (subject === 'all') {
                    card.style.display = 'block';
                } else if (card.classList.contains(`sim-item-${subject}`)) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        }

        // =========================================================================
        // 1. ACS PHASE PLANE & LIMIT CYCLE
        // =========================================================================
        const pCanvas = document.getElementById('canvas-phase');
        const pCtx = pCanvas.getContext('2d');
        const selectSys = document.getElementById('select-system');
        const sliderMu = document.getElementById('slider-mu');
        const valMu = document.getElementById('val-mu');

        let trajectories = [];
        let particles = [];

        function resizePhase() {
            pCanvas.width = pCanvas.parentElement.clientWidth;
            pCanvas.height = 380;
            initPhaseGrid();
        }
        window.addEventListener('resize', resizePhase);

        function initPhaseGrid() {
            trajectories = [];
            particles = [];
            spawnTrajectory(-1.8, -0.4);
            spawnTrajectory(0.2, 0.2);
            spawnTrajectory(2.2, 1.2);
        }

        sliderMu.addEventListener('input', e => {
            valMu.textContent = parseFloat(e.target.value).toFixed(1);
        });

        selectSys.addEventListener('change', () => {
            initPhaseGrid();
        });

        function clearPhaseTrajectories() {
            trajectories = [];
            particles = [];
        }

        function spawnTrajectory(x0, y0) {
            const path = [{ x: x0, y: y0 }];
            let curX = x0;
            let curY = y0;
            const dt = 0.02;
            const mu = parseFloat(sliderMu.value);
            const sys = selectSys.value;

            for (let i = 0; i < 400; i++) {
                let dx, dy;
                if (sys === 'vanderpol') {
                    dx = curY;
                    dy = mu * (1 - curX * curX) * curY - curX;
                } else if (sys === 'relay') {
                    dx = curY;
                    const dead = 0.4;
                    let u = 0;
                    if (curX > dead) u = -1.2;
                    else if (curX < -dead) u = 1.2;
                    dy = -0.3 * curY + u;
                } else if (sys === 'saddle') {
                    dx = 1.2 * curX;
                    dy = -1.2 * curY;
                } else {
                    dx = curY;
                    dy = -curX;
                }
                curX += dx * dt;
                curY += dy * dt;
                path.push({ x: curX, y: curY });
                if (Math.abs(curX) > 4 || Math.abs(curY) > 4) break;
            }
            trajectories.push(path);
            particles.push({ path, idx: 0, speed: 1 });
        }

        pCanvas.addEventListener('click', e => {
            const rect = pCanvas.getBoundingClientRect();
            const w = pCanvas.width;
            const h = pCanvas.height;
            const cx = w / 2;
            const cy = h / 2;
            const scale = 55;
            const clickX = (e.clientX - rect.left - cx) / scale;
            const clickY = -(e.clientY - rect.top - cy) / scale;
            spawnTrajectory(clickX, clickY);
        });

        function drawPhase() {
            const w = pCanvas.width;
            const h = pCanvas.height;
            pCtx.clearRect(0, 0, w, h);

            const cx = w / 2;
            const cy = h / 2;
            const scale = 55;

            // Coordinate grid
            pCtx.strokeStyle = 'rgba(255, 255, 255, 0.08)';
            pCtx.lineWidth = 1;
            for (let x = cx % 40; x < w; x += 40) {
                pCtx.beginPath(); pCtx.moveTo(x, 0); pCtx.lineTo(x, h); pCtx.stroke();
            }
            for (let y = cy % 40; y < h; y += 40) {
                pCtx.beginPath(); pCtx.moveTo(0, y); pCtx.lineTo(w, y); pCtx.stroke();
            }

            // Axes
            pCtx.strokeStyle = 'rgba(56, 189, 248, 0.4)';
            pCtx.lineWidth = 1.5;
            pCtx.beginPath();
            pCtx.moveTo(0, cy); pCtx.lineTo(w, cy);
            pCtx.moveTo(cx, 0); pCtx.lineTo(cx, h);
            pCtx.stroke();

            // Axis labels
            pCtx.fillStyle = '#8292a8';
            pCtx.font = '11px Inter';
            pCtx.fillText('x\u2081 (State Output)', w - 100, cy - 8);
            pCtx.fillText('x\u2082 = dx\u2081/dt (Velocity)', cx + 8, 20);

            // Draw Trajectories
            trajectories.forEach(path => {
                pCtx.strokeStyle = 'rgba(56, 189, 248, 0.5)';
                pCtx.lineWidth = 1.6;
                pCtx.beginPath();
                path.forEach((pt, idx) => {
                    const scrX = cx + pt.x * scale;
                    const scrY = cy - pt.y * scale;
                    if (idx === 0) pCtx.moveTo(scrX, scrY);
                    else pCtx.lineTo(scrX, scrY);
                });
                pCtx.stroke();
            });

            // Animated moving state particles along orbits
            particles.forEach(p => {
                p.idx = (p.idx + p.speed) % p.path.length;
                const pt = p.path[Math.floor(p.idx)];
                if (!pt) return;
                const scrX = cx + pt.x * scale;
                const scrY = cy - pt.y * scale;

                pCtx.shadowBlur = 10;
                pCtx.shadowColor = '#38bdf8';
                pCtx.fillStyle = '#ffffff';
                pCtx.beginPath();
                pCtx.arc(scrX, scrY, 3.5, 0, Math.PI * 2);
                pCtx.fill();
                pCtx.shadowBlur = 0;
            });

            requestAnimationFrame(drawPhase);
        }
        resizePhase();
        drawPhase();

        // =========================================================================
        // 2. ACS POLE PLACEMENT & TRANSIENT RESPONSE
        // =========================================================================
        const tCanvas = document.getElementById('anim-transient-canvas');
        const sCanvas = document.getElementById('anim-splane-canvas');
        const tCtx = tCanvas.getContext('2d');
        const sCtx = sCanvas.getContext('2d');
        const sliderWn = document.getElementById('anim-slider-wn');
        const valWn = document.getElementById('anim-val-wn');
        const sliderZeta = document.getElementById('anim-slider-zeta');
        const valZeta = document.getElementById('anim-val-zeta');

        function resizePoleSim() {
            tCanvas.width = tCanvas.parentElement.clientWidth - 20;
            tCanvas.height = 260;
            sCanvas.width = sCanvas.parentElement.clientWidth - 20;
            sCanvas.height = 260;
        }
        window.addEventListener('resize', resizePoleSim);
        resizePoleSim();

        sliderWn.addEventListener('input', e => { valWn.textContent = parseFloat(e.target.value).toFixed(1) + ' rad/s'; });
        sliderZeta.addEventListener('input', e => { valZeta.textContent = parseFloat(e.target.value).toFixed(2); });
        window.injectAnimStep = () => {};

        function drawPoleSim() {
            const tw = tCanvas.width, th = tCanvas.height;
            tCtx.clearRect(0, 0, tw, th);

            const wn = parseFloat(sliderWn.value);
            const z = parseFloat(sliderZeta.value);

            // Step Target
            const yRef = th * 0.4;
            tCtx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
            tCtx.lineWidth = 1;
            tCtx.setLineDash([4, 4]);
            tCtx.beginPath(); tCtx.moveTo(0, yRef); tCtx.lineTo(tw, yRef); tCtx.stroke();
            tCtx.setLineDash([]);

            // Transient Waveform
            tCtx.strokeStyle = '#38bdf8';
            tCtx.lineWidth = 2.4;
            tCtx.beginPath();
            const maxT = 6.0;
            for (let px = 0; px < tw; px++) {
                const t = (px / tw) * maxT;
                let yVal = 0;
                if (z < 1.0) {
                    const wd = wn * Math.sqrt(1 - z * z);
                    const phi = Math.acos(z);
                    yVal = 1 - (Math.exp(-z * wn * t) / Math.sqrt(1 - z * z)) * Math.sin(wd * t + phi);
                } else if (Math.abs(z - 1.0) < 0.05) {
                    yVal = 1 - (1 + wn * t) * Math.exp(-wn * t);
                } else {
                    const s1 = -wn * (z - Math.sqrt(z * z - 1));
                    const s2 = -wn * (z + Math.sqrt(z * z - 1));
                    yVal = 1 - (s2 * Math.exp(s1 * t) - s1 * Math.exp(s2 * t)) / (s2 - s1);
                }
                const py = (th * 0.85) - yVal * (th * 0.45);
                if (px === 0) tCtx.moveTo(px, py); else tCtx.lineTo(px, py);
            }
            tCtx.stroke();

            // S-Plane
            const sw = sCanvas.width, sh = sCanvas.height;
            sCtx.clearRect(0, 0, sw, sh);
            const scx = sw * 0.7, scy = sh / 2;

            sCtx.fillStyle = 'rgba(16, 185, 129, 0.06)';
            sCtx.fillRect(0, 0, scx, sh);

            sCtx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
            sCtx.beginPath(); sCtx.moveTo(0, scy); sCtx.lineTo(sw, scy); sCtx.moveTo(scx, 0); sCtx.lineTo(scx, sh); sCtx.stroke();

            const scale = 22;
            sCtx.strokeStyle = '#38bdf8';
            sCtx.lineWidth = 3;
            const pSize = 7;
            if (z < 1.0) {
                const sigma = -z * wn;
                const wd = wn * Math.sqrt(1 - z * z);
                [
                    { x: scx + sigma * scale, y: scy - wd * scale },
                    { x: scx + sigma * scale, y: scy + wd * scale }
                ].forEach(p => {
                    sCtx.beginPath();
                    sCtx.moveTo(p.x - pSize, p.y - pSize); sCtx.lineTo(p.x + pSize, p.y + pSize);
                    sCtx.moveTo(p.x + pSize, p.y - pSize); sCtx.lineTo(p.x - pSize, p.y + pSize);
                    sCtx.stroke();
                });
            } else {
                const s1 = -wn * (z - Math.sqrt(z * z - 1));
                const s2 = -wn * (z + Math.sqrt(z * z - 1));
                [s1, s2].forEach(sVal => {
                    const px = scx + sVal * scale;
                    sCtx.beginPath();
                    sCtx.moveTo(px - pSize, scy - pSize); sCtx.lineTo(px + pSize, scy + pSize);
                    sCtx.moveTo(px + pSize, scy - pSize); sCtx.lineTo(px - pSize, scy + pSize);
                    sCtx.stroke();
                });
            }

            requestAnimationFrame(drawPoleSim);
        }
        drawPoleSim();

        // =========================================================================
        // 3. SPWM INVERTER SINE-TRIANGLE
        // =========================================================================
        const pwmCanvas = document.getElementById('canvas-pwm');
        const pwmCtx = pwmCanvas.getContext('2d');
        const sliderMa = document.getElementById('slider-ma');
        const valMa = document.getElementById('val-ma');
        const sliderMf = document.getElementById('slider-mf');
        const valMf = document.getElementById('val-mf');

        let pwmTime = 0;
        let isPWMPaused = false;

        function resizePWM() {
            pwmCanvas.width = pwmCanvas.parentElement.clientWidth;
            pwmCanvas.height = 380;
        }
        window.addEventListener('resize', resizePWM);
        resizePWM();

        sliderMa.addEventListener('input', e => {
            valMa.textContent = parseFloat(e.target.value).toFixed(2);
        });
        sliderMf.addEventListener('input', e => {
            valMf.textContent = e.target.value;
        });

        function togglePWMPause() {
            isPWMPaused = !isPWMPaused;
            document.getElementById('btn-pwm-pause').textContent = isPWMPaused ? '▶️ Resume' : '⏸️ Pause';
        }

        function drawPWM() {
            if (!isPWMPaused) pwmTime += 0.02;

            const w = pwmCanvas.width;
            const h = pwmCanvas.height;
            pwmCtx.clearRect(0, 0, w, h);

            const ma = parseFloat(sliderMa.value);
            const mf = parseInt(sliderMf.value);

            const topH = h * 0.45;
            const botH = h * 0.45;
            const cy1 = topH / 2;
            const cy2 = topH + (botH / 2);

            pwmCtx.strokeStyle = 'rgba(255, 255, 255, 0.1)';
            pwmCtx.lineWidth = 1;
            pwmCtx.beginPath();
            pwmCtx.moveTo(0, topH);
            pwmCtx.lineTo(w, topH);
            pwmCtx.stroke();

            // Carrier Triangle
            pwmCtx.strokeStyle = 'rgba(255, 255, 255, 0.3)';
            pwmCtx.lineWidth = 1.2;
            pwmCtx.beginPath();
            const carrierPeriod = w / (mf / 2);
            for (let x = 0; x < w; x++) {
                const phase = (x % carrierPeriod) / carrierPeriod;
                const tri = (phase < 0.5) ? (4 * phase - 1) : (3 - 4 * phase);
                const y = cy1 - tri * (cy1 * 0.75);
                if (x === 0) pwmCtx.moveTo(x, y);
                else pwmCtx.lineTo(x, y);
            }
            pwmCtx.stroke();

            // Sine Modulating
            pwmCtx.strokeStyle = '#f59e0b';
            pwmCtx.lineWidth = 2.2;
            pwmCtx.beginPath();
            for (let x = 0; x < w; x++) {
                const theta = (x / w) * (Math.PI * 2) + pwmTime;
                const sine = Math.sin(theta) * ma;
                const y = cy1 - sine * (cy1 * 0.75);
                if (x === 0) pwmCtx.moveTo(x, y);
                else pwmCtx.lineTo(x, y);
            }
            pwmCtx.stroke();

            // Switched Output V_AO
            pwmCtx.strokeStyle = '#38bdf8';
            pwmCtx.lineWidth = 2;
            pwmCtx.beginPath();
            let lastHigh = false;
            for (let x = 0; x < w; x++) {
                const phase = (x % carrierPeriod) / carrierPeriod;
                const tri = (phase < 0.5) ? (4 * phase - 1) : (3 - 4 * phase);
                const theta = (x / w) * (Math.PI * 2) + pwmTime;
                const sine = Math.sin(theta) * ma;

                const isHigh = sine > tri;
                const yVal = isHigh ? (cy2 - botH * 0.32) : (cy2 + botH * 0.32);

                if (x === 0) {
                    pwmCtx.moveTo(x, yVal);
                } else {
                    if (isHigh !== lastHigh) {
                        pwmCtx.lineTo(x, isHigh ? (cy2 + botH * 0.32) : (cy2 - botH * 0.32));
                    }
                    pwmCtx.lineTo(x, yVal);
                }
                lastHigh = isHigh;
            }
            pwmCtx.stroke();

            requestAnimationFrame(drawPWM);
        }
        drawPWM();

        // =========================================================================
        // 4. DRIVES CONVERTER DC DRIVE
        // =========================================================================
        const convCanvas = document.getElementById('anim-converter-canvas');
        const stCanvas = document.getElementById('anim-speedtorque-canvas');
        const convCtx = convCanvas.getContext('2d');
        const stCtx = stCanvas.getContext('2d');
        const sliderAlpha = document.getElementById('anim-slider-alpha');
        const valAlpha = document.getElementById('anim-val-alpha');
        const sliderTorque = document.getElementById('anim-slider-torque');
        const valTorque = document.getElementById('anim-val-torque');
        const sliderInduct = document.getElementById('anim-slider-induct');
        const valInduct = document.getElementById('anim-val-induct');

        function resizeConvSim() {
            convCanvas.width = convCanvas.parentElement.clientWidth - 20;
            convCanvas.height = 260;
            stCanvas.width = stCanvas.parentElement.clientWidth - 20;
            stCanvas.height = 260;
        }
        window.addEventListener('resize', resizeConvSim);
        resizeConvSim();

        sliderAlpha.addEventListener('input', e => { valAlpha.textContent = e.target.value + '\u00b0'; });
        sliderTorque.addEventListener('input', e => { valTorque.textContent = parseFloat(e.target.value).toFixed(1) + ' p.u.'; });
        sliderInduct.addEventListener('input', e => {
            const v = parseInt(e.target.value);
            valInduct.textContent = v === 1 ? 'Low' : (v === 2 ? 'Medium' : 'High');
        });

        function drawConvSim() {
            const alphaDeg = parseFloat(sliderAlpha.value);
            const torque = parseFloat(sliderTorque.value);
            const induct = parseInt(sliderInduct.value);

            const isDCM = (torque < 0.6 && induct === 1) || (torque < 0.35 && induct === 2);

            // Current Waveform
            const cw = convCanvas.width, ch = convCanvas.height;
            convCtx.clearRect(0, 0, cw, ch);

            convCtx.strokeStyle = 'rgba(255, 255, 255, 0.15)';
            convCtx.beginPath(); convCtx.moveTo(0, ch * 0.7); convCtx.lineTo(cw, ch * 0.7); convCtx.stroke();

            convCtx.strokeStyle = '#f59e0b';
            convCtx.lineWidth = 2.4;
            convCtx.beginPath();
            const baseCurrent = torque * (ch * 0.35);
            for (let x = 0; x < cw; x++) {
                const cycleX = (x % 120) / 120;
                let cur = 0;
                if (isDCM) {
                    if (cycleX < 0.65) cur = Math.sin(cycleX / 0.65 * Math.PI) * baseCurrent * 1.6;
                    else cur = 0;
                } else {
                    cur = baseCurrent + Math.sin(cycleX * Math.PI * 2) * (18 / induct);
                }
                const py = (ch * 0.7) - cur;
                if (x === 0) convCtx.moveTo(x, py); else convCtx.lineTo(x, py);
            }
            convCtx.stroke();

            // Speed-Torque
            const sw = stCanvas.width, sh = stCanvas.height;
            stCtx.clearRect(0, 0, sw, sh);

            stCtx.strokeStyle = 'rgba(255, 255, 255, 0.15)';
            stCtx.beginPath(); stCtx.moveTo(35, sh - 30); stCtx.lineTo(sw - 10, sh - 30); stCtx.stroke();
            stCtx.beginPath(); stCtx.moveTo(35, sh - 30); stCtx.lineTo(35, 10); stCtx.stroke();

            const noLoadSpeed = (sh - 40) - Math.cos(alphaDeg * Math.PI / 180) * (sh * 0.4);
            stCtx.strokeStyle = 'rgba(245, 158, 11, 0.6)';
            stCtx.lineWidth = 2;
            stCtx.beginPath();
            stCtx.moveTo(35, noLoadSpeed);
            stCtx.lineTo(sw - 20, noLoadSpeed + 45);
            stCtx.stroke();

            const ptX = 35 + torque * ((sw - 60) / 2.0);
            let ptY = noLoadSpeed + (torque * 22);
            if (isDCM) ptY -= 25;

            stCtx.fillStyle = '#38bdf8';
            stCtx.beginPath();
            stCtx.arc(ptX, ptY, 6, 0, Math.PI * 2);
            stCtx.fill();

            requestAnimationFrame(drawConvSim);
        }
        drawConvSim();

        // =========================================================================
        // 5. MOBILE CELLULAR HANDOVER & RSSI
        // =========================================================================
        const hexCanvas = document.getElementById('anim-hex-canvas');
        const rssiCanvas = document.getElementById('anim-rssi-canvas');
        const hexCtx = hexCanvas.getContext('2d');
        const rssiCtx = rssiCanvas.getContext('2d');
        const sliderSpeed = document.getElementById('anim-slider-speed');
        const valSpeed = document.getElementById('anim-val-speed');
        const sliderMargin = document.getElementById('anim-slider-margin');
        const valMargin = document.getElementById('anim-val-margin');

        let carDist = 0.15;
        let connectedTower = 'A';

        function resizeMobileSim() {
            hexCanvas.width = hexCanvas.parentElement.clientWidth - 20;
            hexCanvas.height = 260;
            rssiCanvas.width = rssiCanvas.parentElement.clientWidth - 20;
            rssiCanvas.height = 260;
        }
        window.addEventListener('resize', resizeMobileSim);
        resizeMobileSim();

        sliderSpeed.addEventListener('input', e => { valSpeed.textContent = e.target.value + ' km/h'; });
        sliderMargin.addEventListener('input', e => { valMargin.textContent = e.target.value + ' dB'; });
        window.restartAnimVehicle = () => { carDist = 0.05; connectedTower = 'A'; };

        function drawHexGrid(ctx, x, y, r, color) {
            ctx.strokeStyle = color;
            ctx.fillStyle = color.replace(')', ', 0.05)').replace('rgb', 'rgba');
            ctx.lineWidth = 1.4;
            ctx.beginPath();
            for (let i = 0; i < 6; i++) {
                const angle = (i * 60) * Math.PI / 180;
                const hx = x + r * Math.cos(angle);
                const hy = y + r * Math.sin(angle);
                if (i === 0) ctx.moveTo(hx, hy); else ctx.lineTo(hx, hy);
            }
            ctx.closePath();
            ctx.fill();
            ctx.stroke();
        }

        function drawMobileSim() {
            const hw = hexCanvas.width, hh = hexCanvas.height;
            hexCtx.clearRect(0, 0, hw, hh);

            const vSpeed = parseFloat(sliderSpeed.value);
            const margin = parseFloat(sliderMargin.value);

            carDist += (vSpeed / 120) * 0.003;
            if (carDist > 0.95) carDist = 0.05;

            const btsA = { x: hw * 0.28, y: hh * 0.5 };
            const btsB = { x: hw * 0.72, y: hh * 0.5 };
            const hexR = hw * 0.22;

            drawHexGrid(hexCtx, btsA.x, btsA.y, hexR, 'rgb(56, 189, 248)');
            drawHexGrid(hexCtx, btsB.x, btsB.y, hexR, 'rgb(236, 72, 153)');

            [btsA, btsB].forEach((bts, idx) => {
                hexCtx.fillStyle = idx === 0 ? '#38bdf8' : '#ec4899';
                hexCtx.beginPath(); hexCtx.arc(bts.x, bts.y, 8, 0, Math.PI * 2); hexCtx.fill();
            });

            const carX = btsA.x + (btsB.x - btsA.x) * carDist;
            hexCtx.fillStyle = '#fbbf24';
            hexCtx.beginPath(); hexCtx.arc(carX, hh * 0.5, 6, 0, Math.PI * 2); hexCtx.fill();

            // RSSI
            const rw = rssiCanvas.width, rh = rssiCanvas.height;
            rssiCtx.clearRect(0, 0, rw, rh);

            rssiCtx.strokeStyle = 'rgba(255, 255, 255, 0.15)';
            rssiCtx.beginPath(); rssiCtx.moveTo(35, rh - 30); rssiCtx.lineTo(rw - 10, rh - 30); rssiCtx.stroke();
            rssiCtx.beginPath(); rssiCtx.moveTo(35, rh - 30); rssiCtx.lineTo(35, 15); rssiCtx.stroke();

            // Signal A (Cyan)
            rssiCtx.strokeStyle = '#38bdf8';
            rssiCtx.lineWidth = 2;
            rssiCtx.beginPath();
            for (let x = 35; x < rw - 10; x++) {
                const frac = (x - 35) / (rw - 45);
                const rVal = -40 - frac * 60;
                const py = (rh - 30) - (rVal + 110) * (rh * 0.65 / 80);
                if (x === 35) rssiCtx.moveTo(x, py); else rssiCtx.lineTo(x, py);
            }
            rssiCtx.stroke();

            // Signal B (Pink)
            rssiCtx.strokeStyle = '#ec4899';
            rssiCtx.lineWidth = 2;
            rssiCtx.beginPath();
            for (let x = 35; x < rw - 10; x++) {
                const frac = (x - 35) / (rw - 45);
                const rVal = -100 + frac * 60;
                const py = (rh - 30) - (rVal + 110) * (rh * 0.65 / 80);
                if (x === 35) rssiCtx.moveTo(x, py); else rssiCtx.lineTo(x, py);
            }
            rssiCtx.stroke();

            const curPx = 35 + carDist * (rw - 45);
            rssiCtx.strokeStyle = '#fbbf24';
            rssiCtx.lineWidth = 1.5;
            rssiCtx.setLineDash([3, 3]);
            rssiCtx.beginPath(); rssiCtx.moveTo(curPx, 15); rssiCtx.lineTo(curPx, rh - 30); rssiCtx.stroke();
            rssiCtx.setLineDash([]);

            requestAnimationFrame(drawMobileSim);
        }
        drawMobileSim();

        // =========================================================================
        // 6. CSMA/CA HIDDEN TERMINAL
        // =========================================================================
        const macCanvas = document.getElementById('canvas-mac');
        const macCtx = macCanvas.getContext('2d');
        const statusText = document.getElementById('mac-status-text');

        let rtsEnabled = true;
        let macPacketProgress = 0;
        let macState = 'idle';

        function resizeMAC() {
            macCanvas.width = macCanvas.parentElement.clientWidth;
            macCanvas.height = 380;
        }
        window.addEventListener('resize', resizeMAC);
        resizeMAC();

        function toggleRTSMode() {
            rtsEnabled = !rtsEnabled;
            document.getElementById('btn-toggle-rts').textContent = rtsEnabled ? 'Mode: With RTS/CTS (Collision Free)' : 'Mode: Without RTS/CTS (Hidden Collisions)';
        }

        function triggerMACTransmit() {
            macPacketProgress = 0;
            macState = 'transmitting';
            statusText.textContent = rtsEnabled ? 'Transmitting RTS / Setting NAV...' : 'Simultaneous Transmit... Collision Imminent!';
            statusText.style.color = rtsEnabled ? '#38bdf8' : '#f87171';
        }

        function drawMAC() {
            const w = macCanvas.width;
            const h = macCanvas.height;
            macCtx.clearRect(0, 0, w, h);

            const nodeA = { x: w * 0.2, y: h * 0.5, name: 'Node A (Sender 1)' };
            const nodeAP = { x: w * 0.5, y: h * 0.5, name: 'Access Point (AP)' };
            const nodeC = { x: w * 0.8, y: h * 0.5, name: 'Node C (Sender 2)' };

            const rRange = w * 0.35;
            macCtx.strokeStyle = 'rgba(56, 189, 248, 0.2)';
            macCtx.beginPath();
            macCtx.arc(nodeA.x, nodeA.y, rRange, 0, Math.PI * 2);
            macCtx.stroke();

            macCtx.strokeStyle = 'rgba(236, 72, 153, 0.2)';
            macCtx.beginPath();
            macCtx.arc(nodeC.x, nodeC.y, rRange, 0, Math.PI * 2);
            macCtx.stroke();

            [nodeA, nodeAP, nodeC].forEach((n, idx) => {
                macCtx.fillStyle = idx === 1 ? '#fbbf24' : (idx === 0 ? '#38bdf8' : '#ec4899');
                macCtx.beginPath();
                macCtx.arc(n.x, n.y, 16, 0, Math.PI * 2);
                macCtx.fill();

                macCtx.fillStyle = '#ffffff';
                macCtx.font = 'bold 12px Inter';
                macCtx.textAlign = 'center';
                macCtx.fillText(n.name, n.x, n.y + 32);
            });

            if (macState === 'transmitting') {
                macPacketProgress += 0.015;
                if (macPacketProgress > 1) {
                    macState = 'idle';
                    statusText.textContent = rtsEnabled ? 'Transmission Succeeded! (ACK Received)' : 'Collision Occurred at AP! Backing off...';
                    statusText.style.color = rtsEnabled ? '#34d399' : '#f87171';
                }

                const curAx = nodeA.x + (nodeAP.x - nodeA.x) * macPacketProgress;
                macCtx.fillStyle = '#38bdf8';
                macCtx.beginPath();
                macCtx.arc(curAx, nodeA.y, 6, 0, Math.PI * 2);
                macCtx.fill();

                if (!rtsEnabled) {
                    const curCx = nodeC.x + (nodeAP.x - nodeC.x) * macPacketProgress;
                    macCtx.fillStyle = '#ec4899';
                    macCtx.beginPath();
                    macCtx.arc(curCx, nodeC.y, 6, 0, Math.PI * 2);
                    macCtx.fill();

                    if (macPacketProgress > 0.85) {
                        macCtx.fillStyle = 'rgba(239, 68, 68, 0.4)';
                        macCtx.beginPath();
                        macCtx.arc(nodeAP.x, nodeAP.y, 35, 0, Math.PI * 2);
                        macCtx.fill();
                        macCtx.fillStyle = '#f87171';
                        macCtx.fillText('💥 COLLISION!', nodeAP.x, nodeAP.y - 25);
                    }
                } else {
                    macCtx.fillStyle = 'rgba(16, 185, 129, 0.2)';
                    macCtx.strokeRect(nodeC.x - 40, nodeC.y - 40, 80, 10);
                    macCtx.fillRect(nodeC.x - 40, nodeC.y - 40, 80 * (1 - macPacketProgress), 10);
                }
            }

            requestAnimationFrame(drawMAC);
        }
        drawMAC();
    </script>
</body>
</html>
"""
    return html

if __name__ == '__main__':
    content = build_animations_html()
    with open('animations.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Generated animations.html successfully ({} bytes)".format(len(content)))
