# -*- coding: utf-8 -*-
"""
Generator for all ACS (Advanced Control Systems) diagrams.
Generates technical vector SVGs and converts them to high-resolution PNGs via sips.
"""
import os, subprocess

os.makedirs("images/acs", exist_ok=True)

def save_svg_and_convert(svg_str, png_path):
    svg_path = png_path.replace(".png", ".svg")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_str)
    subprocess.run(["sips", "-s", "format", "png", svg_path, "--out", png_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if os.path.exists(svg_path):
        os.remove(svg_path)
    if os.path.exists(png_path):
        print(f"Generated {png_path} ({os.path.getsize(png_path)} bytes)")

# Common styles
CSS_DEF = """
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0c1220"/>
      <stop offset="100%" stop-color="#151d30"/>
    </linearGradient>
    <linearGradient id="boxGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#38bdf8"/>
    </linearGradient>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#38bdf8"/>
    </marker>
    <marker id="arrow-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#10b981"/>
    </marker>
    <marker id="arrow-amber" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#f59e0b"/>
    </marker>
  </defs>
"""

def gen_state_space_concept():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="900" height="420" viewBox="0 0 900 420">
  {CSS_DEF}
  <rect width="900" height="420" fill="url(#bgGrad)" rx="16"/>
  <rect x="20" y="20" width="860" height="380" fill="none" stroke="#223049" stroke-width="1.5" rx="12"/>
  <text x="450" y="55" fill="#f1f5f9" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" text-anchor="middle">State Space Representation: State Vector, Inputs &amp; Outputs</text>
  
  <!-- Outer Plant Box -->
  <rect x="240" y="100" width="420" height="240" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="2" rx="14" stroke-dasharray="6,4"/>
  <text x="450" y="130" fill="#38bdf8" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" text-anchor="middle">Physical Dynamic Plant S(A, B, C, D)</text>
  
  <!-- Internal State Box -->
  <rect x="340" y="160" width="220" height="130" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="10"/>
  <text x="450" y="200" fill="#34d399" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" text-anchor="middle">Internal State Space</text>
  <text x="450" y="230" fill="#f1f5f9" font-family="-apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">x(t) ∈ ℝⁿ</text>
  <text x="450" y="260" fill="#94a3b8" font-family="-apple-system, sans-serif" font-size="13" text-anchor="middle">Minimum Energy Storage</text>

  <!-- Input Arrow -->
  <path d="M 60 225 L 235 225" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)"/>
  <text x="140" y="210" fill="#38bdf8" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" text-anchor="middle">Input u(t) ∈ ℝᵐ</text>
  <text x="140" y="250" fill="#94a3b8" font-family="-apple-system, sans-serif" font-size="13" text-anchor="middle">(Control Forces / Voltages)</text>

  <!-- Output Arrow -->
  <path d="M 665 225 L 840 225" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)"/>
  <text x="750" y="210" fill="#38bdf8" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" text-anchor="middle">Output y(t) ∈ ℝᵖ</text>
  <text x="750" y="250" fill="#94a3b8" font-family="-apple-system, sans-serif" font-size="13" text-anchor="middle">(Sensors / Measurables)</text>

  <!-- Equations footer -->
  <rect x="180" y="355" width="540" height="35" fill="#0f172a" stroke="#334155" rx="6"/>
  <text x="450" y="378" fill="#e2e8f0" font-family="monospace" font-size="15" text-anchor="middle">State Eq: dx/dt = Ax(t) + Bu(t)  |  Output Eq: y(t) = Cx(t) + Du(t)</text>
</svg>"""
    save_svg_and_convert(svg, "images/acs/state_space_concept.png")

def gen_lti_state_block_diagram():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="960" height="460" viewBox="0 0 960 460">
  {CSS_DEF}
  <rect width="960" height="460" fill="url(#bgGrad)" rx="16"/>
  <rect x="20" y="20" width="920" height="420" fill="none" stroke="#223049" stroke-width="1.5" rx="12"/>
  <text x="480" y="55" fill="#f1f5f9" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" text-anchor="middle">Continuous-Time LTI State Space Block Diagram Architecture</text>
  
  <!-- Input u(t) -->
  <path d="M 50 180 L 150 180" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)"/>
  <text x="90" y="165" fill="#38bdf8" font-family="-apple-system, sans-serif" font-size="16" font-weight="700">u(t)</text>
  
  <!-- B Matrix Block -->
  <rect x="155" y="150" width="70" height="60" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="190" y="187" fill="#f1f5f9" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" text-anchor="middle">B</text>

  <!-- Summer 1 -->
  <circle cx="280" cy="180" r="18" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="280" y="186" fill="#38bdf8" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" text-anchor="middle">Σ</text>
  <path d="M 225 180 L 257 180" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)"/>

  <!-- x_dot arrow -->
  <path d="M 298 180 L 375 180" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)"/>
  <text x="335" y="165" fill="#f59e0b" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" text-anchor="middle">ẋ(t)</text>

  <!-- Integrator Block -->
  <rect x="380" y="145" width="80" height="70" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="2.5" rx="8"/>
  <text x="420" y="187" fill="#fbbf24" font-family="-apple-system, sans-serif" font-size="22" font-weight="700" text-anchor="middle">∫ dt</text>

  <!-- x(t) branch -->
  <path d="M 460 180 L 565 180" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)"/>
  <circle cx="510" cy="180" r="4" fill="#38bdf8"/>
  <text x="510" y="165" fill="#34d399" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" text-anchor="middle">x(t)</text>

  <!-- C Matrix Block -->
  <rect x="570" y="150" width="70" height="60" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="605" y="187" fill="#f1f5f9" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" text-anchor="middle">C</text>

  <!-- Summer 2 -->
  <circle cx="710" cy="180" r="18" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="710" y="186" fill="#38bdf8" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" text-anchor="middle">Σ</text>
  <path d="M 640 180 L 687 180" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)"/>

  <!-- Output y(t) -->
  <path d="M 728 180 L 890 180" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)"/>
  <text x="840" y="165" fill="#38bdf8" font-family="-apple-system, sans-serif" font-size="16" font-weight="700">y(t)</text>

  <!-- Feedback A path -->
  <path d="M 510 180 L 510 290 L 455 290" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>
  <rect x="380" y="260" width="70" height="60" fill="url(#boxGrad)" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="415" y="297" fill="#34d399" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" text-anchor="middle">A</text>
  <path d="M 380 290 L 280 290 L 280 203" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>
  <text x="320" y="310" fill="#94a3b8" font-family="-apple-system, sans-serif" font-size="14" text-anchor="middle">Ax(t) Feedback</text>

  <!-- Direct Feedthrough D path -->
  <path d="M 100 180 L 100 80 L 475 80" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>
  <circle cx="100" cy="180" r="4" fill="#38bdf8"/>
  <rect x="480" y="55" width="70" height="50" fill="url(#boxGrad)" stroke="#a855f7" stroke-width="2" rx="8"/>
  <text x="515" y="87" fill="#c084fc" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" text-anchor="middle">D</text>
  <path d="M 550 80 L 710 80 L 710 157" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>
  <text x="610" y="70" fill="#94a3b8" font-family="-apple-system, sans-serif" font-size="14">Direct Transmission Du(t)</text>

  <!-- Footnote -->
  <text x="480" y="400" fill="#94a3b8" font-family="-apple-system, sans-serif" font-size="14" text-anchor="middle">State Vector ẋ(t) = Ax(t) + Bu(t)  |  Output y(t) = Cx(t) + Du(t)</text>
</svg>"""
    save_svg_and_convert(svg, "images/acs/lti_state_block_diagram.png")

def gen_phase_variables_flow():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="940" height="420" viewBox="0 0 940 420">
  {CSS_DEF}
  <rect width="940" height="420" fill="url(#bgGrad)" rx="16"/>
  <rect x="20" y="20" width="900" height="380" fill="none" stroke="#223049" stroke-width="1.5" rx="12"/>
  <text x="470" y="55" fill="#f1f5f9" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" text-anchor="middle">Phase Variable Canonical Form (Integrator Cascade)</text>
  
  <!-- Summer 0 -->
  <circle cx="160" cy="180" r="18" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="160" y="186" fill="#38bdf8" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" text-anchor="middle">Σ</text>
  
  <!-- Input u(t) -->
  <path d="M 60 180 L 137 180" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)"/>
  <text x="95" y="165" fill="#38bdf8" font-family="-apple-system, sans-serif" font-size="16" font-weight="700">u(t)</text>

  <!-- Chain of 3 Integrators -->
  <!-- Int 3 -->
  <path d="M 178 180 L 255 180" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)"/>
  <text x="215" y="165" fill="#f59e0b" font-family="-apple-system, sans-serif" font-size="15" font-weight="700">ẋ₃</text>
  <rect x="260" y="150" width="70" height="60" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="2" rx="8"/>
  <text x="295" y="187" fill="#fbbf24" font-family="-apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">1/s</text>

  <!-- Int 2 -->
  <path d="M 330 180 L 465 180" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)"/>
  <circle cx="400" cy="180" r="4" fill="#38bdf8"/>
  <text x="400" y="165" fill="#38bdf8" font-family="-apple-system, sans-serif" font-size="15" font-weight="700" text-anchor="middle">x₃ = ẋ₂</text>
  <rect x="470" y="150" width="70" height="60" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="2" rx="8"/>
  <text x="505" y="187" fill="#fbbf24" font-family="-apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">1/s</text>

  <!-- Int 1 -->
  <path d="M 540 180 L 675 180" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)"/>
  <circle cx="610" cy="180" r="4" fill="#38bdf8"/>
  <text x="610" y="165" fill="#38bdf8" font-family="-apple-system, sans-serif" font-size="15" font-weight="700" text-anchor="middle">x₂ = ẋ₁</text>
  <rect x="680" y="150" width="70" height="60" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="2" rx="8"/>
  <text x="715" y="187" fill="#fbbf24" font-family="-apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">1/s</text>

  <!-- Output -->
  <path d="M 750 180 L 870 180" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)"/>
  <circle cx="810" cy="180" r="4" fill="#38bdf8"/>
  <text x="810" y="165" fill="#34d399" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" text-anchor="middle">x₁ = y(t)</text>

  <!-- Feedback loops: -a0, -a1, -a2 -->
  <path d="M 810 180 L 810 320 L 735 320" stroke="#ef4444" stroke-width="2" marker-end="url(#arrow)"/>
  <rect x="670" y="295" width="60" height="50" fill="url(#boxGrad)" stroke="#ef4444" stroke-width="1.5" rx="6"/>
  <text x="700" y="325" fill="#fca5a5" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" text-anchor="middle">-a₀</text>

  <path d="M 610 180 L 610 270 L 535 270" stroke="#ef4444" stroke-width="2" marker-end="url(#arrow)"/>
  <rect x="470" y="245" width="60" height="50" fill="url(#boxGrad)" stroke="#ef4444" stroke-width="1.5" rx="6"/>
  <text x="500" y="275" fill="#fca5a5" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" text-anchor="middle">-a₁</text>

  <path d="M 400 180 L 400 220 L 325 220" stroke="#ef4444" stroke-width="2" marker-end="url(#arrow)"/>
  <rect x="260" y="210" width="60" height="40" fill="url(#boxGrad)" stroke="#ef4444" stroke-width="1.5" rx="6"/>
  <text x="290" y="235" fill="#fca5a5" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" text-anchor="middle">-a₂</text>

  <!-- Return to summer -->
  <path d="M 670 320 L 160 320 L 160 203" stroke="#ef4444" stroke-width="2" marker-end="url(#arrow)"/>
  <path d="M 470 270 L 160 270" stroke="#ef4444" stroke-width="2"/>
  <path d="M 260 230 L 160 230" stroke="#ef4444" stroke-width="2"/>

  <text x="470" y="380" fill="#94a3b8" font-family="-apple-system, sans-serif" font-size="14" text-anchor="middle">Companion Matrix A has 1s on super-diagonal and [-a₀, -a₁, -a₂] in bottom row</text>
</svg>"""
    save_svg_and_convert(svg, "images/acs/phase_variables_flow.png")

def gen_armature_dc_motor():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="920" height="420" viewBox="0 0 920 420">
  {CSS_DEF}
  <rect width="920" height="420" fill="url(#bgGrad)" rx="16"/>
  <rect x="20" y="20" width="880" height="380" fill="none" stroke="#223049" stroke-width="1.5" rx="12"/>
  <text x="460" y="55" fill="#f1f5f9" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" text-anchor="middle">Armature-Controlled DC Servomotor Schematic &amp; Mechanical Load</text>

  <!-- Electrical Armature Circuit -->
  <rect x="50" y="90" width="400" height="250" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="10"/>
  <text x="250" y="120" fill="#38bdf8" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" text-anchor="middle">Armature Circuit (Ra, La, eb)</text>

  <!-- Resistor Ra -->
  <path d="M 80 190 L 120 190 L 130 175 L 145 205 L 160 175 L 175 205 L 190 175 L 200 190 L 230 190" stroke="#f1f5f9" stroke-width="2.5" fill="none"/>
  <text x="165" y="160" fill="#fbbf24" font-family="-apple-system, sans-serif" font-size="15" font-weight="700" text-anchor="middle">Ra</text>

  <!-- Inductor La -->
  <path d="M 230 190 Q 245 170 260 190 Q 275 170 290 190 Q 305 170 320 190 L 350 190" stroke="#f1f5f9" stroke-width="2.5" fill="none"/>
  <text x="275" y="160" fill="#34d399" font-family="-apple-system, sans-serif" font-size="15" font-weight="700" text-anchor="middle">La</text>

  <!-- Armature Rotor Circle -->
  <circle cx="390" cy="190" r="30" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
  <text x="390" y="197" fill="#38bdf8" font-family="-apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">M</text>
  <text x="390" y="240" fill="#94a3b8" font-family="-apple-system, sans-serif" font-size="13" text-anchor="middle">eb = Kb·ω</text>

  <!-- Input Voltage ea(t) -->
  <circle cx="80" cy="190" r="4" fill="#38bdf8"/>
  <circle cx="80" cy="290" r="4" fill="#38bdf8"/>
  <path d="M 80 290 L 390 290 L 390 225" stroke="#f1f5f9" stroke-width="2.5"/>
  <text x="70" y="245" fill="#38bdf8" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" text-anchor="end">ea(t) + -</text>

  <!-- Mechanical Shaft & Load -->
  <rect x="470" y="90" width="400" height="250" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
  <text x="670" y="120" fill="#10b981" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" text-anchor="middle">Mechanical Inertia &amp; Damping (J, B)</text>

  <!-- Shaft -->
  <rect x="420" y="185" width="100" height="10" fill="#64748b"/>
  <text x="470" y="175" fill="#f59e0b" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Tm = Kt·ia</text>

  <!-- Rotor Inertia J Cylinder -->
  <rect x="520" y="160" width="60" height="60" fill="#334155" stroke="#f1f5f9" stroke-width="2" rx="6"/>
  <text x="550" y="196" fill="#f1f5f9" font-family="-apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">J</text>

  <!-- Viscous Friction B -->
  <path d="M 580 190 L 660 190" stroke="#f1f5f9" stroke-width="3"/>
  <rect x="660" y="165" width="50" height="50" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="6"/>
  <text x="685" y="196" fill="#34d399" font-family="-apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">B</text>

  <!-- Angular velocity output arrow -->
  <path d="M 715 190 L 830 190" stroke="#10b981" stroke-width="3" marker-end="url(#arrow-green)"/>
  <text x="790" y="175" fill="#34d399" font-family="-apple-system, sans-serif" font-size="16" font-weight="700">ω(t), θ(t)</text>

  <rect x="150" y="355" width="620" height="32" fill="#0f172a" stroke="#334155" rx="6"/>
  <text x="460" y="376" fill="#cbd5e1" font-family="monospace" font-size="14" text-anchor="middle">State Vector x = [ia, ω, θ]ᵀ  |  dia/dt = -(Ra/La)ia - (Kb/La)ω + (1/La)ea</text>
</svg>"""
    save_svg_and_convert(svg, "images/acs/armature_dc_motor.png")

def gen_state_observer():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="940" height="440" viewBox="0 0 940 440">
  {CSS_DEF}
  <rect width="940" height="440" fill="url(#bgGrad)" rx="16"/>
  <rect x="20" y="20" width="900" height="400" fill="none" stroke="#223049" stroke-width="1.5" rx="12"/>
  <text x="470" y="55" fill="#f1f5f9" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" text-anchor="middle">Full-Order Luenberger State Observer Block Diagram</text>

  <!-- Actual Plant Container (Top) -->
  <rect x="180" y="90" width="560" height="110" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="10"/>
  <text x="460" y="115" fill="#38bdf8" font-family="-apple-system, sans-serif" font-size="15" font-weight="700" text-anchor="middle">Physical Plant System: ẋ = Ax + Bu,  y = Cx</text>
  <rect x="280" y="130" width="120" height="50" fill="#1e293b" stroke="#38bdf8" rx="6"/>
  <text x="340" y="160" fill="#f1f5f9" font-family="-apple-system, sans-serif" font-size="14" text-anchor="middle">ẋ = Ax + Bu</text>
  <path d="M 405 155 L 515 155" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>
  <rect x="520" y="130" width="80" height="50" fill="#1e293b" stroke="#38bdf8" rx="6"/>
  <text x="560" y="160" fill="#f1f5f9" font-family="-apple-system, sans-serif" font-size="14" text-anchor="middle">C</text>
  <path d="M 605 155 L 720 155" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>
  <circle cx="720" cy="155" r="4" fill="#38bdf8"/>
  <text x="760" y="155" fill="#38bdf8" font-family="-apple-system, sans-serif" font-size="16" font-weight="700">y(t)</text>

  <!-- Input u(t) splits to both -->
  <path d="M 60 155 L 275 155" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>
  <circle cx="120" cy="155" r="4" fill="#38bdf8"/>
  <text x="90" y="140" fill="#38bdf8" font-family="-apple-system, sans-serif" font-size="16" font-weight="700">u(t)</text>

  <!-- Observer Container (Bottom) -->
  <rect x="180" y="230" width="560" height="160" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
  <text x="460" y="255" fill="#34d399" font-family="-apple-system, sans-serif" font-size="15" font-weight="700" text-anchor="middle">Luenberger Observer: x̂̇ = Ax̂ + Bu + L(y - Cx̂)</text>

  <!-- Input u branch down to observer -->
  <path d="M 120 155 L 120 320 L 275 320" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Innovation summer -->
  <circle cx="800" cy="270" r="16" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
  <text x="800" y="276" fill="#fbbf24" font-family="-apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">Σ</text>
  
  <!-- Plant y down to summer -->
  <path d="M 720 155 L 800 155 L 800 250" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>
  <text x="815" y="200" fill="#38bdf8" font-family="-apple-system, sans-serif" font-size="14">+y</text>

  <!-- Observer y_hat back to summer -->
  <path d="M 660 320 L 750 320 L 750 270 L 780 270" stroke="#10b981" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="765" y="295" fill="#ef4444" font-family="-apple-system, sans-serif" font-size="14">-ŷ</text>

  <!-- Innovation e_y into Gain L -->
  <path d="M 800 286 L 800 370 L 530 370" stroke="#f59e0b" stroke-width="2.5" marker-end="url(#arrow)"/>
  <text x="680" y="390" fill="#fbbf24" font-family="-apple-system, sans-serif" font-size="14" text-anchor="middle">Error e_y = (y - ŷ)</text>

  <!-- Observer Core Block -->
  <rect x="280" y="295" width="240" height="70" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="400" y="325" fill="#34d399" font-family="-apple-system, sans-serif" font-size="15" font-weight="700" text-anchor="middle">Observer Engine</text>
  <text x="400" y="348" fill="#f1f5f9" font-family="-apple-system, sans-serif" font-size="13" text-anchor="middle">∫ dt  [ A - LC ] + Bu + Ly</text>

  <!-- Estimated State Output -->
  <path d="M 525 320 L 640 320" stroke="#10b981" stroke-width="3" marker-end="url(#arrow-green)"/>
  <circle cx="610" cy="320" r="4" fill="#10b981"/>
  <text x="590" y="305" fill="#34d399" font-family="-apple-system, sans-serif" font-size="17" font-weight="700">x̂(t)</text>
</svg>"""
    save_svg_and_convert(svg, "images/acs/state_observer_block_diagram.png")

def gen_saturation_describing_function():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="900" height="420" viewBox="0 0 900 420">
  {CSS_DEF}
  <rect width="900" height="420" fill="url(#bgGrad)" rx="16"/>
  <rect x="20" y="20" width="860" height="380" fill="none" stroke="#223049" stroke-width="1.5" rx="12"/>
  <text x="450" y="55" fill="#f1f5f9" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" text-anchor="middle">Describing Function: Symmetrical Saturation Non-Linearity</text>

  <!-- Left: Input-Output Saturation Characteristic -->
  <rect x="60" y="90" width="360" height="270" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="10"/>
  <text x="240" y="120" fill="#38bdf8" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" text-anchor="middle">Non-Linear Characteristic y = f(x)</text>

  <!-- Axes -->
  <line x1="90" y1="225" x2="390" y2="225" stroke="#64748b" stroke-width="1.5"/>
  <line x1="240" y1="130" x2="240" y2="320" stroke="#64748b" stroke-width="1.5"/>
  <text x="395" y="230" fill="#94a3b8" font-family="-apple-system, sans-serif" font-size="14">x</text>
  <text x="245" y="140" fill="#94a3b8" font-family="-apple-system, sans-serif" font-size="14">y</text>

  <!-- Saturation Curve: negative flat, slope, positive flat -->
  <path d="M 120 285 L 180 285 L 300 165 L 360 165" stroke="#f59e0b" stroke-width="3.5" fill="none"/>
  
  <!-- Thresholds -S and +S -->
  <line x1="300" y1="165" x2="300" y2="225" stroke="#94a3b8" stroke-dasharray="4,4"/>
  <text x="300" y="245" fill="#fbbf24" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">+S</text>
  <line x1="180" y1="285" x2="180" y2="225" stroke="#94a3b8" stroke-dasharray="4,4"/>
  <text x="180" y="245" fill="#fbbf24" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">-S</text>
  
  <!-- Saturation Levels -->
  <text x="365" y="160" fill="#f59e0b" font-family="-apple-system, sans-serif" font-size="14" font-weight="700">+KS</text>
  <text x="95" y="295" fill="#f59e0b" font-family="-apple-system, sans-serif" font-size="14" font-weight="700">-KS</text>

  <!-- Right: Clipped Sine Wave Output -->
  <rect x="480" y="90" width="360" height="270" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
  <text x="660" y="120" fill="#34d399" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" text-anchor="middle">Input x(t) vs Clipped Output y(t)</text>
  <line x1="510" y1="225" x2="810" y2="225" stroke="#64748b" stroke-width="1.5"/>
  <line x1="540" y1="130" x2="540" y2="320" stroke="#64748b" stroke-width="1.5"/>

  <!-- Pure Sine wave (input) dashed -->
  <path d="M 540 225 Q 585 130 630 225 Q 675 320 720 225 Q 765 130 810 225" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,4" fill="none"/>
  
  <!-- Clipped Wave (output) solid -->
  <path d="M 540 225 L 565 175 L 605 175 L 630 225 L 655 275 L 695 275 L 720 225 L 745 175 L 785 175 L 810 225" stroke="#10b981" stroke-width="3" fill="none"/>
  <text x="760" y="150" fill="#34d399" font-family="-apple-system, sans-serif" font-size="13" font-weight="700">y(t) Flat Top</text>

  <!-- Equation -->
  <rect x="180" y="375" width="540" height="30" fill="#0f172a" stroke="#334155" rx="5"/>
  <text x="450" y="395" fill="#cbd5e1" font-family="monospace" font-size="14" text-anchor="middle">N(X) = (2K/π)[ sin⁻¹(S/X) + (S/X)√(1 - (S/X)²) ]  for X &gt; S</text>
</svg>"""
    save_svg_and_convert(svg, "images/acs/saturation_describing_function.png")

def gen_four_quadrant_hoist():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="920" height="460" viewBox="0 0 920 460">
  {CSS_DEF}
  <rect width="920" height="460" fill="url(#bgGrad)" rx="16"/>
  <rect x="20" y="20" width="880" height="420" fill="none" stroke="#223049" stroke-width="1.5" rx="12"/>
  <text x="460" y="55" fill="#f1f5f9" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" text-anchor="middle">Four-Quadrant Operation of an Electric Motor Hoist Drive</text>

  <!-- Axes -->
  <line x1="120" y1="240" x2="800" y2="240" stroke="#f1f5f9" stroke-width="2.5" marker-end="url(#arrow)"/>
  <line x1="460" y1="390" x2="460" y2="90" stroke="#f1f5f9" stroke-width="2.5" marker-end="url(#arrow)"/>
  <text x="815" y="245" fill="#38bdf8" font-family="-apple-system, sans-serif" font-size="18" font-weight="700">Torque T (+)</text>
  <text x="85" y="245" fill="#38bdf8" font-family="-apple-system, sans-serif" font-size="18" font-weight="700">Torque T (-)</text>
  <text x="460" y="80" fill="#10b981" font-family="-apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">Speed ω (+ Forward)</text>
  <text x="460" y="415" fill="#10b981" font-family="-apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">Speed ω (- Reverse)</text>

  <!-- Quadrant II -->
  <rect x="140" y="100" width="300" height="130" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="8"/>
  <text x="290" y="125" fill="#fbbf24" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" text-anchor="middle">QUADRANT II: Forward Braking</text>
  <text x="290" y="150" fill="#f1f5f9" font-family="-apple-system, sans-serif" font-size="14" text-anchor="middle">ω &gt; 0, T &lt; 0  ⇒  Power P &lt; 0</text>
  <text x="290" y="175" fill="#94a3b8" font-family="-apple-system, sans-serif" font-size="13" text-anchor="middle">Empty cage moving upward rapidly</text>
  <text x="290" y="195" fill="#38bdf8" font-family="-apple-system, sans-serif" font-size="13" text-anchor="middle">Motor brakes against counterweight</text>

  <!-- Quadrant I -->
  <rect x="480" y="100" width="300" height="130" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="8"/>
  <text x="630" y="125" fill="#34d399" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" text-anchor="middle">QUADRANT I: Forward Motoring</text>
  <text x="630" y="150" fill="#f1f5f9" font-family="-apple-system, sans-serif" font-size="14" text-anchor="middle">ω &gt; 0, T &gt; 0  ⇒  Power P &gt; 0</text>
  <text x="630" y="175" fill="#f1f5f9" font-family="-apple-system, sans-serif" font-size="13" text-anchor="middle">Loaded hoist moving upward (Hoisting)</text>
  <text x="630" y="195" fill="#38bdf8" font-family="-apple-system, sans-serif" font-size="13" text-anchor="middle">Motor drives load against gravity</text>

  <!-- Quadrant III -->
  <rect x="140" y="250" width="300" height="130" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="8"/>
  <text x="290" y="275" fill="#38bdf8" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" text-anchor="middle">QUADRANT III: Reverse Motoring</text>
  <text x="290" y="300" fill="#f1f5f9" font-family="-apple-system, sans-serif" font-size="14" text-anchor="middle">ω &lt; 0, T &lt; 0  ⇒  Power P &gt; 0</text>
  <text x="290" y="325" fill="#f1f5f9" font-family="-apple-system, sans-serif" font-size="13" text-anchor="middle">Empty cage lowering down</text>
  <text x="290" y="345" fill="#94a3b8" font-family="-apple-system, sans-serif" font-size="13" text-anchor="middle">Overcoming counterweight upwards</text>

  <!-- Quadrant IV -->
  <rect x="480" y="250" width="300" height="130" fill="url(#boxGrad)" stroke="#ef4444" stroke-width="1.5" rx="8"/>
  <text x="630" y="275" fill="#fca5a5" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" text-anchor="middle">QUADRANT IV: Reverse Braking</text>
  <text x="630" y="300" fill="#f1f5f9" font-family="-apple-system, sans-serif" font-size="14" text-anchor="middle">ω &lt; 0, T &gt; 0  ⇒  Power P &lt; 0</text>
  <text x="630" y="325" fill="#f1f5f9" font-family="-apple-system, sans-serif" font-size="13" text-anchor="middle">Loaded hoist lowering under gravity</text>
  <text x="630" y="345" fill="#fbbf24" font-family="-apple-system, sans-serif" font-size="13" text-anchor="middle">Regenerative braking retards descent</text>
</svg>"""
    save_svg_and_convert(svg, "images/drive/four_quadrant_hoist.png")

def gen_three_tier():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="920" height="440" viewBox="0 0 920 440">
  {CSS_DEF}
  <rect width="920" height="440" fill="url(#bgGrad)" rx="16"/>
  <rect x="20" y="20" width="880" height="400" fill="none" stroke="#223049" stroke-width="1.5" rx="12"/>
  <text x="460" y="55" fill="#f1f5f9" font-family="-apple-system, sans-serif" font-size="20" font-weight="700" text-anchor="middle">Comprehensive Three-Tier Architecture of Mobile Computing Systems</text>

  <!-- Tier 1 -->
  <rect x="50" y="90" width="230" height="300" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="2" rx="12"/>
  <rect x="65" y="105" width="200" height="40" fill="#0284c7" rx="8"/>
  <text x="165" y="130" fill="#ffffff" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" text-anchor="middle">Tier 1: Presentation</text>
  <text x="165" y="170" fill="#38bdf8" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Mobile Client Terminal</text>
  <text x="165" y="200" fill="#cbd5e1" font-family="-apple-system, sans-serif" font-size="13" text-anchor="middle">• Thin / Smart Client UI</text>
  <text x="165" y="225" fill="#cbd5e1" font-family="-apple-system, sans-serif" font-size="13" text-anchor="middle">• Local Caching (SQLite)</text>
  <text x="165" y="250" fill="#cbd5e1" font-family="-apple-system, sans-serif" font-size="13" text-anchor="middle">• Touch / Voice Capture</text>
  <text x="165" y="275" fill="#cbd5e1" font-family="-apple-system, sans-serif" font-size="13" text-anchor="middle">• Context Sensing (GPS)</text>
  <text x="165" y="310" fill="#94a3b8" font-family="-apple-system, sans-serif" font-size="12" text-anchor="middle">Disconnected Operation Engine</text>

  <!-- Arrows 1 <-> 2 -->
  <path d="M 285 220 L 340 220" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>
  <path d="M 340 250 L 285 250" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>
  <text x="312" y="210" fill="#94a3b8" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">WAP/HTTP</text>
  <text x="312" y="270" fill="#94a3b8" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">JSON/REST</text>

  <!-- Tier 2 -->
  <rect x="345" y="90" width="230" height="300" fill="url(#boxGrad)" stroke="#10b981" stroke-width="2" rx="12"/>
  <rect x="360" y="105" width="200" height="40" fill="#059669" rx="8"/>
  <text x="460" y="130" fill="#ffffff" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" text-anchor="middle">Tier 2: Application</text>
  <text x="460" y="170" fill="#34d399" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Middleware &amp; Gateways</text>
  <text x="460" y="200" fill="#cbd5e1" font-family="-apple-system, sans-serif" font-size="13" text-anchor="middle">• Core Business Logic</text>
  <text x="460" y="225" fill="#cbd5e1" font-family="-apple-system, sans-serif" font-size="13" text-anchor="middle">• Content Transcoding</text>
  <text x="460" y="250" fill="#cbd5e1" font-family="-apple-system, sans-serif" font-size="13" text-anchor="middle">• Context &amp; Policy Mgr</text>
  <text x="460" y="275" fill="#cbd5e1" font-family="-apple-system, sans-serif" font-size="13" text-anchor="middle">• Message Queue (MOM)</text>
  <text x="460" y="310" fill="#94a3b8" font-family="-apple-system, sans-serif" font-size="12" text-anchor="middle">Session State &amp; Sync Engine</text>

  <!-- Arrows 2 <-> 3 -->
  <path d="M 580 220 L 635 220" stroke="#10b981" stroke-width="2.5" marker-end="url(#arrow-green)"/>
  <path d="M 635 250 L 580 250" stroke="#10b981" stroke-width="2.5" marker-end="url(#arrow-green)"/>
  <text x="607" y="210" fill="#94a3b8" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">SQL/JDBC</text>
  <text x="607" y="270" fill="#94a3b8" font-family="-apple-system, sans-serif" font-size="11" text-anchor="middle">Encrypted</text>

  <!-- Tier 3 -->
  <rect x="640" y="90" width="230" height="300" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="2" rx="12"/>
  <rect x="655" y="105" width="200" height="40" fill="#d97706" rx="8"/>
  <text x="755" y="130" fill="#ffffff" font-family="-apple-system, sans-serif" font-size="16" font-weight="700" text-anchor="middle">Tier 3: Enterprise Data</text>
  <text x="755" y="170" fill="#fbbf24" font-family="-apple-system, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Authoritative Database</text>
  <text x="755" y="200" fill="#cbd5e1" font-family="-apple-system, sans-serif" font-size="13" text-anchor="middle">• Corporate RDBMS / ERP</text>
  <text x="755" y="225" fill="#cbd5e1" font-family="-apple-system, sans-serif" font-size="13" text-anchor="middle">• ACID Transaction Logs</text>
  <text x="755" y="250" fill="#cbd5e1" font-family="-apple-system, sans-serif" font-size="13" text-anchor="middle">• Big Data / Cloud Lakes</text>
  <text x="755" y="275" fill="#cbd5e1" font-family="-apple-system, sans-serif" font-size="13" text-anchor="middle">• Mainframe Records</text>
  <text x="755" y="310" fill="#94a3b8" font-family="-apple-system, sans-serif" font-size="12" text-anchor="middle">Global Concurrency &amp; Backup</text>
</svg>"""
    save_svg_and_convert(svg, "images/mobile_compute/three_tier_architecture.png")

print("Generating core technical diagrams...")
gen_state_space_concept()
gen_lti_state_block_diagram()
gen_phase_variables_flow()
gen_armature_dc_motor()
gen_state_observer()
gen_saturation_describing_function()
gen_four_quadrant_hoist()
gen_three_tier()
