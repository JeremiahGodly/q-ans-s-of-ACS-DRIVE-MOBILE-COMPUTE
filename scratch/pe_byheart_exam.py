# -*- coding: utf-8 -*-
"""
Byheart Data and Exam Questions for Subject 7: Power Electronics (EET306)
KTU 2019 Scheme S6 EEE Question Bank
Questions: pe-q1 to pe-q26
"""

PE_BYHEART = {
    'pe-q1': {
        "eq": r'$$I_A = \frac{\alpha_2 I_g + I_{CBO1} + I_{CBO2}}{1 - (\alpha_1 + \alpha_2)}, \quad I_L \approx (2 \text{ to } 3) I_H$$',
        "text": r'SCR 4-layer $p_1-n_1-p_2-n_2$ structure modeled as coupled PNP ($Q_1$) and NPN ($Q_2$) transistors. Forward latching occurs via regenerative positive feedback when loop gain $\alpha_1 + \alpha_2 \to 1$. Latching current $I_L$ is minimum turn-on holding value; $I_H$ is drop-out threshold.'
    },
    'pe-q2': {
        "eq": r'$$P_{gm} = V_g I_g = \text{const}, \quad E_s = V_g + R_g I_g, \quad i_c = C_{j2}\frac{dv}{dt}$$',
        "text": r'Turn-on via gate pulse, light (LASCR), thermal, or $dv/dt$. Gate operating point must lie inside preferred triggering window bounded by $V_{g\min}, V_{g\max}, I_{g\min}, I_{g\max}$ and peak gate power hyperbola $P_{gm}$. Pulse transformer / optocoupler provides galvanic isolation.'
    },
    'pe-q3': {
        "eq": r'$$t_{on} = t_d + t_r + t_p, \quad t_q = t_{rr} + t_{gr}, \quad t_c > t_q \ (\text{commutation})$$',
        "text": r'Turn-on transient comprises delay ($t_d$), rise ($t_r$), and spread ($t_p$) times. Turn-off transient requires sweeping out reverse carriers ($t_{rr}$) and thermal recombination of trapped junction charges ($t_{gr}$). Circuit turn-off time must satisfy $t_c > t_q$ to avoid commutation failure.'
    },
    'pe-q4': {
        "eq": r'$$L_s \ge \frac{V_s}{(di/dt)_{\max}}, \quad C_s = \frac{V_s^2}{L_s (dv/dt)_{\max}^2}, \quad R_s \ge \frac{V_s}{I_{T\max}}, \quad \zeta = \frac{R_s}{2}\sqrt{\frac{C_s}{L_s}}$$',
        "text": r'Series inductor $L_s$ suppresses localized gate hot-spot burning from high $di/dt$. Parallel RC snubber dampens transient $dv/dt$ displacement currents across junction $J_2$. Snubber resistor $R_s$ limits discharge current when SCR fires.'
    },
    'pe-q5': {
        "eq": r'$$\beta_{off} = \frac{I_A}{I_{GR}} \approx 3-5 \ (\text{GTO}), \quad R_{DS(on)} \propto V_{BR}^{2.5} \ (\text{MOSFET}), \quad V_{CE(sat)} \approx 1.8-2.5\text{ V} \ (\text{IGBT})$$',
        "text": r'<strong>TRIAC:</strong> Bidirectional AC line switch (4 quadrants).<br><strong>GTO:</strong> Turn-off via large reverse gate current.<br><strong>MOSFET:</strong> Unipolar majority-carrier switch for MHz frequencies ($<600\text{ V}$).<br><strong>IGBT:</strong> Hybrid MOS-input BJT-output with conductivity modulation for medium/high power.'
    },
    'pe-q6': {
        "eq": r'$$V_{dc} = \frac{V_m}{2\pi}(1 + \cos\alpha), \quad V_{rms} = \frac{V_m}{2\sqrt{\pi}}\sqrt{(\pi - \alpha) + \frac{1}{2}\sin 2\alpha}, \quad i_o(\beta) = 0$$',
        "text": r'1-Phase Half-Wave Controlled Rectifier. Inductive RL load extends conduction into negative half-cycle to extinction angle $\beta$. Freewheeling diode clamps $v_o \ge 0$, discharges inductive energy, boosts average DC voltage, and improves power factor.'
    },
    'pe-q7': {
        "eq": r'$$V_{dc} = \frac{2 V_m}{\pi}\cos\alpha, \quad V_{rms} = \frac{V_m}{\sqrt{2}} = V_s, \quad I_{dc} = \frac{V_{dc} - E}{R}$$',
        "text": r'1-Phase Full Converter with RLE load operates in Quadrant I ($0 \le \alpha < 90^\circ$, Rectification) and Quadrant IV ($90^\circ < \alpha < 180^\circ$, Inversion). Line commutation transfers current between SCR pairs. Discontinuous conduction occurs at light loads.'
    },
    'pe-q8': {
        "eq": r'$$\text{DF} = \cos\alpha, \quad \text{THD} = \sqrt{\left(\frac{\pi}{2\sqrt{2}}\right)^2 - 1} \approx 48.34\%, \quad \text{PF} = \frac{2\sqrt{2}}{\pi}\cos\alpha$$',
        "text": r'Displacement Factor $\text{DF} = \cos\phi_1$. Total Harmonic Distortion measures ripple current relative to fundamental. Semi-converter exhibits higher PF ($\text{DF} = \cos(\alpha/2)$) and lower reactive power than full converter due to freewheeling action.'
    },
    'pe-q9': {
        "eq": r'$$V_{dc} = \frac{3 V_{ml}}{\pi}\cos\alpha = \frac{3\sqrt{3}V_{mp}}{\pi}\cos\alpha \approx 1.35 V_L \cos\alpha, \quad V_{rms} = V_{ml}\sqrt{\frac{1}{2} + \frac{3\sqrt{3}}{4\pi}\cos 2\alpha}$$',
        "text": r'3-Phase 6-Pulse Full Bridge Converter: 6 SCRs triggered at $60^\circ$ intervals, each conducting for $120^\circ$. Output line voltage switches between 6 line pairs. Operates as rectifier for $\alpha \le 90^\circ$ and line-commutated inverter for $\alpha > 90^\circ$.'
    },
    'pe-q10': {
        "eq": r'$$\cos(\alpha + \mu) = \cos\alpha - \frac{2 \omega L_s I_{dc}}{V_m}, \quad \Delta V_d = \frac{2 \omega L_s}{\pi} I_{dc} \ (\text{1-ph}), \quad \Delta V_d = \frac{3 \omega L_s}{\pi} I_{dc} \ (\text{3-ph})$$',
        "text": r'Source inductance $L_s$ prevents instantaneous current transfer, causing commutation overlap angle $\mu$. Output voltage drops by $\Delta V_d$. In inverter mode, if $\alpha + \mu > 180^\circ - \omega t_q$, commutation failure occurs.'
    },
    'pe-q11': {
        "eq": r'$$V_o = D V_s, \quad \Delta I_L = \frac{V_s D(1 - D)}{f_s L}, \quad \Delta V_c = \frac{V_s D(1 - D)}{8 f_s^2 L C}, \quad L_c = \frac{(1 - D) R}{2 f_s}$$',
        "text": r'Step-down (Buck) converter in CCM. Inductor volt-second balance yields linear gain $M = D$. Second-order LC filter delivers low output voltage ripple. Critical inductance $L_c$ guarantees continuous conduction at specified load resistance.'
    },
    'pe-q12': {
        "eq": r'$$V_o = \frac{V_s}{1 - D}, \quad \Delta I_L = \frac{V_s D}{f_s L}, \quad \Delta V_c = \frac{V_o D}{R f_s C}, \quad L_c = \frac{D(1 - D)^2 R}{2 f_s}$$',
        "text": r'Step-up (Boost) converter in CCM. Energy stored during switch ON adds in series with DC source during switch OFF. Output capacitor supplies load while switch is ON. Inductor parasitic resistance limits maximum practical voltage gain.'
    },
    'pe-q13': {
        "eq": r'$$V_o = -\frac{D}{1 - D} V_s, \quad \Delta I_L = \frac{V_s D}{f_s L}, \quad \Delta V_c = \frac{V_o D}{R f_s C}, \quad L_c = \frac{(1 - D)^2 R}{2 f_s}$$',
        "text": r'Inverting Buck-Boost converter provides step-down ($D < 0.5$) and step-up ($D > 0.5$) voltage translation with reversed output polarity. Inductor acts as intermediate energy reservoir between input and output ports.'
    },
    'pe-q14': {
        "eq": r'$$V_o = -\frac{D}{1 - D} V_s, \quad V_{C1} = \frac{V_s}{1 - D}, \quad \Delta I_{L1} = \frac{V_s D}{f_s L_1}, \quad \Delta I_{L2} = \frac{V_s D}{f_s L_2}$$',
        "text": r'Ćuk converter transfers energy capacitively via intermediate capacitor $C_1$. Dual input and output inductors eliminate pulsating currents at both terminal ports, yielding low EMI signatures and smooth continuous waveforms.'
    },
    'pe-q15': {
        "eq": r'$$\text{Class A: } (+V_o, +I_o), \ \text{Class B: } (+V_o, -I_o), \ \text{Class C: } (+V_o, \pm I_o), \ \text{Class D: } (\pm V_o, +I_o), \ \text{Class E: } (\pm V_o, \pm I_o)$$',
        "text": r'Chopper classification across $(V_o, I_o)$ plane: Class A (Motoring), Class B (Regenerative braking), Class C (Reversible drive), Class D (Coil de-energization), and Class E (Complete 4-quadrant H-bridge servo drive).'
    },
    'pe-q16': {
        "eq": r'$$\text{Half: } V_{o,rms} = \frac{V_{dc}}{2}, \ V_{o1} = \frac{2 V_{dc}}{\pi}; \quad \text{Full: } V_{o,rms} = V_{dc}, \ V_{o1} = \frac{4 V_{dc}}{\pi}; \quad V_{o1,\text{quasi}} = \frac{4 V_{dc}}{\pi}\sin d$$',
        "text": r'1-Phase VSI topologies: Full-bridge delivers twice the voltage and 4x the power of half-bridge. Feedback diodes circulate reactive load current and return energy to DC source ($v_o \cdot i_o < 0$). Quasi-square wave modulation controls fundamental and eliminates harmonics.'
    },
    'pe-q17': {
        "eq": r'$$V_{L,rms} = \sqrt{\frac{2}{3}} V_{dc} \approx 0.8165 V_{dc}, \quad V_{ph,rms} = \frac{\sqrt{2}}{3} V_{dc} \approx 0.4714 V_{dc}, \quad V_{L1,rms} = \frac{\sqrt{6}}{\pi} V_{dc} \approx 0.7797 V_{dc}$$',
        "text": r'3-Phase VSI 180° conduction: Each switch conducts for 180°, with 3 switches ON simultaneously. Six-step phase voltage waveform. Triplen harmonics are inherently eliminated from line-to-line voltages.'
    },
    'pe-q18': {
        "eq": r'$$V_{L,rms} = \frac{V_{dc}}{\sqrt{2}} \approx 0.7071 V_{dc}, \quad V_{ph,rms} = \frac{V_{dc}}{\sqrt{6}} \approx 0.4082 V_{dc}, \quad \text{Inherent } 60^\circ \text{ Deadband}$$',
        "text": r'3-Phase VSI 120° conduction: Each switch conducts for 120°, with 2 switches ON simultaneously. Inherent 60° deadband prevents shoot-through faults without blanking circuits. Delivers 86.6% of the line voltage of 180° mode.'
    },
    'pe-q19': {
        "eq": r'$$m_a = \frac{A_r}{A_c}, \quad m_f = \frac{f_c}{f_m}, \quad V_{o1\max} = m_a V_{dc} \ (m_a \le 1), \quad f_h = (j \cdot m_f \pm k) f_m$$',
        "text": r'Sinusoidal PWM (SPWM) compares sine reference with triangular carrier. Linear modulation up to $m_a = 1$. High carrier ratio $m_f$ pushes harmonic sidebands far above line frequency, simplifying passive filter design.'
    },
    'pe-q20': {
        "eq": r'$$\text{VSI: Stiff } C_{dc}, \text{ antiparallel diodes, shoot-through risk}; \quad \text{CSI: Stiff } L_{dc}, \text{ series diodes, open-circuit risk}$$',
        "text": r'VSI regulates voltage (load determines current), dominates EVs and industrial inverters. CSI regulates current via large series choke $L_{dc}$ with ASCI commutation, offering inherent short-circuit immunity and four-quadrant regeneration for MW drives.'
    },
    'pe-q21': {
        "eq": r'$$\text{Integral: } V_{o,rms} = V_s \sqrt{\frac{n}{n + m}}, \ \text{PF} = \sqrt{\frac{n}{n + m}}; \quad \text{Phase: } V_{o,rms} = V_s \sqrt{\frac{1}{\pi}\left[(\pi - \alpha) + \frac{1}{2}\sin 2\alpha\right]}$$',
        "text": r'1-Phase AC Voltage Controller with R load: Integral cycle control switches at zero crossings (no RFI, heating loads); Phase angle control varies firing angle $\alpha$ from 0 to 180° to continuously regulate output RMS voltage.'
    },
    'pe-q22': {
        "eq": r'$$i_o(\omega t) = \frac{V_m}{Z}\left[\sin(\omega t - \phi) - \sin(\alpha - \phi) e^{-\frac{R}{\omega L}(\omega t - \alpha)}\right], \quad \alpha \ge \phi \ (\text{Operating Rule})$$',
        "text": r'1-Phase AC Controller with RL load: Controlled discontinuous mode for $\alpha > \phi$. When $\alpha = \phi$, current is continuous sinusoid ($V_{o,rms} = V_s$). Firing at $\alpha < \phi$ causes loss of control and DC core saturation; wide gate pulses required.'
    },
    'pe-q23': {
        "eq": r'$$f_o = \frac{f_s}{k} \ (k = 2, 3\dots), \quad \alpha_P + \alpha_N = 180^\circ \ (\text{Circulating Mode with IGR})$$',
        "text": r'Cycloconverters directly convert AC frequency without intermediate DC link. Step-down operation uses line commutation. Non-circulating mode requires zero-crossing deadtime; circulating mode uses Intergroup Reactor (IGR) to eliminate crossover distortion.'
    },
    'pe-q24': {
        "eq": r'$$P_{sw} = \frac{1}{2} V_s I_o (t_r + t_f) f_s, \quad \text{ZCS: } i_{sw} = 0 \ (\text{IGBT tail loss elimination}), \quad \text{ZVS: } v_{sw} = 0 \ (\text{MOSFET } C_{oss})$$',
        "text": r'Soft switching eliminates hard-switching overlap power dissipation. ZCS turns switch on/off at zero current (ideal for IGBTs). ZVS turns switch on/off at zero voltage (ideal for high-frequency Power MOSFETs, eliminating $\frac{1}{2}CV^2$ losses).'
    },
    'pe-q25': {
        "eq": r'$$\text{Flyback: } V_o = \frac{N_s}{N_p}\left(\frac{D}{1-D}\right)V_s, \quad \text{Forward: } V_o = \frac{N_s}{N_p} D V_s \ (D < 0.5), \quad \text{Push-Pull/Full: } V_o = 2\frac{N_s}{N_p} D V_s$$',
        "text": r'Isolated SMPS topologies: Flyback uses coupled inductor (energy stored in gap during switch ON, $<150\text{ W}$); Forward transfers energy during switch ON (needs tertiary reset winding); Push-Pull, Half-Bridge, and Full-Bridge provide 2-quadrant core utilization for high power.'
    },
    'pe-q26': {
        "eq": r'$$\text{Offline: } 4-10\text{ ms transfer}; \quad \text{Line-Interactive: } 2-4\text{ ms}; \quad \text{Online Double-Conversion: } 0\text{ ms (Zero)}$$',
        "text": r'UPS configurations: Offline provides raw mains with battery backup; Line-Interactive adds AVR voltage conditioning; Online Double-Conversion continuously converts $AC \to DC \to AC$, delivering 0 ms transfer time, perfect sine wave, and static bypass protection.'
    }
}

PE_EXAM_QUESTIONS = {
    "pe-q1": "Explain the physical construction and static V-I characteristics of a Silicon Controlled Rectifier (SCR). Derive the mathematical expression for anode current using the two-transistor analogy.",
    "pe-q2": "Describe the various turn-on methods for an SCR. Explain the gate characteristics, safe triggering area, and design of pulse transformer isolation gate drive circuits.",
    "pe-q3": "Explain the dynamic switching characteristics of an SCR during turn-on and turn-off processes. Define reverse recovery time, gate recovery time, and circuit turn-off time with neat waveforms.",
    "pe-q4": "Explain the need for di/dt and dv/dt protection for an SCR. Derive the design equations for a series inductor and an RC snubber circuit with a step-by-step numerical example.",
    "pe-q5": "Compare the operating principles, switching speeds, conduction losses, and Safe Operating Areas (SOA) of TRIAC, GTO, Power MOSFET, and IGBT.",
    "pe-q6": "Explain the operation of a single-phase half-wave controlled rectifier with R and RL loads. Derive expressions for average and RMS output voltages, and explain the effect of a freewheeling diode.",
    "pe-q7": "Derive the expression for average and RMS output voltages of a single-phase fully controlled bridge rectifier feeding an RLE load. Distinguish between continuous and discontinuous conduction modes.",
    "pe-q8": "Define and derive the performance parameters of phase-controlled converters: Displacement Factor (DF), Harmonic Factor (HF/THD), and Input Power Factor (PF). Compare semi-converter and full converter.",
    "pe-q9": "Describe the working of a three-phase fully controlled bridge converter (6-pulse) with RL load. Derive the expression for average DC output voltage and plot the line-to-line output waveforms.",
    "pe-q10": "Explain the effect of AC source inductance on the performance of single-phase and three-phase full converters. Derive expressions for overlap angle (mu) and average voltage drop.",
    "pe-q11": "Analyze the step-down (Buck) converter in continuous conduction mode. Derive the voltage transfer ratio, peak-to-peak inductor ripple current, output ripple voltage, and critical inductance.",
    "pe-q12": "Explain the operation of a step-up (Boost) converter in continuous conduction mode. Derive the voltage gain using inductor volt-second balance, and calculate the critical inductance for CCM.",
    "pe-q13": "Derive the voltage transfer ratio of an inverting Buck-Boost converter in continuous conduction mode. Derive expressions for inductor ripple current and critical boundary inductance.",
    "pe-q14": "Explain the circuit topology and working principle of a Cuk converter. Derive the voltage ratio and explain why both input and output currents are continuous.",
    "pe-q15": "Classify DC choppers into Class A, B, C, D, and E based on their quadrant of operation. Draw the circuit diagram and explain the four-quadrant operation of a full H-bridge chopper.",
    "pe-q16": "Explain the operation of single-phase half-bridge and full-bridge Voltage Source Inverters (VSI) with R and RL loads. Derive the Fourier series expression for output voltage and discuss feedback diodes.",
    "pe-q17": "Explain the 180-degree conduction mode of a three-phase Voltage Source Inverter with a star-connected balanced load. Derive expressions for line and phase voltages and show Fourier harmonic elimination.",
    "pe-q18": "Analyze the 120-degree conduction mode of a three-phase Voltage Source Inverter. Derive expressions for RMS line and phase voltages and compare performance with the 180-degree conduction mode.",
    "pe-q19": "Explain Pulse Width Modulation (PWM) techniques used in inverters: Single-Pulse, Multi-Pulse, and Sinusoidal PWM (SPWM). Define modulation index (ma) and frequency ratio (mf) with harmonic spectra.",
    "pe-q20": "Compare the operating principles, circuit topologies, and performance of Voltage Source Inverters (VSI) and Current Source Inverters (CSI). Explain the ASCI commutation mechanism.",
    "pe-q21": "Explain the operation of a single-phase AC voltage controller with resistive load using Integral Cycle Control and Phase Angle Control. Derive expressions for RMS output voltage and power factor.",
    "pe-q22": "Analyze the single-phase AC voltage controller with an inductive (RL) load. Discuss the three operating cases based on firing angle alpha and load angle phi, and derive the RMS output voltage.",
    "pe-q23": "Explain the working principle of single-phase to single-phase cycloconverters in mid-point and bridge configurations. Compare circulating and non-circulating current modes.",
    "pe-q24": "Explain the limitations of hard switching in high-frequency converters. Describe the principles and circuit topologies of Zero-Current Switching (ZCS) and Zero-Voltage Switching (ZVS) resonant converters.",
    "pe-q25": "Describe the circuit operation of isolated Switched-Mode Power Supply (SMPS) topologies: Flyback, Forward, Push-Pull, Half-bridge, and Full-bridge converters with comparative evaluation.",
    "pe-q26": "Explain the architectures of Uninterruptible Power Supplies (UPS): Offline, Line-Interactive, and Online Double-Conversion. Discuss the role of the static bypass switch and compare performance metrics."
}
