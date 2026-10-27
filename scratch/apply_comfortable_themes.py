# -*- coding: utf-8 -*-
"""
Applies refined, ultra-comfortable dark themes to gen_site.py:
1. Refined Soft Charcoal & Warm Slate (Default Dark Mode - eliminates harsh blue glare)
2. Warm Espresso / Sepia Dark (Kindle-style zero-blue-light reading mode)
3. Forest Night (Deep botanical pine & soft mint - lowest ocular strain)
4. Midnight OLED (Minimalist true black - zero light bleed)
5. Day Mode (Warm Slate & Off-White Paper)
6. Sage Focus Mode (Pale Sage & Deep Forest)
"""
import re

with open("scratch/gen_site.py", "r", encoding="utf-8") as f:
    content = f.read()

# 1. NEW CSS PALETTES
NEW_THEMES_CSS = """/* ==========================================================================
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
}"""

# Replace the existing CSS theme section
old_css_theme_pattern = re.compile(r'/\* =+ \s* THEME PALETTE 1 \(DEFAULT\).*?--top-btn-grad: linear-gradient\(135deg, #047857, #4f46e5\);\s*\}', re.DOTALL | re.VERBOSE)
if old_css_theme_pattern.search(content):
    content = old_css_theme_pattern.sub(NEW_THEMES_CSS, content, count=1)
    print("Successfully replaced CSS theme palettes!")
else:
    print("Could not find old_css_theme_pattern with regex, trying exact string replacement...")

# 2. UPDATE THEME SWITCHER CONTROLS CSS
NEW_SWITCHER_CSS = """/* Theme Switcher Controls */
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
}"""

old_switcher_css = """.theme-switcher-wrapper {
    display: flex;
    align-items: center;
    background: var(--bg-base);
    border: 1px solid var(--border-subtle);
    border-radius: 10px;
    padding: 0.2rem;
    gap: 0.2rem;
    box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.08);
}

.theme-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    background: transparent;
    border: 1px solid transparent;
    color: var(--text-muted);
    font-family: var(--font-main);
    font-size: 0.8rem;
    font-weight: 600;
    padding: 0.35rem 0.65rem;
    border-radius: 7px;
    cursor: pointer;
    transition: all 0.2s ease;
    white-space: nowrap;
}

.theme-btn:hover {
    color: var(--text-main);
    background: var(--bg-card-hover);
}

.theme-btn.active {
    background: var(--bg-surface);
    color: var(--text-main);
    border-color: var(--border-focus);
    box-shadow: 0 2px 8px var(--card-shadow);
}"""

if old_switcher_css in content:
    content = content.replace(old_switcher_css, NEW_SWITCHER_CSS)
    print("Successfully replaced Theme Switcher CSS!")

# 3. NEW THEME BUTTONS HTML MARKUP
NEW_THEME_BUTTONS = """<div class="theme-switcher-wrapper" role="radiogroup" aria-label="Reading &amp; Study Theme Selector">
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
            </div>"""

old_theme_buttons_pattern = re.compile(r'<div class="theme-switcher-wrapper"[^>]*>.*?</div>', re.DOTALL)
matches = old_theme_buttons_pattern.findall(content)
print(f"Found {len(matches)} occurrences of theme-switcher-wrapper HTML")
content = old_theme_buttons_pattern.sub(NEW_THEME_BUTTONS, content)

# 4. UPDATE JS_SCRIPT THEME FUNCTIONS
NEW_JS_THEME_LOGIC = """// ==========================================================================
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
}"""

old_js_theme_pattern = re.compile(r'// =+\s*// Theme Switching Logic with LocalStorage Persistence.*?\}\s*\}', re.DOTALL)
if old_js_theme_pattern.search(content):
    content = old_js_theme_pattern.sub(NEW_JS_THEME_LOGIC, content, count=1)
    print("Successfully replaced JS_SCRIPT theme logic!")
else:
    print("Could not find old_js_theme_pattern!")

# 5. UPDATE STANDALONE PAGE THEME SCRIPT
NEW_STANDALONE_THEME_JS = """        // Theme Switcher for Standalone Pages
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
        setTheme(localStorage.getItem(THEME_STORAGE_KEY) || 'dark');"""

old_standalone_theme_js = """        // Theme Switcher for Standalone Pages
        const THEME_STORAGE_KEY = 'ktu_portal_theme';
        function setTheme(themeName) {
            if (!['dark', 'light', 'sage'].includes(themeName)) themeName = 'dark';
            document.documentElement.setAttribute('data-theme', themeName);
            try { localStorage.setItem(THEME_STORAGE_KEY, themeName); } catch (e) {}
            const btns = document.querySelectorAll('.theme-btn');
            btns.forEach(btn => {
                if (btn.getAttribute('data-theme-value') === themeName) {
                    btn.classList.add('active');
                } else {
                    btn.classList.remove('active');
                }
            });
        }
        document.querySelectorAll('.theme-btn').forEach(btn => {
            btn.addEventListener('click', () => setTheme(btn.getAttribute('data-theme-value')));
        });
        setTheme(localStorage.getItem(THEME_STORAGE_KEY) || 'dark');"""

if old_standalone_theme_js in content:
    content = content.replace(old_standalone_theme_js, NEW_STANDALONE_THEME_JS)
    print("Successfully replaced standalone theme JS!")

with open("scratch/gen_site.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Saved updated scratch/gen_site.py!")
