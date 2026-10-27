# -*- coding: utf-8 -*-
"""
Applies comprehensive mobile-friendly, space-efficient, and responsive display resolution
enhancements to gen_site.py.
"""

with open("scratch/gen_site.py", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update Viewport tag to support safe area insets (notches, dynamic islands)
code = code.replace(
    '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
    '<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">'
)

# 2. Update Subject Tabs in INDEX_TEMPLATE to support full and short labels
old_tabs_html = """            <!-- Subject Switcher Tabs (3 Web Pages in One Index Page) -->
            <nav class="subject-tabs" role="tablist">
                <button class="tab-btn active tab-acs" data-target="view-acs" role="tab" aria-selected="true">
                    <span>📘</span> Advanced Control Systems (EET401)
                </button>
                <button class="tab-btn tab-drive" data-target="view-drive" role="tab" aria-selected="false">
                    <span>⚡</span> Electric Drives (EET413)
                </button>
                <button class="tab-btn tab-mobile" data-target="view-mobile" role="tab" aria-selected="false">
                    <span>📱</span> Mobile Computing (CST415)
                </button>
            </nav>"""

new_tabs_html = """            <!-- Subject Switcher Tabs (3 Web Pages in One Index Page) -->
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
            </nav>"""

if old_tabs_html in code:
    code = code.replace(old_tabs_html, new_tabs_html)
    print("Updated subject tabs HTML with responsive labels!")
else:
    print("Notice: old_tabs_html not matched exactly, checking tabs...")

# 3. Update brand text in INDEX_TEMPLATE to support responsive subtext
old_brand_html = """            <div class="brand-container">
                <div class="brand-logo-icon">⚡</div>
                <div class="brand-text">
                    <h1>KTU Engineering Mastery Portal</h1>
                    <p>7th Semester B.Tech Comprehensive Question & Answer Bank</p>
                </div>
            </div>"""

new_brand_html = """            <div class="brand-container">
                <div class="brand-logo-icon" aria-hidden="true">⚡</div>
                <div class="brand-text">
                    <h1>KTU Mastery Portal</h1>
                    <p class="brand-subtext">7th Sem B.Tech Question Bank</p>
                </div>
            </div>"""

if old_brand_html in code:
    code = code.replace(old_brand_html, new_brand_html)
    print("Updated brand container HTML!")

# 4. Now let's inject comprehensive responsive CSS rules into CSS_STYLES
# Let's inspect the responsive block at the bottom of CSS_STYLES
old_responsive_block = """/* Responsive adjustments */
@media (max-width: 900px) {
    header.site-header { padding: 0.75rem 1rem; }
    .header-top-row { flex-direction: column; align-items: stretch; }
    .brand-container { justify-content: space-between; }
    .subject-tabs { overflow-x: auto; }
    .theme-switcher-wrapper { align-self: flex-end; }
    .question-card { padding: 1.5rem; }
    .subject-hero { padding: 1.75rem; }
    .subject-hero h2 { font-size: 1.75rem; }
}"""

NEW_RESPONSIVE_CSS = """/* ==========================================================================
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
}"""

if old_responsive_block in code:
    code = code.replace(old_responsive_block, NEW_RESPONSIVE_CSS)
    print("Replaced old responsive block with advanced mobile suite!")
else:
    print("Notice: old_responsive_block not matched, searching for @media (max-width: 900px)...")
    idx = code.find("/* Responsive adjustments */")
    if idx != -1:
        end_idx = code.find('"""\n\nJS_SCRIPT')
        code = code[:idx] + NEW_RESPONSIVE_CSS + code[end_idx:]
        print("Replaced responsive CSS block by slice!")

with open("scratch/gen_site.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Saved updated gen_site.py!")
