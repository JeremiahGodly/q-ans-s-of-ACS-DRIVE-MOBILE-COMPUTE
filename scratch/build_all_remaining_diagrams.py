# -*- coding: utf-8 -*-
"""
Automated High-Resolution Technical Diagram Generator for KTU Exam Portal.
Fills all remaining missing images across ACS, Electric Drives, and Mobile Computing
with crisp, publication-grade vector graphics rendered to PNG.
"""

import os, subprocess

os.makedirs("images/acs", exist_ok=True)
os.makedirs("images/drive", exist_ok=True)
os.makedirs("images/mobile_compute", exist_ok=True)

def render_svg_to_png(svg_content, png_path):
    if os.path.exists(png_path) and os.path.getsize(png_path) > 1000:
        return
    import re
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
  </defs>
  <rect width="960" height="460" fill="url(#bgGrad)" rx="16"/>
  <rect x="20" y="20" width="920" height="420" fill="none" stroke="#223049" stroke-width="1.5" rx="12"/>
  
  <!-- Header Title -->
  <rect x="40" y="35" width="130" height="26" fill="{accent_color}22" stroke="{accent_color}" stroke-width="1" rx="5"/>
  <text x="105" y="52" fill="{accent_color}" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">{badge_text}</text>
  <text x="480" y="55" fill="#f1f5f9" font-family="-apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">{title}</text>
  <text x="480" y="80" fill="#94a3b8" font-family="-apple-system, sans-serif" font-size="13" text-anchor="middle">{subtitle}</text>

  <!-- Graphic Elements Canvas Area -->
  <g transform="translate(0, 10)">
    {elements_xml}
  </g>

  <!-- Footer Note -->
  <rect x="60" y="405" width="840" height="26" fill="#0f172a" stroke="#223049" rx="5"/>
  <text x="500" y="422" fill="#94a3b8" font-family="monospace" font-size="12" text-anchor="middle">{footer_text}</text>
</svg>"""
    render_svg_to_png(svg, png_path)

print("Batch rendering remaining engineering diagrams...")

# ==========================================
# 1. ADVANCED CONTROL SYSTEMS (ACS) DIAGRAMS
# ==========================================

create_card_diagram(
    "images/acs/similarity_transformation.png",
    "Similarity Transformation: Non-Uniqueness of State Models",
    "Mapping between State Spaces: x(t) = P·z(t) with Invariant Eigenvalues",
    "#38bdf8", "ACS • MOD 1",
    """
    <rect x="80" y="110" width="340" height="230" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="10"/>
    <text x="250" y="140" fill="#38bdf8" font-size="16" font-weight="700" text-anchor="middle">Original Basis: x(t) ∈ ℝⁿ</text>
    <text x="250" y="180" fill="#f1f5f9" font-size="15" text-anchor="middle">ẋ(t) = A·x(t) + B·u(t)</text>
    <text x="250" y="215" fill="#f1f5f9" font-size="15" text-anchor="middle">y(t) = C·x(t) + D·u(t)</text>
    <text x="250" y="260" fill="#fbbf24" font-size="13" text-anchor="middle">det(sI - A) = 0  (Poles: λ₁, λ₂, ..., λₙ)</text>

    <!-- Bi-directional Transformation arrow -->
    <path d="M 430 200 L 515 200" stroke="#f59e0b" stroke-width="3" marker-end="url(#arrow)"/>
    <path d="M 515 240 L 430 240" stroke="#f59e0b" stroke-width="3" marker-end="url(#arrow)"/>
    <text x="475" y="190" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">x = P·z</text>
    <text x="475" y="260" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">z = P⁻¹·x</text>

    <rect x="530" y="110" width="350" height="230" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
    <text x="705" y="140" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">Transformed Basis: z(t) ∈ ℝⁿ</text>
    <text x="705" y="180" fill="#f1f5f9" font-size="15" text-anchor="middle">ż(t) = (P⁻¹AP)·z(t) + (P⁻¹B)·u(t)</text>
    <text x="705" y="215" fill="#f1f5f9" font-size="15" text-anchor="middle">y(t) = (CP)·z(t) + D·u(t)</text>
    <text x="705" y="260" fill="#34d399" font-size="13" text-anchor="middle">A_new = P⁻¹AP  |  B_new = P⁻¹B  |  C_new = CP</text>
    """,
    "Invariant Properties: det(sI - A) = det(sI - A_new) | Identical Transfer Function G(s)"
)

create_card_diagram(
    "images/acs/transfer_function_derivation.png",
    "Derivation of Transfer Function Matrix from State Space Equations",
    "Laplace Transformation of LTI Model: G(s) = C·(sI - A)⁻¹·B + D",
    "#38bdf8", "ACS • MOD 1",
    """
    <rect x="60" y="110" width="220" height="240" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="8"/>
    <text x="170" y="140" fill="#38bdf8" font-size="15" font-weight="700" text-anchor="middle">Time-Domain State Model</text>
    <text x="170" y="185" fill="#f1f5f9" font-size="14" text-anchor="middle">ẋ(t) = Ax(t) + Bu(t)</text>
    <text x="170" y="225" fill="#f1f5f9" font-size="14" text-anchor="middle">y(t) = Cx(t) + Du(t)</text>
    <text x="170" y="280" fill="#94a3b8" font-size="12" text-anchor="middle">Zero Initial Conditions</text>
    <text x="170" y="305" fill="#34d399" font-size="13" text-anchor="middle">x(0) = 0</text>

    <path d="M 290 220 L 350 220" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>

    <rect x="360" y="110" width="240" height="240" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="8"/>
    <text x="480" y="140" fill="#fbbf24" font-size="15" font-weight="700" text-anchor="middle">Laplace Domain Analysis</text>
    <text x="480" y="180" fill="#f1f5f9" font-size="13" text-anchor="middle">sX(s) - x(0) = AX(s) + BU(s)</text>
    <text x="480" y="220" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">(sI - A) X(s) = B U(s)</text>
    <text x="480" y="260" fill="#f1f5f9" font-size="13" text-anchor="middle">X(s) = (sI - A)⁻¹ B U(s)</text>
    <text x="480" y="305" fill="#94a3b8" font-size="12" text-anchor="middle">Substitute into Y(s) = CX + DU</text>

    <path d="M 610 220 L 670 220" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>

    <rect x="680" y="110" width="220" height="240" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="8"/>
    <text x="790" y="140" fill="#34d399" font-size="15" font-weight="700" text-anchor="middle">Transfer Function G(s)</text>
    <text x="790" y="190" fill="#f1f5f9" font-size="14" text-anchor="middle">Y(s) = [C(sI-A)⁻¹B + D] U(s)</text>
    <rect x="695" y="220" width="190" height="60" fill="#0f172a" stroke="#10b981" stroke-width="2" rx="6"/>
    <text x="790" y="255" fill="#34d399" font-size="15" font-weight="700" text-anchor="middle">G(s) = C(sI-A)⁻¹B + D</text>
    <text x="790" y="315" fill="#94a3b8" font-size="12" text-anchor="middle">Poles = Roots of det(sI - A) = 0</text>
    """,
    "G(s) = (C·adj(sI - A)·B) / det(sI - A) + D"
)

create_card_diagram(
    "images/acs/diagonal_canonical_form.png",
    "Diagonal and Jordan Canonical Form Architecture",
    "Decoupled Parallel State Variables with Distinct & Repeated Eigenvalues",
    "#38bdf8", "ACS • MOD 1",
    """
    <!-- Input u(t) distribution -->
    <path d="M 80 220 L 170 220" stroke="#38bdf8" stroke-width="3"/>
    <circle cx="170" cy="220" r="4" fill="#38bdf8"/>
    <text x="110" y="205" fill="#38bdf8" font-size="16" font-weight="700">u(t)</text>
    
    <path d="M 170 220 L 170 140 L 230 140" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>
    <path d="M 170 220 L 230 220" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>
    <path d="M 170 220 L 170 300 L 230 300" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>

    <!-- Channel 1 (lambda 1) -->
    <rect x="240" y="115" width="80" height="50" fill="url(#boxGrad)" stroke="#38bdf8" rx="6"/>
    <text x="280" y="145" fill="#f1f5f9" font-size="13" text-anchor="middle">b₁</text>
    <path d="M 320 140 L 380 140" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>
    <rect x="390" y="110" width="160" height="60" fill="url(#boxGrad)" stroke="#10b981" stroke-width="2" rx="8"/>
    <text x="470" y="135" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">Mode 1: 1/(s - λ₁)</text>
    <text x="470" y="155" fill="#94a3b8" font-size="12" text-anchor="middle">ż₁ = λ₁z₁ + b₁u</text>
    <path d="M 550 140 L 610 140" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>
    <rect x="620" y="115" width="80" height="50" fill="url(#boxGrad)" stroke="#38bdf8" rx="6"/>
    <text x="660" y="145" fill="#f1f5f9" font-size="13" text-anchor="middle">c₁</text>

    <!-- Channel 2 (lambda 2) -->
    <rect x="240" y="195" width="80" height="50" fill="url(#boxGrad)" stroke="#38bdf8" rx="6"/>
    <text x="280" y="225" fill="#f1f5f9" font-size="13" text-anchor="middle">b₂</text>
    <path d="M 320 220 L 380 220" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>
    <rect x="390" y="190" width="160" height="60" fill="url(#boxGrad)" stroke="#10b981" stroke-width="2" rx="8"/>
    <text x="470" y="215" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">Mode 2: 1/(s - λ₂)</text>
    <text x="470" y="235" fill="#94a3b8" font-size="12" text-anchor="middle">ż₂ = λ₂z₂ + b₂u</text>
    <path d="M 550 220 L 610 220" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>
    <rect x="620" y="195" width="80" height="50" fill="url(#boxGrad)" stroke="#38bdf8" rx="6"/>
    <text x="660" y="225" fill="#f1f5f9" font-size="13" text-anchor="middle">c₂</text>

    <!-- Channel 3 (lambda 3) -->
    <rect x="240" y="275" width="80" height="50" fill="url(#boxGrad)" stroke="#38bdf8" rx="6"/>
    <text x="280" y="305" fill="#f1f5f9" font-size="13" text-anchor="middle">b₃</text>
    <path d="M 320 300 L 380 300" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>
    <rect x="390" y="270" width="160" height="60" fill="url(#boxGrad)" stroke="#10b981" stroke-width="2" rx="8"/>
    <text x="470" y="295" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">Mode 3: 1/(s - λ₃)</text>
    <text x="470" y="315" fill="#94a3b8" font-size="12" text-anchor="middle">ż₃ = λ₃z₃ + b₃u</text>
    <path d="M 550 300 L 610 300" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>
    <rect x="620" y="275" width="80" height="50" fill="url(#boxGrad)" stroke="#38bdf8" rx="6"/>
    <text x="660" y="305" fill="#f1f5f9" font-size="13" text-anchor="middle">c₃</text>

    <!-- Summing to Output y -->
    <path d="M 700 140 L 760 140 L 760 205" stroke="#38bdf8" stroke-width="2"/>
    <path d="M 700 220 L 745 220" stroke="#38bdf8" stroke-width="2"/>
    <path d="M 700 300 L 760 300 L 760 235" stroke="#38bdf8" stroke-width="2"/>
    <circle cx="760" cy="220" r="16" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="760" y="226" fill="#38bdf8" font-size="18" font-weight="700" text-anchor="middle">Σ</text>
    <path d="M 776 220 L 870 220" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)"/>
    <text x="830" y="205" fill="#38bdf8" font-size="16" font-weight="700">y(t)</text>
    """,
    "Diagonal Matrix Λ = diag(λ₁, λ₂, λ₃) completely uncouples state differential equations."
)

create_card_diagram(
    "images/acs/field_controlled_dc_motor.png",
    "Field-Controlled DC Servomotor State Model",
    "Constant Armature Current Ia with Control Applied to Field Circuit (Rf, Lf)",
    "#38bdf8", "ACS • MOD 1",
    """
    <!-- Field Circuit -->
    <rect x="70" y="110" width="370" height="240" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="10"/>
    <text x="255" y="140" fill="#38bdf8" font-size="15" font-weight="700" text-anchor="middle">Field Control Circuit (Input: ef(t))</text>
    <!-- Field Resistance Rf -->
    <path d="M 100 210 L 140 210 L 150 195 L 165 225 L 180 195 L 195 225 L 210 195 L 220 210 L 250 210" stroke="#f1f5f9" stroke-width="2.5" fill="none"/>
    <text x="180" y="180" fill="#fbbf24" font-size="14" font-weight="700" text-anchor="middle">Rf</text>
    <!-- Field Inductance Lf -->
    <path d="M 250 210 Q 265 190 280 210 Q 295 190 310 210 Q 325 190 340 210 L 370 210" stroke="#f1f5f9" stroke-width="2.5" fill="none"/>
    <text x="295" y="180" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">Lf</text>
    <!-- Input ef -->
    <circle cx="100" cy="210" r="4" fill="#38bdf8"/>
    <circle cx="100" cy="300" r="4" fill="#38bdf8"/>
    <path d="M 100 300 L 370 300 L 370 210" stroke="#f1f5f9" stroke-width="2.5"/>
    <text x="90" y="260" fill="#38bdf8" font-size="15" font-weight="700" text-anchor="end">ef(t) + -</text>
    <text x="250" y="330" fill="#94a3b8" font-size="13" text-anchor="middle">ef = Rf·if + Lf·(dif/dt)</text>

    <!-- Mechanical Rotor Load -->
    <rect x="490" y="110" width="400" height="240" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
    <text x="690" y="140" fill="#34d399" font-size="15" font-weight="700" text-anchor="middle">Mechanical Inertia &amp; Armature (Ia = const)</text>
    <circle cx="560" cy="210" r="28" fill="#1e293b" stroke="#f59e0b" stroke-width="2.5"/>
    <text x="560" y="217" fill="#fbbf24" font-size="16" font-weight="700" text-anchor="middle">Rotor</text>
    <path d="M 588 210 L 670 210" stroke="#f1f5f9" stroke-width="3"/>
    <rect x="670" y="180" width="55" height="60" fill="#334155" stroke="#f1f5f9" rx="5"/>
    <text x="697" y="216" fill="#f1f5f9" font-size="16" font-weight="700" text-anchor="middle">J</text>
    <path d="M 725 210 L 780 210" stroke="#f1f5f9" stroke-width="3"/>
    <rect x="780" y="185" width="45" height="50" fill="#1e293b" stroke="#10b981" rx="5"/>
    <text x="802" y="216" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">B</text>
    <path d="M 825 210 L 870 210" stroke="#10b981" stroke-width="2.5" marker-end="url(#arrow)"/>
    <text x="690" y="280" fill="#fbbf24" font-size="14" font-weight="700" text-anchor="middle">Torque Tm = Km·if  (Linear with Field Current)</text>
    <text x="690" y="310" fill="#94a3b8" font-size="13" text-anchor="middle">J·(dω/dt) + B·ω = Km·if</text>
    """,
    "State Vector x = [if, ω, θ]ᵀ  |  No Back-EMF in Field Circuit allows purely linear decoupled dynamics"
)

create_card_diagram(
    "images/acs/stm_properties.png",
    "Properties of the State Transition Matrix Φ(t) = e^(At)",
    "Matrix Exponential Mathematical Identities & Uniqueness Proofs",
    "#38bdf8", "ACS • MOD 2",
    """
    <rect x="80" y="110" width="370" height="110" fill="url(#boxGrad)" stroke="#38bdf8" rx="8"/>
    <text x="100" y="140" fill="#38bdf8" font-size="16" font-weight="700">1. Identity Property:</text>
    <text x="100" y="175" fill="#f1f5f9" font-size="16" font-family="monospace">Φ(0) = e^(A·0) = I</text>
    <text x="100" y="200" fill="#94a3b8" font-size="13">State at t=0 equals initial state: x(0) = I·x(0)</text>

    <rect x="490" y="110" width="390" height="110" fill="url(#boxGrad)" stroke="#10b981" rx="8"/>
    <text x="510" y="140" fill="#34d399" font-size="16" font-weight="700">2. Inverse Transition Property:</text>
    <text x="510" y="175" fill="#f1f5f9" font-size="16" font-family="monospace">Φ⁻¹(t) = [e^(At)]⁻¹ = e^(-At) = Φ(-t)</text>
    <text x="510" y="200" fill="#94a3b8" font-size="13">Reversing time transitions backward along state trajectory</text>

    <rect x="80" y="240" width="370" height="110" fill="url(#boxGrad)" stroke="#f59e0b" rx="8"/>
    <text x="100" y="270" fill="#fbbf24" font-size="16" font-weight="700">3. Group Composition Property:</text>
    <text x="100" y="305" fill="#f1f5f9" font-size="16" font-family="monospace">Φ(t₁ + t₂) = Φ(t₁) · Φ(t₂)</text>
    <text x="100" y="330" fill="#94a3b8" font-size="13">Transitioning to t₁ then t₂ equals transition to t₁+t₂</text>

    <rect x="490" y="240" width="390" height="110" fill="url(#boxGrad)" stroke="#a855f7" rx="8"/>
    <text x="510" y="270" fill="#c084fc" font-size="16" font-weight="700">4. Differentiation Property:</text>
    <text x="510" y="305" fill="#f1f5f9" font-size="16" font-family="monospace">dΦ(t)/dt = A·e^(At) = A·Φ(t) = Φ(t)·A</text>
    <text x="510" y="330" fill="#94a3b8" font-size="13">Directly satisfies the homogeneous state equation ẋ = Ax</text>
    """,
    "Non-Singular Matrix: det(Φ(t)) = exp(trace(A)·t) ≠ 0 for all finite time t"
)

create_card_diagram(
    "images/acs/kalman_duality.png",
    "Kalman's Duality Principle: Controllability vs Observability",
    "Equivalence between System (A, B) and Dual System (Aᵀ, Bᵀ)",
    "#38bdf8", "ACS • MOD 3",
    """
    <rect x="80" y="110" width="360" height="230" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="2" rx="10"/>
    <text x="260" y="145" fill="#38bdf8" font-size="17" font-weight="700" text-anchor="middle">Primal System S₁(A, B, C)</text>
    <text x="260" y="185" fill="#f1f5f9" font-size="15" text-anchor="middle">Controllability Matrix Qc:</text>
    <rect x="110" y="200" width="300" height="40" fill="#0f172a" stroke="#38bdf8" rx="6"/>
    <text x="260" y="226" fill="#38bdf8" font-family="monospace" font-size="14" font-weight="700" text-anchor="middle">Qc = [ B | AB | A²B | ... | Aⁿ⁻¹B ]</text>
    <text x="260" y="275" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">rank(Qc) = n ⟺ Completely Controllable</text>
    <text x="260" y="310" fill="#94a3b8" font-size="12" text-anchor="middle">Can steer state from x(0) to any x(t₁) via u(t)</text>

    <!-- Duality Arrows -->
    <path d="M 460 200 L 515 200" stroke="#f59e0b" stroke-width="3" marker-end="url(#arrow)"/>
    <path d="M 515 240 L 460 240" stroke="#f59e0b" stroke-width="3" marker-end="url(#arrow)"/>
    <text x="488" y="185" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">Dual</text>
    <text x="488" y="260" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">A ↔ Aᵀ</text>

    <rect x="530" y="110" width="360" height="230" fill="url(#boxGrad)" stroke="#10b981" stroke-width="2" rx="10"/>
    <text x="710" y="145" fill="#34d399" font-size="17" font-weight="700" text-anchor="middle">Dual System S₂(Aᵀ, Cᵀ, Bᵀ)</text>
    <text x="710" y="185" fill="#f1f5f9" font-size="15" text-anchor="middle">Observability Matrix Qo:</text>
    <rect x="560" y="200" width="300" height="40" fill="#0f172a" stroke="#10b981" rx="6"/>
    <text x="710" y="226" fill="#34d399" font-family="monospace" font-size="14" font-weight="700" text-anchor="middle">Qo = [ Cᵀ | AᵀCᵀ | (Aᵀ)²Cᵀ | ... ]ᵀ</text>
    <text x="710" y="275" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">rank(Qo) = n ⟺ Completely Observable</text>
    <text x="710" y="310" fill="#94a3b8" font-size="12" text-anchor="middle">Can reconstruct internal state x(0) from y(t)</text>
    """,
    "Theorem: Pair (A, B) is controllable if and only if the dual pair (Aᵀ, Bᵀ) is observable."
)

create_card_diagram(
    "images/acs/state_feedback_regulator.png",
    "State Feedback Controller Design by Pole Placement (Ackermann's Formula)",
    "Closed-Loop Regulator: u(t) = -K·x(t) + r(t) Placing Poles at Desired Locations",
    "#38bdf8", "ACS • MOD 3",
    """
    <!-- Input Reference r(t) -->
    <path d="M 60 180 L 150 180" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)"/>
    <text x="90" y="165" fill="#38bdf8" font-size="15" font-weight="700">r(t)</text>

    <!-- Summer -->
    <circle cx="170" cy="180" r="18" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="170" y="186" fill="#38bdf8" font-size="18" font-weight="700" text-anchor="middle">Σ</text>

    <!-- u(t) line -->
    <path d="M 188 180 L 270 180" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)"/>
    <text x="225" y="165" fill="#f59e0b" font-size="15" font-weight="700">u(t)</text>

    <!-- Plant S(A, B, C) -->
    <rect x="275" y="130" width="340" height="100" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="2" rx="10"/>
    <text x="445" y="160" fill="#38bdf8" font-size="16" font-weight="700" text-anchor="middle">Open-Loop Plant: ẋ = Ax + Bu, y = Cx</text>
    <text x="445" y="195" fill="#f1f5f9" font-size="14" text-anchor="middle">Integrator State Dynamics: ∫ dt</text>

    <!-- Output y(t) -->
    <path d="M 615 180 L 860 180" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)"/>
    <text x="820" y="165" fill="#38bdf8" font-size="16" font-weight="700">y(t)</text>

    <!-- State tap x(t) -->
    <circle cx="700" cy="180" r="5" fill="#10b981"/>
    <text x="700" y="165" fill="#34d399" font-size="15" font-weight="700" text-anchor="middle">x(t)</text>
    <path d="M 700 185 L 700 290 L 530 290" stroke="#10b981" stroke-width="2.5" marker-end="url(#arrow)"/>

    <!-- State Feedback Gain Matrix K -->
    <rect x="360" y="260" width="165" height="60" fill="url(#boxGrad)" stroke="#10b981" stroke-width="2" rx="8"/>
    <text x="442" y="295" fill="#34d399" font-size="18" font-weight="700" text-anchor="middle">Gain K = [k₁ ... kₙ]</text>

    <!-- Feedback return to summer -->
    <path d="M 360 290 L 170 290 L 170 203" stroke="#10b981" stroke-width="2.5" marker-end="url(#arrow)"/>
    <text x="185" y="225" fill="#ef4444" font-size="16" font-weight="700">-</text>
    <text x="240" y="310" fill="#94a3b8" font-size="13" text-anchor="middle">Feedback: -Kx(t)</text>

    <!-- Ackermann Formula Box -->
    <rect x="220" y="345" width="520" height="35" fill="#0f172a" stroke="#10b981" rx="6"/>
    <text x="480" y="368" fill="#34d399" font-family="monospace" font-size="14" text-anchor="middle">Ackermann's Formula: K = [0 0 ... 1] · Qc⁻¹ · ϕ_desired(A)</text>
    """,
    "Closed-Loop Characteristic Equation: det(sI - (A - BK)) = ϕ_desired(s)"
)

create_card_diagram(
    "images/acs/lyapunov_stability_contours.png",
    "Lyapunov Direct Method: State Space Energy Contours & Trajectories",
    "Positive Definite V(x) & Negative Definite V̇(x) Trajectories Converging to Origin",
    "#38bdf8", "ACS • MOD 5",
    """
    <!-- Coordinate axes -->
    <line x1="120" y1="230" x2="800" y2="230" stroke="#64748b" stroke-width="1.5"/>
    <line x1="460" y1="90" x2="460" y2="370" stroke="#64748b" stroke-width="1.5"/>
    <text x="815" y="235" fill="#94a3b8" font-size="15">x₁</text>
    <text x="460" y="80" fill="#94a3b8" font-size="15" text-anchor="middle">x₂</text>

    <!-- Elliptical Contours V(x) = c -->
    <ellipse cx="460" cy="230" rx="300" ry="120" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="6,4"/>
    <text x="765" y="210" fill="#38bdf8" font-size="13">V(x) = c₃</text>

    <ellipse cx="460" cy="230" rx="200" ry="80" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="6,4"/>
    <text x="665" y="210" fill="#38bdf8" font-size="13">V(x) = c₂</text>

    <ellipse cx="460" cy="230" rx="100" ry="40" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="6,4"/>
    <text x="565" y="210" fill="#38bdf8" font-size="13">V(x) = c₁ (c₁ &lt; c₂ &lt; c₃)</text>

    <!-- Trajectory spiraling inwards toward (0,0) -->
    <path d="M 680 180 Q 550 140 400 170 Q 300 210 360 270 Q 420 320 540 270 Q 600 230 520 200 Q 470 190 440 210 Q 430 230 460 230" 
          stroke="#10b981" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    
    <!-- Origin Equilibrium Point -->
    <circle cx="460" cy="230" r="6" fill="#fbbf24"/>
    <text x="460" y="255" fill="#fbbf24" font-size="14" font-weight="700" text-anchor="middle">Origin (0,0) Asymptotically Stable</text>

    <rect x="180" y="380" width="560" height="22" fill="#0f172a" stroke="#223049" rx="4"/>
    <text x="460" y="396" fill="#34d399" font-family="monospace" font-size="12" text-anchor="middle">V(x) &gt; 0 (Positive Definite)  &amp;  V̇(x) = grad(V)·f(x) &lt; 0 (Negative Definite)</text>
    """,
    "Lyapunov Theorem: Trajectories cross energy contours inward, dissipating energy to equilibrium."
)

print("Rendered ACS primary diagrams.")

# ==========================================
# 2. ELECTRIC DRIVES (DRIVE) DIAGRAMS
# ==========================================

create_card_diagram(
    "images/drive/electric_drive_block_diagram.png",
    "Modern Electric Drive System: Complete Architectural Block Diagram",
    "Energy Flow: Power Source ➔ Power Modulator ➔ Motor ➔ Mechanical Load ➔ Control Loop",
    "#f59e0b", "DRIVE • MOD 1",
    """
    <!-- Power Source -->
    <rect x="50" y="160" width="120" height="80" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="2" rx="8"/>
    <text x="110" y="195" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">Power Source</text>
    <text x="110" y="220" fill="#94a3b8" font-size="12" text-anchor="middle">AC Grid / DC Bus</text>

    <path d="M 175 200 L 235 200" stroke="#f59e0b" stroke-width="3" marker-end="url(#arrow)"/>

    <!-- Power Modulator (Inverter/Converter/Chopper) -->
    <rect x="240" y="150" width="160" height="100" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="2.5" rx="10"/>
    <text x="320" y="185" fill="#fbbf24" font-size="15" font-weight="700" text-anchor="middle">Power Modulator</text>
    <text x="320" y="210" fill="#f1f5f9" font-size="12" text-anchor="middle">VSI / Chopper / Rectifier</text>
    <text x="320" y="230" fill="#94a3b8" font-size="11" text-anchor="middle">IGBT / Thyristor Bridge</text>

    <path d="M 405 200 L 465 200" stroke="#f59e0b" stroke-width="3" marker-end="url(#arrow)"/>

    <!-- Electric Motor -->
    <circle cx="510" cy="200" r="42" fill="url(#boxGrad)" stroke="#10b981" stroke-width="3"/>
    <text x="510" y="195" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">Motor</text>
    <text x="510" y="215" fill="#f1f5f9" font-size="12" text-anchor="middle">DC / IM / PMSM</text>

    <!-- Mechanical Shaft -->
    <rect x="555" y="195" width="80" height="10" fill="#64748b"/>
    <text x="595" y="185" fill="#f59e0b" font-size="12" font-weight="700" text-anchor="middle">Torque T</text>

    <!-- Mechanical Load -->
    <rect x="640" y="160" width="130" height="80" fill="url(#boxGrad)" stroke="#a855f7" stroke-width="2" rx="8"/>
    <text x="705" y="195" fill="#c084fc" font-size="14" font-weight="700" text-anchor="middle">Load Machine</text>
    <text x="705" y="220" fill="#94a3b8" font-size="12" text-anchor="middle">Hoist/Pump/Traction</text>

    <!-- Feedback Sensors & Control Unit (Bottom) -->
    <path d="M 705 245 L 705 320 L 590 320" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>
    <text x="660" y="310" fill="#94a3b8" font-size="12">Speed ω</text>

    <circle cx="435" cy="200" r="4" fill="#38bdf8"/>
    <path d="M 435 200 L 435 320 L 480 320" stroke="#38bdf8" stroke-width="2"/>
    <text x="430" y="270" fill="#94a3b8" font-size="12" text-anchor="end">Current i(t)</text>

    <!-- Controller Unit -->
    <rect x="240" y="285" width="340" height="70" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="2" rx="8"/>
    <text x="410" y="315" fill="#38bdf8" font-size="15" font-weight="700" text-anchor="middle">Microcontroller / DSP Control Unit</text>
    <text x="410" y="338" fill="#f1f5f9" font-size="12" text-anchor="middle">PI Regulators, SVPWM Gate Firing, Closed-Loop Protection</text>

    <!-- Firing pulses up to Modulator -->
    <path d="M 320 285 L 320 255" stroke="#f59e0b" stroke-width="2.5" marker-end="url(#arrow)"/>
    <text x="330" y="275" fill="#fbbf24" font-size="11">Gate Pulses</text>
    """,
    "Fundamental Dynamics: T - T_l = J·(dω/dt) + B·ω  |  Closed-Loop Feedback enforces torque & speed tracking"
)

create_card_diagram(
    "images/drive/cascade_speed_control.png",
    "Closed-Loop Cascade Speed Control Architecture",
    "Inner Fast Current/Torque Loop with Outer Robust Speed Feedback Loop",
    "#f59e0b", "DRIVE • MOD 2",
    """
    <!-- Speed Reference -->
    <path d="M 50 180 L 120 180" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>
    <text x="80" y="165" fill="#38bdf8" font-size="14" font-weight="700">ω_ref</text>

    <!-- Outer Speed Summer -->
    <circle cx="135" cy="180" r="15" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="135" y="185" fill="#38bdf8" font-size="16" font-weight="700" text-anchor="middle">Σ</text>

    <!-- Speed PI Controller -->
    <path d="M 150 180 L 205 180" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>
    <rect x="210" y="150" width="120" height="60" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="2" rx="6"/>
    <text x="270" y="175" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">Speed Controller</text>
    <text x="270" y="195" fill="#f1f5f9" font-size="12" text-anchor="middle">PI (Kp_ω + Ki_ω/s)</text>

    <!-- Current Reference I_ref with Limiter -->
    <path d="M 330 180 L 375 180" stroke="#f59e0b" stroke-width="2.5" marker-end="url(#arrow)"/>
    <rect x="380" y="160" width="40" height="40" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5" rx="4"/>
    <path d="M 388 188 L 398 188 L 405 172 L 414 172" stroke="#fbbf24" stroke-width="2" fill="none"/>
    <text x="400" y="150" fill="#fbbf24" font-size="11" text-anchor="middle">Limiter</text>

    <!-- Inner Current Summer -->
    <path d="M 425 180 L 465 180" stroke="#f59e0b" stroke-width="2.5" marker-end="url(#arrow)"/>
    <circle cx="480" cy="180" r="15" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <text x="480" y="185" fill="#fbbf24" font-size="16" font-weight="700" text-anchor="middle">Σ</text>

    <!-- Inner Current PI Controller -->
    <path d="M 495 180 L 535 180" stroke="#f59e0b" stroke-width="2.5" marker-end="url(#arrow)"/>
    <rect x="540" y="150" width="120" height="60" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="2" rx="6"/>
    <text x="600" y="175" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">Current Controller</text>
    <text x="600" y="195" fill="#f1f5f9" font-size="12" text-anchor="middle">PI (Kp_i + Ki_i/s)</text>

    <!-- Power Converter & Motor -->
    <path d="M 660 180 L 710 180" stroke="#f59e0b" stroke-width="2.5" marker-end="url(#arrow)"/>
    <rect x="715" y="140" width="150" height="80" fill="url(#boxGrad)" stroke="#10b981" stroke-width="2" rx="8"/>
    <text x="790" y="170" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">Converter &amp; DC Motor</text>
    <text x="790" y="195" fill="#f1f5f9" font-size="12" text-anchor="middle">Armature + Inertia J</text>

    <!-- Output Speed -->
    <path d="M 865 180 L 930 180" stroke="#10b981" stroke-width="3" marker-end="url(#arrow)"/>
    <text x="900" y="165" fill="#34d399" font-size="15" font-weight="700">ω(t)</text>

    <!-- Inner current feedback -->
    <circle cx="700" cy="180" r="4" fill="#f59e0b"/>
    <path d="M 700 180 L 700 250 L 480 250 L 480 200" stroke="#f59e0b" stroke-width="2" marker-end="url(#arrow)"/>
    <text x="580" y="240" fill="#fbbf24" font-size="12" text-anchor="middle">Fast Current Feedback ia(t)</text>

    <!-- Outer speed feedback -->
    <circle cx="890" cy="180" r="4" fill="#38bdf8"/>
    <path d="M 890 180 L 890 310 L 135 310 L 135 200" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>
    <text x="510" y="300" fill="#38bdf8" font-size="12" text-anchor="middle">Outer Speed Feedback Loop (Tachometer / Encoder ω)</text>
    """,
    "Bandwidth Hierarchy: Inner current loop operates ~10x faster than outer mechanical speed loop"
)

create_card_diagram(
    "images/drive/vf_speed_control.png",
    "Variable Frequency (V/f) Speed Control of 3-Phase Induction Motor",
    "Constant Air-Gap Flux Operation with Low-Frequency Voltage Boost",
    "#f59e0b", "DRIVE • MOD 3",
    """
    <!-- Left: V vs f Linear Characteristic -->
    <rect x="60" y="110" width="400" height="240" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="10"/>
    <text x="260" y="140" fill="#fbbf24" font-size="15" font-weight="700" text-anchor="middle">Stator Voltage V vs Frequency f</text>
    <line x1="100" y1="310" x2="420" y2="310" stroke="#64748b" stroke-width="1.5"/>
    <line x1="100" y1="310" x2="100" y2="160" stroke="#64748b" stroke-width="1.5"/>
    <text x="430" y="315" fill="#94a3b8" font-size="13">f (Hz)</text>
    <text x="95" y="150" fill="#94a3b8" font-size="13" text-anchor="end">V (Volts)</text>

    <!-- V/f curve: boost at start, linear to rated, flat in field weakening -->
    <path d="M 100 290 L 140 270 L 320 180 L 420 180" stroke="#38bdf8" stroke-width="3" fill="none"/>
    <circle cx="320" cy="180" r="4" fill="#f59e0b"/>
    <line x1="320" y1="180" x2="320" y2="310" stroke="#94a3b8" stroke-dasharray="4,4"/>
    <text x="320" y="330" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle">f_rated (50Hz)</text>
    <text x="220" y="210" fill="#38bdf8" font-size="12" font-weight="700">Constant V/f (Flux Φ = const)</text>
    <text x="370" y="165" fill="#fca5a5" font-size="12" font-weight="700">Field Weakening</text>
    <text x="135" y="295" fill="#fbbf24" font-size="11">V_boost</text>

    <!-- Right: Torque vs Speed Family of Curves -->
    <rect x="490" y="110" width="410" height="240" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
    <text x="695" y="140" fill="#34d399" font-size="15" font-weight="700" text-anchor="middle">Torque-Speed Family (Constant T_max)</text>
    <line x1="520" y1="310" x2="870" y2="310" stroke="#64748b" stroke-width="1.5"/>
    <line x1="530" y1="310" x2="530" y2="160" stroke="#64748b" stroke-width="1.5"/>
    <text x="880" y="315" fill="#94a3b8" font-size="13">Speed ω</text>
    <text x="525" y="150" fill="#94a3b8" font-size="13" text-anchor="end">Torque T</text>

    <!-- 3 parallel shifted torque curves with identical peak T_max -->
    <path d="M 530 260 Q 560 170 590 190 L 610 310" stroke="#10b981" stroke-width="2.5" fill="none"/>
    <path d="M 530 275 Q 640 170 670 190 L 690 310" stroke="#38bdf8" stroke-width="2.5" fill="none"/>
    <path d="M 530 290 Q 720 170 750 190 L 770 310" stroke="#f59e0b" stroke-width="2.5" fill="none"/>
    <line x1="530" y1="170" x2="770" y2="170" stroke="#ef4444" stroke-dasharray="4,4"/>
    <text x="780" y="175" fill="#ef4444" font-size="12" font-weight="700">T_breakdown = const</text>
    <text x="610" y="325" fill="#94a3b8" font-size="11">f₁</text>
    <text x="690" y="325" fill="#94a3b8" font-size="11">f₂</text>
    <text x="770" y="325" fill="#94a3b8" font-size="11">f_rated</text>
    """,
    "Φ_ag ≈ V/f = const guarantees full rated motor breakdown torque across entire operating speed range"
)

create_card_diagram(
    "images/drive/svpwm_inverter.png",
    "Space Vector PWM (SVPWM): Voltage Vectors & Hexagonal Sectors",
    "8 Switching States: 6 Active Vectors (V₁-V₆) and 2 Zero Vectors (V₀, V₇)",
    "#f59e0b", "DRIVE • MOD 5",
    """
    <!-- Hexagon coordinate center -->
    <g transform="translate(480, 240)">
      <!-- Hexagon outer boundary -->
      <polygon points="0,-130 112,-65 112,65 0,130 -112,65 -112,-65" fill="#0f172a" stroke="#223049" stroke-width="2"/>
      
      <!-- 6 Active Voltage Vectors -->
      <line x1="0" y1="0" x2="112" y2="0" stroke="#f59e0b" stroke-width="3" marker-end="url(#arrow)"/>
      <text x="125" y="5" fill="#fbbf24" font-size="13" font-weight="700">V₁(100) 0°</text>

      <line x1="0" y1="0" x2="56" y2="-97" stroke="#f59e0b" stroke-width="3" marker-end="url(#arrow)"/>
      <text x="65" y="-105" fill="#fbbf24" font-size="13" font-weight="700">V₂(110) 60°</text>

      <line x1="0" y1="0" x2="-56" y2="-97" stroke="#f59e0b" stroke-width="3" marker-end="url(#arrow)"/>
      <text x="-125" y="-105" fill="#fbbf24" font-size="13" font-weight="700">V₃(010) 120°</text>

      <line x1="0" y1="0" x2="-112" y2="0" stroke="#f59e0b" stroke-width="3" marker-end="url(#arrow)"/>
      <text x="-185" y="5" fill="#fbbf24" font-size="13" font-weight="700">V₄(011) 180°</text>

      <line x1="0" y1="0" x2="-56" y2="97" stroke="#f59e0b" stroke-width="3" marker-end="url(#arrow)"/>
      <text x="-125" y="115" fill="#fbbf24" font-size="13" font-weight="700">V₅(001) 240°</text>

      <line x1="0" y1="0" x2="56" y2="97" stroke="#f59e0b" stroke-width="3" marker-end="url(#arrow)"/>
      <text x="65" y="115" fill="#fbbf24" font-size="13" font-weight="700">V₆(101) 300°</text>

      <!-- Rotating Reference Vector V_ref in Sector 1 -->
      <line x1="0" y1="0" x2="75" y2="-45" stroke="#38bdf8" stroke-width="3.5" marker-end="url(#arrow)"/>
      <text x="85" y="-55" fill="#38bdf8" font-size="15" font-weight="700">V_ref (θ)</text>
      
      <!-- Sector labels -->
      <text x="45" y="-40" fill="#34d399" font-size="14" font-weight="700">Sector I</text>
      <text x="-20" y="-70" fill="#94a3b8" font-size="12">Sector II</text>
      <text x="-70" y="-30" fill="#94a3b8" font-size="12">Sector III</text>
      <text x="-70" y="40" fill="#94a3b8" font-size="12">Sector IV</text>
      <text x="-20" y="75" fill="#94a3b8" font-size="12">Sector V</text>
      <text x="40" y="45" fill="#94a3b8" font-size="12">Sector VI</text>

      <!-- Center Zero Vectors -->
      <circle cx="0" cy="0" r="7" fill="#ef4444"/>
      <text x="0" y="20" fill="#fca5a5" font-size="11" text-anchor="middle">V₀(000), V₇(111)</text>
    </g>
    """,
    "Synthesis in Sector I: V_ref·Ts = V₁·T₁ + V₂·T₂ + V₀·T₀  |  Yields 15% higher DC-bus voltage utilization"
)

create_card_diagram(
    "images/drive/field_oriented_control.png",
    "Field-Oriented Control (FOC / Vector Control) of Induction Motor",
    "Decoupling Stator Currents into Flux (i_ds) and Torque (i_qs) Components",
    "#f59e0b", "DRIVE • MOD 5",
    """
    <!-- Controller Blocks -->
    <rect x="50" y="120" width="160" height="90" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="2" rx="8"/>
    <text x="130" y="150" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">Speed Controller</text>
    <text x="130" y="175" fill="#f1f5f9" font-size="13" text-anchor="middle">PI (ω_ref - ω)</text>
    <text x="130" y="195" fill="#34d399" font-size="12" text-anchor="middle">Output: i_qs_ref (Torque)</text>

    <path d="M 215 165 L 295 165" stroke="#34d399" stroke-width="2.5" marker-end="url(#arrow)"/>

    <!-- d-q PI Current Regulators -->
    <rect x="300" y="120" width="180" height="180" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="2" rx="10"/>
    <text x="390" y="145" fill="#fbbf24" font-size="14" font-weight="700" text-anchor="middle">d-q Current Regulators</text>
    <text x="390" y="180" fill="#34d399" font-size="13" text-anchor="middle">PI ➔ v_qs* (Torque V)</text>
    <text x="390" y="240" fill="#38bdf8" font-size="13" text-anchor="middle">PI ➔ v_ds* (Flux V)</text>
    <text x="390" y="280" fill="#94a3b8" font-size="11" text-anchor="middle">Input: i_ds_ref = const</text>

    <!-- Inverse Park Transform (d-q -> alpha-beta) -->
    <path d="M 485 180 L 535 180" stroke="#f59e0b" stroke-width="2.5" marker-end="url(#arrow)"/>
    <rect x="540" y="130" width="140" height="100" fill="url(#boxGrad)" stroke="#a855f7" stroke-width="2" rx="8"/>
    <text x="610" y="160" fill="#c084fc" font-size="14" font-weight="700" text-anchor="middle">Inverse Park &amp; Clarke</text>
    <text x="610" y="185" fill="#f1f5f9" font-size="12" text-anchor="middle">dq0 ➔ αβ ➔ abc</text>
    <text x="610" y="210" fill="#94a3b8" font-size="11" text-anchor="middle">Rotor Flux Angle θ_e</text>

    <!-- SVPWM Inverter & Motor -->
    <path d="M 685 180 L 735 180" stroke="#f59e0b" stroke-width="2.5" marker-end="url(#arrow)"/>
    <rect x="740" y="125" width="160" height="110" fill="url(#boxGrad)" stroke="#10b981" stroke-width="2" rx="8"/>
    <text x="820" y="155" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">SVPWM Inverter</text>
    <text x="820" y="180" fill="#f1f5f9" font-size="13" text-anchor="middle">3-Phase Induction Motor</text>
    <text x="820" y="210" fill="#94a3b8" font-size="11" text-anchor="middle">Rotor Flux Orientation</text>

    <!-- Feedback paths -->
    <path d="M 820 240 L 820 330 L 610 330" stroke="#38bdf8" stroke-width="2"/>
    <rect x="470" y="300" width="140" height="60" fill="#0f172a" stroke="#38bdf8" rx="6"/>
    <text x="540" y="325" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">Park / Clarke Transform</text>
    <text x="540" y="345" fill="#f1f5f9" font-size="11" text-anchor="middle">abc ➔ αβ ➔ dq0</text>
    <path d="M 470 330 L 390 330 L 390 305" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>
    """,
    "Decoupling Principle: Induction Motor controlled like a separately excited DC motor (Flux and Torque independent)"
)

print("Rendered Electric Drives primary diagrams.")

# ==========================================
# 3. MOBILE COMPUTING (CST415) DIAGRAMS
# ==========================================

create_card_diagram(
    "images/mobile_compute/multiple_access_techniques.png",
    "Multiple Access Procedures: FDMA, TDMA, CDMA, and SDMA",
    "Resource Orthogonality across Frequency, Time, Spreading Codes, and Spatial Direction",
    "#10b981", "MOBILE • MOD 2",
    """
    <!-- 4 Sub-blocks -->
    <rect x="60" y="110" width="180" height="230" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="2" rx="8"/>
    <text x="150" y="140" fill="#38bdf8" font-size="16" font-weight="700" text-anchor="middle">FDMA (Frequency)</text>
    <rect x="80" y="160" width="140" height="110" fill="#0f172a" stroke="#38bdf8" stroke-dasharray="3,3" rx="4"/>
    <line x1="80" y1="185" x2="220" y2="185" stroke="#38bdf8"/>
    <line x1="80" y1="215" x2="220" y2="215" stroke="#38bdf8"/>
    <line x1="80" y1="245" x2="220" y2="245" stroke="#38bdf8"/>
    <text x="150" y="175" fill="#f1f5f9" font-size="11" text-anchor="middle">User 1 (f₁)</text>
    <text x="150" y="205" fill="#f1f5f9" font-size="11" text-anchor="middle">User 2 (f₂)</text>
    <text x="150" y="235" fill="#f1f5f9" font-size="11" text-anchor="middle">User 3 (f₃)</text>
    <text x="150" y="300" fill="#94a3b8" font-size="12" text-anchor="middle">Guard Bands Required</text>

    <rect x="270" y="110" width="180" height="230" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="2" rx="8"/>
    <text x="360" y="140" fill="#fbbf24" font-size="16" font-weight="700" text-anchor="middle">TDMA (Time)</text>
    <rect x="290" y="160" width="140" height="110" fill="#0f172a" stroke="#f59e0b" stroke-dasharray="3,3" rx="4"/>
    <line x1="335" y1="160" x2="335" y2="270" stroke="#f59e0b"/>
    <line x1="385" y1="160" x2="385" y2="270" stroke="#f59e0b"/>
    <text x="312" y="220" fill="#f1f5f9" font-size="11" text-anchor="middle">Slot 1</text>
    <text x="360" y="220" fill="#f1f5f9" font-size="11" text-anchor="middle">Slot 2</text>
    <text x="407" y="220" fill="#f1f5f9" font-size="11" text-anchor="middle">Slot 3</text>
    <text x="360" y="300" fill="#94a3b8" font-size="12" text-anchor="middle">Burst Sync Required</text>

    <rect x="480" y="110" width="180" height="230" fill="url(#boxGrad)" stroke="#10b981" stroke-width="2" rx="8"/>
    <text x="570" y="140" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">CDMA (Code)</text>
    <rect x="500" y="160" width="140" height="110" fill="#0f172a" stroke="#10b981" stroke-dasharray="3,3" rx="4"/>
    <text x="570" y="185" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">Same Freq + Time</text>
    <text x="570" y="210" fill="#f1f5f9" font-size="11" text-anchor="middle">Code c₁(t) · c₂(t) = 0</text>
    <text x="570" y="235" fill="#f1f5f9" font-size="11" text-anchor="middle">Spread Spectrum</text>
    <text x="570" y="260" fill="#fbbf24" font-size="11" text-anchor="middle">Walsh Orthogonal</text>
    <text x="570" y="300" fill="#94a3b8" font-size="12" text-anchor="middle">Power Control Needed</text>

    <rect x="690" y="110" width="180" height="230" fill="url(#boxGrad)" stroke="#a855f7" stroke-width="2" rx="8"/>
    <text x="780" y="140" fill="#c084fc" font-size="16" font-weight="700" text-anchor="middle">SDMA (Space)</text>
    <rect x="710" y="160" width="140" height="110" fill="#0f172a" stroke="#a855f7" stroke-dasharray="3,3" rx="4"/>
    <circle cx="780" cy="215" r="35" fill="none" stroke="#a855f7" stroke-dasharray="2,2"/>
    <path d="M 780 215 Q 815 170 830 190 Q 805 215 780 215" fill="#c084fc" opacity="0.6"/>
    <path d="M 780 215 Q 730 250 720 230 Q 750 215 780 215" fill="#38bdf8" opacity="0.6"/>
    <text x="780" y="300" fill="#94a3b8" font-size="12" text-anchor="middle">Smart Beamforming</text>
    """,
    "Spectral Efficiency: 1G (FDMA) ➔ 2G (FDMA+TDMA) ➔ 3G (WCDMA) ➔ 4G/5G (OFDMA + Massive MIMO SDMA)"
)

create_card_diagram(
    "images/mobile_compute/gsm_security_a3_a5_a8.png",
    "GSM Cryptographic Security Architecture: A3, A8, and A5 Algorithms",
    "Challenge-Response Authentication (A3), Key Derivation (A8), and Air Stream Cipher (A5)",
    "#10b981", "MOBILE • MOD 2",
    """
    <!-- AUC / HLR Box -->
    <rect x="60" y="110" width="230" height="230" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="2" rx="10"/>
    <text x="175" y="135" fill="#38bdf8" font-size="15" font-weight="700" text-anchor="middle">AUC / HLR (Operator Core)</text>
    <text x="175" y="165" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">Subscriber Secret Ki (128-bit)</text>
    <rect x="80" y="180" width="190" height="65" fill="#0f172a" stroke="#38bdf8" rx="6"/>
    <text x="175" y="200" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">Generate RAND (128-bit)</text>
    <text x="175" y="220" fill="#34d399" font-size="12" text-anchor="middle">A3(Ki, RAND) ➔ SRES (32b)</text>
    <text x="175" y="235" fill="#fbbf24" font-size="12" text-anchor="middle">A8(Ki, RAND) ➔ Kc (64b)</text>
    <text x="175" y="270" fill="#cbd5e1" font-size="12" text-anchor="middle">Triplet = (RAND, SRES, Kc)</text>
    <text x="175" y="315" fill="#94a3b8" font-size="11" text-anchor="middle">Dispatched to Visited VLR</text>

    <!-- Challenge / Response Flow -->
    <path d="M 295 180 L 415 180" stroke="#f59e0b" stroke-width="2.5" marker-end="url(#arrow)"/>
    <text x="355" y="170" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle">1. RAND Challenge</text>

    <path d="M 415 240 L 295 240" stroke="#34d399" stroke-width="2.5" marker-end="url(#arrow)"/>
    <text x="355" y="260" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">2. SRES' Response</text>

    <!-- SIM / Mobile Station -->
    <rect x="420" y="110" width="230" height="230" fill="url(#boxGrad)" stroke="#10b981" stroke-width="2" rx="10"/>
    <text x="535" y="135" fill="#34d399" font-size="15" font-weight="700" text-anchor="middle">SIM Card in Mobile Station</text>
    <text x="535" y="165" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">Secret Key Ki in Secure Silicon</text>
    <rect x="440" y="180" width="190" height="65" fill="#0f172a" stroke="#10b981" rx="6"/>
    <text x="535" y="200" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">Calculate in SIM:</text>
    <text x="535" y="220" fill="#34d399" font-size="12" text-anchor="middle">A3(Ki, RAND) ➔ SRES' (32b)</text>
    <text x="535" y="235" fill="#fbbf24" font-size="12" text-anchor="middle">A8(Ki, RAND) ➔ Kc (64b)</text>
    <text x="535" y="280" fill="#f1f5f9" font-size="12" text-anchor="middle">VLR checks: SRES' == SRES</text>
    <text x="535" y="315" fill="#94a3b8" font-size="11" text-anchor="middle">If MATCH ➔ Access Granted</text>

    <!-- A5 Stream Cipher (Air Interface) -->
    <rect x="680" y="110" width="220" height="230" fill="url(#boxGrad)" stroke="#a855f7" stroke-width="2" rx="10"/>
    <text x="790" y="135" fill="#c084fc" font-size="15" font-weight="700" text-anchor="middle">A5 Stream Cipher</text>
    <text x="790" y="165" fill="#94a3b8" font-size="12" text-anchor="middle">Air Interface Encryption</text>
    <rect x="700" y="180" width="180" height="60" fill="#0f172a" stroke="#a855f7" rx="6"/>
    <text x="790" y="205" fill="#c084fc" font-size="13" font-weight="700" text-anchor="middle">3 LFSRs (A5/1)</text>
    <text x="790" y="225" fill="#f1f5f9" font-size="11" text-anchor="middle">Inputs: Kc + Frame Number</text>
    <text x="790" y="270" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">Ciphertext = Data ⊕ Keystream</text>
    <text x="790" y="315" fill="#94a3b8" font-size="11" text-anchor="middle">Protects Voice &amp; Data bursts</text>
    """,
    "Ki is NEVER transmitted over the air. Only RAND challenge and SRES response are sent."
)

create_card_diagram(
    "images/mobile_compute/wll_architecture.png",
    "Wireless Local Loop (WLL / Fixed Wireless Access) Architecture",
    "Replacing Physical Copper Last-Mile with High-Reliability Radio Frequency Links",
    "#10b981", "MOBILE • MOD 4",
    """
    <!-- Core PSTN / PDN -->
    <rect x="60" y="130" width="150" height="180" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="2" rx="10"/>
    <text x="135" y="160" fill="#38bdf8" font-size="15" font-weight="700" text-anchor="middle">PSTN / Core Net</text>
    <text x="135" y="195" fill="#f1f5f9" font-size="13" text-anchor="middle">Local Exchange (LE)</text>
    <text x="135" y="235" fill="#94a3b8" font-size="12" text-anchor="middle">V5.1 / V5.2 Digital</text>
    <text x="135" y="260" fill="#94a3b8" font-size="12" text-anchor="middle">Signaling Interface</text>

    <path d="M 215 220 L 275 220" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>

    <!-- WLL Controller (WAC) -->
    <rect x="280" y="130" width="160" height="180" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="2" rx="10"/>
    <text x="360" y="160" fill="#fbbf24" font-size="15" font-weight="700" text-anchor="middle">WLL Controller</text>
    <text x="360" y="195" fill="#f1f5f9" font-size="12" text-anchor="middle">• Call Processing</text>
    <text x="360" y="220" fill="#f1f5f9" font-size="12" text-anchor="middle">• Radio Scheduling</text>
    <text x="360" y="245" fill="#f1f5f9" font-size="12" text-anchor="middle">• Subscriber Auth</text>
    <text x="360" y="270" fill="#94a3b8" font-size="11" text-anchor="middle">Traffic Concentration</text>

    <path d="M 445 220 L 505 220" stroke="#f59e0b" stroke-width="2.5" marker-end="url(#arrow)"/>

    <!-- Base Station Tower (WAS) -->
    <rect x="510" y="130" width="160" height="180" fill="url(#boxGrad)" stroke="#10b981" stroke-width="2" rx="10"/>
    <text x="590" y="160" fill="#34d399" font-size="15" font-weight="700" text-anchor="middle">Base Station (BS)</text>
    <text x="590" y="195" fill="#f1f5f9" font-size="12" text-anchor="middle">Multi-Sector Antenna</text>
    <path d="M 590 205 L 590 250 M 575 220 L 605 220 M 580 235 L 600 235" stroke="#34d399" stroke-width="2"/>
    <text x="590" y="280" fill="#94a3b8" font-size="11" text-anchor="middle">Coverage: 3 - 15 km</text>

    <!-- Wireless Radio Link (Curves) -->
    <path d="M 675 200 Q 700 170 725 200" stroke="#10b981" stroke-width="3" fill="none"/>
    <path d="M 685 190 Q 710 160 735 190" stroke="#10b981" stroke-width="2" fill="none"/>
    <text x="705" y="150" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">Radio Link</text>

    <!-- Customer Premises Equipment (CPE) -->
    <rect x="740" y="130" width="160" height="180" fill="url(#boxGrad)" stroke="#a855f7" stroke-width="2" rx="10"/>
    <text x="820" y="160" fill="#c084fc" font-size="15" font-weight="700" text-anchor="middle">Subscriber Premises</text>
    <text x="820" y="195" fill="#f1f5f9" font-size="12" text-anchor="middle">Outdoor Antenna (ODU)</text>
    <text x="820" y="220" fill="#f1f5f9" font-size="12" text-anchor="middle">Indoor Unit (IDU)</text>
    <text x="820" y="250" fill="#38bdf8" font-size="12" text-anchor="middle">RJ-11 Phone / Internet</text>
    <text x="820" y="280" fill="#94a3b8" font-size="11" text-anchor="middle">Standard Dial Tone</text>
    """,
    "Rapid Deployment: Eliminates 70% of infrastructure civil engineering trenching costs"
)

create_card_diagram(
    "images/mobile_compute/interframe_spaces.png",
    "IEEE 802.11 Interframe Spaces (IFS) Priority Hierarchy",
    "Collision Avoidance via SIFS < PIFS < DIFS < EIFS Time Windows",
    "#10b981", "MOBILE • MOD 4",
    """
    <rect x="80" y="130" width="800" height="220" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
    
    <!-- Timeline Axis -->
    <line x1="120" y1="260" x2="840" y2="260" stroke="#f1f5f9" stroke-width="2.5" marker-end="url(#arrow)"/>
    <text x="850" y="265" fill="#94a3b8" font-size="13">Time t</text>
    
    <!-- Medium Busy block -->
    <rect x="120" y="180" width="160" height="80" fill="#ef4444" rx="6"/>
    <text x="200" y="225" fill="#ffffff" font-size="14" font-weight="700" text-anchor="middle">Medium Busy</text>

    <!-- SIFS (Shortest) -->
    <rect x="290" y="195" width="80" height="65" fill="#38bdf8" rx="4"/>
    <text x="330" y="225" fill="#041226" font-size="12" font-weight="700" text-anchor="middle">SIFS</text>
    <text x="330" y="245" fill="#041226" font-size="10" text-anchor="middle">ACK/CTS</text>

    <!-- PIFS -->
    <rect x="290" y="160" width="150" height="30" fill="#fbbf24" rx="4"/>
    <text x="365" y="180" fill="#1f1202" font-size="12" font-weight="700" text-anchor="middle">PIFS (PCF Mode Polling)</text>

    <!-- DIFS -->
    <rect x="290" y="120" width="230" height="35" fill="#10b981" rx="4"/>
    <text x="405" y="142" fill="#021a11" font-size="13" font-weight="700" text-anchor="middle">DIFS (Standard DCF Data Transmission)</text>

    <!-- Contention Window / Backoff -->
    <rect x="525" y="180" width="180" height="80" fill="#334155" stroke="#f1f5f9" stroke-dasharray="3,3" rx="6"/>
    <text x="615" y="215" fill="#f1f5f9" font-size="13" font-weight="700" text-anchor="middle">Contention Window</text>
    <text x="615" y="238" fill="#94a3b8" font-size="11" text-anchor="middle">Random Backoff Slots</text>

    <!-- Next Frame Tx -->
    <rect x="710" y="180" width="120" height="80" fill="#10b981" rx="6"/>
    <text x="770" y="225" fill="#ffffff" font-size="13" font-weight="700" text-anchor="middle">Frame Tx</text>

    <text x="480" y="325" fill="#f1f5f9" font-size="14" font-weight="700" text-anchor="middle">Mathematical Inequality: SIFS &lt; PIFS &lt; DIFS &lt; EIFS</text>
    """,
    "High priority frames (ACK/CTS) wait only SIFS, preempting other stations and preventing collisions."
)

create_card_diagram(
    "images/mobile_compute/cellular_evolution_2g_to_5g.png",
    "Generational Cellular Evolution: 2G GSM to Cloud-Native 5G SBA",
    "Evolution from Circuit-Switched Voice to 20 Gbps Sub-Millisecond 5G Network Slicing",
    "#10b981", "MOBILE • MOD 5",
    """
    <!-- 2G -->
    <rect x="50" y="110" width="190" height="230" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="2" rx="8"/>
    <text x="145" y="138" fill="#38bdf8" font-size="16" font-weight="700" text-anchor="middle">2G (GSM / GPRS)</text>
    <text x="145" y="165" fill="#f1f5f9" font-size="12" text-anchor="middle">Speed: 9.6 - 115 kbps</text>
    <text x="145" y="190" fill="#94a3b8" font-size="12" text-anchor="middle">Latency: ~600 ms</text>
    <text x="145" y="220" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">Circuit-Switched</text>
    <text x="145" y="245" fill="#cbd5e1" font-size="11" text-anchor="middle">TDMA / FDMA Voice</text>
    <text x="145" y="270" fill="#cbd5e1" font-size="11" text-anchor="middle">SMS, Monolithic Core</text>
    <text x="145" y="315" fill="#94a3b8" font-size="11" text-anchor="middle">Era: 1990s</text>

    <!-- 3G -->
    <rect x="260" y="110" width="190" height="230" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="2" rx="8"/>
    <text x="355" y="138" fill="#fbbf24" font-size="16" font-weight="700" text-anchor="middle">3G (UMTS / HSPA)</text>
    <text x="355" y="165" fill="#f1f5f9" font-size="12" text-anchor="middle">Speed: 2 - 42 Mbps</text>
    <text x="355" y="190" fill="#94a3b8" font-size="12" text-anchor="middle">Latency: ~100 ms</text>
    <text x="355" y="220" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">Dual Domain Core</text>
    <text x="355" y="245" fill="#cbd5e1" font-size="11" text-anchor="middle">WCDMA (5MHz)</text>
    <text x="355" y="270" fill="#cbd5e1" font-size="11" text-anchor="middle">Mobile Web &amp; Apps</text>
    <text x="355" y="315" fill="#94a3b8" font-size="11" text-anchor="middle">Era: 2000s</text>

    <!-- 4G -->
    <rect x="470" y="110" width="190" height="230" fill="url(#boxGrad)" stroke="#10b981" stroke-width="2" rx="8"/>
    <text x="565" y="138" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">4G (LTE-Advanced)</text>
    <text x="565" y="165" fill="#f1f5f9" font-size="12" text-anchor="middle">Speed: Up to 1 Gbps</text>
    <text x="565" y="190" fill="#94a3b8" font-size="12" text-anchor="middle">Latency: &lt; 30 ms</text>
    <text x="565" y="220" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">All-IP Flattened Core</text>
    <text x="565" y="245" fill="#cbd5e1" font-size="11" text-anchor="middle">OFDMA + MIMO</text>
    <text x="565" y="270" fill="#cbd5e1" font-size="11" text-anchor="middle">HD Video Streaming</text>
    <text x="565" y="315" fill="#94a3b8" font-size="11" text-anchor="middle">Era: 2010s</text>

    <!-- 5G -->
    <rect x="680" y="110" width="230" height="230" fill="url(#boxGrad)" stroke="#a855f7" stroke-width="2.5" rx="8"/>
    <text x="795" y="138" fill="#c084fc" font-size="16" font-weight="700" text-anchor="middle">5G (New Radio)</text>
    <text x="795" y="165" fill="#f1f5f9" font-size="12" text-anchor="middle">Speed: Up to 20 Gbps</text>
    <text x="795" y="190" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">Latency: &lt; 1 ms (URLLC)</text>
    <text x="795" y="220" fill="#c084fc" font-size="13" font-weight="700" text-anchor="middle">Cloud-Native SBA</text>
    <text x="795" y="245" fill="#cbd5e1" font-size="11" text-anchor="middle">Massive MIMO, mmWave</text>
    <text x="795" y="270" fill="#38bdf8" font-size="11" text-anchor="middle">Network Slicing, IoT, AI</text>
    <text x="795" y="315" fill="#94a3b8" font-size="11" text-anchor="middle">Era: 2020s+</text>
    """,
    "Paradigms: 5G supports eMBB (High Throughput), URLLC (Ultra-Reliable Low Latency), and mMTC (Massive IoT)"
)

print("Batch rendering completed successfully!")
