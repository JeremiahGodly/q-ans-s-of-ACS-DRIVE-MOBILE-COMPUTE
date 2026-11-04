# -*- coding: utf-8 -*-
"""
vector_diagrams_mobile.py
=========================
Pure interactive vector SVG definitions and spatial geometry for Mobile Computing (CST415).
"""

MOBILE_DIAGRAMS = [
    # -------------------------------------------------------------------------
    # 3. GPRS Cellular Network Architecture and Packet Routing (mobile-q21)
    # -------------------------------------------------------------------------
    {
        "qid": "mobile-q21",
        "aliases": ["mobile-q19", "mobile-q20", "mobile-q21", "mobile-q22", "mobile-q27", "mobile-q30", "mobile-q31", "mobile-q32"],
        "title": "General Packet Radio Service (GPRS) Architecture & Data Routing",
        "module": 3,
        "marks": "7 Marks Guaranteed",
        "desc": "Trace the end-to-end packet forwarding route from mobile station through SGSN and GGSN to the public Internet!",
        "equation": r"\text{Throughput}_{\text{GPRS}} = N_{\text{slots}} \times R_{\text{CS}}, \quad \text{Latency} \propto \tau_{\text{Gb}} + \tau_{\text{Gn}} + \tau_{\text{Gi}}",
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

    # -------------------------------------------------------------------------
    # 1. Three-Tier Mobile Computing Architecture (mobile-q1)
    # -------------------------------------------------------------------------
    {
        "qid": "mobile-q1",
        "aliases": ["mobile-q1", "mobile-q2", "mobile-q3", "mobile-q4", "mobile-q5", "mobile-q6", "mobile-q7", "mobile-q8", "mobile-q9"],
        "title": "Three-Tier Mobile Computing Architecture",
        "module": 1,
        "marks": "7 Marks Guaranteed",
        "desc": "Separates Presentation (Mobile Client), Application Logic & Context Management (Middle Tier), and Enterprise Data (Backend Tier).",
        "equation": r"\text{Tier 1: GUI / Thin Client} \iff \text{Tier 2: Logic \& Context Adaptor} \iff \text{Tier 3: DB / Cloud Storage}",
        "marking_tip": "Clearly show the 3 distinct tiers, the wireless link between Tier 1 & Tier 2, and the enterprise secure link to Tier 3 database backend.",
        "svg_viewBox": "0 0 1000 580",
        "ghost_svg": """
            <!-- Tier 1 Box: Presentation (Mobile Client) -->
            <rect x="70" y="140" width="220" height="300" rx="14" class="ghost-fill"/>
            <rect x="95" y="170" width="170" height="200" rx="8" class="ghost-stroke"/>
            <text x="180" y="270" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold" text-anchor="middle">PRESENTATION</text>
            <text x="180" y="415" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="middle">TIER 1: CLIENT</text>

            <!-- Wireless Channel Link -->
            <path d="M 290 290 L 390 290" class="ghost-stroke"/>
            <path d="M 330 260 Q 350 290 330 320" class="ghost-stroke"/>
            <path d="M 350 250 Q 375 290 350 330" class="ghost-stroke"/>
            <text x="340" y="355" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">WIRELESS</text>

            <!-- Tier 2 Box: Application / Middleware -->
            <rect x="390" y="140" width="230" height="300" rx="14" class="ghost-fill"/>
            <rect x="415" y="175" width="180" height="80" rx="6" class="ghost-stroke"/>
            <text x="505" y="215" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="13" text-anchor="middle">APPLICATION</text>
            <text x="505" y="235" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">LOGIC</text>

            <rect x="415" y="275" width="180" height="80" rx="6" class="ghost-stroke"/>
            <text x="505" y="315" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="12" text-anchor="middle">CONTEXT MGR</text>
            <text x="505" y="415" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="middle">TIER 2: MIDDLEWARE</text>

            <!-- Enterprise Secure Link -->
            <path d="M 620 290 L 710 290" class="ghost-stroke"/>
            <rect x="645" y="270" width="40" height="40" rx="4" class="ghost-fill"/>
            <text x="665" y="295" fill="#64748b" font-size="14" text-anchor="middle">🔒</text>

            <!-- Tier 3 Box: Enterprise Backend Database -->
            <rect x="710" y="140" width="220" height="300" rx="14" class="ghost-fill"/>
            <ellipse cx="820" cy="200" rx="60" ry="20" class="ghost-fill"/>
            <path d="M 760 200 L 760 300 C 760 320 880 320 880 300 L 880 200" class="ghost-stroke"/>
            <ellipse cx="820" cy="250" rx="60" ry="20" class="ghost-stroke"/>
            <ellipse cx="820" cy="300" rx="60" ry="20" class="ghost-stroke"/>
            <text x="820" y="355" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="middle">ENTERPRISE DB</text>
            <text x="820" y="415" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="middle">TIER 3: BACKEND</text>
        """,
        "active_svg": """
            <!-- Comp 1: Tier 1 Client Shell -->
            <g id="comp-t3-client" class="active-comp">
                <rect x="70" y="140" width="220" height="300" rx="14" fill="#0f172a" stroke="#fbbf24" stroke-width="3" filter="url(#glow-gold)"/>
                <rect x="95" y="170" width="170" height="200" rx="8" fill="#1e1809" stroke="#fbbf24" stroke-width="2"/>
                <text x="180" y="260" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="900" text-anchor="middle">PRESENTATION</text>
                <text x="180" y="285" fill="#fef08a" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">GUI &amp; Local Cache</text>
                <rect x="85" y="395" width="190" height="32" rx="6" fill="#2d220b" stroke="#fbbf24"/>
                <text x="180" y="416" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="middle">TIER 1: MOBILE CLIENT</text>
            </g>

            <!-- Comp 2: Wireless Radio Channel -->
            <g id="comp-t3-radio" class="active-comp">
                <path d="M 290 290 L 390 290" stroke="#00f2fe" stroke-width="3.5" stroke-dasharray="4,4"/>
                <path d="M 330 260 Q 350 290 330 320" stroke="#00f2fe" stroke-width="3" fill="none" filter="url(#glow-cyan)"/>
                <path d="M 350 250 Q 375 290 350 330" stroke="#00f2fe" stroke-width="3" fill="none" filter="url(#glow-cyan)"/>
                <rect x="300" y="345" width="80" height="22" rx="4" fill="#032732" stroke="#00f2fe"/>
                <text x="340" y="360" fill="#00f2fe" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" text-anchor="middle">WIRELESS</text>
            </g>

            <!-- Comp 3: Tier 2 Application Logic -->
            <g id="comp-t3-applogic" class="active-comp">
                <rect x="390" y="140" width="230" height="300" rx="14" fill="#0f172a" stroke="#38bdf8" stroke-width="3" filter="url(#glow-cyan)"/>
                <rect x="415" y="175" width="180" height="80" rx="6" fill="#0c2d48" stroke="#38bdf8" stroke-width="2.5"/>
                <text x="505" y="210" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="900" text-anchor="middle">APPLICATION</text>
                <text x="505" y="232" fill="#bae6fd" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">Business Logic &amp; Session</text>
            </g>

            <!-- Comp 4: Tier 2 Context Manager -->
            <g id="comp-t3-context" class="active-comp">
                <rect x="415" y="275" width="180" height="80" rx="6" fill="#063826" stroke="#10b981" stroke-width="2.5" filter="url(#glow-green)"/>
                <text x="505" y="310" fill="#10b981" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="900" text-anchor="middle">CONTEXT MGR</text>
                <text x="505" y="332" fill="#a7f3d0" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">Transcoding &amp; Adaptation</text>
                <rect x="405" y="395" width="200" height="32" rx="6" fill="#0c1e33" stroke="#38bdf8"/>
                <text x="505" y="416" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="middle">TIER 2: MIDDLEWARE</text>
            </g>

            <!-- Comp 5: Secure Enterprise Gateway -->
            <g id="comp-t3-gateway" class="active-comp">
                <path d="M 620 290 L 710 290" stroke="#f43f5e" stroke-width="3.5"/>
                <rect x="645" y="270" width="40" height="40" rx="6" fill="#2d0b17" stroke="#f43f5e" stroke-width="2.5" filter="url(#glow-pink)"/>
                <text x="665" y="296" fill="#f43f5e" font-family="'JetBrains Mono', monospace" font-size="18" text-anchor="middle">🔒</text>
                <text x="665" y="325" fill="#f43f5e" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold" text-anchor="middle">FIREWALL</text>
            </g>

            <!-- Comp 6: Tier 3 Enterprise Database -->
            <g id="comp-t3-backend" class="active-comp">
                <rect x="710" y="140" width="220" height="300" rx="14" fill="#0f172a" stroke="#c084fc" stroke-width="3" filter="drop-shadow(0 0 10px rgba(192,132,252,0.6))"/>
                <ellipse cx="820" cy="200" rx="60" ry="20" fill="#2d124d" stroke="#c084fc" stroke-width="2.5"/>
                <path d="M 760 200 L 760 300 C 760 320 880 320 880 300 L 880 200" fill="#1a0c2e" stroke="#c084fc" stroke-width="2.5"/>
                <ellipse cx="820" cy="250" rx="60" ry="20" fill="none" stroke="#c084fc" stroke-width="2"/>
                <ellipse cx="820" cy="300" rx="60" ry="20" fill="#2d124d" stroke="#c084fc" stroke-width="2.5"/>
                <text x="820" y="255" fill="#e9d5ff" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="900" text-anchor="middle">DATA STORAGE</text>
                <text x="820" y="355" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="middle">ENTERPRISE RDBMS</text>
                <rect x="725" y="395" width="190" height="32" rx="6" fill="#220c3a" stroke="#c084fc"/>
                <text x="820" y="416" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="middle">TIER 3: BACKEND</text>
            </g>
        """,
        "components": [
            {
                "id": "comp-t3-client",
                "name": "Tier 1: Mobile Client (Presentation)",
                "tag": "Tier 1",
                "color": "#fbbf24",
                "center": {"x": 180, "y": 290},
                "radius": 110,
                "points": [{"x": 180, "y": 170}, {"x": 180, "y": 290}, {"x": 180, "y": 410}],
                "order": 1
            },
            {
                "id": "comp-t3-radio",
                "name": "Wireless Radio Link (Cellular/WLAN)",
                "tag": "Channel",
                "color": "#00f2fe",
                "center": {"x": 340, "y": 290},
                "radius": 50,
                "points": [{"x": 290, "y": 290}, {"x": 340, "y": 290}, {"x": 390, "y": 290}],
                "order": 2
            },
            {
                "id": "comp-t3-applogic",
                "name": "Tier 2: Application Logic Server",
                "tag": "Logic",
                "color": "#38bdf8",
                "center": {"x": 505, "y": 215},
                "radius": 60,
                "points": [{"x": 415, "y": 215}, {"x": 505, "y": 215}, {"x": 595, "y": 215}],
                "order": 3
            },
            {
                "id": "comp-t3-context",
                "name": "Tier 2: Context Manager & Adaptor",
                "tag": "Context",
                "color": "#10b981",
                "center": {"x": 505, "y": 340},
                "radius": 65,
                "points": [{"x": 415, "y": 315}, {"x": 505, "y": 315}, {"x": 505, "y": 415}],
                "order": 4
            },
            {
                "id": "comp-t3-gateway",
                "name": "Secure Firewall / Enterprise Gateway",
                "tag": "Security",
                "color": "#f43f5e",
                "center": {"x": 665, "y": 290},
                "radius": 45,
                "points": [{"x": 620, "y": 290}, {"x": 665, "y": 290}, {"x": 710, "y": 290}],
                "order": 5
            },
            {
                "id": "comp-t3-backend",
                "name": "Tier 3: Enterprise Database & Cloud Backend",
                "tag": "Tier 3",
                "color": "#c084fc",
                "center": {"x": 820, "y": 290},
                "radius": 110,
                "points": [{"x": 820, "y": 200}, {"x": 820, "y": 290}, {"x": 820, "y": 415}],
                "order": 6
            }
        ]
    },

    # -------------------------------------------------------------------------
    # 2. GSM Complete Cellular Network Architecture (mobile-q10)
    # -------------------------------------------------------------------------
    {
        "qid": "mobile-q10",
        "aliases": ["mobile-q10", "mobile-q11", "mobile-q12", "mobile-q13", "mobile-q14", "mobile-q15", "mobile-q16", "mobile-q17", "mobile-q18", "mobile-q19", "mobile-q20"],
        "title": "GSM Complete Cellular Network Architecture",
        "module": 2,
        "marks": "7 Marks Guaranteed",
        "desc": "Subsystems: Mobile Station (MS), Base Station Subsystem (BSS: BTS+BSC), and Network Switching Subsystem (NSS: MSC, HLR, VLR, AuC, EIR).",
        "equation": r"\text{MS} \xrightarrow{\text{Um}} \text{BTS} \xrightarrow{\text{Abis}} \text{BSC} \xrightarrow{\text{A}} \text{MSC/VLR} \longleftrightarrow \text{HLR/AuC/EIR} \xrightarrow{\text{PSTN}}",
        "marking_tip": "University standard requires demarcating the 3 subsystems (MS, BSS, NSS) and clearly labeling the Um air interface, Abis interface, and A interface.",
        "svg_viewBox": "0 0 1000 580",
        "ghost_svg": """
            <!-- Mobile Station MS -->
            <rect x="60" y="230" width="80" height="120" rx="10" class="ghost-fill"/>
            <text x="100" y="295" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold" text-anchor="middle">MS</text>
            <text x="100" y="320" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="10" text-anchor="middle">+ SIM</text>

            <!-- Um Air Interface -->
            <path d="M 140 290 L 220 290" class="ghost-stroke"/>
            <text x="180" y="280" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="12" text-anchor="middle">Um</text>

            <!-- BTS Tower -->
            <rect x="220" y="230" width="80" height="120" rx="8" class="ghost-fill"/>
            <path d="M 260 230 L 260 170 L 245 155 M 260 170 L 275 155" class="ghost-stroke"/>
            <text x="260" y="295" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold" text-anchor="middle">BTS</text>

            <!-- Abis Interface -->
            <line x1="300" y1="290" x2="380" y2="290" class="ghost-stroke"/>
            <text x="340" y="280" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="12" text-anchor="middle">Abis</text>

            <!-- BSC Controller -->
            <rect x="380" y="230" width="90" height="120" rx="8" class="ghost-fill"/>
            <text x="425" y="295" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold" text-anchor="middle">BSC</text>

            <!-- A Interface -->
            <line x1="470" y1="290" x2="550" y2="290" class="ghost-stroke"/>
            <text x="510" y="280" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="12" text-anchor="middle">A-I/F</text>

            <!-- MSC / VLR Core -->
            <rect x="550" y="220" width="120" height="140" rx="10" class="ghost-fill"/>
            <text x="610" y="285" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="bold" text-anchor="middle">MSC</text>
            <text x="610" y="315" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="13" text-anchor="middle">+ VLR</text>

            <!-- NSS Databases: HLR, AuC, EIR -->
            <path d="M 610 220 L 610 130 L 730 130" class="ghost-stroke"/>
            <rect x="730" y="80" width="100" height="50" rx="6" class="ghost-fill"/>
            <text x="780" y="112" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="13" text-anchor="middle">HLR</text>

            <rect x="730" y="145" width="100" height="50" rx="6" class="ghost-fill"/>
            <text x="780" y="177" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="13" text-anchor="middle">AuC</text>

            <rect x="730" y="210" width="100" height="50" rx="6" class="ghost-fill"/>
            <text x="780" y="242" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="13" text-anchor="middle">EIR</text>

            <!-- PSTN / ISDN Gateway -->
            <line x1="670" y1="290" x2="770" y2="290" class="ghost-stroke"/>
            <rect x="770" y="270" width="140" height="60" rx="8" class="ghost-fill"/>
            <text x="840" y="306" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold" text-anchor="middle">PSTN / ISDN</text>
        """,
        "active_svg": """
            <!-- Comp 1: Mobile Station MS -->
            <g id="comp-gsm-ms" class="active-comp">
                <rect x="60" y="230" width="80" height="120" rx="10" fill="#1e1809" stroke="#fbbf24" stroke-width="3" filter="url(#glow-gold)"/>
                <text x="100" y="285" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="18" font-weight="900" text-anchor="middle">MS</text>
                <rect x="72" y="305" width="56" height="22" rx="4" fill="#2d220b" stroke="#fbbf24"/>
                <text x="100" y="320" fill="#fef08a" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">SIM</text>
            </g>

            <!-- Comp 2: Um Air Interface -->
            <g id="comp-gsm-um" class="active-comp">
                <path d="M 140 290 L 220 290" stroke="#00f2fe" stroke-width="3" stroke-dasharray="4,4"/>
                <rect x="155" y="265" width="45" height="22" rx="4" fill="#032732" stroke="#00f2fe"/>
                <text x="177" y="280" fill="#00f2fe" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">Um</text>
            </g>

            <!-- Comp 3: Base Transceiver Station (BTS) -->
            <g id="comp-gsm-bts" class="active-comp">
                <rect x="220" y="230" width="80" height="120" rx="8" fill="#032732" stroke="#00f2fe" stroke-width="3" filter="url(#glow-cyan)"/>
                <path d="M 260 230 L 260 170 L 242 150 M 260 170 L 278 150" stroke="#00f2fe" stroke-width="3"/>
                <circle cx="260" cy="170" r="4" fill="#00f2fe"/>
                <text x="260" y="295" fill="#00f2fe" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="900" text-anchor="middle">BTS</text>
            </g>

            <!-- Comp 4: Abis Interface -->
            <g id="comp-gsm-abis" class="active-comp">
                <line x1="300" y1="290" x2="380" y2="290" stroke="#38bdf8" stroke-width="3.5" marker-end="url(#arrow-wire)"/>
                <rect x="315" y="265" width="50" height="22" rx="4" fill="#0c2d48" stroke="#38bdf8"/>
                <text x="340" y="280" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">Abis</text>
            </g>

            <!-- Comp 5: Base Station Controller (BSC) -->
            <g id="comp-gsm-bsc" class="active-comp">
                <rect x="380" y="230" width="90" height="120" rx="8" fill="#0c2d48" stroke="#38bdf8" stroke-width="3" filter="url(#glow-cyan)"/>
                <text x="425" y="295" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="900" text-anchor="middle">BSC</text>
            </g>

            <!-- Comp 6: A-Interface -->
            <g id="comp-gsm-aif" class="active-comp">
                <line x1="470" y1="290" x2="550" y2="290" stroke="#10b981" stroke-width="3.5" marker-end="url(#arrow-wire)"/>
                <rect x="490" y="265" width="45" height="22" rx="4" fill="#063826" stroke="#10b981"/>
                <text x="512" y="280" fill="#10b981" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">A-I/F</text>
            </g>

            <!-- Comp 7: Mobile Switching Center (MSC & VLR) -->
            <g id="comp-gsm-msc" class="active-comp">
                <rect x="550" y="220" width="120" height="140" rx="10" fill="#063826" stroke="#10b981" stroke-width="3" filter="url(#glow-green)"/>
                <text x="610" y="278" fill="#10b981" font-family="'JetBrains Mono', monospace" font-size="18" font-weight="900" text-anchor="middle">MSC</text>
                <rect x="565" y="295" width="90" height="26" rx="4" fill="#094530" stroke="#34d399"/>
                <text x="610" y="312" fill="#a7f3d0" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">+ VLR</text>
            </g>

            <!-- Comp 8: HLR / AuC / EIR Databases -->
            <g id="comp-gsm-db" class="active-comp">
                <path d="M 610 220 L 610 130 L 730 130" stroke="#c084fc" stroke-width="3" fill="none"/>
                <path d="M 670 180 L 730 180" stroke="#c084fc" stroke-width="2.5"/>
                <path d="M 670 230 L 730 230" stroke="#c084fc" stroke-width="2.5"/>
                <rect x="730" y="80" width="100" height="45" rx="6" fill="#2d124d" stroke="#c084fc" stroke-width="2.5" filter="drop-shadow(0 0 8px rgba(192,132,252,0.6))"/>
                <text x="780" y="108" fill="#e9d5ff" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="900" text-anchor="middle">HLR</text>
                <rect x="730" y="140" width="100" height="45" rx="6" fill="#2d124d" stroke="#c084fc" stroke-width="2.5"/>
                <text x="780" y="168" fill="#e9d5ff" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="900" text-anchor="middle">AuC</text>
                <rect x="730" y="200" width="100" height="45" rx="6" fill="#2d124d" stroke="#c084fc" stroke-width="2.5"/>
                <text x="780" y="228" fill="#e9d5ff" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="900" text-anchor="middle">EIR</text>
            </g>

            <!-- Comp 9: PSTN / ISDN Public Gateway -->
            <g id="comp-gsm-pstn" class="active-comp">
                <line x1="670" y1="290" x2="770" y2="290" stroke="#f43f5e" stroke-width="3.5" marker-end="url(#arrow-wire)"/>
                <rect x="770" y="265" width="145" height="60" rx="8" fill="#2d0b17" stroke="#f43f5e" stroke-width="3" filter="url(#glow-pink)"/>
                <text x="842" y="301" fill="#f43f5e" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="900" text-anchor="middle">PSTN / ISDN</text>
            </g>
        """,
        "components": [
            {
                "id": "comp-gsm-ms",
                "name": "Mobile Station (MS + SIM)",
                "tag": "Terminal",
                "color": "#fbbf24",
                "center": {"x": 100, "y": 290},
                "radius": 55,
                "points": [{"x": 100, "y": 230}, {"x": 100, "y": 290}, {"x": 100, "y": 350}],
                "order": 1
            },
            {
                "id": "comp-gsm-um",
                "name": "Um Radio Air Interface",
                "tag": "Wireless",
                "color": "#00f2fe",
                "center": {"x": 180, "y": 290},
                "radius": 45,
                "points": [{"x": 140, "y": 290}, {"x": 180, "y": 290}, {"x": 220, "y": 290}],
                "order": 2
            },
            {
                "id": "comp-gsm-bts",
                "name": "Base Transceiver Station (BTS)",
                "tag": "BSS",
                "color": "#00f2fe",
                "center": {"x": 260, "y": 260},
                "radius": 60,
                "points": [{"x": 260, "y": 170}, {"x": 260, "y": 260}, {"x": 260, "y": 350}],
                "order": 3
            },
            {
                "id": "comp-gsm-abis",
                "name": "Abis Digital Interface",
                "tag": "Link",
                "color": "#38bdf8",
                "center": {"x": 340, "y": 290},
                "radius": 45,
                "points": [{"x": 300, "y": 290}, {"x": 340, "y": 290}, {"x": 380, "y": 290}],
                "order": 4
            },
            {
                "id": "comp-gsm-bsc",
                "name": "Base Station Controller (BSC)",
                "tag": "BSS",
                "color": "#38bdf8",
                "center": {"x": 425, "y": 290},
                "radius": 55,
                "points": [{"x": 425, "y": 230}, {"x": 425, "y": 290}, {"x": 425, "y": 350}],
                "order": 5
            },
            {
                "id": "comp-gsm-aif",
                "name": "A-Interface (BSS to NSS)",
                "tag": "Link",
                "color": "#10b981",
                "center": {"x": 510, "y": 290},
                "radius": 45,
                "points": [{"x": 470, "y": 290}, {"x": 510, "y": 290}, {"x": 550, "y": 290}],
                "order": 6
            },
            {
                "id": "comp-gsm-msc",
                "name": "Mobile Switching Center (MSC + VLR)",
                "tag": "NSS",
                "color": "#10b981",
                "center": {"x": 610, "y": 290},
                "radius": 70,
                "points": [{"x": 610, "y": 220}, {"x": 610, "y": 290}, {"x": 610, "y": 360}],
                "order": 7
            },
            {
                "id": "comp-gsm-db",
                "name": "Network Databases (HLR, AuC, EIR)",
                "tag": "Registers",
                "color": "#c084fc",
                "center": {"x": 780, "y": 160},
                "radius": 80,
                "points": [{"x": 780, "y": 100}, {"x": 780, "y": 160}, {"x": 780, "y": 220}],
                "order": 8
            },
            {
                "id": "comp-gsm-pstn",
                "name": "PSTN / ISDN Public Gateway",
                "tag": "External",
                "color": "#f43f5e",
                "center": {"x": 842, "y": 290},
                "radius": 65,
                "points": [{"x": 770, "y": 290}, {"x": 842, "y": 290}, {"x": 915, "y": 290}],
                "order": 9
            }
        ]
    },

    # -------------------------------------------------------------------------
    # 3. IEEE 802.11 CSMA/CA & RTS/CTS Four-Way Handshake (mobile-q26)
    # -------------------------------------------------------------------------
    {
        "qid": "mobile-q26",
        "aliases": ["mobile-q23", "mobile-q24", "mobile-q25", "mobile-q26", "mobile-q28", "mobile-q29", "mobile-q33", "mobile-q34", "mobile-q35", "mobile-q36", "mobile-q37", "mobile-q38"],
        "title": "IEEE 802.11 RTS/CTS 4-Way Handshake with NAV Timing",
        "module": 4,
        "marks": "7 Marks Guaranteed",
        "desc": "Solves Hidden Terminal Problem: Node A sends RTS -> Node B broadcasts CTS -> Node C sets Network Allocation Vector (NAV) -> Node A sends DATA -> Node B ACKs.",
        "equation": r"\text{Total Duration} = \text{DIFS} + \text{RTS} + \text{SIFS} + \text{CTS} + \text{SIFS} + \text{DATA} + \text{SIFS} + \text{ACK}",
        "marking_tip": "Draw the 3 horizontal timelines (Sender A, Receiver B, Hidden Terminal C), the 4 control frames, SIFS/DIFS gaps, and the NAV virtual carrier sensing bar on Node C.",
        "svg_viewBox": "0 0 1000 580",
        "ghost_svg": """
            <!-- Timelines for Sender A, Receiver B, Hidden C -->
            <line x1="80" y1="160" x2="920" y2="160" class="ghost-stroke"/>
            <text x="60" y="165" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold">Node A (Sender)</text>

            <line x1="80" y1="280" x2="920" y2="280" class="ghost-stroke"/>
            <text x="60" y="285" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold">Node B (AP/Rx)</text>

            <line x1="80" y1="420" x2="920" y2="420" class="ghost-stroke"/>
            <text x="60" y="425" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold">Node C (Hidden)</text>

            <!-- DIFS + Backoff -->
            <rect x="180" y="135" width="70" height="50" rx="4" class="ghost-fill"/>
            <text x="215" y="165" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">DIFS</text>

            <!-- Frame 1: RTS -->
            <rect x="250" y="135" width="80" height="50" rx="4" class="ghost-fill"/>
            <text x="290" y="165" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold" text-anchor="middle">RTS</text>

            <!-- Frame 2: CTS -->
            <rect x="360" y="255" width="80" height="50" rx="4" class="ghost-fill"/>
            <text x="400" y="285" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold" text-anchor="middle">CTS</text>

            <!-- Frame 3: DATA Frame -->
            <rect x="470" y="135" width="280" height="50" rx="4" class="ghost-fill"/>
            <text x="610" y="165" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="15" font-weight="bold" text-anchor="middle">DATA FRAME</text>

            <!-- Frame 4: ACK -->
            <rect x="780" y="255" width="80" height="50" rx="4" class="ghost-fill"/>
            <text x="820" y="285" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold" text-anchor="middle">ACK</text>

            <!-- NAV (Network Allocation Vector) on Node C -->
            <rect x="440" y="405" width="420" height="30" rx="4" class="ghost-fill"/>
            <text x="650" y="425" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">NAV (Channel Busy Reservation)</text>
        """,
        "active_svg": """
            <!-- Comp 1: Timelines & Nodes -->
            <g id="comp-rts-nodes" class="active-comp">
                <line x1="80" y1="160" x2="940" y2="160" stroke="#cbd5e1" stroke-width="2.5"/>
                <text x="60" y="165" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold">Node A (Sender)</text>
                <line x1="80" y1="280" x2="940" y2="280" stroke="#cbd5e1" stroke-width="2.5"/>
                <text x="60" y="285" fill="#10b981" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold">Node B (AP/Rx)</text>
                <line x1="80" y1="420" x2="940" y2="420" stroke="#cbd5e1" stroke-width="2.5"/>
                <text x="60" y="425" fill="#f43f5e" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold">Node C (Hidden)</text>
            </g>

            <!-- Comp 2: DIFS & Backoff Delay -->
            <g id="comp-rts-difs" class="active-comp">
                <rect x="170" y="135" width="80" height="50" rx="4" fill="#1e1809" stroke="#fbbf24" stroke-width="2.5" filter="url(#glow-gold)"/>
                <text x="210" y="157" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">DIFS</text>
                <text x="210" y="174" fill="#fef08a" font-family="'JetBrains Mono', monospace" font-size="10" text-anchor="middle">+ Backoff</text>
            </g>

            <!-- Comp 3: RTS Frame (Request to Send) -->
            <g id="comp-rts-rts" class="active-comp">
                <rect x="250" y="135" width="80" height="50" rx="6" fill="#032732" stroke="#00f2fe" stroke-width="3" filter="url(#glow-cyan)"/>
                <text x="290" y="166" fill="#00f2fe" font-family="'JetBrains Mono', monospace" font-size="15" font-weight="900" text-anchor="middle">RTS</text>
                <!-- Arrow from A to B -->
                <path d="M 290 185 L 290 280" stroke="#00f2fe" stroke-width="2.5" stroke-dasharray="3,3" marker-end="url(#arrow-wire)"/>
            </g>

            <!-- Comp 4: SIFS Delay Gaps -->
            <g id="comp-rts-sifs" class="active-comp">
                <rect x="330" y="200" width="30" height="40" rx="3" fill="#0c1e33" stroke="#38bdf8"/>
                <text x="345" y="225" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="9" text-anchor="middle">SIFS</text>
                <rect x="440" y="200" width="30" height="40" rx="3" fill="#0c1e33" stroke="#38bdf8"/>
                <text x="455" y="225" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="9" text-anchor="middle">SIFS</text>
                <rect x="750" y="200" width="30" height="40" rx="3" fill="#0c1e33" stroke="#38bdf8"/>
                <text x="765" y="225" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="9" text-anchor="middle">SIFS</text>
            </g>

            <!-- Comp 5: CTS Frame (Clear to Send) -->
            <g id="comp-rts-cts" class="active-comp">
                <rect x="360" y="255" width="80" height="50" rx="6" fill="#063826" stroke="#10b981" stroke-width="3" filter="url(#glow-green)"/>
                <text x="400" y="286" fill="#10b981" font-family="'JetBrains Mono', monospace" font-size="15" font-weight="900" text-anchor="middle">CTS</text>
                <!-- Broadcast arrow to Node A and Node C -->
                <path d="M 400 255 L 400 160" stroke="#10b981" stroke-width="2.5" stroke-dasharray="3,3" marker-end="url(#arrow-wire)"/>
                <path d="M 400 305 L 400 420" stroke="#10b981" stroke-width="2.5" stroke-dasharray="3,3" marker-end="url(#arrow-wire)"/>
            </g>

            <!-- Comp 6: High Speed DATA Frame -->
            <g id="comp-rts-data" class="active-comp">
                <rect x="470" y="135" width="280" height="50" rx="6" fill="#2d124d" stroke="#c084fc" stroke-width="3" filter="drop-shadow(0 0 10px rgba(192,132,252,0.6))"/>
                <text x="610" y="166" fill="#e9d5ff" font-family="'JetBrains Mono', monospace" font-size="15" font-weight="900" text-anchor="middle">DATA TRANSMISSION</text>
                <path d="M 610 185 L 610 280" stroke="#c084fc" stroke-width="3" marker-end="url(#arrow-wire)"/>
            </g>

            <!-- Comp 7: ACK Frame -->
            <g id="comp-rts-ack" class="active-comp">
                <rect x="780" y="255" width="80" height="50" rx="6" fill="#063826" stroke="#10b981" stroke-width="3" filter="url(#glow-green)"/>
                <text x="820" y="286" fill="#10b981" font-family="'JetBrains Mono', monospace" font-size="15" font-weight="900" text-anchor="middle">ACK</text>
                <path d="M 820 255 L 820 160" stroke="#10b981" stroke-width="2.5" stroke-dasharray="3,3" marker-end="url(#arrow-wire)"/>
            </g>

            <!-- Comp 8: NAV on Hidden Terminal Node C -->
            <g id="comp-rts-nav" class="active-comp">
                <rect x="400" y="405" width="460" height="32" rx="6" fill="#2d0b17" stroke="#f43f5e" stroke-width="3" filter="url(#glow-pink)"/>
                <text x="630" y="426" fill="#f43f5e" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="900" text-anchor="middle">NAV (Virtual Carrier Sense: DEFER TRANSMISSION)</text>
            </g>
        """,
        "components": [
            {
                "id": "comp-rts-nodes",
                "name": "Node Timelines (Sender A, AP B, Hidden C)",
                "tag": "Nodes",
                "color": "#cbd5e1",
                "center": {"x": 200, "y": 280},
                "radius": 80,
                "points": [{"x": 100, "y": 160}, {"x": 100, "y": 280}, {"x": 100, "y": 420}],
                "order": 1
            },
            {
                "id": "comp-rts-difs",
                "name": "DIFS + Random Backoff Period",
                "tag": "Delay",
                "color": "#fbbf24",
                "center": {"x": 210, "y": 160},
                "radius": 45,
                "points": [{"x": 170, "y": 160}, {"x": 210, "y": 160}, {"x": 250, "y": 160}],
                "order": 2
            },
            {
                "id": "comp-rts-rts",
                "name": "RTS Control Frame (Request-to-Send)",
                "tag": "Frame 1",
                "color": "#00f2fe",
                "center": {"x": 290, "y": 160},
                "radius": 45,
                "points": [{"x": 250, "y": 160}, {"x": 290, "y": 160}, {"x": 330, "y": 160}],
                "order": 3
            },
            {
                "id": "comp-rts-sifs",
                "name": "SIFS Guard Intervals",
                "tag": "Gap",
                "color": "#38bdf8",
                "center": {"x": 345, "y": 220},
                "radius": 40,
                "points": [{"x": 345, "y": 220}, {"x": 455, "y": 220}],
                "order": 4
            },
            {
                "id": "comp-rts-cts",
                "name": "CTS Control Frame (Clear-to-Send)",
                "tag": "Frame 2",
                "color": "#10b981",
                "center": {"x": 400, "y": 280},
                "radius": 45,
                "points": [{"x": 360, "y": 280}, {"x": 400, "y": 280}, {"x": 440, "y": 280}],
                "order": 5
            },
            {
                "id": "comp-rts-data",
                "name": "DATA Packet High-Speed Transmission",
                "tag": "Data",
                "color": "#c084fc",
                "center": {"x": 610, "y": 160},
                "radius": 90,
                "points": [{"x": 470, "y": 160}, {"x": 610, "y": 160}, {"x": 750, "y": 160}],
                "order": 6
            },
            {
                "id": "comp-rts-ack",
                "name": "ACK Frame (Positive Acknowledgment)",
                "tag": "Frame 4",
                "color": "#10b981",
                "center": {"x": 820, "y": 280},
                "radius": 45,
                "points": [{"x": 780, "y": 280}, {"x": 820, "y": 280}, {"x": 860, "y": 280}],
                "order": 7
            },
            {
                "id": "comp-rts-nav",
                "name": "Network Allocation Vector (NAV) on Node C",
                "tag": "NAV",
                "color": "#f43f5e",
                "center": {"x": 630, "y": 420},
                "radius": 120,
                "points": [{"x": 400, "y": 420}, {"x": 630, "y": 420}, {"x": 860, "y": 420}],
                "order": 8
            }
        ]
    }
]
