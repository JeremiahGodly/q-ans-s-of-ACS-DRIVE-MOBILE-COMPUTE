# scratch/apply_multilang_feature.py
# Injects Multi-Language (English, Manglish, Malayalam) Support into scratch/gen_site.py

import os
import sys

GEN_SITE_PATH = "scratch/gen_site.py"

with open(GEN_SITE_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Ensure import of LOCAL_LANG_DEMO
if "from local_language_bank import LOCAL_LANG_DEMO" not in content:
    target = "from lecturer_answers import REPRESENTATIVE_ANSWERS"
    replacement = "from lecturer_answers import REPRESENTATIVE_ANSWERS\nfrom local_language_bank import LOCAL_LANG_DEMO"
    if target in content:
        content = content.replace(target, replacement, 1)
        print("1. Added import for LOCAL_LANG_DEMO")

# 2. Replace render_question_card
old_card_fn_start = "def render_question_card(q, subject_class):"
old_card_fn_end = "def render_module_section(mod, subject_class):"

start_idx = content.find(old_card_fn_start)
end_idx = content.find(old_card_fn_end)

if start_idx == -1 or end_idx == -1:
    print("Error: Could not locate render_question_card boundaries!")
    sys.exit(1)

new_card_fn = '''def render_question_card(q, subject_class):
    qid = q["qid"]
    actual_question = EXAM_QUESTIONS_MAP.get(qid, q["title"])
    marks_badge = f'<span class="badge badge-3m">3 Marks (Short Answer)</span>' if q["marks"] == 3 else f'<span class="badge badge-7m">7/14 Marks (Long Essay / Derivation)</span>'
    duration_sec = 300 if q["marks"] == 3 else 720
    duration_str = "05:00" if q["marks"] == 3 else "12:00"
    subj_prefix = qid.split('-')[0].upper()
    q_num = qid.split('-')[1].replace('q', '')
    card_label = f"{subj_prefix} • Q{q_num} ({q['marks']}M)"
    timer_widget = f\'\'\'<div class="card-timer-widget" id="timer-{qid}" data-duration="{duration_sec}" data-qid="{qid}" data-label="{card_label}">
                <button class="timer-btn timer-toggle-btn" onclick="toggleCardTimer('{qid}')" title="Start exam practice countdown with rhythmic pendulum tick sound">
                    <span class="timer-icon">⏱️</span>
                    <span class="timer-display">{duration_str}</span>
                    <span class="timer-action">Start</span>
                </button>
                <button class="timer-btn timer-reset-btn" onclick="resetCardTimer('{qid}')" title="Reset timer" style="display:none;">🔄</button>
            </div>\'\'\'
    type_badge = f'<span class="badge badge-type">{q["type"]}</span>'
    yt_btn = render_youtube_btn(q["yt_query"], actual_question)
    img_box = render_image_box(q.get("img_path"), q.get("img_caption"))

    # Check for lecturer-refined answers
    rep = REPRESENTATIVE_ANSWERS.get(qid)
    if rep:
        content_html = rep["exam_answer"]
        understand_simply = rep.get("understand_simply")
    else:
        content_html = format_paragraphs(q["answer"])
        understand_simply = None

    demo = LOCAL_LANG_DEMO.get(qid)

    # In-card language switcher
    card_lang_toggle = f\'\'\'
    <div class="card-lang-toggle" data-qid="{qid}">
        <button type="button" class="card-lang-btn active" data-card-lang="en" onclick="setCardLang('{qid}', 'en')" title="Switch this card to English">🇬🇧 EN</button>
        <button type="button" class="card-lang-btn" data-card-lang="manglish" onclick="setCardLang('{qid}', 'manglish')" title="Switch this card to Manglish (Local Tone)">🌴 Manglish</button>
        <button type="button" class="card-lang-btn" data-card-lang="ml" onclick="setCardLang('{qid}', 'ml')" title="ഈ ചോദ്യം മലയാളത്തിൽ കാണുക">🇮🇳 മലയാളം</button>
    </div>
    \'\'\'

    # Title markup with 3 language views
    if demo:
        m_title = demo['manglish']['title']
        ml_title = demo['ml']['title']
        title_html = f\'\'\'
        <h3 class="card-title">
            <span class="lang-view lang-en">{actual_question}</span>
            <span class="lang-view lang-manglish">{m_title}</span>
            <span class="lang-view lang-ml font-ml">{ml_title}</span>
        </h3>
        \'\'\'
    else:
        title_html = f\'\'\'
        <h3 class="card-title">
            <span class="lang-view lang-en">{actual_question}</span>
            <span class="lang-view lang-manglish">{actual_question} <span class="lang-demo-tag">🌴 Manglish preview on key questions</span></span>
            <span class="lang-view lang-ml">{actual_question} <span class="lang-demo-tag">🇮🇳 മലയാളം preview on key questions</span></span>
        </h3>
        \'\'\'

    # Byheart markup with 3 language views
    byheart_en = get_byheart_card_html(qid, q["marks"])
    time_badge = '<span class="byheart-time-badge">⏱️ 5 Mins Writing Time</span>' if q["marks"] == 3 else '<span class="byheart-time-badge">⏱️ 12 Mins Writing Time</span>'

    if demo:
        # Manglish Byheart
        m_rem = demo['manglish']['remember_this']
        m_icon = "⚡" if "Equation" in m_rem['title'] else "📌"
        m_eq_html = f'<div class="byheart-eq">{m_rem["eq"]}</div>' if m_rem.get("eq") else ""
        byheart_manglish = f\'\'\'
        <div class="byheart-card">
            <div class="byheart-header">
                <div class="byheart-title-group">
                    <span class="byheart-icon">{m_icon}</span>
                    <span class="byheart-title">{m_rem['title']}</span>
                </div>
                <div class="byheart-badges-group">
                    {time_badge}
                    <span class="byheart-badge">🌴 Manglish Tone</span>
                </div>
            </div>
            <div class="byheart-body">
                {m_eq_html}
                <p class="byheart-text">{m_rem['text']}</p>
            </div>
        </div>
        \'\'\'

        # Malayalam Byheart
        ml_rem = demo['ml']['remember_this']
        ml_icon = "⚡" if ("സമവാക്യം" in ml_rem['title'] or "Equation" in ml_rem['title']) else "📌"
        ml_eq_html = f'<div class="byheart-eq">{ml_rem["eq"]}</div>' if ml_rem.get("eq") else ""
        byheart_ml = f\'\'\'
        <div class="byheart-card font-ml">
            <div class="byheart-header">
                <div class="byheart-title-group">
                    <span class="byheart-icon">{ml_icon}</span>
                    <span class="byheart-title">{ml_rem['title']}</span>
                </div>
                <div class="byheart-badges-group">
                    {time_badge}
                    <span class="byheart-badge">🇮🇳 മലയാളം</span>
                </div>
            </div>
            <div class="byheart-body">
                {ml_eq_html}
                <p class="byheart-text">{ml_rem['text']}</p>
            </div>
        </div>
        \'\'\'

        byheart_block = f\'\'\'
        <div class="lang-view lang-en">{byheart_en}</div>
        <div class="lang-view lang-manglish">{byheart_manglish}</div>
        <div class="lang-view lang-ml">{byheart_ml}</div>
        \'\'\'
    else:
        byheart_block = f\'\'\'
        <div class="lang-view lang-en">{byheart_en}</div>
        <div class="lang-view lang-manglish">{byheart_en}</div>
        <div class="lang-view lang-ml">{byheart_en}</div>
        \'\'\'

    # Section A (Exam-Ready Answer) markup
    if demo:
        exam_section = f\'\'\'
        <!-- English View -->
        <div class="lang-view lang-en">
            <div class="answer-section">
                <div class="answer-section-header">
                    <h4 class="answer-section-title"><span class="section-tag">Section A</span> Exam-Ready Answer</h4>
                </div>
                <div class="exam-ready-content">
                    {content_html}
                </div>
            </div>
        </div>

        <!-- Manglish View -->
        <div class="lang-view lang-manglish">
            <div class="answer-section">
                <div class="answer-section-header">
                    <h4 class="answer-section-title"><span class="section-tag section-tag-manglish">🌴 Manglish</span> Local Tone Study Guide</h4>
                    <button type="button" class="btn-show-english-ref" onclick="toggleEnglishReference('{qid}')">📄 View English Exam Sheet Text</button>
                </div>
                <div class="exam-ready-content">
                    {demo['manglish']['exam_guide']}
                    <div class="english-reference-drawer" id="eng-ref-{qid}" style="display:none;">
                        <div class="ref-drawer-header">📝 Exact English Text for University Examination:</div>
                        <div class="ref-drawer-content">
                            {content_html}
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Malayalam View -->
        <div class="lang-view lang-ml">
            <div class="answer-section">
                <div class="answer-section-header">
                    <h4 class="answer-section-title"><span class="section-tag section-tag-ml">🇮🇳 മലയാളം</span> പ്രാദേശിക പഠന സഹായി</h4>
                    <button type="button" class="btn-show-english-ref" onclick="toggleEnglishReference('{qid}')">📄 പരീക്ഷാ ഇംഗ്ലീഷ് കാണുക</button>
                </div>
                <div class="exam-ready-content font-ml">
                    {demo['ml']['exam_guide']}
                    <div class="english-reference-drawer" id="eng-ref-ml-{qid}" style="display:none;">
                        <div class="ref-drawer-header">📝 പരീക്ഷയിൽ എഴുതേണ്ട ഇംഗ്ലീഷ് വാചകങ്ങൾ:</div>
                        <div class="ref-drawer-content">
                            {content_html}
                        </div>
                    </div>
                </div>
            </div>
        </div>
        \'\'\'
    else:
        demo_notice_manglish = f\'\'\'
        <div class="demo-fallback-box">
            <span class="fallback-icon">🌴</span>
            <div class="fallback-text">
                <strong>Manglish Demo Mode Active:</strong> Full local campus tone is enabled on key representative questions (<strong>ACS Q1, Q2, Q4b, Q13; Drives Q1, Q3, Q4; Mobile Q1, Q7, Q16, Q28</strong>). Standard English is shown below.
            </div>
        </div>
        \'\'\'
        demo_notice_ml = f\'\'\'
        <div class="demo-fallback-box">
            <span class="fallback-icon">🇮🇳</span>
            <div class="fallback-text">
                <strong>മലയാളം Demo Mode Active:</strong> പ്രാദേശിക പഠന സഹായി തെരഞ്ഞെടുത്ത ചോദ്യങ്ങളിൽ ലഭ്യമാണ് (<strong>ACS Q1, Q2, Q4b, Q13; Drives Q1, Q3, Q4; Mobile Q1, Q7, Q16, Q28</strong>). ഈ ചോദ്യത്തിന് ഇംഗ്ലീഷ് താഴെ നൽകിയിരിക്കുന്നു.
            </div>
        </div>
        \'\'\'
        exam_section = f\'\'\'
        <div class="lang-view lang-en">
            <div class="answer-section">
                <div class="answer-section-header">
                    <h4 class="answer-section-title"><span class="section-tag">Section A</span> Exam-Ready Answer</h4>
                </div>
                <div class="exam-ready-content">
                    {content_html}
                </div>
            </div>
        </div>

        <div class="lang-view lang-manglish">
            {demo_notice_manglish}
            <div class="answer-section">
                <div class="answer-section-header">
                    <h4 class="answer-section-title"><span class="section-tag">Section A</span> Exam-Ready Answer</h4>
                </div>
                <div class="exam-ready-content">
                    {content_html}
                </div>
            </div>
        </div>

        <div class="lang-view lang-ml">
            {demo_notice_ml}
            <div class="answer-section">
                <div class="answer-section-header">
                    <h4 class="answer-section-title"><span class="section-tag">Section A</span> Exam-Ready Answer</h4>
                </div>
                <div class="exam-ready-content">
                    {content_html}
                </div>
            </div>
        </div>
        \'\'\'

    # Section B (Understand It Simply) markup
    if demo:
        understand_box = f\'\'\'
        <!-- English Analogy -->
        <div class="lang-view lang-en">
            <details class="understand-simply-drawer">
                <summary class="understand-simply-summary">
                    <div class="drawer-title-group">
                        <span class="drawer-icon">💡</span>
                        <span class="drawer-title"><strong>Understand It Simply</strong> &mdash; Intuitive Explanation &amp; Analogy</span>
                    </div>
                    <div class="drawer-meta-group">
                        <span class="drawer-badge">Learning Aid</span>
                        <span class="drawer-chevron">▼</span>
                    </div>
                </summary>
                <div class="understand-simply-body">
                    {understand_simply if understand_simply else ""}
                </div>
            </details>
        </div>

        <!-- Manglish Analogy -->
        <div class="lang-view lang-manglish">
            <details class="understand-simply-drawer" open>
                <summary class="understand-simply-summary">
                    <div class="drawer-title-group">
                        <span class="drawer-icon">💡</span>
                        <span class="drawer-title"><strong>Understand It Simply (Manglish)</strong> &mdash; Local Campus Analogy</span>
                    </div>
                    <div class="drawer-meta-group">
                        <span class="drawer-badge drawer-badge-manglish">🌴 Local Tone</span>
                        <span class="drawer-chevron">▼</span>
                    </div>
                </summary>
                <div class="understand-simply-body">
                    {demo['manglish']['understand_simply']}
                </div>
            </details>
        </div>

        <!-- Malayalam Analogy -->
        <div class="lang-view lang-ml">
            <details class="understand-simply-drawer font-ml" open>
                <summary class="understand-simply-summary">
                    <div class="drawer-title-group">
                        <span class="drawer-icon">💡</span>
                        <span class="drawer-title"><strong>ലളിതമായി മനസ്സിലാക്കാം</strong> &mdash; പ്രാദേശിക ഉദാഹരണം</span>
                    </div>
                    <div class="drawer-meta-group">
                        <span class="drawer-badge drawer-badge-ml">🇮🇳 മലയാളം</span>
                        <span class="drawer-chevron">▼</span>
                    </div>
                </summary>
                <div class="understand-simply-body font-ml">
                    {demo['ml']['understand_simply']}
                </div>
            </details>
        </div>
        \'\'\'
    else:
        if understand_simply:
            u_drawer = f\'\'\'
            <details class="understand-simply-drawer">
                <summary class="understand-simply-summary">
                    <div class="drawer-title-group">
                        <span class="drawer-icon">💡</span>
                        <span class="drawer-title"><strong>Understand It Simply</strong> &mdash; Intuitive Explanation &amp; Analogy</span>
                    </div>
                    <div class="drawer-meta-group">
                        <span class="drawer-badge">Learning Aid</span>
                        <span class="drawer-chevron">▼</span>
                    </div>
                </summary>
                <div class="understand-simply-body">
                    {understand_simply}
                </div>
            </details>
            \'\'\'
            understand_box = f\'\'\'
            <div class="lang-view lang-en">{u_drawer}</div>
            <div class="lang-view lang-manglish">{u_drawer}</div>
            <div class="lang-view lang-ml">{u_drawer}</div>
            \'\'\'
        else:
            understand_box = ""

    return f"""
    <article class="question-card {subject_class}" id="{qid}" data-marks="{q['marks']}" data-title="{html.escape(actual_question.lower())}">
        <header class="card-header">
            <div class="card-badges">
                {marks_badge}
                {timer_widget}
                {type_badge}
                <span class="badge badge-qid">ID: {qid.upper()}</span>
            </div>
            {title_html}
            <div class="card-action-bar">
                {card_lang_toggle}
                {yt_btn}
                <button class="btn-toggle-answer" onclick="toggleAnswerCard('{qid}')" title="Toggle answer visibility">
                    <span class="toggle-icon">▲</span>
                    <span class="toggle-text">Hide Answer</span>
                </button>
            </div>
        </header>
        <div class="card-body">
            {byheart_block}
            {exam_section}
            {img_box}
            {understand_box}
        </div>
    </article>
    """\n\n'''

content = content[:start_idx] + new_card_fn + content[end_idx:]
print("2. Replaced render_question_card function successfully.")

# 3. Add Language Switcher CSS
css_lang_rules = """
/* =========================================================================
   Language & Tone Switching CSS Rules (English, Manglish, Malayalam)
   ========================================================================= */
.font-ml {
    font-family: 'Noto Sans Malayalam', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    line-height: 1.75;
}

/* Visibility Rules: Default (English) */
html:not([data-lang]) .lang-manglish,
html:not([data-lang]) .lang-ml,
html[data-lang="en"] .lang-manglish,
html[data-lang="en"] .lang-ml {
    display: none !important;
}

html:not([data-lang]) .lang-en,
html[data-lang="en"] .lang-en {
    display: block;
}
html:not([data-lang]) span.lang-en,
html[data-lang="en"] span.lang-en {
    display: inline;
}

/* Visibility Rules: Manglish Mode */
html[data-lang="manglish"] .lang-en,
html[data-lang="manglish"] .lang-ml {
    display: none !important;
}
html[data-lang="manglish"] .lang-manglish {
    display: block;
}
html[data-lang="manglish"] span.lang-manglish {
    display: inline;
}

/* Visibility Rules: Malayalam (മലയാളം) Mode */
html[data-lang="ml"] .lang-en,
html[data-lang="ml"] .lang-manglish {
    display: none !important;
}
html[data-lang="ml"] .lang-ml {
    display: block;
}
html[data-lang="ml"] span.lang-ml {
    display: inline;
}

/* Per-Card Overrides */
article.question-card[data-card-lang="en"] .lang-manglish,
article.question-card[data-card-lang="en"] .lang-ml {
    display: none !important;
}
article.question-card[data-card-lang="en"] .lang-en {
    display: block !important;
}
article.question-card[data-card-lang="en"] span.lang-en {
    display: inline !important;
}

article.question-card[data-card-lang="manglish"] .lang-en,
article.question-card[data-card-lang="manglish"] .lang-ml {
    display: none !important;
}
article.question-card[data-card-lang="manglish"] .lang-manglish {
    display: block !important;
}
article.question-card[data-card-lang="manglish"] span.lang-manglish {
    display: inline !important;
}

article.question-card[data-card-lang="ml"] .lang-en,
article.question-card[data-card-lang="ml"] .lang-manglish {
    display: none !important;
}
article.question-card[data-card-lang="ml"] .lang-ml {
    display: block !important;
}
article.question-card[data-card-lang="ml"] span.lang-ml {
    display: inline !important;
}

/* Global Language Switcher UI */
.lang-switcher-wrapper {
    display: flex;
    align-items: center;
    background: var(--bg-surface);
    border: 1px solid var(--border-subtle);
    border-radius: 9px;
    padding: 0.2rem;
    gap: 0.15rem;
}

.lang-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    background: transparent;
    border: none;
    color: var(--text-muted);
    font-size: 0.8rem;
    font-weight: 500;
    padding: 0.35rem 0.65rem;
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.2s ease;
    white-space: nowrap;
}

.lang-btn:hover {
    color: var(--text-main);
    background: var(--bg-card-hover);
}

.lang-btn.active {
    background: var(--bg-card);
    color: var(--border-focus);
    font-weight: 600;
    box-shadow: 0 1px 4px var(--card-shadow);
}

.lang-badge {
    font-size: 0.62rem;
    background: rgba(16, 185, 129, 0.2);
    color: #34d399;
    padding: 0.08rem 0.32rem;
    border-radius: 4px;
    font-weight: 700;
    text-transform: uppercase;
}

/* Card-level Language Switcher */
.card-lang-toggle {
    display: inline-flex;
    align-items: center;
    background: var(--bg-base);
    border: 1px solid var(--border-subtle);
    border-radius: 7px;
    padding: 0.15rem;
    gap: 0.15rem;
}

.card-lang-btn {
    display: inline-flex;
    align-items: center;
    background: transparent;
    border: none;
    color: var(--text-muted);
    font-size: 0.72rem;
    font-weight: 500;
    padding: 0.22rem 0.5rem;
    border-radius: 5px;
    cursor: pointer;
    transition: all 0.15s ease;
}

.card-lang-btn:hover {
    color: var(--text-main);
    background: var(--bg-card-hover);
}

.card-lang-btn.active {
    background: var(--bg-card);
    color: var(--border-focus);
    font-weight: 600;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
}

/* Local Language Study Guide Styling */
.local-lang-guide {
    font-size: 0.95rem;
    line-height: 1.68;
}

.lang-guide-banner {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    background: rgba(16, 185, 129, 0.08);
    border: 1px solid rgba(16, 185, 129, 0.25);
    border-radius: 8px;
    padding: 0.55rem 0.85rem;
    margin-bottom: 1.1rem;
    font-size: 0.85rem;
}

.lang-guide-banner p {
    margin: 0;
    color: var(--text-body);
}

.guide-badge {
    display: inline-block;
    background: #10b981;
    color: #ffffff;
    font-size: 0.72rem;
    font-weight: 700;
    padding: 0.2rem 0.55rem;
    border-radius: 5px;
    white-space: nowrap;
}

.section-tag-manglish {
    background: rgba(16, 185, 129, 0.2) !important;
    color: #10b981 !important;
}

.section-tag-ml {
    background: rgba(245, 158, 11, 0.2) !important;
    color: #f59e0b !important;
}

.drawer-badge-manglish {
    background: rgba(16, 185, 129, 0.2);
    color: #34d399;
}

.drawer-badge-ml {
    background: rgba(245, 158, 11, 0.2);
    color: #fbbf24;
}

.math-block-highlight {
    background: rgba(0, 0, 0, 0.2);
    border-left: 3px solid var(--border-focus);
    padding: 0.5rem 0.8rem;
    border-radius: 0 6px 6px 0;
    margin: 0.75rem 0;
}

.exam-tip-box {
    background: rgba(245, 158, 11, 0.08);
    border: 1px solid rgba(245, 158, 11, 0.25);
    border-radius: 7px;
    padding: 0.6rem 0.85rem;
    font-size: 0.86rem;
    margin-top: 1rem;
    color: var(--text-body);
}

/* English Reference Drawer inside Manglish/Malayalam */
.btn-show-english-ref {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    background: var(--bg-card);
    border: 1px solid var(--border-subtle);
    color: var(--text-muted);
    font-size: 0.75rem;
    font-weight: 500;
    padding: 0.28rem 0.65rem;
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.2s ease;
    margin-left: auto;
}

.btn-show-english-ref:hover {
    color: var(--text-main);
    border-color: var(--border-focus);
    background: var(--bg-card-hover);
}

.english-reference-drawer {
    margin-top: 1.1rem;
    background: rgba(0, 0, 0, 0.2);
    border: 1px dashed var(--border-subtle);
    border-radius: 8px;
    padding: 0.9rem 1.1rem;
}

.ref-drawer-header {
    font-size: 0.78rem;
    font-weight: 600;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.03em;
    margin-bottom: 0.75rem;
    border-bottom: 1px solid var(--border-subtle);
    padding-bottom: 0.35rem;
}

/* Demo fallback banner for non-demo cards */
.demo-fallback-box {
    display: flex;
    align-items: flex-start;
    gap: 0.65rem;
    background: rgba(56, 189, 248, 0.08);
    border: 1px solid rgba(56, 189, 248, 0.2);
    border-radius: 8px;
    padding: 0.65rem 0.9rem;
    margin-bottom: 1rem;
    font-size: 0.83rem;
    color: var(--text-body);
    line-height: 1.5;
}

.fallback-icon {
    font-size: 1.15rem;
    line-height: 1;
}

.lang-demo-tag {
    font-size: 0.7rem;
    font-weight: 500;
    color: #34d399;
    margin-left: 0.45rem;
    background: rgba(16, 185, 129, 0.15);
    padding: 0.1rem 0.35rem;
    border-radius: 4px;
}

@media (max-width: 960px) {
    .lang-btn .lang-name {
        display: none;
    }
    .lang-btn {
        padding: 0.32rem 0.45rem;
    }
}
"""

if "Language & Tone Switching CSS Rules" not in content:
    # insert before FLOATING_TIMER_HTML =
    timer_pos = content.find("FLOATING_TIMER_HTML =")
    if timer_pos != -1:
        # find the end of CSS_STYLES string before timer_pos
        quote_pos = content.rfind('"""', 0, timer_pos)
        content = content[:quote_pos] + css_lang_rules + '\n"""\n\n' + content[timer_pos:]
        print("3. Injected Multi-Language CSS rules into CSS_STYLES.")

# 4. Add Language Switcher JS
js_lang_code = """
// =========================================================================
// Language & Tone Switching (English, Manglish, Malayalam)
// =========================================================================
const LANG_STORAGE_KEY = 'ktu_portal_lang';

function setGlobalLang(lang) {
    if (!lang) lang = 'en';
    document.documentElement.setAttribute('data-lang', lang);
    try {
        localStorage.setItem(LANG_STORAGE_KEY, lang);
    } catch (e) {}

    // Update global buttons in header
    const globalBtns = document.querySelectorAll('.lang-btn');
    globalBtns.forEach(btn => {
        const val = btn.getAttribute('data-lang-value');
        if (val === lang) {
            btn.classList.add('active');
            btn.setAttribute('aria-checked', 'true');
        } else {
            btn.classList.remove('active');
            btn.setAttribute('aria-checked', 'false');
        }
    });

    // Reset card-specific overrides to match global
    const cards = document.querySelectorAll('.question-card');
    cards.forEach(card => {
        card.removeAttribute('data-card-lang');
        const cardBtns = card.querySelectorAll('.card-lang-btn');
        cardBtns.forEach(btn => {
            const val = btn.getAttribute('data-card-lang');
            if (val === lang) {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });
    });
}

function setCardLang(qid, lang) {
    const card = document.getElementById(qid);
    if (!card) return;
    card.setAttribute('data-card-lang', lang);
    const cardBtns = card.querySelectorAll('.card-lang-btn');
    cardBtns.forEach(btn => {
        const val = btn.getAttribute('data-card-lang');
        if (val === lang) {
            btn.classList.add('active');
        } else {
            btn.classList.remove('active');
        }
    });
}

function toggleEnglishReference(qid) {
    const refDrawer = document.getElementById('eng-ref-' + qid) || document.getElementById('eng-ref-ml-' + qid);
    if (!refDrawer) return;
    if (refDrawer.style.display === 'none' || refDrawer.style.display === '') {
        refDrawer.style.display = 'block';
    } else {
        refDrawer.style.display = 'none';
    }
}

function initLanguageSwitcher() {
    let savedLang = 'en';
    try {
        savedLang = localStorage.getItem(LANG_STORAGE_KEY) || 'en';
    } catch (e) {}
    setGlobalLang(savedLang);

    const globalBtns = document.querySelectorAll('.lang-btn');
    globalBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const val = btn.getAttribute('data-lang-value');
            setGlobalLang(val);
        });
    });
}
"""

if "initLanguageSwitcher" not in content:
    init_portal_target = "function initPortal() {\n    initThemeSwitcher();\n    updateSoundUI();\n}"
    init_portal_replacement = "function initPortal() {\n    initThemeSwitcher();\n    initLanguageSwitcher();\n    updateSoundUI();\n}"
    
    if init_portal_target in content:
        content = content.replace(init_portal_target, js_lang_code + "\n" + init_portal_replacement, 1)
        print("4. Injected Multi-Language JS functions and wired into initPortal().")
    else:
        print("Warning: Could not find exact initPortal definition.")

# 5. Update INDEX_TEMPLATE
# 5a. Add Noto Sans Malayalam font
font_old = "family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap"
font_new = "family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&family=Noto+Sans+Malayalam:wght@400;500;600;700&display=swap"
content = content.replace(font_old, font_new)

# 5b. Add lang preload script in INDEX_TEMPLATE
preload_old = """    <script>
        (function() {
            const savedTheme = localStorage.getItem('ktu_portal_theme') || 'dark';
            document.documentElement.setAttribute('data-theme', savedTheme);
        })();
    </script>"""

preload_new = """    <script>
        (function() {
            const savedTheme = localStorage.getItem('ktu_portal_theme') || 'dark';
            document.documentElement.setAttribute('data-theme', savedTheme);
            const savedLang = localStorage.getItem('ktu_portal_lang') || 'en';
            document.documentElement.setAttribute('data-lang', savedLang);
        })();
    </script>"""

content = content.replace(preload_old, preload_new)

# 5c. Add global lang switcher in INDEX_TEMPLATE
header_target = """            <!-- Theme Switcher Controls (Night, Day, Sage) -->
            <div class="theme-switcher-wrapper" role="radiogroup" aria-label="Reading &amp; Study Theme Selector">"""

header_replacement = """            <!-- Tone / Language Switcher Controls (English, Manglish, Malayalam) -->
            <div class="lang-switcher-wrapper" role="radiogroup" aria-label="Language &amp; Tone Selector">
                <button class="lang-btn active" data-lang-value="en" title="English: University Standard Exam Answers" aria-label="English">
                    <span class="lang-flag">🇬🇧</span>
                    <span class="lang-name">English</span>
                </button>
                <button class="lang-btn" data-lang-value="manglish" title="Manglish: Malayalam in English text with local campus tone" aria-label="Manglish">
                    <span class="lang-flag">🌴</span>
                    <span class="lang-name">Manglish</span>
                    <span class="lang-badge">Demo</span>
                </button>
                <button class="lang-btn" data-lang-value="ml" title="മലയാളം: പ്രാദേശിക സംഭാഷണ ശൈലി" aria-label="Malayalam">
                    <span class="lang-flag">🇮🇳</span>
                    <span class="lang-name">മലയാളം</span>
                    <span class="lang-badge">Demo</span>
                </button>
            </div>

            <!-- Theme Switcher Controls (Night, Day, Sage) -->
            <div class="theme-switcher-wrapper" role="radiogroup" aria-label="Reading &amp; Study Theme Selector">"""

if header_target in content:
    content = content.replace(header_target, header_replacement, 1)
    print("5. Added Global Language Switcher to INDEX_TEMPLATE.")

# 6. Update generate_standalone_page
standalone_target = """            <!-- Header Theme Switcher Palette Selector -->
            <div class="theme-palette-wrapper">"""

standalone_replacement = """            <!-- Tone / Language Switcher Controls -->
            <div class="lang-switcher-wrapper" role="radiogroup" aria-label="Language &amp; Tone Selector">
                <button class="lang-btn active" data-lang-value="en" title="English: University Standard Exam Answers" aria-label="English">
                    <span class="lang-flag">🇬🇧</span>
                    <span class="lang-name">English</span>
                </button>
                <button class="lang-btn" data-lang-value="manglish" title="Manglish: Malayalam in English text with local campus tone" aria-label="Manglish">
                    <span class="lang-flag">🌴</span>
                    <span class="lang-name">Manglish</span>
                    <span class="lang-badge">Demo</span>
                </button>
                <button class="lang-btn" data-lang-value="ml" title="മലയാളം: പ്രാദേശിക സംഭാഷണ ശൈലി" aria-label="Malayalam">
                    <span class="lang-flag">🇮🇳</span>
                    <span class="lang-name">മലയാളം</span>
                    <span class="lang-badge">Demo</span>
                </button>
            </div>

            <!-- Header Theme Switcher Palette Selector -->
            <div class="theme-palette-wrapper">"""

if standalone_target in content:
    content = content.replace(standalone_target, standalone_replacement, 1)
    print("6. Added Global Language Switcher to generate_standalone_page.")

with open(GEN_SITE_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated scratch/gen_site.py successfully!")
