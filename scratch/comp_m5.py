# -*- coding: utf-8 -*-
"""
Module 5: Power Electronics and Electric Drives
Questions comp-q22 to comp-q26 for Comprehensive Course Work (EET308).
"""

M5_QUESTIONS = [
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
