# -*- coding: utf-8 -*-
"""
Module 5 for Power System II (EET304)
Power System Control and Economic Dispatch
"""

M5_QUESTIONS = [
    {
        "qid": "ps2-q21",
        "marks": 7,
        "type": "Long Derivation",
        "title": "Automatic Generation Control (AGC): Single-Area Load Frequency Control Modeling",
        "yt_query": "load frequency control isolated single area transfer function steady state frequency deviation",
        "img_path": "images/ps2/single_area_lfc_block_diagram.png",
        "img_caption": "Figure 5.1: Transfer Function Block Diagram of Isolated Single-Area Load Frequency Control System",
        "answer": r"""
In an interconnected electrical power grid, active power balance must be maintained continuously to preserve system frequency at nominal value ($50 \text{ Hz}$). If total electrical power demand exceeds mechanical generation, kinetic energy is drawn from the spinning rotors, causing system frequency to drop. Conversely, if generation exceeds load, frequency rises. Load Frequency Control (LFC) is the automatic control mechanism that senses frequency deviations and regulates turbine governor valves to restore equilibrium.

To derive the dynamic model of an isolated single-area power system, we formulate the transfer functions of its three constituent subsystems:

1. Speed Governor Mechanism:
The mechanical-hydraulic or electro-hydraulic flyball governor compares the actual machine frequency against reference setpoint $\Delta P_{ref}$. The speed changer position is influenced by the speed droop regulation parameter $R$:
$$\Delta P_g(s) = \frac{1}{1 + s \tau_g} \left[ \Delta P_{ref}(s) - \frac{1}{R} \Delta f(s) \right]$$
where $\tau_g$ is the governor time constant (typically 0.1 to 0.2 seconds), and $R$ is the speed regulation (droop) parameter expressed in $\text{Hz/MW}$ (or per-unit droop, typically 4% to 5%).

2. Prime Mover (Turbine) Model:
The movement of the governor main steam valve $\Delta P_g$ alters the steam mass flow rate entering the turbine stages, developing mechanical power $\Delta P_t$:
$$\Delta P_t(s) = \frac{1}{1 + s \tau_t} \Delta P_g(s)$$
where $\tau_t$ is the turbine charging time constant (typically 0.2 to 2.0 seconds).

3. Generator-Load Dynamic Model:
The net accelerating power driving the system is the difference between mechanical turbine power $\Delta P_t$ and consumer load perturbation $\Delta P_L$:
$$\Delta P_a = \Delta P_t - \Delta P_L$$
The electrical power load demanded by induction motors and industrial drives varies inherently with system frequency:
$$\Delta P_e = \Delta P_L + D \Delta f$$
where $D = \frac{\partial P_L}{\partial f}$ is the load damping constant expressed in $\text{MW/Hz}$ (or per-unit $\text{pu/Hz}$), typically 1% to 2% power change per 1% frequency change ($D \approx 1.0 \text{ to } 2.0$).
Substituting into the swing equation in per-unit:
$$\frac{2H}{f_0} \frac{d(\Delta f)}{dt} = \Delta P_t - (\Delta P_L + D \Delta f)$$
Taking the Laplace transform on both sides:
$$\left( \frac{2H}{f_0} s + D \right) \Delta f(s) = \Delta P_t(s) - \Delta P_L(s)$$
Dividing through by $D$:
$$\Delta f(s) = \frac{1/D}{1 + s \left(\frac{2H}{f_0 D}\right)} \left[ \Delta P_t(s) - \Delta P_L(s) \right] = \frac{K_p}{1 + s \tau_p} \left[ \Delta P_t(s) - \Delta P_L(s) \right]$$
where:
- Power system gain: $K_p = \frac{1}{D}$
- Power system time constant: $\tau_p = \frac{2H}{f_0 D}$ (typically 10 to 20 seconds).

Closed-Loop System Derivation for Uncontrolled Primary Droop Case:
In primary frequency control, the reference speed changer is fixed ($\Delta P_{ref}(s) = 0$). The overall closed-loop transfer function relating frequency deviation $\Delta f(s)$ to a disturbance step in load $\Delta P_L(s) = \frac{\Delta P_L}{s}$ is:
$$\Delta f(s) = \frac{- \frac{K_p}{1 + s \tau_p}}{1 + \left(\frac{1}{1 + s \tau_g}\right)\left(\frac{1}{1 + s \tau_t}\right)\left(\frac{K_p}{1 + s \tau_p}\right)\frac{1}{R}} \cdot \Delta P_L(s)$$

Evaluating Steady-State Frequency Deviation ($\Delta f_{ss}$):
Using the Final Value Theorem of Laplace transforms:
$$\Delta f_{ss} = \lim_{t \to \infty} \Delta f(t) = \lim_{s \to 0} s \Delta f(s)$$
Substituting $\Delta P_L(s) = \frac{\Delta P_L}{s}$ and setting $s \to 0$:
$$\Delta f_{ss} = \lim_{s \to 0} s \left[ \frac{-\frac{K_p}{1 + s\tau_p}}{1 + \frac{K_p / R}{(1 + s\tau_g)(1 + s\tau_t)(1 + s\tau_p)}} \cdot \frac{\Delta P_L}{s} \right]$$
$$\Delta f_{ss} = \frac{-K_p}{1 + \frac{K_p}{R}} \Delta P_L = \frac{-1/D}{1 + \frac{1/D}{R}} \Delta P_L = \frac{-1}{D + \frac{1}{R}} \Delta P_L = \frac{-\Delta P_L}{D + \frac{1}{R}}$$
Defining the Area Frequency Response Characteristic (AFRC) or system stiffness parameter:
$$\beta = D + \frac{1}{R} \text{ (in MW/Hz)}$$
The steady-state frequency drop is:
$$\Delta f_{ss} = -\frac{\Delta P_L}{\beta} = -\frac{\Delta P_L}{D + \frac{1}{R}}$$

Physical Significance:
This derivation proves that primary governor droop control inherently leaves a non-zero steady-state frequency offset ($\Delta f_{ss} \ne 0$) following any load change. Because $1/R \gg D$, the governor droop provides over 95% of the primary frequency restoring capability. To force this residual frequency error completely to zero, a secondary integral control loop must be incorporated.
"""
    },
    {
        "qid": "ps2-q22",
        "marks": 7,
        "type": "Long Derivation",
        "title": "Secondary Frequency Control and Two-Area Interconnected System LFC with ACE",
        "yt_query": "two area load frequency control tie line power flow area control error ACE",
        "img_path": "images/ps2/two_area_lfc_block_diagram.png",
        "img_caption": "Figure 5.2: Two-Area Interconnected Power System LFC with Tie-Line Power Feedback and ACE",
        "answer": r"""
While primary governor action halts dynamic frequency decay following a load surge, it leaves a permanent steady-state frequency offset ($\Delta f_{ss} = -\Delta P_L / \beta$). To eliminate this steady-state error and maintain contracted power exchanges across inter-utility tie-lines, Automatic Generation Control (AGC) introduces secondary integral control.

Secondary Frequency Control in an Isolated Area:
An integral controller operates on the frequency error $\Delta f(t)$ to adjust the speed changer setpoint $\Delta P_{ref}$:
$$\Delta P_{ref}(t) = -K_i \int_0^t \Delta f(\tau) \, d\tau \implies \Delta P_{ref}(s) = -\frac{K_i}{s} \Delta f(s)$$
Applying the Final Value Theorem to the closed-loop system:
$$\Delta f_{ss} = \lim_{s \to 0} s \Delta f(s) = 0$$
The infinite DC gain of the integrator forces the steady-state frequency deviation identically to zero ($\Delta f_{ss} = 0$), restoring system frequency precisely to $50 \text{ Hz}$.

Two-Area Interconnected Power System Dynamics:
In modern grids, neighboring control areas are linked via high-voltage AC tie-lines to share operating reserves and enhance reliability.
Let Area 1 and Area 2 have nominal voltages $|V_1|$ and $|V_2|$ interconnected by a tie-line of reactance $X_{12}$.
The real power transferred from Area 1 to Area 2 under steady-state conditions is:
$$P_{tie12} = \frac{|V_1| |V_2|}{X_{12}} \sin(\delta_1 - \delta_2)$$
For small perturbations around the nominal operating angle difference $(\delta_1^0 - \delta_2^0)$:
$$\Delta P_{tie12} = \left[ \frac{|V_1| |V_2|}{X_{12}} \cos(\delta_1^0 - \delta_2^0) \right] (\Delta\delta_1 - \Delta\delta_2) = T_{12} (\Delta\delta_1 - \Delta\delta_2)$$
where $T_{12}$ is the synchronizing torque coefficient of the tie-line (in $\text{MW/rad}$).
Because electrical angle is the time integral of frequency ($\delta(t) = 2\pi \int \Delta f dt \implies \Delta\delta(s) = \frac{2\pi}{s} \Delta f(s)$):
$$\Delta P_{tie12}(s) = \frac{2\pi T_{12}}{s} \left[ \Delta f_1(s) - \Delta f_2(s) \right]$$
By energy conservation, the tie-line power leaving Area 1 equals the power entering Area 2:
$$\Delta P_{tie21} = -\Delta P_{tie12}$$

Steady-State Analysis for Uncontrolled Case:
Let a load step increase $\Delta P_{L1}$ strike Area 1, with zero load change in Area 2 ($\Delta P_{L2} = 0$). Under primary governor control, the steady-state frequency deviations in both interconnected areas must become identical ($\Delta f_1 = \Delta f_2 = \Delta f_{ss}$):
From the steady-state power balance equations:
$$\Delta P_{m1} - \Delta P_{L1} - \Delta P_{tie12} = D_1 \Delta f_{ss} \implies -\frac{1}{R_1}\Delta f_{ss} - \Delta P_{L1} - \Delta P_{tie12} = D_1 \Delta f_{ss}$$
$$-\Delta P_{L1} - \Delta P_{tie12} = \left( D_1 + \frac{1}{R_1} \right) \Delta f_{ss} = \beta_1 \Delta f_{ss}$$
Similarly for Area 2:
$$-\Delta P_{tie21} = \Delta P_{tie12} = \left( D_2 + \frac{1}{R_2} \right) \Delta f_{ss} = \beta_2 \Delta f_{ss}$$
Summing both area balance equations eliminates tie-line power $\Delta P_{tie12}$:
$$-\Delta P_{L1} = (\beta_1 + \beta_2) \Delta f_{ss} \implies \Delta f_{ss} = \frac{-\Delta P_{L1}}{\beta_1 + \beta_2}$$
The resulting steady-state tie-line power flow is:
$$\Delta P_{tie12} = \beta_2 \Delta f_{ss} = -\frac{\beta_2}{\beta_1 + \beta_2} \Delta P_{L1}$$
This demonstrates that Area 2 inherently helps Area 1 by supplying a portion of the load increase over the tie-line.

Area Control Error (ACE):
Under tie-line bias control, each control area must absorb its own internal load changes rather than drawing permanently from its neighbor, while maintaining scheduled tie-line flows and system frequency.
The Area Control Error ($ACE$) for each area is formulated as a linear combination of tie-line power deviation and frequency deviation:
$$ACE_1 = \Delta P_{tie1} + B_1 \Delta f_1$$
$$ACE_2 = \Delta P_{tie2} + B_2 \Delta f_2$$
where $B_1$ and $B_2$ are the frequency bias factors.
To achieve completely decoupled control, the frequency bias factor is set exactly equal to the area frequency response characteristic ($B_i = \beta_i = D_i + 1/R_i$).
The secondary integral controllers integrate the respective ACE signals:
$$\Delta P_{ref1} = -K_{i1} \int ACE_1 \, dt, \quad \Delta P_{ref2} = -K_{i2} \int ACE_2 \, dt$$
Under steady state ($ACE_1 = 0$ and $ACE_2 = 0$), both conditions are simultaneously satisfied:
$$\Delta f_{ss} = 0 \quad \text{and} \quad \Delta P_{tie, ss} = 0$$
Each area successfully adjusts its own generation to meet its local load change.
"""
    },
    {
        "qid": "ps2-q23",
        "marks": 3,
        "type": "Short Answer",
        "title": "Automatic Voltage Regulator (AVR): Subsystem Transfer Functions and Block Diagram",
        "yt_query": "automatic voltage regulator AVR excitation system transfer functions block diagram",
        "img_path": "images/ps2/avr_closed_loop_model.png",
        "img_caption": "Figure 5.3: Closed-Loop Block Diagram of Excitation System and Automatic Voltage Regulator",
        "answer": r"""
While Load Frequency Control (LFC) regulates real power and system frequency, the Automatic Voltage Regulator (AVR) governs the excitation system of a synchronous generator to maintain terminal voltage magnitude $|V_t|$ within strict operating limits ($\pm 2\%$) under changing reactive power loads.

The AVR is a closed-loop negative feedback servomechanism. Its primary functional subsystems and linearized transfer functions are modeled as follows:

1. Potential Transformer and Rectifier Sensor:
Measures the three-phase terminal voltage $V_t$, rectifies it, and filters high-frequency ripple. It is modeled as a simple first-order lag:
$$V_s(s) = \frac{K_R}{1 + s \tau_R} V_t(s)$$
where sensor gain $K_R \approx 1.0$, and sensor time constant $\tau_R$ is very small (0.01 to 0.05 seconds).

2. Voltage Error Comparator and Magnetic/Electronic Amplifier:
The sensed feedback voltage $V_s$ is compared against reference setpoint $V_{ref}$ to produce error $\Delta V = V_{ref} - V_s$. The error is amplified to drive the exciter:
$$V_a(s) = \frac{K_A}{1 + s \tau_A} \Delta V(s) = \frac{K_A}{1 + s \tau_A} [V_{ref}(s) - V_s(s)]$$
where amplifier gain $K_A$ is large (typically 10 to 400), and time constant $\tau_A$ is small (0.02 to 0.1 seconds).

3. Exciter System (Brushless AC or Static DC Exciter):
The exciter supplies DC current to the synchronous generator rotor field winding. Modern brushless exciters consist of an inverted alternator and rotating diode bridge:
$$V_f(s) = \frac{K_E}{1 + s \tau_E} V_a(s)$$
where exciter gain $K_E \approx 1.0$, and time constant $\tau_E$ ranges from 0.4 to 1.0 seconds.

4. Synchronous Generator Field and Armature Reaction Dynamics:
The generator field winding voltage $V_f$ produces field current, developing internal armature flux and open-circuit terminal voltage. Neglecting saturation, the transfer function relating terminal voltage to field excitation is:
$$V_t(s) = \frac{K_F}{1 + s \tau_F} V_f(s)$$
where generator field time constant $\tau_F$ is relatively large, ranging from 1.0 to 5.0 seconds.

Overall Open-Loop and Closed-Loop Transfer Functions:
The open-loop transfer function of the uncompensated AVR is:
$$G_{open}(s) = \frac{K_A K_E K_F K_R}{(1 + s\tau_A)(1 + s\tau_E)(1 + s\tau_F)(1 + s\tau_R)} \approx \frac{K}{(1 + s\tau_A)(1 + s\tau_E)(1 + s\tau_F)}$$
The closed-loop transfer function is:
$$\frac{V_t(s)}{V_{ref}(s)} = \frac{G(s)}{1 + G(s) H(s)}$$

Stability Analysis and Transient Compensation:
Because the loop contains three or four cascaded lag poles (with $\tau_F$ and $\tau_E$ dominating), increasing the amplifier gain $K_A$ to reduce steady-state terminal voltage error ($e_{ss} = \frac{1}{1 + K_A}$) inevitably pushes closed-loop poles across the imaginary axis into the right half plane, causing oscillatory instability.
To ensure stable transient performance, a derivative feedback stabilizer (rate feedback transformer) with transfer function $\frac{s K_{st}}{1 + s \tau_{st}}$ is connected across the exciter output terminals back to the amplifier summing junction, providing phase lead compensation that damps oscillations and ensures rapid terminal voltage recovery.
"""
    },
    {
        "qid": "ps2-q24",
        "marks": 7,
        "type": "Long Derivation",
        "title": "Economic Load Dispatch Neglecting Losses: Lagrangian Formulation and Equal Incremental Cost",
        "yt_query": "economic load dispatch neglecting losses lagrange multiplier equal incremental fuel cost",
        "img_path": "images/ps2/economic_dispatch_losses_neglected.png",
        "img_caption": "Figure 5.4: Equal Incremental Fuel Cost Criterion for Economic Load Allocation across Units",
        "answer": r"""
The fundamental objective of Economic Load Dispatch (ELD) is to allocate the total system power demand among all available committed generating units in an electrical utility in such a manner that the total operational fuel cost is strictly minimized, while satisfying all physical generation limits and power balance constraints.

Problem Formulation:
Consider a thermal power station comprising $N$ generating units supplying a total consumer load demand $P_D$.
Let $C_i(P_i)$ represent the hourly fuel cost function of generating unit $i$ (in $\text{Rs/h}$ or $\$ \text{/h}$), modeled by the quadratic relationship:
$$C_i(P_i) = \alpha_i + \beta_i P_i + \gamma_i P_i^2 \text{ Rs/h}$$
where $\alpha_i, \beta_i, \gamma_i$ are empirical fuel cost coefficients.
The overall objective function to be minimized is the total generation cost:
$$\text{Minimize } C_t = \sum_{i=1}^N C_i(P_i) = C_1(P_1) + C_2(P_2) + \dots + C_N(P_N)$$

Subject to Constraints:
1. Equality Constraint (Power Balance): Neglecting transmission network line losses ($P_L \approx 0$), total generation must strictly equal total consumer demand:
$$\sum_{i=1}^N P_i = P_D \implies \phi(P_1, P_2, \dots, P_N) = \sum_{i=1}^N P_i - P_D = 0$$
2. Inequality Constraints (Generator Operating Limits): Each thermal turbine-generator has lower physical limits (boiler flame stability, minimum steam flow) and upper thermal ratings:
$$P_{i,min} \le P_i \le P_{i,max} \quad \forall i = 1, 2, \dots, N$$

Mathematical Derivation using the Method of Lagrange Multipliers:
To convert this constrained optimization problem into an unconstrained formulation, we introduce the Lagrange Multiplier $\lambda$ and construct the Lagrangian function $\mathcal{L}$:
$$\mathcal{L}(P_1, P_2, \dots, P_N, \lambda) = C_t - \lambda \cdot \phi = \sum_{i=1}^N C_i(P_i) - \lambda \left( \sum_{i=1}^N P_i - P_D \right)$$

Enforcing the Necessary Conditions for Optimality:
For $\mathcal{L}$ to attain a local minimum, its partial derivatives with respect to all independent variables ($P_1, \dots, P_N$) and the multiplier $\lambda$ must vanish simultaneously:
1. Differentiating with respect to $P_i$:
$$\frac{\partial\mathcal{L}}{\partial P_i} = \frac{\partial}{\partial P_i} \left[ \sum_{k=1}^N C_k(P_k) \right] - \lambda \frac{\partial}{\partial P_i} \left[ \sum_{k=1}^N P_k - P_D \right] = 0$$
Because individual unit cost functions are uncoupled ($\frac{\partial C_k}{\partial P_i} = 0$ for $k \ne i$):
$$\frac{dC_i}{dP_i} - \lambda(1) = 0 \implies \frac{dC_i}{dP_i} = \lambda \quad \forall i = 1, 2, \dots, N$$
2. Differentiating with respect to $\lambda$:
$$\frac{\partial\mathcal{L}}{\partial \lambda} = -\left( \sum_{i=1}^N P_i - P_D \right) = 0 \implies \sum_{i=1}^N P_i = P_D$$

The Equal Incremental Fuel Cost Criterion:
The necessary condition for optimum economic operation when transmission losses are neglected is that all generating units must operate at the exact same Incremental Fuel Cost ($\lambda$):
$$\frac{dC_1}{dP_1} = \frac{dC_2}{dP_2} = \frac{dC_3}{dP_3} = \dots = \frac{dC_N}{dP_N} = \lambda$$
where $\frac{dC_i}{dP_i} = \beta_i + 2\gamma_i P_i$ is the Incremental Cost (in $\text{Rs/MWh}$).
The economic multiplier $\lambda$ represents the marginal cost of supplying the next incremental megawatt of power to the grid.

Incorporation of Generator Inequality Constraints:
When unit operating limits $P_{i,min} \le P_i \le P_{i,max}$ are active, the Kuhn-Tucker optimality conditions govern the dispatch:
- If $\frac{dC_i}{dP_i} = \lambda$, then $P_{i,min} < P_i < P_{i,max}$ (unit is regulating inside its limits).
- If calculated $P_i > P_{i,max}$, the unit cannot supply the optimal power; clamp $P_i = P_{i,max}$. Its incremental cost satisfies $\frac{dC_i}{dP_i} \le \lambda$.
- If calculated $P_i < P_{i,min}$, the unit cannot be backed down further; clamp $P_i = P_{i,min}$. Its incremental cost satisfies $\frac{dC_i}{dP_i} \ge \lambda$.
Any unit pegged at its boundary is removed from further economic adjustment; its generation is subtracted from total demand, and the remaining load is re-dispatched economically among the unconstrained units at a revised $\lambda$.
"""
    },
    {
        "qid": "ps2-q25",
        "marks": 7,
        "type": "Long Derivation",
        "title": "Economic Dispatch Including Losses: Kron's Loss Formula and Penalty Factor Derivation",
        "yt_query": "economic load dispatch including transmission losses penalty factor kron loss formula",
        "img_path": "images/ps2/economic_dispatch_losses_penalty.png",
        "img_caption": "Figure 5.5: Economic Coordination with Transmission Loss Penalty Factors",
        "answer": r"""
In widespread electrical power grids where generating plants are geographically separated from major load centers by hundreds of kilometers, transmission network line losses ($P_L$) cannot be neglected. A generating station with exceptionally low fuel costs may be located so far from the consumer that the $I^2 R$ transmission losses incurred in wheeling its power negate its fuel economy. Therefore, economic dispatch algorithms must coordinate unit fuel costs with marginal transmission losses.

Kron's Transmission Loss Formula:
Total three-phase active power transmission losses are expressed as a quadratic function of generator outputs using Kron's B-Loss Formula:
$$P_L = \sum_{m=1}^N \sum_{n=1}^N P_m B_{mn} P_n + \sum_{n=1}^N B_{n0} P_n + B_{00}$$
where $B_{mn}$ are the transmission loss coefficients (in $\text{MW}^{-1}$), $B_{n0}$ are linear loss coefficients, and $B_{00}$ is a constant representing no-load shunt losses. In matrix notation:
$$P_L = P^T [B] P + B_0^T P + B_{00}$$

Mathematical Formulation of Economic Dispatch with Losses:
The objective is to minimize total generation fuel cost:
$$\text{Minimize } C_t = \sum_{i=1}^N C_i(P_i)$$
Subject to the exact real power balance equality constraint including grid losses:
$$\sum_{i=1}^N P_i = P_D + P_L \implies \sum_{i=1}^N P_i - P_D - P_L = 0$$

Lagrangian Formulation:
Formulating the Lagrangian function with multiplier $\lambda$:
$$\mathcal{L}(P_1, \dots, P_N, \lambda) = \sum_{i=1}^N C_i(P_i) - \lambda \left( \sum_{i=1}^N P_i - P_D - P_L \right)$$

Enforcing the Optimality Conditions:
Differentiating $\mathcal{L}$ with respect to generator output $P_i$:
$$\frac{\partial\mathcal{L}}{\partial P_i} = \frac{dC_i}{dP_i} - \lambda \left( \frac{\partial}{\partial P_i} \sum_{k=1}^N P_k - 0 - \frac{\partial P_L}{\partial P_i} \right) = 0$$
$$\frac{dC_i}{dP_i} - \lambda \left( 1 - \frac{\partial P_L}{\partial P_i} \right) = 0$$
where $\frac{\partial P_L}{\partial P_i}$ is the Incremental Transmission Loss (ITL) of plant $i$.
Rearranging terms:
$$\frac{dC_i}{dP_i} = \lambda \left( 1 - \frac{\partial P_L}{\partial P_i} \right)$$
Dividing both sides by $\left( 1 - \frac{\partial P_L}{\partial P_i} \right)$:
$$\frac{dC_i}{dP_i} \cdot \left[ \frac{1}{1 - \frac{\partial P_L}{\partial P_i}} \right] = \lambda$$

Definition of the Penalty Factor ($L_i$):
We define the Penalty Factor $L_i$ for generating plant $i$ as:
$$L_i = \frac{1}{1 - \frac{\partial P_L}{\partial P_i}}$$
The governing optimality criterion is formulated as the Coordination Equations:
$$\frac{dC_i}{dP_i} \cdot L_i = \lambda \quad \forall i = 1, 2, \dots, N$$
$$\frac{dC_1}{dP_1} L_1 = \frac{dC_2}{dP_2} L_2 = \dots = \frac{dC_N}{dP_N} L_N = \lambda$$

Physical Significance of the Penalty Factor:
1. Plant Close to Load Center: If generating unit $i$ is situated directly at a major load center, transmitting its power incurs zero incremental loss ($\frac{\partial P_L}{\partial P_i} \approx 0$). Consequently, its penalty factor is unity: $L_i \approx 1.0$. The unit is dispatched at its raw incremental fuel cost.
2. Remote Plant with High Transmission Loss: If unit $j$ is situated far away over heavily loaded lines, increasing its generation increases transmission losses ($\frac{\partial P_L}{\partial P_j} > 0$). This forces the denominator $\left(1 - \frac{\partial P_L}{\partial P_j}\right) < 1$, making its penalty factor strictly greater than unity ($L_j > 1.0$). Since $\frac{dC_j}{dP_j} = \frac{\lambda}{L_j} < \lambda$, the remote generator is penalized and forced to operate at a lower incremental cost, backing down its generation.
3. Counter-Flow Relief: In rare network topologies, increasing generation at a specific bus unloads congested lines, actually reducing net losses ($\frac{\partial P_L}{\partial P_k} < 0$). In this case, $L_k < 1.0$, encouraging the system to increase dispatch from that unit.

Thus, the coordination equations seamlessly balance thermodynamic fuel cost against electrical transmission efficiency.
"""
    },
    {
        "qid": "ps2-q26",
        "marks": 7,
        "type": "Long Derivation",
        "title": "Complete Numerical Problem: Economic Load Dispatch with Cost Comparison",
        "yt_query": "economic dispatch numerical problem solved example fuel cost comparison savings",
        "img_path": "images/ps2/economic_dispatch_numerical.png",
        "img_caption": "Figure 5.6: Generation Allocation Curves and Cost Savings under Optimal Economic Dispatch",
        "answer": r"""
Consider a classic KTU university examination problem:
A power station has two thermal generating units supplying a total system demand of $P_D = 180 \text{ MW}$. The quadratic fuel cost functions of the units are given by:
$$C_1(P_1) = 0.05 P_1^2 + 20 P_1 + 800 \text{ Rs/h}$$
$$C_2(P_2) = 0.06 P_2^2 + 15 P_2 + 1000 \text{ Rs/h}$$
The operating limits of both generating units are:
$$20 \text{ MW} \le P_1 \le 120 \text{ MW}$$
$$20 \text{ MW} \le P_2 \le 120 \text{ MW}$$
Neglecting transmission losses, determine:
(i) The incremental fuel cost equations for each unit.
(ii) The optimal economic generation schedule ($P_1$ and $P_2$) and the system marginal cost $\lambda$.
(iii) The total hourly fuel cost under optimal economic dispatch.
(iv) The total hourly fuel cost if the load is shared equally between the units ($P_1 = P_2 = 90 \text{ MW}$).
(v) The net monetary savings in Rs/h achieved by deploying economic dispatch.

Step 1: Formulate Incremental Fuel Cost Equations:
Differentiating the individual cost functions with respect to power output:
- For Unit 1:
  $$\frac{dC_1}{dP_1} = \frac{d}{dP_1}\left(0.05 P_1^2 + 20 P_1 + 800\right) = 0.10 P_1 + 20 \text{ Rs/MWh}$$
- For Unit 2:
  $$\frac{dC_2}{dP_2} = \frac{d}{dP_2}\left(0.06 P_2^2 + 15 P_2 + 1000\right) = 0.12 P_2 + 15 \text{ Rs/MWh}$$

Step 2: Apply the Equal Incremental Cost Criterion:
For optimal economic dispatch neglecting losses:
$$\frac{dC_1}{dP_1} = \frac{dC_2}{dP_2} = \lambda$$
$$0.10 P_1 + 20 = \lambda \implies 0.10 P_1 = \lambda - 20 \implies P_1 = \frac{\lambda - 20}{0.10} = 10\lambda - 200$$
$$0.12 P_2 + 15 = \lambda \implies 0.12 P_2 = \lambda - 15 \implies P_2 = \frac{\lambda - 15}{0.12} = \frac{100}{12}\lambda - \frac{1500}{12} = 8.3333\lambda - 125$$

Step 3: Enforce the Power Balance Constraint:
Total generation must equal total demand:
$$P_1 + P_2 = P_D = 180 \text{ MW}$$
Substituting the expressions for $P_1$ and $P_2$ in terms of $\lambda$:
$$(10\lambda - 200) + (8.3333\lambda - 125) = 180$$
$$18.3333\lambda - 325 = 180$$
$$18.3333\lambda = 180 + 325 = 505$$
$$\lambda = \frac{505}{18.3333} = \frac{505}{55/3} = \frac{1515}{55} = \frac{303}{11} \approx 27.5455 \text{ Rs/MWh}$$

Step 4: Calculate Optimal Generation Allocations:
- For Unit 1:
  $$P_1 = 10(27.5455) - 200 = 275.455 - 200 = 75.455 \text{ MW}$$
- For Unit 2:
  $$P_2 = 8.3333(27.5455) - 125 = \frac{100}{12}\left(\frac{303}{11}\right) - 125 = \frac{30300}{132} - 125 = 229.545 - 125 = 104.545 \text{ MW}$$

Check Power Balance and Unit Limits:
- Total power: $P_1 + P_2 = 75.455 + 104.545 = 180.000 \text{ MW} = P_D$.
- Check limits:
  $20 \le P_1 (75.455) \le 120$ (Satisfied).
  $20 \le P_2 (104.545) \le 120$ (Satisfied).
Both units operate strictly within their allowed operating boundaries.

Step 5: Compute Total Fuel Cost under Economic Dispatch:
- Cost of Unit 1:
  $$C_1(75.455) = 0.05(75.455)^2 + 20(75.455) + 800$$
  $$C_1 = 0.05(5693.46) + 1509.10 + 800 = 284.67 + 1509.10 + 800 = 2593.77 \text{ Rs/h}$$
- Cost of Unit 2:
  $$C_2(104.545) = 0.06(104.545)^2 + 15(104.545) + 1000$$
  $$C_2 = 0.06(10929.65) + 1568.18 + 1000 = 655.78 + 1568.18 + 1000 = 3223.96 \text{ Rs/h}$$
- Total Economic Operating Cost:
  $$C_{total, economic} = C_1 + C_2 = 2593.77 + 3223.96 = 5817.73 \text{ Rs/h}$$

Step 6: Compute Fuel Cost under Equal Load Sharing ($P_1 = P_2 = 90 \text{ MW}$):
If both generators simply share the load equally:
- Cost of Unit 1 at $90 \text{ MW}$:
  $$C_1(90) = 0.05(90)^2 + 20(90) + 800 = 0.05(8100) + 1800 + 800 = 405 + 1800 + 800 = 3005.00 \text{ Rs/h}$$
- Cost of Unit 2 at $90 \text{ MW}$:
  $$C_2(90) = 0.06(90)^2 + 15(90) + 1000 = 0.06(8100) + 1350 + 1000 = 486 + 1350 + 1000 = 2836.00 \text{ Rs/h}$$
- Total Cost under Equal Sharing:
  $$C_{total, equal} = 3005.00 + 2836.00 = 5841.00 \text{ Rs/h}$$

Step 7: Determine Net Hourly Monetary Savings:
$$\text{Net Savings} = C_{total, equal} - C_{total, economic} = 5841.00 - 5817.73 = 23.27 \text{ Rs/h}$$
Annual Cost Savings:
$$\text{Annual Savings} = 23.27 \text{ Rs/h} \times 24 \text{ h/day} \times 365 \text{ days/year} \approx 203,845 \text{ Rs/year}$$
This complete numerical derivation demonstrates the concrete financial savings delivered by the equal incremental cost criterion in utility system operation.
"""
    }
]
