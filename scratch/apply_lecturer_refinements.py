# scratch/apply_lecturer_refinements.py
# Applies lecturer-level answers, structured Exam-Ready Section A,
# and collapsible Understand It Simply Section B to gen_site.py

import re

with open('scratch/gen_site.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Add import for REPRESENTATIVE_ANSWERS
if 'from lecturer_answers import REPRESENTATIVE_ANSWERS' not in code:
    code = code.replace(
        'from exam_questions import EXAM_QUESTIONS_MAP',
        'from exam_questions import EXAM_QUESTIONS_MAP\nfrom lecturer_answers import REPRESENTATIVE_ANSWERS'
    )
    print("Added import for REPRESENTATIVE_ANSWERS.")

# 2. Update render_image_box
new_render_image_box = """def render_image_box(img_path, img_caption):
    if not img_path:
        return ""
    exists = os.path.exists(img_path)
    if exists:
        return f\"\"\"
        <div class="diagram-card has-real-image">
            <div class="diagram-wrapper">
                <img src="{img_path}" alt="{html.escape(img_caption)}" class="diagram-img" loading="lazy">
            </div>
            <p class="diagram-caption"><strong>Figure:</strong> {html.escape(img_caption)}</p>
        </div>
        \"\"\"
    else:
        return f\"\"\"
        <div class="diagram-notice missing-notice">
            <span class="notice-icon">ℹ️</span>
            <span class="notice-text"><strong>Schematic:</strong> {html.escape(img_caption)} &mdash; <em>(Refer to textbook/lecture notes)</em></span>
        </div>
        \"\"\""""

old_render_image_box_pattern = re.compile(r'def render_image_box\(img_path, img_caption\):.*?(?=def render_youtube_btn)', re.DOTALL)
code = old_render_image_box_pattern.sub(new_render_image_box + "\n\n", code, count=1)
print("Updated render_image_box.")

# 3. Update render_question_card
new_render_question_card = """def render_question_card(q, subject_class):
    qid = q["qid"]
    actual_question = EXAM_QUESTIONS_MAP.get(qid, q["title"])
    marks_badge = f'<span class="badge badge-3m">3 Marks (Short Answer)</span>' if q["marks"] == 3 else f'<span class="badge badge-7m">7/14 Marks (Long Essay / Derivation)</span>'
    duration_sec = 300 if q["marks"] == 3 else 720
    duration_str = "05:00" if q["marks"] == 3 else "12:00"
    subj_prefix = qid.split('-')[0].upper()
    q_num = qid.split('-')[1].replace('q', '')
    card_label = f"{subj_prefix} • Q{q_num} ({q['marks']}M)"
    timer_widget = f'''<div class="card-timer-widget" id="timer-{qid}" data-duration="{duration_sec}" data-qid="{qid}" data-label="{card_label}">
                <button class="timer-btn timer-toggle-btn" onclick="toggleCardTimer('{qid}')" title="Start exam practice countdown with rhythmic pendulum tick sound">
                    <span class="timer-icon">⏱️</span>
                    <span class="timer-display">{duration_str}</span>
                    <span class="timer-action">Start</span>
                </button>
                <button class="timer-btn timer-reset-btn" onclick="resetCardTimer('{qid}')" title="Reset timer" style="display:none;">🔄</button>
            </div>'''
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

    understand_box = ""
    if understand_simply:
        understand_box = f'''
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
        '''

    byheart_box = get_byheart_card_html(qid, q["marks"])

    return f\"\"\"
    <article class="question-card {subject_class}" id="{qid}" data-marks="{q['marks']}" data-title="{html.escape(actual_question.lower())}">
        <header class="card-header">
            <div class="card-badges">
                {marks_badge}
                {timer_widget}
                {type_badge}
                <span class="badge badge-qid">ID: {qid.upper()}</span>
            </div>
            <h3 class="card-title">{actual_question}</h3>
            <div class="card-action-bar">
                {yt_btn}
                <button class="btn-toggle-answer" onclick="toggleAnswerCard('{qid}')" title="Toggle answer visibility">
                    <span class="toggle-icon">▲</span>
                    <span class="toggle-text">Hide Answer</span>
                </button>
            </div>
        </header>
        <div class="card-body">
            {byheart_box}
            <div class="answer-section">
                <div class="answer-section-header">
                    <h4 class="answer-section-title"><span class="section-tag">Section A</span> Exam-Ready Answer</h4>
                </div>
                <div class="exam-ready-content">
                    {content_html}
                </div>
            </div>
            {img_box}
            {understand_box}
        </div>
    </article>
    \"\"\""""

old_render_card_pattern = re.compile(r'def render_question_card\(q, subject_class\):.*?(?=def render_module_section)', re.DOTALL)
code = old_render_card_pattern.sub(new_render_question_card + "\n\n", code, count=1)
print("Updated render_question_card.")

# 4. Add CSS styles for Section A, Section B, tables, and clean diagrams to CSS_STYLES
new_css = """
/* =========================================================================
   Section A & Section B: Exam-Ready Answer and Understand It Simply Drawer
   ========================================================================= */
.answer-section-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 0.85rem;
    padding-bottom: 0.4rem;
    border-bottom: 1.5px solid var(--border-subtle);
}

.answer-section-title {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 0.98rem;
    font-weight: 700;
    color: var(--text-main);
    margin: 0;
}

.section-tag {
    font-size: 0.72rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    padding: 0.15rem 0.5rem;
    border-radius: 4px;
    background: rgba(56, 189, 248, 0.15);
    color: var(--border-focus);
    border: 1px solid rgba(56, 189, 248, 0.35);
}

.exam-ready-content {
    color: var(--text-body);
    font-size: 0.94rem;
    line-height: 1.68;
}
.exam-ready-content p {
    margin-bottom: 0.85rem;
}
.exam-ready-content ol, .exam-ready-content ul {
    margin: 0.5rem 0 1rem 1.4rem;
    padding: 0;
}
.exam-ready-content li {
    margin-bottom: 0.45rem;
}

/* Responsive Exam Comparison Table */
.exam-table-container {
    width: 100%;
    overflow-x: auto;
    margin: 0.85rem 0 1.25rem 0;
    border-radius: 8px;
    border: 1px solid var(--border-subtle);
    background: var(--bg-card);
    -webkit-overflow-scrolling: touch;
}

.exam-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.88rem;
    text-align: left;
    margin: 0.85rem 0 1.25rem 0;
    border-radius: 8px;
    overflow: hidden;
    border: 1px solid var(--border-subtle);
}

.exam-table th {
    background: var(--bg-surface);
    color: var(--text-main);
    font-weight: 700;
    padding: 0.65rem 0.85rem;
    border-bottom: 2px solid var(--border-subtle);
    border-right: 1px solid var(--border-subtle);
}
.exam-table th:last-child {
    border-right: none;
}

.exam-table td {
    padding: 0.65rem 0.85rem;
    border-bottom: 1px solid var(--border-subtle);
    border-right: 1px solid var(--border-subtle);
    color: var(--text-body);
    vertical-align: top;
    background: var(--bg-card);
}
.exam-table td:last-child {
    border-right: none;
}

.exam-table tr:last-child td {
    border-bottom: none;
}

.exam-table tr:hover td {
    background: var(--bg-card-hover);
}

/* Clean Professional Diagram Card */
.diagram-card {
    margin-top: 1.2rem;
    background: var(--bg-card);
    border: 1px solid var(--border-subtle);
    border-radius: 12px;
    padding: 1.25rem;
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    transition: border-color 0.2s ease;
}
.diagram-card:hover {
    border-color: var(--border-focus);
}

.diagram-card .diagram-img {
    display: block;
    max-width: 100%;
    height: auto;
    border-radius: 8px;
    border: 1px solid var(--border-subtle);
    margin: 0 auto;
    background: #ffffff;
    box-shadow: 0 4px 16px var(--card-shadow);
}

.diagram-caption {
    font-size: 0.84rem;
    color: var(--text-muted);
    text-align: center;
    margin: 0;
    font-style: normal;
}
.diagram-caption strong {
    color: var(--text-main);
}

.diagram-notice {
    margin-top: 1rem;
    padding: 0.65rem 1rem;
    border-radius: 8px;
    background: var(--bg-card);
    border: 1px dashed var(--border-subtle);
    font-size: 0.82rem;
    color: var(--text-muted);
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

/* Section B: Understand It Simply Collapsible Drawer */
.understand-simply-drawer {
    margin-top: 1.25rem;
    border: 1px solid rgba(245, 158, 11, 0.3);
    background: rgba(245, 158, 11, 0.04);
    border-radius: 10px;
    transition: all 0.25s ease;
}

.understand-simply-drawer[open] {
    border-color: rgba(245, 158, 11, 0.55);
    background: rgba(245, 158, 11, 0.07);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
}

.understand-simply-summary {
    cursor: pointer;
    list-style: none;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.75rem 1rem;
    font-size: 0.88rem;
    font-weight: 600;
    color: #f59e0b;
    user-select: none;
}

.understand-simply-summary::-webkit-details-marker {
    display: none;
}

.understand-simply-summary:hover {
    color: #fbbf24;
}

.drawer-title-group {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
}

.drawer-meta-group {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
}

.drawer-icon {
    font-size: 1.15rem;
    line-height: 1;
}

.drawer-badge {
    font-size: 0.68rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    padding: 0.12rem 0.45rem;
    border-radius: 4px;
    background: rgba(245, 158, 11, 0.2);
    color: #f59e0b;
}

.drawer-chevron {
    font-size: 0.75rem;
    transition: transform 0.25s ease;
}

.understand-simply-drawer[open] .drawer-chevron {
    transform: rotate(180deg);
}

.understand-simply-body {
    padding: 0.85rem 1.15rem 1.15rem 1.15rem;
    border-top: 1px solid rgba(245, 158, 11, 0.2);
    font-size: 0.92rem;
    line-height: 1.65;
    color: var(--text-body);
}

.understand-simply-body p:last-child {
    margin-bottom: 0;
}

/* Light Theme Adjustments */
[data-theme="light"] .understand-simply-drawer {
    background: #fffdf5;
    border-color: #fcd34d;
}
[data-theme="light"] .understand-simply-summary {
    color: #b45309;
}
[data-theme="light"] .drawer-badge {
    background: #fde68a;
    color: #92400e;
}
[data-theme="light"] .understand-simply-body {
    border-top-color: #fde68a;
    color: #451a03;
}
[data-theme="light"] .exam-table th {
    background: #f1f5f9;
    color: #0f172a;
}
[data-theme="light"] .exam-table td {
    background: #ffffff;
    color: #1e293b;
}
[data-theme="light"] .exam-table tr:hover td {
    background: #f8fafc;
}
"""

# Inject before the closing of CSS_STYLES
code = code.replace(
    '/* Question Card Flash Highlight on Jump */',
    new_css + '\n/* Question Card Flash Highlight on Jump */'
)
print("Injected new CSS rules into CSS_STYLES.")

with open('scratch/gen_site.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("gen_site.py successfully updated with lecturer refinements!")
