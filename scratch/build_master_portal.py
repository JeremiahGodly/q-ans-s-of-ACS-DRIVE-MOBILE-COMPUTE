# -*- coding: utf-8 -*-
"""
Master Portal Builder: 15-in-1 Unified KTU Engineering Portal & Standalone Pages
Optimizations:
  1. Simulators isolated strictly in 60fps simulator window (animations.html)
  2. Ultra-fast initial load: on-demand per-subject KaTeX math rendering
  3. Integrated Official University Question Papers & Schemes for each subject
  4. Ergonomic Semester Dropdowns (S1/S2 Foundation, S6 EEE, S7 EEE)
"""

import sys, os, html, urllib.parse

sys.path.append('scratch')

from gen_acs import ACS_MODULES
from gen_drive import DRIVE_MODULES
from gen_mobile import MOBILE_SYLLABUS, MOBILE_MODULES
from gen_maths_lac import MATHS_LAC_MODULES
from gen_maths_vcdet import MATHS_VCDET_MODULES
from gen_physics import PHYSICS_MODULES
from gen_lcs import LCS_MODULES
from gen_ps2 import PS2_MODULES
from gen_mechanics import MECHANICS_MODULES
from gen_pe import PE_MODULES
from gen_res import RES_MODULES
from gen_management import MANAGEMENT_MODULES
from gen_beee import BEEE_MODULES
from gen_comprehensive import COMPREHENSIVE_MODULES
from gen_cprog import CPROG_MODULES

from byheart_data import get_byheart_card_html
from exam_questions import EXAM_QUESTIONS_MAP
from lecturer_answers import REPRESENTATIVE_ANSWERS
from local_language_bank import LOCAL_LANG_BANK
from multi_diagrams_data import EXTRA_DIAGRAMS_MAP

# Authentic Downloaded KTU University Question Papers Catalog
QP_CATALOG = {
    "acs": [
        {"name": "ACS full pyq and answer keys.pdf", "session": "Comprehensive PYQ Collection (2019-2025)", "size": "8.5 MB", "type": "Full Answer Keys"},
        {"name": "EET401 ADVANCED CONTROL SYSTEMS, MAY 2026.pdf", "session": "May 2026 University Exam", "size": "481 KB", "type": "Official Question Paper"},
        {"name": "EET401 ADVANCED CONTROL SYSTEMS, NOVEMBER 2025.pdf", "session": "November 2025 University Exam", "size": "1.6 MB", "type": "Official Question Paper"},
        {"name": "Advanced Control Systems (April 2025) Answer Key.pdf", "session": "April 2025 University Exam", "size": "512 KB", "type": "Official Evaluation Scheme"},
        {"name": "Advanced Control Systems (November 2024) Answer Key_1.pdf", "session": "November 2024 University Exam", "size": "1.0 MB", "type": "Official Evaluation Scheme"}
    ],
    "drive": [
        {"name": "Electric Drives (November 2024) Answer Key.pdf", "session": "November 2024 University Exam", "size": "208 KB", "type": "Official Evaluation Scheme"},
        {"name": "Electric Drives (May 2024) Answer Key.pdf", "session": "May 2024 University Exam", "size": "231 KB", "type": "Official Evaluation Scheme"},
        {"name": "Electric Drives (April 2025) Answer Key.pdf", "session": "April 2025 University Exam", "size": "209 KB", "type": "Official Evaluation Scheme"},
        {"name": "Electric Drives (December 2023) Answer Key.pdf", "session": "December 2023 University Exam", "size": "215 KB", "type": "Official Evaluation Scheme"},
        {"name": "Electric Drives (May 2023) Answer Key.pdf", "session": "May 2023 University Exam", "size": "208 KB", "type": "Official Evaluation Scheme"},
        {"name": "Electric Drives (December 2022) Answer Key.pdf", "session": "December 2022 University Exam", "size": "239 KB", "type": "Official Evaluation Scheme"},
        {"name": "Electric Drives (May 2021) Answer Key.pdf", "session": "May 2021 University Exam", "size": "1.5 MB", "type": "Official Evaluation Scheme"},
        {"name": "Speed vs Torque Characteristics Diagram.pdf", "session": "Reference Characteristic Schematics", "size": "1.1 MB", "type": "Technical Blueprint"}
    ],
    "mobile": [
        {"name": "Introduction to Mobile Computing (November 2024) Answer Key.pdf", "session": "November 2024 University Exam", "size": "136 KB", "type": "Official Evaluation Scheme"},
        {"name": "Introduction to Mobile Computing (May 2024) Answer Key.pdf", "session": "May 2024 University Exam", "size": "140 KB", "type": "Official Evaluation Scheme"},
        {"name": "Introduction to Mobile Computing (December 2023) Answer Key.pdf", "session": "December 2023 University Exam", "size": "133 KB", "type": "Official Evaluation Scheme"},
        {"name": "Introduction to Mobile Computing (2019) Answer Key.pdf", "session": "2019 Scheme Curriculum Model", "size": "485 KB", "type": "Model Evaluation Scheme"}
    ],
    "lac": [
        {"name": "MAT101_Dec2019_QP.pdf", "session": "December 2019 University Exam", "size": "156 KB", "type": "Official Question Paper"},
        {"name": "MAT101_Jan2021_QP.pdf", "session": "January 2021 Improvement Exam", "size": "349 KB", "type": "Official Question Paper"},
        {"name": "MAT101_Dec2021_Solved_Scheme.pdf", "session": "December 2021 Evaluation Scheme", "size": "13.8 MB", "type": "Complete Solved Scheme"}
    ],
    "vcdet": [
        {"name": "MAT102_June2023_QP.pdf", "session": "June 2023 University Exam", "size": "251 KB", "type": "Official Question Paper"}
    ],
    "physics": [
        {"name": "PHT100_Dec2019_QP.pdf", "session": "December 2019 University Exam", "size": "354 KB", "type": "Official Question Paper"},
        {"name": "PHT100_Jan2021_QP.pdf", "session": "January 2021 Improvement Exam", "size": "401 KB", "type": "Official Question Paper"},
        {"name": "PHT100_Dec2021_Answer_Key.pdf", "session": "December 2021 Evaluation Scheme", "size": "2.1 MB", "type": "Official Evaluation Scheme"}
    ],
    "mechanics": [
        {"name": "EST100_Dec2019_QP.pdf", "session": "December 2019 University Exam", "size": "246 KB", "type": "Official Question Paper"},
        {"name": "EST100_Jan2021_QP.pdf", "session": "January 2021 Improvement Exam", "size": "378 KB", "type": "Official Question Paper"},
        {"name": "EST100_Dec2021_Answers.pdf", "session": "December 2021 Evaluation Scheme", "size": "3.9 MB", "type": "Complete Solved Scheme"}
    ],
    "beee": [
        {"name": "EST130_Dec2019_QP.pdf", "session": "December 2019 University Exam", "size": "252 KB", "type": "Official Question Paper"},
        {"name": "EST130_Jan2021_QP.pdf", "session": "January 2021 Improvement Exam", "size": "323 KB", "type": "Official Question Paper"},
        {"name": "EST130_Dec2021_QP.pdf", "session": "December 2021 University Exam", "size": "1.2 MB", "type": "Official Question Paper"}
    ],
    "cprog": [
        {"name": "EST102_June2023_QP.pdf", "session": "June 2023 University Exam", "size": "157 KB", "type": "Official Question Paper"}
    ],
    "lcs": [
        {"name": "EET302_June2023_QP.pdf", "session": "June 2023 University Exam", "size": "208 KB", "type": "Official Question Paper"}
    ],
    "ps2": [
        {"name": "EET304_June2023_QP.pdf", "session": "June 2023 University Exam", "size": "387 KB", "type": "Official Question Paper"}
    ],
    "pe": [
        {"name": "EET306_June2023_QP.pdf", "session": "June 2023 University Exam", "size": "193 KB", "type": "Official Question Paper"}
    ],
    "comp": [
        {"name": "EET308_June2023_QP.pdf", "session": "June 2023 University Exam", "size": "1.0 MB", "type": "Official Question Paper"}
    ],
    "res": [
        {"name": "EET322_June2023_QP.pdf", "session": "June 2023 University Exam", "size": "116 KB", "type": "Official Question Paper"}
    ],
    "mgt": [
        {"name": "HUT310_June2023_QP.pdf", "session": "June 2023 University Exam", "size": "186 KB", "type": "Official Question Paper"},
        {"name": "HUT310_Dec2023_QP.pdf", "session": "December 2023 University Exam", "size": "138 KB", "type": "Official Question Paper"}
    ]
}

# 15 Subjects Registry organized by KTU Semesters
SUBJECTS_CONFIG = [
    # Category 1: S1 / S2 Foundation
    {
        "id": "lac",
        "code": "MAT101",
        "title": "Linear Algebra and Calculus",
        "short": "Maths LAC (MAT101)",
        "icon": "📐",
        "color": "#6366f1",
        "glow": "rgba(99, 102, 241, 0.3)",
        "darker": "#4f46e5",
        "semester": "s1s2",
        "cat_label": "S1/S2 Foundation",
        "modules": MATHS_LAC_MODULES,
        "hero_desc": "Foundational engineering mathematics: Matrix diagonalization, quadratic forms, eigenvalues &amp; eigenvectors, multivariable partial differentiation, Taylor series, multiple integrals (double &amp; triple), vector calculus, gradient, divergence, curl, line and surface integrals, and Green's, Stokes' &amp; Gauss divergence theorems.",
        "filename": "maths_lac.html"
    },
    {
        "id": "vcdet",
        "code": "MAT102",
        "title": "Vector Calculus, Differential Equations and Transforms",
        "short": "Maths VCDET (MAT102)",
        "icon": "📈",
        "color": "#8b5cf6",
        "glow": "rgba(139, 92, 246, 0.3)",
        "darker": "#7c3aed",
        "semester": "s1s2",
        "cat_label": "S1/S2 Foundation",
        "modules": MATHS_VCDET_MODULES,
        "hero_desc": "Advanced engineering calculus and analytical transforms: First-order and second-order linear differential equations with constant/variable coefficients, method of variation of parameters, Cauchy-Euler equations, Laplace transforms &amp; inverse transforms, convolution theorem, Fourier series expansions, and Fourier integral transforms.",
        "filename": "maths_vcdet.html"
    },
    {
        "id": "physics",
        "code": "PHT100",
        "title": "Engineering Physics A",
        "short": "Physics A (PHT100)",
        "icon": "🔬",
        "color": "#ec4899",
        "glow": "rgba(236, 72, 153, 0.3)",
        "darker": "#db2777",
        "semester": "s1s2",
        "cat_label": "S1/S2 Foundation",
        "modules": PHYSICS_MODULES,
        "hero_desc": "Core physical principles for engineers: Simple harmonic motion, damped &amp; forced oscillations, resonance, wave optics (interference, diffraction, polarization), lasers &amp; holography, optical fiber communication, quantum mechanics (wave packets, Schrödinger wave equations), and nanoscience fundamentals.",
        "filename": "physics.html"
    },
    {
        "id": "mechanics",
        "code": "EST100",
        "title": "Engineering Mechanics",
        "short": "Mechanics (EST100)",
        "icon": "⚙️",
        "color": "#ef4444",
        "glow": "rgba(239, 68, 68, 0.3)",
        "darker": "#dc2626",
        "semester": "s1s2",
        "cat_label": "S1/S2 Foundation",
        "modules": MECHANICS_MODULES,
        "hero_desc": "Statics and dynamics of engineering structures: Coplanar force systems, Lami's theorem, moments and couples, Varignon's theorem, equilibrium conditions, friction and belt friction, centroids and second moment of area (moment of inertia), kinematics and kinetics of particles, D'Alembert's principle, work-energy, and impulse-momentum relations.",
        "filename": "mechanics.html"
    },
    {
        "id": "beee",
        "code": "EST130",
        "title": "Basics of Electrical & Electronics Engineering",
        "short": "BEEE (EST130)",
        "icon": "💡",
        "color": "#f97316",
        "glow": "rgba(249, 115, 22, 0.3)",
        "darker": "#ea580c",
        "semester": "s1s2",
        "cat_label": "S1/S2 Foundation",
        "modules": BEEE_MODULES,
        "hero_desc": "Essential electrical &amp; electronic engineering: DC circuit theorems (KVL, KCL, Thevenin, Norton, Superposition), AC single-phase &amp; three-phase star/delta systems, magnetic circuits, transformers and DC/AC machines, PN junction diodes, BJT amplifier configurations, operational amplifiers, and digital logic gates.",
        "filename": "beee.html"
    },
    {
        "id": "cprog",
        "code": "EST102",
        "title": "Programming in C",
        "short": "C Programming (EST102)",
        "icon": "💻",
        "color": "#14b8a6",
        "glow": "rgba(20, 184, 166, 0.3)",
        "darker": "#0d9488",
        "semester": "s1s2",
        "cat_label": "S1/S2 Foundation",
        "modules": CPROG_MODULES,
        "hero_desc": "Procedural algorithm design and C programming: Data types, control flow (loops &amp; conditionals), 1D &amp; 2D arrays, string manipulations, modular functions &amp; recursion, pointer arithmetic &amp; dynamic memory allocation (malloc/free), structures &amp; unions, and file I/O operations.",
        "filename": "c_programming.html"
    },

    # Category 2: S6 EEE
    {
        "id": "lcs",
        "code": "EET302",
        "title": "Linear Control Systems",
        "short": "LCS (EET302)",
        "icon": "🎯",
        "color": "#06b6d4",
        "glow": "rgba(6, 182, 212, 0.3)",
        "darker": "#0891b2",
        "semester": "s6",
        "cat_label": "S6 EEE",
        "modules": LCS_MODULES,
        "hero_desc": "Foundations of dynamic feedback systems: Transfer function modeling, block diagram algebra, Mason's gain formula, time-domain transient analysis (first &amp; second order systems), Routh-Hurwitz stability criterion, Root Locus design, frequency domain analysis via Bode plots, Nyquist stability criterion, and lead/lag/PID compensator design.",
        "filename": "lcs.html"
    },
    {
        "id": "ps2",
        "code": "EET304",
        "title": "Power System II",
        "short": "Power System II (EET304)",
        "icon": "⚡",
        "color": "#eab308",
        "glow": "rgba(234, 179, 8, 0.3)",
        "darker": "#ca8a04",
        "semester": "s6",
        "cat_label": "S6 EEE",
        "modules": PS2_MODULES,
        "hero_desc": "Advanced electrical power network analysis: Per-unit representation, symmetrical components ($I_0, I_1, I_2$), symmetrical and unsymmetrical fault analysis (LG, LL, LLG), load flow studies (Gauss-Seidel &amp; Newton-Raphson), power system stability (swing equation, equal area criterion), and economic dispatch of thermal units.",
        "filename": "power_systems_2.html"
    },
    {
        "id": "pe",
        "code": "EET306",
        "title": "Power Electronics",
        "short": "Power Electronics (EET306)",
        "icon": "🔌",
        "color": "#d946ef",
        "glow": "rgba(217, 70, 239, 0.3)",
        "darker": "#c026d3",
        "semester": "s6",
        "cat_label": "S6 EEE",
        "modules": PE_MODULES,
        "hero_desc": "Solid-state energy conversion: Power semiconductor switching devices (SCR, MOSFET, IGBT), line-commutated controlled rectifiers (single-phase &amp; three-phase converters), DC-DC switch-mode buck, boost, and buck-boost choppers, voltage-source (VSI) &amp; current-source (CSI) inverters, sinusoidal pulse width modulation (SPWM), and cycloconverters.",
        "filename": "power_electronics.html"
    },
    {
        "id": "comp",
        "code": "EET308",
        "title": "Comprehensive Course Work",
        "short": "Comprehensive (EET308)",
        "icon": "🎓",
        "color": "#3b82f6",
        "glow": "rgba(59, 130, 246, 0.3)",
        "darker": "#2563eb",
        "semester": "s6",
        "cat_label": "S6 EEE",
        "modules": COMPREHENSIVE_MODULES,
        "hero_desc": "Capstone synthesis of core electrical &amp; electronics disciplines: Circuit analysis, electromagnetic field theory, electrical machines (transformers, DC &amp; induction/synchronous motors), power systems, control engineering, power electronics, analog/digital electronics, and microprocessor/microcontroller systems.",
        "filename": "comprehensive.html"
    },
    {
        "id": "res",
        "code": "EET322",
        "title": "Renewable Energy Systems",
        "short": "Renewable Energy (EET322)",
        "icon": "☀️",
        "color": "#84cc16",
        "glow": "rgba(132, 204, 22, 0.3)",
        "darker": "#65a30d",
        "semester": "s6",
        "cat_label": "S6 EEE",
        "modules": RES_MODULES,
        "hero_desc": "Green power generation and storage: Solar radiation geometry, photovoltaic (PV) cell I-V characteristics &amp; MPPT algorithms (P&amp;O, Incremental Conductance), wind energy conversion systems (Betz limit, HAWT vs VAWT, pitch/yaw control), biomass gasification, small hydro, geothermal &amp; ocean energy, and grid-connected inverter topologies.",
        "filename": "renewable_energy.html"
    },
    {
        "id": "mgt",
        "code": "HUT300",
        "title": "Management for Engineers",
        "short": "Management (HUT300)",
        "icon": "📊",
        "color": "#a855f7",
        "glow": "rgba(168, 85, 247, 0.3)",
        "darker": "#9333ea",
        "semester": "s6",
        "cat_label": "S6 EEE",
        "modules": MANAGEMENT_MODULES,
        "hero_desc": "Engineering economics, leadership and project management: Classical &amp; modern management theories (Taylor, Fayol), organizational structures, motivation &amp; leadership models, financial management &amp; accounting, project network scheduling (CPM &amp; PERT), quality management (TQM, ISO 9000), and intellectual property rights (IPR).",
        "filename": "management.html"
    },

    # Category 3: S7 EEE
    {
        "id": "acs",
        "code": "EET401",
        "title": "Advanced Control Systems",
        "short": "ACS (EET401)",
        "icon": "📘",
        "color": "#38bdf8",
        "glow": "rgba(56, 189, 248, 0.3)",
        "darker": "#0284c7",
        "semester": "s7",
        "cat_label": "S7 EEE",
        "modules": ACS_MODULES,
        "hero_desc": "Complete university previous year questions, continuous LTI and non-linear system state models, solution of state equations, Cayley-Hamilton state transition matrices, Kalman controllability/observability, Ackermann state feedback pole placement, Luenberger observers, describing functions for non-linear saturation, phase plane singular point analysis, and Lyapunov stability theorems.",
        "filename": "acs.html"
    },
    {
        "id": "drive",
        "code": "EET413",
        "title": "Electric Drives",
        "short": "Drives (EET413)",
        "icon": "⚡",
        "color": "#f59e0b",
        "glow": "rgba(245, 158, 11, 0.3)",
        "darker": "#d97706",
        "semester": "s7",
        "cat_label": "S7 EEE",
        "modules": DRIVE_MODULES,
        "hero_desc": "Exhaustive coverage of drive dynamics, fundamental dynamic torque equation derivations, four-quadrant hoist operations, steady-state stability criteria, phase-controlled converter DC drives with firing angle problem solving, chopper-controlled two-quadrant drives, closed-loop cascade speed control, induction motor stator voltage and V/f speed control, static rotor resistance chopper drives, synchronous motor drives, Space Vector PWM, Clarke/Park reference frame transformations, and Field-Oriented Control (FOC).",
        "filename": "drives.html"
    },
    {
        "id": "mobile",
        "code": "CST415",
        "title": "Introduction to Mobile Computing",
        "short": "Mobile (CST415)",
        "icon": "📱",
        "color": "#10b981",
        "glow": "rgba(16, 185, 129, 0.3)",
        "darker": "#059669",
        "semester": "s7",
        "cat_label": "S7 EEE",
        "modules": MOBILE_MODULES,
        "hero_desc": "Comprehensive curriculum guide and university question bank encompassing the official CST415 syllabus, three-tier mobile computing architecture, client context and adaptability management, cellular multiple access (FDMA, TDMA, CDMA, SDMA), GEO/LEO/MEO satellites, full GSM network architecture with A3/A8/A5 security algorithms, SMS/GPRS architecture and packet workflows, IEEE 802.11 WLAN with hidden/exposed terminal RTS/CTS mechanics, Wireless Local Loop (WLL), Public Key RSA cryptosystem numerical problem solving, Diffie-Hellman key exchange, TLS/SSL protocols, and Orthogonal Frequency Division Multiplexing (OFDM).",
        "filename": "mobile_computing.html"
    }
]

SEMESTERS_DATA = [
    {
        "key": "s1s2",
        "title": "S1 / S2 Foundation",
        "short_title": "S1 / S2",
        "icon": "🏛️",
        "badge": "6 Subjects",
        "desc": "Foundational mathematics, physics, mechanics, electrical basics and C programming",
        "ids": ["lac", "vcdet", "physics", "mechanics", "beee", "cprog"]
    },
    {
        "key": "s6",
        "title": "S6 EEE",
        "short_title": "S6",
        "icon": "⚡",
        "badge": "6 Subjects",
        "desc": "Linear control systems, power systems II, power electronics, comprehensive and renewables",
        "ids": ["lcs", "ps2", "pe", "comp", "res", "mgt"]
    },
    {
        "key": "s7",
        "title": "S7 EEE",
        "short_title": "S7",
        "icon": "🚀",
        "badge": "3 Subjects",
        "desc": "Advanced control systems, electric drives, and mobile computing",
        "ids": ["acs", "drive", "mobile"]
    }
]

# Diagram rendering
def render_single_diagram(img_path, img_caption, badge=None, qid=None, fig_idx=1):
    if not img_path:
        return ""
    badge_html = f'<div class="diagram-badge-pill">{html.escape(badge)}</div>' if badge else ""
    exists = os.path.exists(img_path)

    draw_link_html = ""
    if qid and exists:
        if qid.startswith("drive-"):
            page = "draw_drives.html"
            color = "#f59e0b"
            bg_col = "rgba(245, 158, 11, 0.12)"
            border_col = "rgba(245, 158, 11, 0.4)"
        elif qid.startswith("acs-"):
            page = "draw_acs.html"
            color = "#38bdf8"
            bg_col = "rgba(56, 189, 248, 0.12)"
            border_col = "rgba(56, 189, 248, 0.4)"
        elif qid.startswith("mobile-"):
            page = "draw_mobile.html"
            color = "#10b981"
            bg_col = "rgba(16, 185, 129, 0.12)"
            border_col = "rgba(16, 185, 129, 0.4)"
        else:
            page = "draw.html"
            color = "#6366f1"
            bg_col = "rgba(99, 102, 241, 0.12)"
            border_col = "rgba(99, 102, 241, 0.4)"

        hash_target = f"{qid}-fig{fig_idx}" if fig_idx > 1 else qid
        draw_link_html = f'''<a href="{page}#{hash_target}" class="diagram-draw-link" style="--draw-color:{color}; --draw-bg:{bg_col}; --draw-border:{border_col};" title="Trace &amp; practice drawing this blueprint in the interactive drawing canvas">
            <span class="draw-link-icon">✏️</span>
            <span class="draw-link-label">Practice Drawing Blueprint</span>
            <span class="draw-link-arrow">&rarr;</span>
        </a>'''

    topbar_html = ""
    if badge_html or draw_link_html:
        topbar_html = f'''<div class="diagram-card-topbar">
            {badge_html if badge_html else "<span></span>"}
            {draw_link_html}
        </div>'''

    if exists:
        return f"""
        <div class="diagram-card has-real-image">
            {topbar_html}
            <div class="diagram-wrapper">
                <img src="{img_path}" alt="{html.escape(img_caption)}" class="diagram-img" loading="lazy">
            </div>
            <p class="diagram-caption"><strong>Figure:</strong> {html.escape(img_caption)}</p>
        </div>
        """
    else:
        return f"""
        <div class="diagram-notice missing-notice">
            <span class="notice-icon">ℹ️</span>
            <span class="notice-text"><strong>Schematic:</strong> {html.escape(img_caption)} &mdash; <em>(Refer to textbook/lecture notes)</em></span>
        </div>
        """

def render_diagrams_box(q):
    qid = q.get("qid", "")
    primary_path = q.get("img_path")
    primary_caption = q.get("img_caption", "")
    extra_images = q.get("extra_images") or EXTRA_DIAGRAMS_MAP.get(qid, [])

    if not primary_path and not extra_images:
        return ""

    if not extra_images:
        return render_single_diagram(primary_path, primary_caption, qid=qid, fig_idx=1)

    cards_html = []
    primary_badge = "Figure A • Primary Architecture"
    cards_html.append(render_single_diagram(primary_path, primary_caption, badge=primary_badge, qid=qid, fig_idx=1))

    for idx, extra in enumerate(extra_images, start=2):
        letter = chr(64 + idx)
        badge = extra.get("badge", f"Figure {letter} • Technical Detail")
        cards_html.append(render_single_diagram(extra.get("img_path"), extra.get("img_caption", ""), badge=badge, qid=qid, fig_idx=idx))

    return f"""
    <div class="multi-diagrams-container">
        <div class="multi-diagrams-header">
            <span class="multi-diagrams-icon">📐</span>
            <div class="multi-diagrams-title-group">
                <span class="multi-diagrams-title">Dual Technical Schematics &bull; Full Exam Coverage</span>
                <span class="multi-diagrams-subtitle">Circuit Topology, Force Mechanics &amp; Conduction Waveforms</span>
            </div>
            <span class="multi-diagrams-badge">{len(cards_html)} Figures</span>
        </div>
        <div class="multi-diagrams-grid">
            {''.join(cards_html)}
        </div>
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
    qid = q["qid"]
    actual_question = EXAM_QUESTIONS_MAP.get(qid, q["title"])
    marks_badge = f'<span class="badge badge-3m">3 Marks (Short Answer)</span>' if q["marks"] == 3 else f'<span class="badge badge-7m">7/14 Marks (Long Essay / Derivation)</span>'
    duration_sec = 300 if q["marks"] == 3 else 720
    duration_str = "05:00" if q["marks"] == 3 else "12:00"
    
    parts = qid.split('-')
    subj_prefix = parts[0].upper()
    q_num = parts[1].replace('q', '') if len(parts) > 1 else '1'
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
    img_box = render_diagrams_box(q)

    # Check for lecturer-refined answers
    rep = REPRESENTATIVE_ANSWERS.get(qid)
    if rep:
        content_html = rep["exam_answer"]
        understand_simply = rep.get("understand_simply")
    else:
        content_html = format_paragraphs(q["answer"])
        understand_simply = None

    demo = LOCAL_LANG_BANK.get(qid)

    # In-card language switcher
    card_lang_toggle = f'''
    <div class="card-lang-toggle" data-qid="{qid}">
        <button type="button" class="card-lang-btn active" data-card-lang="en" onclick="setCardLang('{qid}', 'en')" title="Switch this card to English">🇬🇧 EN</button>
        <button type="button" class="card-lang-btn" data-card-lang="manglish" onclick="setCardLang('{qid}', 'manglish')" title="Switch this card to Manglish (Local Tone)">🌴 Manglish</button>
        <button type="button" class="card-lang-btn" data-card-lang="ml" onclick="setCardLang('{qid}', 'ml')" title="ഈ ചോദ്യം മലയാളത്തിൽ കാണുക">🇮🇳 മലയാളം</button>
    </div>
    '''

    if demo:
        m_title = demo['manglish']['title']
        ml_title = demo['ml']['title']
        title_html = f'''
        <h3 class="card-title">
            <span class="lang-view lang-en">{actual_question}</span>
            <span class="lang-view lang-manglish">{m_title}</span>
            <span class="lang-view lang-ml font-ml">{ml_title}</span>
        </h3>
        '''
    else:
        title_html = f'''
        <h3 class="card-title">
            <span class="lang-view lang-en">{actual_question}</span>
            <span class="lang-view lang-manglish">{actual_question}</span>
            <span class="lang-view lang-ml">{actual_question}</span>
        </h3>
        '''

    byheart_en = get_byheart_card_html(qid, q["marks"])
    time_badge = '<span class="byheart-time-badge">⏱️ 5 Mins Writing Time</span>' if q["marks"] == 3 else '<span class="byheart-time-badge">⏱️ 12 Mins Writing Time</span>'

    if demo:
        m_rem = demo['manglish']['remember_this']
        m_icon = "⚡" if "Equation" in m_rem['title'] else "📌"
        m_eq_html = f'<div class="byheart-eq">{m_rem["eq"]}</div>' if m_rem.get("eq") else ""
        byheart_manglish = f'''
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
        '''

        ml_rem = demo['ml']['remember_this']
        ml_icon = "⚡" if ("സമവാക്യം" in ml_rem['title'] or "Equation" in ml_rem['title']) else "📌"
        ml_eq_html = f'<div class="byheart-eq">{ml_rem["eq"]}</div>' if ml_rem.get("eq") else ""
        byheart_ml = f'''
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
        '''

        byheart_block = f'''
        <div class="lang-view lang-en">{byheart_en}</div>
        <div class="lang-view lang-manglish">{byheart_manglish}</div>
        <div class="lang-view lang-ml">{byheart_ml}</div>
        '''
    else:
        byheart_block = f'''
        <div class="lang-view lang-en">{byheart_en}</div>
        <div class="lang-view lang-manglish">{byheart_en}</div>
        <div class="lang-view lang-ml">{byheart_en}</div>
        '''

    if demo:
        exam_section = f'''
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
        '''
    else:
        exam_section = f'''
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
            <div class="answer-section">
                <div class="answer-section-header">
                    <h4 class="answer-section-title"><span class="section-tag section-tag-manglish">🌴 Manglish</span> Local Tone Study Guide</h4>
                </div>
                <div class="exam-ready-content">
                    {content_html}
                </div>
            </div>
        </div>

        <div class="lang-view lang-ml">
            <div class="answer-section">
                <div class="answer-section-header">
                    <h4 class="answer-section-title"><span class="section-tag section-tag-ml">🇮🇳 മലയാളം</span> പ്രാദേശിക പഠന സഹായി</h4>
                </div>
                <div class="exam-ready-content font-ml">
                    {content_html}
                </div>
            </div>
        </div>
        '''

    if demo:
        u_en = understand_simply or f'<p class="understand-para">Study Tip: Focus on fundamental formulas and core operating principles highlighted above.</p>'
        u_drawer = f'''
        <details class="understand-simply-drawer">
            <summary class="understand-summary">
                <span class="summary-left">
                    <span class="summary-icon">💡</span>
                    <span class="summary-title">Understand it simply</span>
                    <span class="summary-badge">Optional &bull; Concepts &amp; Real-world Context</span>
                </span>
                <span class="summary-arrow">&blacktriangledown;</span>
            </summary>
            <div class="understand-body">
                {u_en}
            </div>
        </details>
        '''
        understand_box = f'''
        <div class="lang-view lang-en">{u_drawer}</div>
        <div class="lang-view lang-manglish">{u_drawer}</div>
        <div class="lang-view lang-ml">{u_drawer}</div>
        '''
    else:
        if understand_simply:
            u_drawer = f'''
            <details class="understand-simply-drawer">
                <summary class="understand-summary">
                    <span class="summary-left">
                        <span class="summary-icon">💡</span>
                        <span class="summary-title">Understand it simply</span>
                        <span class="summary-badge">Optional &bull; Concepts &amp; Real-world Context</span>
                    </span>
                    <span class="summary-arrow">&blacktriangledown;</span>
                </summary>
                <div class="understand-body">
                    {understand_simply}
                </div>
            </details>
            '''
            understand_box = f'''
            <div class="lang-view lang-en">{u_drawer}</div>
            <div class="lang-view lang-manglish">{u_drawer}</div>
            <div class="lang-view lang-ml">{u_drawer}</div>
            '''
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
    """

def render_module_section(mod, subject_class):
    q_cards = '\n'.join([render_question_card(q, subject_class) for q in mod["questions"]])
    return f"""
    <section class="module-section" id="{mod['module_id']}">
        <div class="module-header">
            <span class="module-tag">{mod['module_num']}</span>
            <h2 class="module-title">{mod['module_title']}</h2>
            <p class="module-count">{len(mod['questions'])} Elaborated University Questions &amp; Answers</p>
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

# Render Question Papers & Schemes Vault Box
def render_question_papers_box(sid):
    papers = QP_CATALOG.get(sid, [])
    if not papers:
        return ""

    cards_html = []
    for p in papers:
        rel_path = f"question_papers/{sid}/{urllib.parse.quote(p['name'])}"
        cards_html.append(f"""
        <div class="qp-card">
            <div class="qp-card-info">
                <span class="qp-badge">{p['type']}</span>
                <h5 class="qp-session-title">{p['session']}</h5>
                <span class="qp-meta-text">{p['size']} &bull; Authentic KTU PDF</span>
            </div>
            <div class="qp-card-actions">
                <a href="{rel_path}" target="_blank" rel="noopener noreferrer" class="btn-qp-view" title="Open PDF in a new tab">
                    <span>👁️</span> View Paper
                </a>
                <a href="{rel_path}" download="{p['name']}" class="btn-qp-download" title="Download PDF directly">
                    <span>⬇️</span> Download
                </a>
            </div>
        </div>
        """)

    all_cards_str = '\n'.join(cards_html)
    return f"""
    <section class="qp-vault-box" id="qp-vault-{sid}">
        <div class="qp-vault-header">
            <div class="qp-vault-title-group">
                <span class="qp-vault-icon">📄</span>
                <div>
                    <h4 class="qp-vault-title">Official KTU University Question Papers &amp; Evaluation Schemes</h4>
                    <p class="qp-vault-subtitle">Genuine examination papers &amp; schemes downloaded directly from the KTU public repository</p>
                </div>
            </div>
            <span class="qp-vault-count">{len(papers)} Papers Available</span>
        </div>
        <div class="qp-cards-grid">
            {all_cards_str}
        </div>
    </section>
    """

# Read existing CSS and JS from gen_site.py
def load_base_assets():
    with open('scratch/gen_site.py', 'r', encoding='utf-8') as f:
        src = f.read()

    css_start = src.find('CSS_STYLES = """') + len('CSS_STYLES = """')
    css_end = src.find('"""\n\nFLOATING_TIMER_HTML')
    css = src[css_start:css_end]

    js_start = src.find('JS_SCRIPT = """') + len('JS_SCRIPT = """')
    js_end = src.find('"""\n\n\nINDEX_TEMPLATE = """')
    js = src[js_start:js_end]

    return css, js

# Build enhanced lightweight CSS for Semester Dropdowns, Subject Themes, and Question Papers
def generate_extra_subject_css():
    extra_css = """
/* =========================================================================
   GLOBAL ANTI-OVERFLOW, STACKING ORDER & RESPONSIVE FIXES
   ========================================================================= */
*, *::before, *::after {
    box-sizing: border-box;
}

html, body {
    overflow-x: hidden !important;
    max-width: 100vw !important;
    width: 100% !important;
    margin: 0;
    padding: 0;
    position: relative;
}

.site-header {
    position: relative;
    z-index: 2000 !important;
}

.main-content, .content-container {
    position: relative;
    z-index: 5 !important;
    max-width: 100% !important;
    overflow-x: hidden !important;
}

/* KaTeX containment: wide matrices scroll inside equation box, never shift page */
.katex-display {
    overflow-x: auto !important;
    overflow-y: hidden !important;
    max-width: 100% !important;
    padding: 0.5rem 0 !important;
    -webkit-overflow-scrolling: touch;
}

.katex {
    max-width: 100% !important;
}

.question-card, .answer-body, .exam-answer, .simple-explanation {
    max-width: 100% !important;
    overflow-wrap: break-word !important;
    word-break: break-word !important;
    box-sizing: border-box !important;
}

pre, code {
    max-width: 100% !important;
    overflow-x: auto !important;
}

/* Controls row lower than semester dropdown menu */
.controls-row {
    position: relative;
    z-index: 10 !important;
}

/* =========================================================================
   SEMESTER DROPDOWN NAVIGATION & QP VAULT STYLES (ULTRA-LIGHTWEIGHT)
   ========================================================================= */
.semester-nav-container {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 0.75rem;
    flex-wrap: wrap;
    background: var(--bg-base);
    padding: 0.45rem 0.75rem;
    border-radius: 14px;
    border: 1px solid var(--border-subtle);
    margin-top: 0.65rem;
    position: relative;
    z-index: 2000 !important;
}

.semester-dropdowns-group {
    display: flex;
    align-items: center;
    gap: 0.55rem;
    flex-wrap: wrap;
}

.sem-nav-heading {
    font-size: 0.78rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--text-muted);
    margin-right: 0.2rem;
}

.sem-dropdown {
    position: relative;
    display: inline-block;
    z-index: 2001 !important;
}

.sem-dropdown.open {
    z-index: 2002 !important;
}

.sem-dropdown-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: var(--bg-surface);
    color: var(--text-main);
    border: 1px solid var(--border-subtle);
    padding: 0.5rem 0.95rem;
    border-radius: 10px;
    font-family: var(--font-main);
    font-size: 0.84rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
    white-space: nowrap;
}

.sem-dropdown-btn:hover {
    background: var(--bg-card-hover);
    border-color: var(--border-focus);
    color: #ffffff;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.25);
}

.sem-dropdown-btn.active-sem {
    background: var(--bg-accent);
    border-color: var(--border-focus);
    box-shadow: 0 0 14px rgba(56, 189, 248, 0.3);
    color: #ffffff;
}

.sem-dropdown-btn .sem-btn-icon {
    font-size: 1rem;
}

.sem-dropdown-btn .sem-btn-count {
    background: rgba(255, 255, 255, 0.08);
    color: var(--text-muted);
    font-size: 0.7rem;
    padding: 0.15rem 0.45rem;
    border-radius: 12px;
    font-weight: 600;
    border: 1px solid var(--border-subtle);
}

.sem-dropdown-btn .sem-btn-arrow {
    font-size: 0.68rem;
    transition: transform 0.2s ease;
    opacity: 0.75;
}

.sem-dropdown.open .sem-dropdown-btn .sem-btn-arrow {
    transform: rotate(180deg);
}

.sem-dropdown-menu {
    position: absolute;
    top: calc(100% + 6px);
    left: 0;
    min-width: 330px;
    background: var(--bg-surface);
    border: 1px solid var(--border-subtle);
    border-radius: 12px;
    box-shadow: 0 16px 45px rgba(0, 0, 0, 0.75);
    padding: 0.4rem;
    display: none;
    flex-direction: column;
    gap: 0.25rem;
    z-index: 99999 !important;
    animation: semMenuFadeIn 0.18s ease-out;
    backdrop-filter: blur(16px);
}

@keyframes semMenuFadeIn {
    from { opacity: 0; transform: translateY(-6px); }
    to { opacity: 1; transform: translateY(0); }
}

.sem-dropdown.open .sem-dropdown-menu {
    display: flex;
}

.sem-menu-header {
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: var(--text-muted);
    padding: 0.4rem 0.7rem 0.25rem;
    border-bottom: 1px solid var(--border-subtle);
    margin-bottom: 0.2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.sem-menu-item {
    display: flex;
    align-items: center;
    gap: 0.65rem;
    padding: 0.55rem 0.75rem;
    border-radius: 8px;
    text-decoration: none;
    color: var(--text-body);
    transition: all 0.15s ease;
    cursor: pointer;
    background: transparent;
    border: 1px solid transparent;
}

.sem-menu-item:hover {
    background: var(--bg-card-hover);
    color: var(--text-main);
    border-color: var(--border-subtle);
    transform: translateX(3px);
}

.sem-menu-item.active {
    background: var(--bg-accent);
    color: #ffffff;
    font-weight: 600;
    border-color: var(--border-focus);
}

.sem-menu-item .item-icon {
    font-size: 1.15rem;
    flex-shrink: 0;
}

.sem-menu-item .item-info {
    display: flex;
    flex-direction: column;
    flex-grow: 1;
    min-width: 0;
}

.sem-menu-item .item-title {
    font-size: 0.84rem;
    font-weight: 600;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.sem-menu-item .item-code {
    font-size: 0.72rem;
    color: var(--text-muted);
}

.sem-menu-item .item-badge-pill {
    font-size: 0.68rem;
    font-weight: 700;
    padding: 0.15rem 0.45rem;
    border-radius: 6px;
    border: 1px solid var(--border-subtle);
    background: rgba(255, 255, 255, 0.05);
    flex-shrink: 0;
}

/* Active Subject Indicator Pill in Navbar */
.active-subject-indicator {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: var(--bg-surface);
    border: 1px solid var(--border-subtle);
    padding: 0.4rem 0.85rem;
    border-radius: 9999px;
    font-size: 0.78rem;
    color: var(--text-main);
    white-space: nowrap;
}

.active-subject-indicator .indicator-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #10b981;
    box-shadow: 0 0 10px #10b981;
    display: inline-block;
    animation: indicatorPulse 2s infinite ease-in-out;
}

@keyframes indicatorPulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.45; transform: scale(0.8); }
}

.active-subject-indicator .indicator-sem-badge {
    background: var(--bg-accent);
    color: var(--text-main);
    font-size: 0.7rem;
    font-weight: 700;
    padding: 0.15rem 0.45rem;
    border-radius: 6px;
    text-transform: uppercase;
}

.active-subject-indicator .indicator-subject-text {
    font-weight: 600;
    color: var(--text-main);
}

/* Hero Action Bar */
.hero-action-buttons {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    flex-wrap: wrap;
    margin-top: 1.25rem;
}

.hero-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.5rem 1rem;
    border-radius: 10px;
    font-size: 0.82rem;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.2s ease;
    border: 1px solid transparent;
}

.hero-btn-qp {
    background: rgba(56, 189, 248, 0.15);
    color: #38bdf8;
    border-color: rgba(56, 189, 248, 0.4);
}
.hero-btn-qp:hover {
    background: rgba(56, 189, 248, 0.28);
    transform: translateY(-2px);
    box-shadow: 0 4px 14px rgba(56, 189, 248, 0.3);
}

.hero-btn-sim {
    background: rgba(245, 158, 11, 0.15);
    color: #f59e0b;
    border-color: rgba(245, 158, 11, 0.4);
}
.hero-btn-sim:hover {
    background: rgba(245, 158, 11, 0.28);
    transform: translateY(-2px);
    box-shadow: 0 4px 14px rgba(245, 158, 11, 0.3);
}

.hero-btn-draw {
    background: rgba(16, 185, 129, 0.15);
    color: #10b981;
    border-color: rgba(16, 185, 129, 0.4);
}
.hero-btn-draw:hover {
    background: rgba(16, 185, 129, 0.28);
    transform: translateY(-2px);
    box-shadow: 0 4px 14px rgba(16, 185, 129, 0.3);
}

/* Question Papers Vault Component */
.qp-vault-box {
    background: var(--bg-card);
    border: 1px solid var(--border-subtle);
    border-radius: 16px;
    padding: 1.5rem;
    margin-bottom: 2rem;
    box-shadow: var(--card-shadow);
}

.qp-vault-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 0.75rem;
    border-bottom: 1px solid var(--border-subtle);
    padding-bottom: 1rem;
    margin-bottom: 1.25rem;
}

.qp-vault-title-group {
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

.qp-vault-icon {
    font-size: 1.8rem;
}

.qp-vault-title {
    font-size: 1.05rem;
    font-weight: 700;
    color: var(--text-main);
    margin: 0;
}

.qp-vault-subtitle {
    font-size: 0.8rem;
    color: var(--text-muted);
    margin: 0.15rem 0 0;
}

.qp-vault-count {
    background: var(--bg-surface);
    color: var(--border-focus);
    border: 1px solid var(--border-subtle);
    padding: 0.3rem 0.75rem;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 700;
}

.qp-cards-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 1rem;
}

.qp-card {
    background: var(--bg-surface);
    border: 1px solid var(--border-subtle);
    border-radius: 12px;
    padding: 1rem;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 0.85rem;
    transition: all 0.2s ease;
}

.qp-card:hover {
    border-color: var(--border-focus);
    transform: translateY(-2px);
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.3);
}

.qp-card-info {
    display: flex;
    flex-direction: column;
    gap: 0.35rem;
}

.qp-badge {
    align-self: flex-start;
    font-size: 0.68rem;
    font-weight: 700;
    padding: 0.15rem 0.5rem;
    border-radius: 6px;
    background: rgba(56, 189, 248, 0.15);
    color: #38bdf8;
    border: 1px solid rgba(56, 189, 248, 0.3);
    text-transform: uppercase;
}

.qp-session-title {
    font-size: 0.9rem;
    font-weight: 700;
    color: var(--text-main);
    margin: 0;
    line-height: 1.35;
}

.qp-meta-text {
    font-size: 0.75rem;
    color: var(--text-muted);
}

.qp-card-actions {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    border-top: 1px solid var(--border-subtle);
    padding-top: 0.65rem;
}

.btn-qp-view, .btn-qp-download {
    flex: 1;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.35rem;
    padding: 0.45rem 0.65rem;
    border-radius: 8px;
    font-size: 0.78rem;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.15s ease;
}

.btn-qp-view {
    background: var(--bg-card);
    color: var(--text-main);
    border: 1px solid var(--border-subtle);
}
.btn-qp-view:hover {
    background: var(--border-focus);
    color: #ffffff;
    border-color: var(--border-focus);
}

.btn-qp-download {
    background: transparent;
    color: var(--text-muted);
    border: 1px solid var(--border-subtle);
}
.btn-qp-download:hover {
    background: var(--bg-card-hover);
    color: var(--text-main);
}

/* Mobile Quick Selector */
.mobile-sem-select-wrapper {
    display: none;
    width: 100%;
    margin-top: 0.4rem;
}

.mobile-sem-select {
    width: 100%;
    background: var(--bg-surface);
    color: var(--text-main);
    border: 1px solid var(--border-subtle);
    padding: 0.55rem 0.9rem;
    border-radius: 10px;
    font-family: var(--font-main);
    font-size: 0.85rem;
    font-weight: 600;
    outline: none;
    cursor: pointer;
}

@media (max-width: 900px) {
    .semester-dropdowns-group {
        width: 100%;
        justify-content: flex-start;
        overflow: visible !important;
        flex-wrap: wrap;
        gap: 0.45rem;
        padding-bottom: 0.2rem;
    }
    .sem-dropdown-menu {
        position: absolute;
        left: 0;
        min-width: 280px;
        max-width: calc(100vw - 2rem);
        z-index: 99999 !important;
    }
    .active-subject-indicator {
        display: none;
    }
    .mobile-sem-select-wrapper {
        display: block;
    }
}

.footer-subject-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 1.5rem;
    margin-bottom: 2rem;
    text-align: left;
}
.footer-group-title {
    font-size: 0.85rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--text-muted);
    margin-bottom: 0.6rem;
}
.footer-links-col {
    display: flex;
    flex-direction: column;
    gap: 0.35rem;
}
.footer-links-col a {
    color: var(--text-body);
    font-size: 0.82rem;
    text-decoration: none;
    transition: color 0.15s ease;
}
.footer-links-col a:hover {
    color: var(--border-focus);
}
"""

    for s in SUBJECTS_CONFIG:
        sid = s["id"]
        col = s["color"]
        glow = s["glow"]
        extra_css += f"""
/* Subject {sid.upper()} Styles */
.question-card.subject-{sid} {{
    border-left: 5px solid {col};
}}
.hero-{sid} {{
    background: radial-gradient(circle at top right, {glow}, transparent 70%), var(--bg-surface);
    border: 1px solid var(--border-subtle);
}}
.hero-{sid} .hero-badge {{
    background: rgba(255, 255, 255, 0.08);
    color: {col};
    border: 1px solid {glow};
}}
"""
    return extra_css

def generate_enhanced_js():
    return """
// =========================================================================
// Ultra-Fast On-Demand KaTeX Rendering & Dropdown Switching
// =========================================================================
function toggleSemDropdown(semKey, e) {
    if (e) {
        e.stopPropagation();
        e.preventDefault();
    }
    const targetDropdown = document.getElementById('sem-dropdown-' + semKey);
    const allDropdowns = document.querySelectorAll('.sem-dropdown');
    
    allDropdowns.forEach(d => {
        if (d !== targetDropdown) {
            d.classList.remove('open');
        }
    });

    if (targetDropdown) {
        targetDropdown.classList.toggle('open');
    }
}

// Close dropdowns on outside click
document.addEventListener('click', (e) => {
    if (!e.target.closest('.sem-dropdown')) {
        document.querySelectorAll('.sem-dropdown').forEach(d => d.classList.remove('open'));
    }
});

function selectSubjectFromMenu(targetViewId, e) {
    if (e) {
        e.preventDefault();
    }
    document.querySelectorAll('.sem-dropdown').forEach(d => d.classList.remove('open'));
    switchTab(targetViewId);
}

function handleMobileSelect(val) {
    if (!val) return;
    switchTab(val);
}

// High-Performance On-Demand Math Renderer
function renderMathForView(viewId) {
    const viewEl = document.getElementById(viewId);
    if (!viewEl || viewEl.getAttribute('data-math-rendered') === 'true') return;
    if (window.renderMathInElement) {
        window.renderMathInElement(viewEl, {
            delimiters: [
                {left: '$$', right: '$$', display: true},
                {left: '$', right: '$', display: false}
            ],
            throwOnError: false
        });
        viewEl.setAttribute('data-math-rendered', 'true');
    }
}

// Fast SwitchTab: Loads Only Active Subject Equations
function switchTab(targetId) {
    if (!targetId) return;

    // 1. Activate View
    const subjectViews = document.querySelectorAll('.subject-view');
    subjectViews.forEach(view => {
        if (view.id === targetId) {
            view.classList.add('active');
        } else {
            view.classList.remove('active');
        }
    });

    // 2. Find matching menu item to extract metadata
    const menuItems = document.querySelectorAll('.sem-menu-item');
    let activeSem = 's7';
    let activeTitle = '';
    let activeCode = '';
    let activeIcon = '📘';

    menuItems.forEach(item => {
        if (item.getAttribute('data-target') === targetId) {
            item.classList.add('active');
            activeSem = item.getAttribute('data-sem') || 's7';
            activeTitle = item.getAttribute('data-title') || '';
            activeCode = item.getAttribute('data-code') || '';
            activeIcon = item.getAttribute('data-icon') || '📘';
        } else {
            item.classList.remove('active');
        }
    });

    // 3. Highlight the active semester button
    document.querySelectorAll('.sem-dropdown-btn').forEach(btn => {
        if (btn.getAttribute('data-sem') === activeSem) {
            btn.classList.add('active-sem');
        } else {
            btn.classList.remove('active-sem');
        }
    });

    // 4. Update the Active Subject Indicator Pill
    const indSem = document.getElementById('indicator-sem');
    const indTitle = document.getElementById('indicator-title');
    if (indSem) {
        const semLabels = { 's1s2': 'S1 / S2 Foundation', 's6': 'S6 EEE', 's7': 'S7 EEE' };
        indSem.textContent = semLabels[activeSem] || activeSem.toUpperCase();
    }
    if (indTitle && activeTitle) {
        indTitle.textContent = `${activeIcon} ${activeTitle} (${activeCode})`;
    }

    // 5. Sync mobile dropdown
    const mobSelect = document.getElementById('mobile-subject-selector');
    if (mobSelect) {
        mobSelect.value = targetId;
    }

    // 6. Fast targeted KaTeX math rendering (Render ONLY active subject, cache result)
    renderMathForView(targetId);

    // 7. Update URL hash
    try {
        history.replaceState(null, null, '#' + targetId);
    } catch (e) {}

    applyFilters();
    window.scrollTo({ left: 0, top: 0, behavior: 'instant' });
    document.documentElement.scrollLeft = 0;
    document.body.scrollLeft = 0;
}

// Initial Fast Page Load: Render ONLY default view, reset scroll to top
window.addEventListener('DOMContentLoaded', () => {
    window.scrollTo({ left: 0, top: 0, behavior: 'instant' });
    document.documentElement.scrollLeft = 0;
    document.body.scrollLeft = 0;

    let initialView = 'view-acs';
    const hash = window.location.hash;
    if (hash && hash.startsWith('#view-')) {
        initialView = hash.replace('#', '');
    }
    switchTab(initialView);
    window.scrollTo({ left: 0, top: 0, behavior: 'instant' });
});

// Prevent accidental horizontal drift
window.addEventListener('scroll', () => {
    if (window.scrollX !== 0) {
        window.scrollTo({ left: 0, top: window.scrollY, behavior: 'instant' });
    }
}, { passive: true });
"""

FLOATING_TIMER_HTML = """
    <!-- Floating Active Exam Practice Timer (Top-Right Glassmorphism Pill) -->
    <div id="floating-timer" class="floating-timer-widget" style="display:none;" role="region" aria-label="Floating Exam Practice Timer">
        <div class="floating-timer-header">
            <span class="pendulum-icon" id="floating-pendulum" title="Rhythmic mechanical escapement tick">⏱️</span>
            <span class="floating-qid" id="floating-qid">Q-TIMER</span>
            <div class="floating-controls">
                <button type="button" class="float-sound-btn" onclick="toggleTimerSound()" title="Toggle ticking sound">🔊 Sound</button>
                <button type="button" class="float-close-btn" onclick="closeFloatingTimer()" title="Close floating timer widget">&times;</button>
            </div>
        </div>
        <div class="floating-timer-body">
            <div class="floating-time-display" id="floating-time-display">00:00</div>
            <div class="floating-progress-container">
                <div class="floating-progress-bar" id="floating-progress-bar" style="width: 100%;"></div>
            </div>
        </div>
        <div class="floating-timer-footer">
            <button type="button" class="float-btn float-pause-btn" id="floating-pause-btn" onclick="toggleActiveTimer()">
                <span class="float-btn-icon" id="floating-action-icon">⏸️</span>
                <span id="floating-action-text">Pause</span>
            </button>
            <button type="button" class="float-btn float-reset-btn" onclick="resetActiveTimer()">🔄 Reset</button>
            <button type="button" class="float-btn float-jump-btn" onclick="scrollToActiveCard()">🎯 Jump to Card</button>
        </div>
    </div>
"""

# Render Semester Dropdown Navigation Component
def render_semester_nav_bar(is_index=True, current_sid="acs"):
    subj_map = {s["id"]: s for s in SUBJECTS_CONFIG}

    active_sem_key = "s7"
    if current_sid:
        for sem in SEMESTERS_DATA:
            if current_sid in sem["ids"]:
                active_sem_key = sem["key"]
                break

    dropdowns_html = []
    mobile_options = ['<option value="">Jump to any subject...</option>']

    for sem in SEMESTERS_DATA:
        sem_key = sem["key"]
        is_sem_active = (sem_key == active_sem_key)
        btn_active_class = "active-sem" if is_sem_active else ""

        items_html = []
        mobile_options.append(f'<optgroup label="{sem["icon"]} {sem["title"]}">')

        for sid in sem["ids"]:
            s = subj_map[sid]
            is_item_active = (sid == current_sid)
            item_active_class = "active" if is_item_active else ""
            q_cnt = sum(len(m["questions"]) for m in s["modules"])

            if is_index:
                items_html.append(f"""
                <a href="#view-{sid}" class="sem-menu-item {item_active_class}" data-target="view-{sid}" data-sem="{sem_key}" data-title="{html.escape(s['title'])}" data-code="{s['code']}" data-icon="{s['icon']}" onclick="selectSubjectFromMenu('view-{sid}', event)">
                    <span class="item-icon">{s['icon']}</span>
                    <div class="item-info">
                        <span class="item-title">{s['title']}</span>
                        <span class="item-code">{s['code']} &bull; {q_cnt} Qs</span>
                    </div>
                    <span class="item-badge-pill" style="border-color: {s['color']}; color: {s['color']};">{s['code']}</span>
                </a>
                """)
                mobile_options.append(f'<option value="view-{sid}" {"selected" if is_item_active else ""}>{s["icon"]} {s["title"]} ({s["code"]})</option>')
            else:
                items_html.append(f"""
                <a href="{s['filename']}" class="sem-menu-item {item_active_class}" data-sem="{sem_key}">
                    <span class="item-icon">{s['icon']}</span>
                    <div class="item-info">
                        <span class="item-title">{s['title']}</span>
                        <span class="item-code">{s['code']} &bull; {q_cnt} Qs</span>
                    </div>
                    <span class="item-badge-pill" style="border-color: {s['color']}; color: {s['color']};">{s['code']}</span>
                </a>
                """)
                mobile_options.append(f'<option value="{s["filename"]}" {"selected" if is_item_active else ""}>{s["icon"]} {s["title"]} ({s["code"]})</option>')

        mobile_options.append('</optgroup>')

        dropdowns_html.append(f"""
        <div class="sem-dropdown" id="sem-dropdown-{sem_key}">
            <button type="button" class="sem-dropdown-btn {btn_active_class}" data-sem="{sem_key}" onclick="toggleSemDropdown('{sem_key}', event)" aria-haspopup="true" aria-expanded="false" title="Click to view {sem['title']} subjects">
                <span class="sem-btn-icon">{sem['icon']}</span>
                <span class="sem-btn-label">{sem['title']}</span>
                <span class="sem-btn-count">{sem['badge']}</span>
                <span class="sem-btn-arrow">▾</span>
            </button>
            <div class="sem-dropdown-menu" id="menu-{sem_key}">
                <div class="sem-menu-header">
                    <span>{sem['icon']} {sem['title']}</span>
                    <span>{sem['badge']}</span>
                </div>
                {''.join(items_html)}
            </div>
        </div>
        """)

    current_subj = subj_map.get(current_sid, SUBJECTS_CONFIG[0])
    sem_label_active = "S7 EEE" if active_sem_key == "s7" else ("S6 EEE" if active_sem_key == "s6" else "S1 / S2 Foundation")

    return f"""
    <div class="semester-nav-container">
        <div class="semester-dropdowns-group">
            <span class="sem-nav-heading">Semester:</span>
            {''.join(dropdowns_html)}
        </div>

        <div class="active-subject-indicator" id="active-subject-indicator" title="Current course loaded">
            <span class="indicator-dot"></span>
            <span class="indicator-sem-badge" id="indicator-sem">{sem_label_active}</span>
            <span class="indicator-subject-text" id="indicator-title">{current_subj['icon']} {current_subj['title']} ({current_subj['code']})</span>
        </div>

        <div class="mobile-sem-select-wrapper">
            <select class="mobile-sem-select" id="mobile-subject-selector" onchange="{'handleMobileSelect(this.value)' if is_index else 'if(this.value) window.location.href=this.value;'}">
                {''.join(mobile_options)}
            </select>
        </div>
    </div>
    """

# Build standalone page HTML
def generate_standalone_page(s_info, inner_html, all_css, all_js):
    s_title = s_info["title"]
    s_code = s_info["code"]
    s_id = s_info["id"]

    sem_nav_html = render_semester_nav_bar(is_index=False, current_sid=s_id)

    template = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>{s_title} ({s_code}) | KTU Exam Portal</title>
    
    <!-- Instant Anti-FOUC Theme Preload Script -->
    <script>
        (function() {{
            const savedTheme = localStorage.getItem('ktu_portal_theme') || 'dark';
            document.documentElement.setAttribute('data-theme', savedTheme);
            const savedLang = localStorage.getItem('ktu_portal_lang') || 'en';
            document.documentElement.setAttribute('data-lang', savedLang);
        }})();
    </script>

    <!-- KaTeX CDN with Fast On-Demand Auto-Render -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
        onload="renderMathInElement(document.querySelector('.main-content'), {{
            delimiters: [
                {{left: '$$', right: '$$', display: true}},
                {{left: '$', right: '$', display: false}}
            ],
            throwOnError: false
        }});"></script>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&family=Noto+Sans+Malayalam:wght@400;500;600;700&display=swap" rel="stylesheet">

    <style>
        {all_css}
    </style>
</head>
<body>
    <header class="site-header">
        <div class="header-top-row">
            <div class="brand-container">
                <div class="brand-logo-icon">⚡</div>
                <div class="brand-text">
                    <h1>{s_title} ({s_code})</h1>
                    <p>KTU Engineering B.Tech Examination Preparation</p>
                </div>
            </div>

            <!-- Interactive Features -->
            <nav class="feature-nav-bar" aria-label="Interactive Learning Features">
                <a href="index.html" class="feature-nav-link" title="Return to Portal Home &amp; All 15 Subjects">📚 All Subjects (15)</a>
                <a href="animations.html" class="feature-nav-link" title="60fps Real-Time Motion Graphics &amp; Simulators Window">🎬 60fps Simulators</a>
                <a href="mindmap.html" class="feature-nav-link" title="Large Interactive Neural Mind Map with glowing synapses">🧠 Mind Map</a>
                <a href="activities.html" class="feature-nav-link" title="Gamified Focus Lab, Nano Banana Portals &amp; Engineering Drills">🎯 Focus Lab</a>
                <a href="draw.html" class="feature-nav-link" title="Interactive Muscle Memory Canvas: Trace &amp; Draw Engineering Diagrams">✏️ Muscle Memory Canvas</a>
            </nav>

            <!-- Language Switcher -->
            <div class="lang-switcher-wrapper" role="radiogroup" aria-label="Language &amp; Tone Selector">
                <button class="lang-btn active" data-lang-value="en" title="English: University Standard Exam Answers" aria-label="English">
                    <span class="lang-flag">🇬🇧</span>
                    <span class="lang-name">English</span>
                </button>
                <button class="lang-btn" data-lang-value="manglish" title="Manglish: Malayalam in English text with local campus tone" aria-label="Manglish">
                    <span class="lang-flag">🌴</span>
                    <span class="lang-name">Manglish</span>
                </button>
                <button class="lang-btn" data-lang-value="ml" title="മലയാളം: പ്രാദേശിക സംഭാഷണ ശൈലി" aria-label="Malayalam">
                    <span class="lang-flag">🇮🇳</span>
                    <span class="lang-name">മലയാളം</span>
                </button>
            </div>

            <!-- Theme Switcher -->
            <div class="theme-palette-wrapper">
                <span class="theme-palette-label">Theme:</span>
                <div class="theme-btn-group" role="radiogroup" aria-label="Reading &amp; Study Theme Selector">
                    <button class="theme-btn" data-theme-value="dark" title="Soft Charcoal &amp; Slate" aria-label="Dark Mode">
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
                    <button class="theme-btn" data-theme-value="light" title="Warm Slate &amp; Off-White Paper" aria-label="Light Mode">
                        <span class="theme-swatch swatch-light"></span>
                        <span class="theme-title">Day</span>
                    </button>
                    <button class="theme-btn" data-theme-value="sage" title="Sage &amp; Soft Olive Focus" aria-label="Sage Mode">
                        <span class="theme-swatch swatch-sage"></span>
                        <span class="theme-title">Sage</span>
                    </button>
                </div>
            </div>
        </div>

        {sem_nav_html}
    </header>

    <main class="main-content">
        <section class="exam-strategy-banner">
            <div class="strategy-icon">⏱️</div>
            <div class="strategy-details">
                <h4>3-Hour Exam Time Budget (20 Questions / 100 Marks Strategy)</h4>
                <p><strong>Part A (10 Short Answers &times; 3 Marks = 30M):</strong> Allocate <strong>5 mins per answer</strong> (50 mins total) &mdash; target &frac12; to 1 page highlighting key formula and core definition.<br>
                <strong>Part B (10 Essay Answers &times; 7 Marks = 70M):</strong> Allocate <strong>12 mins per answer</strong> (120 mins total) &mdash; target 1.5 to 2 pages with schematic circuit/block diagrams and step-by-step derivations.<br>
                <strong>Strategy &amp; Review Buffer (10 mins):</strong> 5 mins at start for question choice planning + 5 mins at end for question numbering and equation verification.</p>
            </div>
        </section>
        {inner_html}
    </main>

    {FLOATING_TIMER_HTML}

    <button class="back-to-top-btn" id="back-to-top" onclick="window.scrollTo({{top: 0, behavior: 'smooth'}})" title="Scroll to top of page">
        <span>↑</span> Top
    </button>

    <footer class="site-footer">
        <p>&copy; 2026 Academic Engineering Portal. {s_title} ({s_code}) Edition.</p>
    </footer>

    <script>
        {all_js}
    </script>
</body>
</html>
"""
    return template

def main():
    print("=" * 70)
    print("KTU MASTER PORTAL GENERATOR: ULTRA-FAST & LIGHTWEIGHT (SIMULATORS IN 60FPS WINDOW)")
    print("=" * 70)

    base_css, base_js = load_base_assets()
    all_css = base_css + "\n" + generate_extra_subject_css()
    all_js = base_js + "\n" + generate_enhanced_js()

    views_html = []
    subject_counts = {}
    grand_total = 0

    for idx, s in enumerate(SUBJECTS_CONFIG):
        sid = s["id"]
        mods = s["modules"]
        q_count = sum(len(m["questions"]) for m in mods)
        subject_counts[sid] = q_count
        grand_total += q_count

        # Module questions HTML
        mod_cards = '\n'.join([render_module_section(m, f"subject-{sid}") for m in mods])

        # Question Papers Vault Section
        qp_vault_html = render_question_papers_box(sid)
        num_qps = len(QP_CATALOG.get(sid, []))

        # Syllabus section for mobile
        syl_block = render_mobile_syllabus_section() + '\n' if sid == "mobile" else ""

        # Hero Action Buttons with targeted subject filter for 60fps simulator window
        sim_param_map = {
            "acs": "acs",
            "drive": "drive",
            "drives": "drive",
            "mobile": "mobile",
            "lcs": "lcs",
            "pe": "pe",
        }
        sim_target = sim_param_map.get(sid, "all")
        sim_url = f"animations.html?subject={sim_target}"

        hero_actions = f"""
        <div class="hero-action-buttons">
            <a href="#qp-vault-{sid}" class="hero-btn hero-btn-qp" title="View official university question papers and answer schemes">
                <span>📄</span> University Question Papers ({num_qps})
            </a>
            <a href="{sim_url}" class="hero-btn hero-btn-sim" title="Launch real-time 60fps simulators in dedicated simulator window">
                <span>🎬</span> 60fps Simulators Window
            </a>
            <a href="draw.html" class="hero-btn hero-btn-draw" title="Practice diagram blueprints in muscle memory canvas">
                <span>✏️</span> Drawing Blueprints
            </a>
        </div>
        """

        active_view_class = "active" if sid == "acs" else ""
        view_content = f"""
        <!-- VIEW {idx+1}: {s['title']} ({s['code']}) -->
        <div id="view-{sid}" class="subject-view {active_view_class}">
            <div class="subject-hero hero-{sid}">
                <span class="hero-badge">Course Code: {s['code']} &bull; {len(mods)} Modules &bull; {q_count} Questions</span>
                <h2>{s['title']}</h2>
                <p>{s['hero_desc']}</p>
                {hero_actions}
            </div>
            {qp_vault_html}
            {syl_block}
            {mod_cards}
        </div>
        """
        views_html.append(view_content)

        # Generate standalone page
        standalone_inner = f"""
        <div class="subject-hero hero-{sid}">
            <span class="hero-badge">Course Code: {s['code']} &bull; {len(mods)} Modules &bull; {q_count} Questions</span>
            <h2>{s['title']}</h2>
            <p>{s['hero_desc']}</p>
            {hero_actions}
        </div>
        {qp_vault_html}
        {syl_block}
        {mod_cards}
        """
        standalone_html = generate_standalone_page(s, standalone_inner, all_css, all_js)
        with open(s["filename"], "w", encoding="utf-8") as sf:
            sf.write(standalone_html)
        print(f"  [+] Standalone: {s['filename']:24s} ({len(standalone_html):,} bytes, {q_count} Qs, {num_qps} QPs)")

    # Footer links grouped by Semester
    footer_cols = []
    for sem in SEMESTERS_DATA:
        links = []
        for sid in sem["ids"]:
            s = next(item for item in SUBJECTS_CONFIG if item["id"] == sid)
            links.append(f'<a href="#{s["filename"]}" onclick="switchTab(\'view-{s["id"]}\')">{s["title"]} ({s["code"]})</a>')
        col_html = f"""
        <div class="footer-col">
            <div class="footer-group-title">{sem['icon']} {sem['title']}</div>
            <div class="footer-links-col">
                {''.join(links)}
            </div>
        </div>
        """
        footer_cols.append(col_html)
    footer_grouped_str = f'<div class="footer-subject-grid">{"".join(footer_cols)}</div>'

    # Build Index Dropdown Navigation Bar
    sem_nav_index_html = render_semester_nav_bar(is_index=True, current_sid="acs")
    all_views_str = '\n'.join(views_html)

    index_html = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>KTU Engineering Exam Portal | S1/S2, S6, S7 Semesters &bull; 406 Questions &bull; Question Papers</title>
    
    <!-- Instant Anti-FOUC Theme Preload Script -->
    <script>
        (function() {{
            const savedTheme = localStorage.getItem('ktu_portal_theme') || 'dark';
            document.documentElement.setAttribute('data-theme', savedTheme);
            const savedLang = localStorage.getItem('ktu_portal_lang') || 'en';
            document.documentElement.setAttribute('data-lang', savedLang);
        }})();
    </script>

    <!-- KaTeX CDN with Fast On-Demand Math Rendering -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>

    <!-- Google Fonts: Inter & JetBrains Mono -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&family=Noto+Sans+Malayalam:wght@400;500;600;700&display=swap" rel="stylesheet">

    <style>
        {all_css}
    </style>
</head>
<body>

    <!-- Header & Navigation Bar -->
    <header class="site-header">
        <div class="header-top-row">
            <div class="brand-container">
                <div class="brand-logo-icon" aria-hidden="true">⚡</div>
                <div class="brand-text">
                    <h1>KTU Mastery Portal</h1>
                    <p class="brand-subtext">Semester-Wise Exam Vault: S1/S2, S6 &amp; S7 ({grand_total} Questions &bull; Authentic PYQs)</p>
                </div>
            </div>

            <!-- Interactive Features: 60fps Simulators strictly in animations.html -->
            <nav class="feature-nav-bar" aria-label="Interactive Learning Features">
                <a href="animations.html" class="feature-nav-link" title="Launch real-time 60fps motion graphics and physics simulators window">🎬 60fps Simulators</a>
                <a href="mindmap.html" class="feature-nav-link" title="Large Interactive Neural Mind Map with glowing synapses">🧠 Mind Map</a>
                <a href="activities.html" class="feature-nav-link" title="Gamified Focus Lab, Nano Banana Portals &amp; Engineering Drills">🎯 Focus Lab</a>
                <a href="draw.html" class="feature-nav-link" title="Interactive Muscle Memory Canvas: Trace &amp; Draw Engineering Diagrams">✏️ Muscle Memory Canvas</a>
            </nav>

            <!-- Tone / Language Switcher Controls -->
            <div class="lang-switcher-wrapper" role="radiogroup" aria-label="Language &amp; Tone Selector">
                <button class="lang-btn active" data-lang-value="en" title="English: University Standard Exam Answers" aria-label="English">
                    <span class="lang-flag">🇬🇧</span>
                    <span class="lang-name">English</span>
                </button>
                <button class="lang-btn" data-lang-value="manglish" title="Manglish: Malayalam in English text with local campus tone" aria-label="Manglish">
                    <span class="lang-flag">🌴</span>
                    <span class="lang-name">Manglish</span>
                </button>
                <button class="lang-btn" data-lang-value="ml" title="മലയാളം: പ്രാദേശിക സംഭാഷണ ശൈലി" aria-label="Malayalam">
                    <span class="lang-flag">🇮🇳</span>
                    <span class="lang-name">മലയാളം</span>
                </button>
            </div>

            <!-- Theme Switcher Controls -->
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

        <!-- Semester Dropdown Bar: S1/S2, S6, S7 -->
        {sem_nav_index_html}

        <!-- Controls: Search and Dynamic Filtering -->
        <div class="controls-row">
            <div class="search-box-wrapper">
                <span class="search-icon">🔍</span>
                <input type="text" id="global-search" class="search-input" placeholder="Search questions, derivations, equations, concepts in active subject...">
            </div>

            <div class="filter-buttons">
                <button class="filter-btn active" data-filter="all">All Questions</button>
                <button class="filter-btn" data-filter="3m">3 Marks Only</button>
                <button class="filter-btn" data-filter="7m">7/14 Marks Only</button>
                <button class="filter-btn global-collapse-btn" id="btn-toggle-all-answers" onclick="toggleAllAnswers()" title="Collapse all answers for Self-Test / Flashcard Exam Practice">
                    <span class="btn-icon">👁️</span>
                    <span class="btn-text">Collapse All Answers</span>
                </button>
                <span class="stats-badge" id="stats-pill">{grand_total} Master Answers Available</span>
            </div>
        </div>
    </header>

    <!-- Main Content Container containing 15 Integrated Views -->
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

        {all_views_str}

    </main>

    {FLOATING_TIMER_HTML}

    <!-- Floating Back to Top Button -->
    <button class="back-to-top-btn" id="back-to-top" onclick="scrollToTop()" title="Scroll to top of page">
        <span>↑</span> Top
    </button>

    <!-- Footer -->
    <footer class="site-footer">
        <div class="footer-content">
            {footer_grouped_str}
            <p>Designed for APJ Abdul Kalam Technological University (KTU) Engineering Students. Formatted with rigorous paragraph-style academic answers, step-by-step mathematical derivations with KaTeX, explicit image placeholders, and targeted YouTube problem-solving video links.</p>
            <p>&copy; 2026 Academic Engineering Portal. S1/S2, S6, S7 Semesters &bull; 406 Master University Questions.</p>
        </div>
    </footer>

    <!-- Interactive Client-Side JavaScript -->
    <script>
        {all_js}
    </script>
</body>
</html>
"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index_html)
    print("=" * 70)
    print(f"[SUCCESS] Generated index.html successfully ({len(index_html):,} bytes, {grand_total} questions across 15 subjects)!")
    print("=" * 70)

if __name__ == "__main__":
    main()
