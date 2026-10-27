# -*- coding: utf-8 -*-
"""
Batch vector diagram generator for missing Electric Drives (EET413) questions.
Renders 24 high-resolution 960x460 engineering schematics to PNG using sips.
"""
import os, subprocess, re

os.makedirs("images/drive", exist_ok=True)

def render_svg_to_png(svg_content, png_path):
    if os.path.exists(png_path) and os.path.getsize(png_path) > 1000:
        return
    svg_content = re.sub(r'&(?!(amp|lt|gt|quot|apos|#\d+|#x[0-9a-fA-F]+);)', '&amp;', svg_content)
    svg_path = png_path.replace(".png", ".svg")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    res = subprocess.run(["sips", "-s", "format", "png", svg_path, "--out", png_path], 
                         capture_output=True, text=True)
    if os.path.exists(svg_path):
        os.remove(svg_path)
    if os.path.exists(png_path):
        print(f"Rendered -> {png_path} ({os.path.getsize(png_path)} bytes)")
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
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="{accent_color}"/>
    </marker>
    <marker id="arrow-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#10b981"/>
    </marker>
  </defs>
  <rect width="960" height="460" fill="url(#bgGrad)" rx="16"/>
  <rect x="20" y="20" width="920" height="420" fill="none" stroke="#223049" stroke-width="1.5" rx="12"/>
  
  <rect x="40" y="35" width="140" height="26" fill="{accent_color}22" stroke="{accent_color}" stroke-width="1" rx="5"/>
  <text x="110" y="52" fill="{accent_color}" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">{badge_text}</text>
  <text x="500" y="55" fill="#f1f5f9" font-family="-apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">{title}</text>
  <text x="500" y="80" fill="#94a3b8" font-family="-apple-system, sans-serif" font-size="13" text-anchor="middle">{subtitle}</text>
  {elements_xml}
  {f'''<rect x="40" y="405" width="880" height="24" fill="#0b111e" stroke="#223049" stroke-width="1" rx="4"/>
  <text x="480" y="421" fill="#94a3b8" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">{footer_text}</text>''' if footer_text else ''}
</svg>"""
    render_svg_to_png(svg, png_path)

print("Starting generation of missing Electric Drives diagrams...")

# 1. drive-q2: drive_efficiency_curve.png
create_card_diagram(
    "images/drive/drive_efficiency_curve.png",
    "Energy Efficiency Comparison: VFD Electric Drive vs Mechanical Throttling",
    "Cube-Law Fan/Pump Affinity Power Savings: P ∝ N³ with Inverter Speed Control",
    "#f59e0b", "DRIVE • MOD 1",
    """
    <!-- Graph Axes -->
    <path d="M 120 340 L 480 340" stroke="#94a3b8" stroke-width="2"/>
    <path d="M 120 340 L 120 140" stroke="#94a3b8" stroke-width="2"/>
    <text x="300" y="375" fill="#f1f5f9" font-size="13" font-weight="600" text-anchor="middle">Flow Rate / Speed (% of Rated)</text>
    <text x="70" y="240" fill="#f1f5f9" font-size="13" font-weight="600" transform="rotate(-90 70 240)" text-anchor="middle">Power Input (%)</text>

    <!-- Throttling Curve (Mechanical Valve) -->
    <path d="M 120 200 C 220 205, 350 220, 460 330" stroke="#ef4444" stroke-width="3" fill="none"/>
    <text x="350" y="195" fill="#f87171" font-size="12" font-weight="700">Mechanical Throttling Valve</text>

    <!-- VFD Cube Curve -->
    <path d="M 120 335 C 260 330, 380 270, 460 150" stroke="#10b981" stroke-width="3.5" fill="none"/>
    <text x="390" y="140" fill="#34d399" font-size="12" font-weight="700">VFD Drive Speed Control (P ∝ N³)</text>

    <!-- Shaded energy saving area -->
    <path d="M 280 215 L 280 310" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,4"/>
    <rect x="230" y="240" width="110" height="30" fill="#38bdf822" stroke="#38bdf8" rx="4"/>
    <text x="285" y="260" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">Up to 60% Savings</text>

    <!-- Right Side Benefits Card -->
    <rect x="520" y="125" width="390" height="240" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="10"/>
    <text x="715" y="155" fill="#fbbf24" font-size="16" font-weight="700" text-anchor="middle">Key Industrial Advantages</text>
    <text x="545" y="190" fill="#34d399" font-size="13" font-weight="600">✔ High Efficiency:</text>
    <text x="670" y="190" fill="#cbd5e1" font-size="13">Operates above 90% across wide range</text>
    <text x="545" y="225" fill="#38bdf8" font-size="13" font-weight="600">✔ Dynamic Response:</text>
    <text x="690" y="225" fill="#cbd5e1" font-size="13">Sub-millisecond torque/speed control</text>
    <text x="545" y="260" fill="#fbbf24" font-size="13" font-weight="600">✔ Multi-Quadrant:</text>
    <text x="665" y="260" fill="#cbd5e1" font-size="13">Motoring and regenerative braking</text>
    <text x="545" y="295" fill="#a855f7" font-size="13" font-weight="600">✔ Low Maintenance:</text>
    <text x="685" y="295" fill="#cbd5e1" font-size="13">No mechanical gears, clutches, or belts</text>
    <text x="545" y="330" fill="#10b981" font-size="13" font-weight="600">✔ Clean &amp; Compact:</text>
    <text x="680" y="330" fill="#cbd5e1" font-size="13">Zero direct emissions, quiet operation</text>
    """,
    "Affinity Laws for Centrifugal Loads: Flow Q ∝ N | Head H ∝ N² | Mechanical Power P ∝ N³"
)

# 2. drive-q3b: critical_speed_resonance.png
create_card_diagram(
    "images/drive/critical_speed_resonance.png",
    "Critical Speed and Torsional Resonance in Electric Drives",
    "Dynamic Shaft Deflection: r = (m·e·ω²) / (K - m·ω²) Diverges at Resonance ω = ω_n",
    "#f59e0b", "DRIVE • MOD 1",
    """
    <rect x="50" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="10"/>
    <text x="255" y="145" fill="#fbbf24" font-size="16" font-weight="700" text-anchor="middle">1. Rotating Shaft with Eccentric Mass</text>
    <!-- Shaft & Rotor Disk -->
    <line x1="80" y1="230" x2="420" y2="230" stroke="#94a3b8" stroke-width="3"/>
    <circle cx="250" cy="230" r="60" fill="#0b111e" stroke="#38bdf8" stroke-width="3"/>
    <circle cx="250" cy="230" r="4" fill="#38bdf8"/>
    <text x="250" y="215" fill="#38bdf8" font-size="11">Geometric Center</text>
    <!-- Eccentric mass -->
    <circle cx="275" cy="210" r="8" fill="#ef4444"/>
    <text x="290" y="215" fill="#f87171" font-size="12" font-weight="700">Mass m (e)</text>
    <line x1="250" y1="230" x2="275" y2="210" stroke="#ef4444" stroke-width="2"/>
    <text x="255" y="325" fill="#cbd5e1" font-size="12" text-anchor="middle">Centrifugal Force F_c = m · (r + e) · ω²</text>
    <text x="255" y="350" fill="#34d399" font-size="12" text-anchor="middle">Restoring Shaft Stiffness Force F_s = K · r</text>

    <!-- Resonance Graph -->
    <rect x="500" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#ef4444" stroke-width="1.5" rx="10"/>
    <text x="705" y="145" fill="#f87171" font-size="16" font-weight="700" text-anchor="middle">2. Amplitude Divergence at Critical Speed</text>
    <path d="M 540 330 L 870 330" stroke="#94a3b8" stroke-width="1.5"/>
    <path d="M 540 330 L 540 170" stroke="#94a3b8" stroke-width="1.5"/>
    <!-- Resonance curve -->
    <path d="M 550 325 C 620 320, 680 300, 695 180" stroke="#ef4444" stroke-width="3" fill="none"/>
    <path d="M 715 180 C 730 300, 780 320, 850 325" stroke="#ef4444" stroke-width="3" fill="none"/>
    <!-- Critical speed line -->
    <line x1="705" y1="165" x2="705" y2="330" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4,4"/>
    <text x="705" y="350" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">ω_cr = √(K / m)</text>
    <rect x="635" y="180" width="140" height="30" fill="#ef444433" stroke="#ef4444" rx="4"/>
    <text x="705" y="200" fill="#f87171" font-size="11" font-weight="700" text-anchor="middle">Severe Vibration Zone</text>
    <text x="705" y="250" fill="#cbd5e1" font-size="12" text-anchor="middle">At resonance: r → ∞ without damping</text>
    <text x="705" y="280" fill="#94a3b8" font-size="11" text-anchor="middle">Mitigation: Fast ramp-through &amp; notch filters</text>
    """,
    "Operational Guideline: Drives must accelerate rapidly through the critical speed range to avoid mechanical shaft fatigue"
)

# 3. drive-q4: dynamic_torque_derivation.png
create_card_diagram(
    "images/drive/dynamic_torque_derivation.png",
    "Fundamental Dynamic Torque Equation for Rotational Motion",
    "Derivation: T - T_l = J · (dω_m / dt) + D · ω_m from Newton's Second Law for Rotation",
    "#f59e0b", "DRIVE • MOD 1",
    """
    <!-- Motor and Load Shaft Diagram -->
    <rect x="50" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="10"/>
    <text x="255" y="145" fill="#fbbf24" font-size="16" font-weight="700" text-anchor="middle">Rotating Motor-Load Inertia Model</text>
    
    <!-- Motor Cylinder -->
    <rect x="90" y="190" width="90" height="90" fill="#0b111e" stroke="#38bdf8" stroke-width="2" rx="10"/>
    <text x="135" y="240" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">Motor (T)</text>

    <!-- Shaft -->
    <rect x="180" y="225" width="130" height="20" fill="#334155" stroke="#94a3b8"/>
    <!-- Inertia Flywheel -->
    <ellipse cx="245" cy="235" rx="15" ry="45" fill="#1e293b" stroke="#fbbf24" stroke-width="2.5"/>
    <text x="245" y="175" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">Inertia J</text>

    <!-- Load Cylinder -->
    <rect x="310" y="190" width="100" height="90" fill="#0b111e" stroke="#ef4444" stroke-width="2" rx="10"/>
    <text x="360" y="240" fill="#f87171" font-size="14" font-weight="700" text-anchor="middle">Load (T_l)</text>

    <!-- Rotation arrow -->
    <path d="M 210 205 Q 245 190 280 205" fill="none" stroke="#34d399" stroke-width="2.5" marker-end="url(#arrow-green)"/>
    <text x="245" y="305" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">Speed ω_m (rad/s)</text>
    <text x="255" y="345" fill="#cbd5e1" font-size="12" text-anchor="middle">Viscous damping friction: T_v = B · ω_m</text>

    <!-- Mathematical Derivation -->
    <rect x="500" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
    <text x="705" y="145" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">Dynamic Equilibrium Analysis</text>
    <text x="705" y="180" fill="#f1f5f9" font-size="13" text-anchor="middle">Net Accelerating Torque: T_net = T - T_l</text>
    
    <rect x="530" y="200" width="350" height="65" fill="#0b111e" stroke="#10b981" stroke-width="2" rx="6"/>
    <text x="705" y="230" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">T - T_l = J · (dω_m / dt)</text>
    <text x="705" y="252" fill="#fbbf24" font-size="13" text-anchor="middle">Fundamental Equation of Motion</text>

    <text x="705" y="295" fill="#cbd5e1" font-size="12" text-anchor="middle">Acceleration: T &gt; T_l  ⟹  dω_m/dt &gt; 0 (Speed Increases)</text>
    <text x="705" y="325" fill="#cbd5e1" font-size="12" text-anchor="middle">Deceleration: T &lt; T_l  ⟹  dω_m/dt &lt; 0 (Speed Decreases)</text>
    <text x="705" y="355" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">Steady-State: T = T_l  ⟹  dω_m/dt = 0 (Constant Speed)</text>
    """,
    "Total Load Torque Components: T_l = T_friction + T_windage + T_workload | Dynamic Torque J(dω/dt) vanishes at steady state"
)

# 4. drive-q6: stability_criterion_curves.png
create_card_diagram(
    "images/drive/stability_criterion_curves.png",
    "Steady-State Stability Criterion of Electric Drives",
    "Perturbation Stability Condition: (dT_l / dω_m) - (dT / dω_m) > 0 at Operating Point",
    "#f59e0b", "DRIVE • MOD 1",
    """
    <!-- Graph -->
    <rect x="50" y="115" width="430" height="260" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="10"/>
    <text x="265" y="145" fill="#fbbf24" font-size="16" font-weight="700" text-anchor="middle">Torque-Speed Characteristic Intersection</text>
    <path d="M 90 330 L 440 330" stroke="#94a3b8" stroke-width="1.5"/>
    <path d="M 90 330 L 90 170" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="270" y="355" fill="#f1f5f9" font-size="12" text-anchor="middle">Motor Speed ω_m</text>
    <text x="70" y="250" fill="#f1f5f9" font-size="12" transform="rotate(-90 70 250)" text-anchor="middle">Torque T</text>

    <!-- Motor curve (descending) -->
    <path d="M 120 180 Q 250 250 410 320" stroke="#38bdf8" stroke-width="3" fill="none"/>
    <text x="170" y="200" fill="#38bdf8" font-size="13" font-weight="700">Motor Torque T</text>

    <!-- Load curve (ascending) -->
    <path d="M 120 310 Q 260 260 410 180" stroke="#f59e0b" stroke-width="3" fill="none"/>
    <text x="360" y="200" fill="#fbbf24" font-size="13" font-weight="700">Load Torque T_l</text>

    <!-- Operating Point -->
    <circle cx="265" cy="255" r="6" fill="#10b981"/>
    <text x="265" y="240" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">Point A (Stable)</text>

    <!-- Mathematical Derivation -->
    <rect x="510" y="115" width="400" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
    <text x="710" y="145" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">Small Perturbation Analysis</text>
    <text x="710" y="175" fill="#f1f5f9" font-size="13" text-anchor="middle">Let ω_m = ω_m0 + Δω,  T = T₀ + (dT/dω)Δω</text>
    
    <rect x="530" y="195" width="360" height="60" fill="#0b111e" stroke="#10b981" stroke-width="2" rx="6"/>
    <text x="710" y="222" fill="#34d399" font-size="15" font-weight="700" text-anchor="middle">(dT_l / dω_m) - (dT / dω_m) &gt; 0</text>
    <text x="710" y="244" fill="#fbbf24" font-size="12" text-anchor="middle">Necessary &amp; Sufficient Condition for Stability</text>

    <text x="710" y="285" fill="#cbd5e1" font-size="12" text-anchor="middle">If Δω &gt; 0: T_l &gt; T  ⟹  d(Δω)/dt &lt; 0 (Restores speed to A)</text>
    <text x="710" y="315" fill="#cbd5e1" font-size="12" text-anchor="middle">If Δω &lt; 0: T &gt; T_l  ⟹  d(Δω)/dt &gt; 0 (Restores speed to A)</text>
    <text x="710" y="348" fill="#f87171" font-size="11" text-anchor="middle">If (dT_l/dω) &lt; (dT/dω): Runaway instability occurs</text>
    """,
    "Physical Criterion: At the operating point, the slope of the load characteristic must exceed that of the motor characteristic"
)

# 5. drive-q6b: thermal_heating_cooling.png
create_card_diagram(
    "images/drive/thermal_heating_cooling.png",
    "Thermal Heating and Cooling Curves in Electric Motors",
    "Transient Temperature Rise: θ(t) = θ_ss · (1 - e^(-t / τ_h)) and Cooling θ(t) = θ_0 · e^(-t / τ_c)",
    "#f59e0b", "DRIVE • MOD 1",
    """
    <rect x="50" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="10"/>
    <text x="255" y="145" fill="#fbbf24" font-size="16" font-weight="700" text-anchor="middle">1. Heating Transient Curve</text>
    <path d="M 90 330 L 420 330" stroke="#94a3b8" stroke-width="1.5"/>
    <path d="M 90 330 L 90 170" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="260" y="355" fill="#f1f5f9" font-size="12" text-anchor="middle">Time t (Heating)</text>
    <text x="70" y="250" fill="#f1f5f9" font-size="12" transform="rotate(-90 70 250)" text-anchor="middle">Temp Rise θ (°C)</text>

    <!-- Heating curve -->
    <path d="M 90 330 C 140 240, 240 190, 410 190" stroke="#ef4444" stroke-width="3" fill="none"/>
    <line x1="90" y1="190" x2="410" y2="190" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4,4"/>
    <text x="420" y="185" fill="#f87171" font-size="13" font-weight="700">θ_ss</text>
    <text x="255" y="275" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">θ(t) = θ_ss · (1 - e^(-t/τ_h))</text>
    <text x="255" y="305" fill="#cbd5e1" font-size="11" text-anchor="middle">Thermal Time Constant τ_h = C / A·h (15-60 min)</text>

    <rect x="500" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="10"/>
    <text x="705" y="145" fill="#38bdf8" font-size="16" font-weight="700" text-anchor="middle">2. Cooling Transient Curve</text>
    <path d="M 540 330 L 870 330" stroke="#94a3b8" stroke-width="1.5"/>
    <path d="M 540 330 L 540 170" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="710" y="355" fill="#f1f5f9" font-size="12" text-anchor="middle">Time t (Cooling)</text>

    <!-- Cooling curve -->
    <path d="M 540 190 C 620 280, 720 325, 860 328" stroke="#38bdf8" stroke-width="3" fill="none"/>
    <text x="530" y="185" fill="#38bdf8" font-size="13" font-weight="700">θ_0</text>
    <text x="705" y="245" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">θ(t) = θ_0 · e^(-t/τ_c)</text>
    <text x="705" y="285" fill="#cbd5e1" font-size="12" text-anchor="middle">Cooling Time Constant τ_c &gt; τ_h</text>
    <text x="705" y="315" fill="#fbbf24" font-size="11" text-anchor="middle">Notice: Fan stops when motor halts (poor convection)</text>
    """,
    "Motor Insulation Ratings: Class B (130°C), Class F (155°C), Class H (180°C) | Lifetime halves for every 10°C overtemperature"
)

# 6. drive-q7: dc_motor_control_zones.png
create_card_diagram(
    "images/drive/dc_motor_control_zones.png",
    "DC Motor Speed Control Zones: Constant Torque vs Constant Power",
    "Armature Voltage Control Below Base Speed vs Field Weakening Above Base Speed",
    "#f59e0b", "DRIVE • MOD 2",
    """
    <!-- Graph Area -->
    <path d="M 120 340 L 860 340" stroke="#94a3b8" stroke-width="2"/>
    <path d="M 120 340 L 120 140" stroke="#94a3b8" stroke-width="2"/>
    <text x="490" y="375" fill="#f1f5f9" font-size="13" font-weight="600" text-anchor="middle">Motor Speed ω_m (rad/s)</text>
    
    <!-- Base Speed Divider -->
    <line x1="450" y1="120" x2="450" y2="340" stroke="#94a3b8" stroke-width="2" stroke-dasharray="6,6"/>
    <text x="450" y="360" fill="#fbbf24" font-size="14" font-weight="700" text-anchor="middle">Base Speed ω_base</text>

    <!-- Zone 1: Constant Torque -->
    <rect x="130" y="115" width="310" height="35" fill="#38bdf822" stroke="#38bdf8" rx="6"/>
    <text x="285" y="138" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">ZONE 1: Armature Voltage Control</text>
    <!-- Constant torque horizontal line -->
    <line x1="120" y1="180" x2="450" y2="180" stroke="#10b981" stroke-width="4"/>
    <text x="285" y="170" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">Torque T = T_rated (CONSTANT)</text>
    <!-- Power rising line -->
    <line x1="120" y1="340" x2="450" y2="180" stroke="#f59e0b" stroke-width="3"/>
    <text x="270" y="260" fill="#fbbf24" font-size="12" font-weight="600">Power P = T · ω (Rises)</text>
    <text x="285" y="305" fill="#cbd5e1" font-size="12" text-anchor="middle">Flux Φ = Φ_rated | V_a varies 0 to V_rated</text>

    <!-- Zone 2: Constant Power (Field Weakening) -->
    <rect x="460" y="115" width="390" height="35" fill="#f59e0b22" stroke="#f59e0b" rx="6"/>
    <text x="655" y="138" fill="#fbbf24" font-size="14" font-weight="700" text-anchor="middle">ZONE 2: Field Weakening Control</text>
    <!-- Constant power line -->
    <line x1="450" y1="180" x2="850" y2="180" stroke="#f59e0b" stroke-width="4"/>
    <text x="650" y="170" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">Power P = P_rated (CONSTANT)</text>
    <!-- Hyperbolic torque drop -->
    <path d="M 450 180 C 550 240, 680 290, 850 310" stroke="#10b981" stroke-width="3" fill="none"/>
    <text x="660" y="270" fill="#34d399" font-size="12" font-weight="600">Torque T = P / ω (Drops ∝ 1/ω)</text>
    <text x="655" y="305" fill="#cbd5e1" font-size="12" text-anchor="middle">V_a = V_rated | Flux Φ reduced via field current I_f</text>
    """,
    "Separately Excited DC Motor Equations: E_b = K_e · Φ · ω_m | Developed Torque T = K_t · Φ · I_a"
)

# 7. drive-q7b: three_phase_semi_converter.png
create_card_diagram(
    "images/drive/three_phase_semi_converter.png",
    "Three-Phase Semi-Converter Fed Separately Excited DC Motor Drive",
    "Circuit Topology (3 SCRs, 3 Diodes, Freewheeling Diode) and Output Voltage: V_dc = (3·V_ml / 2π)·(1 + cos α)",
    "#f59e0b", "DRIVE • MOD 2",
    """
    <!-- Circuit Box -->
    <rect x="50" y="115" width="460" height="260" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="10"/>
    <text x="280" y="145" fill="#fbbf24" font-size="16" font-weight="700" text-anchor="middle">Bridge Converter Circuit Diagram</text>
    
    <!-- 3 Phase Supply lines -->
    <text x="70" y="185" fill="#38bdf8" font-size="13" font-weight="700">R</text>
    <text x="70" y="225" fill="#fbbf24" font-size="13" font-weight="700">Y</text>
    <text x="70" y="265" fill="#34d399" font-size="13" font-weight="700">B</text>
    <line x1="90" y1="180" x2="160" y2="180" stroke="#38bdf8" stroke-width="2"/>
    <line x1="90" y1="220" x2="160" y2="220" stroke="#fbbf24" stroke-width="2"/>
    <line x1="90" y1="260" x2="160" y2="260" stroke="#34d399" stroke-width="2"/>

    <!-- Bridge Rectifier Blocks -->
    <rect x="170" y="160" width="130" height="120" fill="#0b111e" stroke="#f59e0b" stroke-width="2" rx="8"/>
    <text x="235" y="195" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">Top: 3 SCRs</text>
    <text x="235" y="225" fill="#cbd5e1" font-size="11" text-anchor="middle">(T₁, T₃, T₅)</text>
    <text x="235" y="255" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">Bottom: 3 Diodes</text>
    <text x="235" y="272" fill="#cbd5e1" font-size="11" text-anchor="middle">(D₂, D₄, D₆)</text>

    <!-- DC Motor Load -->
    <line x1="300" y1="190" x2="380" y2="190" stroke="#38bdf8" stroke-width="2.5"/>
    <line x1="300" y1="250" x2="380" y2="250" stroke="#38bdf8" stroke-width="2.5"/>
    
    <!-- Freewheeling Diode -->
    <rect x="330" y="205" width="24" height="30" fill="#1e293b" stroke="#34d399"/>
    <text x="342" y="225" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">FD</text>

    <!-- Motor Armature -->
    <circle cx="430" cy="220" r="28" fill="#0b111e" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="430" y="226" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">DC M</text>
    <text x="430" y="280" fill="#f1f5f9" font-size="11" text-anchor="middle">R_a, L_a, E_b</text>

    <!-- Mathematical Formula & Features -->
    <rect x="530" y="115" width="380" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
    <text x="720" y="145" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">Voltage Formula &amp; Operating Features</text>
    
    <rect x="550" y="170" width="340" height="60" fill="#0b111e" stroke="#10b981" stroke-width="2" rx="6"/>
    <text x="720" y="198" fill="#34d399" font-size="15" font-weight="700" text-anchor="middle">V_dc = (3·V_ml / 2π) · (1 + cos α)</text>
    <text x="720" y="220" fill="#fbbf24" font-size="12" text-anchor="middle">V_ml = Peak Line-to-Line Voltage</text>

    <text x="560" y="260" fill="#cbd5e1" font-size="12">✔ Single-quadrant drive (Motoring only)</text>
    <text x="560" y="285" fill="#cbd5e1" font-size="12">✔ Output voltage cannot become negative</text>
    <text x="560" y="310" fill="#cbd5e1" font-size="12">✔ Higher ripple frequency than 1-phase (300 Hz)</text>
    <text x="560" y="335" fill="#cbd5e1" font-size="12">✔ Freewheeling diode prevents discontinuity</text>
    <text x="560" y="360" fill="#fbbf24" font-size="12">✔ Lower cost than full converter</text>
    """,
    "Quadrant 1 Operation Only: Forward motoring without regenerative capability due to uncontrolled diode bridge half"
)

# 8. drive-q8: single_phase_full_converter_waveforms.png
create_card_diagram(
    "images/drive/single_phase_full_converter_waveforms.png",
    "Single-Phase Full Converter Fed Separately Excited DC Motor: Waveforms",
    "Continuous Conduction Voltage: V_dc = (2·V_m / π) · cos α | Motoring (0° &lt; α &lt; 90°) &amp; Inversion (90° &lt; α &lt; 180°)",
    "#f59e0b", "DRIVE • MOD 2",
    """
    <rect x="50" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="10"/>
    <text x="255" y="145" fill="#fbbf24" font-size="16" font-weight="700" text-anchor="middle">AC Input &amp; Rectified Output Waveforms</text>
    <!-- Waveform axes -->
    <path d="M 80 230 L 430 230" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="435" y="235" fill="#94a3b8" font-size="11">ωt</text>
    
    <!-- AC Sinusoid -->
    <path d="M 90 230 Q 140 160 190 230 Q 240 300 290 230 Q 340 160 390 230" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3,3" fill="none"/>
    
    <!-- Rectified Waveform for alpha = 45 -->
    <path d="M 120 230 L 120 180 Q 155 170 190 230 L 220 250 L 220 180 Q 255 170 290 230 L 320 250 L 320 180 Q 355 170 390 230" stroke="#38bdf8" stroke-width="2.5" fill="none"/>
    <text x="120" y="250" fill="#fbbf24" font-size="12" font-weight="700">α</text>
    <text x="190" y="250" fill="#94a3b8" font-size="11">π</text>
    <text x="290" y="250" fill="#94a3b8" font-size="11">2π</text>
    <text x="255" y="325" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">V_dc = (2·V_m / π) · cos α</text>
    <text x="255" y="355" fill="#cbd5e1" font-size="12" text-anchor="middle">Inductive current keeps SCRs conducting past π</text>

    <rect x="500" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
    <text x="705" y="145" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">Two-Quadrant Converter Operation</text>
    
    <rect x="530" y="175" width="350" height="75" fill="#0b111e" stroke="#38bdf8" stroke-width="1.5" rx="6"/>
    <text x="705" y="200" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">1. Rectification Mode (0° ≤ α &lt; 90°)</text>
    <text x="705" y="222" fill="#f1f5f9" font-size="12" text-anchor="middle">V_dc &gt; 0,  I_a &gt; 0  ⟹  P &gt; 0 (Forward Motoring)</text>
    <text x="705" y="240" fill="#94a3b8" font-size="11" text-anchor="middle">Power flows from AC grid to DC motor</text>

    <rect x="530" y="265" width="350" height="75" fill="#0b111e" stroke="#f59e0b" stroke-width="1.5" rx="6"/>
    <text x="705" y="290" fill="#fbbf24" font-size="14" font-weight="700" text-anchor="middle">2. Line-Commutated Inversion (90° &lt; α &lt; 180°)</text>
    <text x="705" y="312" fill="#f1f5f9" font-size="12" text-anchor="middle">V_dc &lt; 0,  I_a &gt; 0  ⟹  P &lt; 0 (Regenerative Braking)</text>
    <text x="705" y="330" fill="#94a3b8" font-size="11" text-anchor="middle">Energy returns from motor to AC grid (E_b reversed)</text>
    """,
    "Controlled Rectification: SCRs T₁-T₂ triggered at α, T₃-T₄ triggered at π+α under continuous armature conduction"
)

# 9. drive-q8b: three_phase_full_converter.png
create_card_diagram(
    "images/drive/three_phase_full_converter.png",
    "Three-Phase Full Converter Fed Separately Excited DC Motor Drive",
    "Six-Pulse Thyristor Bridge: V_dc = (3·V_ml / π) · cos α with Ripple Frequency = 6·f = 300 Hz",
    "#f59e0b", "DRIVE • MOD 2",
    """
    <rect x="50" y="115" width="460" height="260" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="10"/>
    <text x="280" y="145" fill="#fbbf24" font-size="16" font-weight="700" text-anchor="middle">6-Pulse Thyristor Bridge (SCRs T₁ - T₆)</text>
    
    <!-- Schematic Diagram -->
    <rect x="90" y="180" width="80" height="130" fill="#0b111e" stroke="#38bdf8" stroke-width="2" rx="6"/>
    <text x="130" y="225" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">T₁, T₃, T₅</text>
    <text x="130" y="255" fill="#94a3b8" font-size="11" text-anchor="middle">(Top SCRs)</text>

    <rect x="230" y="180" width="80" height="130" fill="#0b111e" stroke="#10b981" stroke-width="2" rx="6"/>
    <text x="270" y="225" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">T₄, T₆, T₂</text>
    <text x="270" y="255" fill="#94a3b8" font-size="11" text-anchor="middle">(Bottom SCRs)</text>

    <!-- DC output terminals -->
    <line x1="310" y1="210" x2="380" y2="210" stroke="#38bdf8" stroke-width="2.5"/>
    <line x1="310" y1="280" x2="380" y2="280" stroke="#38bdf8" stroke-width="2.5"/>

    <!-- DC Motor -->
    <circle cx="420" cy="245" r="26" fill="#0b111e" stroke="#fbbf24" stroke-width="2.5"/>
    <text x="420" y="250" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">M</text>
    <text x="420" y="295" fill="#f1f5f9" font-size="11" text-anchor="middle">DC Drive</text>

    <rect x="530" y="115" width="380" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
    <text x="720" y="145" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">Analytical Formulations</text>
    
    <rect x="550" y="170" width="340" height="60" fill="#0b111e" stroke="#10b981" stroke-width="2" rx="6"/>
    <text x="720" y="198" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">V_dc = (3 · V_ml / π) · cos α</text>
    <text x="720" y="220" fill="#fbbf24" font-size="12" text-anchor="middle">Motor Speed: ω_m = (V_dc - I_a · R_a) / (K_t · Φ)</text>

    <text x="560" y="260" fill="#cbd5e1" font-size="12">✔ 6-pulse ripple at 300 Hz (Smooth armature current)</text>
    <text x="560" y="285" fill="#cbd5e1" font-size="12">✔ Very low motor torque pulsation &amp; heating</text>
    <text x="560" y="310" fill="#cbd5e1" font-size="12">✔ Two-quadrant capability (Motoring &amp; Inversion)</text>
    <text x="560" y="335" fill="#cbd5e1" font-size="12">✔ Industry workhorse for ratings &gt; 15 kW to MW</text>
    """,
    "Firing Sequence: Thyristors fired in sequence T₁ → T₂ → T₃ → T₄ → T₅ → T₆ at 60° intervals with 120° conduction duration"
)

# 10. drive-q9: class_a_chopper.png
create_card_diagram(
    "images/drive/class_a_chopper.png",
    "Motoring Control of DC Motor using Class-A Step-Down (Buck) Chopper",
    "First-Quadrant Operation (V_o &gt; 0, I_o &gt; 0): Output Voltage V_o = δ · V_dc = (T_on / T) · V_dc",
    "#f59e0b", "DRIVE • MOD 2",
    """
    <rect x="50" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="10"/>
    <text x="255" y="145" fill="#fbbf24" font-size="16" font-weight="700" text-anchor="middle">Class-A Chopper Power Circuit</text>
    
    <!-- DC Source -->
    <line x1="90" y1="200" x2="90" y2="280" stroke="#38bdf8" stroke-width="3"/>
    <line x1="80" y1="225" x2="100" y2="225" stroke="#38bdf8" stroke-width="2"/>
    <line x1="85" y1="255" x2="95" y2="255" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="245" fill="#38bdf8" font-size="14" font-weight="700">V_dc</text>

    <!-- Switch CH -->
    <line x1="90" y1="200" x2="160" y2="200" stroke="#38bdf8" stroke-width="2"/>
    <rect x="160" y="185" width="60" height="30" fill="#0b111e" stroke="#10b981" stroke-width="2" rx="4"/>
    <text x="190" y="205" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">CH1 (IGBT)</text>
    <line x1="220" y1="200" x2="310" y2="200" stroke="#38bdf8" stroke-width="2"/>

    <!-- Freewheeling Diode D_fw -->
    <line x1="260" y1="200" x2="260" y2="280" stroke="#38bdf8" stroke-width="1.5"/>
    <polygon points="260,230 250,250 270,250" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <line x1="250" y1="230" x2="270" y2="230" stroke="#f59e0b" stroke-width="2"/>
    <text x="290" y="245" fill="#fbbf24" font-size="11">D_fw</text>

    <!-- DC Motor Load -->
    <circle cx="350" cy="240" r="24" fill="#0b111e" stroke="#38bdf8" stroke-width="2"/>
    <text x="350" y="245" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">M</text>
    <line x1="310" y1="200" x2="350" y2="216" stroke="#38bdf8" stroke-width="2"/>
    <line x1="350" y1="264" x2="350" y2="280" stroke="#38bdf8" stroke-width="2"/>
    <line x1="90" y1="280" x2="350" y2="280" stroke="#38bdf8" stroke-width="2"/>
    <text x="350" y="315" fill="#f1f5f9" font-size="11" text-anchor="middle">Armature: R_a, L_a, E_b</text>

    <!-- Operation Modes -->
    <rect x="500" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
    <text x="705" y="145" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">Modes of Operation</text>
    
    <rect x="525" y="170" width="360" height="60" fill="#0b111e" stroke="#10b981" stroke-width="1.5" rx="6"/>
    <text x="705" y="195" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">Mode 1: CH1 ON (0 ≤ t &lt; T_on)</text>
    <text x="705" y="217" fill="#cbd5e1" font-size="12" text-anchor="middle">Source supplies motor: v_o = V_dc, current i_a rises</text>

    <rect x="525" y="245" width="360" height="60" fill="#0b111e" stroke="#38bdf8" stroke-width="1.5" rx="6"/>
    <text x="705" y="270" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">Mode 2: CH1 OFF (T_on ≤ t &lt; T)</text>
    <text x="705" y="292" fill="#cbd5e1" font-size="12" text-anchor="middle">Current freewheels through D_fw: v_o = 0, i_a decays</text>

    <text x="705" y="335" fill="#fbbf24" font-size="14" font-weight="700" text-anchor="middle">Average Voltage: V_o = δ · V_dc = (T_on / T) · V_dc</text>
    <text x="705" y="358" fill="#94a3b8" font-size="11" text-anchor="middle">Speed control achieved smoothly by varying duty cycle δ (0 to 1)</text>
    """,
    "First Quadrant Motoring: Output voltage and armature current are always positive (forward motoring acceleration)"
)

# 11. drive-q9b: class_b_chopper.png
create_card_diagram(
    "images/drive/class_b_chopper.png",
    "Regenerative Braking Control of DC Motor using Class-B Step-Up (Boost) Chopper",
    "Second-Quadrant Operation (V_o &gt; 0, I_o &lt; 0): Energy Flows from Motor Back to DC Bus",
    "#f59e0b", "DRIVE • MOD 2",
    """
    <rect x="50" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="10"/>
    <text x="255" y="145" fill="#fbbf24" font-size="16" font-weight="700" text-anchor="middle">Class-B Boost Chopper Circuit</text>
    
    <!-- DC Bus -->
    <line x1="90" y1="180" x2="90" y2="300" stroke="#38bdf8" stroke-width="3"/>
    <text x="65" y="245" fill="#38bdf8" font-size="14" font-weight="700">V_dc</text>

    <!-- Diode D2 to Source -->
    <line x1="90" y1="190" x2="220" y2="190" stroke="#38bdf8" stroke-width="2"/>
    <polygon points="170,190 150,180 150,200" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <line x1="170" y1="180" x2="170" y2="200" stroke="#10b981" stroke-width="2"/>
    <text x="160" y="170" fill="#34d399" font-size="11" font-weight="700">D2</text>

    <!-- Switch CH2 in parallel -->
    <rect x="220" y="215" width="50" height="40" fill="#0b111e" stroke="#ef4444" stroke-width="2" rx="4"/>
    <text x="245" y="240" fill="#f87171" font-size="12" font-weight="700" text-anchor="middle">CH2</text>
    <line x1="245" y1="190" x2="245" y2="215" stroke="#38bdf8" stroke-width="2"/>
    <line x1="245" y1="255" x2="245" y2="290" stroke="#38bdf8" stroke-width="2"/>

    <!-- Inductor L and Motor Generator -->
    <line x1="245" y1="190" x2="320" y2="190" stroke="#38bdf8" stroke-width="2"/>
    <text x="290" y="180" fill="#fbbf24" font-size="12" font-weight="700">L_a</text>
    
    <!-- Motor generating E_b -->
    <circle cx="360" cy="240" r="24" fill="#0b111e" stroke="#fbbf24" stroke-width="2"/>
    <text x="360" y="245" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle">Gen E_b</text>
    <line x1="320" y1="190" x2="360" y2="216" stroke="#38bdf8" stroke-width="2"/>
    <line x1="360" y1="264" x2="360" y2="290" stroke="#38bdf8" stroke-width="2"/>
    <line x1="90" y1="290" x2="360" y2="290" stroke="#38bdf8" stroke-width="2"/>

    <rect x="500" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
    <text x="705" y="145" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">Step-Up Energy Transfer Principle</text>
    
    <rect x="525" y="170" width="360" height="60" fill="#0b111e" stroke="#ef4444" stroke-width="1.5" rx="6"/>
    <text x="705" y="195" fill="#f87171" font-size="14" font-weight="700" text-anchor="middle">Step 1: CH2 ON (Energy Storage)</text>
    <text x="705" y="217" fill="#cbd5e1" font-size="12" text-anchor="middle">E_b shorted through L_a: Inductor stores energy (1/2 L i²)</text>

    <rect x="525" y="245" width="360" height="60" fill="#0b111e" stroke="#10b981" stroke-width="1.5" rx="6"/>
    <text x="705" y="270" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">Step 2: CH2 OFF (Energy Feedback)</text>
    <text x="705" y="292" fill="#cbd5e1" font-size="12" text-anchor="middle">L_a voltage boosts E_b: (E_b + L di/dt) &gt; V_dc, feeds D2 into bus</text>

    <text x="705" y="335" fill="#fbbf24" font-size="14" font-weight="700" text-anchor="middle">Regenerates Even at Low Motor Speeds (E_b &lt; V_dc)</text>
    <text x="705" y="358" fill="#94a3b8" font-size="11" text-anchor="middle">Essential for electric vehicles and industrial cranes/elevators</text>
    """,
    "Quadrant 2 Regenerative Braking: Kinetic energy of load is converted to electrical energy and fed back to the power supply"
)

# 12. drive-q10: class_c_chopper_drive.png
create_card_diagram(
    "images/drive/class_c_chopper_drive.png",
    "Two-Quadrant Class-C Chopper Fed DC Motor Drive",
    "Bidirectional Power Flow: Quadrant 1 (Forward Motoring) and Quadrant 2 (Regenerative Braking)",
    "#f59e0b", "DRIVE • MOD 2",
    """
    <rect x="50" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="10"/>
    <text x="255" y="145" fill="#fbbf24" font-size="16" font-weight="700" text-anchor="middle">Half-Bridge Class-C Topology</text>
    
    <!-- Top Leg: CH1 and D1 -->
    <rect x="150" y="180" width="70" height="35" fill="#0b111e" stroke="#10b981" stroke-width="2" rx="4"/>
    <text x="185" y="202" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">CH1</text>
    <rect x="230" y="180" width="40" height="35" fill="#1e293b" stroke="#38bdf8" rx="4"/>
    <text x="250" y="202" fill="#38bdf8" font-size="11" text-anchor="middle">D1</text>

    <!-- Bottom Leg: CH2 and D2 -->
    <rect x="150" y="245" width="70" height="35" fill="#0b111e" stroke="#ef4444" stroke-width="2" rx="4"/>
    <text x="185" y="267" fill="#f87171" font-size="13" font-weight="700" text-anchor="middle">CH2</text>
    <rect x="230" y="245" width="40" height="35" fill="#1e293b" stroke="#f59e0b" rx="4"/>
    <text x="250" y="267" fill="#fbbf24" font-size="11" text-anchor="middle">D2</text>

    <!-- Motor between legs -->
    <line x1="280" y1="230" x2="330" y2="230" stroke="#38bdf8" stroke-width="2.5"/>
    <circle cx="360" cy="230" r="26" fill="#0b111e" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="360" y="235" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">DC M</text>
    <text x="255" y="325" fill="#f1f5f9" font-size="13" font-weight="700" text-anchor="middle">V_o = δ · V_dc (Always Positive)</text>
    <text x="255" y="350" fill="#cbd5e1" font-size="11" text-anchor="middle">Current i_a can flow in either direction (+ or -)</text>

    <rect x="500" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="10"/>
    <text x="705" y="145" fill="#38bdf8" font-size="16" font-weight="700" text-anchor="middle">Quadrant Plane &amp; Switching Logic</text>
    
    <!-- Quadrant Graph -->
    <line x1="560" y1="240" x2="850" y2="240" stroke="#94a3b8" stroke-width="1.5"/>
    <line x1="705" y1="170" x2="705" y2="330" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="850" y="235" fill="#94a3b8" font-size="11">Current i_a</text>
    <text x="715" y="175" fill="#94a3b8" font-size="11">Voltage v_o</text>

    <!-- Q1 and Q2 highlight -->
    <rect x="710" y="180" width="120" height="55" fill="#10b98122" stroke="#10b981" rx="4"/>
    <text x="770" y="205" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">QUADRANT 1</text>
    <text x="770" y="225" fill="#f1f5f9" font-size="11" text-anchor="middle">CH1 + D2 (Motoring)</text>

    <rect x="580" y="180" width="120" height="55" fill="#f59e0b22" stroke="#f59e0b" rx="4"/>
    <text x="640" y="205" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle">QUADRANT 2</text>
    <text x="640" y="225" fill="#f1f5f9" font-size="11" text-anchor="middle">CH2 + D1 (Braking)</text>

    <text x="705" y="320" fill="#cbd5e1" font-size="12" text-anchor="middle">Zero-Deadtime PWM prevents shoot-through fault</text>
    <text x="705" y="345" fill="#38bdf8" font-size="11" text-anchor="middle">Seamless transitions between motoring and regenerative braking</text>
    """,
    "Class-C chopper combines Class-A and Class-B choppers in parallel to provide two-quadrant operation"
)

# 13. drive-q10b: class_e_chopper.png
create_card_diagram(
    "images/drive/class_e_chopper.png",
    "Four-Quadrant Class-E Chopper Fed DC Motor Drive (H-Bridge)",
    "Complete Speed &amp; Torque Reversal: Forward Motoring, Forward Braking, Reverse Motoring, Reverse Braking",
    "#f59e0b", "DRIVE • MOD 2",
    """
    <rect x="50" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="10"/>
    <text x="255" y="145" fill="#fbbf24" font-size="16" font-weight="700" text-anchor="middle">Full-Bridge H-Configuration</text>
    
    <!-- 4 Switches of H-Bridge -->
    <rect x="110" y="175" width="60" height="35" fill="#0b111e" stroke="#38bdf8" stroke-width="1.5" rx="4"/>
    <text x="140" y="198" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">CH1</text>

    <rect x="330" y="175" width="60" height="35" fill="#0b111e" stroke="#38bdf8" stroke-width="1.5" rx="4"/>
    <text x="360" y="198" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">CH3</text>

    <rect x="110" y="260" width="60" height="35" fill="#0b111e" stroke="#10b981" stroke-width="1.5" rx="4"/>
    <text x="140" y="283" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">CH2</text>

    <rect x="330" y="260" width="60" height="35" fill="#0b111e" stroke="#10b981" stroke-width="1.5" rx="4"/>
    <text x="360" y="283" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">CH4</text>

    <!-- Center DC Motor -->
    <circle cx="250" cy="235" r="26" fill="#0b111e" stroke="#fbbf24" stroke-width="2.5"/>
    <text x="250" y="240" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">M</text>
    <line x1="170" y1="235" x2="224" y2="235" stroke="#f1f5f9" stroke-width="2"/>
    <line x1="276" y1="235" x2="330" y2="235" stroke="#f1f5f9" stroke-width="2"/>

    <text x="255" y="335" fill="#cbd5e1" font-size="12" text-anchor="middle">Bipolar Output: -V_dc ≤ V_o ≤ +V_dc</text>
    <text x="255" y="358" fill="#cbd5e1" font-size="12" text-anchor="middle">Bidirectional Current: -I_max ≤ I_o ≤ +I_max</text>

    <rect x="500" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
    <text x="705" y="145" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">4-Quadrant Operational Modes</text>
    
    <text x="530" y="185" fill="#38bdf8" font-size="13" font-weight="700">Q1: Forward Motoring (+V, +I)</text>
    <text x="760" y="185" fill="#cbd5e1" font-size="12">CH1 ON, CH4 modulated</text>

    <text x="530" y="225" fill="#34d399" font-size="13" font-weight="700">Q2: Forward Braking (+V, -I)</text>
    <text x="760" y="225" fill="#cbd5e1" font-size="12">CH2 modulated, D1, D4 feed bus</text>

    <text x="530" y="265" fill="#fbbf24" font-size="13" font-weight="700">Q3: Reverse Motoring (-V, -I)</text>
    <text x="760" y="265" fill="#cbd5e1" font-size="12">CH3 ON, CH2 modulated</text>

    <text x="530" y="305" fill="#f87171" font-size="13" font-weight="700">Q4: Reverse Braking (-V, +I)</text>
    <text x="760" y="305" fill="#cbd5e1" font-size="12">CH4 modulated, D2, D3 feed bus</text>

    <text x="705" y="350" fill="#38bdf8" font-size="11" font-weight="600" text-anchor="middle">Standard for robotic servo drives, rolling mills, and reversible traction</text>
    """,
    "Class-E Chopper: Provides full 4-quadrant motion without requiring mechanical contactors for armature reversal"
)

# 14. drive-q11: closed_loop_dc_drive_block_diagram.png
create_card_diagram(
    "images/drive/closed_loop_dc_drive_block_diagram.png",
    "Closed-Loop Speed Control of DC Drive with Inner Current Control Loop",
    "Cascaded Control Architecture: Outer Speed PI Controller + Inner Current PI Controller with Limiter",
    "#f59e0b", "DRIVE • MOD 2",
    """
    <!-- Reference Speed -->
    <path d="M 50 200 L 110 200" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>
    <text x="65" y="185" fill="#38bdf8" font-size="13" font-weight="700">ω_ref</text>

    <!-- Outer Speed Comparator -->
    <circle cx="125" cy="200" r="15" fill="#0b111e" stroke="#38bdf8" stroke-width="2"/>
    <text x="125" y="206" fill="#38bdf8" font-size="18" font-weight="700" text-anchor="middle">Σ</text>

    <path d="M 140 200 L 180 200" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>

    <!-- Speed Controller (PI) -->
    <rect x="180" y="175" width="110" height="50" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="2" rx="6"/>
    <text x="235" y="200" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">Speed PI</text>
    <text x="235" y="215" fill="#94a3b8" font-size="10" text-anchor="middle">Controller</text>

    <!-- Current Limiter -->
    <path d="M 290 200 L 320 200" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>
    <rect x="320" y="175" width="70" height="50" fill="#0b111e" stroke="#ef4444" stroke-width="2" rx="6"/>
    <text x="355" y="200" fill="#f87171" font-size="11" font-weight="700" text-anchor="middle">Current</text>
    <text x="355" y="215" fill="#f87171" font-size="11" font-weight="700" text-anchor="middle">Limiter</text>

    <path d="M 390 200 L 440 200" stroke="#f59e0b" stroke-width="2.5" marker-end="url(#arrow)"/>
    <text x="415" y="185" fill="#fbbf24" font-size="12" font-weight="700">I_ref</text>

    <!-- Inner Current Comparator -->
    <circle cx="455" cy="200" r="15" fill="#0b111e" stroke="#f59e0b" stroke-width="2"/>
    <text x="455" y="206" fill="#fbbf24" font-size="18" font-weight="700" text-anchor="middle">Σ</text>

    <path d="M 470 200 L 510 200" stroke="#f59e0b" stroke-width="2.5" marker-end="url(#arrow)"/>

    <!-- Current Controller (PI) -->
    <rect x="510" y="175" width="100" height="50" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="2" rx="6"/>
    <text x="560" y="200" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">Current PI</text>
    <text x="560" y="215" fill="#94a3b8" font-size="10" text-anchor="middle">Controller</text>

    <path d="M 610 200 L 650 200" stroke="#10b981" stroke-width="2.5" marker-end="url(#arrow-green)"/>
    <text x="630" y="185" fill="#34d399" font-size="11">Firing α</text>

    <!-- Power Converter & Motor -->
    <rect x="650" y="170" width="110" height="60" fill="url(#boxGrad)" stroke="#10b981" stroke-width="2" rx="8"/>
    <text x="705" y="195" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">Converter</text>
    <text x="705" y="215" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">&amp; DC Motor</text>

    <path d="M 760 200 L 890 200" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)"/>
    <text x="830" y="185" fill="#38bdf8" font-size="14" font-weight="700">Speed ω</text>

    <!-- Inner Current Feedback Loop -->
    <path d="M 720 230 L 720 280 L 455 280 L 455 215" stroke="#f59e0b" stroke-width="2" marker-end="url(#arrow)"/>
    <rect x="560" y="265" width="80" height="30" fill="#0b111e" stroke="#f59e0b" rx="4"/>
    <text x="600" y="285" fill="#fbbf24" font-size="11" text-anchor="middle">Current Sensor</text>

    <!-- Outer Speed Feedback Loop -->
    <path d="M 830 200 L 830 330 L 125 330 L 125 215" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>
    <rect x="420" y="315" width="120" height="30" fill="#0b111e" stroke="#38bdf8" rx="4"/>
    <text x="480" y="335" fill="#38bdf8" font-size="11" text-anchor="middle">Tachometer / Encoder</text>

    <text x="480" y="380" fill="#f1f5f9" font-size="12" text-anchor="middle">Current limiter clamps I_ref to 150-200% rated to prevent SCR damage during acceleration</text>
    """,
    "Cascaded Control Philosophy: Fast inner current loop (&lt;5 ms) protects hardware; Outer speed loop (&gt;50 ms) ensures precise tracking"
)

# 15. drive-q12: stator_voltage_characteristics.png
create_card_diagram(
    "images/drive/stator_voltage_characteristics.png",
    "Stator Voltage Speed Control of Induction Motors: Torque-Speed Curves",
    "Torque Drops with Square of Voltage: T ∝ V_s² | Narrow Speed Range and Excessive Rotor Heating",
    "#f59e0b", "DRIVE • MOD 3",
    """
    <rect x="50" y="115" width="450" height="260" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="10"/>
    <text x="275" y="145" fill="#fbbf24" font-size="16" font-weight="700" text-anchor="middle">Torque-Speed Family for Varying V_s</text>
    <path d="M 90 330 L 460 330" stroke="#94a3b8" stroke-width="1.5"/>
    <path d="M 90 330 L 90 170" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="470" y="335" fill="#94a3b8" font-size="11">ω_m</text>
    <text x="70" y="250" fill="#94a3b8" font-size="11" transform="rotate(-90 70 250)">Torque T</text>

    <!-- Rated Voltage Curve V1 -->
    <path d="M 90 270 Q 220 160 440 330" stroke="#10b981" stroke-width="3" fill="none"/>
    <text x="240" y="180" fill="#34d399" font-size="12" font-weight="700">V_s = 1.0 V_rated</text>

    <!-- Reduced Voltage Curve V2 = 0.8 -->
    <path d="M 90 295 Q 220 220 440 330" stroke="#38bdf8" stroke-width="2.5" fill="none"/>
    <text x="240" y="235" fill="#38bdf8" font-size="12" font-weight="700">V_s = 0.8 V_rated</text>

    <!-- Reduced Voltage Curve V3 = 0.6 -->
    <path d="M 90 315 Q 220 270 440 330" stroke="#ef4444" stroke-width="2" fill="none"/>
    <text x="240" y="280" fill="#f87171" font-size="12" font-weight="700">V_s = 0.6 V_rated</text>

    <!-- Synchronous Speed line -->
    <line x1="440" y1="170" x2="440" y2="330" stroke="#94a3b8" stroke-dasharray="3,3"/>
    <text x="440" y="350" fill="#fbbf24" font-size="11" text-anchor="middle">ω_s</text>

    <!-- Fan Load Curve T_l ∝ ω² -->
    <path d="M 90 330 Q 300 325 440 240" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="4,4" fill="none"/>
    <text x="370" y="270" fill="#fbbf24" font-size="11" font-weight="700">Fan Load T_l ∝ ω²</text>

    <rect x="520" y="115" width="390" height="260" fill="url(#boxGrad)" stroke="#ef4444" stroke-width="1.5" rx="10"/>
    <text x="715" y="145" fill="#f87171" font-size="16" font-weight="700" text-anchor="middle">Inherent Technical Limitations</text>
    
    <text x="545" y="185" fill="#f87171" font-size="13" font-weight="700">1. Severe Torque Derating:</text>
    <text x="545" y="205" fill="#cbd5e1" font-size="12">Peak breakdown torque T_max ∝ V_s²; drops 64% at 0.6 V</text>

    <text x="545" y="240" fill="#fbbf24" font-size="13" font-weight="700">2. High Rotor Power Dissipation:</text>
    <text x="545" y="260" fill="#cbd5e1" font-size="12">Rotor copper loss P_cr = s · P_ag; increases dramatically at high slip</text>

    <text x="545" y="295" fill="#38bdf8" font-size="13" font-weight="700">3. Narrow Stable Speed Range:</text>
    <text x="545" y="315" fill="#cbd5e1" font-size="12">Stable only from s = 0 to s_maxT; impossible with constant torque loads</text>

    <text x="715" y="355" fill="#34d399" font-size="12" font-weight="600" text-anchor="middle">Only suitable for small centrifugal fans, blowers, and appliance pumps</text>
    """,
    "Maximum Slip Invariance: Slip at maximum torque s_mT = R₂'/X₂' remains independent of stator voltage V_s"
)

# 16. drive-q12b: vsi_vs_csi_drive.png
create_card_diagram(
    "images/drive/vsi_vs_csi_drive.png",
    "Comparison of Inverter Architectures: Voltage Source (VSI) vs Current Source (CSI)",
    "DC Link Filter (Capacitor vs Inductor), Commutation, Regeneration, and Output Waveforms",
    "#f59e0b", "DRIVE • MOD 3",
    """
    <rect x="50" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="10"/>
    <text x="255" y="145" fill="#38bdf8" font-size="16" font-weight="700" text-anchor="middle">Voltage Source Inverter (VSI)</text>
    
    <rect x="80" y="170" width="350" height="40" fill="#0b111e" stroke="#38bdf8" rx="6"/>
    <text x="255" y="195" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">DC Link: Large Parallel Capacitor C</text>

    <text x="70" y="235" fill="#cbd5e1" font-size="12">✔ Low internal impedance; acts as constant voltage source</text>
    <text x="70" y="260" fill="#cbd5e1" font-size="12">✔ Output: Stepped/PWM voltage, sinusoidal current</text>
    <text x="70" y="285" fill="#cbd5e1" font-size="12">✔ Uses self-commutated devices (IGBTs with anti-parallel diodes)</text>
    <text x="70" y="310" fill="#cbd5e1" font-size="12">✔ Regeneration requires back-to-back active front end (AFE)</text>
    <text x="70" y="335" fill="#34d399" font-size="12">✔ High dynamic performance (PWM up to 20 kHz)</text>
    <text x="70" y="360" fill="#fbbf24" font-size="11">Standard for &gt;95% of modern industrial AC drives</text>

    <rect x="500" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
    <text x="705" y="145" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">Current Source Inverter (CSI)</text>
    
    <rect x="530" y="170" width="350" height="40" fill="#0b111e" stroke="#10b981" rx="6"/>
    <text x="705" y="195" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">DC Link: Large Series Inductor L_dc</text>

    <text x="520" y="235" fill="#cbd5e1" font-size="12">✔ High internal impedance; acts as constant current source</text>
    <text x="520" y="260" fill="#cbd5e1" font-size="12">✔ Output: Six-step current, sinusoidal voltage via capacitors</text>
    <text x="520" y="285" fill="#cbd5e1" font-size="12">✔ Uses Thyristors (SCRs/GTOs/IGCTs) with reverse blocking</text>
    <text x="520" y="310" fill="#cbd5e1" font-size="12">✔ Inherent regeneration by simply reversing DC link voltage polarity</text>
    <text x="520" y="335" fill="#34d399" font-size="12">✔ Extreme short-circuit ride-through capability</text>
    <text x="520" y="360" fill="#fbbf24" font-size="11">Preferred for multi-megawatt high voltage drives (e.g. pumps, mills)</text>
    """,
    "DC Link Filter Comparison: VSI capacitor clamps DC bus voltage; CSI inductor maintains constant ripple-free DC link current"
)

# 17. drive-q13: v_f_control_characteristics.png
create_card_diagram(
    "images/drive/v_f_control_characteristics.png",
    "Comprehensive Constant V/f Speed Control of Induction Motors",
    "Stator Flux Maintenance: Φ_m ≈ V_s / f_s = Constant | Voltage Boost at Low Frequency &amp; Field Weakening",
    "#f59e0b", "DRIVE • MOD 3",
    """
    <rect x="50" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="10"/>
    <text x="255" y="145" fill="#fbbf24" font-size="16" font-weight="700" text-anchor="middle">V/f Operational Profile</text>
    <path d="M 90 330 L 420 330" stroke="#94a3b8" stroke-width="1.5"/>
    <path d="M 90 330 L 90 170" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="270" y="355" fill="#f1f5f9" font-size="12" text-anchor="middle">Stator Frequency f_s (Hz)</text>
    <text x="70" y="250" fill="#f1f5f9" font-size="12" transform="rotate(-90 70 250)" text-anchor="middle">Stator Voltage V_s (V)</text>

    <!-- Low frequency boost -->
    <path d="M 90 300 L 140 280 L 320 180 L 410 180" stroke="#38bdf8" stroke-width="3" fill="none"/>
    <line x1="320" y1="170" x2="320" y2="330" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="3,3"/>
    <text x="320" y="348" fill="#fbbf24" font-size="11" text-anchor="middle">f_rated (50 Hz)</text>
    <text x="410" y="175" fill="#38bdf8" font-size="11" font-weight="700">V_rated</text>

    <text x="125" y="315" fill="#f87171" font-size="11">V_boost</text>
    <text x="220" y="225" fill="#34d399" font-size="12" font-weight="700">Constant V/f Slope</text>
    <text x="365" y="210" fill="#fbbf24" font-size="11" font-weight="700">Field Weakening</text>

    <rect x="500" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
    <text x="705" y="145" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">Governing Principles &amp; Derivation</text>
    
    <text x="525" y="180" fill="#f1f5f9" font-size="13">Air-gap Induced EMF: E_g = 4.44 · f_s · N_ph · K_w · Φ_m</text>
    <text x="525" y="210" fill="#38bdf8" font-size="13" font-weight="700">Flux: Φ_m ≈ (V_s - I_s·R_s) / (4.44 · f_s · N_ph · K_w)</text>
    
    <rect x="525" y="230" width="360" height="50" fill="#0b111e" stroke="#10b981" stroke-width="2" rx="6"/>
    <text x="705" y="260" fill="#34d399" font-size="15" font-weight="700" text-anchor="middle">V_s / f_s = Constant  ⟹  Φ_m = Rated Flux</text>

    <text x="525" y="305" fill="#cbd5e1" font-size="12">✔ T_max remains constant across all speeds below f_rated</text>
    <text x="525" y="328" fill="#cbd5e1" font-size="12">✔ Stator resistance drop I_s·R_s dominates at low f_s (needs V_boost)</text>
    <text x="525" y="352" fill="#fbbf24" font-size="12">✔ Above 50 Hz: V_s clamped at rated; flux drops (T_max ∝ 1/f²)</text>
    """,
    "Scalar Control Rule: Maintaining constant V/f ratio preserves magnetic core flux density at its optimum rated saturation limit"
)

# 18. drive-q14: static_rotor_resistance_circuit.png
create_card_diagram(
    "images/drive/static_rotor_resistance_circuit.png",
    "Static Rotor Resistance Speed Control of Wound-Rotor Induction Motor",
    "Chopper-Controlled External Resistor: Effective Resistance R_eff = R_ext · (1 - δ) with Smooth Stepless Variation",
    "#f59e0b", "DRIVE • MOD 3",
    """
    <rect x="50" y="115" width="460" height="260" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="10"/>
    <text x="280" y="145" fill="#fbbf24" font-size="16" font-weight="700" text-anchor="middle">Slip-Ring Chopper Resistance Circuit</text>
    
    <!-- Wound rotor slip rings -->
    <circle cx="100" cy="220" r="28" fill="#0b111e" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="100" y="226" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">Rotor</text>
    <text x="100" y="265" fill="#94a3b8" font-size="10" text-anchor="middle">Slip Rings</text>

    <!-- 3-phase lines to Diode Bridge -->
    <line x1="128" y1="210" x2="190" y2="210" stroke="#38bdf8" stroke-width="2"/>
    <line x1="128" y1="220" x2="190" y2="220" stroke="#38bdf8" stroke-width="2"/>
    <line x1="128" y1="230" x2="190" y2="230" stroke="#38bdf8" stroke-width="2"/>

    <!-- 3 Phase Diode Rectifier -->
    <rect x="190" y="195" width="90" height="60" fill="#0b111e" stroke="#fbbf24" stroke-width="2" rx="6"/>
    <text x="235" y="225" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle">3-Phase</text>
    <text x="235" y="242" fill="#cbd5e1" font-size="11" text-anchor="middle">Rectifier</text>

    <!-- Smoothing Inductor L_d -->
    <line x1="280" y1="210" x2="330" y2="210" stroke="#38bdf8" stroke-width="2"/>
    <text x="305" y="200" fill="#34d399" font-size="12" font-weight="700">L_d</text>

    <!-- Chopper Switch and Resistor R -->
    <line x1="330" y1="210" x2="380" y2="210" stroke="#38bdf8" stroke-width="2"/>
    <rect x="350" y="235" width="40" height="30" fill="#0b111e" stroke="#ef4444" rx="4"/>
    <text x="370" y="255" fill="#f87171" font-size="11" font-weight="700" text-anchor="middle">GTO</text>
    
    <rect x="420" y="215" width="30" height="50" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <text x="435" y="245" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">R</text>

    <line x1="380" y1="210" x2="435" y2="210" stroke="#38bdf8" stroke-width="2"/>
    <line x1="435" y1="265" x2="435" y2="280" stroke="#38bdf8" stroke-width="2"/>
    <line x1="280" y1="240" x2="435" y2="280" stroke="#38bdf8" stroke-width="2"/>

    <!-- Operational Formulations -->
    <rect x="530" y="115" width="380" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
    <text x="720" y="145" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">Chopper Resistance Control Analysis</text>
    
    <rect x="550" y="170" width="340" height="55" fill="#0b111e" stroke="#10b981" stroke-width="2" rx="6"/>
    <text x="720" y="195" fill="#34d399" font-size="15" font-weight="700" text-anchor="middle">R_eff = R_ext · (1 - δ)</text>
    <text x="720" y="215" fill="#fbbf24" font-size="12" text-anchor="middle">Duty Cycle δ = T_on / T (Varies 0 to 1)</text>

    <text x="560" y="255" fill="#cbd5e1" font-size="12">When Chopper OFF (δ = 0): R_eff = R_ext (High Resistance)</text>
    <text x="560" y="280" fill="#cbd5e1" font-size="12">When Chopper ON (δ = 1): R_eff = 0 (External Resistor Shorted)</text>
    <text x="560" y="310" fill="#38bdf8" font-size="12">✔ Stepless, contactless resistance modulation</text>
    <text x="560" y="335" fill="#38bdf8" font-size="12">✔ Balanced three-phase rotor currents (No unbalance)</text>
    <text x="560" y="360" fill="#fbbf24" font-size="11">Drawback: Slip power s·P_ag is still dissipated as heat in R</text>
    """,
    "Effective Rotor Resistance per Phase: R_2,eff = R_2 + 0.5 · R_eff, enabling smooth speed control down to 50% rated"
)

# 19. drive-q14b: slip_power_recovery.png
create_card_diagram(
    "images/drive/slip_power_recovery.png",
    "Slip Power Recovery: Static Kramer (Subsynchronous) vs Static Scherbius (Bidirectional)",
    "Recovery of Rotor Slip Power s·P_ag Back into the AC Grid to Achieve High Energy Efficiency",
    "#f59e0b", "DRIVE • MOD 3",
    """
    <rect x="50" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="10"/>
    <text x="255" y="145" fill="#fbbf24" font-size="16" font-weight="700" text-anchor="middle">1. Static Kramer System (Unidirectional)</text>
    
    <!-- Flow: Rotor -> Diode Bridge -> Inverter -> Transformer -> AC Supply -->
    <rect x="80" y="175" width="80" height="45" fill="#0b111e" stroke="#38bdf8" rx="6"/>
    <text x="120" y="202" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">Rotor</text>
    <path d="M 160 197 L 195 197" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>

    <rect x="200" y="175" width="90" height="45" fill="#0b111e" stroke="#fbbf24" rx="6"/>
    <text x="245" y="195" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">Diode Bridge</text>
    <text x="245" y="210" fill="#cbd5e1" font-size="10" text-anchor="middle">(Rectifier)</text>
    <path d="M 290 197 L 325 197" stroke="#fbbf24" stroke-width="2" marker-end="url(#arrow)"/>

    <rect x="330" y="175" width="100" height="45" fill="#0b111e" stroke="#10b981" rx="6"/>
    <text x="380" y="195" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">SCR Inverter</text>
    <text x="380" y="210" fill="#cbd5e1" font-size="10" text-anchor="middle">(90° &lt; α &lt; 180°)</text>

    <!-- Feedback arrow to Grid -->
    <path d="M 380 220 L 380 270 L 120 270 L 120 220" stroke="#10b981" stroke-width="2" marker-end="url(#arrow-green)"/>
    <text x="250" y="290" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">Slip Power s·P_ag Fed to AC Grid</text>
    <text x="255" y="335" fill="#cbd5e1" font-size="12" text-anchor="middle">Subsynchronous Speeds Only (0 ≤ N ≤ N_s)</text>
    <text x="255" y="358" fill="#94a3b8" font-size="11" text-anchor="middle">Diode bridge prevents reverse power flow</text>

    <rect x="500" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
    <text x="705" y="145" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">2. Static Scherbius System (Bidirectional)</text>
    
    <rect x="530" y="175" width="160" height="50" fill="#0b111e" stroke="#10b981" stroke-width="2" rx="6"/>
    <text x="610" y="198" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">Dual Active Converters</text>
    <text x="610" y="214" fill="#cbd5e1" font-size="10" text-anchor="middle">(Back-to-Back VSI / Cyclo)</text>

    <path d="M 690 200 L 730 200" stroke="#10b981" stroke-width="3"/>
    <path d="M 730 200 L 690 200" stroke="#f59e0b" stroke-width="3"/>

    <rect x="735" y="175" width="150" height="50" fill="#0b111e" stroke="#38bdf8" stroke-width="2" rx="6"/>
    <text x="810" y="198" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">AC Grid Transformer</text>
    <text x="810" y="214" fill="#cbd5e1" font-size="10" text-anchor="middle">(Three-Phase 50 Hz)</text>

    <text x="705" y="260" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">Subsynchronous &amp; Supersynchronous Speeds</text>
    <text x="530" y="295" fill="#cbd5e1" font-size="12">Subsynchronous (N &lt; N_s): Rotor feeds slip power to grid</text>
    <text x="530" y="320" fill="#cbd5e1" font-size="12">Supersynchronous (N &gt; N_s): Grid injects power into rotor</text>
    <text x="705" y="355" fill="#fbbf24" font-size="12" font-weight="600" text-anchor="middle">Foundational for Doubly-Fed Induction Generators (DFIG) in Wind Turbines</text>
    """,
    "Converter Sizing Efficiency: Converter rating is only a fraction s_max · P_rated of total motor power, dramatically cutting drive cost"
)

# 20. drive-q15: synchronous_drive_modes.png
create_card_diagram(
    "images/drive/synchronous_drive_modes.png",
    "Synchronous Motor Drives: True Synchronous vs Self-Controlled Mode",
    "Open-Loop Frequency Stepping (Hunting/Pull-Out Risk) vs Closed-Loop Rotor Position Inverter Gating",
    "#f59e0b", "DRIVE • MOD 4",
    """
    <rect x="50" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="10"/>
    <text x="255" y="145" fill="#fbbf24" font-size="16" font-weight="700" text-anchor="middle">1. True Synchronous Mode (Open-Loop)</text>
    
    <rect x="80" y="175" width="160" height="50" fill="#0b111e" stroke="#38bdf8" rx="6"/>
    <text x="160" y="198" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">Independent Clock</text>
    <text x="160" y="214" fill="#cbd5e1" font-size="11" text-anchor="middle">Oscillator / VFD</text>

    <path d="M 240 200 L 290 200" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>

    <rect x="290" y="175" width="140" height="50" fill="#0b111e" stroke="#fbbf24" rx="6"/>
    <text x="360" y="198" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">Synchronous</text>
    <text x="360" y="214" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">Motor</text>

    <text x="70" y="260" fill="#f87171" font-size="12">✘ Rotor must follow stator rotating magnetic field externally</text>
    <text x="70" y="285" fill="#f87171" font-size="12">✘ Sudden load torque shock causes hunting or loss of synchronism</text>
    <text x="70" y="310" fill="#f87171" font-size="12">✘ Requires damper (amortisseur) windings for starting</text>
    <text x="70" y="335" fill="#cbd5e1" font-size="12">✘ Slow ramp acceleration rate (cannot accelerate instantly)</text>
    <text x="255" y="360" fill="#94a3b8" font-size="11" text-anchor="middle">Used for multi-motor conveyor synchronization</text>

    <rect x="500" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
    <text x="705" y="145" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">2. Self-Controlled Mode (Brushless DC)</text>
    
    <rect x="530" y="175" width="130" height="50" fill="#0b111e" stroke="#10b981" rx="6"/>
    <text x="595" y="198" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">Position Sensor</text>
    <text x="595" y="214" fill="#cbd5e1" font-size="10" text-anchor="middle">(Resolver / Encoder)</text>

    <path d="M 660 200 L 710 200" stroke="#10b981" stroke-width="2.5" marker-end="url(#arrow-green)"/>

    <rect x="710" y="175" width="160" height="50" fill="#0b111e" stroke="#38bdf8" rx="6"/>
    <text x="790" y="198" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">Inverter Gate Driver</text>
    <text x="790" y="214" fill="#cbd5e1" font-size="10" text-anchor="middle">Stator Switching</text>

    <text x="520" y="260" fill="#34d399" font-size="12">✔ Stator field frequency is locked to actual rotor shaft position</text>
    <text x="520" y="285" fill="#34d399" font-size="12">✔ Rotor CANNOT fall out of step (Pull-out completely eliminated)</text>
    <text x="520" y="310" fill="#34d399" font-size="12">✔ Operates with high torque-to-inertia ratio like a DC machine</text>
    <text x="520" y="335" fill="#34d399" font-size="12">✔ Known as Electronic Commutation (BLDC / PMSM)</text>
    <text x="705" y="360" fill="#fbbf24" font-size="11" text-anchor="middle">Ideal for high-performance electric vehicles and industrial robotics</text>
    """,
    "Self-Controlled Operation Principle: Inverter firing signals are derived directly from rotor shaft position, making the motor self-synchronizing"
)

# 21. drive-q15b: lci_synchronous_drive.png
create_card_diagram(
    "images/drive/lci_synchronous_drive.png",
    "Load-Commutated Inverter (LCI) Fed Synchronous Motor Drive",
    "Natural Commutation via Motor Overexcitation (Leading Power Factor): Machine-Induced Back-EMF Turns Off SCRs",
    "#f59e0b", "DRIVE • MOD 4",
    """
    <rect x="50" y="115" width="460" height="260" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="10"/>
    <text x="280" y="145" fill="#fbbf24" font-size="16" font-weight="700" text-anchor="middle">LCI Power Converter Architecture</text>
    
    <!-- Source Rectifier -->
    <rect x="80" y="180" width="100" height="60" fill="#0b111e" stroke="#38bdf8" stroke-width="2" rx="6"/>
    <text x="130" y="208" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">Line Converter</text>
    <text x="130" y="225" fill="#cbd5e1" font-size="10" text-anchor="middle">(Line Commutated)</text>

    <!-- DC Link Inductor L_dc -->
    <line x1="180" y1="210" x2="250" y2="210" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="215" y="200" fill="#fbbf24" font-size="13" font-weight="700">L_dc</text>

    <!-- Machine Inverter -->
    <rect x="250" y="180" width="110" height="60" fill="#0b111e" stroke="#10b981" stroke-width="2" rx="6"/>
    <text x="305" y="208" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">Load Inverter</text>
    <text x="305" y="225" fill="#cbd5e1" font-size="10" text-anchor="middle">(Load Commutated)</text>

    <!-- Synchronous Motor with Field -->
    <line x1="360" y1="210" x2="410" y2="210" stroke="#38bdf8" stroke-width="2.5"/>
    <circle cx="440" cy="210" r="26" fill="#0b111e" stroke="#f59e0b" stroke-width="2.5"/>
    <text x="440" y="215" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">SM</text>
    <text x="440" y="255" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">Overexcited (Leading PF)</text>

    <text x="280" y="325" fill="#f1f5f9" font-size="12" text-anchor="middle">Motor operates at leading power factor (cos φ &gt; 0 leading)</text>
    <text x="280" y="350" fill="#cbd5e1" font-size="11" text-anchor="middle">Internal EMF E_b provides reverse bias to extinguish incoming SCRs</text>

    <rect x="530" y="115" width="380" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
    <text x="720" y="145" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">Low-Speed Starting Strategy</text>
    
    <rect x="550" y="175" width="340" height="65" fill="#0b111e" stroke="#ef4444" stroke-width="1.5" rx="6"/>
    <text x="720" y="200" fill="#f87171" font-size="13" font-weight="700" text-anchor="middle">Problem at Speeds &lt; 10% Rated</text>
    <text x="720" y="222" fill="#cbd5e1" font-size="11" text-anchor="middle">Back EMF E_b is too small to commutate thyristors</text>

    <rect x="550" y="255" width="340" height="65" fill="#0b111e" stroke="#10b981" stroke-width="1.5" rx="6"/>
    <text x="720" y="280" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">Solution: Pulsed DC Link Commutation</text>
    <text x="720" y="302" fill="#cbd5e1" font-size="11" text-anchor="middle">Line converter brings I_dc to zero; Inverter switches at zero current</text>

    <text x="720" y="350" fill="#fbbf24" font-size="12" font-weight="600" text-anchor="middle">Dominates multi-megawatt gas compressor and marine propulsion drives (up to 100 MW)</text>
    """,
    "Commutation Margin Angle γ: Firing angle β = 180° - α satisfies β ≥ γ + u to prevent commutation failure"
)

# 22. drive-q16: clarke_park_transforms.png
create_card_diagram(
    "images/drive/clarke_park_transforms.png",
    "Vector Control Coordinate Transformations: Clarke and Park Projections",
    "Three-Phase abc (120°) → Stationary αβ (90°) → Synchronously Rotating dq Reference Frame",
    "#f59e0b", "DRIVE • MOD 5",
    """
    <!-- 3-Phase abc to alpha-beta (Clarke) -->
    <rect x="50" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="10"/>
    <text x="255" y="145" fill="#38bdf8" font-size="16" font-weight="700" text-anchor="middle">1. Clarke Transform (abc → αβ0)</text>
    
    <rect x="80" y="170" width="350" height="60" fill="#0b111e" stroke="#38bdf8" stroke-width="2" rx="6"/>
    <text x="255" y="195" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">i_α = i_a</text>
    <text x="255" y="215" fill="#f1f5f9" font-size="13" text-anchor="middle">i_β = (1 / √3) · (i_b - i_c)</text>

    <text x="255" y="255" fill="#cbd5e1" font-size="12" text-anchor="middle">Converts 3 non-orthogonal phases (120° apart)</text>
    <text x="255" y="280" fill="#cbd5e1" font-size="12" text-anchor="middle">into 2 orthogonal stationary axes (α and β at 90°)</text>
    <text x="255" y="310" fill="#34d399" font-size="13" font-weight="600" text-anchor="middle">Zero-sequence i₀ = 0 for balanced 3-wire systems</text>
    <text x="255" y="345" fill="#94a3b8" font-size="11" text-anchor="middle">Still AC sinusoidal quantities alternating at frequency ω_e</text>

    <!-- alpha-beta to dq (Park) -->
    <rect x="500" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
    <text x="705" y="145" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">2. Park Transform (αβ → dq Rotating)</text>
    
    <rect x="530" y="170" width="350" height="60" fill="#0b111e" stroke="#10b981" stroke-width="2" rx="6"/>
    <text x="705" y="195" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">i_d = i_α cos θ_e + i_β sin θ_e</text>
    <text x="705" y="215" fill="#fbbf24" font-size="14" font-weight="700" text-anchor="middle">i_q = -i_α sin θ_e + i_β cos θ_e</text>

    <text x="705" y="255" fill="#cbd5e1" font-size="12" text-anchor="middle">Rotates axes at synchronous rotor electrical speed θ_e</text>
    <text x="705" y="280" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">Transforms AC quantities into pure DC steady-state values</text>
    <text x="705" y="310" fill="#38bdf8" font-size="12">i_d controls Rotor Flux (analogous to DC field current I_f)</text>
    <text x="705" y="335" fill="#fbbf24" font-size="12">i_q controls Electromagnetic Torque (analogous to I_a)</text>
    """,
    "Mathematical Orthogonality: Transforms complex coupled AC dynamics into decoupled linear DC-like control equations"
)

# 23. drive-q17: svpwm_sectors_switching.png
create_card_diagram(
    "images/drive/svpwm_sectors_switching.png",
    "Space Vector PWM (SVPWM): Sector Dwell Times and Voltage Vectors",
    "Six Active Vectors (V₁-V₆) and Two Zero Vectors (V₀, V₇): 15.5% Higher DC Bus Utilization than SPWM",
    "#f59e0b", "DRIVE • MOD 5",
    """
    <!-- Hexagon Diagram -->
    <rect x="50" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="10"/>
    <text x="255" y="145" fill="#fbbf24" font-size="16" font-weight="700" text-anchor="middle">SVPWM Vector Hexagon</text>
    
    <!-- Hexagon path -->
    <polygon points="320,240 290,180 220,180 190,240 220,300 290,300" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
    <circle cx="255" cy="240" r="4" fill="#fbbf24"/>
    <text x="255" y="235" fill="#fbbf24" font-size="10">V₀, V₇</text>

    <!-- Vectors -->
    <text x="325" y="245" fill="#34d399" font-size="11" font-weight="700">V₁ (100)</text>
    <text x="295" y="175" fill="#34d399" font-size="11" font-weight="700">V₂ (110)</text>
    <text x="180" y="175" fill="#34d399" font-size="11" font-weight="700">V₃ (010)</text>
    <text x="140" y="245" fill="#34d399" font-size="11" font-weight="700">V₄ (011)</text>
    <text x="180" y="315" fill="#34d399" font-size="11" font-weight="700">V₅ (001)</text>
    <text x="295" y="315" fill="#34d399" font-size="11" font-weight="700">V₆ (101)</text>

    <!-- Reference Vector in Sector 1 -->
    <line x1="255" y1="240" x2="295" y2="205" stroke="#ef4444" stroke-width="3" marker-end="url(#arrow)"/>
    <text x="270" y="195" fill="#f87171" font-size="12" font-weight="700">V_ref</text>
    <text x="255" y="350" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">Sector 1 (0° to 60°)</text>

    <!-- Dwell Times Calculation -->
    <rect x="500" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
    <text x="705" y="145" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">Sector Dwell Time Formulations</text>
    
    <rect x="525" y="170" width="360" height="75" fill="#0b111e" stroke="#10b981" stroke-width="1.5" rx="6"/>
    <text x="705" y="195" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">T₁ = T_s · (m / sin 60°) · sin(60° - θ)</text>
    <text x="705" y="217" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">T₂ = T_s · (m / sin 60°) · sin(θ)</text>
    <text x="705" y="235" fill="#f1f5f9" font-size="12" text-anchor="middle">T₀ = T_s - T₁ - T₂ (Divided equally between V₀ &amp; V₇)</text>

    <text x="530" y="275" fill="#cbd5e1" font-size="12">✔ Maximum Fundamental: V_max = V_dc / √3 ≈ 0.577 V_dc</text>
    <text x="530" y="300" fill="#38bdf8" font-size="12" font-weight="600">✔ Exactly 15.5% greater DC bus voltage than sinusoidal PWM</text>
    <text x="530" y="325" fill="#cbd5e1" font-size="12">✔ Symmetric 7-segment switching pattern: 0-1-2-7-2-1-0</text>
    <text x="530" y="350" fill="#cbd5e1" font-size="12">✔ Minimizes inverter harmonic distortion and switching losses</text>
    """,
    "Maximum Inscription Circle: Circle of radius V_dc/√3 inscribed in hexagon defines linear modulation boundary"
)

# 24. drive-q18: field_oriented_control_block_diagram.png
create_card_diagram(
    "images/drive/field_oriented_control_block_diagram.png",
    "Rotor Field-Oriented Control (FOC) Architecture for Induction Motors",
    "Complete Decoupling of Stator Currents into Flux-Producing (i_ds) and Torque-Producing (i_qs) Components",
    "#f59e0b", "DRIVE • MOD 5",
    """
    <!-- Speed Loop -->
    <text x="60" y="165" fill="#38bdf8" font-size="12" font-weight="700">ω_ref</text>
    <circle cx="100" cy="180" r="12" fill="#0b111e" stroke="#38bdf8"/>
    <text x="100" y="184" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">Σ</text>
    
    <rect x="130" y="160" width="80" height="40" fill="url(#boxGrad)" stroke="#38bdf8" rx="4"/>
    <text x="170" y="185" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="middle">Speed PI</text>

    <path d="M 210 180 L 250 180" stroke="#f59e0b" stroke-width="2" marker-end="url(#arrow)"/>
    <text x="230" y="170" fill="#fbbf24" font-size="11">i_qs*</text>

    <!-- Torque Current Loop (q-axis) -->
    <rect x="260" y="160" width="80" height="40" fill="url(#boxGrad)" stroke="#f59e0b" rx="4"/>
    <text x="300" y="185" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">PI (i_qs)</text>

    <!-- Flux Current Loop (d-axis) -->
    <text x="140" y="245" fill="#34d399" font-size="11" font-weight="700">λ_r* (Flux Ref)</text>
    <rect x="260" y="230" width="80" height="40" fill="url(#boxGrad)" stroke="#10b981" rx="4"/>
    <text x="300" y="255" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">PI (i_ds)</text>

    <!-- Inverse Park Transform -->
    <rect x="380" y="180" width="100" height="80" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="2" rx="6"/>
    <text x="430" y="215" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">Inverse Park</text>
    <text x="430" y="235" fill="#cbd5e1" font-size="10" text-anchor="middle">dq → αβ</text>

    <!-- SVPWM & VSI Inverter -->
    <rect x="520" y="180" width="100" height="80" fill="url(#boxGrad)" stroke="#10b981" stroke-width="2" rx="6"/>
    <text x="570" y="215" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">SVPWM</text>
    <text x="570" y="235" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">&amp; VSI Inverter</text>

    <!-- Induction Motor -->
    <circle cx="680" cy="220" r="30" fill="#0b111e" stroke="#fbbf24" stroke-width="2.5"/>
    <text x="680" y="225" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">IM</text>

    <!-- Feedback Estimator (Flux / Speed) -->
    <rect x="450" y="295" width="230" height="50" fill="url(#boxGrad)" stroke="#a855f7" stroke-width="2" rx="6"/>
    <text x="565" y="320" fill="#c084fc" font-size="12" font-weight="700" text-anchor="middle">Rotor Flux &amp; Angle Estimator (θ_e)</text>
    <text x="565" y="336" fill="#cbd5e1" font-size="10" text-anchor="middle">Slip Relation: ω_sl = (R_r / L_r) · (i_qs / i_ds)</text>

    <text x="480" y="380" fill="#f1f5f9" font-size="12" text-anchor="middle">Direct field alignment (λ_qr = 0) eliminates cross-coupling and yields instantaneous torque response</text>
    """,
    "Torque Equation in FOC: T_e = (3/2) · (P/2) · (L_m / L_r) · λ_dr · i_qs (Linear torque control like a separately excited DC motor)"
)

print("Finished generating Electric Drives diagrams.")
