# -*- coding: utf-8 -*-
"""
Extra data structures for Subject 11: Comprehensive Course Work (EET308).
Contains COMPREHENSIVE_BYHEART and COMPREHENSIVE_EXAM_QUESTIONS dictionaries.
"""

COMPREHENSIVE_BYHEART = {
    'comp-q1': {
        "eq": r'$$R_L = R_{th}, \quad P_{max} = \frac{V_{th}^2}{4 R_{th}}, \quad \mathbf{Z}_L = \mathbf{Z}_{th}^* = R_{th} - jX_{th}, \quad \eta = 50\%$$',
        "text": r'<strong>Maximum Power Transfer:</strong> In DC circuits, maximum power is delivered when $R_L = R_{th}$ with $\eta = 50\%$. In AC circuits with complex load impedance, maximum active power occurs under conjugate match $\mathbf{Z}_L = \mathbf{Z}_{th}^*$, eliminating net loop reactance.'
    },
    'comp-q2': {
        "eq": r'$$i(t) = \frac{V_s}{R}(1 - e^{-t/\tau}), \ \tau = \frac{L}{R} \text{ or } RC, \quad s^2 + 2\zeta\omega_n s + \omega_n^2 = 0, \ \zeta = \frac{R}{2}\sqrt{\frac{C}{L}}$$',
        "text": r'<strong>RL, RC, RLC Transients:</strong> First-order time constants are $\tau = L/R$ and $\tau = RC$. Second-order RLC circuit yields overdamped ($\zeta > 1$), critically damped ($\zeta = 1$), and underdamped oscillatory ($\zeta < 1$) responses with $\omega_d = \omega_n\sqrt{1-\zeta^2}$.'
    },
    'comp-q3': {
        "eq": r'$$\omega_0 = \frac{1}{\sqrt{LC}}, \quad Q = \frac{\omega_0 L}{R} = \frac{1}{R}\sqrt{\frac{L}{C}}, \quad BW = \frac{\omega_0}{Q} = \frac{R}{L}, \quad Z_d = \frac{L}{C R_L}$$',
        "text": r'<strong>AC Resonance:</strong> Series resonance yields minimum impedance $Z_0 = R$ and maximum current with voltage magnification $Q V$. Parallel tank circuit yields maximum dynamic impedance $Z_d = L/(C R_L)$ (anti-resonance) and minimum line current.'
    },
    'comp-q4': {
        "eq": r'$$V_L = \sqrt{3}V_{ph}, \quad P = W_1 + W_2 = \sqrt{3}V_L I_L \cos\phi, \quad \tan\phi = \sqrt{3}\frac{W_1 - W_2}{W_1 + W_2}$$',
        "text": r'<strong>Three-Phase & Two-Wattmeter Method:</strong> Total 3-phase active power is the algebraic sum $W_1 + W_2$. Load power factor is derived from $\tan\phi = \sqrt{3}(W_1 - W_2)/(W_1 + W_2)$. When $\cos\phi = 0.5$, $W_2 = 0$; when $\cos\phi < 0.5$, $W_2$ deflects negative.'
    },
    'comp-q5': {
        "eq": r'$$\nabla \cdot \mathbf{D} = \rho_v, \ \nabla \cdot \mathbf{B} = 0, \ \nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}, \ \nabla \times \mathbf{H} = \mathbf{J}_c + \frac{\partial \mathbf{D}}{\partial t}, \ \mathbf{S} = \mathbf{E} \times \mathbf{H}$$',
        "text": r'<strong>Maxwell\'s Equations & Poynting Vector:</strong> Maxwell added displacement current $\mathbf{J}_d = \partial \mathbf{D}/\partial t$ to Ampère\'s law to satisfy charge continuity. Electromagnetic waves propagate at $v = 1/\sqrt{\mu\varepsilon}$ with intrinsic impedance $\eta = \sqrt{\mu/\varepsilon} \approx 377\,\Omega$. Poynting vector $\mathbf{S}$ denotes power flux density.'
    },
    'comp-q6': {
        "eq": r'$$E_b = \frac{P \Phi Z N}{60 A}, \quad T_e = \frac{P Z}{2\pi A}\Phi I_a, \quad AT_d = \frac{Z I_a}{2 A P}\left(\frac{2\theta_m}{180^\circ}\right), \quad N = \frac{V - I_a R_a}{K\' \Phi}$$',
        "text": r'<strong>DC Machines:</strong> Induced EMF and torque equations dictate electromechanical conversion. Armature reaction causes MNA shift and air-gap distortion; neutralized by interpoles and compensating windings. Speed control uses armature voltage, field flux, or Ward-Leonard drives.'
    },
    'comp-q7': {
        "eq": r'$$W_c = V I_{a0} - I_{a0}^2 R_a, \quad P_{in,mains} = V I_1 = \text{Total Losses of Both Machines}, \quad W_{stray} = \frac{W_{stray,total}}{2}$$',
        "text": r'<strong>DC Machine Testing:</strong> Swinburne\'s no-load test predetermines motor/generator efficiency by isolating constant losses $W_c$. Hopkinson\'s regenerative back-to-back test tests two coupled machines at actual full load, drawing only net system losses from mains.'
    },
    'comp-q8': {
        "eq": r'$$\%VR = \frac{I_2 R_{02}\cos\phi \pm I_2 X_{02}\sin\phi}{V_2}\times 100\%, \quad x = \sqrt{\frac{P_i}{P_{cu,fl}}}, \quad W_{auto} = (1 - k) W_{2-wdg}$$',
        "text": r'<strong>Transformers:</strong> OC test finds core loss $P_i$ and magnetizing parameters; SC test finds copper loss $P_{cu,fl}$ and series leakage impedance. Maximum efficiency occurs when $P_i = x^2 P_{cu,fl}$. Autotransformer saves $(1 - k)$ copper via conductive power transfer.'
    },
    'comp-q9': {
        "eq": r'$$\Phi_r = 1.5\Phi_m, \quad T_e = \frac{3}{\omega_s}\frac{s E_2^2 R_2}{R_2^2 + s^2 X_2^2}, \quad s_{max} = \frac{R_2}{X_2}, \quad T_{max} = \frac{3 E_2^2}{2\omega_s X_2}, \quad I_{st,Y} = \frac{1}{3}I_{st,\Delta}$$',
        "text": r'<strong>Induction Motors:</strong> Balanced 3-phase stator currents produce an RMF of constant magnitude $1.5\Phi_m$ revolving at $N_s$. Breakdown torque $T_{max}$ is independent of rotor resistance $R_2$. Star-delta starting reduces starting line current and torque to $1/3$.'
    },
    'comp-q10': {
        "eq": r'$$E_{ph} = 4.44 k_p k_d f \Phi T_{ph}, \quad P = \frac{E_0 V}{X_d}\sin\delta + \frac{V^2}{2}\left(\frac{1}{X_q} - \frac{1}{X_d}\right)\sin 2\delta$$',
        "text": r'<strong>Synchronous Machines:</strong> EMF method is pessimistic; MMF method is optimistic. Two-reaction theory resolves salient-pole armature currents into $d$ and $q$ axis components ($X_d > X_q$), producing reluctance torque proportional to $\sin 2\delta$.'
    },
    'comp-q11': {
        "eq": r'$$I_{a1} = \frac{E_a}{Z_1 + Z_2 + Z_0 + 3Z_f} \ (\text{SLG}), \quad \frac{2H}{\omega_s}\frac{d^2\delta}{dt^2} = P_m - P_e, \quad \int_{\delta_0}^{\delta_{cr}}(P_m - P_e)d\delta = \int_{\delta_{cr}}^{\delta_{max}}(P_e - P_m)d\delta$$',
        "text": r'<strong>Power Systems & Stability:</strong> Fortescue symmetrical components resolve unsymmetrical faults (SLG: sequence networks in series). Swing equation governs electromechanical dynamics. Equal Area Criterion determines critical clearing angle $\delta_{cr}$ without step integration.'
    },
    'comp-q12': {
        "eq": r'$$T(s) = \frac{C(s)}{R(s)} = \frac{\sum_{k=1}^N P_k \Delta_k}{\Delta}, \quad \Delta = 1 - \sum L_1 + \sum L_2 - \sum L_3 + \dots$$',
        "text": r'<strong>Transfer Function & Mason\'s Rule:</strong> Block diagram algebra simplifies interconnected systems. Mason\'s gain formula evaluates closed-loop transfer functions directly by determining forward paths $P_k$, loops $L_i$, and non-touching loop determinants $\Delta, \Delta_k$.'
    },
    'comp-q13': {
        "eq": r'$$t_p = \frac{\pi}{\omega_n\sqrt{1-\zeta^2}}, \quad M_p = e^{-\frac{\pi\zeta}{\sqrt{1-\zeta^2}}}\times 100\%, \quad t_s(2\%) = \frac{4}{\zeta\omega_n}, \quad e_{ss} = \lim_{s\to 0}\frac{s R(s)}{1 + G(s)}$$',
        "text": r'<strong>Second-Order Time Specifications:</strong> Damping ratio $\zeta$ dictates maximum overshoot $M_p$ and transient oscillations. Settling time is $t_s \approx 4/(\zeta\omega_n)$. Steady-state error depends on system type number and static error constants ($K_p, K_v, K_a$).'
    },
    'comp-q14': {
        "eq": r'$$b_1 = \frac{a_1 a_2 - a_0 a_3}{a_1}, \quad \angle G(s)H(s) = \pm (2k+1)180^\circ, \quad \sigma_A = \frac{\sum P_i - \sum Z_j}{P - Z}, \quad \frac{dK}{ds} = 0$$',
        "text": r'<strong>s-Domain Stability:</strong> Routh-Hurwitz criterion determines RHP roots from sign changes in column 1. Root locus plots closed-loop pole trajectories as gain $K: 0 \to \infty$; breakaway points satisfy $dK/ds = 0$ and asymptotes emanate from centroid $\sigma_A$.'
    },
    'comp-q15': {
        "eq": r'$$GM = -20\log_{10}|G(j\omega_{pc})|, \quad PM = 180^\circ + \angle G(j\omega_{gc}), \quad N = Z - P \implies Z = N + P = 0$$',
        "text": r'<strong>Bode & Nyquist Stability:</strong> Bode plots provide gain margin ($GM$) and phase margin ($PM$). Nyquist criterion maps the s-plane boundary around critical point $(-1 + j0)$; closed-loop stability requires counter-clockwise encirclements equal to open-loop RHP poles ($N = -P$).'
    },
    'comp-q16': {
        "eq": r'$$\mathbf{\dot{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{u}, \ \mathbf{\Phi}(t) = e^{\mathbf{A}t}, \ \text{rank}[\mathbf{B} \ \mathbf{AB} \dots] = n, \ L_x = R_2 R_3 C_4, \ C_x = C_3 \frac{R_4}{R_2}$$',
        "text": r'<strong>Modern Control & Bridges:</strong> State transition matrix $\mathbf{\Phi}(t) = \mathcal{L}^{-1}\{(s\mathbf{I}-\mathbf{A})^{-1}\}$. Kalman tests verify controllability and observability. Maxwell-Wien bridge measures inductance; Schering bridge measures capacitance and $\tan\delta$. CT secondaries must never be open-circuited.'
    },
    'comp-q17': {
        "eq": r'$$V_{dc} = \frac{2V_m}{\pi}, \ \gamma = \sqrt{\left(\frac{I_{rms}}{I_{dc}}\right)^2 - 1} = 0.482, \ \eta = 81.2\%, \ \Delta V_r = \frac{V_m}{2 f R_L C}, \ R_s = \frac{V_{in} - V_Z}{I_Z + I_L}$$',
        "text": r'<strong>Rectifiers & Regulators:</strong> Full-wave bridge rectifier yields $V_{dc} = 2V_m/\pi$, ripple factor $\gamma = 0.482$, and efficiency $\eta = 81.2\%$. C-filter smooths output voltage. Zener diode stabilizes load voltage across varying input voltages and load currents.'
    },
    'comp-q18': {
        "eq": r'$$S = (1 + \beta)\frac{1 + R_{th}/R_E}{1 + \beta + R_{th}/R_E}, \quad A_v = -\frac{R_C \parallel R_L}{r_e}, \quad C_{M} = C_\mu(1 + |A_v|)$$',
        "text": r'<strong>BJT Amplifiers:</strong> Voltage divider bias minimizes stability factor $S \to 1$, preventing thermal runaway. Small-signal CE gain is $A_v = -g_m (R_C \parallel R_L)$ with $180^\circ$ phase inversion. High-frequency roll-off is dominated by Miller effect multiplication of $C_\mu$.'
    },
    'comp-q19': {
        "eq": r'$$A_{v,inv} = -\frac{R_f}{R_1}, \quad A_{v,non} = 1 + \frac{R_f}{R_1}, \quad V_o = \left(1 + \frac{2 R_1}{R_{gain}}\right)\left(\frac{R_3}{R_2}\right)(V_2 - V_1)$$',
        "text": r'<strong>Operational Amplifiers:</strong> Virtual short ($V^+ = V^-$) and zero input current govern Op-Amp analysis. Practical integrators use feedback resistance $R_f$ to prevent DC saturation. 3-Op-Amp instrumentation amplifier offers high CMRR, high input impedance, and single resistor gain tuning.'
    },
    'comp-q20': {
        "eq": r'$$t_H = 0.693(R_A + R_B)C, \quad t_L = 0.693 R_B C, \quad f = \frac{1.44}{(R_A + 2 R_B)C}, \quad T_{mono} = 1.1 R_A C$$',
        "text": r'<strong>IC 555 Timer:</strong> Internal comparators switch at $(1/3)V_{CC}$ and $(2/3)V_{CC}$. Astable multivibrator oscillates at $f = 1.44/((R_A + 2R_B)C)$ with duty cycle $> 50\%$. Monostable multivibrator generates one-shot pulses of duration $T = 1.1 R_A C$.'
    },
    'comp-q21': {
        "eq": r'$$\overline{A + B} = \bar{A}\bar{B}, \ \overline{A B} = \bar{A} + \bar{B}, \ S = A \oplus B \oplus C_{in}, \ Q_{next} = J\bar{Q} + \bar{K}Q, \ J_2 = K_2 = Q_1 Q_0$$',
        "text": r'<strong>Digital Logic & Counters:</strong> De Morgan\'s laws simplify Boolean logic. Full adders use $S = A\oplus B\oplus C_{in}$ and $C_{out} = AB + C_{in}(A\oplus B)$. Master-Slave JK flip-flops eliminate race-around conditions. Synchronous binary counter design uses flip-flop excitation tables.'
    },
    'comp-q22': {
        "eq": r'$$I_A = \frac{\alpha_2 I_g + I_{CBO1} + I_{CBO2}}{1 - (\alpha_1 + \alpha_2)}, \quad I_L > I_H, \quad \text{MOSFET: } R_{DS(on)} \propto T, \quad \text{IGBT: } V_{CE(sat)} \approx 1.5-2.5\text{ V}$$',
        "text": r'<strong>Power Semiconductor Devices:</strong> SCR turns on regeneratively when loop gain $(\alpha_1 + \alpha_2) \to 1$. Latching current $I_L > I_H$. Power MOSFET provides ultra-fast switching with positive temperature coefficient. IGBT combines MOS voltage gate drive with bipolar low on-state drop.'
    },
    'comp-q23': {
        "eq": r'$$V_{dc,1\phi} = \frac{2 V_m}{\pi}\cos\alpha, \quad V_{dc,3\phi} = \frac{3 V_{mL}}{\pi}\cos\alpha = \frac{3\sqrt{3}V_m}{\pi}\cos\alpha, \quad \alpha > 90^\circ \implies \text{Inversion}$$',
        "text": r'<strong>Controlled Rectifiers:</strong> Fully controlled 1-phase bridge gives $V_{dc} = (2V_m/\pi)\cos\alpha$; 3-phase 6-pulse bridge gives $V_{dc} = (3V_{mL}/\pi)\cos\alpha$. Operating at $\alpha > 90^\circ$ enables line-commutated synchronous inversion. Freewheeling diode prevents negative voltage spikes.'
    },
    'comp-q24': {
        "eq": r'$$V_o = D V_s \ (\text{Buck}), \quad V_o = \frac{V_s}{1 - D} \ (\text{Boost}), \quad V_o = -\frac{D}{1 - D}V_s \ (\text{Buck-Boost}), \quad \langle v_L \rangle = 0$$',
        "text": r'<strong>DC-DC Converters:</strong> Steady-state operation is governed by inductor volt-second balance ($\langle v_L \rangle = 0$) and capacitor charge balance ($\langle i_C \rangle = 0$). Buck steps down ($D$), Boost steps up ($1/(1-D)$), and Buck-Boost inverts and scales ($D/(1-D)$).`'
    },
    'comp-q25': {
        "eq": r'$$V_{L1,rms}^{180^\circ} = \frac{\sqrt{6}}{\pi}V_{dc} \approx 0.78 V_{dc}, \quad V_{L,rms}^{120^\circ} = \frac{V_{dc}}{\sqrt{2}}, \quad m_a = \frac{V_m}{V_c}, \quad V_{L1,rms} \approx 0.612 m_a V_{dc}$$',
        "text": r'<strong>Inverters & SPWM:</strong> 3-phase VSI operating in $180^\circ$ conduction mode yields 6-step staircase phase voltages; $120^\circ$ mode provides $60^\circ$ deadband preventing shoot-through. Sinusoidal PWM compares sine reference with triangular carrier, shifting harmonics to carrier sidebands.'
    },
    'comp-q26': {
        "eq": r'$$T_e - T_L = J\frac{d\omega_m}{dt} + B\omega_m, \quad \omega_m = \frac{V_a}{K_a\Phi} - \frac{R_a}{(K_a\Phi)^2}T_e, \quad \frac{V}{f} = \text{const} \implies T_{max} = \text{const}$$',
        "text": r'<strong>Electric Drives & Braking:</strong> 4-quadrant plane governs motoring and braking. DC drives vary armature voltage via phase converters. $V/f$ constant volts-per-hertz maintains rated induction motor flux and maximum torque. Electrical braking includes regenerative, dynamic, and plugging.'
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
