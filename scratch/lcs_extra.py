# -*- coding: utf-8 -*-
"""
Byheart Data and Exam Questions for Linear Control Systems (EET302)
"""

LCS_EXAM_QUESTIONS = {
    "lcs-q1": "Compare open loop and closed loop control systems. Derive the expressions for the sensitivity of closed-loop system transfer function with respect to forward path gain G(s) and feedback path gain H(s).",
    "lcs-q2": "Explain Force-Voltage and Force-Current analogies for translational mechanical systems. Formulate the governing differential equations and provide the comprehensive analogy conversion table.",
    "lcs-q3": "Derive the mathematical model and the transfer functions X1(s)/F(s) and X2(s)/F(s) for a two-mass translational mechanical system with springs, dampers, and an external driving force applied to mass M1.",
    "lcs-q4": "State the fundamental rules of block diagram algebra. Step-by-step, reduce a multi-loop control system block diagram with multiple feedback paths to obtain its overall closed-loop transfer function C(s)/R(s).",
    "lcs-q5": "Define the terms related to Signal Flow Graphs and state Mason's Gain Formula. Using Mason's formula, determine the overall transfer function C(s)/R(s) of a given multi-loop control system.",
    "lcs-q6": "Define standard test signals used in control system analysis with their mathematical expressions. Derive the response of a first-order system to a unit step input and explain the significance of time constant.",
    "lcs-q7": "Derive the mathematical expression for the unit step response of an underdamped second-order control system in the time domain.",
    "lcs-q8": "Derive the mathematical formulas for time domain specifications of a second-order underdamped system: delay time (td), rise time (tr), peak time (tp), maximum percent overshoot (Mp), and settling time (ts).",
    "lcs-q9": "Define steady-state error and derive its expression using the final value theorem. Define static error constants (Kp, Kv, Ka) and tabulate steady-state errors for Type 0, Type 1, and Type 2 systems.",
    "lcs-q10": "Explain the characteristics and operating principles of P, PI, PD, and PID controllers. Discuss their effects on steady-state error, damping, stability, and transient response.",
    "lcs-q11": "Explain the concept of BIBO stability in linear systems. State the necessary and sufficient condition for stability based on impulse response and discuss the relation between s-plane pole locations and stability.",
    "lcs-q12": "State the Routh-Hurwitz stability criterion. Explain how Special Case 1 (first element in a row is zero while others are non-zero) is resolved using the epsilon method with a complete worked example.",
    "lcs-q13": "Explain Special Case 2 of the Routh array when an entire row becomes zero. Describe the construction of the auxiliary polynomial and determine the range of gain K and frequency of sustained oscillations for a fourth-order system.",
    "lcs-q14": "Explain the angle and magnitude conditions of the Root Locus technique. State and explain the eight essential procedural rules for the construction of a complete root locus diagram.",
    "lcs-q15": "Sketch the root locus for a unity feedback control system with open loop transfer function G(s) = K / [s(s+2)(s+4)]. Calculate centroid, asymptotes, breakaway points, imaginary axis crossings, and range of K for stability.",
    "lcs-q16": "Define the frequency domain specifications: resonant peak (Mr), resonant frequency (wr), and bandwidth (wb) for a second-order system. Derive their expressions and correlate them with time-domain specifications.",
    "lcs-q17": "Explain the construction of Bode magnitude and phase plots. Describe the asymptotic magnitude slopes and corner frequency characteristics for standard transfer function factors.",
    "lcs-q18": "Define Gain Crossover Frequency, Phase Crossover Frequency, Gain Margin, and Phase Margin from Bode plots. State the criteria for closed-loop stability and solve a complete numerical problem.",
    "lcs-q19": "Explain the construction of polar plots for Type 0, Type 1, and Type 2 systems. Discuss how the addition of open-loop poles and zeros affects the shape and stability of the polar plot locus.",
    "lcs-q20": "State and prove the Nyquist stability criterion using Cauchy's principle of the argument. Explain the mapping of the Nyquist contour and analyze the closed-loop stability of an open-loop unstable system.",
    "lcs-q21": "Explain the circuits, transfer functions, and pole-zero patterns of phase lead, phase lag, and lead-lag compensator networks. Derive the maximum phase lead angle phi_m and frequency omega_m for a lead network.",
    "lcs-q22": "Explain the step-by-step design procedure of a Phase Lead Compensator using frequency response (Bode plot) to satisfy specified phase margin and velocity error constant specifications.",
    "lcs-q23": "Explain the step-by-step design procedure of a Phase Lag Compensator using Bode plots to improve steady-state error performance without degrading existing phase margin.",
    "lcs-q24": "Explain the state-space representation of continuous-time LTI systems. Define state, state variables, state vector, and state equations, and state the major advantages of state space analysis over transfer functions.",
    "lcs-q25": "Derive the closed-loop transfer function matrix G(s) = C(sI - A)^{-1}B + D from state space equations. Prove that the poles of G(s) are the eigenvalues of state matrix A and solve a numerical problem.",
    "lcs-q26": "Define the state transition matrix Phi(t) = e^{At}. State and prove four important properties of the state transition matrix and calculate e^{At} for a given 2x2 system matrix using the Laplace transform method."
}

LCS_BYHEART = {
    "lcs-q1": {
        "eq": r"$$S^T_G = \frac{1}{1 + G(s)H(s)}, \quad S^T_H = \frac{-G(s)H(s)}{1 + G(s)H(s)}$$",
        "text": r"Negative feedback reduces sensitivity to forward plant drifts by loop factor $(1+GH)$, but sensitivity to feedback sensor drift remains high ($\approx -1$), demanding precision sensor components."
    },
    "lcs-q2": {
        "eq": r"$$F(t) = M \ddot{x} + B \dot{x} + K x \longleftrightarrow e(t) = L \ddot{q} + R \dot{q} + \frac{1}{C}q \longleftrightarrow j(t) = C \ddot{\phi} + G \dot{\phi} + \frac{1}{L}\phi$$",
        "text": r"<strong>F-V Analogy (Mesh):</strong> $F \leftrightarrow v, M \leftrightarrow L, B \leftrightarrow R, K \leftrightarrow 1/C, v \leftrightarrow i, x \leftrightarrow q$.<br><strong>F-I Analogy (Nodal):</strong> $F \leftrightarrow i, M \leftrightarrow C, B \leftrightarrow G=1/R, K \leftrightarrow 1/L, v \leftrightarrow v_n, x \leftrightarrow \phi$."
    },
    "lcs-q3": {
        "eq": r"$$\begin{bmatrix} M_1 s^2 + (B_1 + B_2)s + (K_1 + K_2) & -(B_2 s + K_2) \\ -(B_2 s + K_2) & M_2 s^2 + (B_2 + B_3)s + K_2 \end{bmatrix} \begin{bmatrix} X_1(s) \\ X_2(s) \end{bmatrix} = \begin{bmatrix} F(s) \\ 0 \end{bmatrix}$$",
        "text": r"Coupled mechanical systems produce an impedance matrix whose determinant $\Delta(s) = 0$ yields the characteristic equation, with transfer function $\frac{X_2(s)}{F(s)} = \frac{B_2 s + K_2}{\Delta(s)}$."
    },
    "lcs-q4": {
        "eq": r"$$\frac{C(s)}{R(s)} = \frac{G(s)}{1 \pm G(s)H(s)}, \quad \frac{C(s)}{R(s)} = \frac{G_1 G_2 G_3 G_4}{1 + G_3 H_1 + G_2 G_3 G_4 H_2 + G_1 G_2 G_3 G_4}$$",
        "text": r"Block diagram reduction simplifies multi-loop topologies by combining series blocks ($G_1 G_2$), parallel blocks ($G_1 \pm G_2$), and closing negative feedback loops ($G / (1 + GH)$)."
    },
    "lcs-q5": {
        "eq": r"$$T = \frac{1}{\Delta} \sum_{k=1}^N P_k \Delta_k, \quad \Delta = 1 - \sum L_a + \sum L_b L_c - \sum L_d L_e L_f + \dots$$",
        "text": r"Mason's Gain Formula computes transfer functions by graph inspection without block algebra, where $P_k$ is forward path gain, $\Delta$ is graph determinant, and $\Delta_k$ is the non-touching cofactor of path $k$."
    },
    "lcs-q6": {
        "eq": r"$$c(t) = 1 - e^{-t/T}, \quad c(T) = 63.2\%, \quad c(2T) = 86.5\%, \quad c(3T) = 95.0\%, \quad c(4T) = 98.2\%$$",
        "text": r"A first-order step response approaches unity exponentially, reaching 63.2% of its final value in one time constant $T$ and entering the 2% tolerance band at $t = 4T$."
    },
    "lcs-q7": {
        "eq": r"$$c(t) = 1 - \frac{e^{-\zeta \omega_n t}}{\sqrt{1 - \zeta^2}} \sin(\omega_d t + \theta), \quad \omega_d = \omega_n \sqrt{1 - \zeta^2}, \quad \theta = \cos^{-1}(\zeta) = \tan^{-1}\left(\frac{\sqrt{1-\zeta^2}}{\zeta}\right)$$",
        "text": r"Underdamped second-order step response ($0 < \zeta < 1$) consists of a constant target of 1 enveloped by an exponentially decaying sinusoidal oscillation with damping rate $\zeta\omega_n$ and frequency $\omega_d$."
    },
    "lcs-q8": {
        "eq": r"$$t_r = \frac{\pi - \theta}{\omega_d}, \quad t_p = \frac{\pi}{\omega_d}, \quad M_p = e^{-\frac{\pi\zeta}{\sqrt{1-\zeta^2}}} \times 100\%, \quad t_s(2\%) = \frac{4}{\zeta\omega_n}, \quad t_s(5\%) = \frac{3}{\zeta\omega_n}$$",
        "text": r"Peak overshoot $M_p$ depends strictly on damping ratio $\zeta$ alone, peak time $t_p$ depends on damped frequency $\omega_d$, and settling time $t_s$ is inversely proportional to attenuation factor $\zeta\omega_n$."
    },
    "lcs-q9": {
        "eq": r"$$e_{ss} = \lim_{s \to 0} \frac{s R(s)}{1 + G(s)H(s)}; \quad K_p = \lim_{s\to 0} GH, \quad K_v = \lim_{s\to 0} s GH, \quad K_a = \lim_{s\to 0} s^2 GH$$",
        "text": r"<strong>Type 0:</strong> $e_{ss}(\text{step}) = 1/(1+K_p), e_{ss}(\text{ramp}) = \infty$.<br><strong>Type 1:</strong> $e_{ss}(\text{step}) = 0, e_{ss}(\text{ramp}) = 1/K_v, e_{ss}(\text{para}) = \infty$.<br><strong>Type 2:</strong> $e_{ss}(\text{step}) = 0, e_{ss}(\text{ramp}) = 0, e_{ss}(\text{para}) = 1/K_a$."
    },
    "lcs-q10": {
        "eq": r"$$G_{PID}(s) = K_p + \frac{K_i}{s} + K_d s = \frac{K_d s^2 + K_p s + K_i}{s}$$",
        "text": r"<strong>P:</strong> Speeds response, reduces error.<br><strong>PI:</strong> Adds pole at $s=0$, raises Type by 1, eliminates step error, reduces stability.<br><strong>PD:</strong> Adds LHP zero, increases damping $\zeta$, improves stability, sensitive to noise.<br><strong>PID:</strong> Combines zero steady-state error with rapid damping."
    },
    "lcs-q11": {
        "eq": r"$$\int_0^\infty |g(t)| \, dt < \infty \iff \text{All closed-loop poles lie strictly in open LHP } (\text{Re}(s_i) < 0)$$",
        "text": r"BIBO stability requires absolute integrability of the impulse response. LHP poles decay exponentially ($e^{-\sigma t}$); RHP poles diverge ($e^{+\sigma t}$); simple imaginary axis poles yield sustained marginal oscillations."
    },
    "lcs-q12": {
        "eq": r"$$\text{Number of RHP roots} = \text{Number of sign changes in 1st column of Routh array; replace } 0 \text{ with } \epsilon > 0$$",
        "text": r"In Special Case 1, a leading zero halts division. Replace it with $\epsilon > 0$, compute subsequent rows in terms of $\epsilon$, and evaluate the signs as $\epsilon \to 0^+$. Two sign changes confirm two RHP unstable roots."
    },
    "lcs-q13": {
        "eq": r"$$A(s) = 15.75 s^2 + K_{mar} = 0 \implies \frac{dA(s)}{ds} = 31.5 s; \quad K_{mar} = 19.6875, \quad \omega_{osc} = 1.118 \text{ rad/s}$$",
        "text": r"An entire row of zeros reveals roots symmetric about the origin. Differentiate the even auxiliary polynomial $A(s)$, replace the zero row, and solve $A(s) = 0$ to find sustained oscillation frequency $\omega_{osc}$."
    },
    "lcs-q14": {
        "eq": r"$$\angle G(s)H(s) = \pm (2q+1)180^\circ, \quad |G(s)H(s)| = 1, \quad \sigma_A = \frac{\sum p_i - \sum z_j}{n - m}, \quad \theta_a = \frac{(2q+1)180^\circ}{n - m}$$",
        "text": r"Root locus plots closed-loop pole paths as gain $K$ varies $0 \to \infty$. Branches depart from open poles, approach asymptotes at angle $\theta_a$ intersecting at centroid $\sigma_A$, and break away where $dK/ds = 0$."
    },
    "lcs-q15": {
        "eq": r"$$G(s) = \frac{K}{s(s+2)(s+4)} \implies \sigma_A = -2, \quad \theta_a = 60^\circ, 180^\circ, 300^\circ, \quad s_{break} = -0.845, \quad K_{mar} = 48, \quad \omega_{cr} = \pm j 2.83$$",
        "text": r"Poles at $0, -2, -4$ collide at breakaway point $s = -0.845$ ($K=3.08$), cross $j\omega$-axis at $\pm j 2.83$ at marginal gain $K_{mar} = 48$. Stable range is $0 < K < 48$."
    },
    "lcs-q16": {
        "eq": r"$$M_r = \frac{1}{2\zeta\sqrt{1-\zeta^2}}, \quad \omega_r = \omega_n\sqrt{1-2\zeta^2}, \quad \omega_b = \omega_n\sqrt{(1-2\zeta^2) + \sqrt{4\zeta^4 - 4\zeta^2 + 2}}$$",
        "text": r"Resonant peak $M_r$ exists only for $\zeta < 0.707$ and correlates directly with time overshoot $M_p$. Bandwidth $\omega_b$ is directly proportional to natural frequency $\omega_n$ and inversely to rise time $t_r$."
    },
    "lcs-q17": {
        "eq": r"$$20\log_{10}|G(j\omega)| \text{ (dB) vs } \log\omega, \quad \text{Corner frequency } \omega_c = \frac{1}{T}, \quad \text{Slopes: } \pm 20 \text{ dB/decade}$$",
        "text": r"Bode diagrams plot magnitude in dB and phase in degrees on semi-log scales. Standard factors combine additively: simple poles break at $\omega_c = 1/T$ with $-20 \text{ dB/dec}$ slope change and $-45^\circ$ phase."
    },
    "lcs-q18": {
        "eq": r"$$\omega_{pc}: \angle G(j\omega_{pc}) = -180^\circ, \quad GM = -20\log_{10}|G(j\omega_{pc})|; \quad \omega_{gc}: |G(j\omega_{gc})| = 1, \quad PM = 180^\circ + \angle G(j\omega_{gc})$$",
        "text": r"Stable systems require $\omega_{gc} < \omega_{pc}$, giving $GM > 0 \text{ dB}$ and $PM > 0^\circ$. For $G(s) = 10/[s(1+0.1s)(1+0.05s)]$, $\omega_{pc} = 14.14 \text{ rad/s}, GM = +9.54 \text{ dB}, PM = +33.2^\circ$."
    },
    "lcs-q19": {
        "eq": r"$$\text{Type 0: } (K, 0^\circ) \to 0\angle -n(90^\circ); \quad \text{Type 1: } \infty\angle -90^\circ \to 0\angle -n(90^\circ); \quad \text{Type 2: } \infty\angle -180^\circ \to 0\angle -n(90^\circ)$$",
        "text": r"Polar plots map magnitude and phase vector locus as $\omega: 0 \to \infty$. Adding a pole introduces clockwise rotation ($-90^\circ$ lag), shifting locus toward critical $(-1, j0)$ and reducing stability."
    },
    "lcs-q20": {
        "eq": r"$$N = P - Z \implies Z = P - N \implies Z = P - N_{ccw}; \quad \text{Closed-loop stability requires } Z = 0 \implies N_{ccw} = P$$",
        "text": r"Nyquist stability theorem maps s-plane contour into $G(s)H(s)$ plane. The number of counter-clockwise encirclements of $(-1, j0)$ must equal the number of open-loop RHP poles $P$ for closed-loop stability."
    },
    "lcs-q21": {
        "eq": r"$$G_{lead}(s) = \frac{s + 1/T}{s + 1/(\alpha T)}, \quad \sin\phi_m = \frac{1-\alpha}{1+\alpha}, \quad \omega_m = \frac{1}{T\sqrt{\alpha}}, \quad 0 < \alpha < 1$$",
        "text": r"Lead compensators place zero closer to origin than pole ($\alpha < 1$), providing maximum phase lead $\phi_m = \sin^{-1}(\frac{1-\alpha}{1+\alpha})$ at geometric mean frequency $\omega_m = 1/(T\sqrt{\alpha})$ to boost bandwidth and damping."
    },
    "lcs-q22": {
        "eq": r"$$\phi_m = \gamma_{spec} - \gamma_{un} + \epsilon, \quad \alpha = \frac{1-\sin\phi_m}{1+\sin\phi_m}, \quad 20\log_{10}|G_1(j\omega_m)| = -10\log_{10}(1/\alpha)$$",
        "text": r"Lead compensator design on Bode plot selects required lead $\phi_m$ with safety margin $\epsilon \approx 5^\circ$, calculates $\alpha$, finds new crossover $\omega_m = \omega'_{gc}$ at $-10\log_{10}(1/\alpha) \text{ dB}$, and sets corner frequencies."
    },
    "lcs-q23": {
        "eq": r"$$\phi_{plant}(\omega'_{gc}) = -180^\circ + \gamma_{spec} + \epsilon, \quad \beta = 10^{\frac{|G_1|_{\text{dB}}}{20}}, \quad \omega_z = \frac{1}{T} = \frac{\omega'_{gc}}{10}, \quad \omega_p = \frac{\omega_z}{\beta}$$",
        "text": r"Lag compensator design identifies frequency $\omega'_{gc}$ where plant phase provides required margin $+ \epsilon$, attenuates gain by $\beta$, and places zero one decade below $\omega'_{gc}$ to minimize phase degradation."
    },
    "lcs-q24": {
        "eq": r"$$\dot{\mathbf{x}}(t) = A \mathbf{x}(t) + B \mathbf{u}(t), \quad \mathbf{y}(t) = C \mathbf{x}(t) + D \mathbf{u}(t), \quad \mathbf{x}(t) \in \mathbb{R}^n$$",
        "text": r"State-space represents $n$-th order dynamic systems via coupled first-order vector differential equations, accommodating MIMO architectures, initial conditions, non-linearities, and internal state observability."
    },
    "lcs-q25": {
        "eq": r"$$G(s) = C (s I - A)^{-1} B + D = \frac{C \operatorname{adj}(s I - A) B}{\det(s I - A)} + D$$",
        "text": r"Taking Laplace transforms with zero initial conditions relates state-space to transfer functions, proving that transfer function poles are identically the eigenvalues of state matrix $A$ ($\det(sI-A)=0$)."
    },
    "lcs-q26": {
        "eq": r"$$\Phi(t) = e^{At} = \mathcal{L}^{-1}\{(s I - A)^{-1}\}, \quad \Phi(0) = I, \quad \Phi^{-1}(t) = \Phi(-t), \quad \Phi(t_1 + t_2) = \Phi(t_1)\Phi(t_2)$$",
        "text": r"State transition matrix $\Phi(t) = e^{At}$ maps initial state $x(0)$ to future autonomous trajectory $x(t) = \Phi(t)x(0)$. Evaluated via inverse Laplace transform of the resolvent matrix $(sI - A)^{-1}$."
    }
}
