# -*- coding: utf-8 -*-
"""
Byheart Data and Exam Questions for Power System II (EET304)
"""

PS2_EXAM_QUESTIONS = {
    "ps2-q1": "Derive the mathematical expression for the instantaneous short-circuit current on a transmission line modeled as an RL circuit. Explain the DC offset component and the doubling effect.",
    "ps2-q2": "Explain the physical phenomena occurring during a symmetrical 3-phase fault at the terminals of an unloaded synchronous generator. Define subtransient, transient, and steady-state reactances with neat oscillogram.",
    "ps2-q3": "Define Short Circuit MVA. Explain the selection criteria for circuit breaker ratings, differentiating between rated symmetrical interrupting current and rated momentary making current.",
    "ps2-q4": "Explain the step-by-step algorithm for the formation of the Bus Impedance Matrix (Z_bus). Derive the mathematical formulas for the four types of branch additions and Kron reduction.",
    "ps2-q5": "Calculate the fault current in kA and fault MVA for a 3-phase symmetrical fault on an interconnected power system with two generators, step-up transformers, and transmission line on a 100 MVA base.",
    "ps2-q6": "State Fortescue's theorem and explain the symmetrical components transformation. Define the complex operator 'a', state its mathematical properties, and prove the invariance of complex power.",
    "ps2-q7": "Draw and explain the positive, negative, and zero sequence equivalent circuits of synchronous generators, three-phase transformers (with various winding and grounding connections), and transmission lines.",
    "ps2-q8": "Derive the expressions for sequence currents and fault current for a Single Line-to-Ground (LG) fault on phase 'a' through a fault impedance Zf. Draw the sequence network interconnection.",
    "ps2-q9": "Derive the expressions for sequence currents and fault current for a Line-to-Line (LL) fault between phases 'b' and 'c' through fault impedance Zf. Draw the sequence network interconnection.",
    "ps2-q10": "Derive the expressions for sequence currents, sequence voltages, and ground fault current for a Double Line-to-Ground (LLG) fault on phases 'b' and 'c'. Draw the sequence network interconnection.",
    "ps2-q11": "Classify the buses in a power system for load flow studies. State the known and unknown variables for each bus type and explain the formulation of Bus Admittance Matrix (Y_bus) by inspection.",
    "ps2-q12": "Derive the static real and reactive power flow equations of an n-bus power system in polar coordinates from first principles using complex power injection relations.",
    "ps2-q13": "Explain the Gauss-Seidel method for power flow solution. Derive the iterative bus voltage equation, discuss the role of acceleration factor, and explain the handling of PV buses with reactive power limits.",
    "ps2-q14": "Formulate the Newton-Raphson load flow algorithm in polar coordinates. Derive the explicit mathematical expressions for the diagonal and off-diagonal elements of the Jacobian matrix sub-blocks.",
    "ps2-q15": "State the physical assumptions underlying the Fast Decoupled Load Flow (FDLF) method. Derive the decoupled matrix equations involving B' and B'' and discuss its computational advantages.",
    "ps2-q16": "Derive the swing equation governing the rotor dynamics of a synchronous machine during transients. Define inertia constant H and angular momentum M, and express the equation in electrical radians and degrees.",
    "ps2-q17": "Derive the power-angle equation Pe = Pmax sin(delta) for a synchronous machine connected to an infinite bus. Define synchronizing power coefficient and determine the steady-state stability limit.",
    "ps2-q18": "State and prove the Equal Area Criterion (EAC) for the transient stability of a synchronous machine. Apply EAC to determine the maximum swing angle for a sudden step increase in mechanical power input.",
    "ps2-q19": "Apply the Equal Area Criterion to derive the expression for the Critical Clearing Angle (delta_cr) for a three-phase fault on a double-circuit transmission line. Obtain the critical clearing time formula.",
    "ps2-q20": "Explain the various practical methods employed in modern power systems to improve transient and dynamic stability, including fast fault clearing, auto-reclosing, dynamic braking, and FACTS devices.",
    "ps2-q21": "Develop the transfer function block diagram of an isolated single-area power system for Load Frequency Control (LFC). Derive the expression for steady-state frequency deviation following a step load change.",
    "ps2-q22": "Explain secondary frequency control and the dynamics of a two-area interconnected power system. Derive the tie-line power flow equation and define the Area Control Error (ACE) for each control area.",
    "ps2-q23": "Draw the functional block diagram of an Automatic Voltage Regulator (AVR) for a synchronous generator. State the transfer functions of each constituent component and discuss stability compensation.",
    "ps2-q24": "Formulate the economic load dispatch problem for thermal generating units neglecting transmission line losses. Using Lagrange multipliers, derive the criterion of equal incremental fuel costs.",
    "ps2-q25": "Formulate the economic dispatch problem including transmission network losses using Kron's loss formula. Derive the coordination equations and explain the physical significance of the Penalty Factor Li.",
    "ps2-q26": "Two thermal generating units have fuel cost functions C1 = 0.05 P1^2 + 20 P1 + 800 Rs/h and C2 = 0.06 P2^2 + 15 P2 + 1000 Rs/h with limits 20 <= Pi <= 120 MW. For a total load of 180 MW, find optimal generation schedule, lambda, and calculate hourly cost savings compared to equal load sharing."
}

PS2_BYHEART = {
    "ps2-q1": {
        "eq": r"$$i(t) = \frac{V_m}{|Z|} \sin(\omega t + \alpha - \theta) - \frac{V_m}{|Z|} \sin(\alpha - \theta) e^{-t/\tau}, \quad i_{peak} \approx 2 \frac{V_m}{|Z|}$$",
        "text": r"Short circuit on an RL line produces a symmetrical AC wave plus a decaying DC offset. If fault occurs at voltage zero ($\alpha - \theta = -\pi/2$), maximum DC offset causes the Doubling Effect ($i_{peak} \approx 2 I_m$)."
    },
    "ps2-q2": {
        "eq": r"$$I'' = \frac{E_g}{X_d''}, \quad I' = \frac{E_g}{X_d'}, \quad I = \frac{E_g}{X_d}, \quad E'' = V_t + j I_L X_d''$$",
        "text": r"Damper currents choke stator flux in subtransient period ($X_d''$), field currents resist in transient period ($X_d'$), settling to steady state ($X_d$). Subtransient internal voltage $E'' = V_t + j I_L X_d''$."
    },
    "ps2-q3": {
        "eq": r"$$SCMVA = \frac{MVA_{base}}{X_{th, pu}}, \quad I_{making, peak} = 1.6 \times \sqrt{2} \times I_{sc, sym} \approx 2.55 \times I_{sc, sym}$$",
        "text": r"Short Circuit MVA measures fault severity. Breaker rated making current ($2.55 I_{sc}$) withstands peak first-cycle electromechanical forces; interrupting current is evaluated at contact separation (2 to 5 cycles)."
    },
    "ps2-q4": {
        "eq": r"$$Z_{ij}^{new} = Z_{ij}^{old} - \frac{Z_{iq} Z_{qj}}{Z_{qq}}, \quad I_{f, k} = \frac{V_k(0)}{Z_{kk}}, \quad V_i^{fault} = V_i(0) - \frac{Z_{ik}}{Z_{kk}} V_k(0)$$",
        "text": r"Z_bus algorithm builds impedance matrix by adding branches in 4 topological types. Loop-closing branches (Types 3 and 4) are eliminated by Kron reduction. Driving-point impedance $Z_{kk}$ directly yields fault current."
    },
    "ps2-q5": {
        "eq": r"$$X_{th} = 0.25 \parallel 0.7035 = 0.1844 \text{ pu}, \quad I_f = 2.371 \text{ kA}, \quad SCMVA = 542.3 \text{ MVA}$$",
        "text": r"Per-unit reactance diagram combines parallel generator-transformer branches to fault bus: $X_{th} = 0.1844 \text{ pu}$, giving fault current $I_f = 2.371 \text{ kA}$ and $SCMVA = 542.3 \text{ MVA}$ on $100 \text{ MVA}$ base."
    },
    "ps2-q6": {
        "eq": r"$$V_{abc} = A V_{012}, \quad A = \begin{bmatrix} 1 & 1 & 1 \\ 1 & a^2 & a \\ 1 & a & a^2 \end{bmatrix}, \quad a = 1\angle 120^\circ, \quad 1 + a + a^2 = 0$$",
        "text": r"Fortescue's theorem resolves unbalanced 3-phase phasors into positive ($1, a^2, a$), negative ($1, a, a^2$), and zero ($1, 1, 1$) sequence sets. Complex power is strictly invariant: $S_{3\phi} = 3(V_0 I_0^* + V_1 I_1^* + V_2 I_2^*)$."
    },
    "ps2-q7": {
        "eq": r"$$Z_0 = Z_{g0} + 3 Z_n, \quad Z_1 = Z_2 = Z_{leakage} \text{ (Transformer)}, \quad Z_0 \approx 2.5 \text{ to } 3.5 \times Z_1 \text{ (Line)}$$",
        "text": r"Generator neutral grounding impedance appears as $3Z_n$ in zero-sequence network. Transformers block zero sequence unless grounded star ($Y_g$); delta ($\Delta$) circulates zero sequence internally."
    },
    "ps2-q8": {
        "eq": r"$$I_{a0} = I_{a1} = I_{a2} = \frac{E_a}{Z_1 + Z_2 + Z_0 + 3 Z_f}, \quad I_f = 3 I_{a1} = \frac{3 E_a}{Z_1 + Z_2 + Z_0 + 3 Z_f}$$",
        "text": r"Single Line-to-Ground fault enforces identical sequence currents ($I_{a0} = I_{a1} = I_{a2}$), requiring a Series interconnection of positive, negative, and zero sequence networks with $3Z_f$ inserted."
    },
    "ps2-q9": {
        "eq": r"$$I_{a0} = 0, \quad I_{a1} = -I_{a2} = \frac{E_a}{Z_1 + Z_2 + Z_f}, \quad I_f = -j\sqrt{3} I_{a1} = \frac{\sqrt{3} E_a}{Z_1 + Z_2 + Z_f} \angle -90^\circ$$",
        "text": r"Line-to-Line fault has zero sequence current ($I_{a0} = 0$). Positive and negative sequence networks connect in Parallel opposition; fault current is $\sqrt{3} I_{a1} \approx 86.6\%$ of 3-phase fault."
    },
    "ps2-q10": {
        "eq": r"$$V_{a1} = V_{a2} = V_{a0} - 3 I_{a0} Z_f, \quad I_{a1} = \frac{E_a}{Z_1 + \frac{Z_2 (Z_0 + 3 Z_f)}{Z_2 + Z_0 + 3 Z_f}}, \quad I_f = 3 I_{a0}$$",
        "text": r"Double Line-to-Ground fault enforces equal sequence voltages, requiring a Parallel interconnection of positive, negative, and zero sequence networks; total ground fault current is $3I_{a0}$."
    },
    "ps2-q11": {
        "eq": r"$$Y_{ii} = \sum_{k\ne i} y_{ik} + y_{i0}, \quad Y_{ik} = -y_{ik}; \quad \text{Slack: } |V|, \delta; \quad \text{PV: } P, |V|; \quad \text{PQ: } P, Q$$",
        "text": r"Slack bus fixes $|V|, \delta=0$ to balance losses; PV bus regulates voltage with reactive limits ($Q_{min} \le Q \le Q_{max}$); PQ bus demands real and reactive power. $Y_{bus}$ is symmetric and sparse."
    },
    "ps2-q12": {
        "eq": r"$$P_i = \sum_{k=1}^n |V_i| |V_k| |Y_{ik}| \cos(\theta_{ik} + \delta_k - \delta_i), \quad Q_i = -\sum_{k=1}^n |V_i| |V_k| |Y_{ik}| \sin(\theta_{ik} + \delta_k - \delta_i)$$",
        "text": r"Static power flow equations derived from $S_i^* = P_i - jQ_i = V_i^* \sum Y_{ik} V_k$. Real power depends primarily on angle differences ($\delta_k - \delta_i$); reactive power depends on voltage magnitudes."
    },
    "ps2-q13": {
        "eq": r"$$V_i^{(m+1)} = \frac{1}{Y_{ii}} \left[ \frac{P_i - j Q_i}{(V_i^{(m)})^*} - \sum_{k=1}^{i-1} Y_{ik} V_k^{(m+1)} - \sum_{k=i+1}^n Y_{ik} V_k^{(m)} \right], \quad V_i^{acc} = V_i^{(m)} + \alpha(V_i^{(m+1)} - V_i^{(m)})$$",
        "text": r"Gauss-Seidel substitutes updated voltages immediately, accelerated by factor $\alpha \approx 1.4 \text{ to } 1.6$. PV buses estimate $Q_i$; if $Q_i$ violates limits, bus converts to PQ type."
    },
    "ps2-q14": {
        "eq": r"$$\begin{bmatrix} \Delta P \\ \Delta Q \end{bmatrix} = \begin{bmatrix} H & N \\ M & L \end{bmatrix} \begin{bmatrix} \Delta\delta \\ \Delta|V|/|V| \end{bmatrix}, \quad H_{ii} = -Q_i - |V_i|^2 B_{ii}, \quad L_{ii} = Q_i - |V_i|^2 B_{ii}$$",
        "text": r"Newton-Raphson linearizes power flow using Jacobian matrix with quadratic convergence (3-5 iterations). Off-diagonals satisfy $M_{ik} = -N_{ik}$ and $L_{ik} = H_{ik}$."
    },
    "ps2-q15": {
        "eq": r"$$\left[\frac{\Delta P}{|V|}\right] = [B'][\Delta\delta], \quad \left[\frac{\Delta Q}{|V|}\right] = [B''][\Delta|V|], \quad R \ll X, \quad \cos(\delta_i - \delta_k) \approx 1$$",
        "text": r"Fast Decoupled Load Flow exploits $P-\delta$ and $Q-V$ physical decoupling. Matrices $B'$ and $B''$ are constant, real, symmetric, and inverted only once, accelerating computations 5-fold."
    },
    "ps2-q16": {
        "eq": r"$$\frac{2H}{\omega_s} \frac{d^2\delta}{dt^2} = P_m - P_e \quad \text{or} \quad \frac{H}{\pi f} \frac{d^2\delta}{dt^2} = P_m - P_e, \quad M = \frac{G H}{\pi f}$$",
        "text": r"Swing equation governs rotor acceleration driven by power imbalance $P_m - P_e$. Inertia constant $H$ defines kinetic energy in MJ per MVA rating, normalized across machines."
    },
    "ps2-q17": {
        "eq": r"$$P_e = \frac{|E||V|}{X} \sin\delta = P_{max} \sin\delta, \quad P_{syn} = \frac{dP_e}{d\delta} = P_{max} \cos\delta > 0 \implies 0 \le \delta < 90^\circ$$",
        "text": r"Cylindrical rotor electrical power follows sinusoidal curve peaking at $\delta = 90^\circ$. Steady-state stability requires positive synchronizing power ($P_{syn} > 0$), limiting stable operation to $\delta < 90^\circ$."
    },
    "ps2-q18": {
        "eq": r"$$\int_{\delta_0}^{\delta_{max}} (P_m - P_e) \, d\delta = 0 \implies A_1 = A_2 \quad (\text{Accelerating Area } = \text{ Decelerating Area})$$",
        "text": r"Equal Area Criterion determines transient stability without solving differential equations. Stored kinetic energy gained during acceleration ($A_1$) must be completely absorbed during deceleration ($A_2$)."
    },
    "ps2-q19": {
        "eq": r"$$\cos\delta_{cr} = \frac{P_m(\delta_{max} - \delta_0) - P_{max2}\cos\delta_0 + P_{max3}\cos\delta_{max}}{P_{max3} - P_{max2}}, \quad t_{cr} = \sqrt{\frac{2H(\delta_{cr} - \delta_0)}{\pi f P_m}}$$",
        "text": r"Critical Clearing Angle $\delta_{cr}$ defines the maximum allowable rotor advance before fault isolation. Breakers must trip before critical clearing time $t_{cr}$ to preserve transient stability."
    },
    "ps2-q20": {
        "eq": r"$$E_{acc} \propto t^2, \quad X_{eff} = X_{line} - X_C, \quad P_{max} = \frac{|E||V|}{X_{eff}}$$",
        "text": r"Stability is enhanced by 2-cycle fast fault clearing, high-speed auto-reclosing, dynamic braking resistors, fast static excitation with PSS, series capacitors, and FACTS controllers (STATCOM/SVC/TCSC)."
    },
    "ps2-q21": {
        "eq": r"$$\Delta f_{ss} = \frac{-\Delta P_L}{D + \frac{1}{R}} = \frac{-\Delta P_L}{\beta}, \quad K_p = \frac{1}{D}, \quad \tau_p = \frac{2H}{f_0 D}$$",
        "text": r"Primary governor droop leaves a steady-state frequency drop $\Delta f_{ss} = -\Delta P_L / \beta$, where $\beta = D + 1/R$ is system stiffness. Secondary integral control is required to restore frequency to $50 \text{ Hz}$."
    },
    "ps2-q22": {
        "eq": r"$$ACE_1 = \Delta P_{tie1} + B_1 \Delta f_1, \quad \Delta P_{tie12} = \frac{2\pi T_{12}}{s} (\Delta f_1 - \Delta f_2), \quad B_i = \beta_i = D_i + \frac{1}{R_i}$$",
        "text": r"In interconnected two-area systems, each area regulates its own Area Control Error ($ACE = \Delta P_{tie} + B \Delta f$) via integral control, driving steady-state frequency and tie-line deviations to zero."
    },
    "ps2-q23": {
        "eq": r"$$G_{open}(s) = \frac{K_A K_E K_F K_R}{(1 + s\tau_A)(1 + s\tau_E)(1 + s\tau_F)(1 + s\tau_R)}$$",
        "text": r"Automatic Voltage Regulator controls exciter voltage to maintain terminal voltage $|V_t|$. Rate feedback transformer stabilizers introduce phase lead to prevent oscillatory instability from exciter-generator lag poles."
    },
    "ps2-q24": {
        "eq": r"$$\frac{dC_1}{dP_1} = \frac{dC_2}{dP_2} = \dots = \frac{dC_N}{dP_N} = \lambda, \quad \sum_{i=1}^N P_i = P_D, \quad P_{i, min} \le P_i \le P_{i, max}$$",
        "text": r"Economic load dispatch neglecting losses mandates that all generating units operate at the Equal Incremental Fuel Cost $\lambda$. Constrained units are pegged at their limit, and remaining load is re-dispatched."
    },
    "ps2-q25": {
        "eq": r"$$\frac{dC_i}{dP_i} \cdot L_i = \lambda, \quad L_i = \frac{1}{1 - \frac{\partial P_L}{\partial P_i}}, \quad P_L = \sum\sum P_m B_{mn} P_n$$",
        "text": r"Economic dispatch including losses coordinates incremental fuel cost with transmission Penalty Factor $L_i$. Remote units with high incremental losses ($L_i > 1$) are backed down to optimize overall delivered cost."
    },
    "ps2-q26": {
        "eq": r"$$\lambda = 27.55 \text{ Rs/MWh}, \quad P_1 = 75.45 \text{ MW}, \quad P_2 = 104.55 \text{ MW}, \quad \text{Net Savings} = 23.27 \text{ Rs/h}$$",
        "text": r"Equal incremental cost dispatch allocates $P_1 = 75.45 \text{ MW}, P_2 = 104.55 \text{ MW}$ at $\lambda = 27.55 \text{ Rs/MWh}$, reducing generation costs by $23.27 \text{ Rs/h}$ ($203,845 \text{ Rs/year}$) over equal sharing."
    }
}
