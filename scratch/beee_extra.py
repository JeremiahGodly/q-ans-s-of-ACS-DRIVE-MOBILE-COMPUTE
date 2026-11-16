# -*- coding: utf-8 -*-
"""
Extra data structures for Basics of Electrical & Electronics Engineering (EST130 / BEEE)
BEEE_BYHEART and BEEE_EXAM_QUESTIONS
KTU 2019 Scheme Electrical & Electronics Engineering
"""

BEEE_BYHEART = {
    'beee-q1': {
        "eq": r"""$$\sum I_{\text{in}} = \sum I_{\text{out}}, \quad \sum_{k=1}^m V_k = 0$$""",
        "text": r"""<strong>Kirchhoff’s Current Law (KCL):</strong> Conservation of electric charge; algebraic sum of currents entering and leaving any node is zero ($\sum I = 0$).<br><strong>Kirchhoff’s Voltage Law (KVL):</strong> Conservation of energy; algebraic sum of potential rises and drops around any closed loop is zero ($\sum V = 0$)."""
    },
    'beee-q2': {
        "eq": r"""$$V_1 - V_2 = V_s, \quad \sum I_{\text{supernode}} = 0$$""",
        "text": r"""<strong>Supernode:</strong> Formed when an ideal voltage source is connected between two non-reference nodes. Replace the source branch with an enclosed boundary and apply KCL to the combined supernode, augmented by the source constraint equation ($V_1 - V_2 = V_s$)."""
    },
    'beee-q3': {
        "eq": r"""$$I_L = I_L' + I_L'' + I_L''' + \dots = \sum_{k=1}^n I_L^{(k)}$$""",
        "text": r"""<strong>Superposition Theorem:</strong> In any linear bilateral network with multiple independent sources, the response in any branch is the algebraic sum of responses caused by each independent source acting alone, with all other voltage sources shorted ($V=0$) and current sources opened ($I=0$). Does not apply directly to power."""
    },
    'beee-q4': {
        "eq": r"""$$V_{th} = V_{oc}, \quad R_{th} = R_N, \quad I_N = \frac{V_{th}}{R_{th}}, \quad I_L = \frac{V_{th}}{R_{th} + R_L} = I_N \left(\frac{R_N}{R_N + R_L}\right)$$""",
        "text": r"""<strong>Thevenin’s Theorem:</strong> Replaces network across load terminals with open-circuit voltage $V_{th}$ in series with $R_{th}$.<br><strong>Norton’s Theorem:</strong> Replaces network with short-circuit current $I_N$ in parallel with $R_N = R_{th}$. Dual relationship: $V_{th} = I_N R_{th}$."""
    },
    'beee-q5': {
        "eq": r"""$$R_L = R_{th} \implies P_{\max} = \frac{V_{th}^2}{4 R_{th}}, \quad \eta = \frac{P_L}{P_{total}} \times 100\% = 50\%$$""",
        "text": r"""<strong>Maximum Power Transfer Theorem:</strong> Maximum power is delivered to a load when $R_L = R_{th}$, resulting in $P_{\max} = \frac{V_{th}^2}{4 R_{th}}$. The transmission efficiency at maximum power transfer is strictly $50\%$, with the remaining $50\%$ dissipated as heat in internal resistance."""
    },
    'beee-q6': {
        "eq": r"""$$v(t) = V_m \sin(\omega t \pm \phi), \quad \omega = 2\pi f = \frac{2\pi}{T}, \quad \mathbf{V} = V_{rms}\angle \phi$$""",
        "text": r"""<strong>Sinusoidal AC Generation:</strong> Derived from Faraday’s law $e(t) = -N \frac{d\Phi}{dt} = N B A \omega \sin(\omega t)$ for a coil rotating in a uniform magnetic field.<br><strong>Phasor:</strong> Directed vector rotating counterclockwise at angular velocity $\omega$, representing RMS magnitude and phase angle in the complex plane."""
    },
    'beee-q7': {
        "eq": r"""$$V_{rms} = \frac{V_m}{\sqrt{2}} \approx 0.707 V_m, \quad V_{avg} = \frac{2 V_m}{\pi} \approx 0.637 V_m, \quad K_f = \frac{V_{rms}}{V_{avg}} = 1.11, \quad K_p = \frac{V_m}{V_{rms}} = \sqrt{2} \approx 1.414$$""",
        "text": r"""<strong>RMS Value:</strong> Equivalent DC heating value ($V_m / \sqrt{2}$).<br><strong>Average Value:</strong> Half-cycle arithmetic mean ($2 V_m / \pi$).<br><strong>Form Factor:</strong> $K_f = 1.11$ for pure sine wave.<br><strong>Peak Factor:</strong> $K_p = 1.414$, governing dielectric insulation withstand limits."""
    },
    'beee-q8': {
        "eq": r"""$$\mathbf{Z} = R + j(X_L - X_C), \quad P = V I \cos\phi, \quad Q = V I \sin\phi, \quad S = V I = \sqrt{P^2 + Q^2}, \quad pf = \cos\phi = \frac{R}{|\mathbf{Z}|}$$""",
        "text": r"""<strong>Series R-L:</strong> Current lags voltage by $\phi = \tan^{-1}(X_L/R)$, lagging power factor.<br><strong>Series R-C:</strong> Current leads voltage by $\phi = \tan^{-1}(X_C/R)$, leading power factor.<br><strong>Power Triangle:</strong> Real active power $P$ (Watts), reactive power $Q$ (VAR), apparent power $S$ (VA)."""
    },
    'beee-q9': {
        "eq": r"""$$f_r = \frac{1}{2\pi\sqrt{LC}}, \quad |\mathbf{Z}_r| = R, \quad I_0 = \frac{V}{R}, \quad Q = \frac{1}{R}\sqrt{\frac{L}{C}}, \quad BW = f_2 - f_1 = \frac{f_r}{Q} = \frac{R}{2\pi L}$$""",
        "text": r"""<strong>Series Resonance:</strong> Occurs when $X_L = X_C$, giving purely resistive minimum impedance $|\mathbf{Z}| = R$, maximum in-phase current ($pf = 1.0$), and voltage magnification across $L$ and $C$ ($V_L = V_C = Q \cdot V$). Narrow bandwidth indicates high selectivity."""
    },
    'beee-q10': {
        "eq": r"""$$\mathcal{F} = N I, \quad \Phi = \frac{\mathcal{F}}{S}, \quad S = \frac{l}{\mu_0 \mu_r A}, \quad B = \mu H = \mu_0 \mu_r H, \quad W_h = \eta B_{\max}^{1.6} f$$""",
        "text": r"""<strong>Magnetic Circuits:</strong> MMF ($\mathcal{F} = NI$ in AT) drives flux ($\Phi = \mathcal{F}/S$ in Wb) against reluctance ($S = \frac{l}{\mu A}$). Electric-magnetic analogy: EMF $\leftrightarrow$ MMF, Current $\leftrightarrow$ Flux, Resistance $\leftrightarrow$ Reluctance. Hysteresis loop area represents Steinmetz core energy loss."""
    },
    'beee-q11': {
        "eq": r"""$$E_1 = 4.44 f N_1 \Phi_m, \quad K = \frac{E_2}{E_1} = \frac{N_2}{N_1}, \quad \eta = \frac{x S \cos\phi_2}{x S \cos\phi_2 + W_i + x^2 W_{cu(FL)}}, \quad W_{cu} = W_i \ (\eta_{\max})$$""",
        "text": r"""<strong>Transformer EMF Equation:</strong> Derived from mutual induction $e = -N \frac{d\Phi}{dt}$, yielding RMS $E = 4.44 f N \Phi_m$.<br><strong>Condition for Maximum Efficiency:</strong> Variable copper loss equals constant iron loss ($W_{cu} = W_i$), occurring at fraction $x_m = \sqrt{W_i / W_{cu(FL)}}$."""
    },
    'beee-q12': {
        "eq": r"""$$E_g = \frac{\Phi Z N P}{60 A}, \quad A = P \ (\text{Lap Winding}), \quad A = 2 \ (\text{Wave Winding})$$""",
        "text": r"""<strong>DC Generator EMF Equation:</strong> Generated voltage $E_g = \frac{\Phi Z N P}{60 A}$. Conductor cuts total flux $P\Phi$ in $60/N$ seconds; $Z/A$ conductors in series per path. Commutator acts as a mechanical rectifier converting internal AC EMF into external DC."""
    },
    'beee-q13': {
        "eq": r"""$$V = E_b + I_a R_a, \quad E_b = \frac{\Phi Z N P}{60 A}, \quad T_a = 0.159 \left(\frac{P Z}{A}\right)\Phi I_a \propto \Phi I_a, \quad N \propto \frac{E_b}{\Phi}$$""",
        "text": r"""<strong>DC Motor Operation:</strong> Conductor force $F = B I l$ (Fleming’s Left-Hand Rule).<br><strong>Back-EMF ($E_b$):</strong> Acts as an automatic governor regulating armature current $I_a = (V - E_b)/R_a$. Massive starting current requires starters. Armature torque $T_a \propto \Phi I_a$; speed $N \propto E_b / \Phi$."""
    },
    'beee-q14': {
        "eq": r"""$$\text{Star: } V_L = \sqrt{3} V_{ph}, \; I_L = I_{ph}; \quad \text{Delta: } V_L = V_{ph}, \; I_L = \sqrt{3} I_{ph}; \quad P = \sqrt{3} V_L I_L \cos\phi$$""",
        "text": r"""<strong>Balanced 3-Phase Systems:</strong> Star provides neutral point with $V_L = \sqrt{3} V_{ph}$; Delta provides closed mesh with $I_L = \sqrt{3} I_{ph}$. Total active power in both configurations is universally $P = \sqrt{3} V_L I_L \cos\phi\text{ W}$, and reactive power is $Q = \sqrt{3} V_L I_L \sin\phi\text{ VAR}$."""
    },
    'beee-q15': {
        "eq": r"""$$I_{\text{residual}} = |I_L - I_N| > 30\text{ mA} \implies \text{Trip}, \quad R_{\text{earth}} < 5\,\Omega \ (\text{Domestic})$$""",
        "text": r"""<strong>Wiring & Protection:</strong> Staircase wiring controls one lamp via two SPDT switches. Earthing (pipe/plate) diverts dangerous fault currents, keeping touch potential safe. MCB provides thermal overload and magnetic short-circuit protection; ELCB/RCCB senses core-balance current imbalance $> 30\text{ mA}$ to prevent electrocution."""
    },
    'beee-q16': {
        "eq": r"""$$I = I_0 \left(e^{\frac{V}{\eta V_T}} - 1\right), \quad V_T = \frac{k T}{q} \approx 26\text{ mV}, \quad r_d = \frac{\eta V_T}{I_F} \approx \frac{26\text{ mV}}{I_F\text{ (mA)}}$$""",
        "text": r"""<strong>PN Junction Diode:</strong> Depletion region uncovers immobile ions creating barrier potential ($0.7\text{ V}$ for Si). Forward bias narrows depletion width, triggering exponential diffusion current (Shockley equation). Dynamic resistance $r_d \approx 26 / I_F\text{ mA}$."""
    },
    'beee-q17': {
        "eq": r"""$$\text{HWR: } V_{dc} = \frac{V_m}{\pi}, \eta = 40.6\%, \gamma = 1.21; \quad \text{FWR: } V_{dc} = \frac{2 V_m}{\pi}, \eta = 81.2\%, \gamma = 0.482, \gamma_{cap} \approx \frac{1}{4\sqrt{3} f C R_L}$$""",
        "text": r"""<strong>Rectifiers:</strong> Full-wave bridge rectifier utilizes four diodes in bridge configuration, doubling DC voltage ($2 V_m / \pi$) and efficiency ($81.2\%$) compared to half-wave ($40.6\%$), with lower ripple factor ($\gamma = 0.482$). Shunt capacitor filter smooths ripple via $R_L C$ discharge."""
    },
    'beee-q18': {
        "eq": r"""$$V_L = V_Z, \quad I_s = I_Z + I_L = \frac{V_{in} - V_Z}{R_s}, \quad R_{s\max} = \frac{V_{in(\min)} - V_Z}{I_{L(\max)} + I_{Z\min}}$$""",
        "text": r"""<strong>Zener Diode Regulator:</strong> Operates in reverse breakdown ($V_Z$). Zener breakdown ($< 5\text{ V}$, field ionization, negative temp-co); Avalanche breakdown ($> 6\text{ V}$, impact ionization, positive temp-co). Shunts excess current through Zener, maintaining stable output voltage across line and load variations."""
    },
    'beee-q19': {
        "eq": r"""$$I_E = I_B + I_C, \quad I_C = \beta I_B + I_{CEO}, \quad \beta = \frac{\alpha}{1 - \alpha}, \quad \alpha = \frac{\beta}{1 + \beta}$$""",
        "text": r"""<strong>BJT Characteristics:</strong> Emitter heavily doped, base thin and lightly doped, collector large. CE configuration provides high current gain ($\beta = \frac{\alpha}{1-\alpha} \sim 100$) and power gain. Active region (EBJ forward, CBJ reverse) for amplification; Cut-off and Saturation for digital switching."""
    },
    'beee-q20': {
        "eq": r"""$$I_B \ge \frac{I_{C(sat)}}{\beta_{\min}}, \quad A_v = \frac{v_{out}}{v_{in}} \approx -\frac{R_C \parallel R_L}{r_e'}, \quad \phi = 180^\circ$$""",
        "text": r"""<strong>Transistor Applications:</strong> BJT as switch: OFF in cut-off ($V_{out} = V_{CC}$), ON in saturation ($V_{out} \approx 0.2\text{ V}$). Single-stage CE amplifier: Voltage divider bias stabilizes Q-point; bypass capacitor $C_E$ maximizes AC gain; output voltage exhibits an exact $180^\circ$ phase inversion."""
    },
    'beee-q21': {
        "eq": r"""$$V_+ = V_- \ (\text{Virtual Short}), \quad I_+ = I_- = 0\text{ A}, \quad A_{OL} = \infty, \; R_{in} = \infty, \; R_{out} = 0, \; CMRR = \infty$$""",
        "text": r"""<strong>Ideal Op-Amp & Virtual Ground:</strong> Infinite open-loop gain ($A_{OL} \to \infty$) with negative feedback forces differential input voltage $V_d = V_+ - V_- = 0$, establishing a virtual short. Infinite input impedance ensures zero terminal input current ($I_+ = I_- = 0$). Grounding non-inverting terminal creates a virtual ground at inverting node."""
    },
    'beee-q22': {
        "eq": r"""$$A_{v(inv)} = -\frac{R_f}{R_1}, \quad A_{v(non-inv)} = 1 + \frac{R_f}{R_1}, \quad A_{v(buffer)} = 1.0, \quad Z_{in(buffer)} \approx \infty, \; Z_{out(buffer)} \approx 0$$""",
        "text": r"""<strong>Op-Amp Configurations:</strong> Inverting amplifier provides stabilized gain $A_v = -R_f/R_1$ with $180^\circ$ phase inversion. Non-inverting amplifier provides in-phase gain $A_v = 1 + R_f/R_1 \ge 1$ with ultra-high input impedance. Voltage follower ($R_f=0$) provides unity gain for impedance buffer isolation."""
    },
    'beee-q23': {
        "eq": r"""$$V_{out} = -\left[\frac{R_f}{R_1}V_1 + \frac{R_f}{R_2}V_2\right], \quad V_{out(int)} = -\frac{1}{RC}\int V_{in}\,dt, \quad V_{out(diff)} = -RC \frac{dV_{in}}{dt}$$""",
        "text": r"""<strong>Mathematical Op-Amp Circuits:</strong> Summing amplifier adds input signals with weighted gains. Difference amplifier subtracts common-mode noise. Integrator (feedback capacitor $C$) ramps output proportional to input integral. Differentiator (input capacitor $C$) differentiates input rate of change."""
    },
    'beee-q24': {
        "eq": r"""$$A - B = A + (\text{2’s complement of } B), \quad \text{2’s Comp} = \text{1’s Comp} + 1, \quad \text{Range: } -2^{n-1} \le N \le +2^{n-1}-1$$""",
        "text": r"""<strong>2’s Complement Arithmetic:</strong> Subtraction $A - B$ executed by adding 2’s complement of $B$ to $A$. An end carry signifies a positive answer (discard end carry). Absence of end carry indicates negative answer in 2’s complement form (take 2’s complement of sum to obtain true magnitude)."""
    },
    'beee-q25': {
        "eq": r"""$$\overline{A \cdot B} = \bar{A} + \bar{B}, \quad \overline{A + B} = \bar{A} \cdot \bar{B}, \quad A \oplus B = \bar{A} B + A \bar{B}, \quad \text{NAND/NOR: Universal}$$""",
        "text": r"""<strong>Universal Gates & De Morgan’s Laws:</strong> Any logic function can be realized using solely NAND gates or solely NOR gates. De Morgan’s first law: NAND is equivalent to bubbled OR ($\overline{AB} = \bar{A}+\bar{B}$). De Morgan’s second law: NOR is equivalent to bubbled AND ($\overline{A+B} = \bar{A}\bar{B}$)."""
    },
    'beee-q26': {
        "eq": r"""$$\text{HA: } S = A \oplus B, C = AB; \quad \text{FA: } S = A \oplus B \oplus C_{in}, C_{out} = AB + C_{in}(A \oplus B)$$""",
        "text": r"""<strong>Arithmetic Adders:</strong> Half Adder computes sum and carry of two bits using one XOR gate and one AND gate. Full Adder computes sum and carry of three bits ($A, B, C_{in}$), synthesized using two half adders and one OR gate ($S = A \oplus B \oplus C_{in}$, $C_{out} = AB + C_{in}(A \oplus B)$)."""
    }
}

BEEE_EXAM_QUESTIONS = {
    "beee-q1": "State and explain Kirchhoff's Current Law (KCL) and Kirchhoff's Voltage Law (KVL) with algebraic sign conventions. Explain how they form the basis of mesh and nodal analysis.",
    "beee-q2": "Explain Nodal Voltage Analysis. Explain the supernode concept when an ideal independent voltage source is connected between two non-reference nodes, and solve a numerical problem.",
    "beee-q3": "State Superposition Theorem. Explain its conditions of applicability and limitations. Find the current through the load resistor in a multi-source DC network with independent voltage and current sources.",
    "beee-q4": "State Thevenin's and Norton's Theorems and derive their dual relationship. Find the Thevenin and Norton equivalent circuits across the detector terminals of an unbalanced bridge network.",
    "beee-q5": "State and prove Maximum Power Transfer Theorem for a DC network. Derive the expression for maximum power and show that the transmission efficiency at maximum power is 50%.",
    "beee-q6": "Explain the generation of sinusoidal alternating voltage by a coil rotating in a uniform magnetic field. Define instantaneous value, amplitude, time period, frequency, and phasor representation.",
    "beee-q7": "Derive the mathematical expressions for the RMS value, Average value, Form Factor, and Peak Factor of a pure sinusoidal alternating voltage waveform.",
    "beee-q8": "Derive the expressions for impedance, current, phase angle, and power in a series R-L and series R-C circuit excited by sinusoidal AC. Explain the impedance and power triangles with a numerical problem.",
    "beee-q9": "Derive the condition and expression for resonant frequency in a series R-L-C circuit. Derive the expressions for Quality factor (Q) and half-power bandwidth (BW).",
    "beee-q10": "Define MMF, magnetic flux, reluctance, permeance, and flux density. Compare electric and magnetic circuits in detail. Explain the B-H curve and solve a series magnetic circuit with an air gap.",
    "beee-q11": "Explain the construction and working principle of a single-phase transformer. Derive the EMF equation and the condition for maximum efficiency.",
    "beee-q12": "Explain the constructional details of a DC machine with a neat sketch. Explain the operating principle of a DC generator and derive the generator EMF equation.",
    "beee-q13": "Explain the working principle of a DC motor and the physical significance of Back-EMF. Derive the DC motor armature torque equation and speed relationship.",
    "beee-q14": "Derive the relationship between line and phase voltages and currents in balanced 3-phase Star (Y) and Delta (Δ) connected systems. Derive the expression for total 3-phase active power.",
    "beee-q15": "Draw the schematic layout of a residential distribution board. Explain the two-way control of a lamp (staircase wiring). Explain pipe earthing and compare Fuse, MCB, and ELCB/RCCB.",
    "beee-q16": "Distinguish between intrinsic and extrinsic semiconductors. Explain the formation of a PN junction, depletion layer, and barrier potential. Explain forward and reverse bias V-I characteristics.",
    "beee-q17": "Explain the working of half-wave and full-wave bridge rectifiers with circuit diagrams and waveforms. Derive expressions for V_dc, V_rms, rectification efficiency, and ripple factor. Explain the role of capacitor filter.",
    "beee-q18": "Explain the breakdown mechanisms in a PN junction: Avalanche breakdown versus Zener breakdown. Explain the operation of a Zener diode as a shunt voltage regulator with circuit diagram and design equations.",
    "beee-q19": "Describe the physical structure and operation of an NPN Bipolar Junction Transistor. Plot and explain the Common Emitter (CE) input and output characteristics, identifying all operating regions. Derive the relationship between α and β.",
    "beee-q20": "Explain the operation of a BJT as a digital switch with operating conditions. Draw the circuit diagram of a single-stage Common Emitter (CE) voltage amplifier with voltage-divider biasing and explain its operation and 180° phase inversion.",
    "beee-q21": "Explain the internal architectural block diagram of an operational amplifier and pinout of IC 741. List ideal op-amp characteristics and explain the concepts of Virtual Ground and Virtual Short.",
    "beee-q22": "Derive the closed-loop voltage gain expressions for Inverting and Non-Inverting op-amp configurations. Explain the Voltage Follower (Buffer) circuit and its practical application.",
    "beee-q23": "Explain the circuit operations and derive the output voltage expressions for an op-amp Summing Amplifier, Difference Amplifier, Integrator, and Differentiator.",
    "beee-q24": "Explain decimal, binary, octal, and hexadecimal number systems with radix conversion examples. Explain 1's and 2's complement representations and perform binary subtraction using 2's complement with overflow rules.",
    "beee-q25": "Explain basic and universal logic gates with symbols, Boolean expressions, and truth tables. Show how AND, OR, NOT gates are realized using only NAND gates and only NOR gates. State and prove De Morgan's laws.",
    "beee-q26": "Design a Half Adder and a Full Adder circuit. Write their truth tables, obtain minimized Boolean expressions using K-maps, and implement a Full Adder using two Half Adders and an OR gate."
}
