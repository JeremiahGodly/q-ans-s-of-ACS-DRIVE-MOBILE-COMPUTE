# -*- coding: utf-8 -*-
"""
Updater script for scratch/gen_site.py
- Replaces position: sticky with position: relative so header sits on top and does not follow scroll
- Makes the header sleek and compact
- Adds floating Back to Top button with smooth scroll
"""

with open("scratch/gen_site.py", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update site-header CSS
old_header = """/* Header & Navigation Bar */
header.site-header {
    position: sticky;
    top: 0;
    z-index: 100;
    background: rgba(13, 19, 34, 0.94);
    backdrop-filter: blur(14px);
    border-bottom: 1px solid var(--border-subtle);
    padding: 1rem 2rem;
    display: flex;
    flex-direction: column;
    gap: 1rem;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
}"""

new_header = """/* Header & Navigation Bar - Stuck at Top of Page, Does NOT Follow Scroll */
header.site-header {
    position: relative; /* Positioned at top of document; does NOT follow scroll */
    z-index: 10;
    background: var(--bg-surface);
    border-bottom: 1px solid var(--border-subtle);
    padding: 0.65rem 1.75rem;
    display: flex;
    flex-direction: column;
    gap: 0.55rem;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
}"""

assert old_header in code, "old_header not found"
code = code.replace(old_header, new_header)

# 2. Compact logo and tabs
old_brand = """.brand-logo-icon {
    width: 44px;
    height: 44px;
    background: linear-gradient(135deg, #6366f1, #38bdf8);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.4rem;
    box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4);
}

.brand-text h1 {
    font-size: 1.35rem;
    font-weight: 800;
    letter-spacing: -0.02em;
    background: linear-gradient(90deg, #f8fafc, #93c5fd);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.brand-text p {
    font-size: 0.8rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

/* Subject Tab Switcher (3 Pages in One) */
.subject-tabs {
    display: flex;
    background: var(--bg-base);
    padding: 0.35rem;
    border-radius: 14px;
    border: 1px solid var(--border-subtle);
    gap: 0.35rem;
}

.tab-btn {
    background: transparent;
    border: none;
    color: var(--text-muted);
    font-family: var(--font-main);
    font-size: 0.95rem;
    font-weight: 600;
    padding: 0.65rem 1.4rem;
    border-radius: 10px;
    cursor: pointer;
    transition: all 0.25s ease;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    white-space: nowrap;
}"""

new_brand = """.brand-logo-icon {
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
    background: linear-gradient(90deg, #f8fafc, #93c5fd);
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
}"""

assert old_brand in code, "old_brand not found"
code = code.replace(old_brand, new_brand)

# 3. Compact search and filters
old_search = """.search-box-wrapper {
    position: relative;
    flex: 1;
    min-width: 280px;
    max-width: 500px;
}

.search-input {
    width: 100%;
    background: var(--bg-base);
    border: 1px solid var(--border-subtle);
    color: var(--text-main);
    padding: 0.6rem 1rem 0.6rem 2.6rem;
    border-radius: 10px;
    font-family: var(--font-main);
    font-size: 0.9rem;
    outline: none;
    transition: border-color 0.2s, box-shadow 0.2s;
}"""

new_search = """.search-box-wrapper {
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
}"""

assert old_search in code, "old_search not found"
code = code.replace(old_search, new_search)

# 4. Add back-to-top CSS before end of CSS_STYLES
back_to_top_css = """
/* Floating Back to Top Button */
.back-to-top-btn {
    position: fixed;
    bottom: 2rem;
    right: 2rem;
    z-index: 999;
    background: linear-gradient(135deg, #38bdf8, #6366f1);
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
"""

assert ".subject-hero h2 { font-size: 1.75rem; }" in code, "responsive hero not found"
code = code.replace(".subject-hero h2 { font-size: 1.75rem; }\n}", ".subject-hero h2 { font-size: 1.75rem; }\n}" + back_to_top_css)

# 5. Add back to top button in INDEX_TEMPLATE
old_idx_footer = """    <!-- Footer -->
    <footer class="site-footer">"""

new_idx_footer = """    <!-- Floating Back to Top Button -->
    <button class="back-to-top-btn" id="back-to-top" onclick="scrollToTop()" title="Scroll to top of page">
        <span>↑</span> Top
    </button>

    <!-- Footer -->
    <footer class="site-footer">"""

assert old_idx_footer in code, "old_idx_footer not found"
code = code.replace(old_idx_footer, new_idx_footer)

# 6. Add JS scroll listener in JS_SCRIPT
old_js_end = """    const statsPill = document.getElementById('stats-pill');
    if (statsPill) {
        statsPill.innerText = `${visibleCount} Questions Displayed`;
    }
}"""

new_js_end = """    const statsPill = document.getElementById('stats-pill');
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
}"""

assert old_js_end in code, "old_js_end not found"
code = code.replace(old_js_end, new_js_end)

# 7. Add back to top in standalone template
old_standalone_footer = """    <main class="content-container">
        {{INNER_HTML}}
    </main>

    <footer class="site-footer">"""

new_standalone_footer = """    <main class="content-container">
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
    </script>

    <footer class="site-footer">"""

assert old_standalone_footer in code, "old_standalone_footer not found"
code = code.replace(old_standalone_footer, new_standalone_footer)

with open("scratch/gen_site.py", "w", encoding="utf-8") as f:
    f.write(code)

print("scratch/gen_site.py updated successfully!")
