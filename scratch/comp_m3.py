# -*- coding: utf-8 -*-
"""
Module 3: Control Systems and Instrumentation
Questions comp-q12 to comp-q16 for Comprehensive Course Work (EET308).
"""

M3_QUESTIONS = [
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
