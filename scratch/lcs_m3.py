# -*- coding: utf-8 -*-
"""
Module 3 for Linear Control Systems (EET302)
Stability Analysis and Root Locus Technique
"""

M3_QUESTIONS = [
    {
        "qid": "lcs-q11",
        "marks": 3,
        "type": "Short Answer",
        "title": "Concept of Stability, BIBO Criterion, and S-Plane Pole Locations",
        "yt_query": "stability concepts bibo stability pole locations s plane control systems",
        "img_path": "images/lcs/stability_s_plane_poles.png",
        "img_caption": "Figure 3.1: Complex s-Plane Mapping of Closed-Loop Poles to Impulse Response Modes",
        "answer": r"""
Stability is the most critical requirement in the analysis and design of dynamic control systems. An unstable control system is practically unusable, as its internal variables can grow unboundedly until physical saturation, component damage, or catastrophic breakdown occurs.

The foundational formal definition of stability for a linear time-invariant (LTI) continuous system is Bounded-Input Bounded-Output (BIBO) Stability. A system is defined to be BIBO stable if and only if every bounded input excitation produces a bounded output response:
$$|u(t)| \le M_u < \infty \quad \forall t \ge 0 \implies |y(t)| \le M_y < \infty \quad \forall t \ge 0$$
where $M_u$ and $M_y$ are finite positive constants. The relationship between BIBO stability and the system impulse response $g(t)$ is established through the convolution integral:
$$y(t) = \int_0^\infty g(\tau) u(t - \tau) \, d\tau$$
Taking absolute values on both sides:
$$|y(t)| = \left| \int_0^\infty g(\tau) u(t - \tau) \, d\tau \right| \le \int_0^\infty |g(\tau)| |u(t - \tau)| \, d\tau \le M_u \int_0^\infty |g(\tau)| \, d\tau$$
For the output to remain bounded for all bounded inputs, the integral of the absolute impulse response must be strictly finite:
$$\int_0^\infty |g(t)| \, dt < \infty$$
This condition represents the necessary and sufficient mathematical criterion for the BIBO stability of an LTI system.

In the complex frequency domain ($s = \sigma + j\omega$), the dynamic modes constituting the impulse response are directly governed by the closed-loop transfer function poles, which are the roots of the characteristic equation $1 + G(s)H(s) = 0$. The geometric locations of these poles in the s-plane dictate the qualitative nature of stability:
1. Stable System: All closed-loop poles lie strictly in the open Left Half of the s-plane (LHP, $\text{Re}(s_i) < 0$). Real poles at $s = -\sigma$ generate exponentially decaying modes $e^{-\sigma t}$, while complex conjugate pole pairs at $s = -\sigma \pm j\omega_d$ generate exponentially damped sinusoidal oscillations $e^{-\sigma t}\sin(\omega_d t + \phi)$. In both cases, the transient response decays to zero as $t \to \infty$.
2. Unstable System: If even a single pole lies in the Right Half of the s-plane (RHP, $\text{Re}(s_i) > 0$), it introduces an exponentially growing term $e^{+\sigma t}$ or $e^{+\sigma t}\sin(\omega_d t)$, causing the output to diverge toward infinity. A system is also unstable if multiple (repeated) poles lie on the imaginary axis (e.g., at $s = \pm j\omega_o$), producing algebraically growing resonant terms of the form $t \sin(\omega_o t)$.
3. Marginally (Critically) Stable System: If one or more distinct (non-repeated) pairs of simple poles lie strictly on the imaginary axis ($s = \pm j\omega_o$ with $\sigma = 0$) and all remaining poles lie in the strict LHP, the system produces sustained, undamped sinusoidal oscillations of constant peak amplitude $\sin(\omega_o t)$ for an impulse input. While bounded for an impulse, the response becomes unbounded if driven by a sinusoidal input of frequency $\omega_o$ due to resonance.

Absolute stability is a binary condition indicating whether the system is stable or unstable. In contrast, relative stability quantifies the degree of stability, measured by how far the dominant closed-loop poles reside into the left half plane and how close they are to the imaginary axis.
"""
    },
    {
        "qid": "lcs-q12",
        "marks": 7,
        "type": "Long Derivation",
        "title": "Routh-Hurwitz Stability Criterion and Special Case 1: First Element Zero in a Row",
        "yt_query": "routh hurwitz criterion first element zero epsilon method solved problem",
        "img_path": "images/lcs/routh_array_epsilon_case.png",
        "img_caption": "Figure 3.2: Routh Array Construction Scheme Showing Epsilon Substitution Mechanism",
        "answer": r"""
The Routh-Hurwitz stability criterion is an algebraic frequency-domain method that determines the number of closed-loop poles residing in the right half of the s-plane without requiring direct numerical factorization of the characteristic polynomial.

Consider the $n$-th order closed-loop characteristic polynomial:
$$q(s) = a_0 s^n + a_1 s^{n-1} + a_2 s^{n-2} + a_3 s^{n-3} + \dots + a_{n-1} s + a_n = 0, \quad a_0 > 0$$
Two necessary (but not sufficient) conditions for all roots to have negative real parts are:
1. All polynomial coefficients $a_0, a_1, \dots, a_n$ must be strictly positive ($a_i > 0$).
2. None of the coefficients can be zero (no terms missing between highest and lowest powers).

If these necessary checks pass, the Routh array is constructed systematically:
$$\begin{array}{l|lllll}
s^n & a_0 & a_2 & a_4 & a_6 & \dots \\
s^{n-1} & a_1 & a_3 & a_5 & a_7 & \dots \\
s^{n-2} & b_1 & b_2 & b_3 & \dots & \\
s^{n-3} & c_1 & c_2 & c_3 & \dots & \\
\vdots & \vdots & & & & \\
s^0 & a_n & & & &
\end{array}$$
The array entries are evaluated using the cross-multiplication determinant formulas:
$$b_1 = \frac{a_1 a_2 - a_0 a_3}{a_1}, \quad b_2 = \frac{a_1 a_4 - a_0 a_5}{a_1}, \quad b_3 = \frac{a_1 a_6 - a_0 a_7}{a_1}$$
$$c_1 = \frac{b_1 a_3 - a_1 b_2}{b_1}, \quad c_2 = \frac{b_1 a_5 - a_1 b_3}{b_1}$$
This recursive cross-multiplication continues until all subsequent rows terminate.
Routh's Theorem states that the system is stable if and only if all elements in the first column of the Routh array are strictly positive. If sign changes occur in the first column, the system is unstable, and the total number of sign changes equals the exact number of roots located in the right half of the s-plane (RHP).

Special Case 1: First Element in a Row is Zero, but remaining elements are non-zero.
When computing a row, if the leading element becomes zero while subsequent entries in that same row are non-zero, division by zero occurs in the next row, halting the standard algorithm. Two methods resolve this:
Method 1 (The $\epsilon$-substitution method): Replace the zero element with a small positive number $\epsilon > 0$. Complete the remaining rows of the array expressing entries as rational functions of $\epsilon$. Finally, evaluate the signs of the first column elements by taking the algebraic limit as $\epsilon \to 0^+$.
Method 2 (Polynomial transformation): Substitute $s = \frac{1}{z}$ into the original polynomial $q(s) = 0$, clear denominators to form a new polynomial in $z$, and construct its Routh array. Since the transformation $s = 1/z$ maps the right-half s-plane into the right-half z-plane, the count of sign changes remains identical.

Numerical Demonstration using the $\epsilon$-Method:
Consider the characteristic equation from a KTU university exam:
$$q(s) = s^5 + s^4 + 2s^3 + 2s^2 + 3s + 5 = 0$$
Step 1: Check necessary conditions: All coefficients are present and positive.
Step 2: Construct the first two rows:
$$\begin{array}{l|lll}
s^5 & 1 & 2 & 3 \\
s^4 & 1 & 2 & 5
\end{array}$$
Step 3: Compute row $s^3$:
$$b_1 = \frac{(1)(2) - (1)(2)}{1} = \frac{2 - 2}{1} = 0$$
$$b_2 = \frac{(1)(3) - (1)(5)}{1} = \frac{3 - 5}{1} = -2$$
$$b_3 = 0$$
The leading element $b_1$ is zero, but $b_2 = -2 \ne 0$. This is Special Case 1.
We substitute $b_1 = \epsilon$ where $\epsilon > 0$:
$$\begin{array}{l|lll}
s^5 & 1 & 2 & 3 \\
s^4 & 1 & 2 & 5 \\
s^3 & \epsilon & -2 & 0
\end{array}$$
Step 4: Compute row $s^2$:
$$c_1 = \frac{\epsilon(2) - (1)(-2)}{\epsilon} = \frac{2\epsilon + 2}{\epsilon}$$
$$c_2 = \frac{\epsilon(5) - (1)(0)}{\epsilon} = 5$$
Step 5: Compute row $s^1$:
$$d_1 = \frac{c_1(-2) - \epsilon(5)}{c_1} = \frac{\left(\frac{2\epsilon + 2}{\epsilon}\right)(-2) - 5\epsilon}{\frac{2\epsilon + 2}{\epsilon}} = \frac{-4\epsilon - 4 - 5\epsilon^2}{2\epsilon + 2} = \frac{-5\epsilon^2 - 4\epsilon - 4}{2\epsilon + 2}$$
Step 6: Compute row $s^0$:
$$e_1 = 5$$

Step 7: Evaluate the signs in the first column as $\epsilon \to 0^+$:
- $s^5$ term: $+1$ (Positive)
- $s^4$ term: $+1$ (Positive)
- $s^3$ term: $+\epsilon \to +0$ (Positive)
- $s^2$ term: $\lim_{\epsilon \to 0^+} \frac{2\epsilon + 2}{\epsilon} = +\infty$ (Positive)
- $s^1$ term: $\lim_{\epsilon \to 0^+} \frac{-5(0) - 4(0) - 4}{2(0) + 2} = \frac{-4}{2} = -2$ (Negative!)
- $s^0$ term: $+5$ (Positive)

Examining the sequence of signs in the first column:
$$[+, +, +, +, -, +]$$
There are two distinct sign changes:
1. Transition from $s^2$ ($+\infty$) to $s^1$ ($-2$): First sign change.
2. Transition from $s^1$ ($-2$) to $s^0$ ($+5$): Second sign change.

Conclusion:
Because there are two sign changes in the first column of the Routh array, exactly two roots of the characteristic equation lie in the right half of the s-plane (RHP). Therefore, the closed-loop system is strictly unstable.
"""
    },
    {
        "qid": "lcs-q13",
        "marks": 7,
        "type": "Long Derivation",
        "title": "Routh-Hurwitz Special Case 2: All Elements Zero in a Row and Oscillation Frequency",
        "yt_query": "routh hurwitz entire row of zeros auxiliary polynomial oscillation frequency",
        "img_path": "images/lcs/routh_auxiliary_polynomial.png",
        "img_caption": "Figure 3.3: Symmetric Root Pairs Associated with Auxiliary Polynomial Row of Zeros",
        "answer": r"""
In the construction of the Routh array, Special Case 2 occurs when every element in an entire horizontal row becomes identically zero. This is one of the most mathematically significant occurrences in stability analysis.

Physical Significance of a Row of Zeros:
An entire row of zeros signifies that the characteristic polynomial possesses roots that are perfectly symmetric with respect to the origin of the complex s-plane. Such symmetric root distributions include:
1. Pairs of real roots of equal magnitude and opposite signs: $s = \pm \sigma$.
2. Pairs of purely imaginary conjugate roots: $s = \pm j\omega_o$.
3. Quartets of complex conjugate roots forming a rectangle symmetric about the origin: $s = \pm \sigma \pm j\omega$.

Algorithmic Procedure to Resolve a Row of Zeros:
1. Form the Auxiliary Polynomial $A(s)$ using the coefficients of the row immediately preceding the row of zeros. Because this row always corresponds to an even power of $s$, $A(s)$ is an even polynomial containing only even powers of $s$:
   $$A(s) = a_0 s^{2m} + a_2 s^{2m-2} + \dots + a_{2m}$$
2. Take the first derivative of the auxiliary polynomial with respect to $s$:
   $$\frac{dA(s)}{ds} = 2m a_0 s^{2m-1} + (2m-2) a_2 s^{2m-3} + \dots$$
3. Replace the row of zeros with the coefficients of the derivative polynomial $\frac{dA(s)}{ds}$.
4. Continue the normal Routh array cross-multiplications down to the $s^0$ row.
5. The roots of the auxiliary equation $A(s) = 0$ are simultaneously roots of the original characteristic equation $q(s) = 0$. If no further sign changes occur below the auxiliary row, the roots of $A(s) = 0$ lie on the imaginary axis, indicating marginal stability with sustained oscillation frequency $\omega_{osc}$.

Comprehensive Worked Example from KTU PYQ:
A unity feedback control system has open-loop transfer function:
$$G(s) = \frac{K}{s(s + 1)(s + 2)(s + 5)}$$
Determine:
(i) The range of gain $K$ for system stability.
(ii) The marginal value of gain $K_{mar}$ that causes sustained oscillations.
(iii) The frequency of sustained oscillations $\omega_{osc}$.

Step 1: Form the closed-loop characteristic equation:
$$1 + G(s) = 1 + \frac{K}{s(s + 1)(s + 2)(s + 5)} = 0$$
$$s(s + 1)(s + 2)(s + 5) + K = 0$$
Expanding the polynomial:
$$s(s + 1)(s^2 + 7s + 10) + K = s(s^3 + 7s^2 + 10s + s^2 + 7s + 10) + K = 0$$
$$s(s^3 + 8s^2 + 17s + 10) + K = 0$$
$$s^4 + 8s^3 + 17s^2 + 10s + K = 0$$

Step 2: Construct the Routh array in terms of parameter $K$:
$$\begin{array}{l|lll}
s^4 & 1 & 17 & K \\
s^3 & 8 & 10 & 0 \\
s^2 & b_1 & b_2 & 0 \\
s^1 & c_1 & 0 & 0 \\
s^0 & d_1 & 0 & 0
\end{array}$$
Computing row $s^2$:
$$b_1 = \frac{(8)(17) - (1)(10)}{8} = \frac{136 - 10}{8} = \frac{126}{8} = 15.75$$
$$b_2 = \frac{(8)(K) - (1)(0)}{8} = K$$

Computing row $s^1$:
$$c_1 = \frac{b_1(10) - 8(b_2)}{b_1} = \frac{15.75(10) - 8K}{15.75} = \frac{157.5 - 8K}{15.75}$$

Computing row $s^0$:
$$d_1 = \frac{c_1(K) - 15.75(0)}{c_1} = K$$

Step 3: Analyze stability conditions:
For absolute stability, all elements in the first column must be strictly positive:
1. From row $s^0$: $K > 0$
2. From row $s^1$: $\frac{157.5 - 8K}{15.75} > 0 \implies 157.5 - 8K > 0 \implies 8K < 157.5 \implies K < \frac{157.5}{8} = 19.6875$

Thus, the range of gain $K$ for stable operation is:
$$0 < K < 19.6875$$

Step 4: Evaluate the marginal gain and sustained oscillation frequency:
Setting the $s^1$ row element identically to zero produces a row of zeros:
$$157.5 - 8K_{mar} = 0 \implies K_{mar} = \frac{157.5}{8} = 19.6875$$
At $K = 19.6875$, the row $s^1$ becomes all zeros. We construct the Auxiliary Equation from the preceding $s^2$ row:
$$A(s) = b_1 s^2 + b_2 = 15.75 s^2 + K = 0$$
Substituting $K = 19.6875$:
$$15.75 s^2 + 19.6875 = 0$$
$$s^2 = -\frac{19.6875}{15.75} = -1.25$$
Taking the square root:
$$s = \pm j \sqrt{1.25} = \pm j 1.118 \text{ rad/s}$$
Since these roots are purely imaginary ($s = \pm j\omega_{osc}$), the system operates on the verge of instability, producing sustained undamped sinusoidal oscillations with frequency:
$$\omega_{osc} = \sqrt{1.25} \approx 1.118 \text{ rad/s}$$
This comprehensive calculation demonstrates how Special Case 2 determines exact stability boundaries and oscillation frequencies.
"""
    },
    {
        "qid": "lcs-q14",
        "marks": 7,
        "type": "Long Derivation",
        "title": "Root Locus Method: Angle and Magnitude Conditions, and Complete Construction Rules",
        "yt_query": "root locus construction rules angle magnitude condition control systems",
        "img_path": "images/lcs/root_locus_geometric_rules.png",
        "img_caption": "Figure 3.4: Geometric Principles of Root Locus: Asymptotes, Centroid, and Breakaway Points",
        "answer": r"""
The Root Locus method, developed by Walter R. Evans in 1948, is a powerful graphical technique that plots the trajectories traced out by closed-loop poles in the complex s-plane as a system parameter—most commonly the loop gain $K$—is varied continuously from 0 to $+\infty$.

The foundational mathematical basis stems from the closed-loop characteristic equation:
$$1 + G(s)H(s) = 0 \implies G(s)H(s) = -1 = 1 \cdot e^{j(2q+1)\pi}, \quad q = 0, \pm 1, \pm 2, \dots$$
This complex equality splits into two fundamental governing conditions:
1. Magnitude Condition:
   $$|G(s)H(s)| = 1 \implies \frac{K \prod_{j=1}^m |s - z_j|}{\prod_{i=1}^n |s - p_i|} = 1 \implies K = \frac{\prod_{i=1}^n \text{distance to pole } p_i}{\prod_{j=1}^m \text{distance to zero } z_j}$$
   The magnitude condition determines the exact numerical gain $K$ at any point $s$ already known to lie on the locus.
2. Angle Condition:
   $$\angle G(s)H(s) = \sum_{j=1}^m \angle(s - z_j) - \sum_{i=1}^n \angle(s - p_i) = \pm (2q + 1)180^\circ, \quad q = 0, 1, 2, \dots$$
   A test point $s$ belongs to the root locus if and only if the net sum of angles from all open-loop zeros minus angles from all open-loop poles equals an odd integer multiple of $180^\circ$.

The Evans root locus construction follows eight rigorous procedural rules:
Rule 1: Number of Branches:
The root locus consists of $N = \max(n, m)$ independent continuous branches, where $n$ is the number of finite open-loop poles and $m$ is the number of finite open-loop zeros. In physical systems where $n \ge m$, the total number of branches is exactly $n$.

Rule 2: Starting and Terminating Points:
As $K \to 0$, $G(s)H(s) \to 0$, meaning the closed-loop poles coincide with the open-loop poles. Thus, all $n$ branches originate at the open-loop poles ($K = 0$). As $K \to \infty$, $m$ branches terminate at the $m$ finite open-loop zeros, while the remaining $(n - m)$ branches terminate at zeros situated at infinity along asymptotes.

Rule 3: Symmetry of the Root Locus:
Because complex roots of real-coefficient polynomials always occur in conjugate pairs ($\sigma \pm j\omega$), the root locus is strictly symmetrical about the real axis.

Rule 4: Root Locus on the Real Axis:
A point on the real axis belongs to the root locus if and only if the total count of real open-loop poles and real open-loop zeros lying to its immediate right is an odd number.

Rule 5: Asymptotes and Centroid:
The $(n - m)$ branches terminating at infinity approach straight-line asymptotes as $s \to \infty$.
- Angles of Asymptotes ($\theta_a$):
  $$\theta_a = \frac{(2q + 1)180^\circ}{n - m}, \quad q = 0, 1, 2, \dots, (n - m - 1)$$
- Centroid of Asymptotes ($\sigma_A$): All asymptotes radiate outward from a single intersection point on the real axis called the centroid:
  $$\sigma_A = \frac{\sum \text{Real parts of open-loop poles} - \sum \text{Real parts of open-loop zeros}}{n - m} = \frac{\sum_{i=1}^n p_i - \sum_{j=1}^m z_j}{n - m}$$

Rule 6: Breakaway and Break-in Points:
Points where two or more branches collide and depart from the real axis into the complex plane (or enter the real axis) are breakaway (or break-in) points. At these points, multiple roots exist, satisfying:
$$\frac{dK}{ds} = 0$$
From the characteristic equation $B(s) + K A(s) = 0$, express $K = -\frac{B(s)}{A(s)}$ and solve $\frac{dK}{ds} = 0$. Valid breakaway points must lie on segments of the real axis where the root locus exists.

Rule 7: Angle of Departure and Arrival:
For complex open-loop poles, the angle at which a branch departs from a complex pole $p_k$ is:
$$\phi_d = 180^\circ - \sum \angle(p_k - p_i) + \sum \angle(p_k - z_j)$$
For complex open-loop zeros, the angle of arrival $\phi_a$ at zero $z_k$ is:
$$\phi_a = 180^\circ - \sum \angle(z_k - z_j) + \sum \angle(z_k - p_i)$$

Rule 8: Intersection with the Imaginary Axis:
The points where the root locus crosses the $j\omega$-axis into the unstable right half plane and the corresponding critical gain $K_{mar}$ are evaluated using the Routh-Hurwitz criterion (by setting the $s^1$ row to zero and solving the auxiliary equation).
"""
    },
    {
        "qid": "lcs-q15",
        "marks": 7,
        "type": "Long Derivation",
        "title": "Complete Step-by-Step Root Locus Construction of a Third-Order System",
        "yt_query": "sketch root locus G(s)H(s) = K / s(s+2)(s+4) step by step solved example",
        "img_path": "images/lcs/root_locus_third_order_plot.png",
        "img_caption": "Figure 3.5: Root Locus Diagram for G(s)H(s) = K / [s(s+2)(s+4)] Showing Breakaway and jw Crossings",
        "answer": r"""
Consider the classic KTU university examination problem:
Construct the complete root locus for a unity feedback control system having open-loop transfer function:
$$G(s)H(s) = \frac{K}{s(s + 2)(s + 4)}, \quad K > 0$$
Determine the breakaway point, imaginary axis crossing points, marginal gain $K_{mar}$, and the range of gain $K$ for system stability.

Step 1: Open-Loop Poles and Zeros:
- Open-loop poles: $s = 0, -2, -4$. Total number of poles $n = 3$.
- Open-loop zeros: None ($m = 0$).
- Total number of root locus branches = $n = 3$.
- Three branches start at $s = 0, -2, -4$ at $K = 0$ and terminate at infinity ($n - m = 3$) as $K \to \infty$.

Step 2: Segments on the Real Axis:
Applying Rule 4 (counting poles and zeros to the right):
- Between $s = 0$ and $s = -2$: 1 pole lies to the right (odd count). Root locus exists.
- Between $s = -2$ and $s = -4$: 2 poles lie to the right (even count). Root locus does not exist.
- To the left of $s = -4$ ($-\infty < s < -4$): 3 poles lie to the right (odd count). Root locus exists from $-4$ to $-\infty$.

Step 3: Asymptotes and Centroid:
Number of asymptotes = $n - m = 3 - 0 = 3$.
- Angles of Asymptotes ($\theta_a$ for $q = 0, 1, 2$):
  $$\theta_a = \frac{(2q + 1)180^\circ}{3}$$
  $$\text{For } q = 0: \theta_0 = \frac{180^\circ}{3} = 60^\circ$$
  $$\text{For } q = 1: \theta_1 = \frac{3 \times 180^\circ}{3} = 180^\circ$$
  $$\text{For } q = 2: \theta_2 = \frac{5 \times 180^\circ}{3} = 300^\circ = -60^\circ$$
- Centroid ($\sigma_A$):
  $$\sigma_A = \frac{\sum p_i - \sum z_j}{n - m} = \frac{[0 + (-2) + (-4)] - [0]}{3} = \frac{-6}{3} = -2$$
The three asymptotes radiate from $\sigma_A = -2$ at angles of $60^\circ, 180^\circ,$ and $300^\circ$.

Step 4: Breakaway Point Calculation:
Characteristic equation is $1 + G(s)H(s) = 0$:
$$1 + \frac{K}{s(s^2 + 6s + 8)} = 0 \implies s^3 + 6s^2 + 8s + K = 0$$
Expressing gain $K$ in terms of $s$:
$$K = -(s^3 + 6s^2 + 8s)$$
Taking the derivative with respect to $s$ and setting it to zero:
$$\frac{dK}{ds} = -(3s^2 + 12s + 8) = 0 \implies 3s^2 + 12s + 8 = 0$$
Using the quadratic formula:
$$s = \frac{-12 \pm \sqrt{12^2 - 4(3)(8)}}{2(3)} = \frac{-12 \pm \sqrt{144 - 96}}{6} = \frac{-12 \pm \sqrt{48}}{6} = \frac{-12 \pm 6.9282}{6}$$
$$s_1 = \frac{-12 + 6.9282}{6} = \frac{-5.0718}{6} \approx -0.845$$
$$s_2 = \frac{-12 - 6.9282}{6} = \frac{-18.9282}{6} \approx -3.155$$

Validity Check:
The real-axis root locus exists between $0$ and $-2$, and between $-4$ and $-\infty$.
- $s_1 = -0.845$ lies inside the active segment $[0, -2]$. Therefore, $s = -0.845$ is a valid physical breakaway point.
- $s_2 = -3.155$ lies in the non-locus segment $[-2, -4]$. It is an extraneous mathematical artifact.
Evaluating gain $K$ at $s = -0.845$:
$$K = -[(-0.845)^3 + 6(-0.845)^2 + 8(-0.845)] = -[-0.603 + 4.284 - 6.760] = -(-3.079) = +3.079 > 0$$

Step 5: Imaginary Axis Crossing and Marginal Gain $K_{mar}$:
Using the characteristic equation $s^3 + 6s^2 + 8s + K = 0$, construct the Routh array:
$$\begin{array}{l|ll}
s^3 & 1 & 8 \\
s^2 & 6 & K \\
s^1 & \frac{48 - K}{6} & 0 \\
s^0 & K & 0
\end{array}$$
For stability, all first column entries must be strictly positive:
1. $K > 0$
2. $\frac{48 - K}{6} > 0 \implies K < 48$
Hence, the system is stable for $0 < K < 48$.

At marginal stability ($K = K_{mar} = 48$), the $s^1$ row becomes zero. The auxiliary equation from the $s^2$ row is:
$$A(s) = 6s^2 + K_{mar} = 6s^2 + 48 = 0$$
$$s^2 = -\frac{48}{6} = -8 \implies s = \pm j\sqrt{8} \approx \pm j 2.828 \text{ rad/s}$$
Thus, the root locus crosses the imaginary axis into the right half plane at $s = \pm j 2.83$ at a critical gain $K_{mar} = 48$.

Step 6: Summary of Root Locus Trajectory:
- As $K$ increases from $0$ to $3.079$, two poles move toward each other along the real axis from $s = 0$ and $s = -2$, colliding at $s = -0.845$.
- At $K = 3.079$, they break away into the complex plane at $\pm 90^\circ$ angles, curving toward the asymptotes at $\pm 60^\circ$.
- At $K = 48$, they cross the $j\omega$-axis at $\pm j 2.83$. For $K > 48$, two poles reside in the RHP, causing instability.
- The third branch starts at $s = -4$ at $K = 0$ and travels monotonically leftward toward $-\infty$ along the $180^\circ$ asymptote.
"""
    }
]
