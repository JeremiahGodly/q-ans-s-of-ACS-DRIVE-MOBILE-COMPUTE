# Python script to update gen_site.py with Web Audio API pendulum tick sound and top-right floating timer widget
import re

with open('scratch/gen_site.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update render_question_card to add data-label
old_render_timer = """    timer_widget = f'''<div class="card-timer-widget" id="timer-{q['qid']}" data-duration="{duration_sec}" data-qid="{q['qid']}">
                <button class="timer-btn timer-toggle-btn" onclick="toggleCardTimer('{q['qid']}')" title="Start exam practice countdown">
                    <span class="timer-icon">⏱️</span>
                    <span class="timer-display">{duration_str}</span>
                    <span class="timer-action">Start</span>
                </button>
                <button class="timer-btn timer-reset-btn" onclick="resetCardTimer('{q['qid']}')" title="Reset timer" style="display:none;">🔄</button>
            </div>'''"""

new_render_timer = """    subj_prefix = q['qid'].split('-')[0].upper()
    q_num = q['qid'].split('-')[1].replace('q', '')
    card_label = f"{subj_prefix} • Q{q_num} ({q['marks']}M)"
    timer_widget = f'''<div class="card-timer-widget" id="timer-{q['qid']}" data-duration="{duration_sec}" data-qid="{q['qid']}" data-label="{card_label}">
                <button class="timer-btn timer-toggle-btn" onclick="toggleCardTimer('{q['qid']}')" title="Start exam practice countdown with rhythmic pendulum tick sound">
                    <span class="timer-icon">⏱️</span>
                    <span class="timer-display">{duration_str}</span>
                    <span class="timer-action">Start</span>
                </button>
                <button class="timer-btn timer-reset-btn" onclick="resetCardTimer('{q['qid']}')" title="Reset timer" style="display:none;">🔄</button>
            </div>'''"""

if old_render_timer in content:
    content = content.replace(old_render_timer, new_render_timer)
    print("Updated render_question_card timer_widget successfully.")
else:
    print("Warning: old_render_timer pattern not found directly.")

# 2. Add Floating Timer CSS to CSS_STYLES
floating_timer_css = """
/* =========================================================================
   Floating Top-Right Countdown Timer Widget with Rhythmic Pendulum
   ========================================================================= */
.floating-timer-widget {
    position: fixed;
    top: 76px;
    right: 22px;
    z-index: 10000;
    min-width: 275px;
    max-width: 320px;
    background: var(--bg-surface);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border: 1.5px solid rgba(16, 185, 129, 0.45);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.45), 0 0 18px rgba(16, 185, 129, 0.22);
    border-radius: 14px;
    padding: 0.85rem 1rem;
    transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.22s ease, box-shadow 0.25s ease, border-color 0.25s ease;
    animation: floatIn 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes floatIn {
    from {
        opacity: 0;
        transform: translateY(-16px) scale(0.96);
    }
    to {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}

.floating-timer-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 0.5rem;
    padding-bottom: 0.45rem;
    border-bottom: 1px solid var(--border-subtle);
}

.floating-timer-title {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    font-size: 0.82rem;
    font-weight: 700;
    color: var(--text-main);
}

.floating-pendulum-icon {
    display: inline-block;
    font-size: 1.25rem;
    line-height: 1;
    transform-origin: 50% 10%;
    transition: transform 0.2s ease;
}

@keyframes pendulumSway {
    0% { transform: rotate(-22deg); }
    50% { transform: rotate(22deg); }
    100% { transform: rotate(-22deg); }
}

.floating-pendulum-icon.swinging {
    animation: pendulumSway 1s ease-in-out infinite alternate;
}

.floating-qid {
    background: var(--bg-card);
    border: 1px solid var(--border-subtle);
    padding: 0.15rem 0.45rem;
    border-radius: 6px;
    font-family: var(--font-mono);
    font-size: 0.74rem;
    color: #10b981;
}

.float-btn {
    border: none;
    background: var(--bg-card);
    color: var(--text-main);
    border: 1px solid var(--border-subtle);
    border-radius: 6px;
    padding: 0.3rem 0.55rem;
    font-size: 0.74rem;
    font-weight: 600;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 0.3rem;
    transition: all 0.18s ease;
}

.float-btn:hover {
    background: var(--bg-card-hover);
    border-color: var(--border-focus);
    transform: translateY(-1px);
}

.float-close-btn {
    padding: 0.15rem 0.45rem;
    font-size: 0.85rem;
    color: var(--text-muted);
}
.float-close-btn:hover {
    color: #ef4444;
    border-color: #ef4444;
}

.floating-timer-body {
    margin: 0.4rem 0 0.65rem 0;
}

.floating-time-display {
    font-family: var(--font-mono);
    font-size: 1.95rem;
    font-weight: 800;
    letter-spacing: -0.02em;
    text-align: center;
    color: #10b981;
    text-shadow: 0 0 14px rgba(16, 185, 129, 0.4);
    line-height: 1.1;
    margin-bottom: 0.45rem;
}

.floating-progress-container {
    width: 100%;
    height: 6px;
    background: rgba(255, 255, 255, 0.08);
    border-radius: 999px;
    overflow: hidden;
    position: relative;
}

.floating-progress-bar {
    height: 100%;
    background: linear-gradient(90deg, #10b981, #38bdf8);
    border-radius: 999px;
    transition: width 0.3s ease, background 0.3s ease;
}

.floating-timer-controls {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 0.35rem;
}

.float-action-btn {
    flex: 1.2;
    justify-content: center;
    background: rgba(16, 185, 129, 0.18);
    color: #10b981;
    border-color: rgba(16, 185, 129, 0.45);
}
.float-action-btn:hover {
    background: #10b981;
    color: #064e3b;
    border-color: #10b981;
}

.float-reset-btn {
    padding: 0.3rem 0.45rem;
}

.float-sound-btn {
    padding: 0.3rem 0.45rem;
}
.float-sound-btn.sound-muted {
    color: var(--text-muted);
    border-color: var(--border-subtle);
}

.float-jump-btn {
    padding: 0.3rem 0.5rem;
    color: var(--accent, #38bdf8);
}

/* Floating Timer Warning State (< 60s) */
.floating-timer-widget.timer-warning {
    border-color: #f59e0b;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.45), 0 0 20px rgba(245, 158, 11, 0.35);
}
.floating-timer-widget.timer-warning .floating-time-display {
    color: #f59e0b;
    text-shadow: 0 0 14px rgba(245, 158, 11, 0.45);
}
.floating-timer-widget.timer-warning .floating-progress-bar {
    background: linear-gradient(90deg, #f59e0b, #ef4444);
}

/* Floating Timer Expired State (00:00) */
.floating-timer-widget.timer-expired {
    border-color: #ef4444;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.45), 0 0 24px rgba(239, 68, 68, 0.55);
    animation: expiredFlash 1s infinite alternate;
}
.floating-timer-widget.timer-expired .floating-time-display {
    color: #ef4444;
    text-shadow: 0 0 16px rgba(239, 68, 68, 0.6);
}
.floating-timer-widget.timer-expired .floating-progress-bar {
    background: #ef4444;
}

/* Question Card Flash Highlight on Jump */
@keyframes cardFlashHighlight {
    0% {
        box-shadow: 0 0 0 4px #38bdf8, 0 0 35px rgba(56, 189, 248, 0.7);
        transform: scale(1.008);
    }
    50% {
        box-shadow: 0 0 0 8px #38bdf8, 0 0 45px rgba(56, 189, 248, 0.9);
        transform: scale(1.012);
    }
    100% {
        box-shadow: none;
        transform: scale(1);
    }
}

.flash-highlight {
    animation: cardFlashHighlight 1.8s ease-out;
    border-color: #38bdf8 !important;
}

/* Light Theme Overrides */
[data-theme="light"] .floating-timer-widget {
    background: rgba(255, 255, 255, 0.94);
    box-shadow: 0 10px 30px rgba(15, 23, 42, 0.12), 0 0 16px rgba(16, 185, 129, 0.15);
    border-color: rgba(5, 150, 105, 0.4);
}
[data-theme="light"] .floating-time-display {
    color: #059669;
    text-shadow: none;
}
[data-theme="light"] .floating-progress-container {
    background: rgba(15, 23, 42, 0.08);
}
[data-theme="light"] .float-action-btn {
    background: rgba(5, 150, 105, 0.12);
    color: #065f46;
    border-color: rgba(5, 150, 105, 0.35);
}
[data-theme="light"] .float-action-btn:hover {
    background: #059669;
    color: #ffffff;
}

/* OLED Theme Overrides */
[data-theme="oled"] .floating-timer-widget {
    background: #000000;
    border: 1.5px solid #10b981;
    box-shadow: 0 0 20px rgba(16, 185, 129, 0.3);
}

/* Responsive Floating Timer for Mobile Devices */
@media (max-width: 640px) {
    .floating-timer-widget {
        top: 60px;
        right: 10px;
        min-width: 220px;
        max-width: calc(100vw - 20px);
        padding: 0.6rem 0.75rem;
    }
    .floating-time-display {
        font-size: 1.55rem;
    }
    .floating-timer-controls {
        flex-wrap: wrap;
        gap: 0.25rem;
    }
    .float-btn {
        font-size: 0.7rem;
        padding: 0.22rem 0.4rem;
    }
}
"""

css_target = """@keyframes expiredFlash {
    from { opacity: 1; }
    to { opacity: 0.65; }
}"""

if css_target in content:
    content = content.replace(css_target, css_target + "\n" + floating_timer_css)
    print("Injected floating_timer_css into CSS_STYLES successfully.")
else:
    print("Warning: css_target not found.")

# 3. Define FLOATING_TIMER_HTML
floating_timer_html_def = """
FLOATING_TIMER_HTML = \"\"\"
    <!-- Floating Active Exam Practice Timer (Top-Right Glassmorphism Pill) -->
    <div id="floating-timer" class="floating-timer-widget" style="display: none;" role="region" aria-label="Active Exam Practice Timer">
        <div class="floating-timer-header">
            <div class="floating-timer-title">
                <span class="floating-pendulum-icon" id="floating-pendulum" title="Pendulum ticking">🕰️</span>
                <span class="floating-qid" id="floating-qid">Q1 (3M)</span>
            </div>
            <button class="float-btn float-close-btn" onclick="closeFloatingTimer()" title="Dismiss floating timer widget" aria-label="Dismiss timer">✕</button>
        </div>
        <div class="floating-timer-body">
            <div class="floating-time-display" id="floating-time-display">05:00</div>
            <div class="floating-progress-container" title="Time remaining progress">
                <div class="floating-progress-bar" id="floating-progress-bar" style="width: 100%;"></div>
            </div>
        </div>
        <div class="floating-timer-controls">
            <button class="float-btn float-action-btn" id="floating-action-btn" onclick="toggleActiveTimer()" title="Pause / Resume active countdown">
                <span id="floating-action-icon">⏸️</span> <span id="floating-action-text">Pause</span>
            </button>
            <button class="float-btn float-reset-btn" id="floating-reset-btn" onclick="resetActiveTimer()" title="Reset active countdown">
                🔄 Reset
            </button>
            <button class="float-btn float-sound-btn" id="floating-sound-btn" onclick="toggleTimerSound()" title="Mute or Unmute Tick Sound">
                🔊 Sound
            </button>
            <button class="float-btn float-jump-btn" id="floating-jump-btn" onclick="jumpToActiveQuestion()" title="Scroll directly to active question card">
                🎯 Jump
            </button>
        </div>
    </div>
\"\"\"
"""

# Place FLOATING_TIMER_HTML right before JS_SCRIPT =
content = content.replace("JS_SCRIPT = \"\"\"", floating_timer_html_def + "\nJS_SCRIPT = \"\"\"")

# 4. Construct Full JS_SCRIPT with Pendulum Sound and Floating Timer Synchronizer
new_js_script = """JS_SCRIPT = \"\"\"
// =========================================================================
// Tab Switching for Multi-Subject Index Page
// =========================================================================
const tabBtns = document.querySelectorAll('.tab-btn');
const subjectViews = document.querySelectorAll('.subject-view');

function switchTab(targetId) {
    if (!targetId) return;
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
        const targetEl = document.getElementById(targetId);
        if (targetEl) {
            renderMathInElement(targetEl, {
                delimiters: [
                    {left: '$$', right: '$$', display: true},
                    {left: '$', right: '$', display: false}
                ],
                throwOnError: false
            });
        }
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

// =========================================================================
// Question Filtering & Search
// =========================================================================
const filterBtns = document.querySelectorAll('.filter-btn');
filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        applyFilters();
    });
});

const searchInput = document.getElementById('global-search');
if (searchInput) {
    searchInput.addEventListener('input', () => {
        applyFilters();
    });
}

function applyFilters() {
    const query = searchInput ? searchInput.value.toLowerCase().trim() : '';
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
// 1. 'dark'   : Soft Charcoal & Warm Slate
// 2. 'warm'   : Warm Espresso
// 3. 'forest' : Forest Night
// 4. 'oled'   : Midnight OLED
// 5. 'light'  : Warm Slate & Off-White Paper
// 6. 'sage'   : Sage & Soft Olive
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

// =========================================================================
// Web Audio API Pendulum Mechanical Escapement Sound Synthesizer
// Zero external audio dependencies - 100% offline & instant response
// =========================================================================
let audioCtx = null;
let soundMuted = false;
try {
    soundMuted = localStorage.getItem('exam_timer_sound_muted') === 'true';
} catch (e) {}

function initAudio() {
    if (!audioCtx) {
        const AudioContextClass = window.AudioContext || window.webkitAudioContext;
        if (AudioContextClass) {
            audioCtx = new AudioContextClass();
        }
    }
    if (audioCtx && audioCtx.state === 'suspended') {
        audioCtx.resume();
    }
}

// Alternating Pendulum Escapement Ticks:
// Tick: ~960Hz (left pallet strike)
// Tock: ~720Hz (right pallet strike)
function playPendulumTick(isTock) {
    if (soundMuted || !audioCtx) return;
    try {
        const now = audioCtx.currentTime;
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        const filter = audioCtx.createBiquadFilter();

        const baseFreq = isTock ? 720 : 960;
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(baseFreq, now);
        osc.frequency.exponentialRampToValueAtTime(baseFreq * 0.45, now + 0.035);

        filter.type = 'bandpass';
        filter.frequency.setValueAtTime(baseFreq * 1.4, now);
        filter.Q.setValueAtTime(8, now);

        gain.gain.setValueAtTime(0.0001, now);
        gain.gain.linearRampToValueAtTime(0.2, now + 0.002);
        gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.038);

        osc.connect(filter);
        filter.connect(gain);
        gain.connect(audioCtx.destination);

        osc.start(now);
        osc.stop(now + 0.042);
    } catch (e) {
        console.warn('Audio tick error:', e);
    }
}

// 3-Tone Arpeggio Chime when time hits 00:00 (Time's Up!)
function playTimeUpChime() {
    if (soundMuted || !audioCtx) return;
    try {
        const notes = [523.25, 659.25, 783.99, 1046.50];
        notes.forEach((freq, idx) => {
            const start = audioCtx.currentTime + (idx * 0.12);
            const osc = audioCtx.createOscillator();
            const gain = audioCtx.createGain();

            osc.type = 'sine';
            osc.frequency.setValueAtTime(freq, start);

            gain.gain.setValueAtTime(0.0001, start);
            gain.gain.linearRampToValueAtTime(0.22, start + 0.015);
            gain.gain.exponentialRampToValueAtTime(0.0001, start + 0.55);

            osc.connect(gain);
            gain.connect(audioCtx.destination);

            osc.start(start);
            osc.stop(start + 0.6);
        });
    } catch (e) {
        console.warn('Audio chime error:', e);
    }
}

function toggleTimerSound() {
    initAudio();
    soundMuted = !soundMuted;
    try {
        localStorage.setItem('exam_timer_sound_muted', soundMuted ? 'true' : 'false');
    } catch (e) {}
    updateSoundUI();
    if (!soundMuted) {
        playPendulumTick(false);
    }
}

function updateSoundUI() {
    const soundBtns = document.querySelectorAll('.float-sound-btn');
    soundBtns.forEach(btn => {
        if (soundMuted) {
            btn.innerHTML = '🔇 Muted';
            btn.classList.add('sound-muted');
            btn.setAttribute('title', 'Sound is muted. Click to enable rhythmic pendulum tick');
        } else {
            btn.innerHTML = '🔊 Sound';
            btn.classList.remove('sound-muted');
            btn.setAttribute('title', 'Sound is active. Click to mute pendulum tick');
        }
    });
}

// =========================================================================
// Interactive Exam Countdown Timers & Floating Top-Right Synchronizer
// =========================================================================
const cardTimers = {};
let activeTimerQid = null;

function formatTimerMMSS(seconds) {
    const m = Math.floor(seconds / 60);
    const s = seconds % 60;
    return (m < 10 ? '0' : '') + m + ':' + (s < 10 ? '0' : '') + s;
}

function updateFloatingWidget(qid) {
    const floatWidget = document.getElementById('floating-timer');
    if (!floatWidget) return;

    const timer = cardTimers[qid];
    if (!timer) return;

    const cardWidget = document.getElementById('timer-' + qid);
    const label = cardWidget ? (cardWidget.getAttribute('data-label') || qid.toUpperCase()) : qid.toUpperCase();

    const qidSpan = document.getElementById('floating-qid');
    const timeDisplay = document.getElementById('floating-time-display');
    const progressBar = document.getElementById('floating-progress-bar');
    const actionIcon = document.getElementById('floating-action-icon');
    const actionText = document.getElementById('floating-action-text');
    const pendulumIcon = document.getElementById('floating-pendulum');

    if (qidSpan) qidSpan.textContent = label;
    if (timeDisplay) timeDisplay.textContent = formatTimerMMSS(timer.remaining);

    const pct = Math.max(0, Math.min(100, (timer.remaining / timer.duration) * 100));
    if (progressBar) progressBar.style.width = pct + '%';

    if (timer.state === 'running') {
        if (actionIcon) actionIcon.textContent = '⏸️';
        if (actionText) actionText.textContent = 'Pause';
        if (pendulumIcon) pendulumIcon.classList.add('swinging');
        floatWidget.classList.remove('timer-paused');
        floatWidget.classList.add('timer-running');
    } else if (timer.state === 'paused') {
        if (actionIcon) actionIcon.textContent = '▶️';
        if (actionText) actionText.textContent = 'Resume';
        if (pendulumIcon) pendulumIcon.classList.remove('swinging');
        floatWidget.classList.remove('timer-running');
        floatWidget.classList.add('timer-paused');
    } else if (timer.state === 'expired') {
        if (actionIcon) actionIcon.textContent = '⚠️';
        if (actionText) actionText.textContent = "Time's Up!";
        if (pendulumIcon) pendulumIcon.classList.remove('swinging');
        floatWidget.classList.remove('timer-running', 'timer-paused');
        floatWidget.classList.add('timer-expired');
    } else {
        if (actionIcon) actionIcon.textContent = '▶️';
        if (actionText) actionText.textContent = 'Start';
        if (pendulumIcon) pendulumIcon.classList.remove('swinging');
        floatWidget.classList.remove('timer-running', 'timer-paused', 'timer-expired', 'timer-warning');
    }

    if (timer.remaining <= 60 && timer.remaining > 0) {
        floatWidget.classList.add('timer-warning');
    } else if (timer.remaining > 60) {
        floatWidget.classList.remove('timer-warning');
    }
}

function toggleCardTimer(qid) {
    initAudio();
    const widget = document.getElementById('timer-' + qid);
    if (!widget) return;
    const duration = parseInt(widget.getAttribute('data-duration') || '300', 10);

    // Pause any other previously running timer
    if (activeTimerQid && activeTimerQid !== qid) {
        const prevTimer = cardTimers[activeTimerQid];
        if (prevTimer && prevTimer.state === 'running') {
            clearInterval(prevTimer.intervalId);
            prevTimer.intervalId = null;
            prevTimer.state = 'paused';
            const prevWidget = document.getElementById('timer-' + activeTimerQid);
            if (prevWidget) {
                const prevAction = prevWidget.querySelector('.timer-action');
                if (prevAction) prevAction.textContent = 'Resume';
                prevWidget.classList.remove('timer-running');
                prevWidget.classList.add('timer-paused');
            }
        }
    }

    activeTimerQid = qid;

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

    // Display floating timer
    const floatWidget = document.getElementById('floating-timer');
    if (floatWidget) {
        floatWidget.style.display = 'block';
    }

    if (timer.state === 'running') {
        // Pause timer
        clearInterval(timer.intervalId);
        timer.intervalId = null;
        timer.state = 'paused';
        if (actionSpan) actionSpan.textContent = 'Resume';
        widget.classList.remove('timer-running');
        widget.classList.add('timer-paused');
        updateFloatingWidget(qid);
    } else {
        // Start or Resume
        if (timer.state === 'expired') {
            timer.remaining = timer.duration;
            widget.classList.remove('timer-expired');
        }
        timer.state = 'running';
        if (actionSpan) actionSpan.textContent = 'Pause';
        if (resetBtn) resetBtn.style.display = 'inline-flex';
        widget.classList.remove('timer-paused');
        widget.classList.add('timer-running');

        // Play initial tick and update UI immediately
        playPendulumTick(false);
        updateFloatingWidget(qid);

        timer.intervalId = setInterval(() => {
            timer.remaining--;
            if (displaySpan) displaySpan.textContent = formatTimerMMSS(timer.remaining);

            // Rhythmic Alternating Tick-Tock on every second
            const isTock = ((timer.duration - timer.remaining) % 2 === 1);
            playPendulumTick(isTock);

            if (timer.remaining <= 60 && timer.remaining > 0) {
                widget.classList.add('timer-warning');
            }

            if (timer.remaining <= 0) {
                clearInterval(timer.intervalId);
                timer.intervalId = null;
                timer.state = 'expired';
                if (displaySpan) displaySpan.textContent = '00:00';
                if (actionSpan) actionSpan.textContent = "Time's Up!";
                widget.classList.remove('timer-running', 'timer-warning');
                widget.classList.add('timer-expired');
                playTimeUpChime();
                updateFloatingWidget(qid);
            } else {
                updateFloatingWidget(qid);
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

    if (displaySpan) displaySpan.textContent = formatTimerMMSS(timer.duration);
    if (actionSpan) actionSpan.textContent = 'Start';
    if (resetBtn) resetBtn.style.display = 'none';
    widget.classList.remove('timer-running', 'timer-paused', 'timer-warning', 'timer-expired');

    if (activeTimerQid === qid) {
        updateFloatingWidget(qid);
    }
}

function toggleActiveTimer() {
    if (activeTimerQid) toggleCardTimer(activeTimerQid);
}

function resetActiveTimer() {
    if (activeTimerQid) resetCardTimer(activeTimerQid);
}

function closeFloatingTimer() {
    const floatWidget = document.getElementById('floating-timer');
    if (floatWidget) floatWidget.style.display = 'none';
}

function jumpToActiveQuestion() {
    if (!activeTimerQid) return;
    const card = document.getElementById(activeTimerQid);
    if (!card) return;

    const subjectView = card.closest ? card.closest('.subject-view') : null;
    if (subjectView && !subjectView.classList.contains('active')) {
        const viewId = subjectView.id;
        if (typeof switchTab === 'function') switchTab(viewId);
    }

    if (card.style.display === 'none') {
        if (searchInput) searchInput.value = '';
        const allBtn = document.querySelector('.filter-btn[data-filter="all"]');
        if (allBtn) {
            document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            allBtn.classList.add('active');
        }
        if (typeof applyFilters === 'function') applyFilters();
    }

    card.scrollIntoView({ behavior: 'smooth', block: 'center' });
    card.classList.remove('flash-highlight');
    void card.offsetWidth;
    card.classList.add('flash-highlight');
    setTimeout(() => {
        card.classList.remove('flash-highlight');
    }, 2000);
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

// Initialization on DOMContentLoaded
function initPortal() {
    initThemeSwitcher();
    updateSoundUI();
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initPortal);
} else {
    initPortal();
}
\"\"\"
"""

# Replace old JS_SCRIPT block in content
js_pattern = re.compile(r'JS_SCRIPT = """.*?"""', re.DOTALL)
content = js_pattern.sub(new_js_script, content, count=1)
print("Replaced JS_SCRIPT with complete audio and floating timer logic.")

# 5. Inject FLOATING_TIMER_HTML into INDEX_TEMPLATE
old_index_target = """    <!-- Floating Back to Top Button -->
    <button class="back-to-top-btn" id="back-to-top" onclick="scrollToTop()" title="Scroll to top of page">
        <span>↑</span> Top
    </button>"""

new_index_target = """    {{FLOATING_TIMER_HTML}}

    <!-- Floating Back to Top Button -->
    <button class="back-to-top-btn" id="back-to-top" onclick="scrollToTop()" title="Scroll to top of page">
        <span>↑</span> Top
    </button>"""

content = content.replace(old_index_target, new_index_target)

# In main(): replace {{FLOATING_TIMER_HTML}} in index.html
old_main_replace = """.replace("{{JS_BLOCK}}", JS_SCRIPT)"""
new_main_replace = """.replace("{{JS_BLOCK}}", JS_SCRIPT)
        .replace("{{FLOATING_TIMER_HTML}}", FLOATING_TIMER_HTML)"""

content = content.replace(old_main_replace, new_main_replace)
print("Updated INDEX_TEMPLATE and index.html replacement with FLOATING_TIMER_HTML.")

# 6. Update generate_standalone_page
standalone_pattern = re.compile(r'def generate_standalone_page\(subject_key, subject_title, subject_code, subject_color, subject_view_id, inner_html\):.*?(?=def main\(\):)', re.DOTALL)

new_standalone_func = """def generate_standalone_page(subject_key, subject_title, subject_code, subject_color, subject_view_id, inner_html):
    template = \"\"\"<!DOCTYPE html>
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

            <!-- Header Theme Switcher Palette Selector -->
            <div class="theme-palette-wrapper">
                <span class="theme-palette-label">Theme:</span>
                <div class="theme-btn-group" role="radiogroup" aria-label="Reading & Study Theme Selector">
                    <button class="theme-btn" data-theme-value="dark" title="Soft Charcoal & Slate" aria-label="Dark Mode">
                        <span class="theme-swatch swatch-dark"></span>
                        <span class="theme-title">Dark</span>
                    </button>
                    <button class="theme-btn" data-theme-value="warm" title="Warm Espresso (Zero Blue Light)" aria-label="Warm Mode">
                        <span class="theme-swatch swatch-warm"></span>
                        <span class="theme-title">Warm</span>
                    </button>
                    <button class="theme-btn" data-theme-value="forest" title="Forest Night (Lowest Eye Fatigue)" aria-label="Forest Mode">
                        <span class="theme-swatch swatch-forest"></span>
                        <span class="theme-title">Forest</span>
                    </button>
                    <button class="theme-btn" data-theme-value="oled" title="Midnight OLED (Pitch Black)" aria-label="OLED Mode">
                        <span class="theme-swatch swatch-oled"></span>
                        <span class="theme-title">OLED</span>
                    </button>
                    <button class="theme-btn" data-theme-value="light" title="Warm Slate & Off-White Paper" aria-label="Light Mode">
                        <span class="theme-swatch swatch-light"></span>
                        <span class="theme-title">Light</span>
                    </button>
                    <button class="theme-btn" data-theme-value="sage" title="Sage & Soft Olive Focus" aria-label="Sage Mode">
                        <span class="theme-swatch swatch-sage"></span>
                        <span class="theme-title">Sage</span>
                    </button>
                </div>
            </div>
        </div>

        <nav class="sub-nav">
            <div class="nav-tabs">
                <a href="index.html" class="tab-btn">⚡ Main Portal</a>
                <a href="acs.html" class="tab-btn {{ACTIVE_ACS}}">Advanced Control Systems</a>
                <a href="drives.html" class="tab-btn {{ACTIVE_DRIVE}}">Electric Drives</a>
                <a href="mobile_computing.html" class="tab-btn {{ACTIVE_MOBILE}}">Mobile Computing</a>
            </div>
        </nav>
    </header>

    <main class="main-content">
        <section class="exam-strategy-banner">
            <div class="strategy-icon">⏱️</div>
            <div class="strategy-details">
                <h4>3-Hour Exam Time Budget (20 Questions / 100 Marks Strategy)</h4>
                <p><strong>Part A (10 Short Answers &times; 3 Marks = 30M):</strong> Allocate <strong>5 mins per answer</strong> (50 mins total) &mdash; target &frac12; to 1 page highlighting the key formula and core definition.<br>
                <strong>Part B (10 Essay Answers &times; 7 Marks = 70M):</strong> Allocate <strong>12 mins per answer</strong> (120 mins total) &mdash; target 1.5 to 2 pages with schematic circuit/block diagrams and step-by-step derivations.<br>
                <strong>Strategy &amp; Review Buffer (10 mins):</strong> 5 mins at start for question choice planning + 5 mins at end for question numbering and equation verification.</p>
            </div>
        </section>
        {{INNER_HTML}}
    </main>

    {{FLOATING_TIMER_HTML}}

    <button class="back-to-top-btn" id="back-to-top" onclick="window.scrollTo({top: 0, behavior: 'smooth'})" title="Scroll to top of page">
        <span>↑</span> Top
    </button>

    <footer class="site-footer">
        <p>&copy; 2026 Academic Engineering Portal. Standalone Edition.</p>
    </footer>

    <script>
        {{JS_BLOCK}}
    </script>
</body>
</html>
\"\"\"
    active_acs = "active" if subject_key == "acs" else ""
    active_drive = "active" if subject_key == "drive" else ""
    active_mobile = "active" if subject_key == "mobile" else ""

    return (template
        .replace("{{SUBJECT_TITLE}}", subject_title)
        .replace("{{SUBJECT_CODE}}", subject_code)
        .replace("{{ACTIVE_ACS}}", active_acs)
        .replace("{{ACTIVE_DRIVE}}", active_drive)
        .replace("{{ACTIVE_MOBILE}}", active_mobile)
        .replace("{{CSS_BLOCK}}", CSS_STYLES)
        .replace("{{INNER_HTML}}", inner_html)
        .replace("{{FLOATING_TIMER_HTML}}", FLOATING_TIMER_HTML)
        .replace("{{JS_BLOCK}}", JS_SCRIPT)
    )

"""

content = standalone_pattern.sub(new_standalone_func, content, count=1)
print("Updated generate_standalone_page successfully.")

with open('scratch/gen_site.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("gen_site.py successfully updated with pendulum tick sound and floating timer!")
