# -*- coding: utf-8 -*-
"""
update_diagram_sources.py
=========================
Updates vector_diagrams_drives.py, vector_diagrams_acs.py, and vector_diagrams_mobile.py
with new high-yield diagrams and complete question alias mappings.
"""

import sys, os

def update_drives():
    path = os.path.join(os.path.dirname(__file__), "vector_diagrams_drives.py")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Add drive-q1 diagram at the top of DRIVES_DIAGRAMS list
    drive_q1_code = '''    # -------------------------------------------------------------------------
    # 0. Modern Electric Drive System Block Diagram (drive-q1)
    # -------------------------------------------------------------------------
    {
        "qid": "drive-q1",
        "aliases": ["drive-q1", "drive-q2", "drive-q3", "drive-q3b"],
        "title": "Block Diagram of a Modern Electric Drive System",
        "module": 1,
        "marks": "5 Marks Guaranteed",
        "desc": "Trace the forward power flow and closed-loop sensing/control pathways that govern every industrial electric motion control system!",
        "equation": r"T_e - T_L = J \\frac{d\\omega_m}{dt} + B\\omega_m, \\quad P_m = T_e \\cdot \\omega_m",
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
'''

    # Insert drive-q1 right after DRIVES_DIAGRAMS = [
    target = 'DRIVES_DIAGRAMS = ['
    if target in content and '"qid": "drive-q1"' not in content:
        content = content.replace(target, target + '\n' + drive_q1_code)

    # Add aliases to existing diagrams if not already present
    content = content.replace('"qid": "drive-q8",\n', '"qid": "drive-q8",\n        "aliases": ["drive-q8", "drive-q8b", "drive-q8-fig2", "drive-q8b-fig2", "drive-q7", "drive-q7b"],\n')
    content = content.replace('"qid": "drive-q10",\n', '"qid": "drive-q10",\n        "aliases": ["drive-q10", "drive-q10b", "drive-q10-fig2", "drive-q10b-fig2", "drive-q9", "drive-q9b", "drive-q11", "drive-q11-fig2"],\n')
    content = content.replace('"qid": "drive-q5",\n', '"qid": "drive-q5",\n        "aliases": ["drive-q4", "drive-q5", "drive-q5-fig2", "drive-q6", "drive-q6b"],\n')
    content = content.replace('"qid": "drive-q13",\n', '"qid": "drive-q13",\n        "aliases": ["drive-q12", "drive-q12b", "drive-q13", "drive-q13-fig2", "drive-q14", "drive-q14b", "drive-q15", "drive-q15b", "drive-q16", "drive-q17", "drive-q18"],\n')

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated vector_diagrams_drives.py successfully.")

def update_acs():
    path = os.path.join(os.path.dirname(__file__), "vector_diagrams_acs.py")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Add acs-q2 (Continuous-Time LTI System State Space Block Diagram)
    acs_q2_code = '''    # -------------------------------------------------------------------------
    # 0. General Continuous-Time LTI System State-Space Block Diagram (acs-q2)
    # -------------------------------------------------------------------------
    {
        "qid": "acs-q2",
        "aliases": ["acs-q1", "acs-q2", "acs-q3", "acs-q6", "acs-q7b", "acs-q8", "acs-q9", "acs-q9b", "acs-q10"],
        "title": "State-Space Block Diagram Representation of Continuous-Time LTI System",
        "module": 1,
        "marks": "6 Marks Guaranteed",
        "desc": "Trace the fundamental vector state equations governing modern control engineering: \\\\dot{x} = Ax + Bu and y = Cx + Du!",
        "equation": r"\\dot{\\mathbf{x}}(t) = \\mathbf{A}\\mathbf{x}(t) + \\mathbf{B}\\mathbf{u}(t), \\quad \\mathbf{y}(t) = \\mathbf{C}\\mathbf{x}(t) + \\mathbf{D}\\mathbf{u}(t)",
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
'''

    target = 'ACS_DIAGRAMS = ['
    if target in content and '"qid": "acs-q2"' not in content:
        content = content.replace(target, target + '\n' + acs_q2_code)

    content = content.replace('"qid": "acs-q4",\n', '"qid": "acs-q4",\n        "aliases": ["acs-q4", "acs-q4b"],\n')
    content = content.replace('"qid": "acs-q5",\n', '"qid": "acs-q5",\n        "aliases": ["acs-q5", "acs-q5-fig2", "acs-q7"],\n')
    content = content.replace('"qid": "acs-q13",\n', '"qid": "acs-q13",\n        "aliases": ["acs-q11", "acs-q12", "acs-q13", "acs-q13b", "acs-q14", "acs-q15", "acs-q16", "acs-q16b", "acs-q17", "acs-q17b", "acs-q18", "acs-q19", "acs-q20", "acs-q20b", "acs-q21", "acs-q22"],\n')

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated vector_diagrams_acs.py successfully.")

def update_mobile():
    path = os.path.join(os.path.dirname(__file__), "vector_diagrams_mobile.py")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Add mobile-q21 (GPRS Cellular Architecture & Packet Routing)
    mobile_q21_code = '''    # -------------------------------------------------------------------------
    # 3. GPRS Cellular Network Architecture and Packet Routing (mobile-q21)
    # -------------------------------------------------------------------------
    {
        "qid": "mobile-q21",
        "aliases": ["mobile-q19", "mobile-q20", "mobile-q21", "mobile-q22", "mobile-q27", "mobile-q30", "mobile-q31", "mobile-q32"],
        "title": "General Packet Radio Service (GPRS) Architecture & Data Routing",
        "module": 3,
        "marks": "7 Marks Guaranteed",
        "desc": "Trace the end-to-end packet forwarding route from mobile station through SGSN and GGSN to the public Internet!",
        "equation": r"\\text{Throughput}_{\\text{GPRS}} = N_{\\text{slots}} \\times R_{\\text{CS}}, \\quad \\text{Latency} \\propto \\tau_{\\text{Gb}} + \\tau_{\\text{Gn}} + \\tau_{\\text{Gi}}",
        "marking_tip": "Examiners award 2 marks for MS & BSS/PCU radio interface (Um, Gb), 2 marks for SGSN mobility & ciphering, 2 marks for GGSN router & Gi external IP gateway, and 1 mark for HLR/Billing interfaces.",
        "svg_viewBox": "0 0 1000 580",
        "ghost_svg": """
            <!-- MS GPRS Mobile Station -->
            <rect x="50" y="210" width="130" height="110" rx="10" class="ghost-fill"/>
            <text x="115" y="255" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700" text-anchor="middle">GPRS MS</text>
            <text x="115" y="278" fill="#475569" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">Class A / B / C</text>
            <text x="115" y="298" fill="#475569" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">Packet Terminal</text>

            <!-- Um Radio Interface -->
            <path d="M 180 265 L 260 265" class="ghost-stroke"/>
            <polygon points="260,265 248,259 248,271" class="ghost-fill"/>
            <text x="220" y="250" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">Um (Radio)</text>

            <!-- BSS with PCU -->
            <rect x="260" y="195" width="150" height="140" rx="10" class="ghost-fill"/>
            <text x="335" y="240" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700" text-anchor="middle">BSS</text>
            <text x="335" y="260" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="12" text-anchor="middle">(BTS + BSC)</text>
            <rect x="275" y="280" width="120" height="40" rx="6" class="ghost-fill"/>
            <text x="335" y="305" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="600" text-anchor="middle">PCU</text>

            <!-- Gb Interface -->
            <path d="M 410 265 L 490 265" class="ghost-stroke"/>
            <polygon points="490,265 478,259 478,271" class="ghost-fill"/>
            <text x="450" y="250" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">Gb (Frame Rly)</text>

            <!-- SGSN -->
            <rect x="490" y="200" width="150" height="130" rx="10" class="ghost-fill"/>
            <text x="565" y="245" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="700" text-anchor="middle">SGSN</text>
            <text x="565" y="270" fill="#475569" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">Mobility / Ciphering</text>
            <text x="565" y="290" fill="#475569" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">Packet Routing</text>

            <!-- Gn Interface (IP Backbone) -->
            <path d="M 640 265 L 720 265" class="ghost-stroke"/>
            <polygon points="720,265 708,259 708,271" class="ghost-fill"/>
            <text x="680" y="250" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">Gn (IP Tunnel)</text>

            <!-- GGSN -->
            <rect x="720" y="200" width="140" height="130" rx="10" class="ghost-fill"/>
            <text x="790" y="245" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="700" text-anchor="middle">GGSN</text>
            <text x="790" y="270" fill="#475569" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">Gateway Router</text>
            <text x="790" y="290" fill="#475569" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">PDP Context & IP</text>

            <!-- Gi Interface -->
            <path d="M 860 265 L 910 265" class="ghost-stroke"/>
            <polygon points="910,265 898,259 898,271" class="ghost-fill"/>
            <text x="885" y="250" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">Gi</text>

            <!-- External PDN / Internet Cloud -->
            <circle cx="945" cy="265" r="35" class="ghost-fill"/>
            <text x="945" y="260" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" text-anchor="middle">INTERNET</text>
            <text x="945" y="278" fill="#475569" font-family="'JetBrains Mono', monospace" font-size="10" text-anchor="middle">PDN / IP</text>

            <!-- HLR / EIR / Billing Registers (Top) -->
            <rect x="490" y="50" width="150" height="85" rx="8" class="ghost-fill"/>
            <text x="565" y="85" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700" text-anchor="middle">HLR / AuC</text>
            <text x="565" y="105" fill="#475569" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">Subscriber Profile</text>
            <path d="M 565 135 L 565 200" class="ghost-stroke"/>
            <text x="585" y="170" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="10.5">Gr (SS7)</text>

            <!-- Charging Gateway (Bottom) -->
            <rect x="620" y="420" width="160" height="85" rx="8" class="ghost-fill"/>
            <text x="700" y="455" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="700" text-anchor="middle">CHARGING / CGF</text>
            <text x="700" y="475" fill="#475569" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">CDR Billing Gateway</text>
            <path d="M 565 330 L 565 460 L 620 460" class="ghost-stroke"/>
            <path d="M 790 330 L 790 460 L 780 460" class="ghost-stroke"/>
        """,
        "components": [
            {
                "id": "comp-gprs-ms",
                "name": "GPRS Mobile Station (MS Class A/B/C)",
                "center": [115, 265],
                "radius": 45,
                "svg": """
                    <g id="comp-gprs-ms" class="active-comp" filter="url(#glow-pink)">
                        <rect x="50" y="210" width="130" height="110" rx="10" fill="rgba(236, 72, 153, 0.2)" stroke="#ec4899" stroke-width="2.5"/>
                        <text x="115" y="255" fill="#fdf2f8" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="800" text-anchor="middle">GPRS MS</text>
                        <text x="115" y="278" fill="#f472b6" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">Class A / B / C</text>
                        <text x="115" y="298" fill="#fbcfe8" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">Packet Terminal</text>
                    </g>
                """
            },
            {
                "id": "comp-bss-pcu",
                "name": "BSS with Packet Control Unit (PCU)",
                "center": [335, 265],
                "radius": 45,
                "svg": """
                    <g id="comp-bss-pcu" class="active-comp" filter="url(#glow-gold)">
                        <path d="M 180 265 L 260 265" stroke="#f59e0b" stroke-width="2.5"/>
                        <polygon points="260,265 248,259 248,271" fill="#f59e0b"/>
                        <text x="220" y="250" fill="#fef3c7" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">Um (Radio)</text>
                        <rect x="260" y="195" width="150" height="140" rx="10" fill="rgba(245, 158, 11, 0.2)" stroke="#f59e0b" stroke-width="2.5"/>
                        <text x="335" y="240" fill="#fde68a" font-family="'JetBrains Mono', monospace" font-size="15" font-weight="800" text-anchor="middle">BSS</text>
                        <text x="335" y="260" fill="#fde68a" font-family="'JetBrains Mono', monospace" font-size="12" text-anchor="middle">(BTS + BSC)</text>
                        <rect x="275" y="280" width="120" height="40" rx="6" fill="rgba(245, 158, 11, 0.3)" stroke="#fbbf24" stroke-width="1.8"/>
                        <text x="335" y="305" fill="#fff" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="700" text-anchor="middle">PCU</text>
                    </g>
                """
            },
            {
                "id": "comp-sgsn",
                "name": "Serving GPRS Support Node (SGSN)",
                "center": [565, 265],
                "radius": 45,
                "svg": """
                    <g id="comp-sgsn" class="active-comp" filter="url(#glow-cyan)">
                        <path d="M 410 265 L 490 265" stroke="#06b6d4" stroke-width="2.5"/>
                        <polygon points="490,265 478,259 478,271" fill="#06b6d4"/>
                        <text x="450" y="250" fill="#a5f3fc" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">Gb (Frame Rly)</text>
                        <rect x="490" y="200" width="150" height="130" rx="10" fill="rgba(6, 182, 212, 0.2)" stroke="#06b6d4" stroke-width="2.5"/>
                        <text x="565" y="245" fill="#e0f2fe" font-family="'JetBrains Mono', monospace" font-size="17" font-weight="800" text-anchor="middle">SGSN</text>
                        <text x="565" y="270" fill="#67e8f9" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">Mobility / Ciphering</text>
                        <text x="565" y="290" fill="#a5f3fc" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">Packet Routing</text>
                    </g>
                """
            },
            {
                "id": "comp-ggsn",
                "name": "Gateway GPRS Support Node (GGSN)",
                "center": [790, 265],
                "radius": 45,
                "svg": """
                    <g id="comp-ggsn" class="active-comp" filter="url(#glow-green)">
                        <path d="M 640 265 L 720 265" stroke="#10b981" stroke-width="2.5"/>
                        <polygon points="720,265 708,259 708,271" fill="#10b981"/>
                        <text x="680" y="250" fill="#a7f3d0" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">Gn (IP Tunnel)</text>
                        <rect x="720" y="200" width="140" height="130" rx="10" fill="rgba(16, 185, 129, 0.2)" stroke="#10b981" stroke-width="2.5"/>
                        <text x="790" y="245" fill="#ecfdf5" font-family="'JetBrains Mono', monospace" font-size="17" font-weight="800" text-anchor="middle">GGSN</text>
                        <text x="790" y="270" fill="#6ee7b7" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">Gateway Router</text>
                        <text x="790" y="290" fill="#a7f3d0" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">PDP Context & IP</text>
                    </g>
                """
            },
            {
                "id": "comp-internet-pdn",
                "name": "External Packet Data Network (Internet)",
                "center": [945, 265],
                "radius": 45,
                "svg": """
                    <g id="comp-internet-pdn" class="active-comp" filter="url(#glow-cyan)">
                        <path d="M 860 265 L 910 265" stroke="#06b6d4" stroke-width="2.5"/>
                        <polygon points="910,265 898,259 898,271" fill="#06b6d4"/>
                        <text x="885" y="250" fill="#a5f3fc" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">Gi</text>
                        <circle cx="945" cy="265" r="35" fill="rgba(6, 182, 212, 0.2)" stroke="#06b6d4" stroke-width="2.5"/>
                        <text x="945" y="260" fill="#e0f2fe" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="800" text-anchor="middle">INTERNET</text>
                        <text x="945" y="278" fill="#a5f3fc" font-family="'JetBrains Mono', monospace" font-size="10" text-anchor="middle">PDN / IP</text>
                    </g>
                """
            },
            {
                "id": "comp-hlr-billing",
                "name": "HLR/AuC Database & Charging Gateway (CGF)",
                "center": [565, 90],
                "radius": 45,
                "waypoints": [[565, 90], [700, 460]],
                "svg": """
                    <g id="comp-hlr-billing" class="active-comp" filter="url(#glow-gold)">
                        <!-- HLR -->
                        <rect x="490" y="50" width="150" height="85" rx="8" fill="rgba(245, 158, 11, 0.2)" stroke="#f59e0b" stroke-width="2.5"/>
                        <text x="565" y="85" fill="#fde68a" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="800" text-anchor="middle">HLR / AuC</text>
                        <text x="565" y="105" fill="#fef3c7" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">Subscriber Profile</text>
                        <path d="M 565 135 L 565 200" stroke="#f59e0b" stroke-width="2"/>
                        <text x="585" y="170" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="10.5">Gr (SS7)</text>
                        <!-- CGF -->
                        <rect x="620" y="420" width="160" height="85" rx="8" fill="rgba(245, 158, 11, 0.2)" stroke="#f59e0b" stroke-width="2.5"/>
                        <text x="700" y="455" fill="#fde68a" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="800" text-anchor="middle">CHARGING / CGF</text>
                        <text x="700" y="475" fill="#fef3c7" font-family="'JetBrains Mono', monospace" font-size="10.5" text-anchor="middle">CDR Billing Gateway</text>
                        <path d="M 565 330 L 565 460 L 620 460" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4 3"/>
                        <path d="M 790 330 L 790 460 L 780 460" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4 3"/>
                    </g>
                """
            }
        ]
    },
'''

    target = 'MOBILE_DIAGRAMS = ['
    if target in content and '"qid": "mobile-q21"' not in content:
        content = content.replace(target, target + '\n' + mobile_q21_code)

    content = content.replace('"qid": "mobile-q1",\n', '"qid": "mobile-q1",\n        "aliases": ["mobile-q1", "mobile-q2", "mobile-q3", "mobile-q4", "mobile-q5", "mobile-q6", "mobile-q7", "mobile-q8", "mobile-q9"],\n')
    content = content.replace('"qid": "mobile-q10",\n', '"qid": "mobile-q10",\n        "aliases": ["mobile-q10", "mobile-q11", "mobile-q12", "mobile-q13", "mobile-q14", "mobile-q15", "mobile-q16", "mobile-q17", "mobile-q18", "mobile-q19", "mobile-q20"],\n')
    content = content.replace('"qid": "mobile-q26",\n', '"qid": "mobile-q26",\n        "aliases": ["mobile-q23", "mobile-q24", "mobile-q25", "mobile-q26", "mobile-q28", "mobile-q29", "mobile-q33", "mobile-q34", "mobile-q35", "mobile-q36", "mobile-q37", "mobile-q38"],\n')

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated vector_diagrams_mobile.py successfully.")

if __name__ == "__main__":
    update_drives()
    update_acs()
    update_mobile()
