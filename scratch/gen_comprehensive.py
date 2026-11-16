# -*- coding: utf-8 -*-
"""
Content generator for Subject 11: Comprehensive Course Work (EET308 / COMPREHENSIVE)
KTU 2019 Scheme S6 Electrical & Electronics Engineering Core Disciplines.
All answers are written from the perspective of an experienced electrical engineering professor:
clear, direct, mathematically rigorous, with step-by-step intermediate equations.
All strings are raw multiline strings (r'''...''') to prevent LaTeX backslash corruption.

Covers 5 Core Modules:
- Module 1: Electrical Circuits and Electromagnetic Fields
- Module 2: Electrical Machines and Power Systems
- Module 3: Control Systems and Instrumentation
- Module 4: Analog and Digital Electronics
- Module 5: Power Electronics and Electric Drives

Exports:
- COMPREHENSIVE_MODULES (5 modules, 26 questions: comp-q1 to comp-q26)
- COMPREHENSIVE_BYHEART (26 entries: qid -> {eq, text})
- COMPREHENSIVE_EXAM_QUESTIONS (26 entries: qid -> question_text)
"""

COMPREHENSIVE_MODULES = [
    {
        "module_id": "comp-m1",
        "module_num": "Module 1",
        "module_title": "Electrical Circuits & Electromagnetic Fields",
        "questions": [
            {
                "qid": "comp-q1",
                "marks": 7,
                "type": "Analytical",
                "title": "Network Theorems in AC and DC Circuits & Maximum Power Transfer Proof",
                "yt_query": "thevenin norton maximum power transfer theorem ac dc proof",
                "img_path": "images/comp/thevenin_norton_mpt.png",
                "img_caption": "Figure 1.1: Thévenin and Norton AC Equivalent Circuits and Maximum Power Transfer Characteristic Curve",
                "answer": r"""
Network theorems form the fundamental analytical toolkit for simplifying complex, multiloop electrical networks into manageable equivalent representations. In linear, bilateral lumped-parameter circuits, Thévenin's, Norton's, Superposition, and the Maximum Power Transfer theorems provide rigorous methodologies for evaluating branch currents, node voltages, and power dissipation.

1. Thévenin's and Norton's Theorems:
- Thévenin's Theorem states that any linear, bilateral, active two-terminal network containing independent or dependent sources and impedances can be replaced at its terminal pair $(A-B)$ by an equivalent circuit consisting of a single ideal voltage source $\mathbf{V}_{th}$ in series with an equivalent impedance $\mathbf{Z}_{th}$.
  - The open-circuit voltage $\mathbf{V}_{th}$ is the potential difference appearing across terminals $A-B$ when the load impedance $\mathbf{Z}_L$ is disconnected ($\mathbf{V}_{th} = \mathbf{V}_{oc}$).
  - The Thévenin impedance $\mathbf{Z}_{th}$ is the impedance looking back into the de-energized network across terminals $A-B$ with all independent voltage sources replaced by short circuits ($V=0$) and all independent current sources replaced by open circuits ($I=0$), while retaining all dependent sources.
- Norton's Theorem is the dual of Thévenin's theorem. It replaces the network by an ideal short-circuit current source $\mathbf{I}_N$ connected in parallel with an internal Norton admittance $\mathbf{Y}_N$ (or impedance $\mathbf{Z}_N$).
  - The Norton current is the current flowing through a direct short circuit placed across terminals $A-B$:
  $$\mathbf{I}_N = \mathbf{I}_{sc} = \frac{\mathbf{V}_{th}}{\mathbf{Z}_{th}}$$
  - The Norton impedance equals the Thévenin impedance: $\mathbf{Z}_N = \mathbf{Z}_{th}$.

2. Superposition Theorem:
The Superposition Theorem states that in any linear, bilateral electrical network energized by multiple independent sources, the resultant current or voltage in any branch is the algebraic (or phasor) sum of the currents or voltages produced by each independent source acting alone, with all other independent sources replaced by their respective internal impedances (independent voltage sources short-circuited and independent current sources open-circuited). Dependent sources are left unaltered throughout the decomposition.
$$\mathbf{I}_k = \sum_{m=1}^{N_v} \mathbf{I}_{k, V_m} + \sum_{n=1}^{N_i} \mathbf{I}_{k, I_n}$$
Note that superposition applies strictly to linear responses (current and voltage) and cannot be applied directly to non-linear power quantities ($P \neq \sum P_i$ because $P \propto I^2$).

3. Maximum Power Transfer Theorem:
The Maximum Power Transfer Theorem defines the necessary and sufficient conditions under which an active source network delivers maximum real active power $P_L$ to an adjustable load.

Case A: DC Source and Resistive Load ($R_L$ variable):
Consider a DC network represented by its Thévenin equivalent $(V_{th}, R_{th})$ feeding a variable load resistor $R_L$. The loop current is:
$$I_L = \frac{V_{th}}{R_{th} + R_L}$$
The real power absorbed by the load is:
$$P_L = I_L^2 R_L = \left( \frac{V_{th}}{R_{th} + R_L} \right)^2 R_L = \frac{V_{th}^2 R_L}{(R_{th} + R_L)^2}$$
To determine the condition for maximum load power, we take the first derivative of $P_L$ with respect to $R_L$ and set it to zero:
$$\frac{dP_L}{dR_L} = V_{th}^2 \cdot \frac{(R_{th} + R_L)^2 \cdot 1 - R_L \cdot 2(R_{th} + R_L)}{(R_{th} + R_L)^4} = 0$$
$$(R_{th} + R_L) - 2 R_L = 0 \implies R_{th} - R_L = 0 \implies R_L = R_{th}$$
Checking the second derivative confirms a true maximum:
$$\left. \frac{d^2 P_L}{dR_L^2} \right|_{R_L = R_{th}} = -\frac{V_{th}^2}{8 R_{th}^3} < 0$$
Thus, maximum power transfer in a DC circuit occurs when the load resistance equals the internal Thévenin resistance ($R_L = R_{th}$). Under this matched condition, the maximum power delivered is:
$$P_{L,\max} = \frac{V_{th}^2 R_{th}}{(R_{th} + R_{th})^2} = \frac{V_{th}^2 R_{th}}{4 R_{th}^2} = \frac{V_{th}^2}{4 R_{th}}$$
The total power generated by the source is:
$$P_{source} = V_{th} I_L = V_{th} \left( \frac{V_{th}}{2 R_{th}} \right) = \frac{V_{th}^2}{2 R_{th}}$$
The transmission efficiency at maximum power transfer is:
$$\eta = \frac{P_{L,\max}}{P_{source}} \times 100\% = \frac{V_{th}^2 / (4 R_{th})}{V_{th}^2 / (2 R_{th})} \times 100\% = 50\%$$
Half the generated power is unavoidably dissipated as heat inside the internal source resistance $R_{th}$. Consequently, maximum power transfer is critical in communications and RF electronics (where signal strength is in microwatts/milliwatts and reflection must be eliminated), whereas power systems prioritize transmission efficiency ($\eta > 95\%$) by operating with source internal impedances far smaller than the load impedance ($R_{th} \ll R_L$).

Case B: AC Source and Complex Load Impedance ($\mathbf{Z}_L = R_L + jX_L$ with both $R_L$ and $X_L$ independently variable):
Let the source network be represented by its AC Thévenin equivalent $\mathbf{V}_{th} = V_{th} \angle 0^\circ$ and $\mathbf{Z}_{th} = R_{th} + jX_{th}$.
The load impedance is $\mathbf{Z}_L = R_L + jX_L$.
The phasor current flowing through the circuit is:
$$\mathbf{I}_L = \frac{\mathbf{V}_{th}}{\mathbf{Z}_{th} + \mathbf{Z}_L} = \frac{V_{th}}{(R_{th} + R_L) + j(X_{th} + X_L)}$$
The magnitude of the load current is:
$$I_L = |\mathbf{I}_L| = \frac{V_{th}}{\sqrt{(R_{th} + R_L)^2 + (X_{th} + X_L)^2}}$$
The active power dissipated exclusively in the resistive part of the load $R_L$ is:
$$P_L = I_L^2 R_L = \frac{V_{th}^2 R_L}{(R_{th} + R_L)^2 + (X_{th} + X_L)^2}$$
To maximize $P_L$, we first optimize with respect to the reactive component $X_L$:
$$\frac{\partial P_L}{\partial X_L} = -\frac{V_{th}^2 R_L \cdot 2(X_{th} + X_L)}{\left[ (R_{th} + R_L)^2 + (X_{th} + X_L)^2 \right]^2} = 0$$
$$(X_{th} + X_L) = 0 \implies X_L = -X_{th}$$
This condition means the load reactance must be equal in magnitude and opposite in sign to the internal source reactance (conjugate reactive cancellation, achieving circuit resonance where net loop reactance is zero). Substituting $X_L = -X_{th}$ into the power equation yields:
$$P_L = \frac{V_{th}^2 R_L}{(R_{th} + R_L)^2}$$
Differentiating this residual expression with respect to $R_L$ and setting to zero yields the identical result as the DC case:
$$\frac{\partial P_L}{\partial R_L} = 0 \implies R_L = R_{th}$$
Combining both conditions:
$$\mathbf{Z}_L = R_L + jX_L = R_{th} - jX_{th} = \mathbf{Z}_{th}^*$$
Hence, maximum power transfer in an AC circuit occurs when the load impedance is the complex conjugate of the Thévenin source impedance ($\mathbf{Z}_L = \mathbf{Z}_{th}^*$). The maximum active power delivered to the load is:
$$P_{L,\max} = \frac{V_{th}^2}{4 R_{th}}$$

Case C: AC Load with Variable Magnitude but Fixed Phase Angle ($\mathbf{Z}_L = Z_L \angle \theta_L$):
When only the magnitude $Z_L$ can be adjusted while its power factor angle $\theta_L$ is constant, maximizing $P_L$ yields:
$$Z_L = |\mathbf{Z}_{th}| = \sqrt{R_{th}^2 + X_{th}^2}$$
The load impedance magnitude must equal the magnitude of the Thévenin impedance.
"""
            },
            {
                "qid": "comp-q2",
                "marks": 7,
                "type": "Derivation",
                "title": "Transient Analysis of Series RL, RC, and RLC Circuits for DC Step Excitation",
                "yt_query": "transient analysis series rl rc rlc dc step excitation differential equation",
                "img_path": "images/comp/rlc_transient_waveforms.png",
                "img_caption": "Figure 1.2: Second-Order Series RLC Transient Response Regimes: Overdamped, Critically Damped, and Underdamped",
                "answer": r"""
Electrical transients occur during transitions between distinct steady-state operating conditions following switching operations, faults, or sudden load changes. Energy-storing elements—inductors ($W_L = \frac{1}{2} L i^2$) and capacitors ($W_C = \frac{1}{2} C v^2$)—enforce boundary conditions preventing instantaneous changes in inductor current ($i_L(0^-) = i_L(0^+)$) and capacitor voltage ($v_C(0^-) = v_C(0^+)$).

1. Series RL Circuit with DC Step Excitation $V_s u(t)$:
Consider an unenergized inductor $L$ in series with a resistor $R$ connected to a DC source $V_s$ at time $t=0$. Applying Kirchhoff's Voltage Law (KVL) for $t \ge 0$:
$$R i(t) + L \frac{di(t)}{dt} = V_s$$
Rearranging into standard linear first-order differential form:
$$\frac{di(t)}{dt} + \frac{R}{L} i(t) = \frac{V_s}{L}$$
The integrating factor is $I.F. = e^{\int \frac{R}{L} dt} = e^{\frac{R}{L}t}$. Multiplying both sides:
$$\frac{d}{dt}\left[ i(t) e^{\frac{R}{L}t} \right] = \frac{V_s}{L} e^{\frac{R}{L}t}$$
Integrating with respect to $t$:
$$i(t) e^{\frac{R}{L}t} = \frac{V_s}{L} \cdot \frac{L}{R} e^{\frac{R}{L}t} + K = \frac{V_s}{R} e^{\frac{R}{L}t} + K$$
$$i(t) = \frac{V_s}{R} + K e^{-\frac{R}{L}t}$$
Applying the initial boundary condition $i(0^+) = i(0^-) = 0$:
$$0 = \frac{V_s}{R} + K \implies K = -\frac{V_s}{R}$$
Substituting $K$ yields the complete analytical solution:
$$i(t) = \frac{V_s}{R} \left( 1 - e^{-\frac{t}{\tau}} \right) \quad \text{for } t \ge 0$$
where the inductive time constant is defined as:
$$\tau = \frac{L}{R} \quad \text{seconds}$$
The time constant $\tau$ represents the time required for the current to reach $1 - e^{-1} \approx 63.2\%$ of its steady-state final value $I_{ss} = \frac{V_s}{R}$. The induced inductor voltage is:
$$v_L(t) = L \frac{di(t)}{dt} = L \cdot \frac{V_s}{R} \left( \frac{R}{L} e^{-\frac{t}{\tau}} \right) = V_s e^{-\frac{t}{\tau}}$$
At $t=0^+$, $v_L(0^+) = V_s$ (the inductor opposes current rise and acts as an open circuit). At $t \to \infty$, $v_L(\infty) = 0$ (the inductor acts as an ideal short circuit).

2. Series RC Circuit with DC Step Excitation $V_s u(t)$:
For an uncharged capacitor $C$ in series with resistor $R$ energized by $V_s$ at $t=0$, KVL gives:
$$R i(t) + v_C(t) = V_s \implies R C \frac{dv_C(t)}{dt} + v_C(t) = V_s$$
$$\frac{dv_C(t)}{dt} + \frac{1}{RC} v_C(t) = \frac{V_s}{RC}$$
Solving by the same integrating factor method with boundary condition $v_C(0^+) = v_C(0^-) = 0$:
$$v_C(t) = V_s \left( 1 - e^{-\frac{t}{\tau}} \right) \quad \text{where } \tau = R C \text{ seconds}$$
The charging current is:
$$i(t) = C \frac{dv_C(t)}{dt} = \frac{V_s}{R} e^{-\frac{t}{\tau}}$$
At $t=0^+$, $v_C(0^+) = 0$ and $i(0^+) = \frac{V_s}{R}$ (uncharged capacitor behaves as a short circuit). At $t \to \infty$, $v_C(\infty) = V_s$ and $i(\infty) = 0$ (fully charged capacitor behaves as an open circuit).

3. Series RLC Circuit Transient Analysis:
Applying KVL to a series RLC loop energized by DC voltage $V_s$:
$$R i(t) + L \frac{di(t)}{dt} + \frac{1}{C}\int_0^t i(\tau) d\tau + v_C(0^+) = V_s$$
Differentiating with respect to $t$:
$$L \frac{d^2 i(t)}{dt^2} + R \frac{di(t)}{dt} + \frac{1}{C} i(t) = 0$$
Dividing by $L$:
$$\frac{d^2 i(t)}{dt^2} + \frac{R}{L}\frac{di(t)}{dt} + \frac{1}{LC} i(t) = 0$$
This is a homogeneous second-order linear differential equation with constant coefficients. Writing in standard second-order control/circuit notation:
$$\frac{d^2 i(t)}{dt^2} + 2\alpha \frac{di(t)}{dt} + \omega_0^2 i(t) = 0$$
where:
- Damping attenuation factor: $\alpha = \frac{R}{2L} \text{ rad/s}$
- Undamped resonant angular frequency: $\omega_0 = \frac{1}{\sqrt{LC}} \text{ rad/s}$
- Damping ratio: $\zeta = \frac{\alpha}{\omega_0} = \frac{R}{2L} \sqrt{LC} = \frac{R}{2}\sqrt{\frac{C}{L}}$

The characteristic algebraic equation is:
$$s^2 + 2\alpha s + \omega_0^2 = 0 \implies s_{1,2} = -\alpha \pm \sqrt{\alpha^2 - \omega_0^2}$$

Depending on the discriminant $\Delta = \alpha^2 - \omega_0^2$, three distinct physical regimes emerge:

Case 1: Overdamped System ($\alpha > \omega_0$, $\zeta > 1 \implies R > 2\sqrt{L/C}$):
The characteristic roots are real, distinct, and negative:
$$s_1 = -\alpha + \sqrt{\alpha^2 - \omega_0^2}, \quad s_2 = -\alpha - \sqrt{\alpha^2 - \omega_0^2}$$
The general solution for current is:
$$i(t) = A_1 e^{s_1 t} + A_2 e^{s_2 t}$$
With initial conditions $i(0^+) = 0$ and $\left.\frac{di}{dt}\right|_{0^+} = \frac{V_s}{L}$:
$$i(t) = \frac{V_s}{L(s_1 - s_2)}\left( e^{s_1 t} - e^{s_2 t} \right)$$
The response is purely non-oscillatory and sluggish; the capacitor charges slowly to $V_s$ without overshoot.

Case 2: Critically Damped System ($\alpha = \omega_0$, $\zeta = 1 \implies R = 2\sqrt{L/C}$):
The characteristic roots are real, equal, and negative:
$$s_1 = s_2 = -\alpha = -\frac{R}{2L}$$
The solution takes the repeated root form:
$$i(t) = (A_1 + A_2 t) e^{-\alpha t}$$
Applying $i(0^+) = 0 \implies A_1 = 0$, and $\left.\frac{di}{dt}\right|_{0^+} = A_2 = \frac{V_s}{L}$:
$$i(t) = \frac{V_s}{L} t e^{-\frac{R}{2L}t}$$
Critical damping provides the fastest possible monotonic transition to steady-state without producing any oscillatory overshoot.

Case 3: Underdamped System ($\alpha < \omega_0$, $\zeta < 1 \implies R < 2\sqrt{L/C}$):
The roots are complex conjugate pairs located in the left half of the s-plane:
$$s_{1,2} = -\alpha \pm j \omega_d \quad \text{where } \omega_d = \sqrt{\omega_0^2 - \alpha^2} = \omega_0 \sqrt{1 - \zeta^2}$$
The current response is an exponentially damped sinusoidal oscillation:
$$i(t) = e^{-\alpha t} \left( B_1 \cos\omega_d t + B_2 \sin\omega_d t \right)$$
Using $i(0^+) = 0 \implies B_1 = 0$, and $\left.\frac{di}{dt}\right|_{0^+} = \omega_d B_2 = \frac{V_s}{L} \implies B_2 = \frac{V_s}{\omega_d L}$:
$$i(t) = \frac{V_s}{\omega_d L} e^{-\alpha t} \sin\omega_d t$$
The capacitor voltage is:
$$v_C(t) = V_s - e^{-\alpha t}\left[ V_s \cos\omega_d t + \frac{\alpha V_s}{\omega_d}\sin\omega_d t \right] = V_s \left[ 1 - \frac{\omega_0}{\omega_d} e^{-\alpha t} \sin(\omega_d t + \theta) \right]$$
where $\theta = \tan^{-1}\left(\frac{\omega_d}{\alpha}\right) = \cos^{-1}\zeta$. The capacitor voltage overshoots $V_s$, reaching a peak of up to $2 V_s$ when damping is negligible ($R \to 0$).
"""
            },
            {
                "qid": "comp-q3",
                "marks": 7,
                "type": "Derivation",
                "title": "AC Resonance in Series and Parallel Circuits: Resonant Frequency, Bandwidth, and Q-Factor",
                "yt_query": "ac resonance series parallel rlc bandwidth quality factor selectivity",
                "img_path": "images/comp/series_parallel_resonance.png",
                "img_caption": "Figure 1.3: Frequency Response Curves for Series (Impedance Minimum) and Parallel (Impedance Maximum) Resonant Circuits",
                "answer": r"""
Resonance in an AC circuit occurs at a specific excitation frequency at which the inductive reactance and capacitive reactance cancel each other out, making the net circuit impedance purely resistive. Under resonance, the input voltage and total input current are exactly in phase, resulting in a unity power factor ($\cos\phi = 1.0$).

1. Series RLC Resonance:
Consider an inductor $L$, capacitor $C$, and resistor $R$ connected in series across an AC source $\mathbf{V} = V \angle 0^\circ$ of variable angular frequency $\omega$.
The total complex input impedance is:
$$\mathbf{Z}(j\omega) = R + j\left( \omega L - \frac{1}{\omega C} \right)$$
The condition for resonance is that the imaginary reactive part of $\mathbf{Z}(j\omega)$ becomes identically zero:
$$\text{Im}[\mathbf{Z}(j\omega_0)] = \omega_0 L - \frac{1}{\omega_0 C} = 0 \implies \omega_0^2 = \frac{1}{LC}$$
$$\omega_0 = \frac{1}{\sqrt{LC}} \text{ rad/s} \quad \implies \quad f_0 = \frac{1}{2\pi \sqrt{LC}} \text{ Hz}$$

Characteristics of Series Resonance:
- Impedance is at its absolute minimum: $\mathbf{Z}_0 = R$.
- Current is at its absolute maximum: $\mathbf{I}_0 = \frac{\mathbf{V}}{R} \angle 0^\circ$.
- Power factor is strictly unity ($\cos\phi = 1.0$).
- Voltage Magnification: Although the net reactive voltage is zero ($V_L + V_C = 0$), individual voltages across $L$ and $C$ can be dangerously higher than the applied supply voltage $V$:
$$V_L = I_0 \omega_0 L = \frac{V}{R} \omega_0 L = Q \cdot V$$
$$V_C = \frac{I_0}{\omega_0 C} = \frac{V}{R \omega_0 C} = Q \cdot V$$
where $Q$ is the Quality Factor of the resonant circuit.

2. Quality Factor ($Q$) and Bandwidth ($BW$):
The Quality Factor $Q$ is defined physically as $2\pi$ times the ratio of maximum energy stored in the circuit to the energy dissipated per cycle:
$$Q = 2\pi \frac{\text{Maximum Energy Stored}}{\text{Energy Dissipated per Cycle}} = 2\pi \frac{\frac{1}{2} L I_0^2}{I_{rms}^2 R \cdot T} = 2\pi \frac{\frac{1}{2} L I_0^2}{\frac{1}{2} I_0^2 R (2\pi / \omega_0)} = \frac{\omega_0 L}{R}$$
Substituting $\omega_0 = 1/\sqrt{LC}$:
$$Q = \frac{\omega_0 L}{R} = \frac{1}{\omega_0 C R} = \frac{1}{R}\sqrt{\frac{L}{C}}$$

Half-Power Frequencies ($\omega_1, \omega_2$):
The half-power frequencies (or $3\text{ dB}$ cutoff frequencies) occur when the active power delivered to the circuit drops to half of its maximum resonant value ($P = \frac{1}{2} P_{\max}$), which corresponds to the current falling to $I = \frac{I_0}{\sqrt{2}} \approx 0.707 I_0$.
Setting $|\mathbf{Z}| = \sqrt{2} R$:
$$\sqrt{R^2 + \left( \omega L - \frac{1}{\omega C} \right)^2} = \sqrt{2} R \implies \left( \omega L - \frac{1}{\omega C} \right)^2 = R^2$$
$$\omega L - \frac{1}{\omega C} = \pm R$$
- For lower cutoff frequency $\omega_1$: $\frac{1}{\omega_1 C} - \omega_1 L = R \implies \omega_1^2 + \frac{R}{L}\omega_1 - \frac{1}{LC} = 0$
$$\omega_1 = -\frac{R}{2L} + \sqrt{\left(\frac{R}{2L}\right)^2 + \frac{1}{LC}}$$
- For upper cutoff frequency $\omega_2$: $\omega_2 L - \frac{1}{\omega_2 C} = R \implies \omega_2^2 - \frac{R}{L}\omega_2 - \frac{1}{LC} = 0$
$$\omega_2 = +\frac{R}{2L} + \sqrt{\left(\frac{R}{2L}\right)^2 + \frac{1}{LC}}$$

The Bandwidth ($BW$) is the difference between upper and lower half-power frequencies:
$$BW = \Delta\omega = \omega_2 - \omega_1 = \frac{R}{L} \text{ rad/s} \quad \implies \quad BW = \Delta f = \frac{R}{2\pi L} \text{ Hz}$$
Dividing $\omega_0$ by $BW$:
$$\frac{\omega_0}{BW} = \frac{\omega_0}{R/L} = \frac{\omega_0 L}{R} = Q \implies BW = \frac{\omega_0}{Q} = \frac{f_0}{Q}$$
The resonant frequency is the geometric mean of the half-power frequencies:
$$\omega_0 = \sqrt{\omega_1 \omega_2}$$
Selectivity is inversely proportional to bandwidth: a high-$Q$ circuit exhibits a narrow bandwidth, offering high selectivity to isolate specific frequency signals (essential in RF tuning).

3. Parallel AC Resonance (Practical Tank Circuit):
Consider a practical inductor with internal winding resistance $R_L$ and inductance $L$ connected in parallel with a pure capacitor $C$.
The total circuit admittance is:
$$\mathbf{Y}(j\omega) = \mathbf{Y}_L + \mathbf{Y}_C = \frac{1}{R_L + j\omega L} + j\omega C = \frac{R_L - j\omega L}{R_L^2 + \omega^2 L^2} + j\omega C$$
$$\mathbf{Y}(j\omega) = \frac{R_L}{R_L^2 + \omega^2 L^2} + j\left( \omega C - \frac{\omega L}{R_L^2 + \omega^2 L^2} \right)$$
At parallel resonance, the circuit exhibits unity power factor, which requires the imaginary susceptance to vanish:
$$\omega_r C - \frac{\omega_r L}{R_L^2 + \omega_r^2 L^2} = 0 \implies C = \frac{L}{R_L^2 + \omega_r^2 L^2}$$
$$R_L^2 + \omega_r^2 L^2 = \frac{L}{C} \implies \omega_r^2 L^2 = \frac{L}{C} - R_L^2$$
Dividing by $L^2$:
$$\omega_r = \sqrt{\frac{1}{LC} - \frac{R_L^2}{L^2}} \text{ rad/s}$$
Note that for resonance to exist in a practical tank circuit, the condition $L/C > R_L^2$ must be satisfied. If $R_L \ll \omega L$ (ideal coil), $\omega_r \approx \frac{1}{\sqrt{LC}} = \omega_0$.

Dynamic Impedance ($Z_d$) at Parallel Resonance:
At resonance, the susceptance is zero, leaving only the conductance:
$$\mathbf{Y}_r = \frac{R_L}{R_L^2 + \omega_r^2 L^2} = \frac{R_L}{L/C} = \frac{C R_L}{L}$$
The equivalent dynamic impedance $Z_d$ of the parallel tank at resonance is:
$$Z_d = \frac{1}{\mathbf{Y}_r} = \frac{L}{C R_L}$$
Since $R_L$ is generally small, $Z_d$ is extremely large (anti-resonance). Thus:
- Parallel resonance exhibits maximum impedance $Z_d = \frac{L}{C R_L}$ and minimum line current $I_{line} = \frac{V}{Z_d}$.
- Circulating tank currents inside the $L-C$ loop are magnified: $I_{circ} = Q \cdot I_{line}$.
"""
            },
            {
                "qid": "comp-q4",
                "marks": 7,
                "type": "Derivation",
                "title": "Three-Phase Star/Delta Connections & Two-Wattmeter Power Measurement Method",
                "yt_query": "three phase star delta two wattmeter method power measurement derivation",
                "img_path": "images/comp/two_wattmeter_method.png",
                "img_caption": "Figure 1.4: Two-Wattmeter Connection in a Three-Phase Three-Wire System and Corresponding Phasor Diagram",
                "answer": r"""
Polyphase systems, predominantly balanced three-phase AC systems, provide constant instantaneous power delivery, higher generator utilization, and reduced copper volume in transmission lines compared to single-phase systems.

1. Star (Y) Connection Relationships:
In a balanced star connection, the three line terminals $R, Y, B$ are fed from phase windings meeting at a common neutral point $N$.
- Line currents equal phase currents:
$$I_L = I_{ph}$$
- The line voltage is the phasor difference between two phase voltages:
$$\mathbf{V}_{RY} = \mathbf{V}_{RN} - \mathbf{V}_{YN}$$
With balanced phase voltages $\mathbf{V}_{RN} = V_{ph} \angle 0^\circ$, $\mathbf{V}_{YN} = V_{ph} \angle -120^\circ$, $\mathbf{V}_{BN} = V_{ph} \angle -240^\circ$:
$$\mathbf{V}_{RY} = V_{ph} (1 - \cos(-120^\circ) - j\sin(-120^\circ)) = V_{ph}\left( 1 - \left(-\frac{1}{2}\right) + j\frac{\sqrt{3}}{2} \right) = V_{ph}\left( \frac{3}{2} + j\frac{\sqrt{3}}{2} \right)$$
$$|\mathbf{V}_{RY}| = V_{ph} \sqrt{\left(\frac{3}{2}\right)^2 + \left(\frac{\sqrt{3}}{2}\right)^2} = V_{ph} \sqrt{\frac{9}{4} + \frac{3}{4}} = \sqrt{3} V_{ph}$$
The phase angle is $\tan^{-1}\left( \frac{\sqrt{3}/2}{3/2} \right) = 30^\circ$. Thus:
$$V_L = \sqrt{3} V_{ph} \quad (\text{Line voltage leads phase voltage by } 30^\circ)$$

2. Delta ($\Delta$) Connection Relationships:
In a balanced delta connection, line voltages equal phase voltages:
$$V_L = V_{ph}$$
Line current is the difference between two phase currents ($\mathbf{I}_R = \mathbf{I}_{RY} - \mathbf{I}_{BR}$):
$$I_L = \sqrt{3} I_{ph} \quad (\text{Line current lags phase current by } 30^\circ)$$

In both star and delta balanced systems, total 3-phase active power is identically:
$$P = 3 V_{ph} I_{ph} \cos\phi = \sqrt{3} V_L I_L \cos\phi \quad \text{Watts}$$
Total reactive power: $Q = \sqrt{3} V_L I_L \sin\phi \quad \text{VAR}$.
Total apparent power: $S = \sqrt{3} V_L I_L \quad \text{VA}$.

3. Two-Wattmeter Method for Power Measurement:
Blondel's Theorem states that the power supplied to an $N$-wire system can be measured using $(N-1)$ wattmeters. For a 3-phase, 3-wire system (whether star or delta, balanced or unbalanced, with or without neutral), exactly $3 - 1 = 2$ wattmeters are sufficient.

Circuit Connection:
- Current Coil of Wattmeter 1 ($W_1$) is inserted in line $R$; its Pressure (Voltage) Coil is connected between line $R$ and common line $Y$.
- Current Coil of Wattmeter 2 ($W_2$) is inserted in line $B$; its Pressure Coil is connected between line $B$ and common line $Y$.
- Line $Y$ acts as the common voltage reference point.

Mathematical Derivation for Balanced Star Load:
Let the balanced load have an impedance of $\mathbf{Z} = Z \angle \phi$ per phase (lagging power factor angle $\phi$).
Phase voltages with reference to neutral $N$:
$$\mathbf{V}_{RN} = V_{ph} \angle 0^\circ, \quad \mathbf{V}_{YN} = V_{ph} \angle -120^\circ, \quad \mathbf{V}_{BN} = V_{ph} \angle -240^\circ = V_{ph} \angle +120^\circ$$
Phase and line currents (lagging respective phase voltages by $\phi$):
$$\mathbf{I}_R = I_{ph} \angle -\phi, \quad \mathbf{I}_Y = I_{ph} \angle (-120^\circ - \phi), \quad \mathbf{I}_B = I_{ph} \angle (+120^\circ - \phi)$$

Wattmeter 1 Reading ($W_1$):
Wattmeter 1 responds to the current through its current coil ($\mathbf{I}_R$) and the voltage across its pressure coil ($\mathbf{V}_{RY}$):
$$\mathbf{V}_{RY} = \mathbf{V}_{RN} - \mathbf{V}_{YN} = \sqrt{3} V_{ph} \angle 30^\circ = V_L \angle 30^\circ$$
The phase angle between $\mathbf{V}_{RY}$ and $\mathbf{I}_R$ is:
$$\theta_1 = \angle \mathbf{V}_{RY} - \angle \mathbf{I}_R = 30^\circ - (-\phi) = 30^\circ + \phi \quad \text{(or } 30^\circ - \phi \text{ depending on convention)}$$
By standard phasor geometry, $\mathbf{I}_R$ lags $\mathbf{V}_{RN}$ by $\phi$, while $\mathbf{V}_{RY}$ leads $\mathbf{V}_{RN}$ by $30^\circ$. Hence, the angle between $\mathbf{V}_{RY}$ and $\mathbf{I}_R$ is $(30^\circ - \phi)$.
$$W_1 = |\mathbf{V}_{RY}| |\mathbf{I}_R| \cos(30^\circ - \phi) = V_L I_L \cos(30^\circ - \phi)$$

Wattmeter 2 Reading ($W_2$):
Wattmeter 2 responds to current $\mathbf{I}_B$ and voltage $\mathbf{V}_{BY}$:
$$\mathbf{V}_{BY} = \mathbf{V}_{BN} - \mathbf{V}_{YN} = \sqrt{3} V_{ph} \angle 90^\circ = V_L \angle 90^\circ$$
Current $\mathbf{I}_B = I_L \angle (120^\circ - \phi)$.
The phase angle between $\mathbf{V}_{BY}$ and $\mathbf{I}_B$ is:
$$\theta_2 = (120^\circ - \phi) - 90^\circ = 30^\circ - \phi \quad \implies \angle(\mathbf{V}_{BY}, \mathbf{I}_B) = 30^\circ + \phi$$
$$W_2 = |\mathbf{V}_{BY}| |\mathbf{I}_B| \cos(30^\circ + \phi) = V_L I_L \cos(30^\circ + \phi)$$

Sum of Wattmeter Readings:
$$W_1 + W_2 = V_L I_L \left[ \cos(30^\circ - \phi) + \cos(30^\circ + \phi) \right]$$
Using trigonometric identity $\cos(A - B) + \cos(A + B) = 2 \cos A \cos B$:
$$W_1 + W_2 = V_L I_L \left[ 2 \cos 30^\circ \cos\phi \right] = V_L I_L \left[ 2 \cdot \frac{\sqrt{3}}{2} \cos\phi \right] = \sqrt{3} V_L I_L \cos\phi = P_{\text{total}}$$
Thus, the algebraic sum of the two wattmeter readings directly measures the total 3-phase active power under all conditions.

Difference of Wattmeter Readings:
$$W_1 - W_2 = V_L I_L \left[ \cos(30^\circ - \phi) - \cos(30^\circ + \phi) \right]$$
Using $\cos(A - B) - \cos(A + B) = 2 \sin A \sin B$:
$$W_1 - W_2 = V_L I_L \left[ 2 \sin 30^\circ \sin\phi \right] = V_L I_L \left[ 2 \cdot \frac{1}{2} \sin\phi \right] = V_L I_L \sin\phi$$
Multiplying by $\sqrt{3}$:
$$\sqrt{3}(W_1 - W_2) = \sqrt{3} V_L I_L \sin\phi = Q_{\text{total}} \quad \text{(Total Reactive Power)}$$

Determination of Load Power Factor:
Dividing the difference equation by the sum equation:
$$\frac{\sqrt{3}(W_1 - W_2)}{W_1 + W_2} = \frac{\sqrt{3} V_L I_L \sin\phi}{\sqrt{3} V_L I_L \cos\phi} = \tan\phi$$
$$\phi = \tan^{-1}\left( \sqrt{3} \frac{W_1 - W_2}{W_1 + W_2} \right)$$
$$\text{Power Factor } = \cos\phi = \cos\left( \tan^{-1}\left( \sqrt{3} \frac{W_1 - W_2}{W_1 + W_2} \right) \right) = \frac{1}{\sqrt{1 + 3 \left( \frac{W_1 - W_2}{W_1 + W_2} \right)^2}}$$

Effect of Power Factor on Wattmeter Readings:
1. Unity Power Factor ($\cos\phi = 1, \phi = 0^\circ$):
   $W_1 = V_L I_L \cos 30^\circ = \frac{\sqrt{3}}{2} V_L I_L$; $W_2 = V_L I_L \cos 30^\circ = \frac{\sqrt{3}}{2} V_L I_L$.
   Both wattmeters read positive and equal values ($W_1 = W_2$).
2. Power Factor $0.5$ Lagging ($\phi = 60^\circ$):
   $W_1 = V_L I_L \cos(30^\circ - 60^\circ) = V_L I_L \cos(-30^\circ) = \frac{\sqrt{3}}{2} V_L I_L$.
   $W_2 = V_L I_L \cos(30^\circ + 60^\circ) = V_L I_L \cos 90^\circ = 0$.
   One wattmeter reads total power while the second wattmeter reads zero.
3. Power Factor $< 0.5$ Lagging ($60^\circ < \phi \le 90^\circ$):
   $W_1 > 0$, while $\cos(30^\circ + \phi) < 0 \implies W_2 < 0$.
   Wattmeter 2 pointer deflects backwards (downscale). To read $W_2$, the pressure coil or current coil connections must be reversed, and the reading recorded as a negative quantity: $P = W_1 - W_2$.
4. Zero Power Factor Purely Inductive ($\phi = 90^\circ$):
   $W_1 = V_L I_L \cos(-60^\circ) = \frac{1}{2} V_L I_L$; $W_2 = V_L I_L \cos(120^\circ) = -\frac{1}{2} V_L I_L$.
   $W_1 = -W_2$, so total active power $W_1 + W_2 = 0$.
"""
            },
            {
                "qid": "comp-q5",
                "marks": 7,
                "type": "Descriptive",
                "title": "Electromagnetic Field Theory: Maxwell's Equations, Wave Equation, and Poynting Vector",
                "yt_query": "maxwells four equations differential integral form wave equation poynting vector",
                "img_path": "images/comp/maxwell_poynting_wave.png",
                "img_caption": "Figure 1.5: Electromagnetic Wave Propagation Geometry Showing Orthogonal E, H Fields and Poynting Vector S",
                "answer": r"""
Maxwell's equations represent the unification of electricity and magnetism into a single coherent classical electrodynamic theory. James Clerk Maxwell synthesized the empirical laws discovered by Gauss, Ampère, and Faraday, introducing the pivotal displacement current concept to satisfy charge conservation under time-varying conditions.

1. Maxwell's Four Equations in Differential and Integral Forms:

Equation I: Gauss's Law for Electrostatics:
- Physical Principle: The total electric flux emanating from any closed surface is proportional to the total net electric charge enclosed within that volume.
- Differential (Point) Form:
$$\nabla \cdot \mathbf{D} = \rho_v$$
where $\mathbf{D} = \varepsilon \mathbf{E}$ is the electric flux density ($\text{C/m}^2$), $\mathbf{E}$ is electric field intensity ($\text{V/m}$), and $\rho_v$ is volume charge density ($\text{C/m}^3$).
- Integral Form (applying Gauss's Divergence Theorem):
$$\oint_S \mathbf{D} \cdot d\mathbf{S} = \int_V \rho_v dV = Q_{\text{enclosed}}$$

Equation II: Gauss's Law for Magnetostatics:
- Physical Principle: Isolated magnetic charges (magnetic monopoles) do not exist in nature; magnetic field lines form continuous closed loops without sources or sinks.
- Differential (Point) Form:
$$\nabla \cdot \mathbf{B} = 0$$
where $\mathbf{B} = \mu \mathbf{H}$ is the magnetic flux density ($\text{Tesla}$ or $\text{Wb/m}^2$).
- Integral Form:
$$\oint_S \mathbf{B} \cdot d\mathbf{S} = 0$$

Equation III: Faraday's Law of Electromagnetic Induction:
- Physical Principle: A time-varying magnetic field induces an electromotive force (spatially circulating electric field) that opposes the flux change (Lenz's Law).
- Differential (Point) Form:
$$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$$
- Integral Form (applying Stokes' Theorem):
$$\oint_C \mathbf{E} \cdot d\mathbf{l} = -\frac{d}{dt}\int_S \mathbf{B} \cdot d\mathbf{S} = -\frac{d\Phi_m}{dt}$$

Equation IV: Ampère-Maxwell Circuital Law & Displacement Current:
- Classical Ampère's law stated $\nabla \times \mathbf{H} = \mathbf{J}_c$. Taking the divergence of both sides yields $\nabla \cdot (\nabla \times \mathbf{H}) \equiv 0$, which implies $\nabla \cdot \mathbf{J}_c = 0$. However, the fundamental continuity equation governing conservation of electric charge requires:
$$\nabla \cdot \mathbf{J}_c = -\frac{\partial \rho_v}{\partial t}$$
Using Gauss's law $\rho_v = \nabla \cdot \mathbf{D}$, this becomes:
$$\nabla \cdot \mathbf{J}_c = -\frac{\partial}{\partial t}(\nabla \cdot \mathbf{D}) = -\nabla \cdot \left( \frac{\partial \mathbf{D}}{\partial t} \right) \implies \nabla \cdot \left( \mathbf{J}_c + \frac{\partial \mathbf{D}}{\partial t} \right) = 0$$
Maxwell recognized that time-varying electric fields produce an equivalent current density, termed the Displacement Current Density:
$$\mathbf{J}_d = \frac{\partial \mathbf{D}}{\partial t} = \varepsilon \frac{\partial \mathbf{E}}{\partial t}$$
- Differential (Point) Form of Ampère-Maxwell Law:
$$\nabla \times \mathbf{H} = \mathbf{J}_c + \frac{\partial \mathbf{D}}{\partial t}$$
- Integral Form:
$$\oint_C \mathbf{H} \cdot d\mathbf{l} = \int_S \left( \mathbf{J}_c + \frac{\partial \mathbf{D}}{\partial t} \right) \cdot d\mathbf{S} = I_c + I_d$$

2. Derivation of the Electromagnetic Wave Equation in a Source-Free Lossless Medium:
In a source-free ($\rho_v = 0, \mathbf{J}_c = 0$), linear, isotropic, homogeneous, and lossless dielectric medium ($\varepsilon, \mu = \text{constant}, \sigma = 0$):
$$\nabla \cdot \mathbf{E} = 0, \quad \nabla \cdot \mathbf{H} = 0, \quad \nabla \times \mathbf{E} = -\mu \frac{\partial \mathbf{H}}{\partial t}, \quad \nabla \times \mathbf{H} = \varepsilon \frac{\partial \mathbf{E}}{\partial t}$$
Taking the curl of both sides of Faraday's law:
$$\nabla \times (\nabla \times \mathbf{E}) = \nabla \times \left( -\mu \frac{\partial \mathbf{H}}{\partial t} \right) = -\mu \frac{\partial}{\partial t}(\nabla \times \mathbf{H})$$
Using the vector identity $\nabla \times (\nabla \times \mathbf{A}) \equiv \nabla(\nabla \cdot \mathbf{A}) - \nabla^2 \mathbf{A}$:
$$\nabla(\nabla \cdot \mathbf{E}) - \nabla^2 \mathbf{E} = -\mu \frac{\partial}{\partial t}\left( \varepsilon \frac{\partial \mathbf{E}}{\partial t} \right)$$
Since $\nabla \cdot \mathbf{E} = 0$:
$$-\nabla^2 \mathbf{E} = -\mu \varepsilon \frac{\partial^2 \mathbf{E}}{\partial t^2} \implies \nabla^2 \mathbf{E} = \mu \varepsilon \frac{\partial^2 \mathbf{E}}{\partial t^2}$$
Similarly, taking the curl of the Ampère-Maxwell equation yields the magnetic wave equation:
$$\nabla^2 \mathbf{H} = \mu \varepsilon \frac{\partial^2 \mathbf{H}}{\partial t^2}$$
These are standard three-dimensional wave equations of the form $\nabla^2 \psi = \frac{1}{v^2}\frac{\partial^2 \psi}{\partial t^2}$. The propagation velocity of the electromagnetic wave is:
$$v = \frac{1}{\sqrt{\mu \varepsilon}}$$
In free space ($\mu_0 = 4\pi \times 10^{-7}\text{ H/m}, \varepsilon_0 \approx 8.854 \times 10^{-12}\text{ F/m}$):
$$c = \frac{1}{\sqrt{\mu_0 \varepsilon_0}} \approx 3 \times 10^8 \text{ m/s}$$
The ratio of electric to magnetic field amplitudes defines the Intrinsic (Wave) Impedance $\eta$:
$$\eta = \frac{|\mathbf{E}|}{|\mathbf{H}|} = \sqrt{\frac{\mu}{\varepsilon}} \quad \implies \quad \eta_0 = \sqrt{\frac{\mu_0}{\varepsilon_0}} \approx 120\pi \approx 377\,\Omega \text{ (Free space)}$$

3. Poynting's Theorem and the Poynting Vector:
Poynting's Theorem is the mathematical statement of the conservation of electromagnetic energy.
Using the vector identity $\nabla \cdot (\mathbf{E} \times \mathbf{H}) = \mathbf{H} \cdot (\nabla \times \mathbf{E}) - \mathbf{E} \cdot (\nabla \times \mathbf{H})$:
$$\nabla \cdot (\mathbf{E} \times \mathbf{H}) = \mathbf{H} \cdot \left( -\frac{\partial \mathbf{B}}{\partial t} \right) - \mathbf{E} \cdot \left( \mathbf{J}_c + \frac{\partial \mathbf{D}}{\partial t} \right)$$
Using $\mathbf{B} = \mu \mathbf{H}$ and $\mathbf{D} = \varepsilon \mathbf{E}$:
$$\mathbf{H} \cdot \frac{\partial \mathbf{B}}{\partial t} = \frac{\partial}{\partial t}\left( \frac{1}{2}\mu H^2 \right), \quad \mathbf{E} \cdot \frac{\partial \mathbf{D}}{\partial t} = \frac{\partial}{\partial t}\left( \frac{1}{2}\varepsilon E^2 \right)$$
$$\nabla \cdot (\mathbf{E} \times \mathbf{H}) = -\mathbf{J}_c \cdot \mathbf{E} - \frac{\partial}{\partial t}\left( \frac{1}{2}\varepsilon E^2 + \frac{1}{2}\mu H^2 \right)$$
Integrating over an arbitrary closed volume $V$ bounded by surface $S$ and applying the Divergence Theorem:
$$\oint_S (\mathbf{E} \times \mathbf{H}) \cdot d\mathbf{S} = -\int_V (\mathbf{J}_c \cdot \mathbf{E}) dV - \frac{\partial}{\partial t}\int_V \left( \frac{1}{2}\varepsilon E^2 + \frac{1}{2}\mu H^2 \right) dV$$

The Poynting Vector $\mathbf{S}$ represents the instantaneous power flux density ($\text{W/m}^2$) carried by the electromagnetic field:
$$\mathbf{S} = \mathbf{E} \times \mathbf{H}$$
Physical Interpretation of Poynting's Theorem:
- Left-hand term $\oint_S \mathbf{S} \cdot d\mathbf{S}$: Total rate of electromagnetic power escaping outward through bounding surface $S$.
- First term on right $-\int_V (\mathbf{J}_c \cdot \mathbf{E}) dV$: Ohmic power dissipated within the volume as heat (Joule heating).
- Second term $-\frac{\partial}{\partial t}\int_V w_{em} dV$: Rate of decrease of the stored electric and magnetic energy within volume $V$.
For time-harmonic sinusoidal fields, the Time-Average Poynting Vector is:
$$\mathbf{S}_{avg} = \frac{1}{2}\text{Re}\left[ \mathbf{E} \times \mathbf{H}^* \right] \quad \text{W/m}^2$$
"""
            }
        ]
    },
    {
        "module_id": "comp-m2",
        "module_num": "Module 2",
        "module_title": "Electrical Machines & Power Systems",
        "questions": [
            {
                "qid": "comp-q6",
                "marks": 7,
                "type": "Analytical",
                "title": "DC Machines: EMF & Torque Equations, Armature Reaction, Commutation, and Speed Control",
                "yt_query": "dc machine emf torque equation armature reaction commutation speed control",
                "img_path": "images/comp/dc_machine_characteristics.png",
                "img_caption": "Figure 2.1: DC Machine Armature Reaction Flux Distortion and Speed-Torque Characteristics Under Various Control Methods",
                "answer": r"""
Direct Current (DC) machines operate on the fundamental principles of electromagnetic induction (Faraday's law) and electromagnetic Lorentz force ($d\mathbf{F} = I\,d\mathbf{l} \times \mathbf{B}$).

1. Derivation of Generated EMF Equation:
Let:
- $P$ = Number of field poles
- $\Phi$ = Useful magnetic flux per pole in Webers ($\text{Wb}$)
- $Z$ = Total number of active armature conductors
- $N$ = Armature rotational speed in revolutions per minute ($\text{rpm}$)
- $A$ = Number of parallel armature paths ($A = 2$ for wave winding; $A = P$ for lap winding)

In one complete revolution ($1 \text{ rev}$), each conductor cuts the flux of all $P$ poles:
$$\Delta\Phi = P \cdot \Phi \quad \text{Webers}$$
The time taken for one complete revolution is:
$$\Delta t = \frac{60}{N} \quad \text{seconds}$$
According to Faraday's law of electromagnetic induction, the average electromotive force (EMF) induced in a single conductor is:
$$e_{avg} = \frac{\Delta\Phi}{\Delta t} = \frac{P \Phi}{60 / N} = \frac{P \Phi N}{60} \quad \text{Volts}$$
Since the total $Z$ conductors are divided equally into $A$ parallel paths, the number of conductors connected in series per path is $Z / A$.
The total generated EMF (or back EMF $E_b$ in a motor) is the sum of EMFs across conductors in one parallel path:
$$E = \left( \frac{Z}{A} \right) e_{avg} = \frac{P \Phi Z N}{60 A} \quad \text{Volts}$$
Alternatively, in terms of angular mechanical velocity $\omega_m = \frac{2\pi N}{60} \text{ rad/s}$:
$$E = \left( \frac{P Z}{2\pi A} \right) \Phi \omega_m = K_a \Phi \omega_m \quad \text{where } K_a = \frac{P Z}{2\pi A}$$

2. Derivation of Electromagnetic Torque Equation:
The gross electromagnetic power developed in the armature is equal to the mechanical power converted:
$$P_{em} = E_b I_a = T_e \omega_m$$
where $I_a$ is total armature current and $T_e$ is developed electromagnetic torque ($\text{N}\cdot\text{m}$).
Substituting $E_b = K_a \Phi \omega_m$:
$$(K_a \Phi \omega_m) I_a = T_e \omega_m \implies T_e = K_a \Phi I_a$$
$$T_e = \frac{1}{2\pi} \left( \frac{P Z}{A} \right) \Phi I_a = 0.159 \left( \frac{P Z}{A} \right) \Phi I_a \quad \text{N}\cdot\text{m}$$
Torque is directly proportional to both air-gap flux per pole $\Phi$ and armature current $I_a$.

3. Armature Reaction:
Armature reaction is the magnetic effect produced by the armature MMF on the main field magnetic flux distribution in the machine air-gap.
- On No-Load: Only the main field MMF exists, directed along the direct axis ($d$-axis). The flux is symmetrically distributed, and the Magnetic Neutral Axis (MNA)—where no EMF is induced in conductors—coincides exactly with the Geometrical Neutral Axis (GNA).
- On Load: Armature current establishes a cross-magnetizing MMF along the quadrature axis ($q$-axis), perpendicular to the main field.
- Resultant Effects:
  1. Distortion of Air-Gap Flux: The resultant flux is shifted in the direction of rotation for a generator, and against rotation for a motor. The MNA shifts by a mechanical angle $\theta_m$.
  2. Demagnetizing Effect: Due to magnetic saturation in the trailing pole tips (generator) or leading pole tips (motor), the flux increase in the saturated tip is less than the flux decrease in the weakened tip, leading to a net reduction in useful pole flux $\Phi$ ($1-5\%$), reducing generated voltage or increasing motor speed.

Analytical Expressions for Ampere-Turns:
Let $I_c = I_a / A$ be the current per conductor. For an MNA brush lead of $\theta_m$ mechanical degrees:
- Demagnetizing Ampere-Turns per Pole:
$$AT_d = Z I_c \left( \frac{2 \theta_m}{360^\circ} \right) = \frac{Z I_a}{A} \left( \frac{\theta_m}{180^\circ} \right) \quad \implies \quad AT_d = \frac{Z I_a}{2 A P} \left( \frac{2\theta_e}{180^\circ} \right)$$
- Cross-Magnetizing Ampere-Turns per Pole:
$$AT_c = \frac{Z I_a}{2 A P} \left( 1 - \frac{2\theta_e}{180^\circ} \right)$$

4. Commutation and Mitigation:
Commutation is the process by which current in an armature coil is reversed from $+I_c$ to $-I_c$ as the commutator segments connected to the coil pass under a brush during commutation time $T_c$.
Because the coil possesses self-inductance $L_c$, the rapid current reversal induces a self-induced Reactance Voltage:
$$e_r = L_c \frac{di}{dt} \approx 2 L_c \frac{I_c}{T_c}$$
According to Lenz's law, $e_r$ opposes current reversal, resulting in delayed (under-) commutation, which produces destructive sparking at the trailing edge of the brush.
Methods to Ensure Sparkless Commutation:
- Interpoles (Compoles): Small narrow auxiliary poles placed on the GNA between main poles, wound with heavy conductors carrying full armature current $I_a$. They induce a commutating EMF $e_c$ equal and opposite to the reactance voltage ($e_c = -e_r$), neutralizing cross-magnetizing MMF at the neutral zone.
- Compensating Windings: Conductors embedded in axial slots in the main pole faces carrying current in the reverse direction of adjacent armature conductors, neutralizing cross-magnetizing armature MMF directly beneath pole shoes.

5. Speed Control Methods of DC Motors:
From the fundamental voltage equation $V = E_b + I_a R_a = K_a \Phi \omega_m + I_a R_a$:
$$N = \frac{V - I_a R_a}{K' \Phi}$$
- Armature Resistance Control (Rheostatic Control): Adding variable resistance $R_{ext}$ in series with the armature drops voltage, lowering speed below base speed. Disadvantage: high $I_a^2 R_{ext}$ power dissipation, poor efficiency, and poor speed regulation.
- Field Flux Control: Inserting variable resistance in the shunt field circuit reduces field current $I_f$, decreasing $\Phi$ and increasing speed above base speed (constant power drive).
- Armature Voltage Control (Ward-Leonard System): Feeding the DC motor armature from a dedicated motor-generator set or controlled thyristor rectifier allows continuous adjustment of $V_a$ from 0 to rated voltage, providing smooth speed control from zero to base speed in both directions (four-quadrant operation) with high efficiency.
"""
            },
            {
                "qid": "comp-q7",
                "marks": 7,
                "type": "Analytical",
                "title": "Testing of DC Machines: Swinburne's Test and Hopkinson's Regenerative Test",
                "yt_query": "swinburnes test hopkinsons test dc machine efficiency derivation",
                "img_path": "images/comp/dc_testing_hopkinson.png",
                "img_caption": "Figure 2.2: Circuit Connections for (a) Swinburne's No-Load Test and (b) Hopkinson's Regenerative Back-to-Back Test",
                "answer": r"""
Testing of DC machines is necessary to verify performance guarantees, compute losses, predetermine efficiency across operating load cycles, and assess thermal temperature rise. Tests are classified into indirect no-load methods (Swinburne's test) and regenerative back-to-back load methods (Hopkinson's test).

1. Swinburne's Test (No-Load Indirect Method):
Swinburne's test is an indirect method conducted on a DC shunt machine operated as an unloaded motor at rated voltage and rated speed.

Test Procedure & Loss Determination:
The machine is connected to rated supply voltage $V$. The no-load line current $I_{0}$ and shunt field current $I_{sh}$ are recorded.
Armature no-load current is:
$$I_{a0} = I_0 - I_{sh}$$
No-load total power drawn from supply is:
$$P_{in,0} = V I_0$$
This input power supplies the no-load armature copper loss, the shunt field copper loss, and all rotational losses (iron loss and mechanical friction/windage loss):
$$V I_0 = I_{a0}^2 R_a + V I_{sh} + W_{rotational}$$
The Constant Losses $W_c$ of the machine (combining core iron losses, friction, windage, and shunt field copper loss $V I_{sh}$) are:
$$W_c = V I_0 - I_{a0}^2 R_a$$
Since core flux $\Phi$ and speed $N$ remain substantially constant from no-load to full-load in a DC shunt machine, $W_c$ is treated as constant at all loads.

Predetermination of Efficiency at any Arbitrary Load Current $I$:
Let $I$ be the line current at which efficiency is to be evaluated.
Armature resistance $R_a$ is measured and hot-corrected to $75^\circ\text{C}$ ($R_{a,hot} \approx 1.2 R_{a,dc}$).

Case A: Machine Operating as a Motor:
- Armature current: $I_a = I - I_{sh}$
- Armature copper loss: $P_{cu,a} = I_a^2 R_a$
- Total losses: $W_{total} = W_c + I_a^2 R_a$
- Electrical input power: $P_{in} = V I$
- Mechanical output power: $P_{out} = P_{in} - W_{total} = V I - (W_c + I_a^2 R_a)$
- Efficiency as a motor:
$$\eta_m = \frac{P_{out}}{P_{in}} \times 100\% = \frac{V I - W_c - (I - I_{sh})^2 R_a}{V I} \times 100\%$$

Case B: Machine Operating as a Generator:
- Armature current: $I_a = I + I_{sh}$
- Armature copper loss: $P_{cu,a} = I_a^2 R_a$
- Total losses: $W_{total} = W_c + I_a^2 R_a$
- Electrical output power: $P_{out} = V I$
- Mechanical input power: $P_{in} = P_{out} + W_{total} = V I + W_c + (I + I_{sh})^2 R_a$
- Efficiency as a generator:
$$\eta_g = \frac{P_{out}}{P_{in}} \times 100\% = \frac{V I}{V I + W_c + (I + I_{sh})^2 R_a} \times 100\%$$

Advantages and Disadvantages of Swinburne's Test:
- Advantages: Extremely economical; power consumed is only the no-load losses ($< 5\%$ of rated power); efficiency can be predetermined for any load fraction without physical loading.
- Disadvantages: Cannot be applied to DC series motors (which run dangerously overspeed at no-load); iron loss is assumed constant, ignoring armature reaction flux distortion; does not verify commutation quality under load or assess full-load temperature rise.

2. Hopkinson's Test (Regenerative / Back-to-Back Test):
Hopkinson's test overcomes the limitations of Swinburne's test by loading two identical DC shunt machines to full load while drawing only the net losses from the DC supply mains.

Circuit Arrangement and Operating Principle:
Two identical DC shunt machines are mechanically coupled through a shaft and electrically paralleled across the DC mains.
- Starting: Machine 1 is started as a DC shunt motor from supply mains $V$. Machine 2 runs coupled as an unloaded generator.
- Paralleling (Synchronization): The field rheostat of Machine 2 is adjusted until its open-circuit armature voltage $E_2$ equals the supply mains voltage $V$, verified by a zero reading on a voltmeter bridged across the paralleling switch $S$. Switch $S$ is then closed.
- Loading by Field Control: The field excitation of Machine 2 is increased, raising its induced EMF $E_2 > V$. Machine 2 begins delivering current into the common bus, acting as a generator. Simultaneously, the field excitation of Machine 1 is slightly weakened ($E_1 < V$), causing it to draw higher current from the bus and act as a motor driving Generator 2.

Mathematical Formulation of Losses and Separate Efficiencies:
Let:
- $V$ = Supply mains voltage
- $I_1$ = Current supplied by mains
- $I_2$ = Current delivered by Generator 2 to the common bus
- $I_{m} = I_1 + I_2$ = Total armature current drawn by Motor 1
- $I_{f1}, I_{f2}$ = Shunt field currents of Motor 1 and Generator 2
- $R_a$ = Armature resistance of each machine

Power drawn from mains supplies the net total losses of both machines:
$$P_{in,mains} = V I_1 = \text{Total Losses of Both Machines}$$
Field copper losses:
$$P_{f1} = V I_{f1}, \quad P_{f2} = V I_{f2}$$
Armature copper losses:
$$P_{cu,m} = I_m^2 R_a = (I_1 + I_2)^2 R_a$$
$$P_{cu,g} = I_2^2 R_a$$
The combined stray rotational losses (iron, friction, windage) of both machines are:
$$W_{stray,total} = V I_1 - \left[ (I_1 + I_2)^2 R_a + I_2^2 R_a + V I_{f1} + V I_{f2} \right]$$
Assuming identical mechanical and magnetic construction, the stray loss per machine is:
$$W_{stray} = \frac{W_{stray,total}}{2}$$

Efficiency Calculation:
1. Generator Efficiency ($\eta_g$):
- Electrical output: $P_{out,g} = V I_2$
- Generator total losses: $W_{loss,g} = I_2^2 R_a + V I_{f2} + W_{stray}$
$$\eta_g = \frac{V I_2}{V I_2 + I_2^2 R_a + V I_{f2} + W_{stray}} \times 100\%$$

2. Motor Efficiency ($\eta_m$):
- Electrical input: $P_{in,m} = V (I_m + I_{f1}) = V (I_1 + I_2 + I_{f1})$
- Motor total losses: $W_{loss,m} = (I_1 + I_2)^2 R_a + V I_{f1} + W_{stray}$
$$\eta_m = \frac{P_{in,m} - W_{loss,m}}{P_{in,m}} \times 100\% = 1 - \frac{(I_1 + I_2)^2 R_a + V I_{f1} + W_{stray}}{V (I_1 + I_2 + I_{f1})}$$

Advantages of Hopkinson's Test:
- Both machines run under actual full-load electrical, magnetic, and thermal conditions.
- Commutation spark behavior and temperature rise can be accurately monitored over prolonged runs.
- Power drawn from the grid is strictly equal to the machine losses ($< 10-15\%$ of machine rating), making full-load testing of massive megawatt-scale DC machines feasible in industrial testbeds.
"""
            },
            {
                "qid": "comp-q8",
                "marks": 7,
                "type": "Derivation",
                "title": "Transformers: Equivalent Circuit, Regulation, OC/SC Tests, and Autotransformer Copper Saving",
                "yt_query": "transformer equivalent circuit voltage regulation oc sc test autotransformer copper saving",
                "img_path": "images/comp/transformer_equivalent_circuit.png",
                "img_caption": "Figure 2.3: Transformer Exact Equivalent Circuit Referred to Primary and Phasor Diagram for Lagging Power Factor",
                "answer": r"""
The practical transformer differs from an ideal transformer due to finite winding resistances ($R_1, R_2$), leakage magnetic flux giving rise to leakage reactances ($X_1, X_2$), finite core permeability requiring magnetizing current ($I_m$), and core hysteresis/eddy-current losses modeled by core-loss resistance ($R_c$).

1. Exact and Approximate Equivalent Circuits:
Referred to primary winding:
- Transformation ratio: $k = \frac{V_2}{V_1} = \frac{N_2}{N_1} = \frac{I_1'}{I_2}$
- Secondary winding resistance referred to primary: $R_2' = \frac{R_2}{k^2}$
- Secondary leakage reactance referred to primary: $X_2' = \frac{X_2}{k^2}$
- Equivalent total resistance referred to primary: $R_{01} = R_1 + R_2' = R_1 + \frac{R_2}{k^2}$
- Equivalent total leakage reactance referred to primary: $X_{01} = X_1 + X_2' = X_1 + \frac{X_2}{k^2}$
- Excitation shunt branch: Core resistance $R_c$ (accounting for eddy and hysteresis losses) in parallel with magnetizing reactance $X_m$ (accounting for sinusoidal core flux production), connected across primary voltage $V_1$:
$$\mathbf{I}_0 = \mathbf{I}_c + \mathbf{I}_m, \quad I_c = I_0 \cos\phi_0, \quad I_m = I_0 \sin\phi_0$$
$$R_c = \frac{V_1}{I_c} = \frac{V_1}{I_0 \cos\phi_0}, \quad X_m = \frac{V_1}{I_m} = \frac{V_1}{I_0 \sin\phi_0}$$

2. Open-Circuit (OC) and Short-Circuit (SC) Tests:
- Open-Circuit (OC) Test (determines shunt core parameters $R_c, X_m$ and iron loss $P_i$):
  - Conducted on the Low Voltage (LV) side with the High Voltage (HV) side left open-circuited.
  - Rated voltage $V_1$ at rated frequency is applied. Instruments measure $V_0, I_0, W_0$.
  - Since secondary is open, $I_0 \approx 2-5\%$ of full-load current; series winding copper losses ($I_0^2 R_1$) are negligible.
  - Core loss: $P_i = W_0$.
  - No-load power factor: $\cos\phi_0 = \frac{W_0}{V_0 I_0}$.
  - Shunt parameters: $I_c = I_0 \cos\phi_0$, $I_m = I_0 \sin\phi_0 = \sqrt{I_0^2 - I_c^2}$, $R_c = \frac{V_0}{I_c}$, $X_m = \frac{V_0}{I_m}$.
- Short-Circuit (SC) Test (determines series parameters $R_{01}, X_{01}, Z_{01}$ and full-load copper loss $P_{cu}$):
  - Conducted on the High Voltage (HV) side with the Low Voltage (LV) terminals solidly short-circuited.
  - A reduced voltage $V_{sc}$ ($5-10\%$ of rated voltage) is applied to circulate rated full-load current $I_{sc} = I_{1,fl}$.
  - Since applied voltage is very low, core flux $\Phi \propto V_{sc}$ is small, making iron losses completely negligible.
  - Full-load copper loss: $P_{cu,fl} = W_{sc}$.
  - Equivalent parameters referred to HV side:
  $$Z_{01} = \frac{V_{sc}}{I_{sc}}, \quad R_{01} = \frac{W_{sc}}{I_{sc}^2}, \quad X_{01} = \sqrt{Z_{01}^2 - R_{01}^2}$$

3. Voltage Regulation Derivation:
Voltage regulation is the fractional change in secondary terminal voltage from no-load to full-load at a given power factor:
$$\%VR = \frac{V_2^{NL} - V_2^{FL}}{V_2^{FL}} \times 100\% = \frac{E_2 - V_2}{V_2} \times 100\%$$
Referring all quantities to secondary winding:
$$\mathbf{E}_2 = \mathbf{V}_2 + \mathbf{I}_2 (R_{02} + jX_{02}) = V_2 \angle 0^\circ + (I_2 \cos\phi_2 \mp j I_2 \sin\phi_2)(R_{02} + jX_{02})$$
Expanding and taking real and imaginary projections:
$$E_2 \approx V_2 + I_2 R_{02} \cos\phi_2 \pm I_2 X_{02} \sin\phi_2$$
where $(+)$ is for lagging power factor and $(-)$ is for leading power factor.
$$\%VR \approx \frac{I_2 R_{02} \cos\phi_2 \pm I_2 X_{02} \sin\phi_2}{V_2} \times 100\%$$
- Condition for Zero Voltage Regulation:
$$I_2 R_{02} \cos\phi_2 - I_2 X_{02} \sin\phi_2 = 0 \implies \tan\phi_2 = \frac{R_{02}}{X_{02}} \quad (\text{Leading PF})$$
- Condition for Maximum Voltage Regulation:
$$\frac{d(VR)}{d\phi_2} = 0 \implies -R_{02}\sin\phi_2 + X_{02}\cos\phi_2 = 0 \implies \tan\phi_2 = \frac{X_{02}}{R_{02}} \quad (\text{Lagging PF})$$

4. Efficiency and Condition for Maximum Efficiency:
At fractional load $x$ ($x = I_2 / I_{2,fl}$):
$$\eta = \frac{x S \cos\phi_2}{x S \cos\phi_2 + P_i + x^2 P_{cu,fl}}$$
Differentiating $\eta$ with respect to load current (or fraction $x$) and setting to zero:
$$\frac{d\eta}{dx} = 0 \implies P_i = x^2 P_{cu,fl} \quad \implies \quad \text{Variable Copper Loss} = \text{Constant Iron Loss}$$
The fractional load corresponding to maximum efficiency is:
$$x_{\eta,\max} = \sqrt{\frac{P_i}{P_{cu,fl}}}$$

5. Autotransformers: Operating Principle & Copper Saving Derivation:
An autotransformer uses a single continuous tapped winding common to both primary and secondary circuits.
Power Transfer Mechanism:
Total apparent power transferred consists of two distinct components:
- Inductively transferred power: $S_{ind} = V_1 (I_1 - I_2) = (1 - k) S_{total}$
- Conductively transferred power: $S_{cond} = k S_{total}$

Derivation of Copper Saving:
The weight (volume) of copper in any winding is proportional to the product of number of turns and current rating ($W_{cu} \propto N \cdot I$):
For a Two-Winding Transformer:
$$W_{2-wdg} \propto N_1 I_1 + N_2 I_2$$
Since $N_1 I_1 \approx N_2 I_2$:
$$W_{2-wdg} \propto 2 N_1 I_1$$

For an Autotransformer (Step-Down, $V_1 > V_2, k = V_2/V_1 < 1$):
- Section $AB$ (uncommon part) has $(N_1 - N_2)$ turns carrying current $I_1$.
- Section $BC$ (common part) has $N_2$ turns carrying current $(I_2 - I_1)$.
$$W_{auto} \propto (N_1 - N_2) I_1 + N_2 (I_2 - I_1)$$
$$W_{auto} \propto N_1 I_1 - N_2 I_1 + N_2 I_2 - N_2 I_1 = N_1 I_1 + N_2 I_2 - 2 N_2 I_1$$
Substituting $N_2 I_2 = N_1 I_1$ and $N_2 = k N_1$:
$$W_{auto} \propto 2 N_1 I_1 - 2 (k N_1) I_1 = 2 N_1 I_1 (1 - k)$$
Dividing $W_{auto}$ by $W_{2-wdg}$:
$$\frac{W_{auto}}{W_{2-wdg}} = \frac{2 N_1 I_1 (1 - k)}{2 N_1 I_1} = 1 - k$$
Copper saved by using an autotransformer:
$$\text{Copper Saved} = W_{2-wdg} - W_{auto} = k \cdot W_{2-wdg}$$
When $k \approx 1$ (e.g., $k = 0.9$ for a 220V/200V autotransformer), $90\%$ of the copper is saved, yielding dramatically lower losses, higher efficiency, and compact volume.
"""
            },
            {
                "qid": "comp-q9",
                "marks": 7,
                "type": "Derivation",
                "title": "Three-Phase Induction Motor: Rotating Field, Torque-Slip Equation, and Starting Methods",
                "yt_query": "three phase induction motor rotating magnetic field torque slip characteristics starting methods",
                "img_path": "images/comp/induction_motor_torque_slip.png",
                "img_caption": "Figure 2.4: Three-Phase Induction Motor Torque-Slip Curve Highlighting Operating Modes and Breakdown Torque",
                "answer": r"""
The three-phase induction motor, often called the workhorse of industrial automation, is a singly excited asynchronous machine wherein rotor currents are established entirely via electromagnetic induction from the stator rotating magnetic field.

1. Proof of Rotating Magnetic Field (RMF):
Consider a symmetrical three-phase stator winding with phase coils spatially displaced from each other by $120^\circ$ electrical around the stator bore. Energizing these windings with balanced sinusoidal three-phase currents:
$$i_R(t) = I_m \sin(\omega t)$$
$$i_Y(t) = I_m \sin(\omega t - 120^\circ)$$
$$i_B(t) = I_m \sin(\omega t - 240^\circ) = I_m \sin(\omega t + 120^\circ)$$
Each phase current establishes an alternating spatial flux along its respective magnetic axis:
$$\Phi_R = \Phi_m \sin(\omega t)$$
$$\Phi_Y = \Phi_m \sin(\omega t - 120^\circ)$$
$$\Phi_B = \Phi_m \sin(\omega t + 120^\circ)$$

Evaluating the resultant flux $\mathbf{\Phi}_r$ at different electrical time instants:
- Instant 1: $\omega t = 0$:
  $\Phi_R = 0$
  $\Phi_Y = \Phi_m \sin(-120^\circ) = -\frac{\sqrt{3}}{2}\Phi_m$
  $\Phi_B = \Phi_m \sin(+120^\circ) = +\frac{\sqrt{3}}{2}\Phi_m$
  Resolving along horizontal and vertical axes:
  $$\Phi_{rx} = \Phi_R - \Phi_Y \cos 60^\circ - \Phi_B \cos 60^\circ = 0 - \left(-\frac{\sqrt{3}}{2}\Phi_m\right)\frac{1}{2} - \left(\frac{\sqrt{3}}{2}\Phi_m\right)\frac{1}{2} = 0$$
  $$\Phi_{ry} = 0 - \Phi_Y \sin 60^\circ + \Phi_B \sin 60^\circ = -\left(-\frac{\sqrt{3}}{2}\Phi_m\right)\frac{\sqrt{3}}{2} + \left(\frac{\sqrt{3}}{2}\Phi_m\right)\frac{\sqrt{3}}{2} = \frac{3}{4}\Phi_m + \frac{3}{4}\Phi_m = \frac{3}{2}\Phi_m$$
  Resultant magnitude:
  $$\Phi_r = \sqrt{\Phi_{rx}^2 + \Phi_{ry}^2} = \frac{3}{2}\Phi_m = 1.5 \Phi_m \quad \text{directed at } 90^\circ$$

- Instant 2: $\omega t = 60^\circ$:
  $\Phi_R = \Phi_m \sin 60^\circ = \frac{\sqrt{3}}{2}\Phi_m$
  $\Phi_Y = \Phi_m \sin(-60^\circ) = -\frac{\sqrt{3}}{2}\Phi_m$
  $\Phi_B = \Phi_m \sin(180^\circ) = 0$
  Computing the resultant:
  $$\Phi_r = 2 \left( \frac{\sqrt{3}}{2}\Phi_m \right) \cos 30^\circ = 2 \left( \frac{\sqrt{3}}{2}\Phi_m \right)\frac{\sqrt{3}}{2} = \frac{3}{2}\Phi_m = 1.5 \Phi_m \quad \text{rotated by } 60^\circ$$

General Mathematical Proof:
Using trigonometric identities for any arbitrary $\omega t$:
$$\Phi_r(\theta, t) = \Phi_m \sin\omega t \cos\theta + \Phi_m \sin(\omega t - 120^\circ)\cos(\theta - 120^\circ) + \Phi_m \sin(\omega t + 120^\circ)\cos(\theta + 120^\circ)$$
Using the product-to-sum identity $\sin A \cos B = \frac{1}{2}[\sin(A - B) + \sin(A + B)]$:
$$\Phi_r(\theta, t) = \frac{3}{2}\Phi_m \sin(\omega t - \theta)$$
This represents a traveling magnetic wave of constant magnitude $1.5 \Phi_m$ revolving uniformly around the air-gap at Synchronous Speed:
$$N_s = \frac{120 f}{P} \quad \text{rpm} \quad \text{or} \quad \omega_s = \frac{4\pi f}{P} \quad \text{rad/s}$$

2. Slip and Rotor Electrical Parameters:
Slip $s$ is the fractional difference between synchronous speed and rotor speed $N$:
$$s = \frac{N_s - N}{N_s} \implies N = N_s (1 - s)$$
- Rotor induced frequency: $f_r = s f$
- Rotor induced EMF at slip $s$: $E_{2s} = s E_2$
- Rotor standstill leakage reactance: $X_2 = 2\pi f L_2$
- Rotor running leakage reactance: $X_{2s} = 2\pi f_r L_2 = s X_2$
- Rotor current per phase:
$$I_2 = \frac{E_{2s}}{\sqrt{R_2^2 + X_{2s}^2}} = \frac{s E_2}{\sqrt{R_2^2 + (s X_2)^2}} = \frac{E_2}{\sqrt{(R_2/s)^2 + X_2^2}}$$
- Rotor power factor: $\cos\phi_2 = \frac{R_2}{\sqrt{R_2^2 + (s X_2)^2}} = \frac{R_2/s}{\sqrt{(R_2/s)^2 + X_2^2}}$

3. Derivation of Electromagnetic Torque Equation:
The total mechanical air-gap power transferred across the stator-rotor boundary for a 3-phase motor is:
$$P_g = 3 I_2^2 \left(\frac{R_2}{s}\right) = 3 \left( \frac{s^2 E_2^2}{R_2^2 + s^2 X_2^2} \right) \frac{R_2}{s} = \frac{3 s E_2^2 R_2}{R_2^2 + s^2 X_2^2}$$
Rotor copper loss: $P_{cu,rotor} = 3 I_2^2 R_2 = s P_g$.
Gross mechanical power developed: $P_{mech} = P_g - P_{cu,rotor} = (1 - s) P_g$.
Electromagnetic torque $T_e$ is air-gap power divided by synchronous mechanical speed:
$$T_e = \frac{P_{mech}}{\omega_m} = \frac{(1 - s) P_g}{(1 - s)\omega_s} = \frac{P_g}{\omega_s}$$
$$T_e = \frac{3}{\omega_s} \cdot \frac{s E_2^2 R_2}{R_2^2 + (s X_2)^2} \quad \text{N}\cdot\text{m}$$

Analysis of Torque-Slip Characteristics:
- Low-Slip Region (Normal Operation, $s \ll 1$):
  Here $(s X_2)^2 \ll R_2^2$, so the reactance term is negligible:
  $$T_e \approx \frac{3}{\omega_s} \frac{s E_2^2}{R_2} \implies T_e \propto s$$
  Torque varies linearly with slip; the motor operates stably with high efficiency.
- High-Slip Region ($s \to 1$, Starting Condition):
  Here $(s X_2)^2 \gg R_2^2$, so resistance is negligible:
  $$T_e \approx \frac{3}{\omega_s} \frac{s E_2^2 R_2}{s^2 X_2^2} = \frac{3 E_2^2 R_2}{\omega_s X_2^2} \cdot \frac{1}{s} \implies T_e \propto \frac{1}{s}$$
  Torque is inversely proportional to slip (unstable region).

Condition for Maximum (Breakdown) Torque ($T_{max}$):
Differentiating $T_e$ with respect to slip $s$ and setting $\frac{dT_e}{ds} = 0$:
$$\frac{d}{ds}\left[ \frac{s}{R_2^2 + s^2 X_2^2} \right] = \frac{(R_2^2 + s^2 X_2^2)\cdot 1 - s(2s X_2^2)}{(R_2^2 + s^2 X_2^2)^2} = 0$$
$$R_2^2 - s^2 X_2^2 = 0 \implies s_{\max} = \frac{R_2}{X_2}$$
Maximum torque occurs at a slip equal to the ratio of rotor resistance to standstill reactance.
Substituting $s_{\max} = R_2 / X_2$ into the torque equation:
$$T_{\max} = \frac{3}{\omega_s} \frac{(R_2 / X_2) E_2^2 R_2}{R_2^2 + (R_2 / X_2)^2 X_2^2} = \frac{3}{\omega_s} \frac{(R_2^2 / X_2) E_2^2}{2 R_2^2}$$
$$T_{\max} = \frac{3}{2 \omega_s} \frac{E_2^2}{X_2}$$
Key Insight: Maximum breakdown torque is completely independent of rotor resistance $R_2$. Adding external resistance to a wound-rotor induction motor shifts the point of maximum torque toward standstill ($s = 1$), enabling maximum torque at starting ($s_{max} = 1$ when $R_2 = X_2$) without diminishing $T_{max}$.

4. Starting Methods of Three-Phase Induction Motors:
Direct-On-Line (DOL) starting draws $5-7$ times rated full-load current ($I_{st} = 5 \text{ to } 7 I_{fl}$), causing unacceptable network voltage sags.
- Star-Delta ($\text{Y}-\Delta$) Starter:
  Windings are connected in Star during starting, then switched to Delta after acceleration ($> 80\% N_s$).
  - Starting phase voltage: $V_{ph,Y} = V_L / \sqrt{3}$
  - Starting line current: $I_{st,Y} = \frac{V_L / \sqrt{3}}{Z_{st}} = \frac{1}{3} \left( \frac{\sqrt{3} V_L}{Z_{st}} \right) = \frac{1}{3} I_{st,\Delta}$
  - Starting torque: $T_{st,Y} = \frac{1}{3} T_{st,\Delta}$
  Both starting current and starting torque are reduced to exactly one-third ($33.3\%$) of their DOL values.
- Auto-Transformer Starter:
  Tappings on an autotransformer supply a fraction $x$ ($x = 0.5, 0.65, 0.8$) of line voltage to the stator:
  - Motor terminal voltage: $V_{st} = x V_L$
  - Motor starting current: $I_{motor} = x I_{sc}$
  - Line starting current drawn from mains: $I_{line} = x \cdot I_{motor} = x^2 I_{sc}$
  - Starting torque: $T_{st} = x^2 T_{sc} = x^2 \left( \frac{I_{sc}}{I_{fl}} \right)^2 s_{fl} T_{fl}$
"""
            },
            {
                "qid": "comp-q10",
                "marks": 7,
                "type": "Derivation",
                "title": "Synchronous Machines: Regulation Methods (EMF/MMF) & Two-Reaction Theory",
                "yt_query": "synchronous machine voltage regulation emf mmf method two reaction theory",
                "img_path": "images/comp/synchronous_machine_phasor.png",
                "img_caption": "Figure 2.5: Blondel Two-Reaction Phasor Diagram for Salient Pole Alternator and Power-Angle Curve",
                "answer": r"""
Synchronous machines are doubly excited AC machines operating strictly at synchronous speed $N_s = 120 f / P$. Their voltage regulation under changing load power factor is a critical stability parameter.

1. Generated EMF Equation & Winding Factors:
For a 3-phase alternator with flux per pole $\Phi$ ($\text{Wb}$), frequency $f$ ($\text{Hz}$), and series turns per phase $T_{ph}$:
$$E_{ph} = 4.44 k_p k_d f \Phi T_{ph} \quad \text{Volts}$$
- Pitch Factor (Chording Factor) $k_p$: Accounts for short-pitching coils by chording angle $\alpha$:
$$k_p = \cos\left( \frac{\alpha}{2} \right)$$
Short pitching eliminates specific harmonic orders (e.g., setting $\alpha = 180^\circ / n$ eliminates the $n$-th harmonic) and reduces end-turn copper volume.
- Distribution (Breadth) Factor $k_d$: Accounts for distributing coils over $m$ slots per pole per phase with slot pitch angle $\beta = 180^\circ / (\text{slots/pole})$:
$$k_d = \frac{\sin(m\beta / 2)}{m \sin(\beta / 2)}$$

2. Voltage Regulation Determination:
Voltage regulation is defined as:
$$\%VR = \frac{|E_{0}| - |V|}{V} \times 100\%$$
where $E_0$ is the no-load open-circuit terminal voltage for the same excitation field current $I_f$ that yields rated terminal voltage $V$ at rated load.

Method A: Synchronous Impedance (EMF) Method:
1. Conduct Open-Circuit Test to obtain the Open-Circuit Characteristic (OCC: $V_{oc}$ vs $I_f$).
2. Conduct Short-Circuit Test to obtain the Short-Circuit Characteristic (SCC: $I_{sc}$ vs $I_f$).
3. For a specific field current $I_f$:
$$Z_s = \left. \frac{V_{oc,ph}}{I_{sc,ph}} \right|_{I_f = \text{const}}$$
4. Measure DC armature resistance and correct for skin effect: $R_a \approx 1.25 R_{dc}$.
5. Calculate Synchronous Reactance: $X_s = \sqrt{Z_s^2 - R_a^2}$.
6. Determine No-Load EMF $E_0$ from phasor analysis:
$$\mathbf{E}_0 = \mathbf{V} + \mathbf{I}_a (R_a + jX_s) = (V\cos\phi + I_a R_a) + j(V\sin\phi \pm I_a X_s)$$
$$E_0 = \sqrt{(V\cos\phi + I_a R_a)^2 + (V\sin\phi \pm I_a X_s)^2}$$
where $(+)$ is used for lagging PF and $(-)$ for leading PF.
Critique: The EMF method assumes magnetic linearity and uses unsaturated $Z_s$. Because saturation lowers the actual reactance, the EMF method yields an $E_0$ larger than the real value, predicting higher regulation. Hence, it is known as the Pessimistic Method.

Method B: MMF (Ampere-Turn / Rothert's) Method:
The MMF method treats armature reaction as an MMF rather than a fictitious reactance drop:
1. Determine $F_{f1}$: Field current required to generate rated terminal voltage $V$ on OCC plus armature resistance drop.
2. Determine $F_{ar}$: Field current required to circulate rated armature current on SCC against armature reaction and leakage reactance.
3. Combine field MMF vectors at an angle of $(90^\circ \pm \phi)$:
$$F_R = \sqrt{F_{f1}^2 + F_{ar}^2 - 2 F_{f1} F_{ar} \cos(90^\circ + \phi)} = \sqrt{F_{f1}^2 + F_{ar}^2 + 2 F_{f1} F_{ar} \sin\phi}$$
4. From the OCC curve, read $E_0$ corresponding to resultant field current $F_R$.
Critique: Because it understates saturation, the MMF method yields an $E_0$ smaller than the actual value. Hence, it is known as the Optimistic Method.

3. Blondel's Two-Reaction Theory for Salient Pole Alternators:
In salient pole machines, the air-gap is non-uniform: it is minimal along the direct axis ($d$-axis, center of pole) and maximal along the quadrature axis ($q$-axis, interpolar space). Consequently, the reluctance along the $q$-axis is much higher than along the $d$-axis:
$$\mathcal{R}_q \gg \mathcal{R}_d \implies X_d > X_q$$
where $X_d$ is direct-axis synchronous reactance and $X_q$ is quadrature-axis synchronous reactance.

Armature Current Resolution:
Armature current $\mathbf{I}_a$ is resolved into two orthogonal components:
- Direct-axis current $I_d = I_a \sin(\delta + \phi)$ (produces flux purely along $d$-axis).
- Quadrature-axis current $I_q = I_a \cos(\delta + \phi)$ (produces flux purely along $q$-axis).
where $\delta$ is the power (rotor) angle and $\phi$ is the load power factor angle.

Terminal Voltage Phasor Equation:
$$\mathbf{E}_0 = \mathbf{V} + I_a R_a + j I_d X_d + j I_q X_q$$
Projecting along the $d$ and $q$ axes (neglecting $R_a$):
$$V\sin\delta = I_q X_q \implies I_q = \frac{V\sin\delta}{X_q}$$
$$E_0 = V\cos\delta + I_d X_d \implies I_d = \frac{E_0 - V\cos\delta}{X_d}$$

Determination of Power Angle $\delta$:
From the geometry of the phasor diagram:
$$\tan\delta = \frac{I_a X_q \cos\phi \pm I_a R_a \sin\phi}{V + I_a X_q \sin\phi \mp I_a R_a \cos\phi}$$
Once $\delta$ is calculated, $I_d$ and $I_q$ are determined, and excitation EMF is:
$$E_0 = V\cos\delta + I_d X_d + I_q R_a$$

Power-Angle Equation & Reluctance Torque:
Total electrical power delivered per phase is:
$$P = V I_a \cos\phi = V (I_q \cos\delta + I_d \sin\delta)$$
Substituting $I_d$ and $I_q$:
$$P = V \left( \frac{V\sin\delta}{X_q} \cos\delta + \frac{E_0 - V\cos\delta}{X_d} \sin\delta \right) = \frac{E_0 V}{X_d}\sin\delta + V^2 \sin\delta\cos\delta \left( \frac{1}{X_q} - \frac{1}{X_d} \right)$$
Using $\sin\delta\cos\delta = \frac{1}{2}\sin 2\delta$:
$$P = \frac{E_0 V}{X_d}\sin\delta + \frac{V^2}{2}\left( \frac{X_d - X_q}{X_d X_q} \right)\sin 2\delta$$
Physical Interpretation:
- First Term $\frac{E_0 V}{X_d}\sin\delta$: Fundamental Electromagnetic Excitation Power, arising from interaction between rotor field excitation and stator field.
- Second Term $\frac{V^2}{2}\left( \frac{X_d - X_q}{X_d X_q} \right)\sin 2\delta$: Reluctance Power, independent of field excitation $E_0$. It arises entirely from the saliency of the rotor ($X_d \neq X_q$), which causes the rotor to align with the minimum-reluctance position of the air-gap rotating field. Even if field excitation is completely lost ($E_0 = 0$), a salient-pole alternator can still deliver stable reluctance power up to $\delta = 45^\circ$.
"""
            },
            {
                "qid": "comp-q11",
                "marks": 7,
                "type": "Analytical",
                "title": "Power Systems Analysis: Modeling, Fault Analysis, and Transient Stability",
                "yt_query": "power systems symmetrical components unsymmetrical fault swing equation equal area criterion",
                "img_path": "images/comp/power_system_stability_eac.png",
                "img_caption": "Figure 2.6: Symmetrical Component Interconnections for Asymmetrical Faults and Equal Area Criterion Stability Plot",
                "answer": r"""
Modern electrical power systems demand rigorous analytical modeling to ensure continuous stability under dynamic electromechanical disturbances and fault contingencies.

1. Transmission Line ABCD Parameters:
Transmission lines are represented as two-port four-terminal networks relating sending-end voltage/current to receiving-end quantities:
$$\begin{bmatrix} \mathbf{V}_S \\ \mathbf{I}_S \end{bmatrix} = \begin{bmatrix} A & B \\ C & D \end{bmatrix} \begin{bmatrix} \mathbf{V}_R \\ \mathbf{I}_R \end{bmatrix}$$
Properties of passive linear reciprocal transmission lines:
- Reciprocity: $A D - B C = 1$
- Symmetry: $A = D$ (for identical bilateral lines)

Line Classifications:
- Short Line ($L < 80\text{ km}$, shunt capacitance neglected):
  $$A = D = 1, \quad B = Z = R + j\omega L, \quad C = 0$$
- Medium Line ($80\text{ km} \le L \le 250\text{ km}$):
  - Nominal-$\pi$ Model (total admittance $Y$ split equally at ends $Y/2$):
  $$A = D = 1 + \frac{Y Z}{2}, \quad B = Z, \quad C = Y\left(1 + \frac{Y Z}{4}\right)$$
  - Nominal-T Model (total impedance $Z$ split equally $Z/2$):
  $$A = D = 1 + \frac{Y Z}{2}, \quad B = Z\left(1 + \frac{Y Z}{4}\right), \quad C = Y$$

2. Per-Unit (pu) Representation:
The per-unit value simplifies computational analysis across multiple voltage levels:
$$\text{Value}_{pu} = \frac{\text{Actual Value}}{\text{Base Value}}$$
Base impedance: $Z_{base} = \frac{(V_{base,LL})^2}{S_{base,3\phi}} \ \Omega$.
Base change formula:
$$Z_{pu}^{new} = Z_{pu}^{old} \times \left( \frac{V_{base}^{old}}{V_{base}^{new}} \right)^2 \times \left( \frac{S_{base}^{new}}{S_{base}^{old}} \right)$$

3. Symmetrical and Unsymmetrical Fault Analysis:
Symmetrical (Three-Phase) Fault:
All three phases short simultaneously. The system remains balanced; per-phase analysis using Thévenin equivalent impedance $Z_{th} = Z_1$ suffices:
$$I_f = \frac{V_f}{Z_1 + Z_f}, \quad \text{Short-Circuit MVA} = \sqrt{3} V_L I_f = \frac{\text{Base MVA}}{Z_{pu}}$$

Unsymmetrical Fault Analysis via Symmetrical Components:
Fortescue's Theorem resolves any unbalanced set of 3-phase vectors into three symmetrical components:
$$\begin{bmatrix} \mathbf{I}_a \\ \mathbf{I}_b \\ \mathbf{I}_c \end{bmatrix} = \begin{bmatrix} 1 & 1 & 1 \\ 1 & a^2 & a \\ 1 & a & a^2 \end{bmatrix} \begin{bmatrix} \mathbf{I}_{a0} \\ \mathbf{I}_{a1} \\ \mathbf{I}_{a2} \end{bmatrix}$$
where $a = 1 \angle 120^\circ = -0.5 + j0.866$, and $a^2 = 1 \angle 240^\circ$.

Sequence Network Connections for Shunt Faults:
1. Single Line-to-Ground (SLG) Fault (Phase 'a' to ground):
   - Boundary conditions: $I_b = 0, I_c = 0, V_a = I_a Z_f$.
   - Symmetrical components: $I_{a0} = I_{a1} = I_{a2} = \frac{1}{3}I_a$.
   - Network Interconnection: Positive, Negative, and Zero sequence networks connected in series:
   $$I_{a1} = \frac{E_a}{Z_1 + Z_2 + Z_0 + 3 Z_f}$$
   $$I_f = I_a = 3 I_{a1} = \frac{3 E_a}{Z_1 + Z_2 + Z_0 + 3 Z_f}$$
2. Line-to-Line (LL) Fault (Between Phase 'b' and Phase 'c'):
   - Boundary conditions: $I_a = 0, I_b = -I_c, V_b - V_c = I_b Z_f$.
   - Sequence components: $I_{a0} = 0, I_{a2} = -I_{a1}$.
   - Network Interconnection: Positive and Negative sequence networks connected in parallel opposing:
   $$I_{a1} = \frac{E_a}{Z_1 + Z_2 + Z_f}$$
   $$I_f = I_b = -j\sqrt{3} I_{a1}$$
3. Double Line-to-Ground (DLG) Fault (Phases 'b' and 'c' to ground):
   - Boundary conditions: $I_a = 0, V_b = V_c = (I_b + I_c)Z_f$.
   - Network Interconnection: Positive, Negative, and Zero sequence networks connected in parallel:
   $$I_{a1} = \frac{E_a}{Z_1 + \frac{Z_2 (Z_0 + 3 Z_f)}{Z_2 + Z_0 + 3 Z_f}}$$

4. Rotor Dynamics & The Swing Equation:
The electromechanical equation governing rotor angular motion of a synchronous generator is derived from Newton's second law:
$$J \frac{d^2\theta_m}{dt^2} = T_m - T_e = T_a$$
where $J$ is moment of inertia ($\text{kg}\cdot\text{m}^2$), $\theta_m$ is mechanical rotor position, $T_m$ is shaft mechanical torque, $T_e$ is electromagnetic torque, and $T_a$ is accelerating torque.
Expressing angular position relative to synchronously rotating reference frame: $\theta_m = \omega_{sm} t + \delta_m$.
Differentiating twice: $\frac{d^2\theta_m}{dt^2} = \frac{d^2\delta_m}{dt^2}$.
Multiplying both sides by synchronous speed $\omega_{sm}$:
$$J \omega_{sm} \frac{d^2\delta_m}{dt^2} = P_m - P_e$$
Defining the Angular Momentum $M = J \omega_{sm}$ and Inertia Constant $H$:
$$H = \frac{\text{Stored Kinetic Energy at Synchronous Speed}}{\text{Machine Rating } S_n} = \frac{\frac{1}{2} J \omega_{sm}^2}{S_n} \ \frac{\text{MJ}}{\text{MVA}}$$
$$M = \frac{2 H S_n}{\omega_s} \quad \implies \quad M \frac{d^2\delta}{dt^2} = P_m - P_e$$
In per-unit form:
$$\frac{2 H}{\omega_s} \frac{d^2\delta}{dt^2} = P_{m,pu} - P_{e,pu}$$
where $\omega_s = 2\pi f$ ($\text{rad/s}$) and $P_e = P_{max} \sin\delta$. This non-linear second-order differential equation is the Swing Equation.

5. Transient Stability & The Equal Area Criterion:
For a single machine connected to an infinite bus (SMIB), stability following a disturbance can be assessed without numerically solving the non-linear swing equation by applying the Equal Area Criterion.
Multiplying the swing equation by $2 \frac{d\delta}{dt}$:
$$2 \frac{d\delta}{dt} \frac{d^2\delta}{dt^2} = \frac{\omega_s}{M}(P_m - P_e)\frac{d\delta}{dt} \implies \frac{d}{dt}\left[ \left(\frac{d\delta}{dt}\right)^2 \right] = \frac{2\omega_s}{M}(P_m - P_e)\frac{d\delta}{dt}$$
Integrating from initial angle $\delta_0$ to maximum swing angle $\delta_{max}$:
$$\left( \frac{d\delta}{dt} \right)^2 = \frac{2\omega_s}{M} \int_{\delta_0}^{\delta_{max}} (P_m - P_e) d\delta$$
For the system to remain stable, the rotor speed deviation $\frac{d\delta}{dt}$ must return to zero at some maximum angle $\delta_{max}$, meaning:
$$\int_{\delta_0}^{\delta_{max}} (P_m - P_e) d\delta = 0$$
Dividing into accelerating ($A_1$) and decelerating ($A_2$) energy areas:
$$A_1 = \int_{\delta_0}^{\delta_{cr}} (P_m - P_e^{fault}) d\delta = A_2 = \int_{\delta_{cr}}^{\delta_{max}} (P_e^{post} - P_m) d\delta$$
- Critical Clearing Angle ($\delta_{cr}$): The maximum allowable angle at which circuit breakers can isolate the fault such that $A_1 = A_2$.
For a fault cleared on an unmodified system with $P_e^{fault} = 0$:
$$P_m (\delta_{cr} - \delta_0) = \int_{\delta_{cr}}^{\delta_{max}} (P_{max}\sin\delta - P_m) d\delta$$
$$\cos\delta_{cr} = \frac{P_m}{P_{max}}(\delta_{max} - \delta_0) + \cos\delta_{max}$$
where $\delta_{max} = \pi - \delta_0$. If the fault is cleared before $\delta$ reaches $\delta_{cr}$, the system successfully decelerates and remains transiently stable.
"""
            }
        ]
    },
    {
        "module_id": "comp-m3",
        "module_num": "Module 3",
        "module_title": "Control Systems & Instrumentation",
        "questions": [
            {
                "qid": "comp-q12",
                "marks": 7,
                "type": "Analytical",
                "title": "Transfer Function Derivation, Block Diagram Reduction, and Mason's Gain Formula",
                "yt_query": "transfer function block diagram reduction masons gain formula signal flow graph",
                "img_path": "images/comp/block_diagram_sfg.png",
                "img_caption": "Figure 3.1: Block Diagram Transformation Equivalence Rules and Signal Flow Graph Construction",
                "answer": r"""
A control system regulates physical processes to achieve desired performance specifications. Transfer function modeling enables s-domain algebraic analysis of linear time-invariant (LTI) systems under zero initial conditions.

1. Concept of Transfer Function:
The Transfer Function $G(s)$ of an LTI system is defined as the ratio of the Laplace transform of the output variable $C(s)$ to the Laplace transform of the input variable $R(s)$, assuming all initial conditions are identically zero:
$$G(s) = \left. \frac{\mathcal{L}\{\text{output } c(t)\}}{\mathcal{L}\{\text{input } r(t)\}} \right|_{\text{all initial conditions} = 0} = \frac{C(s)}{R(s)}$$
The inverse Laplace transform of the transfer function yields the Impulse Response $g(t) = \mathcal{L}^{-1}\{G(s)\}$, representing the system's time-domain response to a Dirac delta input $\delta(t)$.

Physical Modeling & Mechanical-Electrical Analogies:
Using D'Alembert's principle, translational mechanical systems are governed by:
$$M \frac{d^2 x(t)}{dt^2} + B \frac{dx(t)}{dt} + K x(t) = F(t)$$
- Force-Voltage ($F-V$) Analogy (Loop / Mesh Basis):
  $$L \frac{d^2 q}{dt^2} + R \frac{dq}{dt} + \frac{1}{C} q = v(t) \implies F \leftrightarrow v, \ v \leftrightarrow i, \ M \leftrightarrow L, \ B \leftrightarrow R, \ K \leftrightarrow \frac{1}{C}$$
- Force-Current ($F-I$) Analogy (Node Basis):
  $$C \frac{d^2 \phi}{dt^2} + \frac{1}{R} \frac{d\phi}{dt} + \frac{1}{L} \phi = i(t) \implies F \leftrightarrow i, \ v \leftrightarrow v, \ M \leftrightarrow C, \ B \leftrightarrow \frac{1}{R}, \ K \leftrightarrow \frac{1}{L}$$

2. Block Diagram Algebra & Reduction Rules:
Complex multivariable and multiloop systems are graphically modeled by blocks representing transfer functions, connected by summing junctions and pickoff (branch) points.
Key Reduction Equivalence Rules:
1. Cascaded (Series) Blocks:
   $$G_{eq}(s) = G_1(s) \cdot G_2(s)$$
2. Parallel Blocks:
   $$G_{eq}(s) = G_1(s) \pm G_2(s)$$
3. Elimination of Negative Feedback Loop:
   $$C(s) = G(s)[R(s) - H(s)C(s)] \implies \frac{C(s)}{R(s)} = \frac{G(s)}{1 + G(s)H(s)}$$
   (For positive feedback, the denominator is $1 - G(s)H(s)$).
4. Moving a Summing Point Ahead of a Block $G(s)$:
   Add a block $1/G(s)$ in the feedback/diverted path.
5. Moving a Summing Point Behind a Block $G(s)$:
   Add a block $G(s)$ in the diverted path.
6. Moving a Pickoff Point Ahead of a Block $G(s)$:
   Add a block $G(s)$ in the branch path.
7. Moving a Pickoff Point Behind a Block $G(s)$:
   Add a block $1/G(s)$ in the branch path.

3. Signal Flow Graphs (SFG) and Mason's Gain Formula:
A Signal Flow Graph is a directed network of nodes (representing system variables) connected by directed branches (representing functional transmittances).
Definitions:
- Forward Path: A continuous path tracing directed branches from input node to output node without passing through any node more than once.
- Forward Path Gain ($P_k$): Product of branch gains along the $k$-th forward path.
- Loop: A closed directed path that originates and terminates at the same node without traversing any other node more than once.
- Loop Gain ($L_i$): Product of branch transmittances along the $i$-th closed loop.
- Non-Touching Loops: Loops that do not share any common node.

Mason's Gain Formula:
The overall closed-loop transfer function $T(s) = \frac{C(s)}{R(s)}$ is given by:
$$T(s) = \frac{C(s)}{R(s)} = \frac{\sum_{k=1}^N P_k \Delta_k}{\Delta}$$
where:
- $N$ = Total number of independent forward paths from input to output.
- $P_k$ = Gain of the $k$-th forward path.
- $\Delta$ = System Graph Determinant:
  $$\Delta = 1 - \sum_i L_i + \sum_{j,k} L_j L_k - \sum_{m,n,p} L_m L_n L_p + \dots$$
  - $\sum L_i$ = Sum of all individual loop gains.
  - $\sum L_j L_k$ = Sum of gain products of all possible combinations of two non-touching loops.
  - $\sum L_m L_n L_p$ = Sum of gain products of all possible combinations of three non-touching loops.
- $\Delta_k$ = Path Factor (Cofactor) of the $k$-th forward path: evaluated as the graph determinant of that part of the SFG which does not touch the $k$-th forward path (obtained by deleting all nodes belonging to forward path $P_k$).

Worked Example:
Consider a multiloop system with two forward paths:
- $P_1 = G_1 G_2 G_3$, $P_2 = G_4$
- Individual loops: $L_1 = -G_1 H_1$, $L_2 = -G_2 H_2$, $L_3 = -G_1 G_2 G_3 H_3$.
- Suppose loops $L_1$ and $L_2$ share a node, but $L_1$ does not touch $L_4$ (if another isolated loop exists). If all loops touch each other, then $\sum L_j L_k = 0$.
$$\Delta = 1 - (L_1 + L_2 + L_3) = 1 + G_1 H_1 + G_2 H_2 + G_1 G_2 G_3 H_3$$
Since forward path $P_1$ touches all loops, $\Delta_1 = 1$. If $P_2$ does not touch $L_2$, then $\Delta_2 = 1 - L_2 = 1 + G_2 H_2$.
$$T(s) = \frac{P_1 \Delta_1 + P_2 \Delta_2}{\Delta} = \frac{G_1 G_2 G_3 (1) + G_4 (1 + G_2 H_2)}{1 + G_1 H_1 + G_2 H_2 + G_1 G_2 G_3 H_3}$$
Mason's formula computes the overall transfer function directly from inspection without tedious step-by-step block manipulations.
"""
            },
            {
                "qid": "comp-q13",
                "marks": 7,
                "type": "Derivation",
                "title": "Time Domain Specifications of Second-Order Underdamped Systems & Steady-State Error",
                "yt_query": "second order system time domain specifications derivation rise peak settling time steady state error",
                "img_path": "images/comp/second_order_time_response.png",
                "img_caption": "Figure 3.2: Transient Step Response of Underdamped Second-Order System Depicting Time-Domain Parameters",
                "answer": r"""
The dynamic performance of linear control systems is evaluated through time-domain specifications under standard test signals (step, ramp, parabolic). Most higher-order systems with dominant pole pairs are accurately approximated as standard second-order systems.

1. Standard Second-Order System Representation:
The canonical closed-loop transfer function of a prototype second-order system with unity feedback is:
$$T(s) = \frac{C(s)}{R(s)} = \frac{\omega_n^2}{s^2 + 2\zeta \omega_n s + \omega_n^2}$$
where:
- $\omega_n$ = Undamped natural frequency ($\text{rad/s}$)
- $\zeta$ = Damping ratio (dimensionless)

The closed-loop poles are the roots of the characteristic equation $s^2 + 2\zeta \omega_n s + \omega_n^2 = 0$:
$$s_{1,2} = -\zeta \omega_n \pm j \omega_n \sqrt{1 - \zeta^2} = -\sigma \pm j \omega_d$$
where $\sigma = \zeta \omega_n$ is the attenuation factor and $\omega_d = \omega_n \sqrt{1 - \zeta^2}$ is the damped natural frequency.

2. Derivation of Unit Step Response for Underdamped Case ($0 < \zeta < 1$):
For a unit step input $r(t) = u(t) \implies R(s) = \frac{1}{s}$:
$$C(s) = \frac{1}{s} \cdot \frac{\omega_n^2}{s^2 + 2\zeta \omega_n s + \omega_n^2} = \frac{1}{s} - \frac{s + 2\zeta \omega_n}{(s + \zeta\omega_n)^2 + \omega_d^2}$$
Completing the square in the numerator:
$$C(s) = \frac{1}{s} - \frac{(s + \zeta\omega_n) + \frac{\zeta}{\sqrt{1 - \zeta^2}} \omega_d}{(s + \zeta\omega_n)^2 + \omega_d^2} = \frac{1}{s} - \frac{s + \zeta\omega_n}{(s + \zeta\omega_n)^2 + \omega_d^2} - \frac{\zeta}{\sqrt{1 - \zeta^2}} \frac{\omega_d}{(s + \zeta\omega_n)^2 + \omega_d^2}$$
Taking the inverse Laplace transform:
$$c(t) = 1 - e^{-\zeta\omega_n t} \cos\omega_d t - \frac{\zeta}{\sqrt{1 - \zeta^2}} e^{-\zeta\omega_n t} \sin\omega_d t$$
$$c(t) = 1 - \frac{e^{-\zeta\omega_n t}}{\sqrt{1 - \zeta^2}} \left[ \sqrt{1 - \zeta^2}\cos\omega_d t + \zeta\sin\omega_d t \right]$$
Letting $\cos\phi = \zeta$ and $\sin\phi = \sqrt{1 - \zeta^2}$, where $\phi = \tan^{-1}\left(\frac{\sqrt{1 - \zeta^2}}{\zeta}\right)$:
$$c(t) = 1 - \frac{e^{-\zeta\omega_n t}}{\sqrt{1 - \zeta^2}} \sin(\omega_d t + \phi) \quad \text{for } t \ge 0$$

3. Derivation of Transient Response Performance Specifications:

Rise Time ($t_r$):
Rise time is the time required for the response to rise from $0$ to $100\%$ of its final steady-state value for the first time ($c(t_r) = 1$):
$$1 = 1 - \frac{e^{-\zeta\omega_n t_r}}{\sqrt{1 - \zeta^2}} \sin(\omega_d t_r + \phi) \implies \sin(\omega_d t_r + \phi) = 0$$
$$\omega_d t_r + \phi = \pi \implies t_r = \frac{\pi - \phi}{\omega_d} = \frac{\pi - \cos^{-1}\zeta}{\omega_n \sqrt{1 - \zeta^2}}$$

Peak Time ($t_p$):
Peak time is the time required for the response to reach its first maximum overshoot. Differentiating $c(t)$ and setting to zero:
$$\frac{dc(t)}{dt} = 0 \implies \frac{d}{dt}\left[ 1 - \frac{e^{-\zeta\omega_n t}}{\sqrt{1 - \zeta^2}}\sin(\omega_d t + \phi) \right] = 0$$
Using product rule and simplifying yields:
$$\frac{dc(t)}{dt} = \frac{\omega_n}{\sqrt{1 - \zeta^2}} e^{-\zeta\omega_n t} \sin\omega_d t = 0$$
Since $e^{-\zeta\omega_n t} \neq 0$, the condition is $\sin\omega_d t = 0 \implies \omega_d t = n\pi$.
The first peak corresponds to $n = 1$:
$$t_p = \frac{\pi}{\omega_d} = \frac{\pi}{\omega_n \sqrt{1 - \zeta^2}}$$

Maximum Percentage Overshoot ($M_p$):
Maximum overshoot is the peak value measured relative to the unit steady-state value:
$$M_p = \frac{c(t_p) - c(\infty)}{c(\infty)} \times 100\% = [c(t_p) - 1] \times 100\%$$
Substituting $t_p = \pi / \omega_d$ into $c(t)$:
$$c(t_p) = 1 - \frac{e^{-\zeta\omega_n (\pi / \omega_d)}}{\sqrt{1 - \zeta^2}} \sin\left(\omega_d \cdot \frac{\pi}{\omega_d} + \phi\right) = 1 - \frac{e^{-\frac{\pi\zeta}{\sqrt{1 - \zeta^2}}}}{\sqrt{1 - \zeta^2}} \sin(\pi + \phi)$$
Since $\sin(\pi + \phi) = -\sin\phi = -\sqrt{1 - \zeta^2}$:
$$c(t_p) = 1 + e^{-\frac{\pi\zeta}{\sqrt{1 - \zeta^2}}}$$
$$M_p = e^{-\frac{\pi\zeta}{\sqrt{1 - \zeta^2}}} \times 100\%$$
$M_p$ depends exclusively on the damping ratio $\zeta$ and is completely independent of $\omega_n$.

Settling Time ($t_s$):
Settling time is the time required for the response to enter and remain within a specified error tolerance band ($\pm 2\%$ or $\pm 5\%$).
The decay is governed by the envelope curves $1 \pm \frac{e^{-\zeta\omega_n t}}{\sqrt{1 - \zeta^2}} \approx 1 \pm e^{-\zeta\omega_n t}$.
- For a $2\%$ tolerance band ($e^{-\zeta\omega_n t_s} = 0.02 \implies \zeta\omega_n t_s \approx 4$):
  $$t_s(2\%) = \frac{4}{\zeta\omega_n} = 4\tau$$
- For a $5\%$ tolerance band ($e^{-\zeta\omega_n t_s} = 0.05 \implies \zeta\omega_n t_s \approx 3$):
  $$t_s(5\%) = \frac{3}{\zeta\omega_n} = 3\tau$$

4. Steady-State Error ($e_{ss}$) and Static Error Constants:
For a unity feedback control system with open-loop transfer function $G(s)$:
$$E(s) = R(s) - C(s) = \frac{R(s)}{1 + G(s)}$$
Applying the Final Value Theorem:
$$e_{ss} = \lim_{t\to\infty} e(t) = \lim_{s\to 0} s E(s) = \lim_{s\to 0} \frac{s R(s)}{1 + G(s)}$$
Open-loop transfer function in pole-zero form: $G(s) = \frac{K (s + z_1)\dots}{s^N (s + p_1)\dots}$, where $N$ represents the System Type (number of pure integrators at the origin).
- Positional Error Constant: $K_p = \lim_{s\to 0} G(s)$
  - For Step Input $R(s) = 1/s$: $e_{ss} = \frac{1}{1 + K_p}$
  - Type 0: $e_{ss} = \frac{1}{1 + K}$; Type 1, 2: $e_{ss} = 0$.
- Velocity Error Constant: $K_v = \lim_{s\to 0} s G(s)$
  - For Ramp Input $R(s) = 1/s^2$: $e_{ss} = \frac{1}{K_v}$
  - Type 0: $e_{ss} = \infty$; Type 1: $e_{ss} = \frac{1}{K_v}$; Type 2: $e_{ss} = 0$.
- Acceleration Error Constant: $K_a = \lim_{s\to 0} s^2 G(s)$
  - For Parabolic Input $R(s) = 1/s^3$: $e_{ss} = \frac{1}{K_a}$
  - Type 0, 1: $e_{ss} = \infty$; Type 2: $e_{ss} = \frac{1}{K_a}$.
"""
            },
            {
                "qid": "comp-q14",
                "marks": 7,
                "type": "Analytical",
                "title": "Stability Analysis in s-Domain: Routh-Hurwitz Criterion and Root Locus Technique",
                "yt_query": "routh hurwitz stability criterion root locus construction rules control systems",
                "img_path": "images/comp/root_locus_routh.png",
                "img_caption": "Figure 3.3: Root Locus Trajectory Showing Asymptotes, Breakaway Points, and Imaginary Axis Crossings",
                "answer": r"""
System stability dictates whether a perturbed system will return to equilibrium without destructive unbounded growth. In the complex s-domain, bounded-input bounded-output (BIBO) stability requires all closed-loop poles to reside strictly in the open Left Half of the s-Plane (LHP, $\text{Re}(s) < 0$).

1. Routh-Hurwitz Stability Criterion:
The Routh-Hurwitz algebraic criterion determines the number of closed-loop poles lying in the Right Half of the s-Plane (RHP) directly from the coefficients of the characteristic equation:
$$q(s) = a_0 s^n + a_1 s^{n-1} + a_2 s^{n-2} + \dots + a_{n-1} s + a_n = 0 \quad (a_0 > 0)$$

Necessary Condition:
All coefficients $a_0, a_1, \dots, a_n$ must be present (non-zero) and must possess the identical algebraic sign. If any term is missing or has a differing sign, the system has at least one pole in the RHP or on the imaginary axis, making it unstable.

Routh Array Formulation:
Row $s^n$: $a_0 \quad a_2 \quad a_4 \quad a_6 \dots$
Row $s^{n-1}$: $a_1 \quad a_3 \quad a_5 \quad a_7 \dots$
Row $s^{n-2}$: $b_1 \quad b_2 \quad b_3 \dots$
Row $s^{n-3}$: $c_1 \quad c_2 \quad c_3 \dots$
where:
$$b_1 = \frac{a_1 a_2 - a_0 a_3}{a_1}, \quad b_2 = \frac{a_1 a_4 - a_0 a_5}{a_1}, \quad b_3 = \frac{a_1 a_6 - a_0 a_7}{a_1}$$
$$c_1 = \frac{b_1 a_3 - a_1 b_2}{b_1}, \quad c_2 = \frac{b_1 a_5 - a_1 b_3}{b_1}$$

Routh Stability Theorem:
A system is stable if and only if all coefficients in the first column of the Routh array are strictly positive. The number of sign changes in the first column equals the number of roots with positive real parts (unstable RHP poles).

Special Cases in Routh Array:
- Case 1: First Element in a Row is Zero, but other elements are non-zero:
  A zero in the first column causes division by zero in subsequent rows.
  Resolution Method: Replace the zero with an infinitesimally small positive quantity $\varepsilon > 0$. Complete the array in terms of $\varepsilon$, and then evaluate signs by taking the limit $\varepsilon \to 0^+$. Alternatively, substitute $s = 1/z$ into $q(s)$ and form the Routh array for the inverted polynomial in $z$.
- Case 2: An Entire Row of Zeros Occurs:
  This indicates the presence of roots symmetrically located about the origin in the s-plane:
  - Pairs of real roots of equal magnitude and opposite signs ($\pm \sigma$)
  - Pairs of purely imaginary conjugate roots on the $j\omega$-axis ($\pm j\omega$)
  - Quads of complex roots ($\pm \sigma \pm j\omega$)
  Resolution Method: Construct an Auxiliary Polynomial $A(s)$ using the coefficients of the row immediately preceding the all-zero row. Differentiate $A(s)$ with respect to $s$ ($\frac{dA(s)}{ds}$), and replace the all-zero row with the coefficients of this derivative. The roots of $A(s) = 0$ give the exact symmetric pole locations (and imaginary axis crossing frequencies $\omega = \sqrt{\dots}$ for sustained marginal oscillation).

2. The Root Locus Technique (W.R. Evans):
The root locus is a graphical trajectory of the closed-loop poles in the complex s-plane as an open-loop gain parameter $K$ is varied continuously from $0$ to $\infty$.
The characteristic equation is $1 + G(s)H(s) = 0 \implies G(s)H(s) = -1 = 1 \angle \pm (2k+1)180^\circ$.
- Angle Condition: $\angle G(s)H(s) = \pm (2k+1)180^\circ$ (must be satisfied for any point on the root locus).
- Magnitude Condition: $|G(s)H(s)| = 1 \implies K = \frac{\prod |s + p_i|}{\prod |s + z_j|}$ (used to compute the exact value of $K$ at any point).

Comprehensive Construction Rules:
1. Symmetry: The root locus is completely symmetrical about the real axis (complex roots occur in conjugate pairs).
2. Number of Branches: The total number of root locus branches equals the number of open-loop poles $P$ (assuming $P \ge Z$).
3. Starting and Ending Points: Branches originate at open-loop poles for $K = 0$ and terminate at open-loop finite zeros or along asymptotes toward infinity for $K = \infty$.
4. Real-Axis Segments: A point on the real axis lies on the root locus if and only if the total number of real open-loop poles and zeros lying to its right is odd.
5. Asymptotes ($K \to \infty$): $(P - Z)$ branches terminate at infinity along straight-line asymptotes.
   - Angles of Asymptotes:
     $$\theta_a = \frac{(2q + 1)180^\circ}{P - Z} \quad \text{for } q = 0, 1, 2, \dots, (P - Z - 1)$$
   - Centroid ($\sigma_A$) of Asymptotes: Point of intersection of asymptotes on the real axis:
     $$\sigma_A = \frac{\sum \text{Real parts of poles} - \sum \text{Real parts of zeros}}{P - Z} = \frac{\sum P_i - \sum Z_j}{P - Z}$$
6. Breakaway and Break-in Points: Points where two or more branches meet and depart from (or arrive onto) the real axis. They are found by expressing $K$ as a function of $s$ from the characteristic equation $1 + K \frac{N(s)}{D(s)} = 0 \implies K = -\frac{D(s)}{N(s)}$, setting:
   $$\frac{dK}{ds} = 0$$
   Only roots that satisfy the real-axis criterion and yield a valid positive real gain $K > 0$ are actual breakaway/break-in points.
7. Angle of Departure from Complex Poles ($\phi_d$) and Angle of Arrival at Complex Zeros ($\phi_a$):
   $$\phi_d = 180^\circ - \sum \phi_p + \sum \phi_z$$
   $$\phi_a = 180^\circ - \sum \phi_z + \sum \phi_p$$
   where $\sum \phi_p$ and $\sum \phi_z$ are the sum of angles subtended by all other open-loop poles and zeros to the complex pole/zero.
8. Crossing of Imaginary Axis: Points where the root locus crosses the $j\omega$-axis (marking the boundary between stability and instability, and identifying critical marginal gain $K_{mar}$) are found by:
   - Substituting $s = j\omega$ into the characteristic equation and equating real and imaginary parts to zero, OR
   - Applying the Routh-Hurwitz criterion to find the gain $K$ that produces an entire row of zeros.
"""
            },
            {
                "qid": "comp-q15",
                "marks": 7,
                "type": "Analytical",
                "title": "Frequency Domain Analysis: Bode Plots and Nyquist Stability Criterion",
                "yt_query": "bode plot gain phase margin nyquist stability criterion cauchy argument",
                "img_path": "images/comp/bode_nyquist_plot.png",
                "img_caption": "Figure 3.4: Bode Magnitude and Phase Response and Nyquist Contour Encirclement Diagram",
                "answer": r"""
Frequency domain analysis evaluates the steady-state response of an LTI system to sinusoidal inputs of varying frequency $\omega$. It provides direct measures of relative stability, bandwidth, and noise rejection without requiring explicit time-domain differential solutions.

1. Bode Plot Construction:
A Bode plot consists of two separate graphs plotted against frequency $\omega$ on a logarithmic scale ($\log_{10}\omega$):
- Magnitude Plot: Logarithmic gain in decibels ($20\log_{10}|G(j\omega)| \text{ dB}$).
- Phase Plot: Phase angle in degrees ($\angle G(j\omega)$).

Asymptotic Approximations of Standard Factors:
Any rational transfer function in Bode canonical form can be factored into four elementary terms:
1. Constant Gain $K$:
   - Magnitude: Horizontal straight line at $20\log_{10} K \text{ dB}$.
   - Phase: $0^\circ$ for $K > 0$; $-180^\circ$ for $K < 0$.
2. Integral / Derivative Factor $(j\omega)^{\pm n}$:
   - For pole at origin $1/(j\omega)^n$: Straight line passing through $0\text{ dB}$ at $\omega = 1\text{ rad/s}$ with slope of $-20n\text{ dB/decade}$. Phase is constant at $-90n^\circ$.
   - For zero at origin $(j\omega)^n$: Slope of $+20n\text{ dB/decade}$, phase is $+90n^\circ$.
3. Simple First-Order Factor $(1 + j\omega T)^{\pm 1}$:
   - Corner Frequency: $\omega_c = \frac{1}{T}$.
   - For pole $\frac{1}{1 + j\omega T}$:
     - Low frequency ($\omega \ll \omega_c$): $0\text{ dB}$ asymptotic line.
     - High frequency ($\omega \gg \omega_c$): Asymptote with slope of $-20\text{ dB/decade}$.
     - Actual magnitude at corner frequency is $20\log_{10}(1/\sqrt{2}) = -3\text{ dB}$.
     - Phase: $0^\circ$ at $\omega \to 0$, $-45^\circ$ at $\omega = \omega_c$, $-90^\circ$ at $\omega \to \infty$.
   - For zero $(1 + j\omega T)$: Asymptote breaks upward at $\omega_c$ with $+20\text{ dB/decade}$ slope; phase goes from $0^\circ \to +45^\circ \to +90^\circ$.
4. Quadratic Second-Order Factor $\left[ 1 + j 2\zeta \left(\frac{\omega}{\omega_n}\right) - \left(\frac{\omega}{\omega_n}\right)^2 \right]^{\pm 1}$:
   - Asymptote breaks at corner frequency $\omega_n$ with a steep slope of $\pm 40\text{ dB/decade}$.
   - Resonant Peak: $M_r = \frac{1}{2\zeta\sqrt{1 - \zeta^2}}$ occurring at $\omega_r = \omega_n \sqrt{1 - 2\zeta^2}$ (for $\zeta < 0.707$).

2. Gain Margin, Phase Margin, and Relative Stability:
Relative stability quantifies how close a stable closed-loop system is to the verge of instability:
- Gain Crossover Frequency ($\omega_{gc}$): The frequency at which the open-loop magnitude is unity ($0\text{ dB}$):
  $$|G(j\omega_{gc})H(j\omega_{gc})| = 1 \quad \implies \quad 20\log_{10}|G(j\omega_{gc})H(j\omega_{gc})| = 0\text{ dB}$$
- Phase Crossover Frequency ($\omega_{pc}$): The frequency at which the open-loop phase lag reaches exactly $-180^\circ$:
  $$\angle G(j\omega_{pc})H(j\omega_{pc}) = -180^\circ$$
- Phase Margin ($PM$): The additional phase lag that can be introduced at $\omega_{gc}$ before the system becomes unstable:
  $$PM = 180^\circ + \angle G(j\omega_{gc})H(j\omega_{gc})$$
- Gain Margin ($GM$): The reciprocal of the open-loop magnitude at $\omega_{pc}$, expressed in decibels:
  $$GM = \frac{1}{|G(j\omega_{pc})H(j\omega_{pc})|} \implies GM_{\text{dB}} = -20\log_{10}|G(j\omega_{pc})H(j\omega_{pc})|$$

Criteria for Closed-Loop Stability from Bode Plots:
- Stable System: Both $GM > 0\text{ dB}$ and $PM > 0^\circ$. The gain crossover frequency occurs before the phase crossover frequency ($\omega_{gc} < \omega_{pc}$).
- Marginally Stable System: $GM = 0\text{ dB}$ and $PM = 0^\circ$, with $\omega_{gc} = \omega_{pc}$.
- Unstable System: $GM < 0\text{ dB}$ and $PM < 0^\circ$, with $\omega_{gc} > \omega_{pc}$.

3. Nyquist Stability Criterion:
The Nyquist criterion relates the open-loop frequency response $G(s)H(s)$ to the closed-loop stability using Cauchy's Principle of the Argument from complex variable analysis.

Cauchy's Principle of the Argument:
If a closed contour $\Gamma_s$ in the s-plane encloses $Z$ zeros and $P$ poles of an analytic function $F(s) = 1 + G(s)H(s)$, then the mapped contour $\Gamma_F$ in the $F(s)$-plane encircles the origin in a clockwise direction $N$ times, where:
$$N = Z - P$$
Since $F(s) = 1 + G(s)H(s)$, encirclement of the origin by $F(s)$ is mathematically identical to encirclement of the Critical Point $(-1 + j0)$ by the open-loop transfer function $G(s)H(s)$.

Nyquist Contour:
To investigate stability, the contour $\Gamma_s$ is selected to enclose the entire Right Half of the s-Plane (RHP):
- Part 1: Positive imaginary axis from $s = +j0$ to $s = +j\infty$.
- Part 2: Semicircular arc of radius $R \to \infty$ spanning $+j\infty \to +R \to -j\infty$.
- Part 3: Negative imaginary axis from $s = -j\infty$ to $s = -j0$.
- Part 4: If open-loop poles exist at the origin, small semicircular indentations of radius $\varepsilon \to 0$ are bypassed into the RHP.

Nyquist Encirclement Formula:
$$N = Z - P$$
where:
- $N$ = Number of clockwise encirclements of the critical point $(-1 + j0)$ by the mapped locus $G(s)H(s)$. (Counter-clockwise encirclements count as negative $N$).
- $P$ = Number of open-loop poles lying in the RHP (known a priori from $G(s)H(s)$).
- $Z$ = Number of closed-loop poles lying in the RHP (unstable closed-loop roots).

Condition for Closed-Loop Stability:
For the closed-loop system to be stable, there must be zero closed-loop poles in the RHP ($Z = 0$):
$$0 = N + P \implies N = -P$$
Conclusion: A feedback control system is closed-loop stable if and only if the Nyquist plot of $G(s)H(s)$ encircles the critical point $(-1 + j0)$ in a Counter-Clockwise direction exactly $P$ times, where $P$ is the number of open-loop poles of $G(s)H(s)$ in the RHP. If the open-loop system is inherently stable ($P = 0$), then the closed-loop system is stable if and only if the Nyquist plot does not encircle $(-1 + j0)$ at all ($N = 0$).
"""
            },
            {
                "qid": "comp-q16",
                "marks": 7,
                "type": "Analytical",
                "title": "Modern Control (State-Space, STM, Controllability) & Electrical Measurement Bridges",
                "yt_query": "state space representation state transition matrix controllability observability bridges ct pt",
                "img_path": "images/comp/state_space_bridges.png",
                "img_caption": "Figure 3.5: State-Space Canonical State Architecture and AC Measurement Bridges (Maxwell-Wien & Schering)",
                "answer": r"""
Modern control theory overcomes the single-input single-output (SISO) limitations of classical transfer function techniques by formulating system dynamics in state-space as coupled first-order matrix differential equations. Concurrently, precise instrumentation bridges and instrument transformers ensure accurate measurement of circuit parameters and high-voltage grid quantities.

1. State-Space Representation:
For an $n$-th order linear time-invariant system with $m$ inputs and $p$ outputs:
- State Differential Equation:
  $$\mathbf{\dot{x}}(t) = \mathbf{A}\mathbf{x}(t) + \mathbf{B}\mathbf{u}(t)$$
- Output Equation:
  $$\mathbf{y}(t) = \mathbf{C}\mathbf{x}(t) + \mathbf{D}\mathbf{u}(t)$$
where:
- $\mathbf{x}(t) \in \mathbb{R}^n$ is the state vector.
- $\mathbf{u}(t) \in \mathbb{R}^m$ is the control input vector.
- $\mathbf{y}(t) \in \mathbb{R}^p$ is the output vector.
- $\mathbf{A} \in \mathbb{R}^{n \times n}$ is the System Matrix.
- $\mathbf{B} \in \mathbb{R}^{n \times m}$ is the Input Matrix.
- $\mathbf{C} \in \mathbb{R}^{p \times n}$ is the Output Matrix.
- $\mathbf{D} \in \mathbb{R}^{p \times m}$ is the Direct Transmission (Feedforward) Matrix.

Conversion to Transfer Function:
Taking the Laplace transform with zero initial conditions:
$$s \mathbf{X}(s) = \mathbf{A}\mathbf{X}(s) + \mathbf{B}\mathbf{U}(s) \implies (s\mathbf{I} - \mathbf{A})\mathbf{X}(s) = \mathbf{B}\mathbf{U}(s) \implies \mathbf{X}(s) = (s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B}\mathbf{U}(s)$$
$$\mathbf{Y}(s) = \mathbf{C}\mathbf{X}(s) + \mathbf{D}\mathbf{U}(s) = \left[ \mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B} + \mathbf{D} \right] \mathbf{U}(s)$$
$$G(s) = \frac{\mathbf{Y}(s)}{\mathbf{U}(s)} = \mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B} + \mathbf{D}$$

2. State Transition Matrix (STM):
The solution to the homogeneous state equation $\mathbf{\dot{x}}(t) = \mathbf{A}\mathbf{x}(t)$ with initial state $\mathbf{x}(0)$ is:
$$\mathbf{x}(t) = e^{\mathbf{A}t} \mathbf{x}(0) = \mathbf{\Phi}(t) \mathbf{x}(0)$$
The matrix exponential $\mathbf{\Phi}(t) = e^{\mathbf{A}t}$ is the State Transition Matrix:
$$\mathbf{\Phi}(t) = \mathcal{L}^{-1}\left\{ (s\mathbf{I} - \mathbf{A})^{-1} \right\} = \mathbf{I} + \mathbf{A}t + \frac{\mathbf{A}^2 t^2}{2!} + \frac{\mathbf{A}^3 t^3}{3!} + \dots$$
Properties of the State Transition Matrix:
1. $\mathbf{\Phi}(0) = e^{\mathbf{A}\cdot 0} = \mathbf{I}$
2. $\mathbf{\Phi}^{-1}(t) = [e^{\mathbf{A}t}]^{-1} = e^{-\mathbf{A}t} = \mathbf{\Phi}(-t)$
3. $\mathbf{\Phi}(t_1 + t_2) = \mathbf{\Phi}(t_1)\mathbf{\Phi}(t_2)$
4. $[\mathbf{\Phi}(t)]^k = \mathbf{\Phi}(k t)$
5. $\frac{d\mathbf{\Phi}(t)}{dt} = \mathbf{A} \mathbf{\Phi}(t) = \mathbf{\Phi}(t) \mathbf{A}$

The complete time-domain solution with non-zero input $\mathbf{u}(t)$ is:
$$\mathbf{x}(t) = \mathbf{\Phi}(t)\mathbf{x}(0) + \int_0^t \mathbf{\Phi}(t - \tau)\mathbf{B}\mathbf{u}(\tau) d\tau$$

3. Controllability and Observability (Kalman's Criteria):
- Controllability: A system is completely state controllable if an unconstrained control vector $\mathbf{u}(t)$ can transfer any initial state $\mathbf{x}(0)$ to any desired terminal state $\mathbf{x}(t_1)$ in a finite time interval $t_1$.
  Kalman's Controllability Matrix:
  $$\mathbf{Q}_c = \begin{bmatrix} \mathbf{B} & \mathbf{A}\mathbf{B} & \mathbf{A}^2\mathbf{B} & \dots & \mathbf{A}^{n-1}\mathbf{B} \end{bmatrix} \in \mathbb{R}^{n \times n}$$
  Condition: The system is controllable if and only if $\text{rank}(\mathbf{Q}_c) = n$ (i.e., $\det(\mathbf{Q}_c) \neq 0$).
- Observability: A system is completely observable if every initial state $\mathbf{x}(0)$ can be uniquely determined from the observation of the output $\mathbf{y}(t)$ over a finite time interval $t_1$.
  Kalman's Observability Matrix:
  $$\mathbf{Q}_o = \begin{bmatrix} \mathbf{C} \\ \mathbf{C}\mathbf{A} \\ \mathbf{C}\mathbf{A}^2 \\ \vdots \\ \mathbf{C}\mathbf{A}^{n-1} \end{bmatrix} \in \mathbb{R}^{n \times n}$$
  Condition: The system is observable if and only if $\text{rank}(\mathbf{Q}_o) = n$ (i.e., $\det(\mathbf{Q}_o) \neq 0$).

4. Electrical Measurement Bridges:
Bridge circuits use a null-deflection balance detector to achieve measurement accuracy independent of source voltage fluctuations.
General AC Bridge Balance Condition:
$$\mathbf{Z}_1 \mathbf{Z}_4 = \mathbf{Z}_2 \mathbf{Z}_3 \implies |\mathbf{Z}_1||\mathbf{Z}_4| = |\mathbf{Z}_2||\mathbf{Z}_3| \quad \text{and} \quad \theta_1 + \theta_4 = \theta_2 + \theta_3$$

- Wheatstone Bridge (DC Resistance $1\,\Omega \text{ to } 100\text{ k}\Omega$):
  $$R_x = \frac{R_2 R_3}{R_1}$$
- Maxwell-Wien Bridge (Medium-Q Inductance, $1 < Q < 10$):
  Measures unknown inductance $L_x$ and series resistance $R_x$ against a standard capacitor $C_4$ in parallel with resistor $R_4$:
  $$\mathbf{Z}_1 = R_x + j\omega L_x, \quad \mathbf{Z}_2 = R_2, \quad \mathbf{Z}_3 = R_3, \quad \mathbf{Y}_4 = \frac{1}{R_4} + j\omega C_4$$
  At balance: $\mathbf{Z}_1 = \mathbf{Z}_2 \mathbf{Z}_3 \mathbf{Y}_4 \implies R_x + j\omega L_x = R_2 R_3 \left( \frac{1}{R_4} + j\omega C_4 \right)$
  Equating real and imaginary parts:
  $$R_x = \frac{R_2 R_3}{R_4}$$
  $$L_x = R_2 R_3 C_4$$
  Quality factor: $Q = \frac{\omega L_x}{R_x} = \omega C_4 R_4$.
- Schering Bridge (Capacitance and Dielectric Loss):
  Measures unknown capacitance $C_x$ and dielectric dissipation factor $\tan\delta$:
  $$\mathbf{Z}_1 = R_x - \frac{j}{\omega C_x}, \quad \mathbf{Z}_2 = R_2, \quad \mathbf{Z}_3 = -\frac{j}{\omega C_3}, \quad \mathbf{Y}_4 = \frac{1}{R_4} + j\omega C_4$$
  Balance equations:
  $$C_x = C_3 \left( \frac{R_4}{R_2} \right)$$
  $$R_x = R_2 \left( \frac{C_4}{C_3} \right)$$
  Dissipation factor (Loss tangent): $D = \tan\delta = \omega C_x R_x = \omega C_4 R_4$.

5. Instrument Transformers (CT and PT):
Instrument transformers scale high transmission voltages and currents down to standardized protective relay and meter levels ($5\text{ A}$ or $1\text{ A}$ for CT; $110\text{ V}$ for PT).
- Current Transformer (CT): Primary winding has few turns in series with the power line; secondary has many turns connected to low-impedance ammeter/relay coils.
  - Transformation Ratio: $R = \frac{I_p}{I_s} \approx n + \frac{I_c\cos\delta + I_m\sin\delta}{I_s}$
  - Ratio Error: $\% \varepsilon = \frac{K_n I_s - I_p}{I_p} \times 100\%$
  - Phase Angle Error: $\theta \approx \frac{180}{\pi}\left( \frac{I_m\cos\delta - I_c\sin\delta}{n I_s} \right) \text{ degrees}$
  - Crucial Safety Rule: The secondary of an energized CT must NEVER be open-circuited. Opening the secondary destroys demagnetizing secondary MMF ($N_s I_s = 0$), forcing the entire huge primary line current to become magnetizing current ($I_p = I_0$), causing catastrophic iron saturation, extreme core overheating, and inducing lethal kilovolt peaks across open secondary terminals.
"""
            }
        ]
    },
    {
        "module_id": "comp-m4",
        "module_num": "Module 4",
        "module_title": "Analog & Digital Electronics",
        "questions": [
            {
                "qid": "comp-q17",
                "marks": 7,
                "type": "Derivation",
                "title": "Semiconductor Diode Rectifiers, Capacitor Filters, and Zener Voltage Regulators",
                "yt_query": "rectifier full wave bridge ripple factor efficiency zener diode voltage regulator",
                "img_path": "images/comp/rectifiers_zener_regulator.png",
                "img_caption": "Figure 4.1: Bridge Rectifier Waveforms with C-Filter and Zener Diode Shunt Voltage Regulator Circuit",
                "answer": r"""
Semiconductor diodes are essential nonlinear electronic components used for rectification, wave shaping, and voltage stabilization.

1. Diode Physics and Shockley Equation:
The current-voltage relationship of a P-N junction diode is described by the Shockley diode equation:
$$I_D = I_s \left( e^{\frac{V_D}{\eta V_T}} - 1 \right)$$
where $I_s$ is reverse saturation current, $\eta$ is ideality factor ($\eta = 1$ for Ge, $\eta \approx 1-2$ for Si), and $V_T = \frac{k T}{q} \approx 26\text{ mV}$ at room temperature ($300\text{ K}$).

2. Rectifier Circuits & Performance Derivations:

Full-Wave Bridge Rectifier:
Consider an AC source $v_s(t) = V_m \sin\omega t$ connected to a full-wave bridge rectifier with four diodes ($D_1-D_4$) feeding load resistance $R_L$.
- During positive half-cycle ($0 \le \omega t \le \pi$): Diodes $D_1$ and $D_2$ conduct.
  $$i_L(t) = I_m \sin\omega t \quad \text{where } I_m = \frac{V_m}{2 r_f + R_L}$$
- During negative half-cycle ($\pi \le \omega t \le 2\pi$): Diodes $D_3$ and $D_4$ conduct.
  $$i_L(t) = -I_m \sin\omega t$$

Mathematical Derivations:
1. Average (DC) Load Current and Voltage:
$$I_{dc} = \frac{1}{\pi} \int_0^\pi I_m \sin\theta\,d\theta = \frac{I_m}{\pi} [-\cos\theta]_0^\pi = \frac{2 I_m}{\pi} \approx 0.637 I_m$$
$$V_{dc} = I_{dc} R_L = \frac{2 I_m R_L}{\pi} \approx \frac{2 V_m}{\pi}$$
(For Half-Wave Rectifier: $I_{dc} = \frac{I_m}{\pi}$, $V_{dc} = \frac{V_m}{\pi}$).

2. Root Mean Square (RMS) Load Current:
$$I_{rms} = \sqrt{\frac{1}{\pi} \int_0^\pi (I_m \sin\theta)^2\,d\theta} = \sqrt{\frac{I_m^2}{\pi} \int_0^\pi \frac{1 - \cos 2\theta}{2}\,d\theta} = \sqrt{\frac{I_m^2}{2\pi} [\pi]} = \frac{I_m}{\sqrt{2}} \approx 0.707 I_m$$
(For Half-Wave Rectifier: $I_{rms} = \frac{I_m}{2}$).

3. Ripple Factor ($\gamma$):
Ripple factor measures the proportion of unwanted AC harmonic content present in the rectified output:
$$\gamma = \frac{I_{ac,rms}}{I_{dc}} = \frac{\sqrt{I_{rms}^2 - I_{dc}^2}}{I_{dc}} = \sqrt{\left(\frac{I_{rms}}{I_{dc}}\right)^2 - 1} = \sqrt{FF^2 - 1}$$
where Form Factor is $FF = \frac{I_{rms}}{I_{dc}}$.
- For Full-Wave Rectifier:
  $$FF = \frac{I_m / \sqrt{2}}{2 I_m / \pi} = \frac{\pi}{2\sqrt{2}} \approx 1.11$$
  $$\gamma = \sqrt{(1.11)^2 - 1} = \sqrt{1.2337 - 1} = \sqrt{0.2337} \approx 0.482 \ (48.2\%)$$
- For Half-Wave Rectifier:
  $$FF = \frac{I_m / 2}{I_m / \pi} = \frac{\pi}{2} \approx 1.57 \implies \gamma = \sqrt{(1.57)^2 - 1} \approx 1.21 \ (121\%)$$

4. Rectification Efficiency ($\eta$):
$$\eta = \frac{\text{DC Output Power } P_{dc}}{\text{AC Input Power } P_{ac}} = \frac{I_{dc}^2 R_L}{I_{rms}^2 (2 r_f + R_L)}$$
Neglecting diode forward resistance ($r_f \ll R_L$):
$$\eta = \frac{(2 I_m / \pi)^2 R_L}{(I_m / \sqrt{2})^2 R_L} = \frac{4 / \pi^2}{1 / 2} = \frac{8}{\pi^2} \approx 81.2\%$$
(For Half-Wave Rectifier: $\eta = \frac{4}{\pi^2} \approx 40.6\%$).

5. Peak Inverse Voltage (PIV):
- Full-Wave Bridge Rectifier: $\text{PIV} = V_m$ (each non-conducting diode blocks maximum secondary peak voltage).
- Center-Tapped Full-Wave Rectifier: $\text{PIV} = 2 V_m$.
- Half-Wave Rectifier: $\text{PIV} = V_m$.

3. Shunt Capacitor (C) Filter Smoothing:
A large capacitor $C$ in parallel with $R_L$ charges to $V_m$ at the voltage peak, then discharges slowly through $R_L$ during the interval between peaks.
Peak-to-Peak Ripple Voltage ($\Delta V_r$):
$$\Delta V_r = \frac{I_{dc}}{2 f C} = \frac{V_m}{2 f R_L C}$$
where $f$ is supply line frequency ($2f$ is full-wave ripple frequency).
The RMS value of the triangular ripple waveform is:
$$V_{r,rms} = \frac{\Delta V_r}{2\sqrt{3}} = \frac{V_m}{4\sqrt{3} f R_L C}$$
DC Output Voltage with filter:
$$V_{dc} = V_m - \frac{\Delta V_r}{2} = V_m - \frac{I_{dc}}{4 f C} \approx V_m$$
Ripple Factor with C-filter:
$$\gamma = \frac{V_{r,rms}}{V_{dc}} \approx \frac{1}{4\sqrt{3} f R_L C}$$

4. Zener Diode Voltage Regulator:
Zener diodes operate in the reverse breakdown region to maintain a constant output voltage $V_Z$ across varying input voltage $V_{in}$ and load current $I_L$.
Breakdown Mechanisms:
- Zener Breakdown: Occurs in heavily doped P-N junctions ($V_Z < 5-6\text{ V}$) under strong electric fields ($> 10^7\text{ V/m}$) through direct quantum mechanical tunneling of valence electrons into the conduction band; possesses a negative temperature coefficient.
- Avalanche Breakdown: Occurs in lightly doped junctions ($V_Z > 6\text{ V}$) through impact ionization, where accelerated carriers dislodge secondary electron-hole pairs; possesses a positive temperature coefficient.

Regulator Circuit Design:
A series resistor $R_s$ drops the voltage difference $(V_{in} - V_Z)$.
Applying KCL at the output node:
$$I_s = I_Z + I_L \implies \frac{V_{in} - V_Z}{R_s} = I_Z + \frac{V_Z}{R_L}$$
For proper regulation, the Zener current must satisfy $I_{Z,\min} \le I_Z \le I_{Z,\max}$ under all line voltage and load current conditions:
- Condition 1: Minimum input voltage $V_{in,\min}$ and maximum load current $I_{L,\max}$ (worst-case lowest Zener current, which must remain above knee current $I_{Z,\min}$):
  $$R_s \le R_{s,\max} = \frac{V_{in,\min} - V_Z}{I_{Z,\min} + I_{L,\max}}$$
- Condition 2: Maximum input voltage $V_{in,\max}$ and minimum load current $I_{L,\min}$ (worst-case highest Zener current, which must not exceed maximum dissipation rating $I_{Z,\max} = P_{Z,\max}/V_Z$):
  $$R_s \ge R_{s,\min} = \frac{V_{in,\max} - V_Z}{I_{Z,\max} + I_{L,\min}}$$
Selecting $R_s$ within $[R_{s,\min}, R_{s,\max}]$ guarantees precise voltage stabilization.
"""
            },
            {
                "qid": "comp-q18",
                "marks": 7,
                "type": "Analytical",
                "title": "BJT CE Configuration: Characteristics, Voltage Divider Bias Stability, and Small-Signal Analysis",
                "yt_query": "bjt ce configuration characteristics voltage divider bias stability factor h parameter model",
                "img_path": "images/comp/bjt_ce_amplifier_biasing.png",
                "img_caption": "Figure 4.2: BJT Common Emitter Output Characteristics, Voltage Divider Bias Circuit, and Small-Signal re Equivalent Model",
                "answer": r"""
The Bipolar Junction Transistor (BJT) is a current-controlled active device consisting of two back-to-back P-N junctions (emitter-base and collector-base). The Common Emitter (CE) configuration is widely utilized due to its balanced combination of high voltage gain, high current gain, and moderate input/output impedances.

1. BJT Common Emitter (CE) Characteristics:
- Input Characteristics ($I_B$ vs $V_{BE}$ for constant $V_{CE}$):
  Resembles a forward-biased diode. Cut-in voltage is $\sim 0.6-0.7\text{ V}$ for Silicon. As $V_{CE}$ increases, the effective base width decreases (Early Effect), slightly reducing $I_B$ for a given $V_{BE}$, shifting the curve slightly to the right.
- Output Characteristics ($I_C$ vs $V_{CE}$ for constant $I_B$):
  - Cutoff Region ($V_{BE} < 0.7\text{ V}$): Both junctions are reverse-biased; $I_C \approx I_{CEO} = (1 + \beta) I_{CBO} \approx 0$.
  - Saturation Region ($V_{CE} < V_{CE(sat)} \approx 0.2\text{ V}$): Both junctions are forward-biased; collector current is limited by the external circuit ($I_C < \beta I_B$).
  - Active Region ($V_{BE} \approx 0.7\text{ V}, V_{CE} > 0.2\text{ V}$): Emitter-base forward-biased, collector-base reverse-biased; $I_C = \beta I_B + I_{CEO}$. The curves exhibit a slight upward slope due to Base-Width Modulation (Early Effect), extrapolating back to the negative voltage axis at the Early Voltage $-V_A$. The finite output resistance is $r_o = \frac{V_A + V_{CE}}{I_C}$.

2. DC Biasing & Stability Factor Analysis:
The quiescent operating point ($Q$-point: $V_{CEQ}, I_{CQ}$) must remain stable against temperature-induced variations in:
1. Reverse saturation current $I_{CO}$ (doubles every $10^\circ\text{C}$).
2. Base-emitter voltage $V_{BE}$ (decreases by $-2.5\text{ mV/}^\circ\text{C}$).
3. Current gain $\beta$ (increases with temperature).

Voltage Divider (Self-Bias / Universal Bias) Circuit:
Resistors $R_1$ and $R_2$ form a potential divider across $V_{CC}$, while emitter resistor $R_E$ provides negative current feedback.
Thévenin Equivalent Looking into Base:
$$V_{th} = V_{CC} \left( \frac{R_2}{R_1 + R_2} \right)$$
$$R_{th} = R_1 \parallel R_2 = \frac{R_1 R_2}{R_1 + R_2}$$
Applying KVL around the base-emitter loop:
$$V_{th} = I_B R_{th} + V_{BE} + I_E R_E$$
Since $I_E = I_B + I_C$:
$$V_{th} = I_B R_{th} + V_{BE} + (I_B + I_C) R_E = I_B (R_{th} + R_E) + V_{BE} + I_C R_E$$
$$I_B = \frac{V_{th} - V_{BE} - I_C R_E}{R_{th} + R_E}$$
Substituting $I_C = \beta I_B + (1 + \beta) I_{CO}$:
$$I_C = \beta \left[ \frac{V_{th} - V_{BE} - I_C R_E}{R_{th} + R_E} \right] + (1 + \beta) I_{CO}$$
$$I_C \left[ 1 + \frac{\beta R_E}{R_{th} + R_E} \right] = \frac{\beta(V_{th} - V_{BE})}{R_{th} + R_E} + (1 + \beta) I_{CO}$$
$$I_C \left[ \frac{R_{th} + R_E (1 + \beta)}{R_{th} + R_E} \right] = \frac{\beta(V_{th} - V_{BE})}{R_{th} + R_E} + (1 + \beta) I_{CO}$$
$$I_C = \frac{\beta(V_{th} - V_{BE})}{R_{th} + (\beta + 1) R_E} + \frac{(1 + \beta)(R_{th} + R_E)}{R_{th} + (\beta + 1) R_E} I_{CO}$$

Derivation of Stability Factor $S$:
The stability factor $S$ quantifies the sensitivity of $I_C$ to changes in $I_{CO}$:
$$S = \frac{\partial I_C}{\partial I_{CO}} = (1 + \beta) \cdot \frac{R_{th} + R_E}{R_{th} + (1 + \beta) R_E} = (1 + \beta) \cdot \frac{1 + R_{th}/R_E}{1 + \beta + R_{th}/R_E}$$
- If $R_{th} / R_E \to \infty$ (Fixed Bias without $R_E$): $S = 1 + \beta$ (worst stability, highly prone to thermal runaway).
- If $R_{th} / R_E \ll 1$ (Stiff Voltage Divider Bias): $S \to 1$ (ideal theoretical stability; $I_C$ is completely immune to transistor variations).
Engineering Rule of Thumb for Stiff Bias: Select $R_2 \le 0.1 \beta R_E$ and $V_E = I_E R_E \approx 0.1 \text{ to } 0.2 V_{CC}$.

3. Small-Signal CE Amplifier Analysis ($r_e$ and $h$-Parameter Models):
For small AC perturbations around the $Q$-point, the transistor is replaced by its small-signal $r_e$ equivalent model:
- Dynamic emitter resistance: $r_e = \frac{V_T}{I_{EQ}} \approx \frac{26\text{ mV}}{I_{EQ}}$
- Transconductance: $g_m = \frac{I_{CQ}}{V_T} = \frac{\beta}{r_\pi} = \frac{1}{r_e}$
- Input base resistance: $r_\pi = \beta r_e = h_{ie}$

Small-Signal Performance Parameters (with fully bypassed emitter capacitor $C_E$):
1. Input Impedance ($Z_{in}$):
   $$Z_{in} = R_1 \parallel R_2 \parallel r_\pi = R_{th} \parallel (\beta r_e)$$
2. Output Impedance ($Z_o$):
   $$Z_o = R_C \parallel r_o \approx R_C$$
3. Voltage Gain ($A_v$):
   The output AC voltage across load $R_L$ is $v_o = -i_c (R_C \parallel R_L) = -g_m v_{be} (R_C \parallel R_L)$.
   Since $v_{in} = v_{be}$:
   $$A_v = \frac{v_o}{v_{in}} = -g_m (R_C \parallel R_L) = -\frac{R_C \parallel R_L}{r_e}$$
   The negative sign denotes an intrinsic $180^\circ$ phase inversion between input and output voltages.
4. Current Gain ($A_i$):
   $$A_i = \frac{i_o}{i_{in}} = A_v \cdot \frac{Z_{in}}{R_L}$$

Frequency Response of CE Amplifier:
- Low-Frequency Roll-Off: Caused by input coupling capacitor $C_{in}$, output coupling capacitor $C_{out}$, and emitter bypass capacitor $C_E$. Cutoff frequencies:
  $$f_{L,in} = \frac{1}{2\pi (R_s + Z_{in}) C_{in}}, \quad f_{L,E} = \frac{1}{2\pi R_e' C_E}$$
- High-Frequency Roll-Off: Caused by internal parasitic junction capacitances (base-emitter capacitance $C_\pi$ and collector-base capacitance $C_\mu$).
  According to Miller's Theorem, feedback capacitance $C_\mu$ connected between base and collector is reflected into the input port as an enlarged equivalent capacitance:
  $$C_{M,in} = C_\mu (1 - A_v) = C_\mu (1 + |A_v|)$$
  Upper Cutoff Frequency:
  $$f_H = \frac{1}{2\pi R_{sig}' (C_\pi + C_{M,in})}$$
The Gain-Bandwidth Product (GBW) remains constant: $GBW = |A_{v,mid}| \cdot BW = f_T = \frac{g_m}{2\pi (C_\pi + C_\mu)}$.
"""
            },
            {
                "qid": "comp-q19",
                "marks": 7,
                "type": "Derivation",
                "title": "Operational Amplifiers: Ideal Characteristics, Inverting/Non-Inverting, and Instrumentation Amplifier",
                "yt_query": "operational amplifier virtual ground inverting non inverting instrumentation amplifier derivation",
                "img_path": "images/comp/opamp_circuits_instrumentation.png",
                "img_caption": "Figure 4.3: Practical Integrator and Three-Op-Amp Instrumentation Amplifier Circuit Schematics",
                "answer": r"""
The operational amplifier (Op-Amp) is a high-gain, direct-coupled differential amplifier capable of processing signals from DC up to several megahertz.

1. Ideal vs Practical Op-Amp Characteristics:
An ideal Op-Amp possesses the following theoretical specifications:
- Open-Loop Differential Voltage Gain: $A_{OL} = \infty$ (practical IC 741: $\sim 2 \times 10^5$ or $106\text{ dB}$)
- Input Impedance: $R_{in} = \infty$ (practical: $2\text{ M}\Omega$ for BJT, $10^{12}\Omega$ for FET inputs)
- Output Impedance: $R_o = 0$ (practical: $\sim 75\,\Omega$)
- Bandwidth: $BW = \infty$ (practical: unity gain frequency $f_T \approx 1\text{ MHz}$)
- Common Mode Rejection Ratio: $CMRR = \infty$ (practical: $\sim 90\text{ dB}$)
- Slew Rate: $SR = \infty$ (practical: $0.5\text{ V/}\mu\text{s}$)
- Input Offset Voltage and Currents: $V_{os} = 0, I_{os} = 0$

Concept of Virtual Ground and Virtual Short:
Because the open-loop gain is exceedingly large ($A_{OL} \to \infty$), in any stable negative feedback configuration where the output remains unsaturated:
$$V_o = A_{OL} (V^+ - V^-) \implies V^+ - V^- = \frac{V_o}{A_{OL}} \to 0 \implies V^+ = V^-$$
This is the Virtual Short concept. If the non-inverting terminal ($V^+$) is connected to electrical ground ($V^+ = 0\text{ V}$), then the inverting terminal is constrained to remain at ground potential ($V^- = 0\text{ V}$) without being physically wired to ground; this condition is termed Virtual Ground. Furthermore, because $R_{in} = \infty$, no current enters either input terminal ($I^+ = I^- = 0$).

2. Fundamental Op-Amp Circuit Configurations:

Inverting Amplifier:
Input $v_{in}$ connects through $R_1$ to the inverting pin; feedback resistor $R_f$ connects output to inverting pin. Non-inverting pin is grounded ($V^+ = 0 \implies V^- = 0$).
Applying KCL at the inverting node:
$$\frac{v_{in} - 0}{R_1} + \frac{v_o - 0}{R_f} = 0 \implies \frac{v_{in}}{R_1} = -\frac{v_o}{R_f}$$
$$A_v = \frac{v_o}{v_{in}} = -\frac{R_f}{R_1}$$
Input impedance is $Z_{in} = R_1$.

Non-Inverting Amplifier:
Input $v_{in}$ is applied directly to non-inverting pin ($V^+ = v_{in}$).
By virtual short: $V^- = V^+ = v_{in}$.
The feedback network $(R_1, R_f)$ forms a voltage divider from $v_o$:
$$V^- = v_o \left( \frac{R_1}{R_1 + R_f} \right) = v_{in}$$
$$A_v = \frac{v_o}{v_{in}} = \frac{R_1 + R_f}{R_1} = 1 + \frac{R_f}{R_1}$$
For $R_f = 0, R_1 = \infty$: $A_v = 1$ (Voltage Follower / Unity-Gain Buffer), providing infinite input impedance and zero output impedance.

Summing Amplifier:
Multiple input voltages ($v_1, v_2, v_3$) connected through resistors ($R_1, R_2, R_3$) to the inverting virtual ground node:
$$v_o = -\left( \frac{R_f}{R_1} v_1 + \frac{R_f}{R_2} v_2 + \frac{R_f}{R_3} v_3 \right)$$

Practical Integrator vs Practical Differentiator:
- Practical Integrator (Lossy Integrator):
  An ideal integrator uses a capacitor $C_f$ in the feedback loop: $v_o(t) = -\frac{1}{R_1 C_f}\int v_{in}(t) dt$. At DC ($\omega \to 0$), the capacitor is an open circuit ($X_C \to \infty$), causing open-loop gain to approach $A_{OL}$, which drives the Op-Amp into rail saturation due to tiny input DC offset voltages.
  Solution: Place a large resistor $R_f$ in parallel with $C_f$. At DC, the gain is stabilized to $-R_f / R_1$. The circuit acts as an active low-pass filter with corner frequency $f_c = \frac{1}{2\pi R_f C_f}$; true mathematical integration occurs for operating frequencies $f \gg f_c$.
- Practical Differentiator:
  An ideal differentiator uses an input series capacitor $C_1$: $v_o(t) = -R_f C_1 \frac{dv_{in}}{dt}$. Because gain increases at $+20\text{ dB/decade}$ with frequency, it amplifies high-frequency noise and tends toward instability.
  Solution: Add a small series resistor $R_1$ in the input path and a small capacitor $C_f$ in parallel with $R_f$ to roll off the gain at high frequencies.

3. Three-Op-Amp Instrumentation Amplifier:
In biomedical and industrial instrumentation, transducer sensor signals are minute differential voltages ($V_2 - V_1 \sim \text{mV}$) superimposed on massive common-mode noise ($V_{cm} \sim \text{Volts}$). The 3-Op-Amp instrumentation amplifier delivers high differential gain, high CMRR ($> 100\text{ dB}$), and high input impedance on both terminals.

Architecture:
- Input Stage: Two non-inverting buffer Op-Amps ($A_1, A_2$) cross-coupled through feedback resistors $R_1, R_1$ and a single common gain-setting resistor $R_{gain}$.
- Output Stage: A standard differential amplifier Op-Amp ($A_3$) with matched resistors $R_2, R_2$ and $R_3, R_3$.

Derivation of Overall Voltage Gain:
Let input voltages be $v_1$ (at Op-Amp $A_1$) and $v_2$ (at Op-Amp $A_2$).
By the virtual short principle:
$$V_1^- = v_1, \quad V_2^- = v_2$$
The current flowing through the gain resistor $R_{gain}$ from node 1 to node 2 is:
$$I = \frac{v_1 - v_2}{R_{gain}}$$
Since no current enters Op-Amp input terminals, the identical current $I$ must flow through both feedback resistors $R_1$:
$$v_{o1} = v_1 + I R_1 = v_1 + \frac{v_1 - v_2}{R_{gain}} R_1$$
$$v_{o2} = v_2 - I R_1 = v_2 - \frac{v_1 - v_2}{R_{gain}} R_1$$
The differential output voltage of the first stage is:
$$v_{o1} - v_{o2} = (v_1 - v_2) + 2 \left( \frac{v_1 - v_2}{R_{gain}} \right) R_1 = (v_1 - v_2) \left[ 1 + \frac{2 R_1}{R_{gain}} \right]$$
Notice that for a common-mode signal ($v_1 = v_2 = v_{cm}$), the current $I = 0$, meaning the first stage provides unity gain ($A_{cm1} = 1$) for common-mode signals while heavily amplifying the differential signal by $\left(1 + \frac{2 R_1}{R_{gain}}\right)$.

The second stage ($A_3$) is a balanced differential subtractor:
$$v_o = \frac{R_3}{R_2} (v_{o2} - v_{o1}) = -\frac{R_3}{R_2} (v_{o1} - v_{o2})$$
In terms of $(v_2 - v_1)$:
$$v_o = \left[ 1 + \frac{2 R_1}{R_{gain}} \right] \left( \frac{R_3}{R_2} \right) (v_2 - v_1)$$
Advantages of Instrumentation Amplifier:
1. High input impedance ($> 10^{10}\,\Omega$) on both differential inputs, preventing loading of high-impedance transducers (e.g., strain gauges, thermocouples, ECG electrodes).
2. Differential gain can be precisely tuned using a single external potentiometer $R_{gain}$ without disturbing circuit resistor matching.
3. Common mode signals undergo zero amplification in stage 1, resulting in outstanding Common Mode Rejection Ratio (CMRR).
"""
            },
            {
                "qid": "comp-q20",
                "marks": 7,
                "type": "Derivation",
                "title": "IC 555 Timer: Internal Block Diagram, Astable & Monostable Multivibrators",
                "yt_query": "555 timer internal architecture astable monostable multivibrator derivation frequency duty cycle",
                "img_path": "images/comp/timer_555_circuits.png",
                "img_caption": "Figure 4.4: Functional Block Diagram of IC 555 Timer and Astable Multivibrator Capacitor Voltage Waveforms",
                "answer": r"""
The IC 555 timer is a versatile monolithic timing circuit capable of generating precise time delays, clock pulses, and pulse-width modulated waveforms.

1. Internal Functional Block Architecture:
The standard 8-pin IC 555 package integrates the following internal blocks:
1. Precision Voltage Divider: Three identical $5\text{ k}\Omega$ resistors connected in series between $V_{CC}$ (Pin 8) and Ground (Pin 1), establishing two internal reference voltages:
   - Upper Reference Voltage: $V_{ref1} = \frac{2}{3} V_{CC}$ (connected to inverting terminal of Upper Comparator).
   - Lower Reference Voltage: $V_{ref2} = \frac{1}{3} V_{CC}$ (connected to non-inverting terminal of Lower Comparator).
2. Upper (Threshold) Comparator: Compares Threshold input (Pin 6) with $\frac{2}{3} V_{CC}$. If $V_{\text{pin 6}} > \frac{2}{3} V_{CC}$, its output goes HIGH, Setting the internal latch (or Resetting the SR flip-flop).
3. Lower (Trigger) Comparator: Compares Trigger input (Pin 2) with $\frac{1}{3} V_{CC}$. If $V_{\text{pin 2}} < \frac{1}{3} V_{CC}$, its output goes HIGH, Setting the SR flip-flop.
4. SR Flip-Flop: Stores the comparator state. An active-low external Reset (Pin 4) can override the flip-flop to force the output LOW.
5. Discharge Transistor ($Q_1$): An internal NPN transistor whose collector is brought out to Pin 7. When flip-flop output $\bar{Q}$ is HIGH, $Q_1$ is driven into saturation, clamping Pin 7 to ground and discharging the external timing capacitor.
6. Output Driver Stage: A high-current totem-pole output buffer (Pin 3) capable of sourcing or sinking up to $200\text{ mA}$ of load current. Pin 5 (Control Voltage) accesses the $\frac{2}{3} V_{CC}$ node, bypassed by a $0.01\,\mu\text{F}$ capacitor to ground for noise immunity.

2. Astable Multivibrator (Free-Running Square-Wave Oscillator):
In the astable configuration, Pins 2 (Trigger) and 6 (Threshold) are tied together and connected to timing capacitor $C$. Resistor $R_A$ is connected between $V_{CC}$ and Pin 7; resistor $R_B$ is connected between Pin 7 and Pin 6/2.

Operating Cycle:
1. Charging Phase (Output HIGH, $Q_1$ OFF):
   Capacitor $C$ charges from $\frac{1}{3} V_{CC}$ to $\frac{2}{3} V_{CC}$ through $(R_A + R_B)$ from supply $V_{CC}$.
   The instantaneous capacitor voltage is governed by:
   $$v_C(t) = V_f - (V_f - V_i) e^{-\frac{t}{\tau_1}}$$
   where $V_f = V_{CC}$, $V_i = \frac{1}{3} V_{CC}$, and $\tau_1 = (R_A + R_B) C$.
   $$v_C(t) = V_{CC} - \left( V_{CC} - \frac{1}{3} V_{CC} \right) e^{-\frac{t}{\tau_1}} = V_{CC} \left[ 1 - \frac{2}{3} e^{-\frac{t}{\tau_1}} \right]$$
   Setting $v_C(t_H) = \frac{2}{3} V_{CC}$:
   $$\frac{2}{3} V_{CC} = V_{CC} \left[ 1 - \frac{2}{3} e^{-\frac{t_H}{\tau_1}} \right] \implies \frac{2}{3} e^{-\frac{t_H}{\tau_1}} = \frac{1}{3} \implies e^{-\frac{t_H}{\tau_1}} = \frac{1}{2}$$
   $$t_H = \tau_1 \ln 2 = (R_A + R_B) C \ln 2 \approx 0.693 (R_A + R_B) C$$

2. Discharging Phase (Output LOW, $Q_1$ ON):
   When $v_C$ reaches $\frac{2}{3} V_{CC}$, the upper comparator triggers the flip-flop, driving output LOW and turning ON discharge transistor $Q_1$. Capacitor $C$ discharges through $R_B$ toward ground potential ($0\text{ V}$).
   Here $V_f = 0\text{ V}$, $V_i = \frac{2}{3} V_{CC}$, and $\tau_2 = R_B C$.
   $$v_C(t) = 0 - \left( 0 - \frac{2}{3} V_{CC} \right) e^{-\frac{t}{\tau_2}} = \frac{2}{3} V_{CC} e^{-\frac{t}{\tau_2}}$$
   The discharge continues until $v_C$ falls to $\frac{1}{3} V_{CC}$:
   $$\frac{1}{3} V_{CC} = \frac{2}{3} V_{CC} e^{-\frac{t_L}{\tau_2}} \implies e^{-\frac{t_L}{\tau_2}} = \frac{1}{2}$$
   $$t_L = \tau_2 \ln 2 = R_B C \ln 2 \approx 0.693 R_B C$$

Total Oscillation Period and Frequency:
$$T = t_H + t_L = 0.693 (R_A + R_B) C + 0.693 R_B C = 0.693 (R_A + 2 R_B) C$$
The oscillation frequency is:
$$f = \frac{1}{T} = \frac{1}{0.693 (R_A + 2 R_B) C} = \frac{1.44}{(R_A + 2 R_B) C} \quad \text{Hz}$$

Duty Cycle ($D$):
$$D = \frac{t_H}{T} \times 100\% = \frac{R_A + R_B}{R_A + 2 R_B} \times 100\%$$
Because $R_A > 0$, $D$ is strictly $> 50\%$ in the standard circuit. To obtain an exact $50\%$ symmetrical square wave (or $D < 50\%$), a diode $D_1$ is connected in parallel with $R_B$ (anode to Pin 7, cathode to Pin 6), bypassing $R_B$ during charging ($t_H = 0.693 R_A C, t_L = 0.693 R_B C$).

3. Monostable Multivibrator (One-Shot Pulse Generator):
In monostable mode, Pin 2 (Trigger) is normally held HIGH at $V_{CC}$ via an external pull-up resistor. Pin 7 and Pin 6 are tied together and connected to timing resistor $R_A$ and capacitor $C$.
- Quiescent State: Output is LOW, transistor $Q_1$ is ON, holding $v_C \approx 0\text{ V}$.
- Triggering: A narrow negative trigger pulse ($< \frac{1}{3} V_{CC}$) applied to Pin 2 forces the lower comparator HIGH, Setting the flip-flop:
  - Output (Pin 3) transitions HIGH.
  - Transistor $Q_1$ turns OFF, allowing capacitor $C$ to charge from $V_{CC}$ through $R_A$.
- Charging Equation:
  $$v_C(t) = V_{CC} \left( 1 - e^{-\frac{t}{R_A C}} \right)$$
  When $v_C$ reaches $\frac{2}{3} V_{CC}$, the upper comparator fires, resetting the flip-flop:
  $$\frac{2}{3} V_{CC} = V_{CC} \left( 1 - e^{-\frac{T}{R_A C}} \right) \implies e^{-\frac{T}{R_A C}} = \frac{1}{3}$$
  $$T = R_A C \ln 3 \approx 1.1 R_A C \quad \text{seconds}$$
The circuit returns to its stable LOW state until another trigger pulse arrives. Output pulse duration $T = 1.1 R_A C$ is independent of supply voltage $V_{CC}$.
"""
            },
            {
                "qid": "comp-q21",
                "marks": 7,
                "type": "Analytical",
                "title": "Digital Electronics: Boolean Theorems, K-Maps, Adders, MUX, and Counters Design",
                "yt_query": "boolean algebra k-map full adder multiplexer synchronous counter design jk flip-flop",
                "img_path": "images/comp/digital_logic_circuits.png",
                "img_caption": "Figure 4.5: Full Adder Gate Architecture and 3-Bit Synchronous Binary Up-Counter Circuit Diagram",
                "answer": r"""
Digital systems manipulate discrete binary information using combinational and sequential logic structures built from fundamental semiconductor logic gates.

1. Boolean Algebra & De Morgan's Theorems:
Fundamental Postulates:
- Identity: $A + 0 = A, \quad A \cdot 1 = A$
- Null Element: $A + 1 = 1, \quad A \cdot 0 = 0$
- Idempotent: $A + A = A, \quad A \cdot A = A$
- Involution: $\overline{\overline{A}} = A$
- Complementarity: $A + \bar{A} = 1, \quad A \cdot \bar{A} = 0$
- Distributive: $A + (B \cdot C) = (A + B)(A + C), \quad A \cdot (B + C) = A B + A C$

De Morgan's Theorems:
1. The complement of a logical sum equals the logical product of the complements:
   $$\overline{A + B} = \bar{A} \cdot \bar{B} \quad \implies \quad \overline{\sum_{i=1}^n X_i} = \prod_{i=1}^n \bar{X}_i$$
2. The complement of a logical product equals the logical sum of the complements:
   $$\overline{A \cdot B} = \bar{A} + \bar{B} \quad \implies \quad \overline{\prod_{i=1}^n X_i} = \sum_{i=1}^n \bar{X}_i$$

2. Karnaugh Map (K-Map) Minimization:
The Karnaugh Map organizes minterms in a Gray-code sequence ($00, 01, 11, 10$) such that adjacent cells differ by only one binary variable.
Rules for 4-Variable K-Map Minimization:
1. Identify all 1s (and 'don't care' conditions $d$ where advantageous).
2. Form the largest possible adjacent groups in powers of two: single cells ($2^0$), pairs ($2^1$, eliminates 1 variable), quads ($2^2$, eliminates 2 variables), octets ($2^3$, eliminates 3 variables), or full map ($2^4 = 1$).
3. Exploit wrap-around adjacency between top/bottom rows and leftmost/rightmost columns.
4. Ensure all prime implicants covering unique $1$s are essential prime implicants to obtain the minimal Sum of Products (SOP) expression.

3. Combinational Building Blocks:

Full Adder Design:
A Full Adder adds two operand bits ($A, B$) and an incoming carry bit ($C_{in}$), producing a Sum ($S$) and Carry Out ($C_{out}$).
- Truth Table Analysis:
  - $S$ is HIGH when an odd number of inputs are HIGH:
    $$S = A \oplus B \oplus C_{in}$$
  - $C_{out}$ is HIGH when any two or more inputs are HIGH:
    $$C_{out} = A B + B C_{in} + A C_{in} = A B + C_{in}(A \oplus B)$$
Implementation using two Half Adders and one OR gate (or 9 universal NAND gates).

4:1 Multiplexer (Data Selector):
Routes one of four data input lines ($I_0, I_1, I_2, I_3$) to a single output line $Y$ based on two select inputs ($S_1, S_0$):
$$Y = \bar{S}_1 \bar{S}_0 I_0 + \bar{S}_1 S_0 I_1 + S_1 \bar{S}_0 I_2 + S_1 S_0 I_3$$
Demultiplexer (1:4) performs the exact inverse operation, taking a single data input and routing it to one of four output channels.

4. Sequential Logic & Flip-Flop Fundamentals:
While combinational circuits depend only on current inputs, sequential circuits possess memory, depending on past states.

Clocked JK Flip-Flop & Race-Around Condition:
Characteristic equation:
$$Q_{next} = J \bar{Q} + \bar{K} Q$$
- The Race-Around Condition:
  Occurs in level-triggered JK flip-flops when $J = K = 1$. The flip-flop is in toggle mode ($Q \to \bar{Q}$). If the clock pulse width $t_p$ exceeds the propagation delay $t_{pd}$ of the logic gates ($t_p > t_{pd}$), the output toggles back and forth uncontrollably multiple times during a single clock pulse, leaving the final output indeterminate at the clock trailing edge.
- Solutions:
  1. Use edge-triggered flip-flops (narrow trigger spikes $\Delta t < t_{pd}$).
  2. Master-Slave JK Flip-Flop Architecture: Composed of two cascaded latches. The Master responds to $J, K$ on the clock HIGH level while the Slave is disabled. On the clock negative edge, the Master is isolated and transfers its state to the Slave, preventing internal feedback races.

5. Design of a 3-Bit Synchronous Binary Up-Counter:
Unlike asynchronous (ripple) counters where clock propagation delay accumulates ($t_{delay} = n \cdot t_{pd}$), a synchronous counter connects the external clock simultaneously to all flip-flops, eliminating clock skew and glitch states.

Design Specification: Counts cyclically $000 \to 001 \to 010 \to 011 \to 100 \to 101 \to 110 \to 111 \to 000$.
Flip-Flops required: $N = 3$ JK flip-flops ($FF_0, FF_1, FF_2$ representing bits $Q_0, Q_1, Q_2$, where $Q_0$ is LSB).

JK Flip-Flop Excitation Table:
- Transition $0 \to 0$: $J = 0, K = X$
- Transition $0 \to 1$: $J = 1, K = X$
- Transition $1 \to 0$: $J = X, K = 1$
- Transition $1 \to 1$: $J = X, K = 0$

Counter State Transition and Excitation Synthesis:
State transitions $(Q_2 Q_1 Q_0)_{present} \to (Q_2 Q_1 Q_0)_{next}$:
- $000 \to 001$: $FF_0(0\to 1 \implies J_0=1, K_0=X); FF_1(0\to 0 \implies J_1=0, K_1=X); FF_2(0\to 0 \implies J_2=0, K_2=X)$
- $001 \to 010$: $FF_0(1\to 0 \implies J_0=X, K_0=1); FF_1(0\to 1 \implies J_1=1, K_1=X); FF_2(0\to 0 \implies J_2=0, K_2=X)$
- $010 \to 011$: $FF_0(0\to 1 \implies J_0=1, K_0=X); FF_1(1\to 1 \implies J_1=X, K_1=0); FF_2(0\to 0 \implies J_2=0, K_2=X)$
- $011 \to 100$: $FF_0(1\to 0 \implies J_0=X, K_0=1); FF_1(1\to 0 \implies J_1=X, K_1=1); FF_2(0\to 1 \implies J_2=1, K_2=X)$
- $100 \to 101$: $FF_0(0\to 1 \implies J_0=1, K_0=X); FF_1(0\to 0 \implies J_1=0, K_1=X); FF_2(1\to 1 \implies J_2=X, K_2=0)$
- $101 \to 110$: $FF_0(1\to 0 \implies J_0=X, K_0=1); FF_1(0\to 1 \implies J_1=1, K_1=X); FF_2(1\to 1 \implies J_2=X, K_2=0)$
- $110 \to 111$: $FF_0(0\to 1 \implies J_0=1, K_0=X); FF_1(1\to 1 \implies J_1=X, K_1=0); FF_2(1\to 1 \implies J_2=X, K_2=0)$
- $111 \to 000$: $FF_0(1\to 0 \implies J_0=X, K_0=1); FF_1(1\to 0 \implies J_1=X, K_1=1); FF_2(1\to 0 \implies J_2=X, K_2=1)$

K-Map Minimization for Flip-Flop Inputs:
- For $FF_0$ (LSB):
  $J_0 = 1, \quad K_0 = 1$
  (Toggles on every single clock pulse).
- For $FF_1$:
  $J_1 = Q_0, \quad K_1 = Q_0$
  (Toggles whenever $Q_0 = 1$).
- For $FF_2$ (MSB):
  $J_2 = Q_1 Q_0, \quad K_2 = Q_1 Q_0$
  (Toggles whenever both $Q_0 = 1$ and $Q_1 = 1$).

Circuit Implementation:
- Connect common clock signal $CLK$ to the clock input of all three JK flip-flops.
- Set $J_0 = K_0 = 1$ (tied to $+V_{CC}$).
- Connect output $Q_0$ directly to inputs $J_1$ and $K_1$ of $FF_1$.
- Connect output $Q_0$ and $Q_1$ to an AND gate; connect the AND gate output ($Q_0 \cdot Q_1$) to inputs $J_2$ and $K_2$ of $FF_2$.
This achieves synchronous high-speed counting up to the maximum toggle frequency of the flip-flops.
"""
            }
        ]
    },
    {
        "module_id": "comp-m5",
        "module_num": "Module 5",
        "module_title": "Power Electronics & Electric Drives",
        "questions": [
            {
                "qid": "comp-q22",
                "marks": 7,
                "type": "Descriptive",
                "title": "Power Semiconductor Devices: SCR Two-Transistor Model, MOSFET, and IGBT",
                "yt_query": "power semiconductor devices scr two transistor analogy mosfet igbt comparison",
                "img_path": "images/comp/power_devices_scr_igbt.png",
                "img_caption": "Figure 5.1: SCR Static V-I Characteristics, Two-Transistor Analogy, and IGBT Cross-Sectional Architecture",
                "answer": r"""
Power semiconductor switching devices are the foundational building blocks of modern power electronic converters, designed to switch megawatts of power with high efficiency, fast response, and minimal forward voltage drops.

1. Silicon Controlled Rectifier (SCR):
The SCR is a four-layer ($P_1-N_1-P_2-N_2$), three-junction ($J_1, J_2, J_3$), three-terminal (Anode $A$, Cathode $K$, Gate $G$) bistable thyristor device.

Static $V-I$ Operating Characteristics:
- Forward Blocking Mode ($V_{AK} > 0, I_g = 0$): Outer junctions $J_1$ and $J_3$ are forward-biased, but middle junction $J_2$ is reverse-biased. The device blocks forward voltage up to the Forward Breakover Voltage $V_{BO}$, conducting only a tiny forward leakage current.
- Forward Conduction Mode: When $V_{AK}$ exceeds $V_{BO}$, or when a positive gate current pulse $I_g$ is injected into junction $J_2$, junction $J_2$ breaks down through regenerative carrier multiplication. The device collapses into a high-conduction ON state with a negligible forward voltage drop ($V_{on} \approx 1.0-1.5\text{ V}$).
- Reverse Blocking Mode ($V_{AK} < 0$): Junctions $J_1$ and $J_3$ are reverse-biased, while $J_2$ is forward-biased. The device blocks reverse voltage until reaching the Reverse Breakdown Voltage $V_{BR}$, beyond which catastrophic thermal breakdown occurs.

Two-Transistor Analogy of SCR:
The $P-N-P-N$ structure can be modeled as two cross-coupled complementary bipolar transistors:
- A PNP transistor $Q_1$ (emitter $P_1$, base $N_1$, collector $P_2$) with common-base current gain $\alpha_1$.
- An NPN transistor $Q_2$ (collector $N_1$, base $P_2$, emitter $N_2$) with common-base current gain $\alpha_2$.

Derivation of Anode Current $I_A$:
Collector current of $Q_1$:
$$I_{C1} = \alpha_1 I_A + I_{CBO1}$$
Collector current of $Q_2$:
$$I_{C2} = \alpha_2 I_K + I_{CBO2}$$
where $I_K = I_A + I_g$ is cathode current, and $I_{CBO1}, I_{CBO2}$ are reverse collector-base leakage currents.
From the physical node geometry, the anode current entering junction $J_2$ equals the sum of both collector currents:
$$I_A = I_{C1} + I_{C2} = \alpha_1 I_A + I_{CBO1} + \alpha_2 (I_A + I_g) + I_{CBO2}$$
$$I_A [1 - (\alpha_1 + \alpha_2)] = \alpha_2 I_g + (I_{CBO1} + I_{CBO2})$$
$$I_A = \frac{\alpha_2 I_g + I_{CBO1} + I_{CBO2}}{1 - (\alpha_1 + \alpha_2)}$$

Regenerative Turn-On Condition:
At low currents, current gains $\alpha_1$ and $\alpha_2$ are small ($\alpha_1 + \alpha_2 \ll 1$), keeping $I_A$ at leakage levels.
When gate current $I_g$ is injected, emitter currents increase, raising both $\alpha_1$ and $\alpha_2$.
As $(\alpha_1 + \alpha_2) \to 1$, the denominator $[1 - (\alpha_1 + \alpha_2)] \to 0$, causing internal regenerative loop gain to become unity ($G_{loop} \ge 1$). Anode current escalates instantaneously toward an externally circuit-limited value; junction $J_2$ becomes flooded with carriers, and the gate permanently loses control.

Key SCR Operational Parameters:
- Latching Current ($I_L$): The minimum anode current that must be established during gate triggering for the SCR to remain in the ON state after the gate trigger pulse is completely removed ($I_L \approx 2 \text{ to } 3 I_H$).
- Holding Current ($I_H$): The minimum anode current below which the SCR automatically turns OFF and reverts to the forward blocking state.
- $di/dt$ Protection: High rate of current rise can cause localized current filamentation near the gate pad before carrier plasma spreads across the silicon die, causing hot-spot destruction. Protection: A small series inductor ($L_s$).
- $dv/dt$ Protection: High rate of voltage rise across $J_2$ induces a displacement charging current $i = C_{j2} \frac{dv}{dt}$ that can false-trigger the SCR. Protection: An RC snubber circuit connected across anode and cathode.

2. Power MOSFET:
- Physical Structure: Vertical Double-Diffused MOS (VDMOS) structure with majority carrier electron flow from source to drain through an induced $N$-channel.
- Key Characteristics:
  - Unipolar majority-carrier device: Zero minority-carrier storage delay, enabling ultra-fast switching frequencies (hundreds of $\text{kHz}$ to several $\text{MHz}$).
  - Voltage-Controlled Gate: Insulated oxide gate ($SiO_2$) draws negligible steady-state drive power ($I_G \approx 0$).
  - Positive Temperature Coefficient of On-State Resistance ($R_{DS(on)}$): As die temperature rises, carrier mobility drops, increasing $R_{DS(on)}$. This prevents current hogging and thermal runaway, making MOSFETs straightforward to parallel directly.
  - Conduction losses scale quadratically with voltage rating ($R_{DS(on)} \propto V_{BR}^{2.5}$), limiting pure power MOSFETs to lower voltage applications ($< 600\text{ V}$).

3. Insulated Gate Bipolar Transistor (IGBT):
- Physical Structure: A hybrid three-terminal device integrating an insulated MOS gate input structure with a four-layer bipolar output structure ($P^+ \text{ substrate} - N^+ \text{ buffer} - N^- \text{ drift} - P \text{ well} - N^+ \text{ emitter}$).
- Operating Principle:
  Applying a positive gate-to-emitter voltage ($V_{GE} > V_{GE(th)}$) inverts the $P$-well to form an electron channel, supplying base current to an internal wide-base PNP bipolar transistor. The $P^+$ substrate injects high densities of minority carrier holes into the lightly doped $N^-$ drift region, causing dramatic Conductivity Modulation.
- Key Advantages:
  - Voltage-controlled input: Requires simple, low-power gate drive circuitry identical to a MOSFET.
  - Low on-state conduction drop: Conductivity modulation suppresses drift region resistance, achieving low saturation voltage ($V_{CE(sat)} \approx 1.5 - 2.5\text{ V}$) even at kilovolt ratings ($1.2\text{ kV} - 6.5\text{ kV}$).
  - Current tailing during turn-off: Recombination of stored minority carriers in the open-base PNP structure causes a current tail, limiting switching frequencies to $20 - 50\text{ kHz}$.

Comprehensive Device Comparison Table:
| Parameter | Thyristor (SCR) | Power MOSFET | IGBT |
| :--- | :--- | :--- | :--- |
| **Control Principle** | Current pulse triggered (Latching) | Voltage-controlled ($V_{GS}$) | Voltage-controlled ($V_{GE}$) |
| **Carrier Type** | Bipolar (electrons & holes) | Unipolar (majority electrons) | Hybrid (bipolar output + MOS input) |
| **Voltage Rating** | Ultra-high ($> 10\text{ kV}$) | Medium ($< 600\text{ V}$) | High ($600\text{ V} - 6.5\text{ kV}$) |
| **Current Rating** | Ultra-high ($> 5000\text{ A}$) | Low-to-Medium ($< 100\text{ A}$) | High ($> 1000\text{ A}$) |
| **Switching Frequency** | Slow ($< 1\text{ kHz}$) | Very Fast ($100\text{ kHz} - 2\text{ MHz}$) | Fast ($10\text{ kHz} - 50\text{ kHz}$) |
| **On-State Drop** | Very low ($1.0 - 1.5\text{ V}$) | High at high voltages ($I_D R_{DS(on)}$) | Low ($1.5 - 2.5\text{ V}$) |
| **Drive Power** | Continuous current pulse required | Negligible (capacitive charging only) | Negligible (capacitive charging only) |
| **Primary Domain** | HVDC, heavy rolling mills | SMPS, RF generators, EV chargers | Traction drives, industrial inverters, wind/solar |
"""
            },
            {
                "qid": "comp-q23",
                "marks": 7,
                "type": "Derivation",
                "title": "Phase-Controlled Rectifiers: 1-Phase & 3-Phase Converters with R and RL Loads",
                "yt_query": "phase controlled rectifier single phase three phase average output voltage derivation continuous conduction",
                "img_path": "images/comp/phase_controlled_rectifiers.png",
                "img_caption": "Figure 5.2: Single-Phase and Three-Phase Fully-Controlled Bridge Converter Waveforms and Two-Quadrant Operating Plane",
                "answer": r"""
Phase-controlled rectifiers convert single-phase or three-phase AC mains voltage into variable DC output voltage by delaying the conduction angle (firing angle $\alpha$) of thyristors relative to the natural AC zero-crossings.

1. Single-Phase Fully-Controlled Bridge Converter:
The converter comprises four thyristors ($T_1, T_2, T_3, T_4$) arranged in a bridge.
- Thyristor pairs $(T_1, T_2)$ are fired simultaneously at $\omega t = \alpha$ during the positive half-cycle.
- Thyristor pairs $(T_3, T_4)$ are fired simultaneously at $\omega t = \pi + \alpha$ during the negative half-cycle.
Input voltage: $v_s(t) = V_m \sin\omega t$.

Case A: Pure Resistive Load (R-Load):
Current ceases whenever input voltage drops to zero:
Conduction interval is from $\alpha$ to $\pi$ for each half-cycle.
Average Output DC Voltage ($V_{dc}$):
$$V_{dc} = \frac{1}{\pi} \int_\alpha^\pi V_m \sin\omega t\,d(\omega t) = \frac{V_m}{\pi} [-\cos\omega t]_\alpha^\pi = \frac{V_m}{\pi} [-\cos\pi - (-\cos\alpha)]$$
$$V_{dc} = \frac{V_m}{\pi} (1 + \cos\alpha)$$
RMS Output Voltage ($V_{rms}$):
$$V_{rms} = \sqrt{\frac{1}{\pi} \int_\alpha^\pi V_m^2 \sin^2\omega t\,d(\omega t)} = \frac{V_m}{\sqrt{2}} \sqrt{1 - \frac{\alpha}{\pi} + \frac{\sin 2\alpha}{2\pi}}$$

Case B: Highly Inductive RL Load (Continuous Conduction Mode):
Due to large load inductance $L$, the load current $I_o$ remains continuous, ripple-free, and smooth ($I_o \approx I_{dc} = \text{constant}$).
When supply voltage crosses zero at $\omega t = \pi$ and goes negative, the inductive EMF of the load forces thyristor pair $(T_1, T_2)$ to remain conducting into the negative voltage region until the next pair $(T_3, T_4)$ is gated at $\omega t = \pi + \alpha$.
Conduction interval per half-cycle is exactly $\pi$ radians (from $\alpha$ to $\pi + \alpha$).

Average Output DC Voltage ($V_{dc}$):
$$V_{dc} = \frac{1}{\pi} \int_\alpha^{\pi + \alpha} V_m \sin\omega t\,d(\omega t) = \frac{V_m}{\pi} [-\cos\omega t]_\alpha^{\pi + \alpha} = \frac{V_m}{\pi} [-\cos(\pi + \alpha) - (-\cos\alpha)]$$
Using $\cos(\pi + \alpha) = -\cos\alpha$:
$$V_{dc} = \frac{V_m}{\pi} [\cos\alpha + \cos\alpha] = \frac{2 V_m}{\pi} \cos\alpha$$
RMS Output Voltage ($V_{rms}$):
$$V_{rms} = \sqrt{\frac{1}{\pi} \int_\alpha^{\pi + \alpha} V_m^2 \sin^2\omega t\,d(\omega t)} = \frac{V_m}{\sqrt{2}}$$
The RMS output voltage is entirely independent of firing angle $\alpha$ and equals the AC supply RMS voltage.

Two-Quadrant Converter Operation:
1. Rectification Mode ($0^\circ \le \alpha \le 90^\circ$):
   $\cos\alpha > 0 \implies V_{dc} > 0$. Power flows from AC supply into the DC load ($P_{dc} = V_{dc} I_{dc} > 0$).
2. Inversion Mode ($90^\circ < \alpha < 180^\circ$):
   $\cos\alpha < 0 \implies V_{dc} < 0$. If an external DC source (such as a regenerating DC motor armature) maintains current in the same unidirectional forward direction ($I_{dc} > 0$), net DC power is negative ($P_{dc} < 0$). The converter operates as a line-commutated synchronous inverter, returning kinetic braking energy from the DC machine directly back into the AC supply grid.

Role of Freewheeling Diode (FD):
Connecting a freewheeling diode across the RL load clamps the output voltage at zero whenever $v_s$ goes negative, preventing $v_o$ from becoming negative:
$$V_{dc,FD} = \frac{V_m}{\pi}(1 + \cos\alpha)$$
Benefits of FD:
1. Eliminates negative voltage spikes across load.
2. Dissipates inductive energy within the diode-load loop, preventing load current discontinuities.
3. Improves input displacement factor and power factor.
4. Prevents line-commutated inversion (restricts operation strictly to Quadrant I).

2. Three-Phase Fully-Controlled Bridge Converter (6-Pulse):
The 3-phase full bridge employs 6 thyristors ($T_1, T_3, T_5$ connected to positive DC bus; $T_4, T_6, T_2$ connected to negative DC bus).
- Conduction Sequence: $T_1 \to T_2 \to T_3 \to T_4 \to T_5 \to T_6$.
- Thyristors fire every $60^\circ$ electrical interval. Each thyristor conducts for $120^\circ$.
- Natural commutation reference is at $\omega t = 30^\circ$ ($\pi/6$), where line voltage $v_{ab}$ crosses $v_{ac}$.
- Firing angle $\alpha$ is measured from the natural commutation instant ($\omega t = \pi/6$).

Derivation of Average DC Output Voltage ($V_{dc}$):
Taking line-to-line voltage $v_{ab} = \sqrt{3} V_m \sin(\omega t + \pi/6) = V_{mL} \sin(\omega t + \pi/6)$:
The output voltage repeats every $60^\circ$ ($\pi/3$ radians):
$$V_{dc} = \frac{1}{\pi/3} \int_{\pi/6 + \alpha}^{\pi/2 + \alpha} V_{mL} \sin\left(\omega t + \frac{\pi}{6}\right) d(\omega t)$$
Letting $\theta = \omega t + \frac{\pi}{6}$:
$$V_{dc} = \frac{3}{\pi} \int_{\pi/3 + \alpha}^{2\pi/3 + \alpha} V_{mL} \sin\theta\,d\theta = \frac{3 V_{mL}}{\pi} [-\cos\theta]_{\pi/3 + \alpha}^{2\pi/3 + \alpha}$$
$$V_{dc} = \frac{3 V_{mL}}{\pi} \left[ -\cos\left(\frac{2\pi}{3} + \alpha\right) + \cos\left(\frac{\pi}{3} + \alpha\right) \right]$$
Using trigonometric identity $\cos(A) - \cos(B) = 2 \sin\left(\frac{A+B}{2}\right)\sin\left(\frac{B-A}{2}\right)$:
$$V_{dc} = \frac{3 V_{mL}}{\pi} \left[ 2 \sin\left(\frac{\pi}{2} + \alpha\right) \sin\left(\frac{\pi}{6}\right) \right] = \frac{3 V_{mL}}{\pi} \left[ 2 \cos\alpha \cdot \frac{1}{2} \right]$$
$$V_{dc} = \frac{3 V_{mL}}{\pi} \cos\alpha = \frac{3\sqrt{3} V_m}{\pi} \cos\alpha \approx 1.654 V_{mL} \cos\alpha$$
where $V_m$ is peak phase voltage and $V_{mL} = \sqrt{3} V_m$ is peak line voltage.
Characteristics:
- Output ripple frequency is 6 times supply frequency ($6f = 300\text{ Hz}$ for $50\text{ Hz}$ supply), resulting in minimal filter requirements.
- Reversible voltage polarity permits smooth transition between rectification ($0^\circ \le \alpha \le 90^\circ$) and regeneration ($90^\circ < \alpha < 180^\circ$).
"""
            },
            {
                "qid": "comp-q24",
                "marks": 7,
                "type": "Derivation",
                "title": "DC-DC Switching Converters: CCM Analysis of Buck, Boost, and Buck-Boost Topologies",
                "yt_query": "dc-dc converters buck boost buck-boost inductor volt-second balance continuous conduction mode",
                "img_path": "images/comp/dcdc_converters_waveforms.png",
                "img_caption": "Figure 5.3: Circuit Topologies and Inductor Current / Voltage Waveforms for Buck, Boost, and Buck-Boost Converters",
                "answer": r"""
DC-DC switching converters (choppers) utilize semiconductor switches (MOSFETs or IGBTs), diodes, and low-loss energy-storage inductors/capacitors to synthesize variable DC voltage levels with conversion efficiencies exceeding $90-95\%$.

Fundamental Principles of Steady-State Operation in Continuous Conduction Mode (CCM):
1. Inductor Volt-Second Balance Principle: In steady-state, the net change in inductor current over a complete switching period $T$ must be zero ($\Delta i_L = \frac{1}{L}\int_0^T v_L(t) dt = 0$). Hence, the average voltage across an ideal inductor over one cycle is identically zero:
   $$\langle v_L \rangle = \frac{1}{T} \int_0^T v_L(t) dt = 0$$
2. Capacitor Charge (Ampere-Second) Balance Principle: In steady-state, the net change in capacitor charge over one cycle is zero ($\Delta Q = \int_0^T i_C(t) dt = 0$). Hence, the average capacitor current over one cycle is identically zero:
   $$\langle i_C \rangle = \frac{1}{T} \int_0^T i_C(t) dt = 0$$

1. Step-Down (Buck) Converter:
The Buck converter steps down an input voltage $V_s$ to a lower output voltage $V_o < V_s$.
- Switching Cycle: Period $T = 1/f_s$. Duty cycle $D = \frac{T_{on}}{T}$.
- Interval 1 ($0 \le t \le D T$, Switch $S$ is ON):
  Freewheeling diode $D_f$ is reverse-biased. Inductor connects to supply:
  $$v_L = V_s - V_o$$
  Inductor current rises linearly from $I_{L,\min}$ to $I_{L,\max}$:
  $$\frac{di_L}{dt} = \frac{V_s - V_o}{L} \implies \Delta I_L = \frac{V_s - V_o}{L} D T$$
- Interval 2 ($D T \le t \le T$, Switch $S$ is OFF):
  Inductor EMF reverses, forcing diode $D_f$ to conduct. Inductor discharges into load:
  $$v_L = -V_o$$
  $$\Delta I_L = \frac{V_o}{L} (1 - D) T$$

Derivation of Voltage Conversion Ratio:
Applying Inductor Volt-Second Balance:
$$\langle v_L \rangle = (V_s - V_o) D T + (-V_o) (1 - D) T = 0$$
$$(V_s - V_o) D - V_o (1 - D) = 0 \implies V_s D - V_o D - V_o + V_o D = 0$$
$$V_o = D V_s$$
Since $0 \le D \le 1$, the output voltage is always less than or equal to $V_s$.

Inductor Current Ripple ($\Delta I_L$) & Output Voltage Ripple ($\Delta V_o$):
$$\Delta I_L = \frac{V_s D (1 - D)}{f_s L}$$
The capacitor current is $i_C(t) = i_L(t) - I_o$. The charge accumulated during the positive half-cycle of triangular $i_C$ is the area of a triangle:
$$\Delta Q = \frac{1}{2} \left(\frac{T}{2}\right) \left(\frac{\Delta I_L}{2}\right) = \frac{T \Delta I_L}{8} = \frac{\Delta I_L}{8 f_s}$$
$$\Delta V_o = \frac{\Delta Q}{C} = \frac{\Delta I_L}{8 f_s C} = \frac{V_s D (1 - D)}{8 L C f_s^2}$$

2. Step-Up (Boost) Converter:
The Boost converter steps up input voltage $V_s$ to a higher output voltage $V_o > V_s$.
- Interval 1 ($0 \le t \le D T$, Switch $S$ is ON):
  Diode is reverse-biased by $V_o$. Inductor stores energy from supply:
  $$v_L = V_s \implies \frac{di_L}{dt} = \frac{V_s}{L} \implies \Delta I_L = \frac{V_s}{L} D T$$
  Capacitor supplies entire load current: $i_C = -I_o$.
- Interval 2 ($D T \le t \le T$, Switch $S$ is OFF):
  Inductor voltage adds to source voltage to forward-bias diode:
  $$v_L = V_s - V_o$$

Derivation of Voltage Conversion Ratio:
Applying Inductor Volt-Second Balance:
$$V_s D T + (V_s - V_o)(1 - D) T = 0$$
$$V_s D + V_s - V_s D - V_o(1 - D) = 0 \implies V_s = V_o (1 - D)$$
$$V_o = \frac{V_s}{1 - D}$$
Since $(1 - D) \le 1$, the output voltage is strictly greater than or equal to $V_s$.
Inductor current ripple: $\Delta I_L = \frac{V_s D}{f_s L}$.
Output voltage ripple (capacitor discharges $I_o$ during $T_{on} = D T$):
$$\Delta V_o = \frac{\Delta Q}{C} = \frac{I_o D T}{C} = \frac{I_o D}{f_s C} = \frac{V_o D}{R_L f_s C}$$

3. Inverting Buck-Boost Converter:
The Buck-Boost converter produces an output voltage that can be higher or lower than input voltage, with opposite polarity.
- Interval 1 ($0 \le t \le D T$, Switch $S$ is ON):
  Diode reverse-biased. Inductor stores energy from supply:
  $$v_L = V_s \implies \Delta I_L = \frac{V_s}{L} D T$$
- Interval 2 ($D T \le t \le T$, Switch $S$ is OFF):
  Inductor discharges through diode into load with reversed polarity ($v_L = -V_o$ where $V_o$ is treated positive):
  $$v_L = -V_o$$

Derivation of Voltage Conversion Ratio:
Applying Inductor Volt-Second Balance:
$$V_s D T + (-V_o)(1 - D) T = 0 \implies V_s D = V_o (1 - D)$$
$$V_o = -V_s \left( \frac{D}{1 - D} \right)$$
- If $D < 0.5 \implies \frac{D}{1 - D} < 1$ (Step-down Buck mode).
- If $D = 0.5 \implies V_o = -V_s$.
- If $D > 0.5 \implies \frac{D}{1 - D} > 1$ (Step-up Boost mode).

Critical Inductance for Continuous Conduction Mode (CCM):
For all converters, CCM requires minimum inductor current to remain positive: $I_{L,\min} = I_L - \frac{\Delta I_L}{2} \ge 0$.
- For Buck: $L_{\min} = \frac{(1 - D) R_L}{2 f_s}$
- For Boost: $L_{\min} = \frac{D (1 - D)^2 R_L}{2 f_s}$
- For Buck-Boost: $L_{\min} = \frac{(1 - D)^2 R_L}{2 f_s}$
"""
            },
            {
                "qid": "comp-q25",
                "marks": 7,
                "type": "Derivation",
                "title": "Voltage Source Inverters: 1-Phase & 3-Phase (180° & 120° Modes) and Sinusoidal PWM",
                "yt_query": "voltage source inverter three phase 180 120 conduction mode sinusoidal pwm spwm derivation",
                "img_path": "images/comp/vsi_inverters_spwm.png",
                "img_caption": "Figure 5.4: Three-Phase 180°/120° VSI Waveforms and Sinusoidal Pulse Width Modulation (SPWM) Scheme",
                "answer": r"""
Voltage Source Inverters (VSI) convert a stiff DC input voltage source into an AC output voltage of controllable magnitude and frequency, serving as the power core for AC motor drives, uninterruptible power supplies (UPS), and solar grid inverters.

1. Single-Phase Full-Bridge Inverter:
The full-bridge inverter uses four switches ($S_1-S_4$) and four antiparallel feedback diodes ($D_1-D_4$) across a DC link voltage $V_{dc}$.
- Square-Wave Mode ($180^\circ$ conduction):
  - Diagonal pair $(S_1, S_2)$ ON for $0 \le \omega t \le \pi \implies v_o = +V_{dc}$.
  - Diagonal pair $(S_3, S_4)$ ON for $\pi \le \omega t \le 2\pi \implies v_o = -V_{dc}$.
- Fourier Series Representation of Output Voltage:
  Because the square waveform possesses odd quarter-wave symmetry:
  $$v_o(t) = \sum_{n=1,3,5\dots}^\infty \frac{4 V_{dc}}{n \pi} \sin(n\omega t)$$
- Fundamental Peak and RMS Output Voltage:
  $$V_{o1,peak} = \frac{4 V_{dc}}{\pi} \approx 1.273 V_{dc}$$
  $$V_{o1,rms} = \frac{4 V_{dc}}{\sqrt{2} \pi} = \frac{2\sqrt{2}}{\pi} V_{dc} \approx 0.90 V_{dc}$$
- Total RMS Output Voltage:
  $$V_{rms} = \sqrt{\frac{1}{\pi}\int_0^\pi V_{dc}^2\,d(\omega t)} = V_{dc}$$
- Total Harmonic Distortion (THD):
  $$THD = \frac{\sqrt{V_{rms}^2 - V_{o1,rms}^2}}{V_{o1,rms}} = \frac{\sqrt{V_{dc}^2 - (0.90 V_{dc})^2}}{0.90 V_{dc}} \approx 48.34\%$$

2. Three-Phase Voltage Source Inverter (Bridge Configuration):
Comprises six semiconductor switches ($S_1$ to $S_6$) with antiparallel diodes.
- Upper switches: $S_1, S_3, S_5$ (connected to $+V_{dc}$).
- Lower switches: $S_4, S_6, S_2$ (connected to ground / negative bus).
- Balanced three-phase star load with isolated neutral point $n$.

Mode A: $180^\circ$ Conduction Mode:
Each switch conducts for an electrical interval of $180^\circ$. At any given instant, exactly three switches are conducting simultaneously (e.g., two upper and one lower, or one upper and two lower). Firing pulses between upper and lower switches of the same leg are complementary (e.g., $S_1$ and $S_4$).

Phase Voltage Determination (Star Load):
Consider State 1 ($S_1, S_6, S_5$ are ON):
Phase $A$ and Phase $C$ are connected to $+V_{dc}$; Phase $B$ is connected to $0\text{ V}$.
The load forms a parallel combination of phases $A$ and $C$ in series with phase $B$:
$$Z_{eq} = \frac{Z}{2} + Z = \frac{3}{2} Z$$
Neutral voltage with respect to negative bus:
$$V_n = \frac{Z/2}{(3/2)Z} V_{dc} = \frac{1}{3} V_{dc}$$
Phase-to-neutral voltages:
$$v_{an} = V_A - V_n = V_{dc} - \frac{1}{3}V_{dc} = +\frac{2}{3} V_{dc}$$
$$v_{bn} = V_B - V_n = 0 - \frac{1}{3}V_{dc} = -\frac{1}{3} V_{dc}$$
$$v_{cn} = V_C - V_n = V_{dc} - \frac{1}{3}V_{dc} = +\frac{2}{3} V_{dc}$$

Across all 6 switching steps of $60^\circ$ each, the phase voltages exhibit a 6-step staircase waveform taking values:
$$v_{an} \in \left\{ +\frac{1}{3}V_{dc}, \ +\frac{2}{3}V_{dc}, \ +\frac{1}{3}V_{dc}, \ -\frac{1}{3}V_{dc}, \ -\frac{2}{3}V_{dc}, \ -\frac{1}{3}V_{dc} \right\}$$
Line voltages are quasi-square waves with $120^\circ$ pulses:
$$v_{ab} = v_{an} - v_{bn} \in \{ +V_{dc}, \ +V_{dc}, \ 0, \ -V_{dc}, \ -V_{dc}, \ 0 \}$$

RMS Voltage Calculations for $180^\circ$ Mode:
- RMS Line Voltage:
  $$V_{L,rms} = \sqrt{\frac{1}{\pi}\int_0^{2\pi/3} V_{dc}^2\,d(\omega t)} = V_{dc} \sqrt{\frac{2}{3}} \approx 0.816 V_{dc}$$
- RMS Fundamental Line Voltage:
  $$V_{L1,rms} = \frac{1}{\sqrt{2}} \left( \frac{4 V_{dc}}{\pi} \cos 30^\circ \right) = \frac{\sqrt{6}}{\pi} V_{dc} \approx 0.7797 V_{dc}$$
- RMS Phase Voltage:
  $$V_{ph,rms} = \sqrt{\frac{1}{\pi}\left[ \int_0^{\pi/3} \left(\frac{V_{dc}}{3}\right)^2 d\theta + \int_{\pi/3}^{2\pi/3} \left(\frac{2V_{dc}}{3}\right)^2 d\theta + \int_{2\pi/3}^\pi \left(\frac{V_{dc}}{3}\right)^2 d\theta \right]} = \frac{\sqrt{2}}{3} V_{dc} \approx 0.471 V_{dc}$$

Mode B: $120^\circ$ Conduction Mode:
In $120^\circ$ mode, each switch conducts for only $120^\circ$. At any instant, exactly two switches are ON (one upper, one lower).
A dead time of $60^\circ$ exists between the turning OFF of an outgoing switch and the turning ON of the incoming switch in the same leg, completely eliminating the danger of shoot-through DC-bus short circuits.
- RMS Line Voltage:
  $$V_{L,rms} = \frac{V_{dc}}{\sqrt{2}} \approx 0.707 V_{dc}$$
- RMS Fundamental Line Voltage:
  $$V_{L1,rms} = \frac{\sqrt{6}}{\pi} V_{dc} \cos 30^\circ \approx 0.675 V_{dc}$$

3. Sinusoidal Pulse Width Modulation (SPWM):
To eliminate low-order harmonics ($3\text{rd}, 5\text{th}, 7\text{th}$) and regulate fundamental voltage linearly without bulky DC-link preregulators, Sinusoidal PWM is universally employed.

Principle:
A low-frequency sinusoidal modulating reference signal $v_m(t) = V_m \sin\omega_m t$ is compared against a high-frequency triangular carrier signal $v_c(t)$ of peak amplitude $V_c$ and frequency $f_c$.
- When $v_m > v_c$: The upper switch is turned ON ($v_o = +V_{dc}/2$).
- When $v_m < v_c$: The lower switch is turned ON ($v_o = -V_{dc}/2$).

Key Modulation Indices:
1. Amplitude Modulation Index ($m_a$):
   $$m_a = \frac{V_m}{V_c}$$
   - Linear Modulation Region ($0 \le m_a \le 1$): The peak of the fundamental output voltage varies linearly with $m_a$:
     $$V_{o1,peak} = m_a \left(\frac{V_{dc}}{2}\right) \quad (\text{Half-Bridge}) \quad \implies \quad V_{o1,rms} = \frac{m_a V_{dc}}{2\sqrt{2}}$$
     $$V_{L1,rms} = \frac{\sqrt{3}}{2\sqrt{2}} m_a V_{dc} \approx 0.612 m_a V_{dc} \quad (\text{Three-Phase})$$
   - Overmodulation Region ($m_a > 1$): Fundamental output increases nonlinearly up to square-wave limit ($V_{o1,peak} \to \frac{4}{\pi}\frac{V_{dc}}{2}$), introducing low-order harmonics.
2. Frequency Modulation Ratio ($m_f$):
   $$m_f = \frac{f_c}{f_m}$$
   - Selecting $m_f$ as an odd multiple of 3 eliminates all triplen harmonics in 3-phase line-to-line voltages.
   - Harmonic Spectrum: The fundamental is accompanied by carrier sideband harmonics clustered at frequencies:
     $$f_h = j \cdot m_f \pm k \quad (j = 1, 2\dots)$$
     Since $f_c$ is typically several kilohertz ($2 - 20\text{ kHz}$), these harmonics occur far above the fundamental power frequency, enabling small, lightweight, and inexpensive LC low-pass filters to achieve nearly pure sinusoidal output currents.
"""
            },
            {
                "qid": "comp-q26",
                "marks": 7,
                "type": "Analytical",
                "title": "Electric Drives: 4-Quadrant Dynamics, DC Drive Control, V/f AC Drives, and Electrical Braking",
                "yt_query": "electric drives four quadrant operation dc motor converter speed control v f scalar control electrical braking",
                "img_path": "images/comp/electric_drives_4quadrant.png",
                "img_caption": "Figure 5.5: Four-Quadrant Torque-Speed Operational Plane and Volts-per-Hertz (V/f) Speed Control Characteristic",
                "answer": r"""
An electric drive converts electrical energy into controlled mechanical motion. Modern industrial electric drives combine power electronic converters, digital controllers, and electrical machines to achieve precise four-quadrant speed and torque regulation.

1. Dynamics of Motor-Load System & Four-Quadrant Operation:
The fundamental dynamic equation governing the mechanical shaft of an electric drive is:
$$T_e - T_L = J \frac{d\omega_m}{dt} + B \omega_m$$
where $T_e$ is developed motor electromagnetic torque ($\text{N}\cdot\text{m}$), $T_L$ is load torque, $J$ is net moment of inertia ($\text{kg}\cdot\text{m}^2$), $\omega_m$ is angular speed ($\text{rad/s}$), and $B$ is viscous friction coefficient.

Four-Quadrant Operational Classification:
On the Torque-Speed ($\omega_m - T_e$) plane:
- Quadrant I: Forward Motoring ($\omega_m > 0, T_e > 0$):
  Motor rotates forward and delivers positive mechanical power ($P = T_e \omega_m > 0$).
- Quadrant II: Forward Braking / Generating ($\omega_m > 0, T_e < 0$):
  Motor rotates forward, but develops counter-torque opposing motion ($P < 0$). Kinetic energy is extracted from the load and converted into electrical energy.
- Quadrant III: Reverse Motoring ($\omega_m < 0, T_e < 0$):
  Motor rotates in reverse direction and develops negative torque in direction of motion ($P = (-T_e)(-\omega_m) > 0$).
- Quadrant IV: Reverse Braking / Generating ($\omega_m < 0, T_e > 0$):
  Motor rotates in reverse, but develops positive forward torque to decelerate the reverse-moving load ($P < 0$).

Industrial Application Examples:
- Electric Traction: Motoring up an incline (Q-I), regenerative braking down an incline (Q-II), reversing into siding (Q-III), and braking in reverse (Q-IV).
- Hoists and Elevators: Lifting loaded cage (Q-I), lowering loaded cage under regenerative counter-torque (Q-IV), lowering empty cage (Q-III), and stopping ascending cage (Q-II).

2. Speed Control of Separately Excited DC Motor using Controlled Rectifiers:
For a separately excited DC motor with armature resistance $R_a$ and back EMF constant $K_b$:
$$V_a = E_b + I_a R_a = K_b \Phi \omega_m + I_a R_a$$
$$T_e = K_t \Phi I_a \implies I_a = \frac{T_e}{K_t \Phi}$$
Substituting $I_a$ into the voltage equation:
$$\omega_m = \frac{V_a}{K_b \Phi} - \frac{R_a}{(K_b \Phi)(K_t \Phi)} T_e = \frac{V_a}{K_a \Phi} - \frac{R_a}{(K_a \Phi)^2} T_e$$
When fed from a single-phase fully-controlled bridge converter in continuous conduction:
$$V_a = \frac{2 V_m}{\pi} \cos\alpha$$
$$\omega_m = \frac{2 V_m \cos\alpha}{\pi K_a \Phi} - \frac{R_a}{(K_a \Phi)^2} T_e$$
By continuously varying the firing angle $\alpha$ from $0^\circ$ to $90^\circ$, armature terminal voltage $V_a$ is smoothly adjusted from rated voltage down to zero, providing continuous speed control below base speed.
For complete Four-Quadrant DC Drive operation, Dual Converters (two full-bridge converters connected back-to-back with circulating or non-circulating current mode) are utilized to handle both bidirectional armature voltage and bidirectional armature current.

3. Constant Volts-per-Hertz ($V/f$) Control of 3-Phase Induction Motors:
From the induction motor stator EMF equation:
$$E_1 \approx V_1 = 4.44 k_w f_1 \Phi_m T_1 \implies \Phi_m \propto \frac{V_1}{f_1}$$
Air-gap magnetic flux $\Phi_m$ is directly proportional to the ratio of applied stator voltage $V_1$ to supply frequency $f_1$.

Control Strategy Across Operating Zones:
- Zone 1: Sub-Synchronous Constant Torque Region ($f_1 \le f_{rated}$):
  If frequency $f_1$ is decreased to lower motor speed without changing voltage $V_1$, the ratio $V_1 / f_1$ would rise dramatically, driving the magnetic core into deep saturation, drawing excessive magnetizing current, and causing destructive overheating.
  Strategy: Scale stator voltage $V_1$ in direct proportion to frequency $f_1$ such that:
  $$\frac{V_1}{f_1} = \text{constant}$$
  This maintains air-gap flux at its rated level ($\Phi_m = \Phi_{rated}$).
  Maximum Breakdown Torque Under Constant $V/f$:
  $$T_{\max} = \frac{3}{2 \omega_s} \frac{V_1^2}{X_1 + X_2'} \propto \frac{1}{f_1} \left( \frac{V_1}{2\pi f_1 (L_1 + L_2')} \right) \propto \left( \frac{V_1}{f_1} \right)^2 = \text{constant}$$
  The maximum breakdown torque remains constant across the entire sub-synchronous operating range!
  Low-Frequency Voltage Boost: At very low frequencies ($< 10\text{ Hz}$), the stator resistance drop $I_1 R_1$ becomes significant compared to $V_1$, reducing effective air-gap EMF $E_1$. An additional voltage offset (voltage boost $V_{boost}$) is added to sustain rated flux and high starting torque.
- Zone 2: Super-Synchronous Constant Power Region (Field Weakening, $f_1 > f_{rated}$):
  Above rated base frequency, stator voltage cannot exceed the rated insulation limit ($V_1 = V_{rated} = \text{constant}$).
  As frequency increases, flux decreases inversely ($\Phi_m \propto 1/f_1$). The motor enters the field-weakening regime:
  $$T_{\max} \propto \frac{1}{f_1^2}$$
  Available torque drops quadratically, while mechanical power capability remains constant ($P = T \cdot \omega_m \approx \text{constant}$).

4. Electrical Braking Methods:
Electrical braking converts kinetic energy stored in the rotating drive inertia into electrical energy, decelerating the machine rapidly, smoothly, and without mechanical friction brake wear.

1. Regenerative Braking:
- Principle: Occurs when the motor speed exceeds the synchronous speed ($N > N_s$ for induction motor $\implies s < 0$) or when back EMF exceeds supply voltage ($E_b > V$ for DC motor).
- Mechanism: The machine acts as a generator, converting kinetic energy into electrical energy and feeding it directly back into the supply grid (or DC link).
- Induction Motor: For $s < 0$, rotor resistance term $R_2 / s$ becomes negative, reversing the direction of air-gap power and developing negative braking torque. Highly energy-efficient; widely used in electric trains and hybrid vehicles.

2. Dynamic (Rheostatic) Braking:
- Principle: The motor is disconnected from the electrical supply mains and its terminals are connected across an external dissipation resistor bank $R_B$.
- DC Motor: Shunt field excitation is maintained. The rotating armature acts as a loaded DC generator delivering current $I_B = \frac{E_b}{R_a + R_B}$ into $R_B$, dissipating kinetic energy purely as heat ($I_B^2 R_B$).
- Induction Motor: Stator AC supply is cut off and replaced by a DC excitation current, creating a stationary magnetic field in the air-gap. The rotating rotor cuts this stationary field, inducing currents that dissipate kinetic energy in the rotor resistance.

3. Counter-Current Braking (Plugging):
- Principle: Developing intense counter-torque by reversing the direction of the machine's magnetic field while running.
- DC Motor: Armature terminal connections are reversed while leaving field excitation unaltered. Total loop voltage becomes $V + E_b \approx 2 V$. A heavy series braking resistor must be immediately inserted to limit armature current:
  $$I_{plug} = \frac{V + E_b}{R_a + R_{ext}}$$
- Induction Motor: Any two stator phase leads are swapped (e.g., swapping phases $Y$ and $B$). The rotating magnetic field instantly reverses direction ($N_s \to -N_s$). The relative slip becomes:
  $$s_{plug} = \frac{-N_s - N}{-N_s} = \frac{N_s + N}{N_s} = 2 - s \approx 2.0$$
- Emergency Stopping: Plugging generates the highest decelerating torque, but dissipates huge power ($I^2 R$) combining kinetic energy and grid power. An automatic zero-speed centrifugal or plugging switch must disconnect the motor the instant speed approaches zero to prevent the machine from accelerating in reverse.
"""
            }
        ]
    },
]

COMPREHENSIVE_BYHEART = {
    "comp-q1": {
        "eq": r"""$$R_L = R_{th}, \quad P_{max} = \frac{V_{th}^2}{4 R_{th}}, \quad \mathbf{Z}_L = \mathbf{Z}_{th}^* = R_{th} - jX_{th}, \quad \eta = 50\%$$""",
        "text": r"""<strong>Maximum Power Transfer:</strong> In DC circuits, maximum power is delivered when $R_L = R_{th}$ with $\eta = 50\%$. In AC circuits with complex load impedance, maximum active power occurs under conjugate match $\mathbf{Z}_L = \mathbf{Z}_{th}^*$, eliminating net loop reactance."""
    },
    "comp-q2": {
        "eq": r"""$$i(t) = \frac{V_s}{R}(1 - e^{-t/\tau}), \ \tau = \frac{L}{R} \text{ or } RC, \quad s^2 + 2\zeta\omega_n s + \omega_n^2 = 0, \ \zeta = \frac{R}{2}\sqrt{\frac{C}{L}}$$""",
        "text": r"""<strong>RL, RC, RLC Transients:</strong> First-order time constants are $\tau = L/R$ and $\tau = RC$. Second-order RLC circuit yields overdamped ($\zeta > 1$), critically damped ($\zeta = 1$), and underdamped oscillatory ($\zeta < 1$) responses with $\omega_d = \omega_n\sqrt{1-\zeta^2}$."""
    },
    "comp-q3": {
        "eq": r"""$$\omega_0 = \frac{1}{\sqrt{LC}}, \quad Q = \frac{\omega_0 L}{R} = \frac{1}{R}\sqrt{\frac{L}{C}}, \quad BW = \frac{\omega_0}{Q} = \frac{R}{L}, \quad Z_d = \frac{L}{C R_L}$$""",
        "text": r"""<strong>AC Resonance:</strong> Series resonance yields minimum impedance $Z_0 = R$ and maximum current with voltage magnification $Q V$. Parallel tank circuit yields maximum dynamic impedance $Z_d = L/(C R_L)$ (anti-resonance) and minimum line current."""
    },
    "comp-q4": {
        "eq": r"""$$V_L = \sqrt{3}V_{ph}, \quad P = W_1 + W_2 = \sqrt{3}V_L I_L \cos\phi, \quad \tan\phi = \sqrt{3}\frac{W_1 - W_2}{W_1 + W_2}$$""",
        "text": r"""<strong>Three-Phase & Two-Wattmeter Method:</strong> Total 3-phase active power is the algebraic sum $W_1 + W_2$. Load power factor is derived from $\tan\phi = \sqrt{3}(W_1 - W_2)/(W_1 + W_2)$. When $\cos\phi = 0.5$, $W_2 = 0$; when $\cos\phi < 0.5$, $W_2$ deflects negative."""
    },
    "comp-q5": {
        "eq": r"""$$\nabla \cdot \mathbf{D} = \rho_v, \ \nabla \cdot \mathbf{B} = 0, \ \nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}, \ \nabla \times \mathbf{H} = \mathbf{J}_c + \frac{\partial \mathbf{D}}{\partial t}, \ \mathbf{S} = \mathbf{E} \times \mathbf{H}$$""",
        "text": r"""<strong>Maxwell\'s Equations & Poynting Vector:</strong> Maxwell added displacement current $\mathbf{J}_d = \partial \mathbf{D}/\partial t$ to Ampère\'s law to satisfy charge continuity. Electromagnetic waves propagate at $v = 1/\sqrt{\mu\varepsilon}$ with intrinsic impedance $\eta = \sqrt{\mu/\varepsilon} \approx 377\,\Omega$. Poynting vector $\mathbf{S}$ denotes power flux density."""
    },
    "comp-q6": {
        "eq": r"""$$E_b = \frac{P \Phi Z N}{60 A}, \quad T_e = \frac{P Z}{2\pi A}\Phi I_a, \quad AT_d = \frac{Z I_a}{2 A P}\left(\frac{2\theta_m}{180^\circ}\right), \quad N = \frac{V - I_a R_a}{K\' \Phi}$$""",
        "text": r"""<strong>DC Machines:</strong> Induced EMF and torque equations dictate electromechanical conversion. Armature reaction causes MNA shift and air-gap distortion; neutralized by interpoles and compensating windings. Speed control uses armature voltage, field flux, or Ward-Leonard drives."""
    },
    "comp-q7": {
        "eq": r"""$$W_c = V I_{a0} - I_{a0}^2 R_a, \quad P_{in,mains} = V I_1 = \text{Total Losses of Both Machines}, \quad W_{stray} = \frac{W_{stray,total}}{2}$$""",
        "text": r"""<strong>DC Machine Testing:</strong> Swinburne\'s no-load test predetermines motor/generator efficiency by isolating constant losses $W_c$. Hopkinson\'s regenerative back-to-back test tests two coupled machines at actual full load, drawing only net system losses from mains."""
    },
    "comp-q8": {
        "eq": r"""$$\%VR = \frac{I_2 R_{02}\cos\phi \pm I_2 X_{02}\sin\phi}{V_2}\times 100\%, \quad x = \sqrt{\frac{P_i}{P_{cu,fl}}}, \quad W_{auto} = (1 - k) W_{2-wdg}$$""",
        "text": r"""<strong>Transformers:</strong> OC test finds core loss $P_i$ and magnetizing parameters; SC test finds copper loss $P_{cu,fl}$ and series leakage impedance. Maximum efficiency occurs when $P_i = x^2 P_{cu,fl}$. Autotransformer saves $(1 - k)$ copper via conductive power transfer."""
    },
    "comp-q9": {
        "eq": r"""$$\Phi_r = 1.5\Phi_m, \quad T_e = \frac{3}{\omega_s}\frac{s E_2^2 R_2}{R_2^2 + s^2 X_2^2}, \quad s_{max} = \frac{R_2}{X_2}, \quad T_{max} = \frac{3 E_2^2}{2\omega_s X_2}, \quad I_{st,Y} = \frac{1}{3}I_{st,\Delta}$$""",
        "text": r"""<strong>Induction Motors:</strong> Balanced 3-phase stator currents produce an RMF of constant magnitude $1.5\Phi_m$ revolving at $N_s$. Breakdown torque $T_{max}$ is independent of rotor resistance $R_2$. Star-delta starting reduces starting line current and torque to $1/3$."""
    },
    "comp-q10": {
        "eq": r"""$$E_{ph} = 4.44 k_p k_d f \Phi T_{ph}, \quad P = \frac{E_0 V}{X_d}\sin\delta + \frac{V^2}{2}\left(\frac{1}{X_q} - \frac{1}{X_d}\right)\sin 2\delta$$""",
        "text": r"""<strong>Synchronous Machines:</strong> EMF method is pessimistic; MMF method is optimistic. Two-reaction theory resolves salient-pole armature currents into $d$ and $q$ axis components ($X_d > X_q$), producing reluctance torque proportional to $\sin 2\delta$."""
    },
    "comp-q11": {
        "eq": r"""$$I_{a1} = \frac{E_a}{Z_1 + Z_2 + Z_0 + 3Z_f} \ (\text{SLG}), \quad \frac{2H}{\omega_s}\frac{d^2\delta}{dt^2} = P_m - P_e, \quad \int_{\delta_0}^{\delta_{cr}}(P_m - P_e)d\delta = \int_{\delta_{cr}}^{\delta_{max}}(P_e - P_m)d\delta$$""",
        "text": r"""<strong>Power Systems & Stability:</strong> Fortescue symmetrical components resolve unsymmetrical faults (SLG: sequence networks in series). Swing equation governs electromechanical dynamics. Equal Area Criterion determines critical clearing angle $\delta_{cr}$ without step integration."""
    },
    "comp-q12": {
        "eq": r"""$$T(s) = \frac{C(s)}{R(s)} = \frac{\sum_{k=1}^N P_k \Delta_k}{\Delta}, \quad \Delta = 1 - \sum L_1 + \sum L_2 - \sum L_3 + \dots$$""",
        "text": r"""<strong>Transfer Function & Mason\'s Rule:</strong> Block diagram algebra simplifies interconnected systems. Mason\'s gain formula evaluates closed-loop transfer functions directly by determining forward paths $P_k$, loops $L_i$, and non-touching loop determinants $\Delta, \Delta_k$."""
    },
    "comp-q13": {
        "eq": r"""$$t_p = \frac{\pi}{\omega_n\sqrt{1-\zeta^2}}, \quad M_p = e^{-\frac{\pi\zeta}{\sqrt{1-\zeta^2}}}\times 100\%, \quad t_s(2\%) = \frac{4}{\zeta\omega_n}, \quad e_{ss} = \lim_{s\to 0}\frac{s R(s)}{1 + G(s)}$$""",
        "text": r"""<strong>Second-Order Time Specifications:</strong> Damping ratio $\zeta$ dictates maximum overshoot $M_p$ and transient oscillations. Settling time is $t_s \approx 4/(\zeta\omega_n)$. Steady-state error depends on system type number and static error constants ($K_p, K_v, K_a$)."""
    },
    "comp-q14": {
        "eq": r"""$$b_1 = \frac{a_1 a_2 - a_0 a_3}{a_1}, \quad \angle G(s)H(s) = \pm (2k+1)180^\circ, \quad \sigma_A = \frac{\sum P_i - \sum Z_j}{P - Z}, \quad \frac{dK}{ds} = 0$$""",
        "text": r"""<strong>s-Domain Stability:</strong> Routh-Hurwitz criterion determines RHP roots from sign changes in column 1. Root locus plots closed-loop pole trajectories as gain $K: 0 \to \infty$; breakaway points satisfy $dK/ds = 0$ and asymptotes emanate from centroid $\sigma_A$."""
    },
    "comp-q15": {
        "eq": r"""$$GM = -20\log_{10}|G(j\omega_{pc})|, \quad PM = 180^\circ + \angle G(j\omega_{gc}), \quad N = Z - P \implies Z = N + P = 0$$""",
        "text": r"""<strong>Bode & Nyquist Stability:</strong> Bode plots provide gain margin ($GM$) and phase margin ($PM$). Nyquist criterion maps the s-plane boundary around critical point $(-1 + j0)$; closed-loop stability requires counter-clockwise encirclements equal to open-loop RHP poles ($N = -P$)."""
    },
    "comp-q16": {
        "eq": r"""$$\mathbf{\dot{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{u}, \ \mathbf{\Phi}(t) = e^{\mathbf{A}t}, \ \text{rank}[\mathbf{B} \ \mathbf{AB} \dots] = n, \ L_x = R_2 R_3 C_4, \ C_x = C_3 \frac{R_4}{R_2}$$""",
        "text": r"""<strong>Modern Control & Bridges:</strong> State transition matrix $\mathbf{\Phi}(t) = \mathcal{L}^{-1}\{(s\mathbf{I}-\mathbf{A})^{-1}\}$. Kalman tests verify controllability and observability. Maxwell-Wien bridge measures inductance; Schering bridge measures capacitance and $\tan\delta$. CT secondaries must never be open-circuited."""
    },
    "comp-q17": {
        "eq": r"""$$V_{dc} = \frac{2V_m}{\pi}, \ \gamma = \sqrt{\left(\frac{I_{rms}}{I_{dc}}\right)^2 - 1} = 0.482, \ \eta = 81.2\%, \ \Delta V_r = \frac{V_m}{2 f R_L C}, \ R_s = \frac{V_{in} - V_Z}{I_Z + I_L}$$""",
        "text": r"""<strong>Rectifiers & Regulators:</strong> Full-wave bridge rectifier yields $V_{dc} = 2V_m/\pi$, ripple factor $\gamma = 0.482$, and efficiency $\eta = 81.2\%$. C-filter smooths output voltage. Zener diode stabilizes load voltage across varying input voltages and load currents."""
    },
    "comp-q18": {
        "eq": r"""$$S = (1 + \beta)\frac{1 + R_{th}/R_E}{1 + \beta + R_{th}/R_E}, \quad A_v = -\frac{R_C \parallel R_L}{r_e}, \quad C_{M} = C_\mu(1 + |A_v|)$$""",
        "text": r"""<strong>BJT Amplifiers:</strong> Voltage divider bias minimizes stability factor $S \to 1$, preventing thermal runaway. Small-signal CE gain is $A_v = -g_m (R_C \parallel R_L)$ with $180^\circ$ phase inversion. High-frequency roll-off is dominated by Miller effect multiplication of $C_\mu$."""
    },
    "comp-q19": {
        "eq": r"""$$A_{v,inv} = -\frac{R_f}{R_1}, \quad A_{v,non} = 1 + \frac{R_f}{R_1}, \quad V_o = \left(1 + \frac{2 R_1}{R_{gain}}\right)\left(\frac{R_3}{R_2}\right)(V_2 - V_1)$$""",
        "text": r"""<strong>Operational Amplifiers:</strong> Virtual short ($V^+ = V^-$) and zero input current govern Op-Amp analysis. Practical integrators use feedback resistance $R_f$ to prevent DC saturation. 3-Op-Amp instrumentation amplifier offers high CMRR, high input impedance, and single resistor gain tuning."""
    },
    "comp-q20": {
        "eq": r"""$$t_H = 0.693(R_A + R_B)C, \quad t_L = 0.693 R_B C, \quad f = \frac{1.44}{(R_A + 2 R_B)C}, \quad T_{mono} = 1.1 R_A C$$""",
        "text": r"""<strong>IC 555 Timer:</strong> Internal comparators switch at $(1/3)V_{CC}$ and $(2/3)V_{CC}$. Astable multivibrator oscillates at $f = 1.44/((R_A + 2R_B)C)$ with duty cycle $> 50\%$. Monostable multivibrator generates one-shot pulses of duration $T = 1.1 R_A C$."""
    },
    "comp-q21": {
        "eq": r"""$$\overline{A + B} = \bar{A}\bar{B}, \ \overline{A B} = \bar{A} + \bar{B}, \ S = A \oplus B \oplus C_{in}, \ Q_{next} = J\bar{Q} + \bar{K}Q, \ J_2 = K_2 = Q_1 Q_0$$""",
        "text": r"""<strong>Digital Logic & Counters:</strong> De Morgan\'s laws simplify Boolean logic. Full adders use $S = A\oplus B\oplus C_{in}$ and $C_{out} = AB + C_{in}(A\oplus B)$. Master-Slave JK flip-flops eliminate race-around conditions. Synchronous binary counter design uses flip-flop excitation tables."""
    },
    "comp-q22": {
        "eq": r"""$$I_A = \frac{\alpha_2 I_g + I_{CBO1} + I_{CBO2}}{1 - (\alpha_1 + \alpha_2)}, \quad I_L > I_H, \quad \text{MOSFET: } R_{DS(on)} \propto T, \quad \text{IGBT: } V_{CE(sat)} \approx 1.5-2.5\text{ V}$$""",
        "text": r"""<strong>Power Semiconductor Devices:</strong> SCR turns on regeneratively when loop gain $(\alpha_1 + \alpha_2) \to 1$. Latching current $I_L > I_H$. Power MOSFET provides ultra-fast switching with positive temperature coefficient. IGBT combines MOS voltage gate drive with bipolar low on-state drop."""
    },
    "comp-q23": {
        "eq": r"""$$V_{dc,1\phi} = \frac{2 V_m}{\pi}\cos\alpha, \quad V_{dc,3\phi} = \frac{3 V_{mL}}{\pi}\cos\alpha = \frac{3\sqrt{3}V_m}{\pi}\cos\alpha, \quad \alpha > 90^\circ \implies \text{Inversion}$$""",
        "text": r"""<strong>Controlled Rectifiers:</strong> Fully controlled 1-phase bridge gives $V_{dc} = (2V_m/\pi)\cos\alpha$; 3-phase 6-pulse bridge gives $V_{dc} = (3V_{mL}/\pi)\cos\alpha$. Operating at $\alpha > 90^\circ$ enables line-commutated synchronous inversion. Freewheeling diode prevents negative voltage spikes."""
    },
    "comp-q24": {
        "eq": r"""$$V_o = D V_s \ (\text{Buck}), \quad V_o = \frac{V_s}{1 - D} \ (\text{Boost}), \quad V_o = -\frac{D}{1 - D}V_s \ (\text{Buck-Boost}), \quad \langle v_L \rangle = 0$$""",
        "text": r"""<strong>DC-DC Converters:</strong> Steady-state operation is governed by inductor volt-second balance ($\langle v_L \rangle = 0$) and capacitor charge balance ($\langle i_C \rangle = 0$). Buck steps down ($D$), Boost steps up ($1/(1-D)$), and Buck-Boost inverts and scales ($D/(1-D)$).`"""
    },
    "comp-q25": {
        "eq": r"""$$V_{L1,rms}^{180^\circ} = \frac{\sqrt{6}}{\pi}V_{dc} \approx 0.78 V_{dc}, \quad V_{L,rms}^{120^\circ} = \frac{V_{dc}}{\sqrt{2}}, \quad m_a = \frac{V_m}{V_c}, \quad V_{L1,rms} \approx 0.612 m_a V_{dc}$$""",
        "text": r"""<strong>Inverters & SPWM:</strong> 3-phase VSI operating in $180^\circ$ conduction mode yields 6-step staircase phase voltages; $120^\circ$ mode provides $60^\circ$ deadband preventing shoot-through. Sinusoidal PWM compares sine reference with triangular carrier, shifting harmonics to carrier sidebands."""
    },
    "comp-q26": {
        "eq": r"""$$T_e - T_L = J\frac{d\omega_m}{dt} + B\omega_m, \quad \omega_m = \frac{V_a}{K_a\Phi} - \frac{R_a}{(K_a\Phi)^2}T_e, \quad \frac{V}{f} = \text{const} \implies T_{max} = \text{const}$$""",
        "text": r"""<strong>Electric Drives & Braking:</strong> 4-quadrant plane governs motoring and braking. DC drives vary armature voltage via phase converters. $V/f$ constant volts-per-hertz maintains rated induction motor flux and maximum torque. Electrical braking includes regenerative, dynamic, and plugging."""
    }
}

COMPREHENSIVE_EXAM_QUESTIONS = {
    "comp-q1": "State and prove Thévenin's, Norton's, and the Maximum Power Transfer theorems for DC and AC circuits. Derive the complex load condition for maximum active power transfer.",
    "comp-q2": "Derive the transient current and voltage responses for series RL, RC, and series RLC circuits excited by a DC step input. Discuss overdamped, critically damped, and underdamped conditions.",
    "comp-q3": "Derive the resonant frequency, half-power bandwidth, and Quality factor for a series RLC circuit. Explain parallel resonance in a practical tank circuit and derive its dynamic impedance.",
    "comp-q4": "Derive the relationships between line and phase voltages and currents in balanced Star and Delta AC systems. Explain the two-wattmeter method of 3-phase power measurement and derive the power factor formula.",
    "comp-q5": "State and explain Maxwell's four equations in differential and integral forms. Derive the electromagnetic wave equation in a lossless medium and state Poynting's theorem.",
    "comp-q6": "Derive the generated EMF and torque equations of a DC machine. Explain armature reaction, commutation, methods of improving commutation, and speed control techniques for DC motors.",
    "comp-q7": "Explain the testing of DC machines using Swinburne's test and Hopkinson's regenerative test. Derive the equations for predetermining motor and generator efficiency.",
    "comp-q8": "Draw the exact and approximate equivalent circuits of a single-phase transformer. Derive the voltage regulation expression and explain OC/SC tests and autotransformer copper saving.",
    "comp-q9": "Prove mathematically that a balanced 3-phase stator winding produces a rotating magnetic field of constant magnitude. Derive the torque-slip equation and discuss starting methods of induction motors.",
    "comp-q10": "Explain the determination of voltage regulation of an alternator by EMF and MMF methods. Describe Blondel's two-reaction theory for salient-pole synchronous machines and derive the power-angle equation.",
    "comp-q11": "Explain transmission line ABCD parameters and per-unit representation. Analyze symmetrical and unsymmetrical faults using symmetrical components, and derive the swing equation and equal area criterion.",
    "comp-q12": "Define transfer function and explain mechanical-electrical analogies. State the block diagram reduction rules and Mason's gain formula with an illustrative signal flow graph example.",
    "comp-q13": "Derive the step response of an underdamped second-order control system and formulate the time-domain specifications: rise time, peak time, peak overshoot, and settling time. Discuss steady-state error.",
    "comp-q14": "Explain the Routh-Hurwitz stability criterion including its special cases. Formulate the comprehensive construction rules for the Root Locus technique.",
    "comp-q15": "Explain the construction of Bode plots and the determination of gain margin and phase margin. Explain the Nyquist stability criterion using Cauchy's principle of the argument.",
    "comp-q16": "Explain state-space representation, state transition matrix, and Kalman's criteria for controllability and observability. Describe AC bridges (Maxwell-Wien, Schering) and instrument transformers.",
    "comp-q17": "Explain the operation and performance metrics (ripple factor, efficiency, PIV) of half-wave and full-wave rectifiers with capacitor filters. Describe the design of a Zener diode voltage regulator.",
    "comp-q18": "Explain BJT input and output characteristics in CE configuration. Derive the stability factor for a voltage divider bias circuit and conduct small-signal low-frequency amplifier analysis.",
    "comp-q19": "List the ideal characteristics of an Op-Amp. Derive the voltage gain for inverting, non-inverting, practical integrator, and three-Op-Amp instrumentation amplifier circuits.",
    "comp-q20": "Draw the internal block diagram of IC 555 timer. Explain its operation as an astable and monostable multivibrator, deriving the formulas for frequency, duty cycle, and pulse duration.",
    "comp-q21": "State De Morgan's laws and K-map minimization rules. Design a Full Adder and explain multiplexers. Explain the race-around condition in JK flip-flops and design a 3-bit synchronous binary counter.",
    "comp-q22": "Explain the static V-I characteristics and two-transistor analogy of an SCR. Compare the structure, characteristics, and switching performance of SCR, Power MOSFET, and IGBT.",
    "comp-q23": "Derive the average DC output voltage and RMS voltage for single-phase and three-phase fully-controlled bridge rectifiers with R and RL loads. Explain inversion mode and freewheeling diode action.",
    "comp-q24": "Explain the continuous conduction mode (CCM) operation of Buck, Boost, and Buck-Boost DC-DC converters using inductor volt-second and capacitor charge balance, deriving voltage conversion ratios.",
    "comp-q25": "Describe single-phase and three-phase voltage source inverters operating in 180° and 120° conduction modes with phase and line waveforms. Explain Sinusoidal PWM and its harmonic benefits.",
    "comp-q26": "Explain four-quadrant operation of electric drives. Describe converter speed control of DC motors, constant V/f speed control of induction motors, and electrical braking methods."
}

__all__ = ["COMPREHENSIVE_MODULES", "COMPREHENSIVE_BYHEART", "COMPREHENSIVE_EXAM_QUESTIONS"]

if __name__ == "__main__":
    total_q = sum(len(m["questions"]) for m in COMPREHENSIVE_MODULES)
    print(f"gen_comprehensive.py verified: {len(COMPREHENSIVE_MODULES)} modules, {total_q} questions, "
          f"{len(COMPREHENSIVE_BYHEART)} byheart cards, {len(COMPREHENSIVE_EXAM_QUESTIONS)} exam questions.")
