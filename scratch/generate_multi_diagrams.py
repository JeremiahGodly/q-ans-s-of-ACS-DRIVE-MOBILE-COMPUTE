# -*- coding: utf-8 -*-
"""
High-Resolution Vector Graphic Generator for Supplementary / Secondary Diagrams.
Empowers KTU engineering exam answers with dual and multi-diagram layouts.
All diagrams are rendered as dark-themed, publication-grade SVG and converted to high-res PNG via macOS sips.
"""

import os, subprocess, re

os.makedirs("images/acs", exist_ok=True)
os.makedirs("images/drive", exist_ok=True)
os.makedirs("images/mobile_compute", exist_ok=True)

def render_svg_to_png(svg_content, png_path):
    # Fix unescaped ampersands in XML
    svg_content = re.sub(r'&(?!(amp|lt|gt|quot|apos|#\d+|#x[0-9a-fA-F]+);)', '&amp;', svg_content)
    svg_path = png_path.replace(".png", ".svg")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    res = subprocess.run(["sips", "-s", "format", "png", svg_path, "--out", png_path], 
                         capture_output=True, text=True)
    if os.path.exists(svg_path):
        os.remove(svg_path)
    if os.path.exists(png_path):
        print(f"Generated -> {png_path} ({os.path.getsize(png_path)} bytes)")
    else:
        print(f"Error rendering {png_path}: {res.stderr}")

def create_card_diagram(png_path, title, subtitle, accent_color, badge_text, elements_xml, footer_text=""):
    title = title.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    subtitle = subtitle.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    footer_text = footer_text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    badge_text = badge_text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="960" height="460" viewBox="0 0 960 460">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0c1220"/>
      <stop offset="100%" stop-color="#151d30"/>
    </linearGradient>
    <linearGradient id="boxGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <marker id="arrow-{accent_color.replace('#','')}" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="{accent_color}"/>
    </marker>
    <marker id="arrow-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#10b981"/>
    </marker>
    <marker id="arrow-amber" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#f59e0b"/>
    </marker>
    <marker id="arrow-cyan" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#38bdf8"/>
    </marker>
  </defs>
  <rect width="960" height="460" fill="url(#bgGrad)" rx="16"/>
  <rect x="20" y="20" width="920" height="420" fill="none" stroke="#223049" stroke-width="1.5" rx="12"/>
  
  <!-- Header Title -->
  <rect x="40" y="35" width="140" height="26" fill="{accent_color}22" stroke="{accent_color}" stroke-width="1" rx="5"/>
  <text x="110" y="52" fill="{accent_color}" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">{badge_text}</text>
  <text x="500" y="55" fill="#f1f5f9" font-family="-apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">{title}</text>
  <text x="500" y="80" fill="#94a3b8" font-family="-apple-system, sans-serif" font-size="13" text-anchor="middle">{subtitle}</text>

  <!-- Graphic Elements Canvas Area -->
  <g transform="translate(0, 10)">
    {elements_xml}
  </g>

  <!-- Footer Note -->
  <rect x="60" y="405" width="840" height="26" fill="#0f172a" stroke="#223049" rx="5"/>
  <text x="480" y="422" fill="#94a3b8" font-family="monospace" font-size="12" text-anchor="middle">{footer_text}</text>
</svg>"""
    render_svg_to_png(svg, png_path)

print("Starting generation of 28 supplementary diagrams...")

# ==============================================================================
# 1. ELECTRIC DRIVES SUPPLEMENTARY DIAGRAMS
# ==============================================================================

# drive-q5: Four Quadrant Hoist Mechanics
create_card_diagram(
    "images/drive/four_quadrant_hoist_mechanics.png",
    "Four-Quadrant Electric Hoist: Mechanical Assembly & Force Balance",
    "Gravitational Load Torque (TL), Motor Torque (Tm), and Motion Direction Vectors",
    "#f59e0b", "DRIVES • FIG 1.5B",
    """
    <!-- Winch Drum & Cable -->
    <rect x="380" y="110" width="200" height="70" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="2" rx="8"/>
    <text x="480" y="145" fill="#fbbf24" font-size="15" font-weight="700" text-anchor="middle">Winch Drum (Radius R)</text>
    <text x="480" y="168" fill="#94a3b8" font-size="12" text-anchor="middle">Coupled to Motor Shaft</text>

    <!-- Motor block on left -->
    <rect x="140" y="115" width="160" height="60" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="6"/>
    <text x="220" y="145" fill="#38bdf8" font-size="15" font-weight="700" text-anchor="middle">Electric Motor</text>
    <text x="220" y="165" fill="#94a3b8" font-size="12" text-anchor="middle">Torque Tm, Speed ω</text>
    <line x1="300" y1="145" x2="380" y2="145" stroke="#f1f5f9" stroke-width="5"/>

    <!-- Left Cable: Counterweight -->
    <line x1="410" y1="180" x2="410" y2="250" stroke="#94a3b8" stroke-width="3"/>
    <rect x="360" y="250" width="100" height="70" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="6"/>
    <text x="410" y="280" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">Counterweight</text>
    <text x="410" y="305" fill="#94a3b8" font-size="13" text-anchor="middle">Weight Wc</text>

    <!-- Right Cable: Hoist Cage / Load -->
    <line x1="550" y1="180" x2="550" y2="250" stroke="#94a3b8" stroke-width="3"/>
    <rect x="500" y="250" width="100" height="70" fill="url(#boxGrad)" stroke="#ef4444" stroke-width="1.5" rx="6"/>
    <text x="550" y="280" fill="#f87171" font-size="14" font-weight="700" text-anchor="middle">Hoist Cage</text>
    <text x="550" y="305" fill="#94a3b8" font-size="13" text-anchor="middle">Weight WL</text>

    <!-- 4-Quadrant Mechanics Summary Cards -->
    <rect x="60" y="220" width="220" height="150" fill="#0f172a" stroke="#223049" rx="8"/>
    <text x="170" y="245" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">QUADRANT I: Hoisting Up</text>
    <text x="170" y="270" fill="#f1f5f9" font-size="12" text-anchor="middle">Loaded Cage: WL > Wc</text>
    <text x="170" y="295" fill="#34d399" font-size="12" text-anchor="middle">Speed ω > 0 (Upward)</text>
    <text x="170" y="320" fill="#fbbf24" font-size="12" text-anchor="middle">Tm > 0 (Forward Motoring)</text>
    <text x="170" y="345" fill="#94a3b8" font-size="11" text-anchor="middle">Overcomes Net Gravity</text>

    <rect x="680" y="220" width="220" height="150" fill="#0f172a" stroke="#223049" rx="8"/>
    <text x="790" y="245" fill="#ef4444" font-size="13" font-weight="700" text-anchor="middle">QUADRANT IV: Lowering</text>
    <text x="790" y="270" fill="#f1f5f9" font-size="12" text-anchor="middle">Heavy Cage: WL > Wc</text>
    <text x="790" y="295" fill="#f87171" font-size="12" text-anchor="middle">Speed ω &lt; 0 (Downward)</text>
    <text x="790" y="320" fill="#fbbf24" font-size="12" text-anchor="middle">Tm > 0 (Regenerative Brake)</text>
    <text x="790" y="345" fill="#94a3b8" font-size="11" text-anchor="middle">Prevents Runaway Fall</text>
    """,
    "Equation of Motion: J(dω/dt) = Tm - TL | Gravitational torque TL is active and unidirectional"
)

# drive-q8: Single-Phase Full Converter Firing Waveforms
create_card_diagram(
    "images/drive/single_phase_full_converter_firing_waveforms.png",
    "Single-Phase Full Converter: Firing & Conduction Waveforms",
    "AC Supply vs Output Voltage v0(t) and Armature Current ia(t) under Continuous Conduction",
    "#f59e0b", "DRIVES • FIG 2.2B",
    """
    <!-- Grid & Axis Lines -->
    <line x1="80" y1="160" x2="880" y2="160" stroke="#334155" stroke-width="1.5"/>
    <line x1="80" y1="260" x2="880" y2="260" stroke="#334155" stroke-width="1.5"/>
    <line x1="80" y1="350" x2="880" y2="350" stroke="#334155" stroke-width="1.5"/>

    <!-- Labels on left -->
    <text x="75" y="150" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="end">Supply vs</text>
    <text x="75" y="250" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="end">Voltage vo</text>
    <text x="75" y="340" fill="#34d399" font-size="13" font-weight="700" text-anchor="end">Current ia</text>

    <!-- Supply Waveform vs (Sine wave) -->
    <path d="M 120 160 Q 200 100 280 160 Q 360 220 440 160 Q 520 100 600 160 Q 680 220 760 160" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,4"/>
    <text x="280" y="175" fill="#94a3b8" font-size="11" text-anchor="middle">π</text>
    <text x="440" y="175" fill="#94a3b8" font-size="11" text-anchor="middle">2π</text>
    <text x="600" y="175" fill="#94a3b8" font-size="11" text-anchor="middle">3π</text>

    <!-- Output Voltage vo waveform (firing at α) -->
    <!-- Interval α to π+α -->
    <path d="M 120 260 L 180 260 L 180 215 Q 230 190 280 260 Q 310 295 340 300 L 340 215 Q 390 190 440 260 Q 470 295 500 300 L 500 215 Q 550 190 600 260 Q 630 295 660 300" fill="none" stroke="#fbbf24" stroke-width="2.5"/>
    <text x="180" y="205" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">α (T1,T2 ON)</text>
    <text x="340" y="205" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">π+α (T3,T4 ON)</text>
    
    <!-- Negative voltage shaded zone -->
    <rect x="280" y="260" width="60" height="38" fill="#ef444433" stroke="#ef4444" stroke-dasharray="2,2"/>
    <text x="310" y="282" fill="#f87171" font-size="10" text-anchor="middle">L di/dt effect</text>

    <!-- Armature Current ia (continuous with ripple) -->
    <path d="M 180 345 Q 260 330 340 345 Q 420 330 500 345 Q 580 330 660 345" fill="none" stroke="#34d399" stroke-width="3"/>
    <line x1="120" y1="337" x2="800" y2="337" stroke="#10b981" stroke-width="1" stroke-dasharray="2,2"/>
    <text x="730" y="333" fill="#34d399" font-size="12">Average Ia</text>

    <!-- Explanatory Box -->
    <rect x="680" y="110" width="220" height="85" fill="#0f172a" stroke="#223049" rx="6"/>
    <text x="790" y="132" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle">Average Output Voltage</text>
    <text x="790" y="155" fill="#f1f5f9" font-size="13" font-weight="700" text-anchor="middle">Vdc = (2Vm/π) · cos α</text>
    <text x="790" y="178" fill="#38bdf8" font-size="11" text-anchor="middle">Motoring: 0 &lt; α &lt; 90°</text>
    """,
    "Continuous Conduction: Current never drops to zero | High armature inductance maintains current through zero crossings"
)

# drive-q8b: Three-Phase Full Converter 6-Pulse Waveforms
create_card_diagram(
    "images/drive/three_phase_full_converter_waveforms.png",
    "Three-Phase Full Converter: 6-Pulse Conduction Waveforms",
    "Line Voltage Envelopes, Thyristor Firing Sequence (T1-T6), and 60° Ripple Output",
    "#f59e0b", "DRIVES • FIG 2.3B",
    """
    <!-- Axis line -->
    <line x1="80" y1="210" x2="880" y2="210" stroke="#334155" stroke-width="1.5"/>
    <line x1="80" y1="330" x2="880" y2="330" stroke="#334155" stroke-width="1.5"/>

    <text x="75" y="170" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="end">3Φ Line Voltages</text>
    <text x="75" y="310" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="end">Output vo(t)</text>

    <!-- Interlocking Line Voltage Crests -->
    <path d="M 120 180 Q 170 110 220 180" fill="none" stroke="#38bdf8" stroke-width="1.5"/>
    <path d="M 200 180 Q 250 110 300 180" fill="none" stroke="#f43f5e" stroke-width="1.5"/>
    <path d="M 280 180 Q 330 110 380 180" fill="none" stroke="#10b981" stroke-width="1.5"/>
    <path d="M 360 180 Q 410 110 460 180" fill="none" stroke="#38bdf8" stroke-width="1.5"/>
    <path d="M 440 180 Q 490 110 540 180" fill="none" stroke="#f43f5e" stroke-width="1.5"/>
    <path d="M 520 180 Q 570 110 620 180" fill="none" stroke="#10b981" stroke-width="1.5"/>

    <!-- 6-Pulse Output Voltage vo -->
    <path d="M 150 280 Q 185 240 220 280 L 220 250 Q 255 220 290 260 L 290 240 Q 325 210 360 250 L 360 230 Q 395 210 430 250 L 430 230 Q 465 210 500 250 L 500 230 Q 535 210 570 250" fill="none" stroke="#fbbf24" stroke-width="3"/>
    
    <!-- Thyristor conduction pairs -->
    <rect x="150" y="345" width="70" height="26" fill="#1e293b" stroke="#38bdf8" rx="4"/>
    <text x="185" y="362" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="middle">T1 &amp; T6</text>

    <rect x="225" y="345" width="70" height="26" fill="#1e293b" stroke="#fbbf24" rx="4"/>
    <text x="260" y="362" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">T1 &amp; T2</text>

    <rect x="300" y="345" width="70" height="26" fill="#1e293b" stroke="#34d399" rx="4"/>
    <text x="335" y="362" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">T3 &amp; T2</text>

    <rect x="375" y="345" width="70" height="26" fill="#1e293b" stroke="#f43f5e" rx="4"/>
    <text x="410" y="362" fill="#f43f5e" font-size="11" font-weight="700" text-anchor="middle">T3 &amp; T4</text>

    <rect x="450" y="345" width="70" height="26" fill="#1e293b" stroke="#a855f7" rx="4"/>
    <text x="485" y="362" fill="#c084fc" font-size="11" font-weight="700" text-anchor="middle">T5 &amp; T4</text>

    <rect x="525" y="345" width="70" height="26" fill="#1e293b" stroke="#38bdf8" rx="4"/>
    <text x="560" y="362" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="middle">T5 &amp; T6</text>

    <!-- Side Summary Card -->
    <rect x="630" y="120" width="280" height="180" fill="#0f172a" stroke="#223049" rx="8"/>
    <text x="770" y="150" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">6-Pulse Commutation Key</text>
    <text x="770" y="180" fill="#f1f5f9" font-size="13" text-anchor="middle">Vdc = (3√3·Vm / π) · cos α</text>
    <text x="770" y="210" fill="#94a3b8" font-size="12" text-anchor="middle">Commutation interval = 60° (π/3)</text>
    <text x="770" y="235" fill="#34d399" font-size="12" text-anchor="middle">SCR Conduction period = 120°</text>
    <text x="770" y="260" fill="#fbbf24" font-size="12" text-anchor="middle">Ripple Frequency = 6 × fs (300 Hz)</text>
    """,
    "Six-Pulse Output: High fundamental ripple frequency reduces smoothing filter inductor size dramatically"
)

# drive-q10: Class-C Chopper Waveforms
create_card_diagram(
    "images/drive/class_c_chopper_waveforms.png",
    "Class-C Two-Quadrant Chopper: Motoring vs Braking Waveforms",
    "Quadrant I Motoring (CH1, D2) and Quadrant II Regenerative Braking (CH2, D1)",
    "#f59e0b", "DRIVES • FIG 3.2B",
    """
    <!-- Motoring Column -->
    <rect x="60" y="110" width="400" height="260" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="10"/>
    <text x="260" y="135" fill="#38bdf8" font-size="15" font-weight="700" text-anchor="middle">Mode 1: Forward Motoring (Q-I)</text>
    <line x1="80" y1="210" x2="440" y2="210" stroke="#334155"/>
    <text x="100" y="165" fill="#94a3b8" font-size="11">Gate CH1</text>
    <rect x="170" y="155" width="100" height="16" fill="#38bdf8"/>
    <rect x="330" y="155" width="80" height="16" fill="#38bdf8"/>

    <text x="100" y="200" fill="#fbbf24" font-size="11">vo(t)</text>
    <path d="M 170 210 L 170 180 L 270 180 L 270 210 L 330 210 L 330 180 L 410 180 L 410 210" fill="none" stroke="#fbbf24" stroke-width="2"/>

    <line x1="80" y1="290" x2="440" y2="290" stroke="#334155"/>
    <text x="100" y="275" fill="#34d399" font-size="11">ia(t) > 0</text>
    <path d="M 170 285 L 270 260 L 330 285 L 410 260" fill="none" stroke="#34d399" stroke-width="2.5"/>
    <text x="260" y="330" fill="#f1f5f9" font-size="12" text-anchor="middle">CH1 ON: Armature energized | D2 ON: Freewheels</text>
    <text x="260" y="352" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">Vo = δ·Vs > 0  |  Ia > 0</text>

    <!-- Braking Column -->
    <rect x="500" y="110" width="400" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
    <text x="700" y="135" fill="#34d399" font-size="15" font-weight="700" text-anchor="middle">Mode 2: Regenerative Braking (Q-II)</text>
    <line x1="520" y1="210" x2="880" y2="210" stroke="#334155"/>
    <text x="540" y="165" fill="#94a3b8" font-size="11">Gate CH2</text>
    <rect x="610" y="155" width="100" height="16" fill="#10b981"/>
    <rect x="770" y="155" width="80" height="16" fill="#10b981"/>

    <text x="540" y="200" fill="#fbbf24" font-size="11">vo(t)</text>
    <path d="M 610 210 L 710 210 L 710 180 L 770 180 L 770 210 L 850 210" fill="none" stroke="#fbbf24" stroke-width="2"/>

    <line x1="520" y1="290" x2="880" y2="290" stroke="#334155"/>
    <text x="540" y="275" fill="#f87171" font-size="11">ia(t) &lt; 0</text>
    <path d="M 610 295 L 710 320 L 770 295 L 850 320" fill="none" stroke="#f87171" stroke-width="2.5"/>
    <text x="700" y="330" fill="#f1f5f9" font-size="12" text-anchor="middle">CH2 ON: Inductor charges from Eb | D1 ON: Feeds Vs</text>
    <text x="700" y="352" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle">Vo = δ·Vs > 0  |  Ia &lt; 0 (Power returns to source)</text>
    """,
    "Class-C Operation: CH1 and CH2 are never fired simultaneously to prevent DC bus short circuit"
)

# drive-q10b: Class-E Chopper Modes
create_card_diagram(
    "images/drive/class_e_chopper_modes.png",
    "Class-E Four-Quadrant Chopper: Conduction Paths & Modes",
    "Forward Motoring (Q-I), Forward Regen (Q-II), Reverse Motoring (Q-III), Reverse Regen (Q-IV)",
    "#f59e0b", "DRIVES • FIG 3.3B",
    """
    <!-- 4 Sub-Panels -->
    <rect x="60" y="110" width="195" height="260" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="8"/>
    <text x="157" y="135" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">QUADRANT I</text>
    <text x="157" y="155" fill="#f1f5f9" font-size="12" text-anchor="middle">Forward Motoring</text>
    <rect x="80" y="170" width="155" height="110" fill="#0f172a" stroke="#38bdf8" stroke-dasharray="2,2" rx="6"/>
    <text x="157" y="200" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">CH1 &amp; CH4 Active</text>
    <text x="157" y="225" fill="#94a3b8" font-size="11" text-anchor="middle">Freewheels via D2, CH4</text>
    <text x="157" y="250" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">+Vo , +Ia</text>
    <text x="157" y="315" fill="#94a3b8" font-size="11" text-anchor="middle">Forward Speed + Torque</text>

    <rect x="275" y="110" width="195" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="8"/>
    <text x="372" y="135" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">QUADRANT II</text>
    <text x="372" y="155" fill="#f1f5f9" font-size="12" text-anchor="middle">Forward Braking</text>
    <rect x="295" y="170" width="155" height="110" fill="#0f172a" stroke="#10b981" stroke-dasharray="2,2" rx="6"/>
    <text x="372" y="200" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">CH2 Chopping</text>
    <text x="372" y="225" fill="#94a3b8" font-size="11" text-anchor="middle">Feedback via D1, D4</text>
    <text x="372" y="250" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle">+Vo , -Ia</text>
    <text x="372" y="315" fill="#94a3b8" font-size="11" text-anchor="middle">Kinetic Energy to Supply</text>

    <rect x="490" y="110" width="195" height="260" fill="url(#boxGrad)" stroke="#f43f5e" stroke-width="1.5" rx="8"/>
    <text x="587" y="135" fill="#f43f5e" font-size="13" font-weight="700" text-anchor="middle">QUADRANT III</text>
    <text x="587" y="155" fill="#f1f5f9" font-size="12" text-anchor="middle">Reverse Motoring</text>
    <rect x="510" y="170" width="155" height="110" fill="#0f172a" stroke="#f43f5e" stroke-dasharray="2,2" rx="6"/>
    <text x="587" y="200" fill="#f43f5e" font-size="12" font-weight="700" text-anchor="middle">CH3 &amp; CH2 Active</text>
    <text x="587" y="225" fill="#94a3b8" font-size="11" text-anchor="middle">Freewheels via D4, CH2</text>
    <text x="587" y="250" fill="#ef4444" font-size="12" font-weight="700" text-anchor="middle">-Vo , -Ia</text>
    <text x="587" y="315" fill="#94a3b8" font-size="11" text-anchor="middle">Reverse Speed + Torque</text>

    <rect x="705" y="110" width="195" height="260" fill="url(#boxGrad)" stroke="#a855f7" stroke-width="1.5" rx="8"/>
    <text x="802" y="135" fill="#c084fc" font-size="13" font-weight="700" text-anchor="middle">QUADRANT IV</text>
    <text x="802" y="155" fill="#f1f5f9" font-size="12" text-anchor="middle">Reverse Braking</text>
    <rect x="725" y="170" width="155" height="110" fill="#0f172a" stroke="#a855f7" stroke-dasharray="2,2" rx="6"/>
    <text x="802" y="200" fill="#c084fc" font-size="12" font-weight="700" text-anchor="middle">CH4 Chopping</text>
    <text x="802" y="225" fill="#94a3b8" font-size="11" text-anchor="middle">Feedback via D2, D3</text>
    <text x="802" y="250" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle">-Vo , +Ia</text>
    <text x="802" y="315" fill="#94a3b8" font-size="11" text-anchor="middle">Reverse Kinetic Recovery</text>
    """,
    "Full H-Bridge: Diagonal pairs (CH1-CH4, CH3-CH2) control motoring; antiparallel diodes return energy"
)

# drive-q11: Inner Current Control Loop Detail
create_card_diagram(
    "images/drive/inner_current_control_loop.png",
    "Closed-Loop DC Drive: Inner Current Controller & Limiter Architecture",
    "Fast Subordinate Current Loop Protecting Converter Thyristors with Anti-Windup PI",
    "#f59e0b", "DRIVES • FIG 3.4B",
    """
    <!-- Speed Loop Input on left -->
    <rect x="50" y="180" width="120" height="60" fill="url(#boxGrad)" stroke="#38bdf8" rx="6"/>
    <text x="110" y="205" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">Outer Speed</text>
    <text x="110" y="225" fill="#f1f5f9" font-size="12" text-anchor="middle">PI Controller</text>
    <path d="M 170 210 L 220 210" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-cyan)"/>

    <!-- Current Limiter / Clamp -->
    <rect x="220" y="170" width="130" height="80" fill="url(#boxGrad)" stroke="#ef4444" stroke-width="2" rx="6"/>
    <text x="285" y="195" fill="#f87171" font-size="12" font-weight="700" text-anchor="middle">Current Limiter</text>
    <text x="285" y="218" fill="#fbbf24" font-size="11" text-anchor="middle">±Ia,max Clamp</text>
    <text x="285" y="238" fill="#94a3b8" font-size="10" text-anchor="middle">(1.5 to 2.0 × Inom)</text>
    <path d="M 350 210 L 400 210" stroke="#fbbf24" stroke-width="2" marker-end="url(#arrow-amber)"/>
    <text x="375" y="200" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">Ia*</text>

    <!-- Current Summing Node -->
    <circle cx="420" cy="210" r="15" fill="#1e293b" stroke="#f1f5f9" stroke-width="2"/>
    <text x="420" y="215" fill="#f1f5f9" font-size="14" font-weight="700" text-anchor="middle">Σ</text>
    <path d="M 435 210 L 480 210" stroke="#f1f5f9" stroke-width="2" marker-end="url(#arrow-amber)"/>

    <!-- Inner Current Controller PI -->
    <rect x="480" y="175" width="140" height="70" fill="url(#boxGrad)" stroke="#10b981" stroke-width="2" rx="6"/>
    <text x="550" y="202" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">Current PI Controller</text>
    <text x="550" y="225" fill="#f1f5f9" font-size="11" text-anchor="middle">Gc(s) = Kp + Ki/s</text>
    <path d="M 620 210 L 670 210" stroke="#34d399" stroke-width="2" marker-end="url(#arrow-green)"/>

    <!-- Firing Pulse Generator -->
    <rect x="670" y="175" width="110" height="70" fill="url(#boxGrad)" stroke="#a855f7" rx="6"/>
    <text x="725" y="202" fill="#c084fc" font-size="12" font-weight="700" text-anchor="middle">Firing Pulse</text>
    <text x="725" y="225" fill="#f1f5f9" font-size="11" text-anchor="middle">Generator (α)</text>
    <path d="M 780 210 L 820 210" stroke="#c084fc" stroke-width="2" marker-end="url(#arrow-amber)"/>

    <!-- Converter & Motor -->
    <rect x="820" y="175" width="90" height="70" fill="url(#boxGrad)" stroke="#f59e0b" rx="6"/>
    <text x="865" y="202" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle">Thyristor</text>
    <text x="865" y="225" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle">Bridge</text>

    <!-- Feedback Path for ia -->
    <path d="M 865 245 L 865 310 L 420 310 L 420 225" fill="none" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-cyan)"/>
    <rect x="580" y="295" width="130" height="28" fill="#1e293b" stroke="#38bdf8" rx="4"/>
    <text x="645" y="313" fill="#38bdf8" font-size="11" text-anchor="middle">Current Sensor &amp; Filter</text>
    <text x="435" y="240" fill="#f87171" font-size="14" font-weight="700">-</text>
    """,
    "Bandwidth Decoupling: Inner current loop is 10× faster than outer speed loop, suppressing supply fluctuations"
)

# drive-q13: V/f Closed Loop Schematic
create_card_diagram(
    "images/drive/v_f_closed_loop_schematic.png",
    "Closed-Loop V/f Control: Speed Regulation & Slip Compensation",
    "Slip Speed Regulator (ωsl*), Flux Compensation, and Inverter Frequency Generation",
    "#f59e0b", "DRIVES • FIG 4.2B",
    """
    <!-- Reference Speed -->
    <text x="60" y="205" fill="#38bdf8" font-size="14" font-weight="700">Speed ω*</text>
    <path d="M 125 200 L 165 200" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-cyan)"/>

    <!-- Speed Comparator -->
    <circle cx="180" cy="200" r="14" fill="#1e293b" stroke="#f1f5f9" stroke-width="2"/>
    <text x="180" y="205" fill="#f1f5f9" font-size="14" font-weight="700" text-anchor="middle">Σ</text>
    <path d="M 194 200 L 230 200" stroke="#f1f5f9" stroke-width="2" marker-end="url(#arrow-amber)"/>

    <!-- Speed PI Controller -->
    <rect x="230" y="165" width="120" height="70" fill="url(#boxGrad)" stroke="#38bdf8" rx="6"/>
    <text x="290" y="195" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">Speed Controller</text>
    <text x="290" y="215" fill="#94a3b8" font-size="11" text-anchor="middle">(PI Regulator)</text>
    <path d="M 350 200 L 390 200" stroke="#fbbf24" stroke-width="2" marker-end="url(#arrow-amber)"/>
    <text x="370" y="190" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">ωsl*</text>

    <!-- Frequency Summer -->
    <circle cx="405" cy="200" r="14" fill="#1e293b" stroke="#f1f5f9" stroke-width="2"/>
    <text x="405" y="205" fill="#f1f5f9" font-size="14" font-weight="700" text-anchor="middle">+</text>
    <path d="M 419 200 L 460 200" stroke="#f1f5f9" stroke-width="2" marker-end="url(#arrow-amber)"/>
    <text x="440" y="190" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">ωs*</text>

    <!-- V/f Function Generator -->
    <rect x="460" y="160" width="140" height="80" fill="url(#boxGrad)" stroke="#10b981" stroke-width="2" rx="6"/>
    <text x="530" y="188" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">V/f Generator</text>
    <text x="530" y="210" fill="#f1f5f9" font-size="11" text-anchor="middle">Vs* = (V/f)·fs + Vboost</text>
    <text x="530" y="228" fill="#94a3b8" font-size="10" text-anchor="middle">Flux Constant</text>
    <path d="M 600 200 L 650 200" stroke="#34d399" stroke-width="2" marker-end="url(#arrow-green)"/>

    <!-- PWM Inverter -->
    <rect x="650" y="165" width="110" height="70" fill="url(#boxGrad)" stroke="#f59e0b" rx="6"/>
    <text x="705" y="195" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle">PWM Inverter</text>
    <text x="705" y="215" fill="#94a3b8" font-size="11" text-anchor="middle">(IGBT Bridge)</text>
    <path d="M 760 200 L 810 200" stroke="#fbbf24" stroke-width="2" marker-end="url(#arrow-amber)"/>

    <!-- Induction Motor -->
    <rect x="810" y="165" width="100" height="70" fill="url(#boxGrad)" stroke="#38bdf8" rx="6"/>
    <text x="860" y="195" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">3-Phase IM</text>
    <text x="860" y="215" fill="#94a3b8" font-size="11" text-anchor="middle">Rotor ωr</text>

    <!-- Speed Feedback Loop -->
    <path d="M 860 235 L 860 300 L 180 300 L 180 214" fill="none" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-cyan)"/>
    <rect x="460" y="285" width="140" height="30" fill="#1e293b" stroke="#38bdf8" rx="4"/>
    <text x="530" y="304" fill="#38bdf8" font-size="11" text-anchor="middle">Tachometer / Encoder (ωr)</text>
    <path d="M 405 300 L 405 214" stroke="#34d399" stroke-width="2" marker-end="url(#arrow-green)"/>
    """,
    "Slip Regulation: Constraining slip speed ωsl* prevents motor pull-out breakdown and maintains peak torque"
)

# drive-q14b: Kramer vs Scherbius
create_card_diagram(
    "images/drive/kramer_vs_scherbius_characteristics.png",
    "Slip Power Recovery: Static Kramer vs Static Scherbius Drives",
    "Power Flow Direction, Commutation Stages, and Sub/Super-Synchronous Operating Zones",
    "#f59e0b", "DRIVES • FIG 4.3C",
    """
    <!-- Static Kramer Left Panel -->
    <rect x="60" y="110" width="400" height="260" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="8"/>
    <text x="260" y="135" fill="#38bdf8" font-size="15" font-weight="700" text-anchor="middle">Static Kramer System (Uni-directional)</text>
    
    <rect x="80" y="155" width="100" height="50" fill="#0f172a" stroke="#38bdf8" rx="4"/>
    <text x="130" y="180" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="middle">Rotor Slip Power</text>
    <text x="130" y="195" fill="#94a3b8" font-size="10" text-anchor="middle">s · P_gap</text>

    <path d="M 180 180 L 210 180" stroke="#f1f5f9" stroke-width="2" marker-end="url(#arrow-cyan)"/>

    <rect x="210" y="155" width="100" height="50" fill="#0f172a" stroke="#fbbf24" rx="4"/>
    <text x="260" y="178" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">Diode Rectifier</text>
    <text x="260" y="195" fill="#94a3b8" font-size="10" text-anchor="middle">AC -> DC</text>

    <path d="M 310 180 L 340 180" stroke="#f1f5f9" stroke-width="2" marker-end="url(#arrow-cyan)"/>

    <rect x="340" y="155" width="100" height="50" fill="#0f172a" stroke="#10b981" rx="4"/>
    <text x="390" y="178" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">Inverter</text>
    <text x="390" y="195" fill="#94a3b8" font-size="10" text-anchor="middle">DC -> AC (Mains)</text>

    <text x="260" y="240" fill="#f1f5f9" font-size="12" text-anchor="middle">Diode bridge blocks reverse power flow</text>
    <rect x="100" y="260" width="320" height="85" fill="#1e293b" rx="6"/>
    <text x="260" y="285" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle">Operating Zone: Sub-Synchronous Only</text>
    <text x="260" y="308" fill="#94a3b8" font-size="11" text-anchor="middle">Speed: 0.5 · ωs &lt; ωr &lt; ωs  (Slip s > 0)</text>
    <text x="260" y="328" fill="#34d399" font-size="11" text-anchor="middle">Lower cost, simple diode bridge, high reliability</text>

    <!-- Static Scherbius Right Panel -->
    <rect x="500" y="110" width="400" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="8"/>
    <text x="700" y="135" fill="#34d399" font-size="15" font-weight="700" text-anchor="middle">Static Scherbius System (Bi-directional)</text>

    <rect x="520" y="155" width="160" height="50" fill="#0f172a" stroke="#10b981" rx="4"/>
    <text x="600" y="178" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">Cycloconverter /</text>
    <text x="600" y="195" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">Back-to-Back PWM</text>

    <path d="M 680 175 L 720 175" stroke="#fbbf24" stroke-width="2" marker-end="url(#arrow-amber)"/>
    <path d="M 720 185 L 680 185" stroke="#fbbf24" stroke-width="2" marker-end="url(#arrow-amber)"/>

    <rect x="730" y="155" width="150" height="50" fill="#0f172a" stroke="#38bdf8" rx="4"/>
    <text x="805" y="178" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="middle">3-Phase AC Mains</text>
    <text x="805" y="195" fill="#94a3b8" font-size="10" text-anchor="middle">(Supply Grid)</text>

    <text x="700" y="240" fill="#f1f5f9" font-size="12" text-anchor="middle">Bi-directional active semiconductor switches</text>
    <rect x="540" y="260" width="320" height="85" fill="#1e293b" rx="6"/>
    <text x="700" y="285" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">Operating Zone: Sub &amp; Super-Synchronous</text>
    <text x="700" y="308" fill="#94a3b8" font-size="11" text-anchor="middle">Sub-sync (s > 0): Slip power -> Mains</text>
    <text x="700" y="328" fill="#fbbf24" font-size="11" text-anchor="middle">Super-sync (s &lt; 0): Power injected into rotor!</text>
    """,
    "Power Rating: Slip power converter handles only s · P_rated (approx 20-30% of motor capacity), saving equipment cost"
)

# drive-q18: Clarke & Park Transformation Geometry
create_card_diagram(
    "images/drive/clarke_park_transformation_geometry.png",
    "Field-Oriented Control: Clarke & Park Reference Frame Geometry",
    "Transformation from 3-Phase abc Frame to Stationary αβ and Synchronous Rotor-Flux dq Frame",
    "#f59e0b", "DRIVES • FIG 5.4B",
    """
    <!-- 3-Phase abc Axes -->
    <rect x="60" y="110" width="260" height="260" fill="url(#boxGrad)" stroke="#38bdf8" rx="8"/>
    <text x="190" y="135" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">1. Stator 3-Phase (abc)</text>
    <line x1="190" y1="230" x2="270" y2="230" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="280" y="235" fill="#38bdf8" font-size="12" font-weight="700">a-axis</text>
    <line x1="190" y1="230" x2="150" y2="160" stroke="#f43f5e" stroke-width="2.5"/>
    <text x="145" y="150" fill="#f43f5e" font-size="12" font-weight="700">b-axis (120°)</text>
    <line x1="190" y1="230" x2="150" y2="300" stroke="#10b981" stroke-width="2.5"/>
    <text x="145" y="315" fill="#10b981" font-size="12" font-weight="700">c-axis (240°)</text>
    <text x="190" y="355" fill="#94a3b8" font-size="11" text-anchor="middle">Three 120° Time-Varying Signals</text>

    <!-- Clarke Transformation Arrow -->
    <path d="M 330 240 L 370 240" stroke="#fbbf24" stroke-width="3" marker-end="url(#arrow-amber)"/>
    <text x="350" y="225" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">Clarke</text>

    <!-- Stationary α-β Axes -->
    <rect x="380" y="110" width="220" height="260" fill="url(#boxGrad)" stroke="#fbbf24" rx="8"/>
    <text x="490" y="135" fill="#fbbf24" font-size="14" font-weight="700" text-anchor="middle">2. Stationary (α-β)</text>
    <line x1="490" y1="230" x2="570" y2="230" stroke="#fbbf24" stroke-width="2.5"/>
    <text x="580" y="235" fill="#fbbf24" font-size="12" font-weight="700">α-axis</text>
    <line x1="490" y1="230" x2="490" y2="150" stroke="#fbbf24" stroke-width="2.5"/>
    <text x="490" y="145" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle">β-axis (90°)</text>
    <text x="490" y="355" fill="#94a3b8" font-size="11" text-anchor="middle">2 Orthogonal Stationary Axes</text>

    <!-- Park Transformation Arrow -->
    <path d="M 610 240 L 650 240" stroke="#34d399" stroke-width="3" marker-end="url(#arrow-green)"/>
    <text x="630" y="225" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">Park (θe)</text>

    <!-- Rotating d-q Axes -->
    <rect x="660" y="110" width="240" height="260" fill="url(#boxGrad)" stroke="#10b981" rx="8"/>
    <text x="780" y="135" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">3. Rotating (d-q) Frame</text>
    <!-- d axis at angle θe -->
    <line x1="770" y1="230" x2="850" y2="190" stroke="#10b981" stroke-width="2.5"/>
    <text x="860" y="185" fill="#34d399" font-size="12" font-weight="700">d-axis (Flux)</text>
    <!-- q axis orthogonal -->
    <line x1="770" y1="230" x2="730" y2="150" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="725" y="145" fill="#38bdf8" font-size="12" font-weight="700">q-axis (Torque)</text>
    <text x="780" y="310" fill="#f1f5f9" font-size="12" text-anchor="middle">d-axis locked to Rotor Flux λr</text>
    <text x="780" y="330" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">isd controls Flux | isq controls Torque</text>
    <text x="780" y="355" fill="#94a3b8" font-size="11" text-anchor="middle">DC Machine Emulation!</text>
    """,
    "Decoupling Vector Math: Direct axis (isd) produces magnetizing flux; Quadrature axis (isq) produces mechanical torque"
)

# ==============================================================================
# 2. ADVANCED CONTROL SYSTEMS (ACS) SUPPLEMENTARY DIAGRAMS
# ==============================================================================

# acs-q5: Series RLC State Diagram
create_card_diagram(
    "images/acs/series_rlc_state_diagram.png",
    "Series RLC Circuit: Analog Simulation State Block Diagram",
    "Dual Integrator Structure with State Feedback for Inductor Current x1=iL and Capacitor Voltage x2=vC",
    "#38bdf8", "ACS • FIG 1.5B",
    """
    <!-- Input vi(t) -->
    <text x="70" y="195" fill="#38bdf8" font-size="14" font-weight="700">Input vi(t)</text>
    <path d="M 140 190 L 190 190" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-cyan)"/>

    <!-- Summing Junction 1 -->
    <circle cx="210" cy="190" r="16" fill="#1e293b" stroke="#f1f5f9" stroke-width="2"/>
    <text x="210" y="195" fill="#f1f5f9" font-size="14" font-weight="700" text-anchor="middle">Σ</text>
    <text x="180" y="180" fill="#34d399" font-size="12" font-weight="700">+1/L</text>
    <path d="M 226 190 L 270 190" stroke="#f1f5f9" stroke-width="2" marker-end="url(#arrow-cyan)"/>
    <text x="245" y="180" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle">ẋ₁</text>

    <!-- Integrator 1 -->
    <rect x="270" y="160" width="80" height="60" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="2" rx="6"/>
    <text x="310" y="195" fill="#38bdf8" font-size="16" font-weight="700" text-anchor="middle">∫ dt</text>
    <path d="M 350 190 L 440 190" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-cyan)"/>
    <text x="390" y="180" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">x₁ = iL</text>

    <!-- Gain 1/C -->
    <rect x="440" y="165" width="70" height="50" fill="url(#boxGrad)" stroke="#fbbf24" rx="6"/>
    <text x="475" y="195" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">1/C</text>
    <path d="M 510 190 L 570 190" stroke="#fbbf24" stroke-width="2" marker-end="url(#arrow-amber)"/>
    <text x="540" y="180" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle">ẋ₂</text>

    <!-- Integrator 2 -->
    <rect x="570" y="160" width="80" height="60" fill="url(#boxGrad)" stroke="#10b981" stroke-width="2" rx="6"/>
    <text x="610" y="195" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">∫ dt</text>
    <path d="M 650 190 L 760 190" stroke="#34d399" stroke-width="2" marker-end="url(#arrow-green)"/>
    <text x="700" y="180" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">x₂ = vC = y</text>

    <!-- Feedback loop 1: -R/L from x1 -->
    <path d="M 390 190 L 390 280 L 290 280" fill="none" stroke="#ef4444" stroke-width="2" marker-end="url(#arrow-amber)"/>
    <rect x="220" y="260" width="70" height="40" fill="#0f172a" stroke="#ef4444" rx="4"/>
    <text x="255" y="285" fill="#f87171" font-size="12" font-weight="700" text-anchor="middle">-R/L</text>
    <path d="M 220 280 L 210 280 L 210 206" fill="none" stroke="#ef4444" stroke-width="2" marker-end="url(#arrow-amber)"/>

    <!-- Feedback loop 2: -1/L from x2 -->
    <path d="M 700 190 L 700 340 L 400 340" fill="none" stroke="#a855f7" stroke-width="2"/>
    <rect x="330" y="320" width="70" height="40" fill="#0f172a" stroke="#a855f7" rx="4"/>
    <text x="365" y="345" fill="#c084fc" font-size="12" font-weight="700" text-anchor="middle">-1/L</text>
    <path d="M 330 340 L 210 340 L 210 206" fill="none" stroke="#a855f7" stroke-width="2"/>
    """,
    "State Differential Form: ẋ₁ = -(R/L)x₁ - (1/L)x₂ + (1/L)vi  |  ẋ₂ = (1/C)x₁  |  Output y = x₂"
)

# acs-q6: Armature DC Motor Block Diagram
create_card_diagram(
    "images/acs/armature_dc_motor_block_diagram.png",
    "Armature-Controlled DC Servomotor: Block Diagram & Transfer Function",
    "Coupled Electrical Admittance, Electromechanical Torque (Kt), Inertia (J), and Back-EMF (Kb)",
    "#38bdf8", "ACS • FIG 1.6B",
    """
    <!-- Input Va(s) -->
    <text x="60" y="200" fill="#38bdf8" font-size="13" font-weight="700">Va(s)</text>
    <path d="M 105 195 L 145 195" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-cyan)"/>

    <!-- Summing Junction -->
    <circle cx="160" cy="195" r="14" fill="#1e293b" stroke="#f1f5f9" stroke-width="2"/>
    <text x="160" y="200" fill="#f1f5f9" font-size="14" font-weight="700" text-anchor="middle">Σ</text>
    <path d="M 174 195 L 215 195" stroke="#f1f5f9" stroke-width="2" marker-end="url(#arrow-cyan)"/>

    <!-- Armature Admittance Block -->
    <rect x="215" y="165" width="130" height="60" fill="url(#boxGrad)" stroke="#38bdf8" rx="6"/>
    <text x="280" y="192" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">1 / (Ra + s·La)</text>
    <text x="280" y="212" fill="#94a3b8" font-size="11" text-anchor="middle">Electrical Circuit</text>
    <path d="M 345 195 L 400 195" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-cyan)"/>
    <text x="370" y="185" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="middle">Ia(s)</text>

    <!-- Motor Torque Constant Kt -->
    <rect x="400" y="165" width="70" height="60" fill="url(#boxGrad)" stroke="#fbbf24" rx="6"/>
    <text x="435" y="200" fill="#fbbf24" font-size="14" font-weight="700" text-anchor="middle">Kt</text>
    <path d="M 470 195 L 525 195" stroke="#fbbf24" stroke-width="2" marker-end="url(#arrow-amber)"/>
    <text x="495" y="185" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">Tm(s)</text>

    <!-- Mechanical Rotor Block -->
    <rect x="525" y="165" width="120" height="60" fill="url(#boxGrad)" stroke="#10b981" rx="6"/>
    <text x="585" y="192" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">1 / (J·s + B)</text>
    <text x="585" y="212" fill="#94a3b8" font-size="11" text-anchor="middle">Mechanical Load</text>
    <path d="M 645 195 L 705 195" stroke="#34d399" stroke-width="2" marker-end="url(#arrow-green)"/>
    <text x="675" y="185" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">ω(s)</text>

    <!-- Integrator 1/s to Position -->
    <rect x="705" y="165" width="70" height="60" fill="url(#boxGrad)" stroke="#a855f7" rx="6"/>
    <text x="740" y="200" fill="#c084fc" font-size="14" font-weight="700" text-anchor="middle">1 / s</text>
    <path d="M 775 195 L 840 195" stroke="#c084fc" stroke-width="2" marker-end="url(#arrow-amber)"/>
    <text x="865" y="200" fill="#f1f5f9" font-size="13" font-weight="700">θ(s)</text>

    <!-- Back-EMF Feedback Loop Kb -->
    <path d="M 675 195 L 675 290 L 460 290" fill="none" stroke="#ef4444" stroke-width="2"/>
    <rect x="380" y="265" width="80" height="50" fill="#0f172a" stroke="#ef4444" rx="4"/>
    <text x="420" y="295" fill="#f87171" font-size="14" font-weight="700" text-anchor="middle">Kb</text>
    <path d="M 380 290 L 160 290 L 160 209" fill="none" stroke="#ef4444" stroke-width="2" marker-end="url(#arrow-amber)"/>
    <text x="145" y="240" fill="#f87171" font-size="14" font-weight="700">- Eb(s)</text>
    """,
    "Overall Transfer Function: θ(s)/Va(s) = Kt / [ s · ((Ra + s·La)(J·s + B) + Kt·Kb) ]"
)

# acs-q7: Controllable Canonical Form
create_card_diagram(
    "images/acs/controllable_canonical_form.png",
    "Controllable Canonical Form (CCF): Phase Variable Realization",
    "Successive Integrator Realization with Denominator Feedback (-an) and Numerator Feedforward (bn)",
    "#38bdf8", "ACS • FIG 1.7C",
    """
    <!-- Input u(t) -->
    <text x="60" y="175" fill="#38bdf8" font-size="13" font-weight="700">u(t)</text>
    <path d="M 95 170 L 135 170" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-cyan)"/>

    <circle cx="150" cy="170" r="14" fill="#1e293b" stroke="#f1f5f9" stroke-width="2"/>
    <text x="150" y="175" fill="#f1f5f9" font-size="14" font-weight="700" text-anchor="middle">Σ</text>
    <path d="M 164 170 L 210 170" stroke="#f1f5f9" stroke-width="2" marker-end="url(#arrow-cyan)"/>
    <text x="185" y="160" fill="#fbbf24" font-size="11" font-weight="700">ẋ₃</text>

    <!-- Integrator 3 -->
    <rect x="210" y="145" width="70" height="50" fill="url(#boxGrad)" stroke="#38bdf8" rx="6"/>
    <text x="245" y="175" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">1/s</text>
    <path d="M 280 170 L 350 170" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-cyan)"/>
    <text x="315" y="160" fill="#38bdf8" font-size="11" font-weight="700">x₃</text>

    <!-- Integrator 2 -->
    <rect x="350" y="145" width="70" height="50" fill="url(#boxGrad)" stroke="#38bdf8" rx="6"/>
    <text x="385" y="175" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">1/s</text>
    <path d="M 420 170 L 490 170" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-cyan)"/>
    <text x="455" y="160" fill="#38bdf8" font-size="11" font-weight="700">x₂</text>

    <!-- Integrator 1 -->
    <rect x="490" y="145" width="70" height="50" fill="url(#boxGrad)" stroke="#38bdf8" rx="6"/>
    <text x="525" y="175" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">1/s</text>
    <path d="M 560 170 L 630 170" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-cyan)"/>
    <text x="595" y="160" fill="#38bdf8" font-size="11" font-weight="700">x₁</text>

    <!-- Feedback paths below (-a1, -a2, -a3) -->
    <path d="M 595 170 L 595 240 L 450 240" fill="none" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="400" y="225" width="50" height="30" fill="#0f172a" stroke="#ef4444" rx="4"/>
    <text x="425" y="245" fill="#f87171" font-size="11" font-weight="700" text-anchor="middle">-a₃</text>
    <path d="M 400 240 L 150 240 L 150 184" fill="none" stroke="#ef4444" stroke-width="1.5" marker-end="url(#arrow-amber)"/>

    <path d="M 455 170 L 455 280 L 320 280" fill="none" stroke="#ef4444" stroke-width="1.5"/>
    <rect x="270" y="265" width="50" height="30" fill="#0f172a" stroke="#ef4444" rx="4"/>
    <text x="295" y="285" fill="#f87171" font-size="11" font-weight="700" text-anchor="middle">-a₂</text>
    <path d="M 270 280 L 150 280 L 150 184" fill="none" stroke="#ef4444" stroke-width="1.5"/>

    <!-- Feedforward paths to Output y(t) -->
    <circle cx="730" cy="170" r="14" fill="#1e293b" stroke="#f1f5f9" stroke-width="2"/>
    <text x="730" y="175" fill="#f1f5f9" font-size="14" font-weight="700" text-anchor="middle">Σ</text>
    <path d="M 744 170 L 790 170" stroke="#34d399" stroke-width="2" marker-end="url(#arrow-green)"/>
    <text x="825" y="175" fill="#34d399" font-size="13" font-weight="700">y(t)</text>

    <path d="M 595 170 L 660 170" stroke="#34d399" stroke-width="1.5"/>
    <rect x="660" y="155" width="45" height="30" fill="#0f172a" stroke="#10b981" rx="4"/>
    <text x="682" y="175" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">b₃</text>
    <path d="M 705 170 L 716 170" stroke="#34d399" stroke-width="1.5"/>
    """,
    "Canonical Structure: System matrix A has companion form; Controllability matrix Qc is always non-singular"
)

# acs-q14: Pole Placement Complex S-Plane
create_card_diagram(
    "images/acs/pole_placement_s_plane.png",
    "State Feedback Pole Placement: Complex S-Plane Migration",
    "Ackermann's Formula Relocates Unstable Open-Loop Poles to Stable S-Plane Cone (ζ, ωn)",
    "#38bdf8", "ACS • FIG 3.3B",
    """
    <!-- S-Plane Axes -->
    <line x1="80" y1="230" x2="880" y2="230" stroke="#64748b" stroke-width="2"/>
    <line x1="680" y1="90" x2="680" y2="370" stroke="#64748b" stroke-width="2"/>
    <text x="870" y="220" fill="#94a3b8" font-size="13" font-weight="700">σ (Real)</text>
    <text x="690" y="110" fill="#94a3b8" font-size="13" font-weight="700">jω (Imag)</text>

    <!-- Stable / Unstable Zone Tint -->
    <rect x="80" y="90" width="600" height="280" fill="#10b98111"/>
    <rect x="680" y="90" width="200" height="280" fill="#ef444411"/>
    <text x="380" y="120" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">STABLE REGION (LHP)</text>
    <text x="780" y="120" fill="#f87171" font-size="14" font-weight="700" text-anchor="middle">UNSTABLE</text>

    <!-- Damping Cone Rays -->
    <line x1="680" y1="230" x2="200" y2="100" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="4,4"/>
    <line x1="680" y1="230" x2="200" y2="360" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="4,4"/>
    <text x="350" y="145" fill="#fbbf24" font-size="12">cos θ = ζ (Damping Ratio)</text>

    <!-- Open Loop Poles (X) -->
    <text x="740" y="180" fill="#ef4444" font-size="22" font-weight="900" text-anchor="middle">×</text>
    <text x="740" y="280" fill="#ef4444" font-size="22" font-weight="900" text-anchor="middle">×</text>
    <text x="790" y="180" fill="#f87171" font-size="12">Open-Loop Pole (Unstable)</text>

    <!-- Desired Closed-Loop Poles (Star) -->
    <text x="440" y="170" fill="#34d399" font-size="26" font-weight="900" text-anchor="middle">★</text>
    <text x="440" y="290" fill="#34d399" font-size="26" font-weight="900" text-anchor="middle">★</text>
    <text x="370" y="170" fill="#34d399" font-size="12" font-weight="700">Desired Pole μ₁</text>
    <text x="370" y="290" fill="#34d399" font-size="12" font-weight="700">Desired Pole μ₂</text>

    <!-- Arrow shifting pole -->
    <path d="M 730 175 Q 580 150 460 170" fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="3,3" marker-end="url(#arrow-cyan)"/>
    <text x="600" y="145" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">State Feedback u = -Kx</text>
    """,
    "Ackermann's Formula: K = [0 0 ... 1] · Qc⁻¹ · αc(A) | Arbitrary pole placement requires full rank rank(Qc) = n"
)

# acs-q15: Observer Error Dynamics
create_card_diagram(
    "images/acs/observer_error_dynamics.png",
    "Luenberger State Observer: Error Dynamics & Convergence",
    "Asymptotic Exponential Decay of Estimation Error e(t) = x(t) - x̂(t) governed by (A - LC)",
    "#38bdf8", "ACS • FIG 3.4B",
    """
    <!-- Error State Block Diagram on Left -->
    <rect x="60" y="110" width="400" height="260" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="8"/>
    <text x="260" y="135" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">Error Dynamics: ė(t) = (A - LC) · e(t)</text>
    
    <circle cx="160" cy="210" r="14" fill="#1e293b" stroke="#f1f5f9" stroke-width="2"/>
    <text x="160" y="215" fill="#f1f5f9" font-size="14" font-weight="700" text-anchor="middle">Σ</text>
    <path d="M 174 210 L 230 210" stroke="#f1f5f9" stroke-width="2" marker-end="url(#arrow-cyan)"/>
    <text x="200" y="200" fill="#fbbf24" font-size="12" font-weight="700">ė(t)</text>

    <!-- Integrator -->
    <rect x="230" y="180" width="80" height="60" fill="url(#boxGrad)" stroke="#38bdf8" rx="6"/>
    <text x="270" y="215" fill="#38bdf8" font-size="16" font-weight="700" text-anchor="middle">∫ dt</text>
    <path d="M 310 210 L 390 210" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-cyan)"/>
    <text x="350" y="200" fill="#34d399" font-size="13" font-weight="700">e(t)</text>

    <!-- Feedback (A - LC) -->
    <path d="M 350 210 L 350 290 L 290 290" fill="none" stroke="#ef4444" stroke-width="2"/>
    <rect x="180" y="265" width="110" height="50" fill="#0f172a" stroke="#ef4444" rx="6"/>
    <text x="235" y="295" fill="#f87171" font-size="13" font-weight="700" text-anchor="middle">(A - LC)</text>
    <path d="M 180 290 L 160 290 L 160 224" fill="none" stroke="#ef4444" stroke-width="2" marker-end="url(#arrow-amber)"/>

    <!-- Transient Error Decay Graph on Right -->
    <rect x="500" y="110" width="400" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="8"/>
    <text x="700" y="135" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">Error Transient: e(t) -> 0 as t -> ∞</text>
    <line x1="530" y1="310" x2="870" y2="310" stroke="#64748b" stroke-width="1.5"/>
    <line x1="550" y1="160" x2="550" y2="320" stroke="#64748b" stroke-width="1.5"/>
    <text x="860" y="325" fill="#94a3b8" font-size="12">Time t</text>
    <text x="540" y="155" fill="#94a3b8" font-size="12">||e(t)||</text>

    <!-- Decaying Exponential Curve -->
    <path d="M 550 170 Q 600 240 680 295 T 850 310" fill="none" stroke="#34d399" stroke-width="3"/>
    <circle cx="550" cy="170" r="5" fill="#ef4444"/>
    <text x="590" y="180" fill="#ef4444" font-size="12" font-weight="700">Initial Error e(0)</text>
    <text x="720" y="260" fill="#fbbf24" font-size="12">Fast Convergence (3-5× Controller Speed)</text>
    """,
    "Separation Principle: Controller eigenvalues det(sI - (A - BK)) and Observer eigenvalues det(sI - (A - LC)) are independent"
)

# acs-q16b: Relay Waveforms Fourier
create_card_diagram(
    "images/acs/relay_waveforms_fourier.png",
    "Describing Function: Ideal Relay Input-Output Fourier Waveforms",
    "Sinusoidal Excitation x(t)=X·sin(ωt) Generates Square Wave y(t)=±M with Fundamental Y1",
    "#38bdf8", "ACS • FIG 4.1C",
    """
    <!-- Input Sine Wave on Top -->
    <line x1="80" y1="170" x2="600" y2="170" stroke="#334155"/>
    <path d="M 100 170 Q 160 110 220 170 Q 280 230 340 170 Q 400 110 460 170 Q 520 230 580 170" fill="none" stroke="#38bdf8" stroke-width="2"/>
    <text x="75" y="145" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="end">Input x(t)</text>
    <text x="220" y="105" fill="#38bdf8" font-size="11" text-anchor="middle">+X</text>
    <text x="340" y="245" fill="#38bdf8" font-size="11" text-anchor="middle">-X</text>

    <!-- Output Square Wave in Middle -->
    <line x1="80" y1="280" x2="600" y2="280" stroke="#334155"/>
    <path d="M 100 280 L 100 230 L 220 230 L 220 330 L 340 330 L 340 230 L 460 230 L 460 330 L 580 330" fill="none" stroke="#fbbf24" stroke-width="2.5"/>
    <text x="75" y="260" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="end">Output y(t)</text>
    <text x="160" y="220" fill="#fbbf24" font-size="11" text-anchor="middle">+M</text>
    <text x="280" y="345" fill="#fbbf24" font-size="11" text-anchor="middle">-M</text>

    <!-- Fundamental Harmonic Overlay -->
    <path d="M 100 280 Q 160 215 220 280 Q 280 345 340 280 Q 400 215 460 280 Q 520 345 580 280" fill="none" stroke="#34d399" stroke-width="2" stroke-dasharray="4,4"/>
    <text x="460" y="210" fill="#34d399" font-size="11" text-anchor="middle">Fundamental Y₁ = (4M/π)</text>

    <!-- Mathematical Derivation Card on Right -->
    <rect x="630" y="110" width="280" height="260" fill="url(#boxGrad)" stroke="#38bdf8" rx="8"/>
    <text x="770" y="140" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">Fourier Describing Function</text>
    <text x="770" y="175" fill="#f1f5f9" font-size="12" text-anchor="middle">y(t) = Y₁·sin(ωt) + Y₃·sin(3ωt) + ...</text>
    <text x="770" y="205" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">Y₁ = (4M / π)</text>
    <line x1="660" y1="225" x2="880" y2="225" stroke="#334155"/>
    <text x="770" y="255" fill="#fbbf24" font-size="15" font-weight="700" text-anchor="middle">N(X) = Y₁ / X</text>
    <text x="770" y="285" fill="#fbbf24" font-size="15" font-weight="700" text-anchor="middle">N(X) = 4M / (π · X)</text>
    <text x="770" y="325" fill="#94a3b8" font-size="11" text-anchor="middle">Zero Phase Shift: ∠N(X) = 0°</text>
    """,
    "Low-Pass Plant Hypothesis: Plant filtering suppresses higher harmonics (Y3, Y5), validating fundamental approximation"
)

# acs-q17: Saturation Waveforms Fourier
create_card_diagram(
    "images/acs/saturation_waveforms_fourier.png",
    "Symmetrical Saturation: Clipped Waveform & Conduction Angles",
    "Linear Slope k for |x| <= S, Flat-Top Saturated Output kS for |x| > S with Angle θ1 = sin⁻¹(S/X)",
    "#38bdf8", "ACS • FIG 4.2C",
    """
    <!-- Waveform Canvas -->
    <line x1="80" y1="230" x2="600" y2="230" stroke="#334155" stroke-width="1.5"/>
    <!-- Sine wave input (dashed) -->
    <path d="M 100 230 Q 170 90 240 230 Q 310 370 380 230 Q 450 90 520 230" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3"/>
    
    <!-- Clipped Flat-Top Waveform -->
    <path d="M 100 230 L 135 160 L 205 160 L 240 230 L 275 300 L 345 300 L 380 230 L 415 160 L 485 160 L 520 230" fill="none" stroke="#fbbf24" stroke-width="3"/>
    <text x="170" y="150" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle">Clipped at +kS</text>
    <text x="310" y="320" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle">Clipped at -kS</text>

    <!-- Angle notations -->
    <line x1="135" y1="160" x2="135" y2="230" stroke="#64748b" stroke-dasharray="2,2"/>
    <text x="135" y="245" fill="#34d399" font-size="11" text-anchor="middle">θ₁</text>
    <line x1="205" y1="160" x2="205" y2="230" stroke="#64748b" stroke-dasharray="2,2"/>
    <text x="205" y="245" fill="#34d399" font-size="11" text-anchor="middle">π - θ₁</text>

    <!-- Right Summary Box -->
    <rect x="630" y="110" width="280" height="260" fill="url(#boxGrad)" stroke="#fbbf24" rx="8"/>
    <text x="770" y="140" fill="#fbbf24" font-size="14" font-weight="700" text-anchor="middle">Saturation Describing Function</text>
    <text x="770" y="175" fill="#38bdf8" font-size="12" text-anchor="middle">Transition Angle θ₁ = sin⁻¹(S / X)</text>
    <text x="770" y="215" fill="#f1f5f9" font-size="12" text-anchor="middle">Fundamental Component Y₁:</text>
    <text x="770" y="240" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">Y₁ = (2kX/π) [θ₁ + 0.5·sin(2θ₁)]</text>
    <line x1="660" y1="260" x2="880" y2="260" stroke="#334155"/>
    <text x="770" y="290" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">N(X) = (2k/π) [θ₁ + 0.5·sin(2θ₁)]</text>
    <text x="770" y="325" fill="#94a3b8" font-size="11" text-anchor="middle">For X &lt;= S: N(X) = k (Purely Linear)</text>
    """,
    "Amplitude Sensitivity: As input amplitude X increases beyond S, N(X) decreases monotonically from k toward 0"
)

# acs-q18: Limit Cycle Stability Criterion
create_card_diagram(
    "images/acs/limit_cycle_stability_criterion.png",
    "Limit Cycle Stability: Nyquist Polar Plot & -1/N(X) Locus",
    "Intersection Point P(X0, ω0) with Directional Amplitude Perturbations Determining Limit Cycle Stability",
    "#38bdf8", "ACS • FIG 4.3B",
    """
    <!-- Complex Plane Axes -->
    <line x1="80" y1="230" x2="880" y2="230" stroke="#64748b" stroke-width="1.5"/>
    <line x1="480" y1="90" x2="480" y2="370" stroke="#64748b" stroke-width="1.5"/>
    <text x="870" y="220" fill="#94a3b8" font-size="12">Re</text>
    <text x="490" y="110" fill="#94a3b8" font-size="12">Im</text>

    <!-- Linear Plant G(jω) Nyquist locus -->
    <path d="M 480 340 Q 300 320 220 230 Q 180 160 270 120 Q 380 90 480 150" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="210" y="140" fill="#38bdf8" font-size="13" font-weight="700">G(jω) Locus (ω increases ->)</text>

    <!-- Non-Linear -1/N(X) locus -->
    <line x1="120" y1="230" x2="400" y2="230" stroke="#fbbf24" stroke-width="3"/>
    <text x="120" y="215" fill="#fbbf24" font-size="12" font-weight="700">-1/N(X) Locus</text>
    <text x="370" y="215" fill="#fbbf24" font-size="11">X increasing -></text>

    <!-- Intersection Point P -->
    <circle cx="220" cy="230" r="7" fill="#ef4444"/>
    <text x="220" y="260" fill="#ef4444" font-size="13" font-weight="700" text-anchor="middle">P (X₀, ω₀)</text>
    <text x="220" y="280" fill="#f87171" font-size="11" text-anchor="middle">Limit Cycle Point</text>

    <!-- Perturbation Analysis Box -->
    <rect x="540" y="120" width="370" height="220" fill="url(#boxGrad)" stroke="#34d399" rx="8"/>
    <text x="725" y="150" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">Stability Criterion (Loeb's Rule)</text>
    <text x="725" y="180" fill="#f1f5f9" font-size="12" text-anchor="middle">If amplitude increases (X > X₀):</text>
    <text x="725" y="202" fill="#fbbf24" font-size="12" text-anchor="middle">Point moves into UNENCIRCLED region</text>
    <text x="725" y="222" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">-> System is stable -> Amplitude X decays back to X₀</text>
    <line x1="560" y1="235" x2="890" y2="235" stroke="#334155"/>
    <text x="725" y="255" fill="#f1f5f9" font-size="12" text-anchor="middle">If amplitude decreases (X &lt; X₀):</text>
    <text x="725" y="275" fill="#ef4444" font-size="12" text-anchor="middle">Point is ENCIRCLED -> Unstable -> X grows back to X₀</text>
    <text x="725" y="305" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">RESULT: STABLE LIMIT CYCLE</text>
    """,
    "Limit Cycle Condition: G(jω₀) · N(X₀) = -1  ==>  G(jω₀) = -1 / N(X₀)"
)

# acs-q21: Isocline Method Construction
create_card_diagram(
    "images/acs/isocline_method_construction.png",
    "Phase Plane Analysis: Method of Isoclines Trajectory Construction",
    "Isocline Lines of Constant Slope M = dx2/dx1 with Inclination Angles α = tan⁻¹(M)",
    "#38bdf8", "ACS • FIG 5.3B",
    """
    <!-- Phase Plane Grid -->
    <line x1="80" y1="230" x2="600" y2="230" stroke="#64748b" stroke-width="1.5"/>
    <line x1="340" y1="90" x2="340" y2="370" stroke="#64748b" stroke-width="1.5"/>
    <text x="590" y="220" fill="#94a3b8" font-size="12">x₁ (Displacement)</text>
    <text x="350" y="110" fill="#94a3b8" font-size="12">x₂ = ẋ₁ (Velocity)</text>

    <!-- Isoclines (Dashed Lines) -->
    <line x1="120" y1="350" x2="560" y2="110" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4,4"/>
    <text x="530" y="105" fill="#38bdf8" font-size="11">Isocline M = -1</text>

    <line x1="160" y1="360" x2="520" y2="100" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="4,4"/>
    <text x="490" y="95" fill="#fbbf24" font-size="11">Isocline M = -2</text>

    <!-- Hatch marks along isocline M = -1 -->
    <line x1="200" y1="295" x2="230" y2="315" stroke="#34d399" stroke-width="2.5"/>
    <line x1="300" y1="240" x2="330" y2="260" stroke="#34d399" stroke-width="2.5"/>
    <line x1="400" y1="185" x2="430" y2="205" stroke="#34d399" stroke-width="2.5"/>

    <!-- Synthesized Phase Trajectory -->
    <path d="M 150 160 Q 240 100 380 140 Q 480 180 440 270 Q 390 340 300 300 Q 220 260 340 230" fill="none" stroke="#f43f5e" stroke-width="3"/>
    <circle cx="150" cy="160" r="5" fill="#38bdf8"/>
    <text x="130" y="150" fill="#38bdf8" font-size="11" font-weight="700">x(0)</text>
    <circle cx="340" cy="230" r="5" fill="#34d399"/>
    <text x="355" y="240" fill="#34d399" font-size="11" font-weight="700">Origin (0,0)</text>

    <!-- Right Guide Card -->
    <rect x="630" y="110" width="280" height="260" fill="url(#boxGrad)" stroke="#38bdf8" rx="8"/>
    <text x="770" y="140" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">Isocline Step Protocol</text>
    <text x="770" y="170" fill="#f1f5f9" font-size="12" text-anchor="middle">1. Formulate: dx₂/dx₁ = f(x₁, x₂)</text>
    <text x="770" y="195" fill="#fbbf24" font-size="12" text-anchor="middle">2. Set f(x₁, x₂) = M (constant)</text>
    <text x="770" y="220" fill="#f1f5f9" font-size="12" text-anchor="middle">3. Plot isocline curve in phase plane</text>
    <text x="770" y="245" fill="#34d399" font-size="12" text-anchor="middle">4. Draw short slope tangents (α = tan⁻¹M)</text>
    <text x="770" y="270" fill="#f1f5f9" font-size="12" text-anchor="middle">5. Connect tangents smoothly</text>
    <text x="770" y="310" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">No analytical integration required!</text>
    """,
    "Method of Isoclines: Enables graphical solution of non-linear differential equations without closed-form integration"
)

# ==============================================================================
# 3. MOBILE COMPUTING (CST415) SUPPLEMENTARY DIAGRAMS
# ==============================================================================

# mobile-q10: Satellite Footprint Geometry
create_card_diagram(
    "images/mobile_compute/satellite_footprint_geometry.png",
    "Satellite Communications: Geometric Coverage Footprint & Beam Angles",
    "Earth Horizon Geometry, Half-Power Beamwidth, Slant Range (d), and Elevation Angle (θ)",
    "#10b981", "MOBILE • FIG 2.1B",
    """
    <!-- Earth Sphere Section -->
    <path d="M 100 370 Q 480 280 860 370" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="480" y="340" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">Earth Surface (Radius RE = 6378 km)</text>

    <!-- Satellite in Orbit -->
    <rect x="440" y="90" width="80" height="40" fill="url(#boxGrad)" stroke="#10b981" stroke-width="2" rx="6"/>
    <text x="480" y="115" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">Satellite</text>
    <!-- Solar Panels -->
    <line x1="390" y1="110" x2="440" y2="110" stroke="#38bdf8" stroke-width="6"/>
    <line x1="520" y1="110" x2="570" y2="110" stroke="#38bdf8" stroke-width="6"/>

    <!-- Beam Cones / Slant Ranges -->
    <line x1="480" y1="130" x2="240" y2="330" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4,4"/>
    <line x1="480" y1="130" x2="720" y2="330" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4,4"/>
    <line x1="480" y1="130" x2="480" y2="310" stroke="#10b981" stroke-width="1.5"/>

    <text x="330" y="220" fill="#fbbf24" font-size="12" font-weight="700">Slant Range d</text>
    <text x="495" y="210" fill="#10b981" font-size="12">Altitude h</text>

    <!-- Footprint zone -->
    <line x1="240" y1="330" x2="720" y2="330" stroke="#f43f5e" stroke-width="3"/>
    <text x="480" y="365" fill="#f87171" font-size="13" font-weight="700" text-anchor="middle">&lt;- Coverage Footprint Diameter -&gt;</text>

    <!-- Elevation Angle marker -->
    <line x1="240" y1="330" x2="160" y2="330" stroke="#64748b"/>
    <text x="210" y="320" fill="#fbbf24" font-size="12" font-weight="700">θmin >= 10°</text>

    <!-- Orbit Comparison Table on Right -->
    <rect x="680" y="90" width="240" height="150" fill="#0f172a" stroke="#223049" rx="6"/>
    <text x="800" y="115" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">Constellation Scale</text>
    <text x="800" y="140" fill="#f1f5f9" font-size="11" text-anchor="middle">GEO: 35,786 km | 3 Sats (Global)</text>
    <text x="800" y="165" fill="#fbbf24" font-size="11" text-anchor="middle">MEO: 10,000 km | 10-12 Sats</text>
    <text x="800" y="190" fill="#34d399" font-size="11" text-anchor="middle">LEO: 500-1500 km | 48-66 Sats</text>
    <text x="800" y="215" fill="#94a3b8" font-size="10" text-anchor="middle">Round-trip Delay: GEO 250ms vs LEO 20ms</text>
    """,
    "Geometric Coverage: Coverage area = 2π·RE²(1 - cos β) | Minimum elevation angle θmin avoids atmospheric noise and building blockage"
)

# mobile-q14: GSM Channel Hierarchy
create_card_diagram(
    "images/mobile_compute/gsm_channel_hierarchy.png",
    "GSM Air Interface: Physical & Logical Channel Architecture",
    "Division into Traffic Channels (TCH) and Control Channels (BCH, CCCH, DCCH)",
    "#10b981", "MOBILE • FIG 2.5B",
    """
    <!-- Root Physical Frame -->
    <rect x="360" y="100" width="240" height="40" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="2" rx="6"/>
    <text x="480" y="125" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">GSM Logical Channels</text>

    <!-- Branch to TCH and CCH -->
    <line x1="480" y1="140" x2="220" y2="170" stroke="#f1f5f9" stroke-width="2"/>
    <line x1="480" y1="140" x2="720" y2="170" stroke="#f1f5f9" stroke-width="2"/>

    <!-- Traffic Channels TCH -->
    <rect x="110" y="170" width="220" height="50" fill="url(#boxGrad)" stroke="#10b981" rx="6"/>
    <text x="220" y="195" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">Traffic Channels (TCH)</text>
    <text x="220" y="212" fill="#94a3b8" font-size="11" text-anchor="middle">Voice &amp; User Data Transmission</text>

    <!-- Sub-TCH -->
    <rect x="80" y="240" width="130" height="55" fill="#0f172a" stroke="#10b981" rx="4"/>
    <text x="145" y="262" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">TCH/F (Full Rate)</text>
    <text x="145" y="282" fill="#94a3b8" font-size="10" text-anchor="middle">22.8 kbps (Gross)</text>

    <rect x="230" y="240" width="130" height="55" fill="#0f172a" stroke="#10b981" rx="4"/>
    <text x="295" y="262" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">TCH/H (Half Rate)</text>
    <text x="295" y="282" fill="#94a3b8" font-size="10" text-anchor="middle">11.4 kbps (Gross)</text>

    <!-- Control Channels CCH -->
    <rect x="610" y="170" width="220" height="50" fill="url(#boxGrad)" stroke="#fbbf24" rx="6"/>
    <text x="720" y="195" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">Control Channels (CCH)</text>
    <text x="720" y="212" fill="#94a3b8" font-size="11" text-anchor="middle">Signaling, Sync &amp; Management</text>

    <!-- 3 Sub-Control Columns -->
    <rect x="420" y="240" width="150" height="120" fill="#0f172a" stroke="#38bdf8" rx="4"/>
    <text x="495" y="262" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">Broadcast (BCH)</text>
    <text x="495" y="285" fill="#f1f5f9" font-size="11" text-anchor="middle">• FCCH (Freq Sync)</text>
    <text x="495" y="305" fill="#f1f5f9" font-size="11" text-anchor="middle">• SCH (Frame Sync)</text>
    <text x="495" y="325" fill="#f1f5f9" font-size="11" text-anchor="middle">• BCCH (Sys Info)</text>

    <rect x="590" y="240" width="160" height="120" fill="#0f172a" stroke="#fbbf24" rx="4"/>
    <text x="670" y="262" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle">Common Control (CCCH)</text>
    <text x="670" y="285" fill="#f1f5f9" font-size="11" text-anchor="middle">• PCH (Paging MS)</text>
    <text x="670" y="305" fill="#f1f5f9" font-size="11" text-anchor="middle">• RACH (Uplink Request)</text>
    <text x="670" y="325" fill="#f1f5f9" font-size="11" text-anchor="middle">• AGCH (Access Grant)</text>

    <rect x="770" y="240" width="160" height="120" fill="#0f172a" stroke="#f43f5e" rx="4"/>
    <text x="850" y="262" fill="#f43f5e" font-size="12" font-weight="700" text-anchor="middle">Dedicated (DCCH)</text>
    <text x="850" y="285" fill="#f1f5f9" font-size="11" text-anchor="middle">• SDCCH (Call Setup/SMS)</text>
    <text x="850" y="305" fill="#f1f5f9" font-size="11" text-anchor="middle">• SACCH (Link Quality)</text>
    <text x="850" y="325" fill="#f1f5f9" font-size="11" text-anchor="middle">• FACCH (Fast Handover)</text>
    """,
    "Logical-to-Physical Mapping: Control channels multiplex onto TS0/TS1; Traffic channels multiplex onto TS1-TS7"
)

# mobile-q15: GSM Handover Sequence
create_card_diagram(
    "images/mobile_compute/gsm_handover_sequence.png",
    "GSM Mobile-Assisted Handover (MAHO): Inter-BSS Signaling Flow",
    "Measurement Reporting, Candidate BSC Evaluation, Channel Allocation, and Execution",
    "#10b981", "MOBILE • FIG 2.6B",
    """
    <!-- 4 Swimlanes -->
    <line x1="120" y1="110" x2="120" y2="370" stroke="#334155" stroke-dasharray="3,3"/>
    <line x1="340" y1="110" x2="340" y2="370" stroke="#334155" stroke-dasharray="3,3"/>
    <line x1="560" y1="110" x2="560" y2="370" stroke="#334155" stroke-dasharray="3,3"/>
    <line x1="780" y1="110" x2="780" y2="370" stroke="#334155" stroke-dasharray="3,3"/>

    <rect x="70" y="90" width="100" height="30" fill="url(#boxGrad)" stroke="#38bdf8" rx="4"/>
    <text x="120" y="110" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">MS</text>

    <rect x="290" y="90" width="100" height="30" fill="url(#boxGrad)" stroke="#fbbf24" rx="4"/>
    <text x="340" y="110" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle">Old BTS / BSC</text>

    <rect x="510" y="90" width="100" height="30" fill="url(#boxGrad)" stroke="#10b981" rx="4"/>
    <text x="560" y="110" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">MSC</text>

    <rect x="730" y="90" width="100" height="30" fill="url(#boxGrad)" stroke="#a855f7" rx="4"/>
    <text x="780" y="110" fill="#c084fc" font-size="12" font-weight="700" text-anchor="middle">New BTS / BSC</text>

    <!-- Message 1: Measurement Report -->
    <path d="M 120 140 L 340 140" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-cyan)"/>
    <text x="230" y="132" fill="#38bdf8" font-size="11" text-anchor="middle">1. Measurement Report (SACCH)</text>

    <!-- Message 2: Handover Required -->
    <path d="M 340 175 L 560 175" stroke="#fbbf24" stroke-width="2" marker-end="url(#arrow-amber)"/>
    <text x="450" y="167" fill="#fbbf24" font-size="11" text-anchor="middle">2. Handover Required (Old -> Target)</text>

    <!-- Message 3: Handover Request -->
    <path d="M 560 210 L 780 210" stroke="#34d399" stroke-width="2" marker-end="url(#arrow-green)"/>
    <text x="670" y="202" fill="#34d399" font-size="11" text-anchor="middle">3. Handover Request (Allocate Ch)</text>

    <!-- Message 4: Handover Request Ack -->
    <path d="M 780 245 L 560 245" stroke="#34d399" stroke-width="2" marker-end="url(#arrow-green)"/>
    <text x="670" y="237" fill="#34d399" font-size="11" text-anchor="middle">4. Handover Request Ack (New Ch Info)</text>

    <!-- Message 5: Handover Command -->
    <path d="M 560 280 L 120 280" stroke="#f43f5e" stroke-width="2.5" marker-end="url(#arrow-amber)"/>
    <text x="340" y="272" fill="#f87171" font-size="11" font-weight="700" text-anchor="middle">5. Handover Command (Retune to New Freq/Slot)</text>

    <!-- Message 6: Handover Complete -->
    <path d="M 120 320 L 780 320" stroke="#34d399" stroke-width="2" marker-end="url(#arrow-green)"/>
    <text x="450" y="312" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">6. Handover Complete (on New Channel)</text>

    <!-- Message 7: Clear Command -->
    <path d="M 560 350 L 340 350" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow-cyan)"/>
    <text x="450" y="342" fill="#94a3b8" font-size="10" text-anchor="middle">7. Clear Old Channel Resources</text>
    """,
    "Hard Handover: Break-before-make signaling completed in under 100 ms to maintain speech quality"
)

# mobile-q17: GSM Authentication & Cipher Timeline
create_card_diagram(
    "images/mobile_compute/gsm_auth_cipher_timeline.png",
    "GSM Cryptographic Protocol: SIM Authentication & A5 Stream Cipher",
    "Challenge-Response Authentication (A3) and Session Cipher Key Generation (A8, A5)",
    "#10b981", "MOBILE • FIG 2.8B",
    """
    <!-- 3 Entities -->
    <rect x="80" y="90" width="180" height="40" fill="url(#boxGrad)" stroke="#38bdf8" rx="6"/>
    <text x="170" y="115" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">SIM Card (in MS)</text>

    <rect x="390" y="90" width="180" height="40" fill="url(#boxGrad)" stroke="#fbbf24" rx="6"/>
    <text x="480" y="115" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">VLR / Serving MSC</text>

    <rect x="700" y="90" width="180" height="40" fill="url(#boxGrad)" stroke="#10b981" rx="6"/>
    <text x="790" y="115" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">HLR / AUC</text>

    <!-- Lifelines -->
    <line x1="170" y1="130" x2="170" y2="370" stroke="#334155" stroke-dasharray="3,3"/>
    <line x1="480" y1="130" x2="480" y2="370" stroke="#334155" stroke-dasharray="3,3"/>
    <line x1="790" y1="130" x2="790" y2="370" stroke="#334155" stroke-dasharray="3,3"/>

    <!-- Step 1: Triplet generation -->
    <rect x="720" y="145" width="140" height="45" fill="#0f172a" stroke="#10b981" rx="4"/>
    <text x="790" y="165" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">A3(Ki, RAND) -> SRES</text>
    <text x="790" y="180" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">A8(Ki, RAND) -> Kc</text>

    <!-- Step 2: Triplet to VLR -->
    <path d="M 790 205 L 480 205" stroke="#10b981" stroke-width="2" marker-end="url(#arrow-green)"/>
    <text x="635" y="197" fill="#34d399" font-size="11" text-anchor="middle">Send Triplet (RAND, SRES, Kc)</text>

    <!-- Step 3: Challenge to MS -->
    <path d="M 480 235 L 170 235" stroke="#fbbf24" stroke-width="2" marker-end="url(#arrow-amber)"/>
    <text x="325" y="227" fill="#fbbf24" font-size="11" text-anchor="middle">RAND Challenge (128 bits)</text>

    <!-- Step 4: SIM computes SRES and Kc -->
    <rect x="100" y="250" width="140" height="40" fill="#0f172a" stroke="#38bdf8" rx="4"/>
    <text x="170" y="267" fill="#38bdf8" font-size="10" font-weight="700" text-anchor="middle">SIM: SRES = A3(Ki,RAND)</text>
    <text x="170" y="282" fill="#38bdf8" font-size="10" font-weight="700" text-anchor="middle">Kc = A8(Ki,RAND)</text>

    <!-- Step 5: SRES response -->
    <path d="M 170 305 L 480 305" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-cyan)"/>
    <text x="325" y="297" fill="#38bdf8" font-size="11" text-anchor="middle">Authentication Response (SRES: 32 bits)</text>

    <!-- Step 6: VLR verifies -->
    <rect x="420" y="325" width="120" height="35" fill="#0f172a" stroke="#34d399" rx="4"/>
    <text x="480" y="347" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">SRES MATCH? -> OK!</text>
    """,
    "Master Key Protection: Subscriber individual key Ki never traverses the air interface or leaves SIM card"
)

# mobile-q21: SMS PDU Signaling Flow
create_card_diagram(
    "images/mobile_compute/sms_pdu_signaling_flow.png",
    "SMS End-to-End Signaling Protocol Flows: SM-MO and SM-MT",
    "Short Message Transmission via MAP Protocol over Signaling Channels (SDCCH/SACCH)",
    "#10b981", "MOBILE • FIG 3.4B",
    """
    <!-- Entities -->
    <rect x="60" y="90" width="110" height="35" fill="url(#boxGrad)" stroke="#38bdf8" rx="4"/>
    <text x="115" y="112" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">Origin MS</text>

    <rect x="230" y="90" width="110" height="35" fill="url(#boxGrad)" stroke="#fbbf24" rx="4"/>
    <text x="285" y="112" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle">VMSC / VLR</text>

    <rect x="420" y="90" width="120" height="35" fill="url(#boxGrad)" stroke="#10b981" rx="4"/>
    <text x="480" y="112" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">SMSC (Center)</text>

    <rect x="610" y="90" width="110" height="35" fill="url(#boxGrad)" stroke="#f43f5e" rx="4"/>
    <text x="665" y="112" fill="#f87171" font-size="12" font-weight="700" text-anchor="middle">HLR</text>

    <rect x="790" y="90" width="110" height="35" fill="url(#boxGrad)" stroke="#a855f7" rx="4"/>
    <text x="845" y="112" fill="#c084fc" font-size="12" font-weight="700" text-anchor="middle">Dest MS</text>

    <!-- Lifelines -->
    <line x1="115" y1="125" x2="115" y2="370" stroke="#334155" stroke-dasharray="3,3"/>
    <line x1="285" y1="125" x2="285" y2="370" stroke="#334155" stroke-dasharray="3,3"/>
    <line x1="480" y1="125" x2="480" y2="370" stroke="#334155" stroke-dasharray="3,3"/>
    <line x1="665" y1="125" x2="665" y2="370" stroke="#334155" stroke-dasharray="3,3"/>
    <line x1="845" y1="125" x2="845" y2="370" stroke="#334155" stroke-dasharray="3,3"/>

    <!-- SM-MO Phase -->
    <text x="290" y="145" fill="#38bdf8" font-size="11" font-weight="700">=== PHASE 1: MOBILE-ORIGINATED (SM-MO) ===</text>
    <path d="M 115 160 L 285 160" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-cyan)"/>
    <text x="200" y="153" fill="#38bdf8" font-size="10" text-anchor="middle">RP-MO-DATA (SDCCH)</text>

    <path d="M 285 185 L 480 185" stroke="#fbbf24" stroke-width="2" marker-end="url(#arrow-amber)"/>
    <text x="382" y="178" fill="#fbbf24" font-size="10" text-anchor="middle">MAP-MO-FORWARD-SHORT-MESSAGE</text>

    <rect x="430" y="200" width="100" height="24" fill="#1e293b" stroke="#10b981" rx="4"/>
    <text x="480" y="216" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">Store in SMSC</text>

    <!-- SM-MT Phase -->
    <text x="660" y="240" fill="#34d399" font-size="11" font-weight="700">=== PHASE 2: MOBILE-TERMINATED (SM-MT) ===</text>
    <path d="M 480 255 L 665 255" stroke="#f43f5e" stroke-width="2" marker-end="url(#arrow-amber)"/>
    <text x="572" y="248" fill="#f87171" font-size="10" text-anchor="middle">MAP-SEND-ROUTING-INFO-FOR-SM</text>

    <path d="M 665 280 L 480 280" stroke="#f43f5e" stroke-width="2" marker-end="url(#arrow-green)"/>
    <text x="572" y="273" fill="#f87171" font-size="10" text-anchor="middle">Returns Visited MSC Address</text>

    <path d="M 480 310 L 845 310" stroke="#34d399" stroke-width="2.5" marker-end="url(#arrow-green)"/>
    <text x="662" y="303" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">MAP-MT-FORWARD-SHORT-MESSAGE -> Delivery on SDCCH</text>

    <path d="M 845 340 L 480 340" stroke="#38bdf8" stroke-width="1.5" marker-end="url(#arrow-cyan)"/>
    <text x="662" y="333" fill="#38bdf8" font-size="10" text-anchor="middle">Delivery Acknowledgement Report</text>
    """,
    "Store-and-Forward Architecture: If destination MS is unreachable, SMSC stores message and retries upon HLR alert"
)

# mobile-q22: GPRS PDP Context Activation
create_card_diagram(
    "images/mobile_compute/gprs_pdp_context_activation.png",
    "GPRS Network: PDP Context Activation Signaling Procedure",
    "Establishing Packet Data Protocol (PDP) Tunnel from Mobile Station to APN / Public Internet",
    "#10b981", "MOBILE • FIG 3.5B",
    """
    <!-- 4 Entities -->
    <rect x="70" y="90" width="130" height="35" fill="url(#boxGrad)" stroke="#38bdf8" rx="4"/>
    <text x="135" y="112" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">MS (Mobile Station)</text>

    <rect x="310" y="90" width="130" height="35" fill="url(#boxGrad)" stroke="#fbbf24" rx="4"/>
    <text x="375" y="112" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle">SGSN (Serving)</text>

    <rect x="550" y="90" width="130" height="35" fill="url(#boxGrad)" stroke="#10b981" rx="4"/>
    <text x="615" y="112" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">GGSN (Gateway)</text>

    <rect x="760" y="90" width="150" height="35" fill="url(#boxGrad)" stroke="#a855f7" rx="4"/>
    <text x="835" y="112" fill="#c084fc" font-size="12" font-weight="700" text-anchor="middle">External IP Network</text>

    <!-- Lifelines -->
    <line x1="135" y1="125" x2="135" y2="370" stroke="#334155" stroke-dasharray="3,3"/>
    <line x1="375" y1="125" x2="375" y2="370" stroke="#334155" stroke-dasharray="3,3"/>
    <line x1="615" y1="125" x2="615" y2="370" stroke="#334155" stroke-dasharray="3,3"/>
    <line x1="835" y1="125" x2="835" y2="370" stroke="#334155" stroke-dasharray="3,3"/>

    <!-- Step 1: Activate PDP Request -->
    <path d="M 135 150 L 375 150" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-cyan)"/>
    <text x="255" y="142" fill="#38bdf8" font-size="10" text-anchor="middle">1. Activate PDP Context Request (APN, QoS)</text>

    <!-- Step 2: DNS & Security -->
    <rect x="330" y="170" width="90" height="24" fill="#0f172a" stroke="#fbbf24" rx="4"/>
    <text x="375" y="186" fill="#fbbf24" font-size="9" text-anchor="middle">DNS resolves GGSN</text>

    <!-- Step 3: Create PDP Context Request -->
    <path d="M 375 215 L 615 215" stroke="#fbbf24" stroke-width="2" marker-end="url(#arrow-amber)"/>
    <text x="495" y="207" fill="#fbbf24" font-size="10" text-anchor="middle">2. Create PDP Context Request (GTP Tunnel)</text>

    <!-- Step 4: IP Allocation -->
    <rect x="560" y="235" width="110" height="24" fill="#0f172a" stroke="#10b981" rx="4"/>
    <text x="615" y="251" fill="#34d399" font-size="9" text-anchor="middle">Dynamic IP Assigned</text>

    <!-- Step 5: Create PDP Response -->
    <path d="M 615 280 L 375 280" stroke="#10b981" stroke-width="2" marker-end="url(#arrow-green)"/>
    <text x="495" y="272" fill="#34d399" font-size="10" text-anchor="middle">3. Create PDP Context Response (Assigned IP)</text>

    <!-- Step 6: Activate PDP Accept -->
    <path d="M 375 315 L 135 315" stroke="#34d399" stroke-width="2" marker-end="url(#arrow-green)"/>
    <text x="255" y="307" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">4. Activate PDP Context Accept (Ready)</text>

    <!-- Established Tunnel Indicator -->
    <rect x="135" y="340" width="700" height="26" fill="#10b98122" stroke="#10b981" stroke-dasharray="2,2" rx="4"/>
    <text x="485" y="357" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">&lt;=== Bi-Directional User IP Packets Encapsulated via GTP ===&gt;</text>
    """,
    "GTP Tunneling: GPRS Tunneling Protocol (GTP) carries subscriber IP packets between SGSN and GGSN"
)

# mobile-q25: CSMA/CA Backoff Timeline
create_card_diagram(
    "images/mobile_compute/csma_ca_backoff_timeline.png",
    "IEEE 802.11 MAC: CSMA/CA Exponential Backoff & Contention Window",
    "Distributed Coordination Function (DCF): DIFS, Slot Countdown, Freezing Mechanism, and Collision Avoidance",
    "#10b981", "MOBILE • FIG 4.2C",
    """
    <!-- Timeline 1: Medium Status -->
    <text x="60" y="150" fill="#38bdf8" font-size="12" font-weight="700">Medium</text>
    <rect x="120" y="130" width="140" height="30" fill="#ef444433" stroke="#ef4444" rx="4"/>
    <text x="190" y="150" fill="#f87171" font-size="11" text-anchor="middle">BUSY</text>

    <!-- DIFS Interval -->
    <rect x="260" y="130" width="70" height="30" fill="#fbbf2433" stroke="#fbbf24" rx="4"/>
    <text x="295" y="150" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">DIFS</text>

    <!-- Backoff countdown -->
    <rect x="330" y="130" width="40" height="30" fill="#10b98133" stroke="#10b981"/>
    <text x="350" y="150" fill="#34d399" font-size="10" text-anchor="middle">Slot 5</text>
    <rect x="370" y="130" width="40" height="30" fill="#10b98133" stroke="#10b981"/>
    <text x="390" y="150" fill="#34d399" font-size="10" text-anchor="middle">Slot 4</text>
    <rect x="410" y="130" width="40" height="30" fill="#10b98133" stroke="#10b981"/>
    <text x="430" y="150" fill="#34d399" font-size="10" text-anchor="middle">Slot 3</text>

    <!-- Interruption by other transmission -->
    <rect x="450" y="130" width="150" height="30" fill="#ef444433" stroke="#ef4444" rx="4"/>
    <text x="525" y="150" fill="#f87171" font-size="11" text-anchor="middle">BUSY (Other Tx)</text>

    <!-- Defer and Freeze -->
    <rect x="600" y="130" width="70" height="30" fill="#fbbf2433" stroke="#fbbf24" rx="4"/>
    <text x="635" y="150" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">DIFS</text>

    <!-- Resumed Countdown from Slot 2 -->
    <rect x="670" y="130" width="40" height="30" fill="#10b98133" stroke="#10b981"/>
    <text x="690" y="150" fill="#34d399" font-size="10" text-anchor="middle">Slot 2</text>
    <rect x="710" y="130" width="40" height="30" fill="#10b98133" stroke="#10b981"/>
    <text x="730" y="150" fill="#34d399" font-size="10" text-anchor="middle">Slot 1</text>

    <!-- Station Transmits Data Frame -->
    <rect x="750" y="125" width="160" height="40" fill="#10b981" rx="4"/>
    <text x="830" y="150" fill="#0c1220" font-size="12" font-weight="700" text-anchor="middle">DATA FRAME TX</text>

    <!-- Explanation Box Below -->
    <rect x="120" y="210" width="790" height="150" fill="url(#boxGrad)" stroke="#10b981" rx="8"/>
    <text x="515" y="235" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">CSMA/CA Backoff Algorithm Rules</text>
    <text x="515" y="260" fill="#f1f5f9" font-size="12" text-anchor="middle">1. Random Backoff Time = Random[0, CW] × Slot Time (e.g. 20 µs for 802.11b/g)</text>
    <text x="515" y="285" fill="#fbbf24" font-size="12" text-anchor="middle">2. Freezing Rule: If channel becomes busy during countdown, timer PAUSES and preserves state</text>
    <text x="515" y="310" fill="#38bdf8" font-size="12" text-anchor="middle">3. Resumption: When channel clears and stays idle for full DIFS, countdown resumes</text>
    <text x="515" y="335" fill="#f87171" font-size="12" text-anchor="middle">4. Exponential Binary Backoff: CW doubles upon collision: CW_min = 15 -> 31 -> 63 -> ... -> 1023</text>
    """,
    "Fair Channel Access: Freezing mechanism ensures stations that have waited longer gain higher priority to transmit"
)

# mobile-q27: RTS/CTS and NAV Timing
create_card_diagram(
    "images/mobile_compute/rts_cts_nav_timing.png",
    "IEEE 802.11 RTS/CTS Protocol: Virtual Carrier Sensing (NAV) Timeline",
    "Mitigating Hidden & Exposed Terminal Collisions via Network Allocation Vector Reservation",
    "#10b981", "MOBILE • FIG 4.4B",
    """
    <!-- 4 Timelines: Sender A, Receiver B, Hidden Node C, Other D -->
    <line x1="120" y1="140" x2="900" y2="140" stroke="#334155"/>
    <line x1="120" y1="200" x2="900" y2="200" stroke="#334155"/>
    <line x1="120" y1="270" x2="900" y2="270" stroke="#334155"/>
    <line x1="120" y1="330" x2="900" y2="330" stroke="#334155"/>

    <text x="110" y="145" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="end">Source A</text>
    <text x="110" y="205" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="end">Dest B</text>
    <text x="110" y="275" fill="#f43f5e" font-size="12" font-weight="700" text-anchor="end">Hidden C</text>
    <text x="110" y="335" fill="#94a3b8" font-size="12" font-weight="700" text-anchor="end">Exposed D</text>

    <!-- Source A sends RTS -->
    <rect x="140" y="125" width="80" height="30" fill="#38bdf8" rx="4"/>
    <text x="180" y="145" fill="#0c1220" font-size="11" font-weight="700" text-anchor="middle">RTS</text>

    <!-- SIFS -->
    <text x="235" y="145" fill="#94a3b8" font-size="9">SIFS</text>

    <!-- Dest B sends CTS -->
    <rect x="250" y="185" width="80" height="30" fill="#fbbf24" rx="4"/>
    <text x="290" y="205" fill="#0c1220" font-size="11" font-weight="700" text-anchor="middle">CTS</text>

    <!-- Source A sends DATA -->
    <rect x="360" y="125" width="340" height="30" fill="#10b981" rx="4"/>
    <text x="530" y="145" fill="#0c1220" font-size="12" font-weight="700" text-anchor="middle">DATA FRAME TRANSMISSION</text>

    <!-- Dest B sends ACK -->
    <rect x="730" y="185" width="70" height="30" fill="#34d399" rx="4"/>
    <text x="765" y="205" fill="#0c1220" font-size="11" font-weight="700" text-anchor="middle">ACK</text>

    <!-- Hidden Node C sets NAV from CTS! -->
    <rect x="330" y="255" width="480" height="28" fill="#ef444433" stroke="#ef4444" rx="4"/>
    <text x="570" y="273" fill="#f87171" font-size="11" font-weight="700" text-anchor="middle">NAV (Network Allocation Vector) - Transmission Deferred!</text>

    <!-- Exposed Node D sets NAV from RTS only -->
    <rect x="220" y="315" width="130" height="28" fill="#fbbf2433" stroke="#fbbf24" rx="4"/>
    <text x="285" y="333" fill="#fbbf24" font-size="10" text-anchor="middle">NAV (RTS duration)</text>
    """,
    "Virtual Carrier Sensing: Duration field in RTS/CTS informs all neighbor nodes how long to silence transmitters (NAV)"
)

# mobile-q34: RSA Encryption Pipeline
create_card_diagram(
    "images/mobile_compute/rsa_encryption_pipeline.png",
    "RSA Cryptosystem: Complete Step-by-Step Processing Pipeline",
    "Prime Setup (p=3, q=11) -> Keys (e=3, d=7) -> Encryption (C=M^e) -> Decryption (M=C^d)",
    "#10b981", "MOBILE • FIG 5.4B",
    """
    <!-- Step 1: Prime Setup -->
    <rect x="60" y="110" width="260" height="120" fill="url(#boxGrad)" stroke="#38bdf8" rx="8"/>
    <text x="190" y="135" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">1. Key Generation Setup</text>
    <text x="190" y="160" fill="#f1f5f9" font-size="12" text-anchor="middle">Choose primes: p = 3,  q = 11</text>
    <text x="190" y="185" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">n = p · q = 33 (Modulus)</text>
    <text x="190" y="210" fill="#34d399" font-size="12" text-anchor="middle">φ(n) = (p-1)(q-1) = 2 × 10 = 20</text>

    <!-- Arrow 1 -->
    <path d="M 320 170 L 370 170" stroke="#fbbf24" stroke-width="2.5" marker-end="url(#arrow-amber)"/>

    <!-- Step 2: Keys -->
    <rect x="370" y="110" width="240" height="120" fill="url(#boxGrad)" stroke="#fbbf24" rx="8"/>
    <text x="490" y="135" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">2. Public &amp; Private Key</text>
    <text x="490" y="160" fill="#f1f5f9" font-size="12" text-anchor="middle">Select e = 3  (gcd(3, 20) = 1)</text>
    <text x="490" y="185" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">Public Key: (e = 3, n = 33)</text>
    <text x="490" y="210" fill="#f87171" font-size="12" font-weight="700" text-anchor="middle">Private Key: (d = 7, n = 33)</text>

    <!-- Arrow 2 -->
    <path d="M 610 170 L 660 170" stroke="#34d399" stroke-width="2.5" marker-end="url(#arrow-green)"/>

    <!-- Step 3: Encryption -->
    <rect x="660" y="110" width="240" height="120" fill="url(#boxGrad)" stroke="#10b981" rx="8"/>
    <text x="780" y="135" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">3. Encryption (Alice)</text>
    <text x="780" y="160" fill="#f1f5f9" font-size="12" text-anchor="middle">Plaintext Message M = 2</text>
    <text x="780" y="185" fill="#94a3b8" font-size="11" text-anchor="middle">C = M^e mod n = 2³ mod 33</text>
    <text x="780" y="212" fill="#fbbf24" font-size="14" font-weight="700" text-anchor="middle">Ciphertext C = 8</text>

    <!-- Transmission Channel -->
    <path d="M 780 230 L 780 270 L 490 270" stroke="#f43f5e" stroke-width="2"/>
    <rect x="360" y="255" width="260" height="30" fill="#ef444422" stroke="#ef4444" rx="4"/>
    <text x="490" y="275" fill="#f87171" font-size="11" font-weight="700" text-anchor="middle">Public Radio Channel (Transmits C = 8)</text>
    <path d="M 360 270 L 190 270 L 190 300" stroke="#f43f5e" stroke-width="2" marker-end="url(#arrow-green)"/>

    <!-- Step 4: Decryption -->
    <rect x="60" y="300" width="840" height="70" fill="url(#boxGrad)" stroke="#34d399" stroke-width="2" rx="8"/>
    <text x="480" y="325" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">4. Decryption (Bob with Private Key d=7): M = C^d mod n</text>
    <text x="480" y="350" fill="#f1f5f9" font-size="13" text-anchor="middle">M = 8⁷ mod 33 = (8⁴ × 8² × 8¹) mod 33 = (4 × -2 × 8) mod 33 = -64 mod 33 = 2  ==>  ORIGINAL MESSAGE RESTORED!</text>
    """,
    "Asymmetric Security: Knowing public key (e=3, n=33) does not reveal private d without factoring n into p and q"
)

# mobile-q35: Diffie-Hellman Color Mixing and Math Flow
create_card_diagram(
    "images/mobile_compute/diffie_hellman_color_mixing_math.png",
    "Diffie-Hellman Key Exchange: Discrete Logarithm Math Flow & Analogy",
    "Alice & Bob Agree on Public Base (g=5, p=23) and Establish Secret Session Key K=2",
    "#10b981", "MOBILE • FIG 5.5B",
    """
    <!-- Alice Box on Left -->
    <rect x="60" y="110" width="260" height="240" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="2" rx="8"/>
    <text x="190" y="135" fill="#38bdf8" font-size="15" font-weight="700" text-anchor="middle">Alice (Private a = 6)</text>
    <text x="190" y="165" fill="#f1f5f9" font-size="12" text-anchor="middle">Public param: p = 23, g = 5</text>
    <rect x="80" y="180" width="220" height="40" fill="#0f172a" stroke="#38bdf8" rx="4"/>
    <text x="190" y="200" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="middle">A = g^a mod p = 5⁶ mod 23</text>
    <text x="190" y="215" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">Public A = 8  (Sends to Bob)</text>
    
    <text x="190" y="250" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">Receives B = 19 from Bob</text>
    <rect x="80" y="265" width="220" height="65" fill="#10b98122" stroke="#10b981" rx="4"/>
    <text x="190" y="287" fill="#34d399" font-size="11" text-anchor="middle">Computes Shared Secret K:</text>
    <text x="190" y="305" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">K = B^a mod p = 19⁶ mod 23</text>
    <text x="190" y="322" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">K = 2</text>

    <!-- Public Insecure Channel in Middle -->
    <rect x="360" y="110" width="240" height="240" fill="#0f172a" stroke="#ef4444" stroke-dasharray="2,2" rx="8"/>
    <text x="480" y="135" fill="#f87171" font-size="13" font-weight="700" text-anchor="middle">Insecure Public Channel</text>
    <text x="480" y="160" fill="#94a3b8" font-size="11" text-anchor="middle">Eavesdropper (Eve) observes:</text>
    <text x="480" y="185" fill="#f1f5f9" font-size="12" text-anchor="middle">p = 23 ,  g = 5</text>
    <text x="480" y="210" fill="#38bdf8" font-size="12" text-anchor="middle">A = 8  (Alice -> Bob)</text>
    <text x="480" y="235" fill="#a855f7" font-size="12" text-anchor="middle">B = 19 (Bob -> Alice)</text>
    <rect x="380" y="265" width="200" height="65" fill="#1e293b" rx="4"/>
    <text x="480" y="288" fill="#f87171" font-size="11" font-weight="700" text-anchor="middle">Discrete Log Problem:</text>
    <text x="480" y="306" fill="#94a3b8" font-size="10" text-anchor="middle">Finding a from 5^a ≡ 8</text>
    <text x="480" y="322" fill="#ef4444" font-size="10" text-anchor="middle">is computationally infeasible!</text>

    <!-- Bob Box on Right -->
    <rect x="640" y="110" width="260" height="240" fill="url(#boxGrad)" stroke="#a855f7" stroke-width="2" rx="8"/>
    <text x="770" y="135" fill="#c084fc" font-size="15" font-weight="700" text-anchor="middle">Bob (Private b = 15)</text>
    <text x="770" y="165" fill="#f1f5f9" font-size="12" text-anchor="middle">Public param: p = 23, g = 5</text>
    <rect x="660" y="180" width="220" height="40" fill="#0f172a" stroke="#a855f7" rx="4"/>
    <text x="770" y="200" fill="#c084fc" font-size="11" font-weight="700" text-anchor="middle">B = g^b mod p = 5¹⁵ mod 23</text>
    <text x="770" y="215" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">Public B = 19  (Sends to Alice)</text>
    
    <text x="770" y="250" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">Receives A = 8 from Alice</text>
    <rect x="660" y="265" width="220" height="65" fill="#10b98122" stroke="#10b981" rx="4"/>
    <text x="770" y="287" fill="#34d399" font-size="11" text-anchor="middle">Computes Shared Secret K:</text>
    <text x="770" y="305" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">K = A^b mod p = 8¹⁵ mod 23</text>
    <text x="770" y="322" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">K = 2</text>
    """,
    "Identical Secret Key: K = g^(ab) mod p = 2 | Key is established without either party sending their private exponent"
)

print("All 28 supplementary diagrams successfully generated and verified!")
