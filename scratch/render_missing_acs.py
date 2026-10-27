# -*- coding: utf-8 -*-
"""
Batch vector diagram generator for missing Advanced Control Systems (ACS) questions.
Renders crisp 960x460 technical schematics to PNG using sips.
"""
import os, subprocess, re

os.makedirs("images/acs", exist_ok=True)

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
    <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#38bdf8"/>
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
  
  <rect x="40" y="35" width="130" height="26" fill="{accent_color}22" stroke="{accent_color}" stroke-width="1" rx="5"/>
  <text x="105" y="52" fill="{accent_color}" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">{badge_text}</text>
  <text x="480" y="55" fill="#f1f5f9" font-family="-apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">{title}</text>
  <text x="480" y="80" fill="#94a3b8" font-family="-apple-system, sans-serif" font-size="13" text-anchor="middle">{subtitle}</text>
  {elements_xml}
  {f'''<rect x="40" y="405" width="880" height="24" fill="#0b111e" stroke="#223049" stroke-width="1" rx="4"/>
  <text x="480" y="421" fill="#94a3b8" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">{footer_text}</text>''' if footer_text else ''}
</svg>"""
    render_svg_to_png(svg, png_path)

print("Starting generation of missing ACS diagrams...")

# 1. acs-q8: autonomous_response_flow.png
create_card_diagram(
    "images/acs/autonomous_response_flow.png",
    "Solution of Autonomous State Equations via Laplace Transforms",
    "Derivation of Homogeneous Zero-Input State Trajectory: x(t) = e^(At) · x(0)",
    "#38bdf8", "ACS • MOD 1",
    """
    <rect x="50" y="115" width="230" height="260" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="8"/>
    <text x="165" y="145" fill="#38bdf8" font-size="15" font-weight="700" text-anchor="middle">Step 1: Time Domain</text>
    <text x="165" y="185" fill="#f1f5f9" font-size="14" text-anchor="middle">ẋ(t) = A · x(t)</text>
    <text x="165" y="215" fill="#94a3b8" font-size="12" text-anchor="middle">Initial condition: x(0)</text>
    <text x="165" y="255" fill="#fbbf24" font-size="13" text-anchor="middle">Autonomous System (u=0)</text>
    <text x="165" y="295" fill="#cbd5e1" font-size="12" text-anchor="middle">Unforced Natural Motion</text>

    <path d="M 290 245 L 340 245" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>

    <rect x="350" y="115" width="260" height="260" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="8"/>
    <text x="480" y="145" fill="#fbbf24" font-size="15" font-weight="700" text-anchor="middle">Step 2: Laplace Domain</text>
    <text x="480" y="180" fill="#f1f5f9" font-size="13" text-anchor="middle">sX(s) - x(0) = A · X(s)</text>
    <text x="480" y="215" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">(sI - A) X(s) = x(0)</text>
    <text x="480" y="255" fill="#f1f5f9" font-size="13" text-anchor="middle">X(s) = (sI - A)⁻¹ x(0)</text>
    <text x="480" y="295" fill="#34d399" font-size="13" text-anchor="middle">Resolvent Matrix Φ(s) = (sI - A)⁻¹</text>
    <text x="480" y="330" fill="#94a3b8" font-size="11" text-anchor="middle">Inverse: adj(sI - A) / det(sI - A)</text>

    <path d="M 620 245 L 670 245" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>

    <rect x="680" y="115" width="230" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="8"/>
    <text x="795" y="145" fill="#34d399" font-size="15" font-weight="700" text-anchor="middle">Step 3: State Solution</text>
    <text x="795" y="185" fill="#f1f5f9" font-size="13" text-anchor="middle">x(t) = ℒ⁻¹[(sI - A)⁻¹] · x(0)</text>
    <rect x="695" y="215" width="200" height="60" fill="#0b111e" stroke="#10b981" stroke-width="2" rx="6"/>
    <text x="795" y="242" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">x(t) = e^(At) · x(0)</text>
    <text x="795" y="262" fill="#38bdf8" font-size="13" text-anchor="middle">x(t) = Φ(t) · x(0)</text>
    <text x="795" y="310" fill="#94a3b8" font-size="12" text-anchor="middle">Φ(t) = State Transition Matrix</text>
    <text x="795" y="340" fill="#fbbf24" font-size="11" text-anchor="middle">Governs All Autonomous Modes</text>
    """,
    "Fundamental Resolvent Theorem: Φ(t) = ℒ⁻¹[(sI - A)⁻¹] = e^(At), satisfying dΦ(t)/dt = A·Φ(t) with Φ(0) = I"
)

# 2. acs-q9b: discrete_state_model.png
create_card_diagram(
    "images/acs/discrete_state_model.png",
    "Discrete-Time State Space System Model with Zero-Order Hold",
    "Continuous-to-Discrete Discretization: x(k+1) = G · x(k) + H · u(k), y(k) = C · x(k) + D · u(k)",
    "#38bdf8", "ACS • MOD 2",
    """
    <path d="M 60 220 L 140 220" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>
    <text x="80" y="205" fill="#38bdf8" font-size="14" font-weight="700">u(k)</text>

    <!-- Matrix H -->
    <rect x="150" y="190" width="70" height="60" fill="url(#boxGrad)" stroke="#38bdf8" rx="6"/>
    <text x="185" y="226" fill="#f1f5f9" font-size="16" font-weight="700" text-anchor="middle">H</text>

    <path d="M 220 220 L 305 220" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>

    <!-- Summing node -->
    <circle cx="320" cy="220" r="15" fill="#0b111e" stroke="#38bdf8" stroke-width="2"/>
    <text x="320" y="226" fill="#38bdf8" font-size="18" font-weight="700" text-anchor="middle">Σ</text>

    <path d="M 335 220 L 420 220" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>
    <text x="375" y="205" fill="#fbbf24" font-size="13" font-weight="700">x(k+1)</text>

    <!-- Unit Delay z^-1 -->
    <rect x="430" y="190" width="90" height="60" fill="url(#boxGrad)" stroke="#10b981" stroke-width="2" rx="8"/>
    <text x="475" y="226" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">z⁻¹</text>
    <text x="475" y="244" fill="#94a3b8" font-size="10" text-anchor="middle">Unit Delay</text>

    <path d="M 520 220 L 630 220" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>
    <circle cx="580" cy="220" r="4" fill="#38bdf8"/>
    <text x="585" y="205" fill="#34d399" font-size="14" font-weight="700">x(k)</text>

    <!-- Matrix C -->
    <rect x="640" y="190" width="70" height="60" fill="url(#boxGrad)" stroke="#38bdf8" rx="6"/>
    <text x="675" y="226" fill="#f1f5f9" font-size="16" font-weight="700" text-anchor="middle">C</text>

    <path d="M 710 220 L 785 220" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>

    <!-- Output Summing node -->
    <circle cx="800" cy="220" r="15" fill="#0b111e" stroke="#38bdf8" stroke-width="2"/>
    <text x="800" y="226" fill="#38bdf8" font-size="18" font-weight="700" text-anchor="middle">Σ</text>

    <path d="M 815 220 L 890 220" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>
    <text x="860" y="205" fill="#38bdf8" font-size="14" font-weight="700">y(k)</text>

    <!-- Feedback loop G -->
    <path d="M 580 220 L 580 320 L 515 320" stroke="#f59e0b" stroke-width="2"/>
    <rect x="420" y="295" width="90" height="50" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="6"/>
    <text x="465" y="326" fill="#fbbf24" font-size="16" font-weight="700" text-anchor="middle">G = e^(AT)</text>
    <path d="M 420 320 L 320 320 L 320 240" stroke="#f59e0b" stroke-width="2" marker-end="url(#arrow)"/>

    <!-- Feedforward D -->
    <path d="M 100 220 L 100 130 L 730 130" stroke="#94a3b8" stroke-width="1.5"/>
    <rect x="730" y="110" width="60" height="40" fill="url(#boxGrad)" stroke="#94a3b8" rx="4"/>
    <text x="760" y="135" fill="#cbd5e1" font-size="14" font-weight="700" text-anchor="middle">D</text>
    <path d="M 790 130 L 800 130 L 800 200" stroke="#94a3b8" stroke-width="1.5" marker-end="url(#arrow)"/>
    """,
    "Discretization Matrices: G = e^(AT), H = [∫₀ᵀ e^(Aτ) dτ] B | Pulse Transfer Function: G(z) = C(zI - G)⁻¹ H + D"
)

# 3. acs-q10: cayley_hamilton_method.png
create_card_diagram(
    "images/acs/cayley_hamilton_method.png",
    "Cayley-Hamilton Theorem for Computing State Transition Matrix e^(At)",
    "Every Square Matrix Satisfies Its Own Characteristic Equation: Δ(A) = 0",
    "#38bdf8", "ACS • MOD 2",
    """
    <rect x="50" y="115" width="260" height="260" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="8"/>
    <text x="180" y="145" fill="#38bdf8" font-size="15" font-weight="700" text-anchor="middle">1. Characteristic Polynomial</text>
    <text x="180" y="185" fill="#f1f5f9" font-size="13" text-anchor="middle">|λI - A| = 0</text>
    <text x="180" y="215" fill="#fbbf24" font-size="13" text-anchor="middle">λⁿ + aₙ₋₁λⁿ⁻¹ + ... + a₀ = 0</text>
    <text x="180" y="255" fill="#cbd5e1" font-size="12" text-anchor="middle">Eigenvalues: λ₁, λ₂, ..., λₙ</text>
    <text x="180" y="295" fill="#94a3b8" font-size="12" text-anchor="middle">Matrix Substitution:</text>
    <text x="180" y="325" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">Aⁿ + aₙ₋₁Aⁿ⁻¹ + ... + a₀I = 0</text>

    <path d="M 320 245 L 360 245" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>

    <rect x="370" y="115" width="260" height="260" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="8"/>
    <text x="500" y="145" fill="#fbbf24" font-size="15" font-weight="700" text-anchor="middle">2. Function Interpolation</text>
    <text x="500" y="180" fill="#f1f5f9" font-size="13" text-anchor="middle">f(λ) = e^(λt) = q(λ)Δ(λ) + r(λ)</text>
    <text x="500" y="215" fill="#38bdf8" font-size="13" text-anchor="middle">Remainder r(λ) of order (n-1):</text>
    <text x="500" y="245" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">r(λ) = α₀ + α₁λ + ... + αₙ₋₁λⁿ⁻¹</text>
    <text x="500" y="280" fill="#f1f5f9" font-size="12" text-anchor="middle">Distinct λ: e^(λᵢt) = r(λᵢ)</text>
    <text x="500" y="315" fill="#94a3b8" font-size="11" text-anchor="middle">Repeated λ: dᵐ/dλᵐ [e^(λt)] = dᵐ/dλᵐ [r(λ)]</text>
    <text x="500" y="345" fill="#cbd5e1" font-size="12" text-anchor="middle">Solve n equations for α₀, ..., αₙ₋₁</text>

    <path d="M 640 245 L 680 245" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>

    <rect x="690" y="115" width="220" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="8"/>
    <text x="800" y="145" fill="#34d399" font-size="15" font-weight="700" text-anchor="middle">3. Matrix Polynomial</text>
    <text x="800" y="185" fill="#94a3b8" font-size="12" text-anchor="middle">Substitute Matrix A into r(λ):</text>
    <rect x="700" y="215" width="200" height="70" fill="#0b111e" stroke="#10b981" stroke-width="2" rx="6"/>
    <text x="800" y="245" fill="#34d399" font-size="15" font-weight="700" text-anchor="middle">e^(At) = α₀I + α₁A +</text>
    <text x="800" y="268" fill="#34d399" font-size="15" font-weight="700" text-anchor="middle">... + αₙ₋₁Aⁿ⁻¹</text>
    <text x="800" y="320" fill="#f1f5f9" font-size="12" text-anchor="middle">Exact Analytical STM</text>
    <text x="800" y="345" fill="#38bdf8" font-size="11" text-anchor="middle">No infinite series truncation</text>
    """,
    "Cayley-Hamilton Reduction: Powers of Aⁿ and higher are expressed as linear combinations of {I, A, A², ..., Aⁿ⁻¹}"
)

# 4. acs-q11: convolution_integral.png
create_card_diagram(
    "images/acs/convolution_integral.png",
    "Complete Solution of Non-Homogeneous State Equations",
    "Superposition of Zero-Input Response (ZIR) and Zero-State Response (ZSR) via Convolution",
    "#38bdf8", "ACS • MOD 2",
    """
    <!-- Input u(t) branch -->
    <path d="M 60 170 L 150 170" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>
    <text x="80" y="155" fill="#38bdf8" font-size="15" font-weight="700">u(τ)</text>

    <!-- Branching to ZSR -->
    <rect x="160" y="140" width="100" height="60" fill="url(#boxGrad)" stroke="#38bdf8" rx="6"/>
    <text x="210" y="175" fill="#f1f5f9" font-size="15" font-weight="700" text-anchor="middle">Input B</text>

    <path d="M 260 170 L 330 170" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>

    <!-- Convolution Block -->
    <rect x="340" y="130" width="280" height="80" fill="url(#boxGrad)" stroke="#10b981" stroke-width="2" rx="8"/>
    <text x="480" y="160" fill="#34d399" font-size="15" font-weight="700" text-anchor="middle">Convolution Integral (ZSR)</text>
    <text x="480" y="190" fill="#f1f5f9" font-size="14" text-anchor="middle">∫₀ᵗ Φ(t - τ) · B · u(τ) dτ</text>

    <path d="M 620 170 L 730 170 L 730 225" stroke="#10b981" stroke-width="2.5" marker-end="url(#arrow-green)"/>

    <!-- Initial state x(0) branch (ZIR) -->
    <path d="M 60 300 L 230 300" stroke="#f59e0b" stroke-width="2.5" marker-end="url(#arrow)"/>
    <text x="120" y="285" fill="#fbbf24" font-size="15" font-weight="700">x(0) Initial State</text>

    <rect x="240" y="270" width="260" height="65" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="8"/>
    <text x="370" y="300" fill="#fbbf24" font-size="15" font-weight="700" text-anchor="middle">Zero-Input Response (ZIR)</text>
    <text x="370" y="324" fill="#f1f5f9" font-size="14" text-anchor="middle">x_zir(t) = Φ(t) · x(0) = e^(At) · x(0)</text>

    <path d="M 500 300 L 730 300 L 730 255" stroke="#f59e0b" stroke-width="2.5" marker-end="url(#arrow)"/>

    <!-- Main Summing Junction -->
    <circle cx="730" cy="240" r="18" fill="#0b111e" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="730" y="247" fill="#38bdf8" font-size="22" font-weight="700" text-anchor="middle">Σ</text>

    <path d="M 750 240 L 820 240" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)"/>

    <rect x="830" y="200" width="90" height="80" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="2" rx="8"/>
    <text x="875" y="235" fill="#38bdf8" font-size="16" font-weight="700" text-anchor="middle">x(t)</text>
    <text x="875" y="260" fill="#94a3b8" font-size="11" text-anchor="middle">Total State</text>
    """,
    "Complete State Trajectory: x(t) = Φ(t)·x(0) + ∫₀ᵗ Φ(t - τ)·B·u(τ) dτ | Output: y(t) = C·x(t) + D·u(t)"
)

# 5. acs-q13: gilbert_method.png
create_card_diagram(
    "images/acs/gilbert_method.png",
    "Gilbert's Diagonal Modal Test for Controllability and Observability",
    "Inspection of Input Distribution Rows (B̂) and Output Measurement Columns (Ĉ) in Jordan Canonical Form",
    "#38bdf8", "ACS • MOD 3",
    """
    <rect x="50" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="10"/>
    <text x="255" y="145" fill="#38bdf8" font-size="16" font-weight="700" text-anchor="middle">Controllability Criterion (Input B̂ = P⁻¹B)</text>
    <rect x="80" y="170" width="350" height="40" fill="#0b111e" stroke="#10b981" stroke-width="1.5" rx="6"/>
    <text x="255" y="195" fill="#34d399" font-size="13" font-weight="600" text-anchor="middle">Row i of B̂ ≠ [0 0 ... 0]  ⟹  Mode λᵢ is CONTROLLABLE</text>
    
    <rect x="80" y="225" width="350" height="40" fill="#0b111e" stroke="#ef4444" stroke-width="1.5" rx="6"/>
    <text x="255" y="250" fill="#f87171" font-size="13" font-weight="600" text-anchor="middle">Row j of B̂ = [0 0 ... 0]  ⟹  Mode λⱼ is UNCONTROLLABLE</text>
    
    <text x="255" y="295" fill="#f1f5f9" font-size="12" text-anchor="middle">Physical Meaning: Input u(t) cannot excite state zⱼ(t)</text>
    <text x="255" y="325" fill="#94a3b8" font-size="12" text-anchor="middle">żⱼ = λⱼ zⱼ + 0 · u(t) (Disconnected from actuation)</text>
    <text x="255" y="355" fill="#fbbf24" font-size="11" text-anchor="middle">For Jordan blocks: inspect row corresponding to last state of block</text>

    <rect x="500" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
    <text x="705" y="145" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">Observability Criterion (Output Ĉ = CP)</text>
    <rect x="530" y="170" width="350" height="40" fill="#0b111e" stroke="#10b981" stroke-width="1.5" rx="6"/>
    <text x="705" y="195" fill="#34d399" font-size="13" font-weight="600" text-anchor="middle">Col i of Ĉ ≠ [0; 0; ...; 0]  ⟹  Mode λᵢ is OBSERVABLE</text>
    
    <rect x="530" y="225" width="350" height="40" fill="#0b111e" stroke="#ef4444" stroke-width="1.5" rx="6"/>
    <text x="705" y="250" fill="#f87171" font-size="13" font-weight="600" text-anchor="middle">Col k of Ĉ = [0; 0; ...; 0]  ⟹  Mode λₖ is UNOBSERVABLE</text>
    
    <text x="705" y="295" fill="#f1f5f9" font-size="12" text-anchor="middle">Physical Meaning: State zₖ(t) produces zero output response</text>
    <text x="705" y="325" fill="#94a3b8" font-size="12" text-anchor="middle">y(t) = c₁z₁ + ... + 0·zₖ + ... + cₙzₙ (State hidden from sensor)</text>
    <text x="705" y="355" fill="#fbbf24" font-size="11" text-anchor="middle">For Jordan blocks: inspect col corresponding to first state of block</text>
    """,
    "Gilbert's Theorem applies directly to systems with distinct eigenvalues diagonalized via modal matrix P = [v₁ v₂ ... vₙ]"
)

# 6. acs-q13b: pbh_rank_test.png
create_card_diagram(
    "images/acs/pbh_rank_test.png",
    "Popov-Belevitch-Hautus (PBH) Rank Tests for Controllability and Observability",
    "Algebraic Rank Condition Evaluated at Every Distinct System Eigenvalue λᵢ of Matrix A",
    "#38bdf8", "ACS • MOD 3",
    """
    <rect x="50" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="10"/>
    <text x="255" y="145" fill="#38bdf8" font-size="16" font-weight="700" text-anchor="middle">PBH Controllability Rank Test</text>
    
    <rect x="80" y="170" width="350" height="65" fill="#0b111e" stroke="#38bdf8" stroke-width="2" rx="6"/>
    <text x="255" y="200" fill="#38bdf8" font-size="15" font-weight="700" text-anchor="middle">rank [ sI - A | B ] = n</text>
    <text x="255" y="222" fill="#fbbf24" font-size="12" text-anchor="middle">Evaluated at every eigenvalue s = λᵢ (i = 1, ..., n)</text>

    <text x="255" y="265" fill="#f1f5f9" font-size="13" text-anchor="middle">Eigenvector Formulation:</text>
    <text x="255" y="290" fill="#34d399" font-size="14" font-weight="600" text-anchor="middle">vᴴ · A = λ vᴴ  ⟹  vᴴ · B ≠ 0</text>
    <text x="255" y="325" fill="#94a3b8" font-size="12" text-anchor="middle">No left eigenvector of A lies in the null space of B</text>
    <text x="255" y="355" fill="#cbd5e1" font-size="11" text-anchor="middle">Stabilizability: condition holds for all Re(λᵢ) ≥ 0</text>

    <rect x="500" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
    <text x="705" y="145" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">PBH Observability Rank Test</text>
    
    <rect x="530" y="170" width="350" height="65" fill="#0b111e" stroke="#10b981" stroke-width="2" rx="6"/>
    <text x="705" y="200" fill="#34d399" font-size="15" font-weight="700" text-anchor="middle">rank [ (sI - A)ᵀ | Cᵀ ]ᵀ = n</text>
    <text x="705" y="222" fill="#fbbf24" font-size="12" text-anchor="middle">Matrix size (2n × n) must maintain full column rank n</text>

    <text x="705" y="265" fill="#f1f5f9" font-size="13" text-anchor="middle">Eigenvector Formulation:</text>
    <text x="705" y="290" fill="#34d399" font-size="14" font-weight="600" text-anchor="middle">A · w = λ w  ⟹  C · w ≠ 0</text>
    <text x="705" y="325" fill="#94a3b8" font-size="12" text-anchor="middle">No right eigenvector of A lies in the null space of C</text>
    <text x="705" y="355" fill="#cbd5e1" font-size="11" text-anchor="middle">Detectability: condition holds for all Re(λᵢ) ≥ 0</text>
    """,
    "PBH Criteria Advantages: Does not require computing matrix powers Aⁿ⁻¹ or inverting modal transformation matrices P"
)

# 7. acs-q16: nonlinear_phenomena.png
create_card_diagram(
    "images/acs/nonlinear_phenomena.png",
    "Unique Physical Phenomena in Non-Linear Control Systems",
    "Non-LTI Dynamic Behaviors: Limit Cycles, Jump Resonance, Subharmonic Generation, and Chaos",
    "#38bdf8", "ACS • MOD 4",
    """
    <!-- 1. Limit Cycles -->
    <rect x="50" y="110" width="200" height="260" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="8"/>
    <text x="150" y="135" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">1. Limit Cycles</text>
    <!-- Circle trajectory -->
    <ellipse cx="150" cy="205" rx="55" ry="40" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
    <path d="M 120 180 Q 140 195 150 205" fill="none" stroke="#34d399" stroke-width="1.5" marker-end="url(#arrow-green)"/>
    <path d="M 195 240 Q 170 215 150 205" fill="none" stroke="#f59e0b" stroke-width="1.5" marker-end="url(#arrow)"/>
    <text x="150" y="280" fill="#f1f5f9" font-size="11" text-anchor="middle">Self-Sustained Oscillation</text>
    <text x="150" y="305" fill="#94a3b8" font-size="10" text-anchor="middle">Isolated closed trajectory</text>
    <text x="150" y="330" fill="#cbd5e1" font-size="10" text-anchor="middle">Fixed amplitude &amp; frequency</text>
    <text x="150" y="355" fill="#fbbf24" font-size="10" text-anchor="middle">Independent of initial state</text>

    <!-- 2. Jump Resonance -->
    <rect x="270" y="110" width="200" height="260" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="8"/>
    <text x="370" y="135" fill="#fbbf24" font-size="14" font-weight="700" text-anchor="middle">2. Jump Resonance</text>
    <!-- Hysteresis frequency curve -->
    <path d="M 290 230 C 320 220, 340 160, 360 160 C 375 160, 380 200, 370 210 C 360 220, 390 240, 450 245" fill="none" stroke="#fbbf24" stroke-width="2.5"/>
    <path d="M 370 170 L 370 235" stroke="#ef4444" stroke-width="2" stroke-dasharray="3,3" marker-end="url(#arrow)"/>
    <text x="370" y="280" fill="#f1f5f9" font-size="11" text-anchor="middle">Discontinuous Jump</text>
    <text x="370" y="305" fill="#94a3b8" font-size="10" text-anchor="middle">Multi-valued amplitude response</text>
    <text x="370" y="330" fill="#cbd5e1" font-size="10" text-anchor="middle">Bending resonance curve</text>
    <text x="370" y="355" fill="#fbbf24" font-size="10" text-anchor="middle">Hysteresis loop under sweep</text>

    <!-- 3. Subharmonics -->
    <rect x="490" y="110" width="200" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="8"/>
    <text x="590" y="135" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">3. Subharmonics</text>
    <!-- Waveform with multiple periods -->
    <path d="M 510 210 Q 525 170 540 210 Q 555 250 570 210 Q 585 170 600 210 Q 615 250 630 210 Q 645 170 660 210 Q 675 250 680 210" fill="none" stroke="#34d399" stroke-width="2"/>
    <text x="590" y="280" fill="#f1f5f9" font-size="11" text-anchor="middle">Fractional Frequencies</text>
    <text x="590" y="305" fill="#94a3b8" font-size="10" text-anchor="middle">Response at ω/2, ω/3, ω/n</text>
    <text x="590" y="330" fill="#cbd5e1" font-size="10" text-anchor="middle">Harmonic energy transfer</text>
    <text x="590" y="355" fill="#fbbf24" font-size="10" text-anchor="middle">Absent in linear LTI systems</text>

    <!-- 4. Chaos -->
    <rect x="710" y="110" width="200" height="260" fill="url(#boxGrad)" stroke="#a855f7" stroke-width="1.5" rx="8"/>
    <text x="810" y="135" fill="#c084fc" font-size="14" font-weight="700" text-anchor="middle">4. Deterministic Chaos</text>
    <!-- Chaotic attractor loops -->
    <path d="M 740 210 Q 770 160 800 210 Q 830 260 860 210 Q 890 160 810 240 Q 750 200 830 180" fill="none" stroke="#c084fc" stroke-width="1.8"/>
    <text x="810" y="280" fill="#f1f5f9" font-size="11" text-anchor="middle">Strange Attractors</text>
    <text x="810" y="305" fill="#94a3b8" font-size="10" text-anchor="middle">Aperiodic bounded trajectories</text>
    <text x="810" y="330" fill="#cbd5e1" font-size="10" text-anchor="middle">Extreme sensitivity to ICs</text>
    <text x="810" y="355" fill="#fbbf24" font-size="10" text-anchor="middle">Broadband continuous spectrum</text>
    """,
    "Fundamental Non-Linearity Property: Principle of Superposition Does NOT Apply | System response depends on input amplitude"
)

# 8. acs-q16b: relay_describing_function.png
create_card_diagram(
    "images/acs/relay_describing_function.png",
    "Describing Function of Ideal Relay vs Relay with Dead-Zone",
    "Quasi-Linearization: Fundamental Harmonic Gain N(X) = Y₁ / X as Input Amplitude X Varies",
    "#38bdf8", "ACS • MOD 4",
    """
    <!-- Ideal Relay -->
    <rect x="50" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="10"/>
    <text x="255" y="145" fill="#38bdf8" font-size="16" font-weight="700" text-anchor="middle">1. Ideal On-Off Relay</text>
    <!-- Ideal Relay V-I curve -->
    <path d="M 120 220 L 390 220" stroke="#94a3b8" stroke-width="1"/>
    <path d="M 255 160 L 255 280" stroke="#94a3b8" stroke-width="1"/>
    <path d="M 140 260 L 255 260 L 255 180 L 370 180" stroke="#38bdf8" stroke-width="3" fill="none"/>
    <text x="380" y="175" fill="#38bdf8" font-size="12" font-weight="700">+M</text>
    <text x="130" y="275" fill="#38bdf8" font-size="12" font-weight="700">-M</text>
    <rect x="80" y="295" width="350" height="60" fill="#0b111e" stroke="#38bdf8" stroke-width="1.5" rx="6"/>
    <text x="255" y="320" fill="#38bdf8" font-size="15" font-weight="700" text-anchor="middle">N(X) = 4M / (πX) ∠0°</text>
    <text x="255" y="342" fill="#cbd5e1" font-size="12" text-anchor="middle">Purely real gain, inversely proportional to input amplitude X</text>

    <!-- Relay with Dead-Zone -->
    <rect x="500" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="10"/>
    <text x="705" y="145" fill="#fbbf24" font-size="16" font-weight="700" text-anchor="middle">2. Relay with Dead-Zone (±Δ)</text>
    <!-- Deadzone curve -->
    <path d="M 570 220 L 840 220" stroke="#94a3b8" stroke-width="1"/>
    <path d="M 705 160 L 705 280" stroke="#94a3b8" stroke-width="1"/>
    <path d="M 590 260 L 665 260 L 665 220 L 745 220 L 745 180 L 820 180" stroke="#fbbf24" stroke-width="3" fill="none"/>
    <text x="655" y="210" fill="#fbbf24" font-size="11">-Δ</text>
    <text x="755" y="235" fill="#fbbf24" font-size="11">+Δ</text>
    <text x="830" y="175" fill="#fbbf24" font-size="12" font-weight="700">+M</text>
    <rect x="530" y="295" width="350" height="60" fill="#0b111e" stroke="#f59e0b" stroke-width="1.5" rx="6"/>
    <text x="705" y="320" fill="#fbbf24" font-size="14" font-weight="700" text-anchor="middle">N(X) = (4M / πX) · √(1 - (Δ/X)²)</text>
    <text x="705" y="342" fill="#cbd5e1" font-size="12" text-anchor="middle">N(X) = 0 for X &lt; Δ; Maximum at X = √2 · Δ</text>
    """,
    "Harmonic Balance Condition: Limit cycle exists where G(jω) = -1 / N(X) in the complex frequency plane"
)

# 9. acs-q17b: dead_zone_describing_function.png
create_card_diagram(
    "images/acs/dead_zone_describing_function.png",
    "Derivation of the Describing Function for Dead-Zone Non-Linearity",
    "Piecewise Characteristic Curve, Conduction Angle α = sin⁻¹(δ/X), and Fourier Integral Evaluation",
    "#38bdf8", "ACS • MOD 4",
    """
    <rect x="50" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="10"/>
    <text x="255" y="145" fill="#38bdf8" font-size="16" font-weight="700" text-anchor="middle">1. Characteristic Curve y = f(x)</text>
    <!-- Axes -->
    <path d="M 90 230 L 420 230" stroke="#94a3b8" stroke-width="1"/>
    <path d="M 255 160 L 255 300" stroke="#94a3b8" stroke-width="1"/>
    <!-- Deadzone line -->
    <path d="M 120 290 L 195 230 L 315 230 L 390 170" stroke="#38bdf8" stroke-width="3" fill="none"/>
    <text x="180" y="220" fill="#fbbf24" font-size="12">-δ</text>
    <text x="325" y="245" fill="#fbbf24" font-size="12">+δ</text>
    <text x="395" y="165" fill="#34d399" font-size="13" font-weight="700">Slope k</text>
    <text x="255" y="330" fill="#cbd5e1" font-size="12" text-anchor="middle">y = 0 for |x| ≤ δ; y = k(x - δ) for x &gt; δ</text>
    <text x="255" y="355" fill="#94a3b8" font-size="11" text-anchor="middle">Conduction threshold: α = sin⁻¹(δ / X)</text>

    <rect x="500" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
    <text x="705" y="145" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">2. Fourier Fundamental Coefficient B₁</text>
    <text x="705" y="180" fill="#f1f5f9" font-size="13" text-anchor="middle">B₁ = (4/π) ∫_α^(π/2) k (X sin θ - δ) sin θ dθ</text>
    <text x="705" y="215" fill="#94a3b8" font-size="12" text-anchor="middle">Integrating and substituting δ/X = sin α:</text>
    
    <rect x="520" y="240" width="370" height="65" fill="#0b111e" stroke="#10b981" stroke-width="2" rx="6"/>
    <text x="705" y="265" fill="#34d399" font-size="15" font-weight="700" text-anchor="middle">N(X) = k [ 1 - (2/π) f(δ/X) ]</text>
    <text x="705" y="290" fill="#fbbf24" font-size="12" text-anchor="middle">where f(u) = sin⁻¹(u) + u · √(1 - u²)</text>

    <text x="705" y="335" fill="#cbd5e1" font-size="12" text-anchor="middle">For X ≫ δ: N(X) → k (approaches linear gain)</text>
    <text x="705" y="358" fill="#94a3b8" font-size="11" text-anchor="middle">For X ≤ δ: N(X) = 0 (signal trapped in dead-band)</text>
    """,
    "Dead-zone non-linearity causes low-amplitude signal attenuation and tracking errors in servomechanisms"
)

# 10. acs-q19: singular_points_types.png
create_card_diagram(
    "images/acs/singular_points_types.png",
    "Phase Plane Classification of Singular Equilibrium Points",
    "Eigenvalues of Jacobian Matrix J = [∂f₁/∂x₁, ∂f₁/∂x₂; ∂f₂/∂x₁, ∂f₂/∂x₂] Evaluated at (x₁*, x₂*)",
    "#38bdf8", "ACS • MOD 4",
    """
    <!-- 1. Stable Node -->
    <rect x="50" y="110" width="200" height="260" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="8"/>
    <text x="150" y="135" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">Stable Node</text>
    <path d="M 150 150 L 150 250" stroke="#94a3b8" stroke-width="0.8"/>
    <path d="M 100 200 L 200 200" stroke="#94a3b8" stroke-width="0.8"/>
    <!-- Inward trajectories -->
    <path d="M 110 160 Q 135 190 150 200" stroke="#38bdf8" stroke-width="1.8" fill="none" marker-end="url(#arrow)"/>
    <path d="M 190 160 Q 165 190 150 200" stroke="#38bdf8" stroke-width="1.8" fill="none" marker-end="url(#arrow)"/>
    <path d="M 110 240 Q 135 210 150 200" stroke="#38bdf8" stroke-width="1.8" fill="none" marker-end="url(#arrow)"/>
    <path d="M 190 240 Q 165 210 150 200" stroke="#38bdf8" stroke-width="1.8" fill="none" marker-end="url(#arrow)"/>
    <circle cx="150" cy="200" r="4" fill="#38bdf8"/>
    <text x="150" y="280" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">Real, Negative λ</text>
    <text x="150" y="305" fill="#f1f5f9" font-size="11" text-anchor="middle">λ₂ &lt; λ₁ &lt; 0</text>
    <text x="150" y="330" fill="#94a3b8" font-size="10" text-anchor="middle">Asymptotically stable</text>
    <text x="150" y="355" fill="#cbd5e1" font-size="10" text-anchor="middle">No oscillations</text>

    <!-- 2. Saddle Point -->
    <rect x="270" y="110" width="200" height="260" fill="url(#boxGrad)" stroke="#ef4444" stroke-width="1.5" rx="8"/>
    <text x="370" y="135" fill="#f87171" font-size="14" font-weight="700" text-anchor="middle">Saddle Point</text>
    <path d="M 370 150 L 370 250" stroke="#94a3b8" stroke-width="0.8"/>
    <path d="M 320 200 L 420 200" stroke="#94a3b8" stroke-width="0.8"/>
    <!-- Hyperbolic trajectories -->
    <path d="M 330 160 Q 360 190 330 240" stroke="#f87171" stroke-width="1.8" fill="none"/>
    <path d="M 410 160 Q 380 190 410 240" stroke="#f87171" stroke-width="1.8" fill="none"/>
    <path d="M 370 160 L 370 195" stroke="#34d399" stroke-width="2" marker-end="url(#arrow-green)"/>
    <path d="M 370 240 L 370 205" stroke="#34d399" stroke-width="2" marker-end="url(#arrow-green)"/>
    <circle cx="370" cy="200" r="4" fill="#f87171"/>
    <text x="370" y="280" fill="#f87171" font-size="12" font-weight="700" text-anchor="middle">Real, Opposite Signs</text>
    <text x="370" y="305" fill="#f1f5f9" font-size="11" text-anchor="middle">λ₁ &lt; 0 &lt; λ₂</text>
    <text x="370" y="330" fill="#94a3b8" font-size="10" text-anchor="middle">Always Unstable</text>
    <text x="370" y="355" fill="#cbd5e1" font-size="10" text-anchor="middle">Separatrix divide basins</text>

    <!-- 3. Stable Focus -->
    <rect x="490" y="110" width="200" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="8"/>
    <text x="590" y="135" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">Stable Focus</text>
    <path d="M 590 150 L 590 250" stroke="#94a3b8" stroke-width="0.8"/>
    <path d="M 540 200 L 640 200" stroke="#94a3b8" stroke-width="0.8"/>
    <!-- Inward spiral -->
    <path d="M 550 170 Q 630 160 625 210 Q 620 240 580 230 Q 565 215 580 195 Q 595 190 590 200" stroke="#34d399" stroke-width="1.8" fill="none"/>
    <circle cx="590" cy="200" r="4" fill="#34d399"/>
    <text x="590" y="280" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">Complex Conjugate</text>
    <text x="590" y="305" fill="#f1f5f9" font-size="11" text-anchor="middle">λ = -σ ± jω  (σ &gt; 0)</text>
    <text x="590" y="330" fill="#94a3b8" font-size="10" text-anchor="middle">Damped oscillatory</text>
    <text x="590" y="355" fill="#cbd5e1" font-size="10" text-anchor="middle">Asymptotically stable</text>

    <!-- 4. Center / Vortex -->
    <rect x="710" y="110" width="200" height="260" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="8"/>
    <text x="810" y="135" fill="#fbbf24" font-size="14" font-weight="700" text-anchor="middle">Center (Vortex)</text>
    <path d="M 810 150 L 810 250" stroke="#94a3b8" stroke-width="0.8"/>
    <path d="M 760 200 L 860 200" stroke="#94a3b8" stroke-width="0.8"/>
    <!-- Concentric ellipses -->
    <ellipse cx="810" cy="200" rx="35" ry="25" stroke="#fbbf24" stroke-width="1.8" fill="none"/>
    <ellipse cx="810" cy="200" rx="18" ry="12" stroke="#fbbf24" stroke-width="1.5" fill="none"/>
    <circle cx="810" cy="200" r="4" fill="#fbbf24"/>
    <text x="810" y="280" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle">Purely Imaginary</text>
    <text x="810" y="305" fill="#f1f5f9" font-size="11" text-anchor="middle">λ = ± jω  (σ = 0)</text>
    <text x="810" y="330" fill="#94a3b8" font-size="10" text-anchor="middle">Marginally stable</text>
    <text x="810" y="355" fill="#cbd5e1" font-size="10" text-anchor="middle">Sustained periodic orbits</text>
    """,
    "Singular points represent equilibrium states where dx₁/dt = 0 and dx₂/dt = 0 simultaneously"
)

# 11. acs-q20: sylvester_definiteness.png
create_card_diagram(
    "images/acs/sylvester_definiteness.png",
    "Sylvester's Criterion for Sign Definiteness of Quadratic Forms",
    "Evaluation of Principal Leading Minors Δ₁ = p₁₁, Δ₂ = det[P₂], ..., Δₙ = det[Pₙ] of Symmetric Matrix P",
    "#38bdf8", "ACS • MOD 5",
    """
    <rect x="50" y="115" width="270" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
    <text x="185" y="145" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">1. Positive Definite</text>
    <text x="185" y="175" fill="#f1f5f9" font-size="13" text-anchor="middle">V(x) = xᵀ P x &gt; 0, ∀ x ≠ 0</text>
    <rect x="70" y="195" width="230" height="60" fill="#0b111e" stroke="#10b981" stroke-width="2" rx="6"/>
    <text x="185" y="222" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">All Minors Positive:</text>
    <text x="185" y="244" fill="#f1f5f9" font-size="13" text-anchor="middle">Δ₁ &gt; 0,  Δ₂ &gt; 0,  ...,  Δₙ &gt; 0</text>
    <text x="185" y="295" fill="#cbd5e1" font-size="12" text-anchor="middle">All Eigenvalues λᵢ(P) &gt; 0</text>
    <text x="185" y="325" fill="#94a3b8" font-size="12" text-anchor="middle">Cup-shaped bowl surface</text>
    <text x="185" y="350" fill="#34d399" font-size="11" text-anchor="middle">Valid Lyapunov Candidate V(x)</text>

    <rect x="345" y="115" width="270" height="260" fill="url(#boxGrad)" stroke="#ef4444" stroke-width="1.5" rx="10"/>
    <text x="480" y="145" fill="#f87171" font-size="16" font-weight="700" text-anchor="middle">2. Negative Definite</text>
    <text x="480" y="175" fill="#f1f5f9" font-size="13" text-anchor="middle">V̇(x) = xᵀ Q x &lt; 0, ∀ x ≠ 0</text>
    <rect x="365" y="195" width="230" height="60" fill="#0b111e" stroke="#ef4444" stroke-width="2" rx="6"/>
    <text x="480" y="222" fill="#f87171" font-size="14" font-weight="700" text-anchor="middle">Alternating Minor Signs:</text>
    <text x="480" y="244" fill="#f1f5f9" font-size="13" text-anchor="middle">Δ₁ &lt; 0,  Δ₂ &gt; 0,  Δ₃ &lt; 0, ...</text>
    <text x="480" y="295" fill="#cbd5e1" font-size="12" text-anchor="middle">All Eigenvalues λᵢ(P) &lt; 0</text>
    <text x="480" y="325" fill="#94a3b8" font-size="12" text-anchor="middle">Inverted bowl (peak at origin)</text>
    <text x="480" y="350" fill="#f87171" font-size="11" text-anchor="middle">Required for V̇(x) in Stability</text>

    <rect x="640" y="115" width="270" height="260" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="10"/>
    <text x="775" y="145" fill="#fbbf24" font-size="16" font-weight="700" text-anchor="middle">3. Indefinite</text>
    <text x="775" y="175" fill="#f1f5f9" font-size="13" text-anchor="middle">V(x) takes both + and - values</text>
    <rect x="660" y="195" width="230" height="60" fill="#0b111e" stroke="#f59e0b" stroke-width="2" rx="6"/>
    <text x="775" y="222" fill="#fbbf24" font-size="14" font-weight="700" text-anchor="middle">Mixed Signs or Violations:</text>
    <text x="775" y="244" fill="#f1f5f9" font-size="13" text-anchor="middle">Neither Definite nor Semi</text>
    <text x="775" y="295" fill="#cbd5e1" font-size="12" text-anchor="middle">Both positive and negative λᵢ</text>
    <text x="775" y="325" fill="#94a3b8" font-size="12" text-anchor="middle">Saddle-shaped surface</text>
    <text x="775" y="350" fill="#fbbf24" font-size="11" text-anchor="middle">Indicates Instability</text>
    """,
    "Lyapunov Stability Criterion: System is Asymptotically Stable if V(x) is Positive Definite and V̇(x) is Negative Definite"
)

# 12. acs-q20b: krasovskii_variable_gradient.png
create_card_diagram(
    "images/acs/krasovskii_variable_gradient.png",
    "Generation of Lyapunov Functions: Krasovskii vs Variable Gradient Method",
    "Systematic Techniques for Constructing Scalar Energy Functions V(x) for Non-Linear Systems ẋ = f(x)",
    "#38bdf8", "ACS • MOD 5",
    """
    <rect x="50" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="10"/>
    <text x="255" y="145" fill="#38bdf8" font-size="16" font-weight="700" text-anchor="middle">1. Krasovskii's Method</text>
    <text x="255" y="175" fill="#f1f5f9" font-size="13" text-anchor="middle">Candidate: V(x) = fᵀ(x) · P · f(x)  (P = Pᵀ &gt; 0)</text>
    
    <rect x="80" y="195" width="350" height="55" fill="#0b111e" stroke="#38bdf8" stroke-width="1.5" rx="6"/>
    <text x="255" y="220" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">Jacobian Matrix J(x) = ∂f / ∂x</text>
    <text x="255" y="240" fill="#fbbf24" font-size="12" text-anchor="middle">F(x) = Jᵀ(x) · P + P · J(x)</text>

    <text x="255" y="280" fill="#cbd5e1" font-size="12" text-anchor="middle">Derivative: V̇(x) = fᵀ(x) [ Jᵀ P + P J ] f(x)</text>
    <text x="255" y="310" fill="#34d399" font-size="13" font-weight="600" text-anchor="middle">If F(x) &lt; 0 (Negative Definite) ⟹ STABLE</text>
    <text x="255" y="345" fill="#94a3b8" font-size="11" text-anchor="middle">Highly effective for non-linear systems with f(0) = 0</text>

    <rect x="500" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
    <text x="705" y="145" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">2. Variable Gradient Method</text>
    <text x="705" y="175" fill="#f1f5f9" font-size="13" text-anchor="middle">Assume Gradient Vector: ∇V = [g₁(x), ..., gₙ(x)]ᵀ</text>
    
    <rect x="530" y="195" width="350" height="55" fill="#0b111e" stroke="#10b981" stroke-width="1.5" rx="6"/>
    <text x="705" y="220" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">Curl Invariance: ∂gᵢ / ∂xⱼ = ∂gⱼ / ∂xᵢ</text>
    <text x="705" y="240" fill="#fbbf24" font-size="12" text-anchor="middle">Path Independence for Exact Potential</text>

    <text x="705" y="280" fill="#cbd5e1" font-size="12" text-anchor="middle">Time Derivative: V̇(x) = ∇Vᵀ · f(x) = ∑ gᵢ(x) · fᵢ(x)</text>
    <text x="705" y="310" fill="#34d399" font-size="13" font-weight="600" text-anchor="middle">Line Integral: V(x) = ∫₀ˣ ∇V · dx</text>
    <text x="705" y="345" fill="#94a3b8" font-size="11" text-anchor="middle">Allows flexible parameter tuning to enforce V̇(x) ≤ 0</text>
    """,
    "Variable Gradient method provides wider freedom by formulating coefficients as linear or non-linear functions of states"
)

print("Finished generating ACS diagrams.")
