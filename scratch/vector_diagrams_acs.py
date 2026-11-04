# -*- coding: utf-8 -*-
"""
vector_diagrams_acs.py
======================
Pure interactive vector SVG definitions and spatial geometry for Advanced Control Systems (EET401).
"""

ACS_DIAGRAMS = [
    # -------------------------------------------------------------------------
    # 0. General Continuous-Time LTI System State-Space Block Diagram (acs-q2)
    # -------------------------------------------------------------------------
    {
        "qid": "acs-q2",
        "aliases": ["acs-q1", "acs-q2", "acs-q3", "acs-q6", "acs-q7b", "acs-q8", "acs-q9", "acs-q9b", "acs-q10"],
        "title": "State-Space Block Diagram Representation of Continuous-Time LTI System",
        "module": 1,
        "marks": "6 Marks Guaranteed",
        "desc": "Trace the fundamental vector state equations governing modern control engineering: \\dot{x} = Ax + Bu and y = Cx + Du!",
        "equation": r"\dot{\mathbf{x}}(t) = \mathbf{A}\mathbf{x}(t) + \mathbf{B}\mathbf{u}(t), \quad \mathbf{y}(t) = \mathbf{C}\mathbf{x}(t) + \mathbf{D}\mathbf{u}(t)",
        "marking_tip": "KTU Examiners allocate 2 marks for the input-to-state integrator loop (B, Summer 1, Integrator 1/s, and feedback matrix A), 2 marks for output summing logic (C and Summer 2), and 2 marks for direct feedforward transmission matrix D.",
        "svg_viewBox": "0 0 1000 580",
        "ghost_svg": """
            <!-- Input u(t) -->
            <path d="M 60 260 L 160 260" class="ghost-stroke"/>
            <polygon points="160,260 148,254 148,266" class="ghost-fill"/>
            <text x="100" y="245" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="600">u(t)</text>

            <!-- Input Matrix B -->
            <rect x="160" y="215" width="90" height="90" rx="8" class="ghost-fill"/>
            <text x="205" y="270" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="24" font-weight="700" text-anchor="middle">B</text>

            <!-- Arrow B to Summer 1 -->
            <path d="M 250 260 L 330 260" class="ghost-stroke"/>
            <polygon points="330,260 318,254 318,266" class="ghost-fill"/>

            <!-- Summer 1 -->
            <circle cx="355" cy="260" r="25" class="ghost-fill"/>
            <text x="355" y="267" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="20" font-weight="700" text-anchor="middle">+</text>

            <!-- x_dot(t) -->
            <path d="M 380 260 L 460 260" class="ghost-stroke"/>
            <polygon points="460,260 448,254 448,266" class="ghost-fill"/>
            <text x="415" y="245" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="600" text-anchor="middle">ẋ(t)</text>

            <!-- Integrator 1/s -->
            <rect x="460" y="215" width="100" height="90" rx="8" class="ghost-fill"/>
            <text x="510" y="260" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="22" font-weight="700" text-anchor="middle">∫ dt</text>
            <text x="510" y="285" fill="#475569" font-family="'JetBrains Mono', monospace" font-size="12" text-anchor="middle">(1/s)</text>

            <!-- State x(t) pickoff -->
            <path d="M 560 260 L 680 260" class="ghost-stroke"/>
            <polygon points="680,260 668,254 668,266" class="ghost-fill"/>
            <circle cx="620" cy="260" r="6" class="ghost-fill"/>
            <text x="615" y="245" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="15" font-weight="600" text-anchor="middle">x(t)</text>

            <!-- Output Matrix C -->
            <rect x="680" y="215" width="90" height="90" rx="8" class="ghost-fill"/>
            <text x="725" y="270" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="24" font-weight="700" text-anchor="middle">C</text>

            <!-- Arrow C to Summer 2 -->
            <path d="M 770 260 L 835 260" class="ghost-stroke"/>
            <polygon points="835,260 823,254 823,266" class="ghost-fill"/>

            <!-- Summer 2 -->
            <circle cx="860" cy="260" r="25" class="ghost-fill"/>
            <text x="860" y="267" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="20" font-weight="700" text-anchor="middle">+</text>

            <!-- Output y(t) -->
            <path d="M 885 260 L 960 260" class="ghost-stroke"/>
            <polygon points="960,260 948,254 948,266" class="ghost-fill"/>
            <text x="925" y="245" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="600">y(t)</text>

            <!-- Matrix A in Feedback Loop -->
            <path d="M 620 260 L 620 420 L 560 420" class="ghost-stroke"/>
            <polygon points="560,420 572,414 572,426" class="ghost-fill"/>
            <rect x="460" y="375" width="100" height="90" rx="8" class="ghost-fill"/>
            <text x="510" y="430" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="24" font-weight="700" text-anchor="middle">A</text>
            <path d="M 460 420 L 355 420 L 355 285" class="ghost-stroke"/>
            <polygon points="355,285 349,297 361,297" class="ghost-fill"/>

            <!-- Matrix D in Feedforward Loop -->
            <circle cx="110" cy="260" r="5" class="ghost-fill"/>
            <path d="M 110 260 L 110 100 L 460 100" class="ghost-stroke"/>
            <polygon points="460,100 448,94 448,106" class="ghost-fill"/>
            <rect x="460" y="55" width="100" height="90" rx="8" class="ghost-fill"/>
            <text x="510" y="110" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="24" font-weight="700" text-anchor="middle">D</text>
            <path d="M 560 100 L 860 100 L 860 235" class="ghost-stroke"/>
            <polygon points="860,235 854,223 866,223" class="ghost-fill"/>
        """,
        "components": [
            {
                "id": "comp-input-b",
                "name": "Input Matrix B & Signal u(t)",
                "center": [205, 260],
                "radius": 45,
                "svg": """
                    <g id="comp-input-b" class="active-comp" filter="url(#glow-cyan)">
                        <path d="M 60 260 L 160 260" stroke="#06b6d4" stroke-width="3"/>
                        <polygon points="160,260 148,254 148,266" fill="#06b6d4"/>
                        <text x="100" y="245" fill="#a5f3fc" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700">u(t)</text>
                        <rect x="160" y="215" width="90" height="90" rx="8" fill="rgba(6, 182, 212, 0.2)" stroke="#06b6d4" stroke-width="2.5"/>
                        <text x="205" y="270" fill="#e0f2fe" font-family="'JetBrains Mono', monospace" font-size="24" font-weight="800" text-anchor="middle">B</text>
                    </g>
                """
            },
            {
                "id": "comp-summer1",
                "name": "State Derivative Summing Junction",
                "center": [355, 260],
                "radius": 40,
                "svg": """
                    <g id="comp-summer1" class="active-comp" filter="url(#glow-gold)">
                        <path d="M 250 260 L 330 260" stroke="#f59e0b" stroke-width="2.5"/>
                        <polygon points="330,260 318,254 318,266" fill="#f59e0b"/>
                        <circle cx="355" cy="260" r="25" fill="rgba(245, 158, 11, 0.2)" stroke="#f59e0b" stroke-width="2.5"/>
                        <text x="355" y="267" fill="#fef3c7" font-family="'JetBrains Mono', monospace" font-size="20" font-weight="800" text-anchor="middle">+</text>
                    </g>
                """
            },
            {
                "id": "comp-integrator",
                "name": "Continuous State Integrator (1/s)",
                "center": [510, 260],
                "radius": 45,
                "svg": """
                    <g id="comp-integrator" class="active-comp" filter="url(#glow-green)">
                        <path d="M 380 260 L 460 260" stroke="#10b981" stroke-width="2.5"/>
                        <polygon points="460,260 448,254 448,266" fill="#10b981"/>
                        <text x="415" y="245" fill="#a7f3d0" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700" text-anchor="middle">ẋ(t)</text>
                        <rect x="460" y="215" width="100" height="90" rx="8" fill="rgba(16, 185, 129, 0.2)" stroke="#10b981" stroke-width="2.5"/>
                        <text x="510" y="260" fill="#ecfdf5" font-family="'JetBrains Mono', monospace" font-size="22" font-weight="800" text-anchor="middle">∫ dt</text>
                        <text x="510" y="285" fill="#6ee7b7" font-family="'JetBrains Mono', monospace" font-size="12" text-anchor="middle">(1/s)</text>
                    </g>
                """
            },
            {
                "id": "comp-matrix-a",
                "name": "System Matrix A (State Feedback)",
                "center": [510, 420],
                "radius": 45,
                "svg": """
                    <g id="comp-matrix-a" class="active-comp" filter="url(#glow-pink)">
                        <path d="M 620 260 L 620 420 L 560 420" stroke="#ec4899" stroke-width="2.5"/>
                        <polygon points="560,420 572,414 572,426" fill="#ec4899"/>
                        <rect x="460" y="375" width="100" height="90" rx="8" fill="rgba(236, 72, 153, 0.2)" stroke="#ec4899" stroke-width="2.5"/>
                        <text x="510" y="430" fill="#fdf2f8" font-family="'JetBrains Mono', monospace" font-size="24" font-weight="800" text-anchor="middle">A</text>
                        <path d="M 460 420 L 355 420 L 355 285" stroke="#ec4899" stroke-width="2.5"/>
                        <polygon points="355,285 349,297 361,297" fill="#ec4899"/>
                    </g>
                """
            },
            {
                "id": "comp-matrix-c",
                "name": "Output Matrix C & State Pickoff x(t)",
                "center": [725, 260],
                "radius": 45,
                "svg": """
                    <g id="comp-matrix-c" class="active-comp" filter="url(#glow-cyan)">
                        <path d="M 560 260 L 680 260" stroke="#06b6d4" stroke-width="2.5"/>
                        <polygon points="680,260 668,254 668,266" fill="#06b6d4"/>
                        <circle cx="620" cy="260" r="6" fill="#06b6d4"/>
                        <text x="615" y="245" fill="#a5f3fc" font-family="'JetBrains Mono', monospace" font-size="15" font-weight="700" text-anchor="middle">x(t)</text>
                        <rect x="680" y="215" width="90" height="90" rx="8" fill="rgba(6, 182, 212, 0.2)" stroke="#06b6d4" stroke-width="2.5"/>
                        <text x="725" y="270" fill="#e0f2fe" font-family="'JetBrains Mono', monospace" font-size="24" font-weight="800" text-anchor="middle">C</text>
                    </g>
                """
            },
            {
                "id": "comp-summer2",
                "name": "Output Summing Junction & y(t)",
                "center": [860, 260],
                "radius": 45,
                "svg": """
                    <g id="comp-summer2" class="active-comp" filter="url(#glow-gold)">
                        <path d="M 770 260 L 835 260" stroke="#f59e0b" stroke-width="2.5"/>
                        <polygon points="835,260 823,254 823,266" fill="#f59e0b"/>
                        <circle cx="860" cy="260" r="25" fill="rgba(245, 158, 11, 0.2)" stroke="#f59e0b" stroke-width="2.5"/>
                        <text x="860" y="267" fill="#fef3c7" font-family="'JetBrains Mono', monospace" font-size="20" font-weight="800" text-anchor="middle">+</text>
                        <path d="M 885 260 L 960 260" stroke="#f59e0b" stroke-width="3"/>
                        <polygon points="960,260 948,254 948,266" fill="#f59e0b"/>
                        <text x="925" y="245" fill="#fde68a" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700">y(t)</text>
                    </g>
                """
            },
            {
                "id": "comp-matrix-d",
                "name": "Direct Transmission Matrix D",
                "center": [510, 100],
                "radius": 45,
                "svg": """
                    <g id="comp-matrix-d" class="active-comp" filter="url(#glow-green)">
                        <circle cx="110" cy="260" r="5" fill="#10b981"/>
                        <path d="M 110 260 L 110 100 L 460 100" stroke="#10b981" stroke-width="2.5"/>
                        <polygon points="460,100 448,94 448,106" fill="#10b981"/>
                        <rect x="460" y="55" width="100" height="90" rx="8" fill="rgba(16, 185, 129, 0.2)" stroke="#10b981" stroke-width="2.5"/>
                        <text x="510" y="110" fill="#ecfdf5" font-family="'JetBrains Mono', monospace" font-size="24" font-weight="800" text-anchor="middle">D</text>
                        <path d="M 560 100 L 860 100 L 860 235" stroke="#10b981" stroke-width="2.5"/>
                        <polygon points="860,235 854,223 866,223" fill="#10b981"/>
                    </g>
                """
            }
        ]
    },

    # -------------------------------------------------------------------------
    # 1. Electrical Series RLC Circuit State Space Network (acs-q4)
    # -------------------------------------------------------------------------
    {
        "qid": "acs-q4",
        "aliases": ["acs-q4", "acs-q4b"],
        "title": "State Space Model of Electrical Series RLC Circuit",
        "module": 1,
        "marks": "7 Marks Guaranteed",
        "desc": "Select state variables x1(t) = i_L(t) (inductor current) and x2(t) = v_C(t) (capacitor voltage). Swipe to trace the loop!",
        "equation": r"\begin{bmatrix} \dot{x}_1 \\ \dot{x}_2 \end{bmatrix} = \begin{bmatrix} -R/L & -1/L \\ 1/C & 0 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} + \begin{bmatrix} 1/L \\ 0 \end{bmatrix} u(t), \quad y = \begin{bmatrix} 0 & 1 \end{bmatrix} x",
        "marking_tip": "University examiners award 3 marks for the series schematic with labeled states iL and vC, and 4 marks for deriving the state differential equations.",
        "svg_viewBox": "0 0 1000 580",
        "ghost_svg": """
            <!-- Input Source u(t) -->
            <circle cx="150" cy="290" r="32" class="ghost-fill"/>
            <path d="M 135 290 Q 142 270 150 290 Q 158 310 165 290" class="ghost-stroke"/>
            <text x="150" y="340" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" text-anchor="middle">u(t) = e(t)</text>
            <text x="150" y="245" fill="#64748b" font-size="14" text-anchor="middle">(+)</text>
            <text x="150" y="375" fill="#64748b" font-size="14" text-anchor="middle">(-)</text>

            <!-- Top wire to Resistor R -->
            <path d="M 150 258 L 150 180 L 280 180" class="ghost-stroke"/>

            <!-- Resistor R -->
            <path d="M 280 180 L 290 180 L 298 160 L 314 200 L 330 160 L 346 200 L 362 160 L 378 200 L 386 180 L 410 180" class="ghost-stroke"/>
            <text x="345" y="140" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="15" text-anchor="middle">R (Ω)</text>

            <!-- Inductor L with state x1 = iL -->
            <path d="M 410 180 L 460 180 C 470 150, 495 150, 495 180 C 495 150, 525 150, 525 180 C 525 150, 555 150, 555 180 C 555 150, 585 150, 585 180 L 650 180" class="ghost-stroke"/>
            <text x="540" y="140" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="15" text-anchor="middle">L (State x1 = iL)</text>

            <!-- Wire to Shunt Capacitor C -->
            <path d="M 650 180 L 720 180 L 720 255" class="ghost-stroke"/>

            <!-- Capacitor C with state x2 = vC -->
            <line x1="680" y1="255" x2="760" y2="255" class="ghost-stroke" stroke-width="3"/>
            <line x1="680" y1="275" x2="760" y2="275" class="ghost-stroke" stroke-width="3"/>
            <line x1="720" y1="275" x2="720" y2="400" class="ghost-stroke"/>
            <text x="790" y="270" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14">C (x2 = vC)</text>

            <!-- Output Terminals y(t) = vC -->
            <line x1="720" y1="180" x2="880" y2="180" class="ghost-stroke"/>
            <circle cx="880" cy="180" r="5" class="ghost-fill"/>
            <line x1="720" y1="400" x2="880" y2="400" class="ghost-stroke"/>
            <circle cx="880" cy="400" r="5" class="ghost-fill"/>
            <text x="910" y="295" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold">y(t) = vC</text>

            <!-- Ground Common Rail -->
            <path d="M 150 322 L 150 400 L 720 400" class="ghost-stroke"/>
            <line x1="420" y1="400" x2="420" y2="420" class="ghost-stroke"/>
            <line x1="400" y1="420" x2="440" y2="420" class="ghost-stroke"/>
            <line x1="410" y1="426" x2="430" y2="426" class="ghost-stroke"/>
        """,
        "active_svg": """
            <!-- Comp 1: Input Voltage Source u(t) -->
            <g id="comp-rlc-source" class="active-comp">
                <circle cx="150" cy="290" r="32" fill="#2d220b" stroke="#fbbf24" stroke-width="3.5" filter="url(#glow-gold)"/>
                <path d="M 135 290 Q 142 270 150 290 Q 158 310 165 290" fill="none" stroke="#fbbf24" stroke-width="3.5" stroke-linecap="round"/>
                <text x="150" y="342" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="middle">u(t)</text>
                <text x="150" y="248" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="15" font-weight="bold" text-anchor="middle">(+)</text>
                <text x="150" y="375" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="15" font-weight="bold" text-anchor="middle">(-)</text>
            </g>

            <!-- Comp 2: Top Line to Resistor -->
            <g id="comp-rlc-wire1" class="active-comp">
                <path d="M 150 258 L 150 180 L 280 180" fill="none" stroke="#38bdf8" stroke-width="3.5" stroke-linecap="round" filter="url(#glow-cyan)"/>
                <path d="M 210 180 L 225 180" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow-wire)"/>
            </g>

            <!-- Comp 3: Series Resistor R -->
            <g id="comp-rlc-resistor" class="active-comp">
                <path d="M 280 180 L 290 180 L 298 160 L 314 200 L 330 160 L 346 200 L 362 160 L 378 200 L 386 180 L 410 180" fill="none" stroke="#ff7b00" stroke-width="3.5" stroke-linejoin="round" filter="drop-shadow(0 0 8px rgba(255,123,0,0.6))"/>
                <rect x="325" y="125" width="45" height="24" rx="4" fill="#3a1c04" stroke="#ff7b00"/>
                <text x="347" y="142" fill="#ff7b00" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold" text-anchor="middle">R</text>
            </g>

            <!-- Comp 4: Energy Storage Inductor L -->
            <g id="comp-rlc-inductor" class="active-comp">
                <path d="M 410 180 L 460 180 C 470 148, 495 148, 495 180 C 495 148, 525 148, 525 180 C 525 148, 555 148, 555 180 C 555 148, 585 148, 585 180 L 650 180" fill="none" stroke="#c084fc" stroke-width="3.5" filter="drop-shadow(0 0 10px rgba(192,132,252,0.6))"/>
                <rect x="470" y="122" width="140" height="26" rx="5" fill="#2d124d" stroke="#c084fc"/>
                <text x="540" y="140" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">L (State x1 = iL)</text>
            </g>

            <!-- Comp 5: Shunt Storage Capacitor C -->
            <g id="comp-rlc-capacitor" class="active-comp">
                <path d="M 650 180 L 720 180 L 720 255" fill="none" stroke="#10b981" stroke-width="3.5"/>
                <line x1="680" y1="255" x2="760" y2="255" stroke="#10b981" stroke-width="4.5" filter="url(#glow-green)"/>
                <line x1="680" y1="275" x2="760" y2="275" stroke="#10b981" stroke-width="4.5" filter="url(#glow-green)"/>
                <line x1="720" y1="275" x2="720" y2="400" stroke="#10b981" stroke-width="3.5"/>
                <rect x="765" y="252" width="140" height="26" rx="5" fill="#063826" stroke="#10b981"/>
                <text x="835" y="270" fill="#34d399" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">C (State x2 = vC)</text>
            </g>

            <!-- Comp 6: Ground Return Bus -->
            <g id="comp-rlc-ground" class="active-comp">
                <path d="M 150 322 L 150 400 L 720 400" fill="none" stroke="#38bdf8" stroke-width="3.5" stroke-linecap="round" filter="url(#glow-cyan)"/>
                <line x1="420" y1="400" x2="420" y2="425" stroke="#38bdf8" stroke-width="3"/>
                <line x1="395" y1="425" x2="445" y2="425" stroke="#38bdf8" stroke-width="3.5"/>
                <line x1="405" y1="432" x2="435" y2="432" stroke="#38bdf8" stroke-width="2.5"/>
                <line x1="415" y1="438" x2="425" y2="438" stroke="#38bdf8" stroke-width="2"/>
                <circle cx="720" cy="400" r="5" fill="#38bdf8"/>
            </g>

            <!-- Comp 7: Output Voltage Probe y = vC -->
            <g id="comp-rlc-output" class="active-comp">
                <line x1="720" y1="180" x2="880" y2="180" stroke="#f43f5e" stroke-width="3" stroke-dasharray="4,4"/>
                <circle cx="880" cy="180" r="5" fill="#f43f5e"/>
                <line x1="720" y1="400" x2="880" y2="400" stroke="#f43f5e" stroke-width="3" stroke-dasharray="4,4"/>
                <circle cx="880" cy="400" r="5" fill="#f43f5e"/>
                <rect x="850" y="275" width="120" height="30" rx="6" fill="#2d0b17" stroke="#f43f5e" stroke-width="2" filter="url(#glow-pink)"/>
                <text x="910" y="295" fill="#f43f5e" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="900" text-anchor="middle">y(t) = vC(t)</text>
            </g>

            <!-- Comp 8: State Differential Annotation -->
            <g id="comp-rlc-eqs" class="active-comp">
                <rect x="250" y="460" width="500" height="45" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
                <text x="500" y="488" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="middle">dx1/dt = -(R/L)x1 - (1/L)x2 + (1/L)u,   dx2/dt = (1/C)x1</text>
            </g>
        """,
        "components": [
            {
                "id": "comp-rlc-source",
                "name": "Input Voltage Source u(t)",
                "tag": "Input",
                "color": "#fbbf24",
                "center": {"x": 150, "y": 290},
                "radius": 50,
                "points": [{"x": 150, "y": 258}, {"x": 150, "y": 290}, {"x": 150, "y": 322}],
                "order": 1
            },
            {
                "id": "comp-rlc-wire1",
                "name": "Input Connecting Wire",
                "tag": "Rail",
                "color": "#38bdf8",
                "center": {"x": 200, "y": 180},
                "radius": 50,
                "points": [{"x": 150, "y": 180}, {"x": 200, "y": 180}, {"x": 280, "y": 180}],
                "order": 2
            },
            {
                "id": "comp-rlc-resistor",
                "name": "Series Resistor (R)",
                "tag": "Passive",
                "color": "#ff7b00",
                "center": {"x": 345, "y": 180},
                "radius": 55,
                "points": [{"x": 280, "y": 180}, {"x": 345, "y": 180}, {"x": 410, "y": 180}],
                "order": 3
            },
            {
                "id": "comp-rlc-inductor",
                "name": "Energy Storage Inductor L (State x1 = iL)",
                "tag": "State x1",
                "color": "#c084fc",
                "center": {"x": 530, "y": 180},
                "radius": 75,
                "points": [{"x": 410, "y": 180}, {"x": 530, "y": 180}, {"x": 650, "y": 180}],
                "order": 4
            },
            {
                "id": "comp-rlc-capacitor",
                "name": "Shunt Storage Capacitor C (State x2 = vC)",
                "tag": "State x2",
                "color": "#10b981",
                "center": {"x": 720, "y": 265},
                "radius": 65,
                "points": [{"x": 720, "y": 180}, {"x": 720, "y": 265}, {"x": 720, "y": 400}],
                "order": 5
            },
            {
                "id": "comp-rlc-ground",
                "name": "Common Return Bus & Ground",
                "tag": "Ground",
                "color": "#38bdf8",
                "center": {"x": 435, "y": 400},
                "radius": 85,
                "points": [{"x": 150, "y": 400}, {"x": 420, "y": 400}, {"x": 720, "y": 400}],
                "order": 6
            },
            {
                "id": "comp-rlc-output",
                "name": "Output Voltage Terminals (y = vC)",
                "tag": "Output",
                "color": "#f43f5e",
                "center": {"x": 880, "y": 290},
                "radius": 60,
                "points": [{"x": 880, "y": 180}, {"x": 880, "y": 290}, {"x": 880, "y": 400}],
                "order": 7
            },
            {
                "id": "comp-rlc-eqs",
                "name": "State Equations Formulation Banner",
                "tag": "Math",
                "color": "#38bdf8",
                "center": {"x": 500, "y": 480},
                "radius": 70,
                "points": [{"x": 300, "y": 480}, {"x": 500, "y": 480}, {"x": 700, "y": 480}],
                "order": 8
            }
        ]
    },

    # -------------------------------------------------------------------------
    # 2. Armature-Controlled DC Servomotor State Model (acs-q5)
    # -------------------------------------------------------------------------
    {
        "qid": "acs-q5",
        "aliases": ["acs-q5", "acs-q5-fig2", "acs-q7"],
        "title": "Armature-Controlled DC Servomotor State Flow Diagram",
        "module": 1,
        "marks": "7 Marks Guaranteed",
        "desc": "Models electro-mechanical energy conversion: Input ea(t) -> Armature Current ia -> Motor Torque Tm -> Speed ω -> Angular Position θ.",
        "equation": r"\dot{x} = \begin{bmatrix} -R_a/L_a & -K_b/L_a & 0 \\ K_t/J & -B/J & 0 \\ 0 & 1 & 0 \end{bmatrix} x + \begin{bmatrix} 1/L_a \\ 0 \\ 0 \end{bmatrix} e_a, \quad y = \theta",
        "marking_tip": "University standard requires drawing the closed-loop signal flow diagram with forward blocks (1/(La s+Ra), Kt, 1/(Js+B), 1/s) and back-EMF feedback (Kb).",
        "svg_viewBox": "0 0 1000 580",
        "ghost_svg": """
            <!-- Input ea(t) & Summing Junction -->
            <line x1="60" y1="200" x2="132" y2="200" class="ghost-stroke"/>
            <text x="80" y="185" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="13">ea(t)</text>
            <circle cx="150" cy="200" r="18" class="ghost-fill"/>

            <!-- Armature Electrical Block 1/(La s + Ra) -->
            <line x1="168" y1="200" x2="220" y2="200" class="ghost-stroke"/>
            <rect x="220" y="165" width="115" height="70" rx="8" class="ghost-fill"/>
            <text x="277" y="205" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="12" text-anchor="middle">1/(La·s + Ra)</text>

            <!-- Armature Current ia & Torque Constant Kt -->
            <line x1="335" y1="200" x2="395" y2="200" class="ghost-stroke"/>
            <text x="365" y="185" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="13">ia</text>
            <rect x="395" y="165" width="80" height="70" rx="8" class="ghost-fill"/>
            <text x="435" y="205" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold" text-anchor="middle">Kt</text>

            <!-- Motor Torque Tm & Mechanical Block 1/(J s + B) -->
            <line x1="475" y1="200" x2="535" y2="200" class="ghost-stroke"/>
            <text x="505" y="185" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="13">Tm</text>
            <rect x="535" y="165" width="115" height="70" rx="8" class="ghost-fill"/>
            <text x="592" y="205" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="12" text-anchor="middle">1/(J·s + B)</text>

            <!-- Speed State x1 = ω & Position Integrator 1/s -->
            <line x1="650" y1="200" x2="725" y2="200" class="ghost-stroke"/>
            <text x="685" y="185" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="13">ω(t)</text>
            <rect x="725" y="165" width="80" height="70" rx="8" class="ghost-fill"/>
            <text x="765" y="205" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold" text-anchor="middle">1/s</text>

            <!-- Output Position State x2 = θ -->
            <line x1="805" y1="200" x2="920" y2="200" class="ghost-stroke"/>
            <text x="860" y="185" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold">θ(t)</text>

            <!-- Back-EMF Feedback Block Kb -->
            <path d="M 685 200 L 685 340 L 480 340" class="ghost-stroke"/>
            <rect x="400" y="305" width="80" height="70" rx="8" class="ghost-fill"/>
            <text x="440" y="345" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold" text-anchor="middle">Kb</text>
            <path d="M 400 340 L 150 340 L 150 218" class="ghost-stroke"/>
            <text x="260" y="325" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="12">eb = Kb·ω</text>
        """,
        "active_svg": """
            <!-- Comp 1: Armature Input Voltage ea(t) -->
            <g id="comp-dcm-input" class="active-comp">
                <line x1="60" y1="200" x2="132" y2="200" stroke="#fbbf24" stroke-width="3.5" marker-end="url(#arrow-wire)"/>
                <rect x="55" y="175" width="60" height="24" rx="4" fill="#2d220b" stroke="#fbbf24"/>
                <text x="85" y="192" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">ea(t)</text>
            </g>

            <!-- Comp 2: Back-EMF Summing Junction -->
            <g id="comp-dcm-sum" class="active-comp">
                <circle cx="150" cy="200" r="18" fill="#141c2f" stroke="#38bdf8" stroke-width="3" filter="url(#glow-cyan)"/>
                <text x="150" y="205" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold" text-anchor="middle">Σ</text>
                <text x="132" y="190" fill="#38bdf8" font-size="13">+</text>
                <text x="145" y="228" fill="#f43f5e" font-size="13">-</text>
            </g>

            <!-- Comp 3: Armature Impedance Block -->
            <g id="comp-dcm-elec" class="active-comp">
                <line x1="168" y1="200" x2="220" y2="200" stroke="#38bdf8" stroke-width="3.5" marker-end="url(#arrow-wire)"/>
                <rect x="220" y="165" width="115" height="70" rx="8" fill="#032732" stroke="#00f2fe" stroke-width="3" filter="url(#glow-cyan)"/>
                <text x="277" y="196" fill="#00f2fe" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">ELECTRICAL</text>
                <text x="277" y="215" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">1/(La·s + Ra)</text>
            </g>

            <!-- Comp 4: Motor Torque Constant Kt -->
            <g id="comp-dcm-kt" class="active-comp">
                <line x1="335" y1="200" x2="395" y2="200" stroke="#00f2fe" stroke-width="3.5" marker-end="url(#arrow-wire)"/>
                <text x="365" y="185" fill="#00f2fe" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold">ia</text>
                <rect x="395" y="165" width="80" height="70" rx="8" fill="#1e1809" stroke="#fbbf24" stroke-width="3" filter="url(#glow-gold)"/>
                <text x="435" y="196" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">TORQUE</text>
                <text x="435" y="218" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="900" text-anchor="middle">Kt</text>
            </g>

            <!-- Comp 5: Mechanical Dynamics Block -->
            <g id="comp-dcm-mech" class="active-comp">
                <line x1="475" y1="200" x2="535" y2="200" stroke="#fbbf24" stroke-width="3.5" marker-end="url(#arrow-wire)"/>
                <text x="505" y="185" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold">Tm</text>
                <rect x="535" y="165" width="115" height="70" rx="8" fill="#063826" stroke="#10b981" stroke-width="3" filter="url(#glow-green)"/>
                <text x="592" y="196" fill="#10b981" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">ROTOR INERTIA</text>
                <text x="592" y="215" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">1/(J·s + B)</text>
            </g>

            <!-- Comp 6: Speed State Output ω -->
            <g id="comp-dcm-speed" class="active-comp">
                <line x1="650" y1="200" x2="725" y2="200" stroke="#10b981" stroke-width="3.5" marker-end="url(#arrow-wire)"/>
                <circle cx="685" cy="200" r="5" fill="#10b981"/>
                <rect x="660" y="162" width="50" height="22" rx="4" fill="#063826" stroke="#10b981"/>
                <text x="685" y="178" fill="#34d399" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">ω(t)</text>
            </g>

            <!-- Comp 7: Position Integrator 1/s -->
            <g id="comp-dcm-pos" class="active-comp">
                <rect x="725" y="165" width="80" height="70" rx="8" fill="#2d124d" stroke="#c084fc" stroke-width="3" filter="drop-shadow(0 0 10px rgba(192,132,252,0.6))"/>
                <text x="765" y="196" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">INTEGRATOR</text>
                <text x="765" y="218" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="900" text-anchor="middle">1/s</text>
                <line x1="805" y1="200" x2="905" y2="200" stroke="#c084fc" stroke-width="3.5" marker-end="url(#arrow-wire)"/>
                <rect x="880" y="180" width="70" height="32" rx="6" fill="#2d0b17" stroke="#f43f5e" stroke-width="2"/>
                <text x="915" y="201" fill="#f43f5e" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="900" text-anchor="middle">θ(t)</text>
            </g>

            <!-- Comp 8: Back-EMF Feedback Constant Kb -->
            <g id="comp-dcm-kb" class="active-comp">
                <path d="M 685 200 L 685 340 L 480 340" stroke="#f43f5e" stroke-width="3" fill="none" marker-end="url(#arrow-wire)"/>
                <rect x="400" y="305" width="80" height="70" rx="8" fill="#2d0b17" stroke="#f43f5e" stroke-width="3" filter="url(#glow-pink)"/>
                <text x="440" y="336" fill="#f43f5e" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">BACK-EMF</text>
                <text x="440" y="358" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="900" text-anchor="middle">Kb</text>
            </g>

            <!-- Comp 9: Negative Feedback Return Loop -->
            <g id="comp-dcm-loop" class="active-comp">
                <path d="M 400 340 L 150 340 L 150 218" stroke="#f43f5e" stroke-width="3" fill="none" marker-end="url(#arrow-wire)"/>
                <rect x="220" y="325" width="120" height="25" rx="5" fill="#1e1809" stroke="#fbbf24"/>
                <text x="280" y="342" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">eb(t) = Kb·ω(t)</text>
            </g>
        """,
        "components": [
            {
                "id": "comp-dcm-input",
                "name": "Armature Input Voltage ea(t)",
                "tag": "Input",
                "color": "#fbbf24",
                "center": {"x": 85, "y": 200},
                "radius": 40,
                "points": [{"x": 60, "y": 200}, {"x": 130, "y": 200}],
                "order": 1
            },
            {
                "id": "comp-dcm-sum",
                "name": "Back-EMF Comparator (Σ)",
                "tag": "Summing",
                "color": "#38bdf8",
                "center": {"x": 150, "y": 200},
                "radius": 35,
                "points": [{"x": 150, "y": 200}],
                "order": 2
            },
            {
                "id": "comp-dcm-elec",
                "name": "Armature Electrical Block 1/(La s + Ra)",
                "tag": "Impedance",
                "color": "#00f2fe",
                "center": {"x": 277, "y": 200},
                "radius": 60,
                "points": [{"x": 220, "y": 200}, {"x": 277, "y": 200}, {"x": 335, "y": 200}],
                "order": 3
            },
            {
                "id": "comp-dcm-kt",
                "name": "Motor Torque Constant (Kt)",
                "tag": "Torque",
                "color": "#fbbf24",
                "center": {"x": 435, "y": 200},
                "radius": 50,
                "points": [{"x": 395, "y": 200}, {"x": 435, "y": 200}, {"x": 475, "y": 200}],
                "order": 4
            },
            {
                "id": "comp-dcm-mech",
                "name": "Mechanical Dynamics Block 1/(J s + B)",
                "tag": "Rotor",
                "color": "#10b981",
                "center": {"x": 592, "y": 200},
                "radius": 60,
                "points": [{"x": 535, "y": 200}, {"x": 592, "y": 200}, {"x": 650, "y": 200}],
                "order": 5
            },
            {
                "id": "comp-dcm-speed",
                "name": "Shaft Speed State x1 = ω(t)",
                "tag": "State x1",
                "color": "#10b981",
                "center": {"x": 685, "y": 200},
                "radius": 35,
                "points": [{"x": 650, "y": 200}, {"x": 685, "y": 200}, {"x": 725, "y": 200}],
                "order": 6
            },
            {
                "id": "comp-dcm-pos",
                "name": "Position Integrator 1/s yielding θ(t)",
                "tag": "State x2",
                "color": "#c084fc",
                "center": {"x": 800, "y": 200},
                "radius": 65,
                "points": [{"x": 725, "y": 200}, {"x": 805, "y": 200}, {"x": 905, "y": 200}],
                "order": 7
            },
            {
                "id": "comp-dcm-kb",
                "name": "Back-EMF Feedback Constant (Kb)",
                "tag": "Feedback",
                "color": "#f43f5e",
                "center": {"x": 440, "y": 340},
                "radius": 55,
                "points": [{"x": 400, "y": 340}, {"x": 440, "y": 340}, {"x": 480, "y": 340}],
                "order": 8
            },
            {
                "id": "comp-dcm-loop",
                "name": "Negative Feedback Loop Path",
                "tag": "Return",
                "color": "#f43f5e",
                "center": {"x": 280, "y": 340},
                "radius": 65,
                "points": [{"x": 400, "y": 340}, {"x": 280, "y": 340}, {"x": 150, "y": 340}, {"x": 150, "y": 220}],
                "order": 9
            }
        ]
    },

    # -------------------------------------------------------------------------
    # 3. State Feedback Pole Placement Regulator System (acs-q13)
    # -------------------------------------------------------------------------
    {
        "qid": "acs-q13",
        "aliases": ["acs-q11", "acs-q12", "acs-q13", "acs-q13b", "acs-q14", "acs-q15", "acs-q16", "acs-q16b", "acs-q17", "acs-q17b", "acs-q18", "acs-q19", "acs-q20", "acs-q20b", "acs-q21", "acs-q22"],
        "title": "State Feedback Pole Placement Regulator System (Ackermann)",
        "module": 3,
        "marks": "7 Marks Guaranteed",
        "desc": "Universal question! Closed loop pole placement via full state feedback u = -Kx + r to shift unstable open loop poles to desired locations in the s-plane.",
        "equation": r"u = -Kx + r, \quad \dot{x} = (A - BK)x + Br, \quad K = [0 \dots 1] M_c^{-1} \phi_d(A)",
        "marking_tip": "Draw the continuous state space plant with integrators, the state vector tapping node x, the feedback gain matrix K, and the input comparator.",
        "svg_viewBox": "0 0 1000 580",
        "ghost_svg": """
            <!-- Reference Input r(t) & Input Summing -->
            <line x1="80" y1="200" x2="162" y2="200" class="ghost-stroke"/>
            <text x="110" y="185" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="13">r(t)</text>
            <circle cx="180" cy="200" r="18" class="ghost-fill"/>

            <!-- Plant Input Matrix B -->
            <line x1="198" y1="200" x2="260" y2="200" class="ghost-stroke"/>
            <rect x="260" y="165" width="80" height="70" rx="8" class="ghost-fill"/>
            <text x="300" y="206" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold" text-anchor="middle">B</text>

            <!-- Internal Summing Junction for A matrix -->
            <line x1="340" y1="200" x2="402" y2="200" class="ghost-stroke"/>
            <circle cx="420" cy="200" r="18" class="ghost-fill"/>

            <!-- State Integrator Block 1/s -->
            <line x1="438" y1="200" x2="510" y2="200" class="ghost-stroke"/>
            <text x="470" y="185" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="13">x_dot</text>
            <rect x="510" y="165" width="100" height="70" rx="8" class="ghost-fill"/>
            <text x="560" y="206" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="18" font-weight="bold" text-anchor="middle">∫ dt</text>

            <!-- Output Matrix C & Output y(t) -->
            <line x1="610" y1="200" x2="720" y2="200" class="ghost-stroke"/>
            <circle cx="660" cy="200" r="5" class="ghost-fill"/>
            <text x="660" y="185" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="13">x(t)</text>
            <rect x="720" y="165" width="80" height="70" rx="8" class="ghost-fill"/>
            <text x="760" y="206" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold" text-anchor="middle">C</text>
            <line x1="800" y1="200" x2="900" y2="200" class="ghost-stroke"/>
            <text x="860" y="185" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold">y = Cx</text>

            <!-- Plant Dynamics Matrix A Feedback -->
            <path d="M 660 200 L 660 100 L 460 100" class="ghost-stroke"/>
            <rect x="380" y="65" width="80" height="70" rx="8" class="ghost-fill"/>
            <text x="420" y="106" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold" text-anchor="middle">A</text>
            <path d="M 380 100 L 320 100 L 420 182" class="ghost-stroke"/>

            <!-- State Feedback Gain Matrix K -->
            <path d="M 660 200 L 660 350 L 480 350" class="ghost-stroke"/>
            <rect x="380" y="315" width="100" height="70" rx="8" class="ghost-fill"/>
            <text x="430" y="356" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold" text-anchor="middle">K</text>
            <path d="M 380 350 L 180 350 L 180 218" class="ghost-stroke"/>
            <text x="260" y="335" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="12">u = -Kx</text>
        """,
        "active_svg": """
            <!-- Comp 1: Reference Command r(t) -->
            <g id="comp-sf-ref" class="active-comp">
                <line x1="80" y1="200" x2="162" y2="200" stroke="#fbbf24" stroke-width="3.5" marker-end="url(#arrow-wire)"/>
                <rect x="75" y="175" width="55" height="24" rx="4" fill="#2d220b" stroke="#fbbf24"/>
                <text x="102" y="192" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">r(t)</text>
            </g>

            <!-- Comp 2: Feedback Comparator -->
            <g id="comp-sf-sum1" class="active-comp">
                <circle cx="180" cy="200" r="18" fill="#141c2f" stroke="#38bdf8" stroke-width="3" filter="url(#glow-cyan)"/>
                <text x="180" y="205" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold" text-anchor="middle">Σ</text>
                <text x="162" y="190" fill="#38bdf8" font-size="13">+</text>
                <text x="175" y="228" fill="#f43f5e" font-size="13">-</text>
            </g>

            <!-- Comp 3: Input Matrix B -->
            <g id="comp-sf-b" class="active-comp">
                <line x1="198" y1="200" x2="260" y2="200" stroke="#38bdf8" stroke-width="3.5" marker-end="url(#arrow-wire)"/>
                <text x="228" y="185" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold">u(t)</text>
                <rect x="260" y="165" width="80" height="70" rx="8" fill="#032732" stroke="#00f2fe" stroke-width="3" filter="url(#glow-cyan)"/>
                <text x="300" y="196" fill="#00f2fe" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">INPUT</text>
                <text x="300" y="218" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="18" font-weight="900" text-anchor="middle">B</text>
            </g>

            <!-- Comp 4: Plant Internal Summing -->
            <g id="comp-sf-sum2" class="active-comp">
                <line x1="340" y1="200" x2="402" y2="200" stroke="#00f2fe" stroke-width="3.5" marker-end="url(#arrow-wire)"/>
                <circle cx="420" cy="200" r="18" fill="#141c2f" stroke="#10b981" stroke-width="3" filter="url(#glow-green)"/>
                <text x="420" y="205" fill="#10b981" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold" text-anchor="middle">+</text>
            </g>

            <!-- Comp 5: Continuous Integrator Block ∫ dt -->
            <g id="comp-sf-integrator" class="active-comp">
                <line x1="438" y1="200" x2="510" y2="200" stroke="#10b981" stroke-width="3.5" marker-end="url(#arrow-wire)"/>
                <rect x="460" y="172" width="45" height="22" rx="4" fill="#063826" stroke="#10b981"/>
                <text x="482" y="188" fill="#34d399" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">x_dot</text>
                <rect x="510" y="165" width="100" height="70" rx="8" fill="#1e1809" stroke="#fbbf24" stroke-width="3" filter="url(#glow-gold)"/>
                <text x="560" y="196" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">INTEGRATOR</text>
                <text x="560" y="218" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="18" font-weight="900" text-anchor="middle">∫ dt</text>
            </g>

            <!-- Comp 6: Plant System Matrix A -->
            <g id="comp-sf-a" class="active-comp">
                <path d="M 660 200 L 660 100 L 460 100" stroke="#10b981" stroke-width="3" fill="none" marker-end="url(#arrow-wire)"/>
                <rect x="380" y="65" width="80" height="70" rx="8" fill="#063826" stroke="#10b981" stroke-width="3" filter="url(#glow-green)"/>
                <text x="420" y="96" fill="#10b981" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">SYSTEM</text>
                <text x="420" y="118" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="18" font-weight="900" text-anchor="middle">A</text>
                <path d="M 380 100 L 320 100 L 420 182" stroke="#10b981" stroke-width="2.5" fill="none" marker-end="url(#arrow-wire)"/>
            </g>

            <!-- Comp 7: Output Transmission Matrix C -->
            <g id="comp-sf-c" class="active-comp">
                <line x1="610" y1="200" x2="720" y2="200" stroke="#fbbf24" stroke-width="3.5" marker-end="url(#arrow-wire)"/>
                <circle cx="660" cy="200" r="5" fill="#fbbf24"/>
                <rect x="640" y="165" width="40" height="22" rx="4" fill="#2d220b" stroke="#fbbf24"/>
                <text x="660" y="181" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">x(t)</text>
                <rect x="720" y="165" width="80" height="70" rx="8" fill="#2d124d" stroke="#c084fc" stroke-width="3" filter="drop-shadow(0 0 10px rgba(192,132,252,0.6))"/>
                <text x="760" y="196" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">OUTPUT</text>
                <text x="760" y="218" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="18" font-weight="900" text-anchor="middle">C</text>
                <line x1="800" y1="200" x2="900" y2="200" stroke="#c084fc" stroke-width="3.5" marker-end="url(#arrow-wire)"/>
                <rect x="880" y="180" width="80" height="32" rx="6" fill="#2d0b17" stroke="#f43f5e" stroke-width="2"/>
                <text x="920" y="201" fill="#f43f5e" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="900" text-anchor="middle">y = Cx</text>
            </g>

            <!-- Comp 8: Feedback Gain Matrix K -->
            <g id="comp-sf-k" class="active-comp">
                <path d="M 660 200 L 660 350 L 480 350" stroke="#f43f5e" stroke-width="3" fill="none" marker-end="url(#arrow-wire)"/>
                <rect x="380" y="315" width="100" height="70" rx="8" fill="#2d0b17" stroke="#f43f5e" stroke-width="3" filter="url(#glow-pink)"/>
                <text x="430" y="346" fill="#f43f5e" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">FEEDBACK GAIN</text>
                <text x="430" y="368" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="18" font-weight="900" text-anchor="middle">K</text>
            </g>

            <!-- Comp 9: Control Law Loop u = -Kx -->
            <g id="comp-sf-loop" class="active-comp">
                <path d="M 380 350 L 180 350 L 180 218" stroke="#f43f5e" stroke-width="3" fill="none" marker-end="url(#arrow-wire)"/>
                <rect x="235" y="335" width="105" height="24" rx="5" fill="#1e1809" stroke="#fbbf24"/>
                <text x="287" y="351" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">u = -Kx + r</text>
            </g>
        """,
        "components": [
            {
                "id": "comp-sf-ref",
                "name": "Reference Command Input r(t)",
                "tag": "Command",
                "color": "#fbbf24",
                "center": {"x": 102, "y": 200},
                "radius": 40,
                "points": [{"x": 80, "y": 200}, {"x": 160, "y": 200}],
                "order": 1
            },
            {
                "id": "comp-sf-sum1",
                "name": "State Feedback Comparator (Σ)",
                "tag": "Summing",
                "color": "#38bdf8",
                "center": {"x": 180, "y": 200},
                "radius": 35,
                "points": [{"x": 180, "y": 200}],
                "order": 2
            },
            {
                "id": "comp-sf-b",
                "name": "Plant Input Matrix (B)",
                "tag": "Input",
                "color": "#00f2fe",
                "center": {"x": 300, "y": 200},
                "radius": 50,
                "points": [{"x": 260, "y": 200}, {"x": 300, "y": 200}, {"x": 340, "y": 200}],
                "order": 3
            },
            {
                "id": "comp-sf-sum2",
                "name": "Internal State Adder (+)",
                "tag": "Adder",
                "color": "#10b981",
                "center": {"x": 420, "y": 200},
                "radius": 35,
                "points": [{"x": 420, "y": 200}],
                "order": 4
            },
            {
                "id": "comp-sf-integrator",
                "name": "State Vector Integrator (∫ dt)",
                "tag": "Integrator",
                "color": "#fbbf24",
                "center": {"x": 560, "y": 200},
                "radius": 60,
                "points": [{"x": 510, "y": 200}, {"x": 560, "y": 200}, {"x": 610, "y": 200}],
                "order": 5
            },
            {
                "id": "comp-sf-a",
                "name": "Plant Dynamics Matrix (A)",
                "tag": "Plant",
                "color": "#10b981",
                "center": {"x": 420, "y": 100},
                "radius": 50,
                "points": [{"x": 380, "y": 100}, {"x": 420, "y": 100}, {"x": 460, "y": 100}],
                "order": 6
            },
            {
                "id": "comp-sf-c",
                "name": "Plant Output Matrix (C)",
                "tag": "Output",
                "color": "#c084fc",
                "center": {"x": 760, "y": 200},
                "radius": 55,
                "points": [{"x": 720, "y": 200}, {"x": 760, "y": 200}, {"x": 800, "y": 200}],
                "order": 7
            },
            {
                "id": "comp-sf-k",
                "name": "State Feedback Gain Matrix (K)",
                "tag": "Gain K",
                "color": "#f43f5e",
                "center": {"x": 430, "y": 350},
                "radius": 60,
                "points": [{"x": 380, "y": 350}, {"x": 430, "y": 350}, {"x": 480, "y": 350}],
                "order": 8
            },
            {
                "id": "comp-sf-loop",
                "name": "Control Law Closed Loop (u = -Kx)",
                "tag": "Loop",
                "color": "#f43f5e",
                "center": {"x": 280, "y": 350},
                "radius": 70,
                "points": [{"x": 380, "y": 350}, {"x": 280, "y": 350}, {"x": 180, "y": 350}, {"x": 180, "y": 220}],
                "order": 9
            }
        ]
    }
]
