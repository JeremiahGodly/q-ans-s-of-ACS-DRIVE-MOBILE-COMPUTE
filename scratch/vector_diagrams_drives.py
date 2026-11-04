# -*- coding: utf-8 -*-
"""
vector_diagrams_drives.py
=========================
Pure interactive vector SVG definitions and spatial geometry for Electric Drives (EET413).
"""

DRIVES_DIAGRAMS = [
    # -------------------------------------------------------------------------
    # 0. Modern Electric Drive System Block Diagram (drive-q1)
    # -------------------------------------------------------------------------
    {
        "qid": "drive-q1",
        "aliases": ["drive-q1", "drive-q2", "drive-q3", "drive-q3b"],
        "title": "Block Diagram of a Modern Electric Drive System",
        "module": 1,
        "marks": "5 Marks Guaranteed",
        "desc": "Trace the forward power flow and closed-loop sensing/control pathways that govern every industrial electric motion control system!",
        "equation": r"T_e - T_L = J \frac{d\omega_m}{dt} + B\omega_m, \quad P_m = T_e \cdot \omega_m",
        "marking_tip": "KTU Examiners award 1 mark for Source & Power Modulator, 1 mark for Motor & Load with shaft dynamics, 1 mark for Sensing Unit (Speed/Current), 1 mark for Control Unit & Command input, and 1 mark for correct bidirectional power/feedback flow arrows.",
        "svg_viewBox": "0 0 1000 580",
        "ghost_svg": """
            <!-- Power Source -->
            <rect x="60" y="140" width="140" height="90" rx="10" class="ghost-fill"/>
            <text x="130" y="185" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="600" text-anchor="middle">POWER</text>
            <text x="130" y="205" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="600" text-anchor="middle">SOURCE</text>
            <text x="130" y="222" fill="#475569" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">1-ph / 3-ph AC / DC</text>

            <!-- Arrow Source to Modulator -->
            <path d="M 200 185 L 280 185" class="ghost-stroke"/>
            <polygon points="280,185 270,180 270,190" class="ghost-fill"/>

            <!-- Power Modulator -->
            <rect x="280" y="140" width="160" height="90" rx="10" class="ghost-fill"/>
            <text x="360" y="182" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="600" text-anchor="middle">POWER</text>
            <text x="360" y="202" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="600" text-anchor="middle">MODULATOR</text>
            <text x="360" y="220" fill="#475569" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">Converter / Chopper</text>

            <!-- Arrow Modulator to Motor -->
            <path d="M 440 185 L 520 185" class="ghost-stroke"/>
            <polygon points="520,185 510,180 510,190" class="ghost-fill"/>

            <!-- Electric Motor -->
            <rect x="520" y="140" width="150" height="90" rx="10" class="ghost-fill"/>
            <circle cx="595" cy="185" r="28" class="ghost-stroke"/>
            <text x="595" y="190" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="15" font-weight="700" text-anchor="middle">M</text>
            <text x="595" y="222" fill="#475569" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">DC / Induction / Sync</text>

            <!-- Mechanical Shaft to Load -->
            <rect x="670" y="180" width="80" height="10" class="ghost-fill"/>
            <text x="710" y="172" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">Shaft (Te, ωm)</text>

            <!-- Mechanical Load -->
            <rect x="750" y="140" width="160" height="90" rx="10" class="ghost-fill"/>
            <text x="830" y="185" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="600" text-anchor="middle">MECHANICAL</text>
            <text x="830" y="205" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="600" text-anchor="middle">LOAD</text>
            <text x="830" y="222" fill="#475569" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">Pump / Hoist / Traction</text>

            <!-- Sensing Unit (Speed & Current) -->
            <rect x="520" y="340" width="150" height="90" rx="10" class="ghost-fill"/>
            <text x="595" y="380" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="13.5" font-weight="600" text-anchor="middle">SENSING</text>
            <text x="595" y="400" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="13.5" font-weight="600" text-anchor="middle">UNIT</text>
            <text x="595" y="418" fill="#475569" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">Current & Speed Tach</text>

            <!-- Sensor Pickoffs from Motor & Modulator -->
            <path d="M 595 230 L 595 340" class="ghost-stroke"/>
            <polygon points="595,340 590,330 600,330" class="ghost-fill"/>
            <text x="615" y="285" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="11">ωm, θ</text>

            <path d="M 480 185 L 480 370 L 520 370" class="ghost-stroke"/>
            <polygon points="520,370 510,365 510,375" class="ghost-fill"/>
            <text x="495" y="358" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="11">Ia, Va</text>

            <!-- Arrow Sensing to Control Unit -->
            <path d="M 520 395 L 440 395" class="ghost-stroke"/>
            <polygon points="440,395 450,390 450,400" class="ghost-fill"/>
            <text x="480" y="415" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">Feedback</text>

            <!-- Control Unit -->
            <rect x="280" y="340" width="160" height="90" rx="10" class="ghost-fill"/>
            <text x="360" y="380" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="600" text-anchor="middle">CONTROL</text>
            <text x="360" y="400" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="600" text-anchor="middle">UNIT</text>
            <text x="360" y="418" fill="#475569" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">DSP / Microcontroller</text>

            <!-- Gate Signals Control to Modulator -->
            <path d="M 360 340 L 360 230" class="ghost-stroke"/>
            <polygon points="360,230 355,240 365,240" class="ghost-fill"/>
            <text x="385" y="285" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="11">Gate Pulses / α</text>

            <!-- Input Command -->
            <rect x="60" y="340" width="140" height="90" rx="10" class="ghost-fill"/>
            <text x="130" y="380" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="13.5" font-weight="600" text-anchor="middle">INPUT</text>
            <text x="130" y="400" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="13.5" font-weight="600" text-anchor="middle">COMMAND</text>
            <text x="130" y="418" fill="#475569" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">Ref Speed ω*, T*</text>

            <!-- Arrow Command to Control -->
            <path d="M 200 385 L 280 385" class="ghost-stroke"/>
            <polygon points="280,385 270,380 270,390" class="ghost-fill"/>
        """,
        "components": [
            {
                "id": "comp-source",
                "name": "Electrical Power Source",
                "center": [130, 185],
                "radius": 45,
                "svg": """
                    <g id="comp-source" class="active-comp" filter="url(#glow-gold)">
                        <rect x="60" y="140" width="140" height="90" rx="10" fill="rgba(245, 158, 11, 0.18)" stroke="#f59e0b" stroke-width="2.5"/>
                        <text x="130" y="185" fill="#fde68a" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700" text-anchor="middle">POWER</text>
                        <text x="130" y="205" fill="#fde68a" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700" text-anchor="middle">SOURCE</text>
                        <text x="130" y="222" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">1-ph / 3-ph AC / DC</text>
                    </g>
                """
            },
            {
                "id": "comp-modulator",
                "name": "Power Modulator (Converter/Inverter)",
                "center": [360, 185],
                "radius": 45,
                "svg": """
                    <g id="comp-modulator" class="active-comp" filter="url(#glow-cyan)">
                        <rect x="280" y="140" width="160" height="90" rx="10" fill="rgba(6, 182, 212, 0.18)" stroke="#06b6d4" stroke-width="2.5"/>
                        <text x="360" y="182" fill="#a5f3fc" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700" text-anchor="middle">POWER</text>
                        <text x="360" y="202" fill="#a5f3fc" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700" text-anchor="middle">MODULATOR</text>
                        <text x="360" y="220" fill="#22d3ee" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">Converter / Chopper</text>
                    </g>
                """
            },
            {
                "id": "comp-motor",
                "name": "Electric Motor (DC/AC)",
                "center": [595, 185],
                "radius": 45,
                "svg": """
                    <g id="comp-motor" class="active-comp" filter="url(#glow-green)">
                        <rect x="520" y="140" width="150" height="90" rx="10" fill="rgba(16, 185, 129, 0.18)" stroke="#10b981" stroke-width="2.5"/>
                        <circle cx="595" cy="185" r="28" fill="rgba(16, 185, 129, 0.25)" stroke="#10b981" stroke-width="2"/>
                        <text x="595" y="191" fill="#ecfdf5" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="800" text-anchor="middle">M</text>
                        <text x="595" y="222" fill="#6ee7b7" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">DC / Induction / Sync</text>
                    </g>
                """
            },
            {
                "id": "comp-load",
                "name": "Mechanical Load",
                "center": [830, 185],
                "radius": 45,
                "svg": """
                    <g id="comp-load" class="active-comp" filter="url(#glow-pink)">
                        <rect x="750" y="140" width="160" height="90" rx="10" fill="rgba(236, 72, 153, 0.18)" stroke="#ec4899" stroke-width="2.5"/>
                        <text x="830" y="185" fill="#fbcfe8" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700" text-anchor="middle">MECHANICAL</text>
                        <text x="830" y="205" fill="#fbcfe8" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700" text-anchor="middle">LOAD</text>
                        <text x="830" y="222" fill="#f472b6" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">Pump / Hoist / Traction</text>
                    </g>
                """
            },
            {
                "id": "comp-forward-power",
                "name": "Forward Power Bus & Shaft",
                "center": [240, 185],
                "radius": 45,
                "waypoints": [[240, 185], [480, 185], [710, 185]],
                "svg": """
                    <g id="comp-forward-power" class="active-comp" filter="url(#glow-gold)">
                        <!-- Power arrows -->
                        <path d="M 200 185 L 280 185" stroke="#f59e0b" stroke-width="3" stroke-linecap="round"/>
                        <polygon points="280,185 268,179 268,191" fill="#f59e0b"/>
                        <path d="M 440 185 L 520 185" stroke="#f59e0b" stroke-width="3" stroke-linecap="round"/>
                        <polygon points="520,185 508,179 508,191" fill="#f59e0b"/>
                        <!-- Mechanical Shaft -->
                        <rect x="670" y="180" width="80" height="10" rx="3" fill="#f59e0b" stroke="#fbbf24" stroke-width="1.5"/>
                        <text x="710" y="172" fill="#fef08a" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="600" text-anchor="middle">Shaft (Te, ωm)</text>
                    </g>
                """
            },
            {
                "id": "comp-sensing",
                "name": "Sensing Unit (Speed & Current)",
                "center": [595, 385],
                "radius": 45,
                "svg": """
                    <g id="comp-sensing" class="active-comp" filter="url(#glow-cyan)">
                        <rect x="520" y="340" width="150" height="90" rx="10" fill="rgba(6, 182, 212, 0.18)" stroke="#06b6d4" stroke-width="2.5"/>
                        <text x="595" y="380" fill="#a5f3fc" font-family="'JetBrains Mono', monospace" font-size="13.5" font-weight="700" text-anchor="middle">SENSING</text>
                        <text x="595" y="400" fill="#a5f3fc" font-family="'JetBrains Mono', monospace" font-size="13.5" font-weight="700" text-anchor="middle">UNIT</text>
                        <text x="595" y="418" fill="#67e8f9" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">Current & Speed Tach</text>
                    </g>
                """
            },
            {
                "id": "comp-control",
                "name": "Control Unit (DSP / Microcontroller)",
                "center": [360, 385],
                "radius": 45,
                "svg": """
                    <g id="comp-control" class="active-comp" filter="url(#glow-green)">
                        <rect x="280" y="340" width="160" height="90" rx="10" fill="rgba(16, 185, 129, 0.18)" stroke="#10b981" stroke-width="2.5"/>
                        <text x="360" y="380" fill="#ecfdf5" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700" text-anchor="middle">CONTROL</text>
                        <text x="360" y="400" fill="#ecfdf5" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700" text-anchor="middle">UNIT</text>
                        <text x="360" y="418" fill="#6ee7b7" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">DSP / Microcontroller</text>
                    </g>
                """
            },
            {
                "id": "comp-command-feedback",
                "name": "Command Input & Feedback Loops",
                "center": [130, 385],
                "radius": 45,
                "waypoints": [[130, 385], [240, 385], [360, 285], [480, 395], [595, 285]],
                "svg": """
                    <g id="comp-command-feedback" class="active-comp" filter="url(#glow-gold)">
                        <!-- Input Command -->
                        <rect x="60" y="340" width="140" height="90" rx="10" fill="rgba(245, 158, 11, 0.18)" stroke="#f59e0b" stroke-width="2.5"/>
                        <text x="130" y="380" fill="#fde68a" font-family="'JetBrains Mono', monospace" font-size="13.5" font-weight="700" text-anchor="middle">INPUT</text>
                        <text x="130" y="400" fill="#fde68a" font-family="'JetBrains Mono', monospace" font-size="13.5" font-weight="700" text-anchor="middle">COMMAND</text>
                        <text x="130" y="418" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">Ref Speed ω*, T*</text>
                        <!-- Command arrow -->
                        <path d="M 200 385 L 280 385" stroke="#f59e0b" stroke-width="2.5"/>
                        <polygon points="280,385 270,380 270,390" fill="#f59e0b"/>
                        <!-- Feedback lines -->
                        <path d="M 520 395 L 440 395" stroke="#06b6d4" stroke-width="2.5"/>
                        <polygon points="440,395 450,390 450,400" fill="#06b6d4"/>
                        <text x="480" y="415" fill="#67e8f9" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">Feedback</text>
                        <path d="M 595 230 L 595 340" stroke="#06b6d4" stroke-width="2.5"/>
                        <polygon points="595,340 590,330 600,330" fill="#06b6d4"/>
                        <text x="615" y="285" fill="#67e8f9" font-family="'JetBrains Mono', monospace" font-size="11">ωm, θ</text>
                        <path d="M 480 185 L 480 370 L 520 370" stroke="#06b6d4" stroke-width="2.5"/>
                        <polygon points="520,370 510,365 510,375" fill="#06b6d4"/>
                        <text x="495" y="358" fill="#67e8f9" font-family="'JetBrains Mono', monospace" font-size="11">Ia, Va</text>
                        <!-- Firing Pulses -->
                        <path d="M 360 340 L 360 230" stroke="#10b981" stroke-width="2.5"/>
                        <polygon points="360,230 355,240 365,240" fill="#10b981"/>
                        <text x="385" y="285" fill="#6ee7b7" font-family="'JetBrains Mono', monospace" font-size="11">Gate Pulses / α</text>
                    </g>
                """
            }
        ]
    },

    # -------------------------------------------------------------------------
    # 1. Single-Phase Fully Controlled Rectifier Fed DC Motor Drive (drive-q8)
    # -------------------------------------------------------------------------
    {
        "qid": "drive-q8",
        "aliases": ["drive-q8", "drive-q8b", "drive-q8-fig2", "drive-q8b-fig2", "drive-q7", "drive-q7b"],
        "title": "Single-Phase Fully Controlled Rectifier Fed DC Motor Drive",
        "module": 2,
        "marks": "7 Marks Guaranteed",
        "desc": "Swipe near any circuit element to snap the vector schematic into place with vibrant neon lines and audio feedback!",
        "equation": r"V_o = \frac{2V_m}{\pi}\cos\alpha, \quad \omega_m = \frac{V_o - I_a R_a}{K_m}, \quad T_e = K_m I_a",
        "marking_tip": "Examiners award 3 marks for correct thyristor bridge polarity (T1, T4 & T3, T2), 2 marks for freewheeling diode D_fw, and 2 marks for motor armature loop.",
        "svg_viewBox": "0 0 1000 580",
        "ghost_svg": """
            <!-- AC Source -->
            <circle cx="130" cy="290" r="28" class="ghost-fill"/>
            <path d="M 116 290 Q 123 274 130 290 Q 137 306 144 290" class="ghost-stroke"/>
            <text x="130" y="335" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="12" text-anchor="middle">vs = Vm·sin(ωt)</text>

            <!-- AC Connecting Wires -->
            <path d="M 130 262 L 130 220 L 260 220" class="ghost-stroke"/>
            <path d="M 130 318 L 130 360 L 400 360" class="ghost-stroke"/>

            <!-- SCR T1 -->
            <path d="M 260 220 L 260 185" class="ghost-stroke"/>
            <polygon points="245,185 275,185 260,160" class="ghost-fill"/>
            <line x1="245" y1="160" x2="275" y2="160" class="ghost-stroke"/>
            <line x1="260" y1="160" x2="260" y2="140" class="ghost-stroke"/>
            <line x1="250" y1="180" x2="235" y2="185" class="ghost-stroke"/>
            <text x="220" y="170" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="13">T1</text>

            <!-- SCR T4 -->
            <path d="M 260 440 L 260 310" class="ghost-stroke"/>
            <polygon points="245,310 275,310 260,285" class="ghost-fill"/>
            <line x1="245" y1="285" x2="275" y2="285" class="ghost-stroke"/>
            <line x1="260" y1="285" x2="260" y2="220" class="ghost-stroke"/>
            <line x1="250" y1="305" x2="235" y2="310" class="ghost-stroke"/>
            <text x="220" y="295" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="13">T4</text>

            <!-- SCR T3 -->
            <path d="M 400 360 L 400 185" class="ghost-stroke"/>
            <polygon points="385,185 415,185 400,160" class="ghost-fill"/>
            <line x1="385" y1="160" x2="415" y2="160" class="ghost-stroke"/>
            <line x1="400" y1="160" x2="400" y2="140" class="ghost-stroke"/>
            <line x1="410" y1="180" x2="425" y2="185" class="ghost-stroke"/>
            <text x="435" y="170" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="13">T3</text>

            <!-- SCR T2 -->
            <path d="M 400 440 L 400 410" class="ghost-stroke"/>
            <polygon points="385,410 415,410 400,385" class="ghost-fill"/>
            <line x1="385" y1="385" x2="415" y2="385" class="ghost-stroke"/>
            <line x1="400" y1="385" x2="400" y2="360" class="ghost-stroke"/>
            <line x1="410" y1="405" x2="425" y2="410" class="ghost-stroke"/>
            <text x="435" y="395" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="13">T2</text>

            <!-- DC Bus Bars -->
            <path d="M 260 140 L 400 140 L 520 140 L 610 140" class="ghost-stroke"/>
            <path d="M 260 440 L 400 440 L 520 440 L 850 440" class="ghost-stroke"/>

            <!-- Freewheeling Diode Dfw -->
            <path d="M 520 440 L 520 310" class="ghost-stroke"/>
            <polygon points="505,310 535,310 520,280" class="ghost-fill"/>
            <line x1="505" y1="280" x2="535" y2="280" class="ghost-stroke"/>
            <line x1="520" y1="280" x2="520" y2="140" class="ghost-stroke"/>
            <text x="520" y="340" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="12" text-anchor="middle">D_fw</text>

            <!-- Armature Resistor Ra -->
            <path d="M 610 140 L 620 140 L 627 122 L 639 158 L 651 122 L 663 158 L 675 122 L 687 158 L 694 140 L 710 140" class="ghost-stroke"/>
            <text x="655" y="105" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="13" text-anchor="middle">Ra</text>

            <!-- Armature Inductor La -->
            <path d="M 710 140 C 715 110, 735 110, 735 140 C 735 110, 760 110, 760 140 C 760 110, 785 110, 785 140 C 785 110, 810 110, 810 140 L 850 140 L 850 240" class="ghost-stroke"/>
            <text x="760" y="105" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="13" text-anchor="middle">La</text>

            <!-- Motor Armature M -->
            <circle cx="850" cy="280" r="36" class="ghost-fill"/>
            <rect x="838" y="240" width="24" height="8" rx="2" class="ghost-fill"/>
            <rect x="838" y="312" width="24" height="8" rx="2" class="ghost-fill"/>
            <text x="850" y="287" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="20" font-weight="bold" text-anchor="middle">M</text>

            <!-- Back-EMF Eb & Return Wire -->
            <path d="M 850 320 L 850 370" class="ghost-stroke"/>
            <circle cx="850" cy="390" r="14" class="ghost-fill"/>
            <text x="850" y="395" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="12" text-anchor="middle">Eb</text>
            <path d="M 850 404 L 850 440" class="ghost-stroke"/>
        """,
        "active_svg": """
            <!-- Component 1: AC Voltage Source -->
            <g id="comp-ac-source" class="active-comp">
                <circle cx="130" cy="290" r="28" fill="#2d220b" stroke="#fbbf24" stroke-width="3" filter="url(#glow-gold)"/>
                <path d="M 116 290 Q 123 274 130 290 Q 137 306 144 290" fill="none" stroke="#fbbf24" stroke-width="3.5" stroke-linecap="round"/>
                <text x="130" y="336" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" text-anchor="middle">vs = Vm·sin(ωt)</text>
                <circle cx="130" cy="262" r="4" fill="#fbbf24"/>
                <circle cx="130" cy="318" r="4" fill="#fbbf24"/>
            </g>

            <!-- Component 2: AC Connecting Lines -->
            <g id="comp-ac-wires" class="active-comp">
                <path d="M 130 262 L 130 220 L 260 220" fill="none" stroke="#f59e0b" stroke-width="3.5" stroke-linecap="round"/>
                <path d="M 130 318 L 130 360 L 400 360" fill="none" stroke="#f59e0b" stroke-width="3.5" stroke-linecap="round"/>
                <circle cx="260" cy="220" r="4.5" fill="#f59e0b"/>
                <circle cx="400" cy="360" r="4.5" fill="#f59e0b"/>
                <rect x="180" y="206" width="24" height="18" rx="3" fill="#1e1809" stroke="#f59e0b"/>
                <text x="192" y="220" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">A</text>
                <rect x="235" y="346" width="24" height="18" rx="3" fill="#1e1809" stroke="#f59e0b"/>
                <text x="247" y="360" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">B</text>
            </g>

            <!-- Component 3: SCR T1 -->
            <g id="comp-t1-scr" class="active-comp">
                <line x1="260" y1="220" x2="260" y2="185" stroke="#00f2fe" stroke-width="3.5"/>
                <polygon points="245,185 275,185 260,160" fill="#03303d" stroke="#00f2fe" stroke-width="2.5" filter="url(#glow-cyan)"/>
                <line x1="245" y1="160" x2="275" y2="160" stroke="#00f2fe" stroke-width="3.5"/>
                <line x1="260" y1="160" x2="260" y2="140" stroke="#00f2fe" stroke-width="3.5"/>
                <line x1="250" y1="180" x2="235" y2="185" stroke="#00f2fe" stroke-width="2.5"/>
                <circle cx="235" cy="185" r="2.5" fill="#00f2fe"/>
                <rect x="206" y="152" width="28" height="20" rx="4" fill="#032732" stroke="#00f2fe"/>
                <text x="220" y="167" fill="#00f2fe" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="800">T1</text>
            </g>

            <!-- Component 4: SCR T4 -->
            <g id="comp-t4-scr" class="active-comp">
                <line x1="260" y1="440" x2="260" y2="310" stroke="#00f2fe" stroke-width="3.5"/>
                <polygon points="245,310 275,310 260,285" fill="#03303d" stroke="#00f2fe" stroke-width="2.5" filter="url(#glow-cyan)"/>
                <line x1="245" y1="285" x2="275" y2="285" stroke="#00f2fe" stroke-width="3.5"/>
                <line x1="260" y1="285" x2="260" y2="220" stroke="#00f2fe" stroke-width="3.5"/>
                <line x1="250" y1="305" x2="235" y2="310" stroke="#00f2fe" stroke-width="2.5"/>
                <circle cx="235" cy="310" r="2.5" fill="#00f2fe"/>
                <rect x="206" y="278" width="28" height="20" rx="4" fill="#032732" stroke="#00f2fe"/>
                <text x="220" y="293" fill="#00f2fe" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="800">T4</text>
            </g>

            <!-- Component 5: SCR T3 -->
            <g id="comp-t3-scr" class="active-comp">
                <line x1="400" y1="360" x2="400" y2="185" stroke="#00f2fe" stroke-width="3.5"/>
                <polygon points="385,185 415,185 400,160" fill="#03303d" stroke="#00f2fe" stroke-width="2.5" filter="url(#glow-cyan)"/>
                <line x1="385" y1="160" x2="415" y2="160" stroke="#00f2fe" stroke-width="3.5"/>
                <line x1="400" y1="160" x2="400" y2="140" stroke="#00f2fe" stroke-width="3.5"/>
                <line x1="410" y1="180" x2="425" y2="185" stroke="#00f2fe" stroke-width="2.5"/>
                <circle cx="425" cy="185" r="2.5" fill="#00f2fe"/>
                <rect x="428" y="152" width="28" height="20" rx="4" fill="#032732" stroke="#00f2fe"/>
                <text x="442" y="167" fill="#00f2fe" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="800">T3</text>
            </g>

            <!-- Component 6: SCR T2 -->
            <g id="comp-t2-scr" class="active-comp">
                <line x1="400" y1="440" x2="400" y2="410" stroke="#00f2fe" stroke-width="3.5"/>
                <polygon points="385,410 415,410 400,385" fill="#03303d" stroke="#00f2fe" stroke-width="2.5" filter="url(#glow-cyan)"/>
                <line x1="385" y1="385" x2="415" y2="385" stroke="#00f2fe" stroke-width="3.5"/>
                <line x1="400" y1="385" x2="400" y2="360" stroke="#00f2fe" stroke-width="3.5"/>
                <line x1="410" y1="405" x2="425" y2="410" stroke="#00f2fe" stroke-width="2.5"/>
                <circle cx="425" cy="410" r="2.5" fill="#00f2fe"/>
                <rect x="428" y="378" width="28" height="20" rx="4" fill="#032732" stroke="#00f2fe"/>
                <text x="442" y="393" fill="#00f2fe" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="800">T2</text>
            </g>

            <!-- Component 7: Positive Top DC Bus -->
            <g id="comp-pos-rail" class="active-comp">
                <path d="M 260 140 L 400 140 L 520 140 L 610 140" fill="none" stroke="#38bdf8" stroke-width="4" stroke-linecap="round" filter="url(#glow-cyan)"/>
                <circle cx="260" cy="140" r="5" fill="#38bdf8"/>
                <circle cx="400" cy="140" r="5" fill="#38bdf8"/>
                <circle cx="520" cy="140" r="5" fill="#38bdf8"/>
                <rect x="455" y="112" width="36" height="20" rx="4" fill="#0369a1" stroke="#38bdf8"/>
                <text x="473" y="126" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="800" text-anchor="middle">(+)</text>
            </g>

            <!-- Component 8: Negative Bottom DC Bus -->
            <g id="comp-neg-rail" class="active-comp">
                <path d="M 260 440 L 400 440 L 520 440 L 850 440" fill="none" stroke="#38bdf8" stroke-width="4" stroke-linecap="round" filter="url(#glow-cyan)"/>
                <circle cx="260" cy="440" r="5" fill="#38bdf8"/>
                <circle cx="400" cy="440" r="5" fill="#38bdf8"/>
                <circle cx="520" cy="440" r="5" fill="#38bdf8"/>
                <circle cx="850" cy="440" r="5" fill="#38bdf8"/>
                <rect x="455" y="448" width="36" height="20" rx="4" fill="#0369a1" stroke="#38bdf8"/>
                <text x="473" y="462" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="800" text-anchor="middle">(-)</text>
            </g>

            <!-- Component 9: Freewheeling Diode Dfw -->
            <g id="comp-diode-dfw" class="active-comp">
                <line x1="520" y1="440" x2="520" y2="310" stroke="#10b981" stroke-width="3"/>
                <polygon points="505,310 535,310 520,280" fill="#063826" stroke="#10b981" stroke-width="2.5" filter="url(#glow-green)"/>
                <line x1="505" y1="280" x2="535" y2="280" stroke="#10b981" stroke-width="3.5"/>
                <line x1="520" y1="280" x2="520" y2="140" stroke="#10b981" stroke-width="3"/>
                <rect x="480" y="328" width="80" height="22" rx="5" fill="#062d1f" stroke="#10b981" stroke-width="1"/>
                <text x="520" y="343" fill="#34d399" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="800" text-anchor="middle">D_fw</text>
            </g>

            <!-- Component 10: Armature Resistor Ra -->
            <g id="comp-resistor-ra" class="active-comp">
                <path d="M 610 140 L 620 140 L 627 122 L 639 158 L 651 122 L 663 158 L 675 122 L 687 158 L 694 140 L 710 140" fill="none" stroke="#ff7b00" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" filter="drop-shadow(0 0 8px rgba(255,123,0,0.6))"/>
                <rect x="640" y="94" width="30" height="20" rx="4" fill="#3a1c04" stroke="#ff7b00"/>
                <text x="655" y="108" fill="#ff7b00" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="800" text-anchor="middle">Ra</text>
            </g>

            <!-- Component 11: Armature Inductor La -->
            <g id="comp-inductor-la" class="active-comp">
                <path d="M 710 140 C 715 110, 735 110, 735 140 C 735 110, 760 110, 760 140 C 760 110, 785 110, 785 140 C 785 110, 810 110, 810 140 L 850 140 L 850 240" fill="none" stroke="#c084fc" stroke-width="3.5" stroke-linecap="round" filter="drop-shadow(0 0 8px rgba(192,132,252,0.6))"/>
                <circle cx="850" cy="140" r="4" fill="#c084fc"/>
                <rect x="745" y="94" width="30" height="20" rx="4" fill="#2d124d" stroke="#c084fc"/>
                <text x="760" y="108" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="800" text-anchor="middle">La</text>
            </g>

            <!-- Component 12: DC Motor Armature & Back-EMF -->
            <g id="comp-motor-armature" class="active-comp">
                <rect x="838" y="240" width="24" height="8" rx="2" fill="#334155" stroke="#f43f5e" stroke-width="2"/>
                <rect x="838" y="312" width="24" height="8" rx="2" fill="#334155" stroke="#f43f5e" stroke-width="2"/>
                <circle cx="850" cy="280" r="36" fill="#2d0b17" stroke="#f43f5e" stroke-width="3.5" filter="url(#glow-pink)"/>
                <text x="850" y="289" fill="#f43f5e" font-family="'JetBrains Mono', monospace" font-size="22" font-weight="900" text-anchor="middle">M</text>
                <path d="M 850 320 L 850 376" stroke="#f43f5e" stroke-width="3"/>
                <circle cx="850" cy="390" r="14" fill="#2d0b17" stroke="#f43f5e" stroke-width="2.5"/>
                <text x="850" y="394" fill="#f43f5e" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">Eb</text>
                <path d="M 850 404 L 850 440" stroke="#f43f5e" stroke-width="3"/>
                <rect x="880" y="270" width="85" height="22" rx="4" fill="#260813" stroke="#f43f5e"/>
                <text x="922" y="285" fill="#fb7185" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">DC MOTOR</text>
            </g>
        """,
        "components": [
            {
                "id": "comp-ac-source",
                "name": "AC Voltage Source (vs)",
                "tag": "Source",
                "color": "#fbbf24",
                "center": {"x": 130, "y": 290},
                "radius": 45,
                "points": [{"x": 130, "y": 262}, {"x": 130, "y": 290}, {"x": 130, "y": 318}, {"x": 102, "y": 290}, {"x": 158, "y": 290}],
                "order": 1
            },
            {
                "id": "comp-ac-wires",
                "name": "AC Connecting Lines (A, B)",
                "tag": "Terminals",
                "color": "#f59e0b",
                "center": {"x": 260, "y": 290},
                "radius": 70,
                "points": [{"x": 130, "y": 220}, {"x": 200, "y": 220}, {"x": 260, "y": 220}, {"x": 130, "y": 360}, {"x": 260, "y": 360}, {"x": 400, "y": 360}],
                "order": 2
            },
            {
                "id": "comp-t1-scr",
                "name": "Thyristor T1 (Top-Left SCR)",
                "tag": "Switch",
                "color": "#00f2fe",
                "center": {"x": 260, "y": 175},
                "radius": 50,
                "points": [{"x": 260, "y": 220}, {"x": 260, "y": 185}, {"x": 260, "y": 160}, {"x": 260, "y": 140}, {"x": 245, "y": 185}, {"x": 275, "y": 185}, {"x": 235, "y": 185}],
                "order": 3
            },
            {
                "id": "comp-t4-scr",
                "name": "Thyristor T4 (Bottom-Left SCR)",
                "tag": "Switch",
                "color": "#00f2fe",
                "center": {"x": 260, "y": 310},
                "radius": 50,
                "points": [{"x": 260, "y": 440}, {"x": 260, "y": 310}, {"x": 260, "y": 285}, {"x": 260, "y": 220}, {"x": 245, "y": 310}, {"x": 275, "y": 310}, {"x": 235, "y": 310}],
                "order": 4
            },
            {
                "id": "comp-t3-scr",
                "name": "Thyristor T3 (Top-Right SCR)",
                "tag": "Switch",
                "color": "#00f2fe",
                "center": {"x": 400, "y": 175},
                "radius": 50,
                "points": [{"x": 400, "y": 360}, {"x": 400, "y": 185}, {"x": 400, "y": 160}, {"x": 400, "y": 140}, {"x": 385, "y": 185}, {"x": 415, "y": 185}, {"x": 425, "y": 185}],
                "order": 5
            },
            {
                "id": "comp-t2-scr",
                "name": "Thyristor T2 (Bottom-Right SCR)",
                "tag": "Switch",
                "color": "#00f2fe",
                "center": {"x": 400, "y": 400},
                "radius": 50,
                "points": [{"x": 400, "y": 440}, {"x": 400, "y": 410}, {"x": 400, "y": 385}, {"x": 400, "y": 360}, {"x": 385, "y": 410}, {"x": 415, "y": 410}, {"x": 425, "y": 410}],
                "order": 6
            },
            {
                "id": "comp-pos-rail",
                "name": "Positive (+) DC Bus Bar",
                "tag": "Bus Bar",
                "color": "#38bdf8",
                "center": {"x": 435, "y": 140},
                "radius": 120,
                "points": [{"x": 260, "y": 140}, {"x": 330, "y": 140}, {"x": 400, "y": 140}, {"x": 460, "y": 140}, {"x": 520, "y": 140}, {"x": 610, "y": 140}],
                "order": 7
            },
            {
                "id": "comp-neg-rail",
                "name": "Negative (-) DC Bus Bar",
                "tag": "Bus Bar",
                "color": "#38bdf8",
                "center": {"x": 550, "y": 440},
                "radius": 180,
                "points": [{"x": 260, "y": 440}, {"x": 400, "y": 440}, {"x": 520, "y": 440}, {"x": 680, "y": 440}, {"x": 770, "y": 440}, {"x": 850, "y": 440}],
                "order": 8
            },
            {
                "id": "comp-diode-dfw",
                "name": "Freewheeling Diode (Dfw)",
                "tag": "Protection",
                "color": "#10b981",
                "center": {"x": 520, "y": 290},
                "radius": 70,
                "points": [{"x": 520, "y": 440}, {"x": 520, "y": 310}, {"x": 520, "y": 280}, {"x": 520, "y": 140}, {"x": 505, "y": 310}, {"x": 535, "y": 310}, {"x": 505, "y": 280}, {"x": 535, "y": 280}],
                "order": 9
            },
            {
                "id": "comp-resistor-ra",
                "name": "Armature Resistance (Ra)",
                "tag": "Load",
                "color": "#ff7b00",
                "center": {"x": 655, "y": 140},
                "radius": 50,
                "points": [{"x": 610, "y": 140}, {"x": 627, "y": 122}, {"x": 639, "y": 158}, {"x": 651, "y": 122}, {"x": 663, "y": 158}, {"x": 675, "y": 122}, {"x": 687, "y": 158}, {"x": 710, "y": 140}],
                "order": 10
            },
            {
                "id": "comp-inductor-la",
                "name": "Armature Inductance (La)",
                "tag": "Load",
                "color": "#c084fc",
                "center": {"x": 760, "y": 140},
                "radius": 60,
                "points": [{"x": 710, "y": 140}, {"x": 735, "y": 120}, {"x": 760, "y": 120}, {"x": 785, "y": 120}, {"x": 810, "y": 140}, {"x": 850, "y": 140}, {"x": 850, "y": 200}],
                "order": 11
            },
            {
                "id": "comp-motor-armature",
                "name": "DC Motor Armature (M & Eb)",
                "tag": "Machine",
                "color": "#f43f5e",
                "center": {"x": 850, "y": 280},
                "radius": 75,
                "points": [{"x": 850, "y": 240}, {"x": 850, "y": 280}, {"x": 850, "y": 320}, {"x": 814, "y": 280}, {"x": 886, "y": 280}, {"x": 850, "y": 380}, {"x": 850, "y": 440}],
                "order": 12
            }
        ]
    },

    # -------------------------------------------------------------------------
    # 2. Two-Quadrant Class-C Chopper DC Motor Drive (drive-q10)
    # -------------------------------------------------------------------------
    {
        "qid": "drive-q10",
        "aliases": ["drive-q10", "drive-q10b", "drive-q10-fig2", "drive-q10b-fig2", "drive-q9", "drive-q9b", "drive-q11", "drive-q11-fig2"],
        "title": "Two-Quadrant Class-C Chopper Fed DC Motor Drive",
        "module": 3,
        "marks": "7 Marks Guaranteed",
        "desc": "Operating in Quadrants I (Forward Motoring) & II (Regenerative Braking). Trace the chopper switches, diodes, and DC armature load!",
        "equation": r"V_o = \delta V_{dc}, \quad I_a = \frac{\delta V_{dc} - E_b}{R_a}, \quad \text{Regeneration: } E_b > V_{dc}",
        "marking_tip": "Clearly show CH1 in series for motoring with freewheeling diode D1, and CH2 across the load with antiparallel diode D2 returning current to Vdc.",
        "svg_viewBox": "0 0 1000 580",
        "ghost_svg": """
            <!-- DC Source Vdc -->
            <line x1="120" y1="200" x2="120" y2="380" class="ghost-stroke"/>
            <line x1="100" y1="260" x2="140" y2="260" class="ghost-stroke" stroke-width="3"/>
            <line x1="110" y1="280" x2="130" y2="280" class="ghost-stroke"/>
            <line x1="100" y1="300" x2="140" y2="300" class="ghost-stroke" stroke-width="3"/>
            <line x1="110" y1="320" x2="130" y2="320" class="ghost-stroke"/>
            <text x="75" y="295" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold">Vdc</text>

            <!-- Top and Bottom DC rails -->
            <path d="M 120 200 L 320 200" class="ghost-stroke"/>
            <path d="M 120 380 L 320 380 L 540 380 L 850 380" class="ghost-stroke"/>

            <!-- Chopper CH1 -->
            <rect x="320" y="170" width="80" height="60" rx="8" class="ghost-fill"/>
            <text x="360" y="205" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold" text-anchor="middle">CH1</text>

            <!-- Diode D2 across CH1 -->
            <path d="M 320 150 L 400 150" class="ghost-stroke"/>
            <polygon points="350,140 350,160 370,150" class="ghost-fill"/>
            <line x1="370" y1="140" x2="370" y2="160" class="ghost-stroke"/>
            <text x="360" y="130" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="12" text-anchor="middle">D2</text>

            <!-- Mid Junction & CH2 / D1 -->
            <line x1="400" y1="200" x2="480" y2="200" class="ghost-stroke"/>
            <line x1="480" y1="200" x2="480" y2="250" class="ghost-stroke"/>
            <!-- Chopper CH2 -->
            <rect x="440" y="250" width="80" height="60" rx="8" class="ghost-fill"/>
            <text x="480" y="285" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold" text-anchor="middle">CH2</text>
            <line x1="480" y1="310" x2="480" y2="380" class="ghost-stroke"/>

            <!-- Diode D1 across CH2 -->
            <path d="M 540 200 L 540 380" class="ghost-stroke"/>
            <polygon points="525,290 555,290 540,260" class="ghost-fill"/>
            <line x1="525" y1="260" x2="555" y2="260" class="ghost-stroke"/>
            <text x="570" y="280" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="13">D1</text>

            <!-- Series Inductor L -->
            <path d="M 480 200 L 620 200 C 630 180, 650 180, 650 200 C 650 180, 670 180, 670 200 C 670 180, 690 180, 690 200 L 730 200" class="ghost-stroke"/>
            <text x="660" y="170" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="13" text-anchor="middle">L</text>

            <!-- Armature Resistance Ra -->
            <path d="M 730 200 L 740 185 L 755 215 L 770 185 L 785 215 L 795 200 L 850 200" class="ghost-stroke"/>
            <text x="765" y="170" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="13" text-anchor="middle">Ra</text>

            <!-- DC Machine Armature M & Eb -->
            <line x1="850" y1="200" x2="850" y2="240" class="ghost-stroke"/>
            <circle cx="850" cy="275" r="32" class="ghost-fill"/>
            <text x="850" y="282" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="20" font-weight="bold" text-anchor="middle">M</text>
            <line x1="850" y1="307" x2="850" y2="330" class="ghost-stroke"/>
            <circle cx="850" cy="345" r="14" class="ghost-fill"/>
            <text x="850" y="350" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="12" text-anchor="middle">Eb</text>
            <line x1="850" y1="359" x2="850" y2="380" class="ghost-stroke"/>
        """,
        "active_svg": """
            <!-- Comp 1: DC Source Vdc -->
            <g id="comp-c-vdc" class="active-comp">
                <line x1="120" y1="200" x2="120" y2="380" stroke="#fbbf24" stroke-width="3.5"/>
                <line x1="100" y1="260" x2="140" y2="260" stroke="#fbbf24" stroke-width="4.5"/>
                <line x1="110" y1="280" x2="130" y2="280" stroke="#fbbf24" stroke-width="3"/>
                <line x1="100" y1="300" x2="140" y2="300" stroke="#fbbf24" stroke-width="4.5"/>
                <line x1="110" y1="320" x2="130" y2="320" stroke="#fbbf24" stroke-width="3"/>
                <circle cx="120" cy="200" r="5" fill="#fbbf24"/>
                <circle cx="120" cy="380" r="5" fill="#fbbf24"/>
                <rect x="55" y="278" width="45" height="24" rx="4" fill="#2d220b" stroke="#fbbf24"/>
                <text x="77" y="295" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="middle">Vdc</text>
            </g>

            <!-- Comp 2: DC Rails -->
            <g id="comp-c-rails" class="active-comp">
                <path d="M 120 200 L 320 200" stroke="#38bdf8" stroke-width="3.5" fill="none" filter="url(#glow-cyan)"/>
                <path d="M 120 380 L 320 380 L 480 380 L 540 380 L 850 380" stroke="#38bdf8" stroke-width="3.5" fill="none" filter="url(#glow-cyan)"/>
                <circle cx="480" cy="380" r="4.5" fill="#38bdf8"/>
                <circle cx="540" cy="380" r="4.5" fill="#38bdf8"/>
                <circle cx="850" cy="380" r="4.5" fill="#38bdf8"/>
            </g>

            <!-- Comp 3: Motoring Chopper CH1 -->
            <g id="comp-c-ch1" class="active-comp">
                <rect x="320" y="170" width="80" height="60" rx="8" fill="#032732" stroke="#00f2fe" stroke-width="3" filter="url(#glow-cyan)"/>
                <text x="360" y="206" fill="#00f2fe" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="900" text-anchor="middle">CH1</text>
                <text x="360" y="222" fill="#7dd3fc" font-family="'JetBrains Mono', monospace" font-size="9" text-anchor="middle">MOTORING</text>
            </g>

            <!-- Comp 4: Regeneration Feedback Diode D2 -->
            <g id="comp-c-d2" class="active-comp">
                <path d="M 320 200 L 320 145 L 400 145 L 400 200" stroke="#10b981" stroke-width="2.5" fill="none"/>
                <polygon points="350,135 350,155 375,145" fill="#063826" stroke="#10b981" stroke-width="2.5" filter="url(#glow-green)"/>
                <line x1="375" y1="135" x2="375" y2="155" stroke="#10b981" stroke-width="3.5"/>
                <text x="362" y="125" fill="#34d399" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">D2 (Feedback)</text>
            </g>

            <!-- Comp 5: Braking Chopper CH2 -->
            <g id="comp-c-ch2" class="active-comp">
                <line x1="480" y1="200" x2="480" y2="250" stroke="#00f2fe" stroke-width="3"/>
                <rect x="440" y="250" width="80" height="60" rx="8" fill="#032732" stroke="#00f2fe" stroke-width="3" filter="url(#glow-cyan)"/>
                <line x1="480" y1="310" x2="480" y2="380" stroke="#00f2fe" stroke-width="3"/>
                <text x="480" y="286" fill="#00f2fe" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="900" text-anchor="middle">CH2</text>
                <text x="480" y="302" fill="#7dd3fc" font-family="'JetBrains Mono', monospace" font-size="9" text-anchor="middle">BRAKING</text>
            </g>

            <!-- Comp 6: Freewheeling Diode D1 -->
            <g id="comp-c-d1" class="active-comp">
                <path d="M 480 200 L 540 200 L 540 380" stroke="#10b981" stroke-width="3" fill="none"/>
                <polygon points="525,295 555,295 540,265" fill="#063826" stroke="#10b981" stroke-width="2.5" filter="url(#glow-green)"/>
                <line x1="525" y1="265" x2="555" y2="265" stroke="#10b981" stroke-width="3.5"/>
                <text x="568" y="284" fill="#34d399" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold">D1</text>
            </g>

            <!-- Comp 7: Smoothing Inductor L -->
            <g id="comp-c-inductor" class="active-comp">
                <path d="M 540 200 L 620 200 C 630 175, 650 175, 650 200 C 650 175, 670 175, 670 200 C 670 175, 690 175, 690 200 L 730 200" fill="none" stroke="#c084fc" stroke-width="3.5" filter="drop-shadow(0 0 8px rgba(192,132,252,0.6))"/>
                <rect x="645" y="152" width="30" height="20" rx="4" fill="#2d124d" stroke="#c084fc"/>
                <text x="660" y="166" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">L</text>
            </g>

            <!-- Comp 8: Armature Resistor Ra -->
            <g id="comp-c-resistor" class="active-comp">
                <path d="M 730 200 L 740 185 L 755 215 L 770 185 L 785 215 L 795 200 L 850 200" fill="none" stroke="#ff7b00" stroke-width="3.5" stroke-linejoin="round" filter="drop-shadow(0 0 8px rgba(255,123,0,0.6))"/>
                <rect x="750" y="152" width="30" height="20" rx="4" fill="#3a1c04" stroke="#ff7b00"/>
                <text x="765" y="166" fill="#ff7b00" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">Ra</text>
            </g>

            <!-- Comp 9: DC Motor Armature M -->
            <g id="comp-c-armature" class="active-comp">
                <line x1="850" y1="200" x2="850" y2="242" stroke="#f43f5e" stroke-width="3.5"/>
                <rect x="838" y="240" width="24" height="6" rx="2" fill="#334155" stroke="#f43f5e"/>
                <circle cx="850" cy="275" r="32" fill="#2d0b17" stroke="#f43f5e" stroke-width="3.5" filter="url(#glow-pink)"/>
                <text x="850" y="284" fill="#f43f5e" font-family="'JetBrains Mono', monospace" font-size="20" font-weight="900" text-anchor="middle">M</text>
                <rect x="838" y="304" width="24" height="6" rx="2" fill="#334155" stroke="#f43f5e"/>
                <line x1="850" y1="310" x2="850" y2="330" stroke="#f43f5e" stroke-width="3"/>
                <circle cx="850" cy="345" r="14" fill="#2d0b17" stroke="#f43f5e" stroke-width="2.5"/>
                <text x="850" y="349" fill="#f43f5e" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">Eb</text>
                <line x1="850" y1="359" x2="850" y2="380" stroke="#f43f5e" stroke-width="3"/>
                <circle cx="850" cy="380" r="4.5" fill="#f43f5e"/>
            </g>

            <!-- Comp 10: Conduction Flow Indicators -->
            <g id="comp-c-loops" class="active-comp">
                <path d="M 360 250 Q 420 260 480 230" fill="none" stroke="#38bdf8" stroke-dasharray="4,4" stroke-width="2" marker-end="url(#arrow-wire)"/>
                <rect x="620" y="280" width="160" height="26" rx="6" fill="#0c1e33" stroke="#38bdf8"/>
                <text x="700" y="297" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">Mode 1: CH1+D1 (Motoring)</text>
                <rect x="620" y="315" width="160" height="26" rx="6" fill="#1b2a1a" stroke="#10b981"/>
                <text x="700" y="332" fill="#34d399" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">Mode 2: CH2+D2 (Braking)</text>
            </g>
        """,
        "components": [
            {
                "id": "comp-c-vdc",
                "name": "DC Voltage Source (Vdc)",
                "tag": "Supply",
                "color": "#fbbf24",
                "center": {"x": 120, "y": 290},
                "radius": 55,
                "points": [{"x": 120, "y": 200}, {"x": 120, "y": 260}, {"x": 120, "y": 320}, {"x": 120, "y": 380}],
                "order": 1
            },
            {
                "id": "comp-c-rails",
                "name": "Power Bus Lines (+ & -)",
                "tag": "Bus",
                "color": "#38bdf8",
                "center": {"x": 220, "y": 290},
                "radius": 70,
                "points": [{"x": 120, "y": 200}, {"x": 220, "y": 200}, {"x": 320, "y": 200}, {"x": 120, "y": 380}, {"x": 220, "y": 380}, {"x": 320, "y": 380}],
                "order": 2
            },
            {
                "id": "comp-c-ch1",
                "name": "Motoring Chopper Switch (CH1)",
                "tag": "Switch",
                "color": "#00f2fe",
                "center": {"x": 360, "y": 200},
                "radius": 50,
                "points": [{"x": 320, "y": 200}, {"x": 360, "y": 200}, {"x": 400, "y": 200}],
                "order": 3
            },
            {
                "id": "comp-c-d2",
                "name": "Feedback Diode (D2)",
                "tag": "Diode",
                "color": "#10b981",
                "center": {"x": 360, "y": 145},
                "radius": 45,
                "points": [{"x": 320, "y": 145}, {"x": 360, "y": 145}, {"x": 400, "y": 145}],
                "order": 4
            },
            {
                "id": "comp-c-ch2",
                "name": "Regenerative Braking Chopper (CH2)",
                "tag": "Switch",
                "color": "#00f2fe",
                "center": {"x": 480, "y": 280},
                "radius": 50,
                "points": [{"x": 480, "y": 200}, {"x": 480, "y": 280}, {"x": 480, "y": 380}],
                "order": 5
            },
            {
                "id": "comp-c-d1",
                "name": "Freewheeling Diode (D1)",
                "tag": "Diode",
                "color": "#10b981",
                "center": {"x": 540, "y": 290},
                "radius": 50,
                "points": [{"x": 540, "y": 200}, {"x": 540, "y": 290}, {"x": 540, "y": 380}],
                "order": 6
            },
            {
                "id": "comp-c-inductor",
                "name": "Smoothing Inductor (L)",
                "tag": "Filter",
                "color": "#c084fc",
                "center": {"x": 660, "y": 200},
                "radius": 50,
                "points": [{"x": 620, "y": 200}, {"x": 660, "y": 200}, {"x": 700, "y": 200}],
                "order": 7
            },
            {
                "id": "comp-c-resistor",
                "name": "Armature Resistance (Ra)",
                "tag": "Load",
                "color": "#ff7b00",
                "center": {"x": 765, "y": 200},
                "radius": 45,
                "points": [{"x": 730, "y": 200}, {"x": 765, "y": 200}, {"x": 800, "y": 200}],
                "order": 8
            },
            {
                "id": "comp-c-armature",
                "name": "DC Motor Armature (M & Eb)",
                "tag": "Motor",
                "color": "#f43f5e",
                "center": {"x": 850, "y": 290},
                "radius": 70,
                "points": [{"x": 850, "y": 200}, {"x": 850, "y": 275}, {"x": 850, "y": 345}, {"x": 850, "y": 380}],
                "order": 9
            },
            {
                "id": "comp-c-loops",
                "name": "Two-Quadrant Modes (I & II)",
                "tag": "Legend",
                "color": "#38bdf8",
                "center": {"x": 700, "y": 310},
                "radius": 60,
                "points": [{"x": 650, "y": 290}, {"x": 750, "y": 290}, {"x": 650, "y": 330}, {"x": 750, "y": 330}],
                "order": 10
            }
        ]
    },

    # -------------------------------------------------------------------------
    # 3. Four-Quadrant Hoist Mechanical Dynamics (drive-q5)
    # -------------------------------------------------------------------------
    {
        "qid": "drive-q5",
        "aliases": ["drive-q4", "drive-q5", "drive-q5-fig2", "drive-q6", "drive-q6b"],
        "title": "Four-Quadrant Hoist Operation & Torque Dynamics",
        "module": 1,
        "marks": "7 Marks Guaranteed",
        "desc": "Universal university question! Understand physical gravity balance between Loaded Cage WL and Counterweight Wc across all four quadrants.",
        "equation": r"T - T_L = J\frac{d\omega}{dt}, \quad T_L = (W_L - W_c)R, \quad P = T\omega",
        "marking_tip": "Draw the hoist mechanical drum assembly on the left and the 4-Quadrant omega-T axes on the right with Motoring/Braking classifications.",
        "svg_viewBox": "0 0 1000 580",
        "ghost_svg": """
            <!-- Drum Assembly -->
            <circle cx="200" cy="180" r="60" class="ghost-fill"/>
            <circle cx="200" cy="180" r="16" class="ghost-stroke"/>
            <text x="200" y="186" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="12" text-anchor="middle">DRUM</text>
            <path d="M 140 180 L 140 380" class="ghost-stroke"/>
            <rect x="110" y="380" width="60" height="75" rx="6" class="ghost-fill"/>
            <text x="140" y="422" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold" text-anchor="middle">WL</text>

            <path d="M 260 180 L 260 320" class="ghost-stroke"/>
            <rect x="235" y="320" width="50" height="60" rx="6" class="ghost-fill"/>
            <text x="260" y="355" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold" text-anchor="middle">Wc</text>

            <!-- 4-Quadrant Axes -->
            <line x1="420" y1="280" x2="940" y2="280" class="ghost-stroke"/>
            <line x1="680" y1="40" x2="680" y2="520" class="ghost-stroke"/>
            <text x="925" y="270" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold">Torque T (+)</text>
            <text x="690" y="60" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold">Speed ω (+)</text>

            <!-- 4 Quadrants Box -->
            <rect x="710" y="80" width="200" height="170" rx="8" class="ghost-fill"/>
            <text x="810" y="140" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" text-anchor="middle">QUADRANT I</text>
            <text x="810" y="165" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">Forward Motoring</text>

            <rect x="450" y="80" width="200" height="170" rx="8" class="ghost-fill"/>
            <text x="550" y="140" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" text-anchor="middle">QUADRANT II</text>
            <text x="550" y="165" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">Forward Braking</text>

            <rect x="450" y="310" width="200" height="170" rx="8" class="ghost-fill"/>
            <text x="550" y="370" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" text-anchor="middle">QUADRANT III</text>
            <text x="550" y="395" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">Reverse Motoring</text>

            <rect x="710" y="310" width="200" height="170" rx="8" class="ghost-fill"/>
            <text x="810" y="370" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" text-anchor="middle">QUADRANT IV</text>
            <text x="810" y="395" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">Reverse Braking</text>
        """,
        "active_svg": """
            <!-- Comp 1: Drum & Motor Shaft -->
            <g id="comp-h-drum" class="active-comp">
                <circle cx="200" cy="180" r="60" fill="#1e1809" stroke="#fbbf24" stroke-width="3.5" filter="url(#glow-gold)"/>
                <circle cx="200" cy="180" r="16" fill="#fbbf24" stroke="#ffffff" stroke-width="2"/>
                <path d="M 200 135 A 45 45 0 0 1 245 180" stroke="#fbbf24" stroke-width="3" fill="none" marker-end="url(#arrow-wire)"/>
                <text x="200" y="185" fill="#070912" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="900" text-anchor="middle">ωm</text>
                <text x="200" y="260" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="middle">CABLE DRUM (Radius R)</text>
            </g>

            <!-- Comp 2: Loaded Cage WL -->
            <g id="comp-h-cage" class="active-comp">
                <line x1="140" y1="180" x2="140" y2="380" stroke="#f59e0b" stroke-width="4"/>
                <rect x="110" y="380" width="60" height="75" rx="6" fill="#3a1c04" stroke="#f59e0b" stroke-width="3"/>
                <text x="140" y="420" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="900" text-anchor="middle">WL</text>
                <text x="140" y="440" fill="#cbd5e1" font-family="'JetBrains Mono', monospace" font-size="10" text-anchor="middle">LOADED CAGE</text>
                <path d="M 140 460 L 140 495" stroke="#ef4444" stroke-width="3" marker-end="url(#arrow-wire)"/>
                <text x="160" y="485" fill="#ef4444" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">TL (Gravity)</text>
            </g>

            <!-- Comp 3: Counterweight Wc -->
            <g id="comp-h-counterweight" class="active-comp">
                <line x1="260" y1="180" x2="260" y2="320" stroke="#38bdf8" stroke-width="4"/>
                <rect x="235" y="320" width="50" height="60" rx="6" fill="#0c2d48" stroke="#38bdf8" stroke-width="3"/>
                <text x="260" y="354" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="15" font-weight="900" text-anchor="middle">Wc</text>
                <text x="260" y="372" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9" text-anchor="middle">WEIGHT</text>
            </g>

            <!-- Comp 4: Cartesian Axes -->
            <g id="comp-h-axes" class="active-comp">
                <line x1="420" y1="280" x2="940" y2="280" stroke="#cbd5e1" stroke-width="3" marker-end="url(#arrow-wire)"/>
                <line x1="680" y1="40" x2="680" y2="520" stroke="#cbd5e1" stroke-width="3" marker-end="url(#arrow-wire)"/>
                <text x="930" y="268" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold">Torque T (+)</text>
                <text x="690" y="60" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold">Speed ω (+)</text>
                <text x="430" y="268" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="12">(-) T</text>
                <text x="690" y="510" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="12">(-) ω</text>
            </g>

            <!-- Comp 5: Quadrant I (Forward Motoring) -->
            <g id="comp-h-q1" class="active-comp">
                <rect x="710" y="80" width="200" height="170" rx="8" fill="#052e16" stroke="#10b981" stroke-width="2.5" filter="url(#glow-green)"/>
                <text x="810" y="125" fill="#34d399" font-family="'JetBrains Mono', monospace" font-size="15" font-weight="900" text-anchor="middle">QUADRANT I</text>
                <text x="810" y="150" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="middle">FORWARD MOTORING</text>
                <text x="810" y="180" fill="#86efac" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">Hoisting Loaded Cage Up</text>
                <text x="810" y="205" fill="#cbd5e1" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">ω &gt; 0, T &gt; 0, P &gt; 0</text>
            </g>

            <!-- Comp 6: Quadrant II (Forward Braking) -->
            <g id="comp-h-q2" class="active-comp">
                <rect x="450" y="80" width="200" height="170" rx="8" fill="#2c1a04" stroke="#ff7b00" stroke-width="2.5"/>
                <text x="550" y="125" fill="#fb923c" font-family="'JetBrains Mono', monospace" font-size="15" font-weight="900" text-anchor="middle">QUADRANT II</text>
                <text x="550" y="150" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="middle">FORWARD BRAKING</text>
                <text x="550" y="180" fill="#fdba74" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">Ascent Deceleration</text>
                <text x="550" y="205" fill="#cbd5e1" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">ω &gt; 0, T &lt; 0, P &lt; 0</text>
            </g>

            <!-- Comp 7: Quadrant III (Reverse Motoring) -->
            <g id="comp-h-q3" class="active-comp">
                <rect x="450" y="310" width="200" height="170" rx="8" fill="#141c2f" stroke="#38bdf8" stroke-width="2.5" filter="url(#glow-cyan)"/>
                <text x="550" y="355" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="15" font-weight="900" text-anchor="middle">QUADRANT III</text>
                <text x="550" y="380" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="middle">REVERSE MOTORING</text>
                <text x="550" y="410" fill="#7dd3fc" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">Powering Empty Cage Down</text>
                <text x="550" y="435" fill="#cbd5e1" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">ω &lt; 0, T &lt; 0, P &gt; 0</text>
            </g>

            <!-- Comp 8: Quadrant IV (Reverse Braking) -->
            <g id="comp-h-q4" class="active-comp">
                <rect x="710" y="310" width="200" height="170" rx="8" fill="#2d0b17" stroke="#f43f5e" stroke-width="2.5" filter="url(#glow-pink)"/>
                <text x="810" y="355" fill="#f43f5e" font-family="'JetBrains Mono', monospace" font-size="15" font-weight="900" text-anchor="middle">QUADRANT IV</text>
                <text x="810" y="380" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="middle">REVERSE BRAKING</text>
                <text x="810" y="410" fill="#fca5a5" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">Lowering Loaded Cage Safely</text>
                <text x="810" y="435" fill="#cbd5e1" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">ω &lt; 0, T &gt; 0, P &lt; 0</text>
            </g>
        """,
        "components": [
            {
                "id": "comp-h-drum",
                "name": "Hoist Drum Assembly (Radius R)",
                "tag": "Mechanical",
                "color": "#fbbf24",
                "center": {"x": 200, "y": 180},
                "radius": 65,
                "points": [{"x": 200, "y": 180}, {"x": 140, "y": 180}, {"x": 260, "y": 180}],
                "order": 1
            },
            {
                "id": "comp-h-cage",
                "name": "Loaded Hoist Cage (WL)",
                "tag": "Load",
                "color": "#f59e0b",
                "center": {"x": 140, "y": 420},
                "radius": 60,
                "points": [{"x": 140, "y": 280}, {"x": 140, "y": 380}, {"x": 140, "y": 450}],
                "order": 2
            },
            {
                "id": "comp-h-counterweight",
                "name": "Balancing Counterweight (Wc)",
                "tag": "Weight",
                "color": "#38bdf8",
                "center": {"x": 260, "y": 350},
                "radius": 50,
                "points": [{"x": 260, "y": 250}, {"x": 260, "y": 320}, {"x": 260, "y": 380}],
                "order": 3
            },
            {
                "id": "comp-h-axes",
                "name": "Omega-Torque (ω-T) Coordinate Axes",
                "tag": "Axes",
                "color": "#cbd5e1",
                "center": {"x": 680, "y": 280},
                "radius": 80,
                "points": [{"x": 550, "y": 280}, {"x": 680, "y": 280}, {"x": 810, "y": 280}, {"x": 680, "y": 150}, {"x": 680, "y": 410}],
                "order": 4
            },
            {
                "id": "comp-h-q1",
                "name": "Quadrant I: Forward Motoring",
                "tag": "Quad 1",
                "color": "#10b981",
                "center": {"x": 810, "y": 165},
                "radius": 80,
                "points": [{"x": 750, "y": 120}, {"x": 870, "y": 120}, {"x": 810, "y": 200}],
                "order": 5
            },
            {
                "id": "comp-h-q2",
                "name": "Quadrant II: Forward Braking",
                "tag": "Quad 2",
                "color": "#ff7b00",
                "center": {"x": 550, "y": 165},
                "radius": 80,
                "points": [{"x": 490, "y": 120}, {"x": 610, "y": 120}, {"x": 550, "y": 200}],
                "order": 6
            },
            {
                "id": "comp-h-q3",
                "name": "Quadrant III: Reverse Motoring",
                "tag": "Quad 3",
                "color": "#38bdf8",
                "center": {"x": 550, "y": 395},
                "radius": 80,
                "points": [{"x": 490, "y": 350}, {"x": 610, "y": 350}, {"x": 550, "y": 430}],
                "order": 7
            },
            {
                "id": "comp-h-q4",
                "name": "Quadrant IV: Reverse Braking",
                "tag": "Quad 4",
                "color": "#f43f5e",
                "center": {"x": 810, "y": 395},
                "radius": 80,
                "points": [{"x": 750, "y": 350}, {"x": 870, "y": 350}, {"x": 810, "y": 430}],
                "order": 8
            }
        ]
    },

    # -------------------------------------------------------------------------
    # 4. Closed-Loop V/f Speed Control Scheme of 3-Phase Induction Motor (drive-q13)
    # -------------------------------------------------------------------------
    {
        "qid": "drive-q13",
        "aliases": ["drive-q12", "drive-q12b", "drive-q13", "drive-q13-fig2", "drive-q14", "drive-q14b", "drive-q15", "drive-q15b", "drive-q16", "drive-q17", "drive-q18"],
        "title": "Closed-Loop V/f Speed Control Scheme of Induction Motor",
        "module": 4,
        "marks": "7 Marks Guaranteed",
        "desc": "Maintains constant air-gap flux Φm by keeping stator voltage-to-frequency ratio V/f constant under closed-loop slip regulation.",
        "equation": r"\Phi_m \propto \frac{V_s}{f_s} = \text{constant}, \quad \omega_e^* = \omega_m + \omega_{sl}^*, \quad T_e \propto s\frac{V^2}{f}",
        "marking_tip": "Clearly show the summing comparator (ω* vs ω), the PI speed controller, slip adder, V/f generator block, and the PWM VSI feeding the 3-phase IM.",
        "svg_viewBox": "0 0 1000 580",
        "ghost_svg": """
            <!-- Reference Setter & Summing Point -->
            <line x1="80" y1="220" x2="160" y2="220" class="ghost-stroke"/>
            <text x="110" y="205" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="13">ωm*</text>
            <circle cx="180" cy="220" r="18" class="ghost-fill"/>

            <!-- PI Speed Controller -->
            <line x1="198" y1="220" x2="250" y2="220" class="ghost-stroke"/>
            <rect x="250" y="185" width="100" height="70" rx="8" class="ghost-fill"/>
            <text x="300" y="225" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="middle">PI SPEED</text>

            <!-- Slip Adder -->
            <line x1="350" y1="220" x2="410" y2="220" class="ghost-stroke"/>
            <text x="380" y="205" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="12">ωsl*</text>
            <circle cx="430" cy="220" r="18" class="ghost-fill"/>

            <!-- V/f Function Generator -->
            <line x1="448" y1="220" x2="510" y2="220" class="ghost-stroke"/>
            <text x="475" y="205" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="12">ωe*</text>
            <rect x="510" y="185" width="110" height="70" rx="8" class="ghost-fill"/>
            <text x="565" y="225" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold" text-anchor="middle">V/f RATIO</text>

            <!-- PWM Inverter (VSI) -->
            <line x1="620" y1="220" x2="680" y2="220" class="ghost-stroke"/>
            <rect x="680" y="175" width="110" height="90" rx="8" class="ghost-fill"/>
            <text x="735" y="225" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold" text-anchor="middle">PWM VSI</text>

            <!-- 3-Phase Induction Motor -->
            <line x1="790" y1="210" x2="840" y2="210" class="ghost-stroke"/>
            <line x1="790" y1="220" x2="840" y2="220" class="ghost-stroke"/>
            <line x1="790" y1="230" x2="840" y2="230" class="ghost-stroke"/>
            <circle cx="880" cy="220" r="40" class="ghost-fill"/>
            <text x="880" y="226" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold" text-anchor="middle">3Φ IM</text>

            <!-- Speed Sensor / Feedback Loop -->
            <path d="M 880 260 L 880 380 L 180 380 L 180 238" class="ghost-stroke"/>
            <rect x="500" y="355" width="130" height="50" rx="6" class="ghost-fill"/>
            <text x="565" y="385" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">SPEED SENSOR</text>
        """,
        "active_svg": """
            <!-- Comp 1: Reference Speed Input -->
            <g id="comp-vf-ref" class="active-comp">
                <line x1="80" y1="220" x2="162" y2="220" stroke="#fbbf24" stroke-width="3.5" marker-end="url(#arrow-wire)"/>
                <rect x="75" y="195" width="55" height="22" rx="4" fill="#2d220b" stroke="#fbbf24"/>
                <text x="102" y="210" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">ωm*</text>
            </g>

            <!-- Comp 2: Speed Summing Junction -->
            <g id="comp-vf-sum1" class="active-comp">
                <circle cx="180" cy="220" r="18" fill="#141c2f" stroke="#38bdf8" stroke-width="3" filter="url(#glow-cyan)"/>
                <text x="180" y="225" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold" text-anchor="middle">Σ</text>
                <text x="162" y="210" fill="#38bdf8" font-size="13">+</text>
                <text x="175" y="248" fill="#f43f5e" font-size="13">-</text>
            </g>

            <!-- Comp 3: PI Speed Controller -->
            <g id="comp-vf-pi" class="active-comp">
                <line x1="198" y1="220" x2="250" y2="220" stroke="#38bdf8" stroke-width="3.5" marker-end="url(#arrow-wire)"/>
                <rect x="250" y="185" width="100" height="70" rx="8" fill="#032732" stroke="#00f2fe" stroke-width="3" filter="url(#glow-cyan)"/>
                <text x="300" y="218" fill="#00f2fe" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="900" text-anchor="middle">PI SPEED</text>
                <text x="300" y="238" fill="#7dd3fc" font-family="'JetBrains Mono', monospace" font-size="10" text-anchor="middle">CONTROLLER</text>
            </g>

            <!-- Comp 4: Slip Adder Junction -->
            <g id="comp-vf-sum2" class="active-comp">
                <line x1="350" y1="220" x2="412" y2="220" stroke="#00f2fe" stroke-width="3.5" marker-end="url(#arrow-wire)"/>
                <text x="380" y="210" fill="#00f2fe" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold">ωsl*</text>
                <circle cx="430" cy="220" r="18" fill="#141c2f" stroke="#10b981" stroke-width="3" filter="url(#glow-green)"/>
                <text x="430" y="225" fill="#10b981" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold" text-anchor="middle">+</text>
            </g>

            <!-- Comp 5: V/f Generator Block -->
            <g id="comp-vf-gen" class="active-comp">
                <line x1="448" y1="220" x2="510" y2="220" stroke="#10b981" stroke-width="3.5" marker-end="url(#arrow-wire)"/>
                <text x="480" y="210" fill="#10b981" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold">ωe*</text>
                <rect x="510" y="185" width="110" height="70" rx="8" fill="#1e1809" stroke="#fbbf24" stroke-width="3" filter="url(#glow-gold)"/>
                <text x="565" y="218" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="900" text-anchor="middle">V/f RATIO</text>
                <text x="565" y="238" fill="#fef08a" font-family="'JetBrains Mono', monospace" font-size="10" text-anchor="middle">Vs* &amp; fs*</text>
            </g>

            <!-- Comp 6: PWM Inverter VSI -->
            <g id="comp-vf-vsi" class="active-comp">
                <line x1="620" y1="220" x2="680" y2="220" stroke="#fbbf24" stroke-width="3.5" marker-end="url(#arrow-wire)"/>
                <rect x="680" y="175" width="110" height="90" rx="8" fill="#2d124d" stroke="#c084fc" stroke-width="3" filter="drop-shadow(0 0 10px rgba(192,132,252,0.6))"/>
                <text x="735" y="215" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="900" text-anchor="middle">PWM VSI</text>
                <text x="735" y="238" fill="#e9d5ff" font-family="'JetBrains Mono', monospace" font-size="10" text-anchor="middle">IGBT INVERTER</text>
            </g>

            <!-- Comp 7: 3-Phase Induction Motor -->
            <g id="comp-vf-motor" class="active-comp">
                <line x1="790" y1="210" x2="840" y2="210" stroke="#c084fc" stroke-width="2.5"/>
                <line x1="790" y1="220" x2="840" y2="220" stroke="#c084fc" stroke-width="2.5"/>
                <line x1="790" y1="230" x2="840" y2="230" stroke="#c084fc" stroke-width="2.5"/>
                <circle cx="880" cy="220" r="40" fill="#2d0b17" stroke="#f43f5e" stroke-width="3.5" filter="url(#glow-pink)"/>
                <text x="880" y="226" fill="#f43f5e" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="900" text-anchor="middle">3Φ IM</text>
            </g>

            <!-- Comp 8: Speed Sensor Block -->
            <g id="comp-vf-sensor" class="active-comp">
                <path d="M 880 260 L 880 380 L 630 380" stroke="#f43f5e" stroke-width="3" fill="none"/>
                <rect x="500" y="355" width="130" height="50" rx="6" fill="#032732" stroke="#00f2fe" stroke-width="2.5"/>
                <text x="565" y="384" fill="#00f2fe" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">TACHOMETER</text>
            </g>

            <!-- Comp 9: Feedback Return Path -->
            <g id="comp-vf-feedback" class="active-comp">
                <path d="M 500 380 L 180 380 L 180 238" stroke="#00f2fe" stroke-width="3" fill="none" marker-end="url(#arrow-wire)"/>
                <path d="M 430 380 L 430 238" stroke="#10b981" stroke-width="2.5" stroke-dasharray="4,4" fill="none" marker-end="url(#arrow-wire)"/>
                <text x="320" y="370" fill="#00f2fe" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">Actual Speed Feedback (ωm)</text>
            </g>
        """,
        "components": [
            {
                "id": "comp-vf-ref",
                "name": "Reference Speed Setter (ωm*)",
                "tag": "Input",
                "color": "#fbbf24",
                "center": {"x": 102, "y": 210},
                "radius": 40,
                "points": [{"x": 80, "y": 220}, {"x": 130, "y": 220}, {"x": 160, "y": 220}],
                "order": 1
            },
            {
                "id": "comp-vf-sum1",
                "name": "Speed Summing Junction (Σ)",
                "tag": "Comparator",
                "color": "#38bdf8",
                "center": {"x": 180, "y": 220},
                "radius": 35,
                "points": [{"x": 180, "y": 220}],
                "order": 2
            },
            {
                "id": "comp-vf-pi",
                "name": "PI Speed Controller Block",
                "tag": "Control",
                "color": "#00f2fe",
                "center": {"x": 300, "y": 220},
                "radius": 55,
                "points": [{"x": 250, "y": 220}, {"x": 300, "y": 220}, {"x": 350, "y": 220}],
                "order": 3
            },
            {
                "id": "comp-vf-sum2",
                "name": "Slip Speed Adder (+)",
                "tag": "Adder",
                "color": "#10b981",
                "center": {"x": 430, "y": 220},
                "radius": 35,
                "points": [{"x": 430, "y": 220}],
                "order": 4
            },
            {
                "id": "comp-vf-gen",
                "name": "V/f Function Generator (Vs*/fs*)",
                "tag": "Flux",
                "color": "#fbbf24",
                "center": {"x": 565, "y": 220},
                "radius": 60,
                "points": [{"x": 510, "y": 220}, {"x": 565, "y": 220}, {"x": 620, "y": 220}],
                "order": 5
            },
            {
                "id": "comp-vf-vsi",
                "name": "3-Phase PWM Voltage Source Inverter",
                "tag": "Inverter",
                "color": "#c084fc",
                "center": {"x": 735, "y": 220},
                "radius": 60,
                "points": [{"x": 680, "y": 220}, {"x": 735, "y": 220}, {"x": 790, "y": 220}],
                "order": 6
            },
            {
                "id": "comp-vf-motor",
                "name": "3-Phase Induction Motor (3Φ IM)",
                "tag": "Motor",
                "color": "#f43f5e",
                "center": {"x": 880, "y": 220},
                "radius": 55,
                "points": [{"x": 840, "y": 220}, {"x": 880, "y": 220}],
                "order": 7
            },
            {
                "id": "comp-vf-sensor",
                "name": "Shaft Tachometer Speed Sensor",
                "tag": "Sensor",
                "color": "#00f2fe",
                "center": {"x": 565, "y": 380},
                "radius": 65,
                "points": [{"x": 880, "y": 320}, {"x": 880, "y": 380}, {"x": 565, "y": 380}],
                "order": 8
            },
            {
                "id": "comp-vf-feedback",
                "name": "Closed-Loop Feedback Path",
                "tag": "Loop",
                "color": "#00f2fe",
                "center": {"x": 300, "y": 380},
                "radius": 75,
                "points": [{"x": 500, "y": 380}, {"x": 300, "y": 380}, {"x": 180, "y": 380}, {"x": 180, "y": 260}],
                "order": 9
            }
        ]
    }
]
