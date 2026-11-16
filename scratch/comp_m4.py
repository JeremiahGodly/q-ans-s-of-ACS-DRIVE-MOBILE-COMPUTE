# -*- coding: utf-8 -*-
"""
Module 4: Analog and Digital Electronics
Questions comp-q17 to comp-q21 for Comprehensive Course Work (EET308).
"""

M4_QUESTIONS = [
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
