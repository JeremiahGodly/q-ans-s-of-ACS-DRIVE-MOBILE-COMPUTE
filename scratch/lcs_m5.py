# -*- coding: utf-8 -*-
"""
Module 5 for Linear Control Systems (EET302)
Compensator Design and State Space Basics
"""

M5_QUESTIONS = [
    {
        "qid": "lcs-q21",
        "marks": 3,
        "type": "Short Answer",
        "title": "Compensator Networks: Phase Lead, Phase Lag, and Lead-Lag Characteristics",
        "yt_query": "phase lead phase lag compensator maximum phase lead phi_m derivation control systems",
        "img_path": "images/lcs/lead_lag_compensator_circuits.png",
        "img_caption": "Figure 5.1: Passive RC Circuits and s-Plane Pole-Zero Configurations for Lead and Lag Networks",
        "answer": r"""
In feedback control system design, simple gain adjustments frequently cannot satisfy both steady-state accuracy and transient response specifications simultaneously. Compensators are auxiliary physical hardware networks or digital filter algorithms introduced into the control loop to reshape the overall frequency response and open-loop pole-zero pattern.

1. Phase Lead Compensator:
A passive phase-lead network consists of a parallel combination of resistor $R_1$ and capacitor $C$, connected in series with a resistor $R_2$. The voltage transfer function is derived by voltage division:
$$G_c(s) = \frac{V_o(s)}{V_i(s)} = \frac{R_2}{R_2 + \frac{R_1 \cdot \frac{1}{sC}}{R_1 + \frac{1}{sC}}} = \frac{R_2(1 + s R_1 C)}{R_2(1 + s R_1 C) + R_1} = \frac{R_2(1 + s R_1 C)}{(R_1 + R_2) + s R_1 R_2 C}$$
Factoring out $(R_1 + R_2)$:
$$G_c(s) = \frac{R_2}{R_1 + R_2} \cdot \frac{1 + s R_1 C}{1 + s \left(\frac{R_1 R_2}{R_1 + R_2}\right) C}$$
Defining the time constant $T = R_1 C$ and the attenuation factor $\alpha = \frac{R_2}{R_1 + R_2} < 1$:
$$G_c(s) = \alpha \cdot \frac{1 + sT}{1 + s \alpha T} = \frac{s + \frac{1}{T}}{s + \frac{1}{\alpha T}}$$
Since $\alpha < 1$, the zero at $s = -1/T$ is closer to the origin than the pole at $s = -1/(\alpha T)$.
Substituting $s = j\omega$, the phase angle is:
$$\phi(\omega) = \tan^{-1}(\omega T) - \tan^{-1}(\alpha \omega T)$$
Because $\alpha < 1$, $\phi(\omega) > 0$ for all $\omega > 0$, generating positive phase lead.
To find the frequency $\omega_m$ where the maximum phase lead $\phi_m$ occurs, we maximize $\tan\phi$:
$$\tan\phi = \frac{\omega T - \alpha \omega T}{1 + \alpha \omega^2 T^2} = \frac{(1 - \alpha)\omega T}{1 + \alpha \omega^2 T^2}$$
Differentiating with respect to $\omega$ and setting the numerator derivative to zero:
$$\frac{d}{d\omega} \left[\frac{\omega}{1 + \alpha \omega^2 T^2}\right] = \frac{(1 + \alpha \omega^2 T^2)(1) - \omega(2\alpha \omega T^2)}{(1 + \alpha \omega^2 T^2)^2} = \frac{1 - \alpha \omega^2 T^2}{(1 + \alpha \omega^2 T^2)^2} = 0$$
$$1 - \alpha \omega_m^2 T^2 = 0 \implies \omega_m = \frac{1}{T \sqrt{\alpha}}$$
The frequency $\omega_m$ is the geometric mean of the corner frequencies: $\omega_m = \sqrt{\frac{1}{T} \cdot \frac{1}{\alpha T}}$.
Substituting $\omega_m = \frac{1}{T\sqrt{\alpha}}$ back into the expression for $\tan\phi_m$:
$$\tan\phi_m = \frac{(1 - \alpha) \frac{1}{\sqrt{\alpha}}}{1 + \alpha \left(\frac{1}{\alpha}\right)} = \frac{1 - \alpha}{2\sqrt{\alpha}}$$
Constructing a right-angled triangle with opposite side $(1 - \alpha)$ and adjacent side $2\sqrt{\alpha}$, the hypotenuse is $\sqrt{(1 - \alpha)^2 + 4\alpha} = \sqrt{1 - 2\alpha + \alpha^2 + 4\alpha} = \sqrt{(1 + \alpha)^2} = 1 + \alpha$.
Thus, the maximum phase lead angle is given by the celebrated relation:
$$\sin\phi_m = \frac{1 - \alpha}{1 + \alpha} \iff \alpha = \frac{1 - \sin\phi_m}{1 + \sin\phi_m}$$
The magnitude at $\omega_m$ is $|G_c(j\omega_m)| = \sqrt{\alpha}$, corresponding to a attenuation of $20\log_{10}\sqrt{\alpha} = -10\log_{10}(1/\alpha) \text{ dB}$.

2. Phase Lag Compensator:
A passive phase-lag network swaps the placement: a series combination of $R_1$ and $C$ connects in parallel with $R_2$ across the output terminals. Its transfer function is:
$$G_c(s) = \frac{s + \frac{1}{T}}{s + \frac{1}{\beta T}} = \frac{1 + sT}{1 + s\beta T}, \quad \text{where } \beta > 1$$
In a lag compensator, the pole at $s = -1/(\beta T)$ is located much closer to the origin than the zero at $s = -1/T$. It introduces negative phase lag at intermediate frequencies while providing high attenuation (gain reduction by $20\log_{10}\beta \text{ dB}$) at high frequencies.

Comparison of Compensators:
- Lead Compensator: Increases system bandwidth, speeds up transient response, improves damping ratio $\zeta$ and phase margin. Trade-off: Amplifies high-frequency noise and increases maximum actuator effort.
- Lag Compensator: Drastically suppresses high-frequency loop gain, permitting high open-loop gain to minimize steady-state error without destabilizing the system. Trade-off: Reduces closed-loop bandwidth and slows down transient response.
- Lead-Lag Compensator: Combines both networks in cascade ($G_c(s) = \frac{s + 1/T_1}{s + 1/(\alpha T_1)} \cdot \frac{s + 1/T_2}{s + 1/(\beta T_2)}$ with $\alpha < 1, \beta > 1$), simultaneously providing high steady-state precision and fast transient damping.
"""
    },
    {
        "qid": "lcs-q22",
        "marks": 7,
        "type": "Long Derivation",
        "title": "Bode Plot Design Procedure of a Phase Lead Compensator",
        "yt_query": "design of lead compensator using bode plot control systems step by step",
        "img_path": "images/lcs/lead_compensator_design_bode.png",
        "img_caption": "Figure 5.2: Bode Magnitude and Phase Reshaping during Phase Lead Compensator Synthesis",
        "answer": r"""
The frequency-domain synthesis of a phase lead compensator reshapes the open-loop frequency response to satisfy simultaneous requirements on steady-state accuracy (such as static velocity error constant $K_v$) and relative stability (phase margin $PM$).

Consider the standard lead compensator transfer function:
$$G_c(s) = \frac{s + \frac{1}{T}}{s + \frac{1}{\alpha T}} = \frac{1 + sT}{1 + s\alpha T}, \quad 0 < \alpha < 1$$
Because the DC gain of this network as $s \to 0$ is $1$, introducing the compensator does not alter the static error constants if the loop gain is maintained.

Step-by-Step Algorithmic Design Procedure:
Step 1: Determine the Open-Loop Gain $K$:
Evaluate the required open-loop amplifier gain $K$ to satisfy the specified steady-state error or error constant. For instance, if a velocity error constant $K_v$ is specified:
$$K_v = \lim_{s \to 0} s G(s) \implies K = \text{evaluated value}$$
Define the uncompensated system transfer function with gain $K$ incorporated as $G_1(s) = K G(s)$.

Step 2: Plot the Bode Diagram of the Uncompensated System:
Construct the asymptotic magnitude plot and phase plot of $G_1(j\omega)$. From this plot, determine:
- The uncompensated gain crossover frequency $\omega_{gc}$.
- The uncompensated phase margin $\gamma_{un} = 180^\circ + \angle G_1(j\omega_{gc})$.

Step 3: Calculate the Required Phase Lead $\phi_m$:
Let $\gamma_{spec}$ denote the desired closed-loop phase margin specified by the designer. Adding the lead compensator introduces phase lead, but its high-frequency gain will shift the gain crossover frequency to a higher value where the plant has greater phase lag. To counteract this destabilizing shift, an empirical safety margin $\epsilon \approx 5^\circ \text{ to } 8^\circ$ is added:
$$\phi_m = \gamma_{spec} - \gamma_{un} + \epsilon$$

Step 4: Determine the Attenuation Factor $\alpha$:
Using the derived trigonometric relation:
$$\alpha = \frac{1 - \sin\phi_m}{1 + \sin\phi_m}$$
Note: If $\phi_m > 60^\circ$, a single-stage lead network yields an excessively small $\alpha$, causing severe noise amplification. In such cases, two identical cascaded lead networks each providing $\phi_m / 2$ should be designed.

Step 5: Identify the New Gain Crossover Frequency $\omega'_{gc}$:
The lead compensator introduces a magnitude boost of $+10 \log_{10}(1/\alpha) \text{ dB}$ at its maximum phase frequency $\omega_m = 1/(T\sqrt{\alpha})$.
To make $\omega_m$ coincide exactly with the new gain crossover frequency $\omega'_{gc}$, locate the frequency on the uncompensated magnitude curve where:
$$20 \log_{10}|G_1(j\omega'_{gc})| = -10 \log_{10}\left(\frac{1}{\alpha}\right) = 20\log_{10}\sqrt{\alpha} \text{ dB}$$
Read this frequency $\omega'_{gc}$ directly from the Bode magnitude plot and assign:
$$\omega_m = \omega'_{gc}$$

Step 6: Calculate the Compensator Corner Frequencies:
Using $\omega_m = \frac{1}{T\sqrt{\alpha}}$:
- Time constant: $T = \frac{1}{\omega_m \sqrt{\alpha}}$
- Zero corner frequency: $\omega_z = \frac{1}{T} = \omega_m \sqrt{\alpha}$
- Pole corner frequency: $\omega_p = \frac{1}{\alpha T} = \frac{\omega_m}{\sqrt{\alpha}}$

Step 7: Formulate the Final Compensated Transfer Function:
The complete compensated open-loop transfer function is:
$$G_{open}(s) = G_c(s) G_1(s) = \left(\frac{1 + sT}{1 + s\alpha T}\right) G_1(s)$$

Step 8: Verification:
Re-evaluate the phase margin of the compensated system at $\omega'_{gc}$:
$$\gamma_{final} = 180^\circ + \angle G_c(j\omega'_{gc}) + \angle G_1(j\omega'_{gc})$$
If $\gamma_{final} \ge \gamma_{spec}$, the design is complete. If the achieved phase margin is slightly below specifications due to steep plant phase roll-off, increase the safety margin $\epsilon$ by $2^\circ \text{ to } 3^\circ$ and repeat from Step 3.
"""
    },
    {
        "qid": "lcs-q23",
        "marks": 7,
        "type": "Long Derivation",
        "title": "Bode Plot Design Procedure of a Phase Lag Compensator",
        "yt_query": "design of lag compensator using bode plot control systems step by step",
        "img_path": "images/lcs/lag_compensator_design_bode.png",
        "img_caption": "Figure 5.3: Bode Diagram Gain Attenuation Mechanism in Phase Lag Compensator Synthesis",
        "answer": r"""
A phase lag compensator is employed when the uncompensated control system exhibits acceptable transient response characteristics but suffers from unacceptably large steady-state tracking errors. Rather than relying on phase addition, the lag compensator achieves stability by attenuating high-frequency loop gain, lowering the gain crossover frequency to a lower frequency where the uncompensated plant possesses an inherently healthy phase margin.

The transfer function of the phase lag compensator is universally expressed in time-constant form as:
$$G_c(s) = \beta \cdot \frac{1 + sT}{1 + s\beta T} = \frac{s + \frac{1}{T}}{s + \frac{1}{\beta T}}, \quad \beta > 1$$
At zero frequency ($s \to 0$), the gain is $\beta$, which amplifies the low-frequency loop gain to satisfy steady-state error constants. At high frequencies ($\omega \gg 1/T$), the high-frequency attenuation is $\frac{1}{\beta}$, shifting the magnitude curve downward by $-20\log_{10}\beta \text{ dB}$.

Step-by-Step Algorithmic Design Procedure:
Step 1: Evaluate the Loop Gain $K$:
Determine the amplifier gain $K$ necessary to satisfy the specified steady-state error constant (e.g., $K_v$ or $K_p$). Incorporate this gain into the uncompensated system:
$$G_1(s) = K G(s)$$

Step 2: Construct the Bode Plot of the Gain-Adjusted System:
Plot the magnitude and phase curves of $G_1(j\omega)$. Evaluate the uncompensated phase margin $\gamma_{un}$. Typically, due to the high gain $K$, the uncompensated system exhibits an unacceptably small or negative phase margin.

Step 3: Select the New Gain Crossover Frequency $\omega'_{gc}$:
Let $\gamma_{spec}$ represent the required phase margin. Because the lag compensator contributes a small residual phase lag at high frequencies, we allocate a safety margin $\epsilon \approx 5^\circ \text{ to } 12^\circ$ (commonly $5^\circ$).
Find the frequency on the uncompensated phase curve where the phase angle equals:
$$\phi_{plant}(\omega'_{gc}) = -180^\circ + \gamma_{spec} + \epsilon$$
Read this specific frequency directly from the phase plot and designate it as the new gain crossover frequency $\omega'_{gc}$.

Step 4: Determine the Lag Factor $\beta$:
At the newly chosen frequency $\omega'_{gc}$, the compensated loop magnitude must equal $0 \text{ dB}$. Thus, the lag compensator must provide an exact high-frequency attenuation equal to the excess gain of $G_1(j\omega'_{gc})$:
$$20 \log_{10}|G_1(j\omega'_{gc})| = 20 \log_{10}\beta \text{ dB}$$
$$\beta = 10^{\frac{|G_1(j\omega'_{gc})|_{\text{dB}}}{20}} = |G_1(j\omega'_{gc})|$$

Step 5: Place the Compensator Zero and Pole:
To prevent the phase lag of the compensator from eroding the phase margin at the new crossover frequency $\omega'_{gc}$, the compensator zero must be placed well below $\omega'_{gc}$, typically one decade below:
$$\omega_z = \frac{1}{T} = 0.1 \times \omega'_{gc} = \frac{\omega'_{gc}}{10}$$
Consequently:
$$T = \frac{10}{\omega'_{gc}}$$
The compensator pole is positioned at:
$$\omega_p = \frac{1}{\beta T} = \frac{\omega_z}{\beta} = \frac{\omega'_{gc}}{10 \beta}$$
At $\omega = \omega'_{gc}$, the phase contribution of the lag compensator is:
$$\phi_c(\omega'_{gc}) = \tan^{-1}(\omega'_{gc} T) - \tan^{-1}(\beta \omega'_{gc} T) = \tan^{-1}(10) - \tan^{-1}(10\beta) \approx 84.3^\circ - 89.5^\circ \approx -5.2^\circ$$
This validates the chosen safety margin $\epsilon \approx 5^\circ$.

Step 6: Assemble the Compensated System Transfer Function:
$$G_{open}(s) = \left(\frac{1 + sT}{1 + s\beta T}\right) G_1(s)$$

Step 7: Verification:
Re-plot the compensated Bode magnitude and phase curves and verify that the actual phase margin satisfies $\gamma_{final} \ge \gamma_{spec}$ while the steady-state error constant remains precisely at the specified target.
"""
    },
    {
        "qid": "lcs-q24",
        "marks": 3,
        "type": "Short Answer",
        "title": "State Space Representation: Mathematical Formulation and Advantages",
        "yt_query": "state space representation state variables state vector control systems",
        "img_path": "images/lcs/state_space_block_diagram.png",
        "img_caption": "Figure 5.4: Structural Block Diagram of Continuous-Time Linear Time-Invariant State Space System",
        "answer": r"""
Classical control theory relies predominantly on input-output transfer functions in the complex frequency domain. While highly effective for single-input single-output (SISO) linear time-invariant systems with zero initial conditions, transfer function techniques treat the plant as a 'black box' and obscure the internal energy distribution. Modern control theory overcomes these limitations through the state space approach.

The state of a dynamic system is defined as the minimal set of variables $x_1(t), x_2(t), \dots, x_n(t)$ such that the knowledge of these variables at an initial time $t = t_0$, together with the complete specification of the input vector $u(t)$ for $t \ge t_0$, completely determines the future state trajectory and output vector $y(t)$ for all $t > t_0$.

For an $n$-th order, $m$-input, $p$-output continuous-time linear time-invariant system, the state-space model is formulated by two vector-matrix equations:
1. State Differential Equation:
   $$\dot{x}(t) = A x(t) + B u(t)$$
2. Output Algebraic Equation:
   $$y(t) = C x(t) + D u(t)$$
where:
- $x(t) \in \mathbb{R}^n$ is the $n \times 1$ State Vector grouping all $n$ state variables.
- $\dot{x}(t) \in \mathbb{R}^n$ is the state velocity vector $\left[\frac{dx_1}{dt}, \dots, \frac{dx_n}{dt}\right]^T$.
- $u(t) \in \mathbb{R}^m$ is the $m \times 1$ Input (Control) Vector.
- $y(t) \in \mathbb{R}^p$ is the $p \times 1$ Output Vector.
- $A \in \mathbb{R}^{n \times n}$ is the System Matrix (governing internal state dynamics).
- $B \in \mathbb{R}^{n \times m}$ is the Input Distribution Matrix.
- $C \in \mathbb{R}^{p \times n}$ is the Output (Observation) Matrix.
- $D \in \mathbb{R}^{p \times m}$ is the Direct Transmission (Feedthrough) Matrix (frequently zero in physical systems).

In the operational block diagram, the state vector $x(t)$ represents the physical outputs of a bank of $n$ parallel analog integrators ($1/s$). The vector $\dot{x}(t)$ drives the integrator inputs, synthesized by summing the linear feedback $A x(t)$ and the input excitation $B u(t)$.

Major Advantages of State Space Analysis over Transfer Functions:
1. MIMO Capability: State space natively handles Multiple-Input Multiple-Output (MIMO) systems without needing cumbersome matrices of cross-coupled transfer functions.
2. Initial Conditions: It naturally incorporates non-zero initial conditions $x(0) \ne 0$ into transient solutions.
3. Internal Visibility: It exposes internal system states (such as mechanical stresses or inductor currents), facilitating the detection of uncontrollable or unobservable dynamic modes that are invisible in transfer functions due to pole-zero cancellations.
4. Non-Linear and Time-Varying Systems: The state-space framework extends directly to non-linear differential equations ($\dot{x} = f(x, u, t)$) and time-varying systems where Laplace transforms cannot be applied.
5. Optimal and Digital Control: It provides the computational foundation for modern state feedback pole placement, Kalman filtering, and linear quadratic regulator (LQR) design.
"""
    },
    {
        "qid": "lcs-q25",
        "marks": 7,
        "type": "Long Derivation",
        "title": "Derivation of Transfer Function Matrix from State Space Model and Numerical Problem",
        "yt_query": "transfer function from state space model C(sI-A)^-1 B + D control systems",
        "img_path": "images/lcs/state_to_transfer_function.png",
        "img_caption": "Figure 5.5: Derivation Flowchart: State Matrix Resolvent to Transfer Function Poles",
        "answer": r"""
To establish the formal link between modern state space theory and classical frequency-domain techniques, we derive the overall transfer function matrix directly from the continuous state differential equations.

Consider the general LTI state-space model:
$$\dot{x}(t) = A x(t) + B u(t)$$
$$y(t) = C x(t) + D u(t)$$
By definition, the transfer function is the ratio of the Laplace transform of the output to the Laplace transform of the input under the strict assumption of zero initial conditions ($x(0) = 0$).

Taking the unilateral Laplace transform on both sides of the state differential equation:
$$\mathcal{L}\{\dot{x}(t)\} = s X(s) - x(0) = A X(s) + B U(s)$$
Substituting $x(0) = 0$:
$$s X(s) = A X(s) + B U(s)$$
Collecting the state transform vectors on the left-hand side:
$$s X(s) - A X(s) = B U(s)$$
$$(s I - A) X(s) = B U(s)$$
where $I$ is the $n \times n$ identity matrix, and $(sI - A)$ is the characteristic matrix.
Provided $s$ does not coincide with any eigenvalue of $A$, the matrix $(sI - A)$ is invertible. Premultiplying both sides by the matrix inverse $(sI - A)^{-1}$:
$$X(s) = (s I - A)^{-1} B U(s)$$
The matrix $\Phi(s) = (sI - A)^{-1}$ is known as the resolvent matrix.

Next, taking the Laplace transform of the output equation:
$$Y(s) = C X(s) + D U(s)$$
Substituting the derived expression for $X(s)$ into the output equation:
$$Y(s) = C \left[ (s I - A)^{-1} B U(s) \right] + D U(s)$$
Factoring out the input vector $U(s)$ on the right-hand side:
$$Y(s) = \left[ C (s I - A)^{-1} B + D \right] U(s)$$
Dividing by $U(s)$ yields the celebrated transfer function matrix formula:
$$G(s) = \frac{Y(s)}{U(s)} = C (s I - A)^{-1} B + D$$
Using the adjoint formulation for the matrix inverse:
$$(s I - A)^{-1} = \frac{\text{adj}(s I - A)}{\det(s I - A)}$$
Substituting this gives:
$$G(s) = \frac{C \, \text{adj}(s I - A) \, B}{\det(s I - A)} + D$$
This algebraic result proves that the poles of the transfer function $G(s)$ are precisely the roots of the characteristic equation $\det(sI - A) = 0$, meaning that system poles are identical to the eigenvalues of the state matrix $A$.

Comprehensive Numerical Demonstration from KTU PYQ:
A system is described by the state space matrices:
$$A = \begin{bmatrix} 0 & 1 \\ -2 & -3 \end{bmatrix}, \quad B = \begin{bmatrix} 0 \\ 1 \end{bmatrix}, \quad C = \begin{bmatrix} 1 & 0 \end{bmatrix}, \quad D = [0]$$
Determine the closed-loop transfer function $G(s) = \frac{Y(s)}{U(s)}$.

Step 1: Construct the matrix $(sI - A)$:
$$s I - A = s \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} - \begin{bmatrix} 0 & 1 \\ -2 & -3 \end{bmatrix} = \begin{bmatrix} s & 0 \\ 0 & s \end{bmatrix} - \begin{bmatrix} 0 & 1 \\ -2 & -3 \end{bmatrix} = \begin{bmatrix} s & -1 \\ 2 & s + 3 \end{bmatrix}$$

Step 2: Calculate the determinant $\det(sI - A)$:
$$\det(s I - A) = s(s + 3) - (-1)(2) = s^2 + 3s + 2 = (s + 1)(s + 2)$$
The system eigenvalues are $\lambda_1 = -1$ and $\lambda_2 = -2$.

Step 3: Evaluate the adjoint matrix $\text{adj}(sI - A)$:
For a $2 \times 2$ matrix $\begin{bmatrix} a & b \\ c & d \end{bmatrix}$, the adjoint is $\begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$:
$$\text{adj}(s I - A) = \begin{bmatrix} s + 3 & 1 \\ -2 & s \end{bmatrix}$$

Step 4: Compute the matrix product $\text{adj}(sI - A) B$:
$$\text{adj}(s I - A) B = \begin{bmatrix} s + 3 & 1 \\ -2 & s \end{bmatrix} \begin{bmatrix} 0 \\ 1 \end{bmatrix} = \begin{bmatrix} (s+3)(0) + (1)(1) \\ (-2)(0) + (s)(1) \end{bmatrix} = \begin{bmatrix} 1 \\ s \end{bmatrix}$$

Step 5: Compute the row-vector multiplication $C \left[\text{adj}(sI - A) B\right]$:
$$C \begin{bmatrix} 1 \\ s \end{bmatrix} = \begin{bmatrix} 1 & 0 \end{bmatrix} \begin{bmatrix} 1 \\ s \end{bmatrix} = (1)(1) + (0)(s) = 1$$

Step 6: Assemble the transfer function $G(s)$:
$$G(s) = \frac{1}{\det(s I - A)} + 0 = \frac{1}{s^2 + 3s + 2} = \frac{1}{(s + 1)(s + 2)}$$
The transfer function has poles at $s = -1$ and $s = -2$, confirming complete equivalence with the eigenvalues of matrix $A$.
"""
    },
    {
        "qid": "lcs-q26",
        "marks": 7,
        "type": "Long Derivation",
        "title": "State Transition Matrix: Properties, Solution of State Equation, and e^{At} Computation",
        "yt_query": "state transition matrix properties computation laplace transform method control systems",
        "img_path": "images/lcs/state_transition_matrix.png",
        "img_caption": "Figure 5.6: State Transition Mapping Trajectory from Initial State x(0) to x(t)",
        "answer": r"""
In modern state space analysis, the state transition matrix constitutes the fundamental mathematical operator governing the unforced free evolution of an autonomous dynamic system.

Consider the unforced homogeneous continuous-time state equation:
$$\dot{x}(t) = A x(t), \quad x(0) = x_0$$
This is a first-order vector-matrix differential equation whose scalar counterpart $\dot{x} = a x$ has the familiar exponential solution $x(t) = e^{at} x(0)$. By direct mathematical analogy, the solution to the vector system is expressed as:
$$x(t) = e^{At} x(0) = \Phi(t) x(0)$$
where $\Phi(t) = e^{At}$ is the State Transition Matrix.

Formal Definition:
The state transition matrix $\Phi(t)$ is defined by the infinite Taylor matrix series expansion:
$$\Phi(t) = e^{At} = I + A t + \frac{A^2 t^2}{2!} + \frac{A^3 t^3}{3!} + \dots = \sum_{k=0}^\infty \frac{A^k t^k}{k!}$$
Alternatively, taking the Laplace transform of $\dot{x}(t) = A x(t)$:
$$s X(s) - x(0) = A X(s) \implies (s I - A) X(s) = x(0) \implies X(s) = (s I - A)^{-1} x(0)$$
Taking the inverse Laplace transform yields the closed-form operational definition:
$$\Phi(t) = e^{At} = \mathcal{L}^{-1}\left\{ (s I - A)^{-1} \right\}$$

Five Essential Properties of the State Transition Matrix:
Property 1 (Identity at zero time):
$$\Phi(0) = e^{A(0)} = I$$
Proof: Substituting $t = 0$ into the series expansion: $\Phi(0) = I + 0 + 0 + \dots = I$.

Property 2 (Inverse and Time-Reversal):
$$\Phi^{-1}(t) = \Phi(-t) = e^{-At}$$
Proof: $\Phi(t)\Phi(-t) = e^{At} e^{-At} = e^{A(t - t)} = e^0 = I$. Thus, the inverse of $\Phi(t)$ is obtained simply by replacing $t$ with $-t$.

Property 3 (Semi-group Law / Successive Transitions):
$$\Phi(t_1 + t_2) = \Phi(t_1) \Phi(t_2) = \Phi(t_2) \Phi(t_1)$$
Proof: Transitioning from $t = 0$ to $t_1$ gives $x(t_1) = \Phi(t_1)x(0)$. Transitioning from $t_1$ to $(t_1 + t_2)$ gives $x(t_1 + t_2) = \Phi(t_2) x(t_1) = \Phi(t_2)\Phi(t_1)x(0)$. Direct transition from $0$ gives $x(t_1 + t_2) = \Phi(t_1 + t_2)x(0)$. Equating both yields $\Phi(t_1 + t_2) = \Phi(t_1)\Phi(t_2)$.

Property 4 (Power Property):
$$[\Phi(t)]^k = \Phi(k t) \quad \text{for any integer } k$$
Proof: Applying Property 3 repeatedly $k$ times: $[\Phi(t)]^k = (e^{At})^k = e^{A(k t)} = \Phi(k t)$.

Property 5 (Time Derivative):
$$\frac{d\Phi(t)}{dt} = A \Phi(t) = \Phi(t) A$$
Proof: Differentiating the series term by term:
$$\frac{d}{dt}\left[I + A t + \frac{A^2 t^2}{2!} + \dots\right] = 0 + A + A^2 t + \frac{A^3 t^2}{2!} + \dots = A\left[I + A t + \frac{A^2 t^2}{2!} + \dots\right] = A \Phi(t)$$

Full Analytical Computation from KTU PYQ:
Given the system matrix:
$$A = \begin{bmatrix} 0 & 1 \\ -2 & -3 \end{bmatrix}$$
Compute the state transition matrix $\Phi(t) = e^{At}$ using the Laplace transform resolvent method.

Step 1: Compute $(sI - A)$:
$$s I - A = \begin{bmatrix} s & -1 \\ 2 & s + 3 \end{bmatrix}$$

Step 2: Evaluate determinant and inverse $(sI - A)^{-1}$:
$$\det(s I - A) = s(s + 3) + 2 = s^2 + 3s + 2 = (s + 1)(s + 2)$$
$$\text{adj}(s I - A) = \begin{bmatrix} s + 3 & 1 \\ -2 & s \end{bmatrix}$$
$$(s I - A)^{-1} = \frac{1}{(s + 1)(s + 2)} \begin{bmatrix} s + 3 & 1 \\ -2 & s \end{bmatrix} = \begin{bmatrix} \frac{s + 3}{(s + 1)(s + 2)} & \frac{1}{(s + 1)(s + 2)} \\ \frac{-2}{(s + 1)(s + 2)} & \frac{s}{(s + 1)(s + 2)} \end{bmatrix}$$

Step 3: Perform partial fraction expansions for each matrix entry:
1. Entry $(1,1)$:
   $$\frac{s + 3}{(s + 1)(s + 2)} = \frac{A_1}{s + 1} + \frac{B_1}{s + 2} = \frac{-1 + 3}{(-1 + 2)(s + 1)} + \frac{-2 + 3}{(-2 + 1)(s + 2)} = \frac{2}{s + 1} - \frac{1}{s + 2}$$
2. Entry $(1,2)$:
   $$\frac{1}{(s + 1)(s + 2)} = \frac{1}{s + 1} - \frac{1}{s + 2}$$
3. Entry $(2,1)$:
   $$\frac{-2}{(s + 1)(s + 2)} = \frac{-2}{s + 1} + \frac{2}{s + 2}$$
4. Entry $(2,2)$:
   $$\frac{s}{(s + 1)(s + 2)} = \frac{-1}{s + 1} + \frac{2}{s + 2}$$

Step 4: Take inverse Laplace transforms term-by-term:
$$\Phi(t) = \mathcal{L}^{-1}\left\{ (s I - A)^{-1} \right\} = \begin{bmatrix} 2 e^{-t} - e^{-2t} & e^{-t} - e^{-2t} \\ -2 e^{-t} + 2 e^{-2t} & -e^{-t} + 2 e^{-2t} \end{bmatrix}$$

Step 5: Verify Property 1 ($\Phi(0) = I$):
$$\Phi(0) = \begin{bmatrix} 2(1) - 1 & 1 - 1 \\ -2(1) + 2(1) & -(1) + 2(1) \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = I$$
The result perfectly matches the identity matrix, confirming the mathematical accuracy of the derived state transition matrix.
"""
    }
]
