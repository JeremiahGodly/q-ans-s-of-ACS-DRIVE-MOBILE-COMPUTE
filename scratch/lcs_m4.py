# -*- coding: utf-8 -*-
"""
Module 4 for Linear Control Systems (EET302)
Frequency Response Analysis and Nyquist Criterion
"""

M4_QUESTIONS = [
    {
        "qid": "lcs-q16",
        "marks": 3,
        "type": "Short Answer",
        "title": "Frequency Domain Specifications and Time-Domain Correlation",
        "yt_query": "frequency domain specifications resonant peak resonant frequency bandwidth derivation control systems",
        "img_path": "images/lcs/frequency_domain_specs.png",
        "img_caption": "Figure 4.1: Closed-Loop Frequency Response Curve Depicting Mr, wr, and Bandwidth wb",
        "answer": r"""
The steady-state response of a linear time-invariant system to a sinusoidal input of frequency $\omega$ is known as its frequency response. When excited by $r(t) = A \sin(\omega t)$, the steady-state output is $c(t) = A |M(j\omega)| \sin[\omega t + \angle M(j\omega)]$, where $M(s) = \frac{C(s)}{R(s)}$ is the closed-loop transfer function.

For a standard second-order system:
$$M(s) = \frac{\omega_n^2}{s^2 + 2\zeta \omega_n s + \omega_n^2}$$
Substituting $s = j\omega$ and normalizing by defining the frequency ratio $u = \frac{\omega}{\omega_n}$:
$$M(j\omega) = \frac{\omega_n^2}{-\omega^2 + j 2\zeta \omega_n \omega + \omega_n^2} = \frac{1}{(1 - u^2) + j 2\zeta u}$$
The magnitude of the closed-loop frequency response is:
$$|M(j\omega)| = M(u) = \frac{1}{\sqrt{(1 - u^2)^2 + 4\zeta^2 u^2}}$$

We derive the primary frequency domain specifications:
1. Resonant Peak ($M_r$):
The resonant peak is the maximum value attained by $|M(j\omega)|$. To find the extremum, we minimize the radicand in the denominator: $g(u) = (1 - u^2)^2 + 4\zeta^2 u^2$.
Differentiating with respect to $u$:
$$\frac{dg(u)}{du} = 2(1 - u^2)(-2u) + 8\zeta^2 u = -4u(1 - u^2) + 8\zeta^2 u = 4u [u^2 - (1 - 2\zeta^2)] = 0$$
Setting this to zero yields the non-trivial resonant frequency ratio:
$$u_r = \frac{\omega_r}{\omega_n} = \sqrt{1 - 2\zeta^2}$$
For a real physical peak to exist, $1 - 2\zeta^2 > 0$, which requires $\zeta < \frac{1}{\sqrt{2}} \approx 0.707$. If $\zeta \ge 0.707$, the magnitude decreases monotonically from unity without any resonant peak.
Substituting $u_r = \sqrt{1 - 2\zeta^2}$ back into $M(u)$:
$$M_r = \frac{1}{\sqrt{[1 - (1 - 2\zeta^2)]^2 + 4\zeta^2(1 - 2\zeta^2)}} = \frac{1}{\sqrt{4\zeta^4 + 4\zeta^2 - 8\zeta^4}} = \frac{1}{\sqrt{4\zeta^2(1 - \zeta^2)}} = \frac{1}{2\zeta \sqrt{1 - \zeta^2}}$$

2. Resonant Frequency ($\omega_r$):
The frequency at which the maximum resonant peak occurs:
$$\omega_r = \omega_n \sqrt{1 - 2\zeta^2}$$

3. Bandwidth ($\omega_b$):
The bandwidth is the frequency at which the closed-loop magnitude drops by $3 \text{ dB}$ below its zero-frequency value (i.e., $|M(j\omega_b)| = \frac{1}{\sqrt{2}} M(0) = \frac{1}{\sqrt{2}}$):
$$\frac{1}{\sqrt{(1 - u_b^2)^2 + 4\zeta^2 u_b^2}} = \frac{1}{\sqrt{2}}$$
Squaring both sides:
$$(1 - u_b^2)^2 + 4\zeta^2 u_b^2 = 2 \implies u_b^4 - 2(1 - 2\zeta^2) u_b^2 - 1 = 0$$
Solving this quadratic equation in $u_b^2$ using the quadratic formula:
$$u_b^2 = (1 - 2\zeta^2) + \sqrt{(1 - 2\zeta^2)^2 + 1} = (1 - 2\zeta^2) + \sqrt{4\zeta^4 - 4\zeta^2 + 2}$$
Multiplying by $\omega_n$ yields the exact closed-loop bandwidth formula:
$$\omega_b = \omega_n \left[ (1 - 2\zeta^2) + \sqrt{4\zeta^4 - 4\zeta^2 + 2} \right]^{1/2}$$

Correlation between Time and Frequency Domain Performance:
- Both the time-domain peak overshoot $M_p = e^{-\frac{\pi\zeta}{\sqrt{1-\zeta^2}}}$ and the frequency-domain resonant peak $M_r = \frac{1}{2\zeta\sqrt{1-\zeta^2}}$ depend strictly and monotonically on damping ratio $\zeta$. A large $M_r$ directly indicates a large $M_p$ and poor transient damping.
- The resonant frequency $\omega_r = \omega_n \sqrt{1 - 2\zeta^2}$ is intimately linked to the damped ringing frequency $\omega_d = \omega_n \sqrt{1 - \zeta^2}$ and peak time $t_p = \frac{\pi}{\omega_d}$.
- System bandwidth $\omega_b$ is directly proportional to natural frequency $\omega_n$, which is inversely proportional to rise time $t_r$. A wider bandwidth ensures faster transient tracking speed, but admits greater high-frequency noise.
"""
    },
    {
        "qid": "lcs-q17",
        "marks": 7,
        "type": "Long Derivation",
        "title": "Bode Plot Construction: Asymptotic Magnitude Factors, Phase Calculation, and Slope Rules",
        "yt_query": "bode plot construction corner frequencies magnitude phase plot control systems",
        "img_path": "images/lcs/bode_plot_construction_slopes.png",
        "img_caption": "Figure 4.2: Asymptotic Bode Magnitude Slopes and Phase Curves for Canonical Factors",
        "answer": r"""
The Bode plot, introduced by Hendrik W. Bode in 1940, consists of two separate rectangular graphs plotted against frequency on a logarithmic scale:
1. Logarithmic Magnitude Plot: $20 \log_{10}|G(j\omega)|$ in decibels (dB) versus $\log_{10}\omega$.
2. Phase Angle Plot: Phase $\angle G(j\omega)$ in degrees versus $\log_{10}\omega$.

The fundamental mathematical advantage of the Bode diagram is that the multiplication of transfer function factors is transformed into simple algebraic addition of their respective decibel magnitudes and phase angles:
$$G(s) = K \frac{\prod (1 + s T_a)}{s^N \prod (1 + s T_1) \prod (s^2 + 2\zeta \omega_n s + \omega_n^2)}$$
$$20\log_{10}|G(j\omega)| = 20\log_{10} K + \sum 20\log_{10}|1 + j\omega T_a| - 20 N \log_{10}\omega - \sum 20\log_{10}|1 + j\omega T_1| - \dots$$
$$\angle G(j\omega) = \sum \tan^{-1}(\omega T_a) - N(90^\circ) - \sum \tan^{-1}(\omega T_1) - \dots$$

Every rational transfer function can be completely decomposed into five standard factors:
1. Constant Gain $K$:
   - Magnitude: $20 \log_{10} K$ dB (a horizontal line with zero slope for all frequencies).
   - Phase: $0^\circ$ if $K > 0$; $-180^\circ$ if $K < 0$.
2. Pole at the Origin $\frac{1}{s}$ (or $\frac{1}{(j\omega)^N}$):
   - Magnitude: $20\log_{10}\left|\frac{1}{(j\omega)^N}\right| = -20 N \log_{10}\omega$ dB. This is a straight line passing through $0$ dB at $\omega = 1 \text{ rad/s}$ with a constant downward slope of $-20 N \text{ dB/decade}$.
   - Phase: $-N \times 90^\circ$ constant for all $\omega$.
3. Zero at the Origin $s$ (or $(j\omega)^M$):
   - Magnitude: $+20 M \log_{10}\omega$ dB. A straight line passing through $0$ dB at $\omega = 1 \text{ rad/s}$ with an upward slope of $+20 M \text{ dB/decade}$.
   - Phase: $+M \times 90^\circ$.
4. Simple First-Order Pole $\frac{1}{1 + sT}$:
   - At frequencies well below the corner frequency ($\omega \ll \frac{1}{T}$): $1 + j\omega T \approx 1 \implies 20\log_{10}(1) = 0 \text{ dB}$ (low-frequency asymptote).
   - At frequencies well above the corner frequency ($\omega \gg \frac{1}{T}$): $1 + j\omega T \approx j\omega T \implies -20\log_{10}(\omega T) \text{ dB}$ (high-frequency asymptote with slope $-20 \text{ dB/decade}$).
   - The two asymptotes intersect at the corner frequency: $\omega_c = \frac{1}{T} \text{ rad/s}$.
   - Actual magnitude at corner frequency: $-20\log_{10}|1 + j1| = -20\log_{10}\sqrt{2} \approx -3.01 \text{ dB}$.
   - Phase: $\phi(\omega) = -\tan^{-1}(\omega T)$. At $\omega = 0.1 \omega_c$, $\phi \approx -5.7^\circ$; at $\omega = \omega_c$, $\phi = -45^\circ$; at $\omega = 10 \omega_c$, $\phi \approx -84.3^\circ \to -90^\circ$.
5. Simple First-Order Zero $(1 + sT)$:
   - Same corner frequency $\omega_c = \frac{1}{T}$, but introduces an asymptotic slope change of $+20 \text{ dB/decade}$ and a positive phase lead approaching $+90^\circ$ ($+45^\circ$ at $\omega_c$).

Systematic Bode Plot Construction Algorithm:
Step 1: Convert the given transfer function $G(s)H(s)$ into standard time-constant (Bode) form:
$$G(s)H(s) = \frac{K (1 + sT_1)}{s^N (1 + sT_a)(1 + sT_b)}$$
Step 2: Identify all corner frequencies: $\omega_{c1} = \frac{1}{T_1}, \omega_{ca} = \frac{1}{T_a}, \omega_{cb} = \frac{1}{T_b}$ and arrange them in ascending numerical order.
Step 3: Determine the initial asymptotic line. Choose a starting frequency $\omega_l$ at least one decade below the lowest corner frequency. If the system has $N$ poles at the origin:
- Initial slope = $-20 N \text{ dB/decade}$.
- Initial magnitude at $\omega = \omega_l$: $M_l = 20\log_{10} K - 20 N \log_{10}\omega_l$ dB.
Step 4: Progress through each corner frequency in order:
- At a first-order pole corner frequency, alter the slope by $-20 \text{ dB/decade}$.
- At a first-order zero corner frequency, alter the slope by $+20 \text{ dB/decade}$.
Step 5: Tabulate phase angles $\phi(\omega) = -N(90^\circ) + \tan^{-1}(\omega T_1) - \tan^{-1}(\omega T_a) - \tan^{-1}(\omega T_b)$ over a range spanning two decades below the lowest corner frequency to two decades above the highest corner frequency, and sketch the continuous phase curve.
"""
    },
    {
        "qid": "lcs-q18",
        "marks": 7,
        "type": "Long Derivation",
        "title": "Gain Margin and Phase Margin from Bode Plots: Analytical Definitions and Stability Criteria",
        "yt_query": "gain margin phase margin bode plot stability gain crossover phase crossover",
        "img_path": "images/lcs/gain_phase_margin_bode.png",
        "img_caption": "Figure 4.3: Graphical Identification of wgc, wpc, Gain Margin, and Phase Margin on Bode Plot",
        "answer": r"""
Relative stability in the frequency domain is evaluated using two vital stability metrics: Gain Margin (GM) and Phase Margin (PM). These measures quantify how much additional gain or phase lag can be tolerated by the feedback loop before it transitions from stability into sustained oscillation.

1. Phase Crossover Frequency ($\omega_{pc}$):
The phase crossover frequency is the exact frequency at which the open-loop phase angle curve crosses $-180^\circ$:
$$\angle G(j\omega_{pc})H(j\omega_{pc}) = -180^\circ$$

2. Gain Margin ($GM$):
The Gain Margin is defined as the reciprocal of the open-loop magnitude evaluated at the phase crossover frequency $\omega_{pc}$. In decibels, it is expressed as:
$$GM = 20 \log_{10} \frac{1}{|G(j\omega_{pc})H(j\omega_{pc})|} = -20 \log_{10} |G(j\omega_{pc})H(j\omega_{pc})| \text{ dB}$$
- Physical Meaning: $GM$ represents the factor by which the system loop gain can be increased before the system becomes unstable. If the magnitude in dB at $\omega_{pc}$ is negative (e.g., $-15 \text{ dB}$), the Gain Margin is positive ($+15 \text{ dB}$), indicating a safe operational buffer.

3. Gain Crossover Frequency ($\omega_{gc}$):
The gain crossover frequency is the exact frequency at which the open-loop magnitude curve crosses the unity gain line ($0 \text{ dB}$):
$$|G(j\omega_{gc})H(j\omega_{gc})| = 1 \implies 20\log_{10}|G(j\omega_{gc})H(j\omega_{gc})| = 0 \text{ dB}$$

4. Phase Margin ($PM$):
The Phase Margin is defined as the amount of additional phase lag that can be introduced into the feedback loop at the gain crossover frequency $\omega_{gc}$ before the closed-loop system reaches the verge of instability:
$$PM = 180^\circ + \angle G(j\omega_{gc})H(j\omega_{gc})$$
- Physical Meaning: Because stability requires the phase at unity gain to be above $-180^\circ$, if $\angle G(j\omega_{gc})H(j\omega_{gc}) = -135^\circ$, the Phase Margin is $PM = 180^\circ + (-135^\circ) = +45^\circ$. The system can tolerate an additional $45^\circ$ of unmodeled sensor delay before oscillating.

Criteria for Closed-Loop Stability from Bode Plot:
For minimum-phase open-loop systems (systems having no poles or zeros in the right half of the s-plane):
1. Stable System:
   $$GM > 0 \text{ dB} \quad \text{and} \quad PM > 0^\circ \iff \omega_{gc} < \omega_{pc}$$
   The gain crossover frequency occurs before the phase crossover frequency.
2. Marginally Stable System:
   $$GM = 0 \text{ dB} \quad \text{and} \quad PM = 0^\circ \iff \omega_{gc} = \omega_{pc}$$
   The magnitude is $0 \text{ dB}$ at the exact instant the phase is $-180^\circ$, producing sustained sinusoidal oscillations.
3. Unstable System:
   $$GM < 0 \text{ dB} \quad \text{and} \quad PM < 0^\circ \iff \omega_{gc} > \omega_{pc}$$
   The loop gain exceeds unity at the frequency where phase lag exceeds $180^\circ$, causing regenerative feedback and exponential divergence.

Comprehensive Numerical Computation from KTU PYQ:
Given: $G(s) = \frac{10}{s(1 + 0.1s)(1 + 0.05s)}$ with unity feedback ($H(s) = 1$).
Step 1: Substitute $s = j\omega$:
$$G(j\omega) = \frac{10}{j\omega(1 + j0.1\omega)(1 + j0.05\omega)}$$
Magnitude expression:
$$|G(j\omega)| = \frac{10}{\omega \sqrt{1 + 0.01\omega^2}\sqrt{1 + 0.0025\omega^2}}$$
Phase angle expression:
$$\angle G(j\omega) = -90^\circ - \tan^{-1}(0.1\omega) - \tan^{-1}(0.05\omega)$$

Step 2: Determine Phase Crossover Frequency $\omega_{pc}$:
Set $\angle G(j\omega_{pc}) = -180^\circ$:
$$-90^\circ - \tan^{-1}(0.1\omega_{pc}) - \tan^{-1}(0.05\omega_{pc}) = -180^\circ$$
$$\tan^{-1}(0.1\omega_{pc}) + \tan^{-1}(0.05\omega_{pc}) = 90^\circ$$
Using the identity $\tan(A + B) = \frac{\tan A + \tan B}{1 - \tan A \tan B} = \tan(90^\circ) = \infty$:
$$1 - (0.1\omega_{pc})(0.05\omega_{pc}) = 0 \implies 0.005 \omega_{pc}^2 = 1 \implies \omega_{pc}^2 = \frac{1}{0.005} = 200$$
$$\omega_{pc} = \sqrt{200} \approx 14.142 \text{ rad/s}$$

Step 3: Calculate Gain Margin:
Evaluate magnitude at $\omega_{pc} = 14.142 \text{ rad/s}$:
$$|G(j\omega_{pc})| = \frac{10}{14.142 \sqrt{1 + 0.01(200)}\sqrt{1 + 0.0025(200)}} = \frac{10}{14.142 \sqrt{3} \sqrt{1.5}} = \frac{10}{14.142 \times 1.732 \times 1.2247} = \frac{10}{30.0} = 0.3333$$
$$GM = 20\log_{10}\frac{1}{0.3333} = 20\log_{10}(3.0) \approx +9.54 \text{ dB}$$

Step 4: Determine Gain Crossover Frequency $\omega_{gc}$:
Set $|G(j\omega_{gc})| = 1$:
$$\frac{10}{\omega_{gc} \sqrt{1 + 0.01\omega_{gc}^2}\sqrt{1 + 0.0025\omega_{gc}^2}} = 1 \implies \omega_{gc}^2 (1 + 0.01\omega_{gc}^2)(1 + 0.0025\omega_{gc}^2) = 100$$
Solving iteratively: for $\omega = 7.0 \text{ rad/s}$:
$|G(j7)| = \frac{10}{7 \sqrt{1 + 0.49}\sqrt{1 + 0.1225}} = \frac{10}{7 \times 1.22 \times 1.06} = \frac{10}{9.05} \approx 1.10$
For $\omega = 7.5 \text{ rad/s}$: $|G(j7.5)| \approx 0.98 \approx 1$.
Thus, $\omega_{gc} \approx 7.4 \text{ rad/s}$.

Step 5: Calculate Phase Margin:
Evaluate phase at $\omega_{gc} = 7.4 \text{ rad/s}$:
$$\angle G(j7.4) = -90^\circ - \tan^{-1}(0.1 \times 7.4) - \tan^{-1}(0.05 \times 7.4) = -90^\circ - \tan^{-1}(0.74) - \tan^{-1}(0.37) = -90^\circ - 36.5^\circ - 20.3^\circ = -146.8^\circ$$
$$PM = 180^\circ + (-146.8^\circ) = +33.2^\circ$$
Because $\omega_{gc} (7.4) < \omega_{pc} (14.14)$, $GM = +9.54 \text{ dB} > 0$, and $PM = +33.2^\circ > 0$, the closed-loop system is strictly stable with excellent relative stability margins.
"""
    },
    {
        "qid": "lcs-q19",
        "marks": 3,
        "type": "Short Answer",
        "title": "Polar Plots: Asymptotic Behavior of Type 0, 1, and 2 Systems and Pole Addition Effects",
        "yt_query": "polar plots type 0 type 1 type 2 systems shape control systems",
        "img_path": "images/lcs/polar_plots_type_classification.png",
        "img_caption": "Figure 4.4: Canonical Nyquist Polar Plots for Type 0, Type 1, and Type 2 Open-Loop Transfer Functions",
        "answer": r"""
A polar plot of a sinusoidal transfer function $G(j\omega)$ is a plot of the magnitude $|G(j\omega)|$ versus the phase angle $\angle G(j\omega)$ on polar coordinates as the excitation frequency $\omega$ is varied continuously from $0$ to $+\infty$. In the complex plane, it traces out a continuous vector locus whose length equals the gain and whose angle with respect to the positive real axis represents the phase shift.

The geometry of a polar plot is governed by two fundamental asymptotic endpoints:
1. Low-Frequency Asymptote ($\omega \to 0$): Governed by the system Type number $N$ (number of poles at the origin):
   - Type 0 Systems ($N = 0$): $|G(j0)| = K$ (finite non-zero magnitude) and $\angle G(j0) = 0^\circ$. The polar plot originates on the positive real axis at $(K, 0^\circ)$.
   - Type 1 Systems ($N = 1$): As $\omega \to 0$, $|G(j\omega)| \to \infty$ and $\angle G(j\omega) \to -90^\circ$. The locus enters the complex plane from $-\infty$ along an asymptote parallel to the negative imaginary axis with a constant real-axis intercept given by $-K(T_1 + T_2)$.
   - Type 2 Systems ($N = 2$): As $\omega \to 0$, $|G(j\omega)| \to \infty$ and $\angle G(j\omega) \to -180^\circ$. The locus originates from $-\infty$ parallel to the negative real axis.

2. High-Frequency Asymptote ($\omega \to \infty$): Governed by the system Order $n$ (total number of open-loop poles minus zeros, assuming strictly proper system):
   - As $\omega \to \infty$, $|G(j\omega)| \to 0$ (the locus always terminates at the origin).
   - The angle of arrival at the origin is strictly $-n \times 90^\circ$:
     - For $n = 1$: Terminates at $0$ at $-90^\circ$ (tangent to negative imaginary axis, Quadrant IV).
     - For $n = 2$: Terminates at $0$ at $-180^\circ$ (tangent to negative real axis, Quadrant III).
     - For $n = 3$: Terminates at $0$ at $-270^\circ = +90^\circ$ (tangent to positive imaginary axis, Quadrant II).
     - For $n = 4$: Terminates at $0$ at $-360^\circ = 0^\circ$ (tangent to positive real axis, Quadrant I).

Effects of Adding Poles and Zeros to Transfer Function:
1. Addition of a Pole: Adding a simple pole $\frac{1}{1 + sT}$ introduces an additional phase lag of $\tan^{-1}(\omega T)$, rotating the entire polar plot clockwise by up to $90^\circ$ at high frequencies and reducing magnitude by $\frac{1}{\sqrt{1 + \omega^2 T^2}}$. This bends the locus closer to the critical point $(-1 + j0)$, generally degrading system stability.
2. Addition of a Zero: Adding a zero $(1 + sT)$ introduces phase lead of $+\tan^{-1}(\omega T)$, shifting the locus counter-clockwise by up to $90^\circ$ and expanding high-frequency magnitude. This pulls the locus away from $(-1 + j0)$, improving stability and damping.
"""
    },
    {
        "qid": "lcs-q20",
        "marks": 7,
        "type": "Long Derivation",
        "title": "Nyquist Stability Criterion: Cauchy's Argument Principle and Encirclement Analysis",
        "yt_query": "nyquist stability criterion cauchy argument principle N=P-Z control systems",
        "img_path": "images/lcs/nyquist_stability_contour.png",
        "img_caption": "Figure 4.5: Mapping of Nyquist s-Plane Contour into G(s)H(s) Plane around (-1, j0)",
        "answer": r"""
The Nyquist stability criterion, formulated by Harry Nyquist in 1932, is a powerful frequency-domain technique that determines the closed-loop stability of dynamic systems directly from the open-loop frequency response $G(j\omega)H(j\omega)$ without computing closed-loop roots. It accommodates non-minimum phase plants and systems with pure transport time delays.

The mathematical foundation rests on Cauchy's Principle of the Argument from complex variable theory:
Let $F(s)$ be a single-valued analytic function with $Z$ zeros and $P$ poles inside a closed continuous contour $\Gamma_s$ traversed in the clockwise direction in the s-plane. As $s$ traverses $\Gamma_s$ once in the clockwise direction, the corresponding locus of $F(s)$ in the complex $F(s)$-plane encircles the origin $N$ times in the clockwise direction, where:
$$N = Z - P$$
If $P > Z$, $N$ is negative, indicating $|N|$ counter-clockwise encirclements of the origin.

In closed-loop control systems, the characteristic function is:
$$F(s) = 1 + G(s)H(s)$$
Notice that:
1. The poles of $F(s)$ are identical to the poles of $G(s)H(s)$ (the open-loop poles).
2. The zeros of $F(s) = 1 + G(s)H(s) = 0$ are the closed-loop poles.
Instead of plotting $1 + G(s)H(s)$ around the origin, we subtract $1$ and plot the open-loop transfer function $G(s)H(s)$ directly. Encirclements of the origin by $1 + G(s)H(s)$ correspond precisely to encirclements of the critical point $(-1 + j0)$ by the locus of $G(s)H(s)$.

Nyquist Contour:
To detect whether any closed-loop poles reside in the unstable right half of the s-plane (RHP), we construct the Nyquist Contour $\Gamma_s$ enclosing the entire right-half s-plane:
1. Path along the imaginary axis from $s = -j\infty$ to $+j\infty$. (If open-loop poles exist at the origin, small semicircular indentations of radius $\epsilon \to 0$ bypass the poles into the RHP).
2. A large semicircular arc $s = R e^{j\theta}$ as $R \to \infty$ traversing from $\theta = +90^\circ$ through $0^\circ$ to $-90^\circ$.

The Nyquist Stability Theorem:
Let:
- $P$ = number of open-loop poles of $G(s)H(s)$ lying strictly in the right half of the s-plane (RHP).
- $Z$ = number of closed-loop poles lying in the right half of the s-plane.
- $N$ = number of clockwise encirclements of the critical point $(-1 + j0)$ by the complete Nyquist plot of $G(s)H(s)$ as $s$ traverses the Nyquist contour.
Then:
$$N = P - Z \implies Z = P - N$$
For a closed-loop system to be strictly stable, it must possess absolutely zero closed-loop poles in the right half plane ($Z = 0$). Therefore, the necessary and sufficient condition for closed-loop stability is:
$$N = P \quad \text{or} \quad N_{ccw} = P$$
where $N_{ccw} = -N$ is the number of counter-clockwise encirclements of $(-1 + j0)$.
- If the open-loop system is already stable ($P = 0$), then stability requires $N = 0$; that is, the Nyquist plot must not encircle the critical point $(-1 + j0)$ at all.
- If the open-loop system is open-loop unstable with $P$ poles in the RHP, then for closed-loop stability, the Nyquist plot must encircle the critical point $(-1 + j0)$ exactly $P$ times in the counter-clockwise direction ($N = -P$).

Step-by-Step Stability Analysis of an Open-Loop Unstable System:
Consider an open-loop unstable plant:
$$G(s)H(s) = \frac{K(s + 2)}{(s - 1)(s + 4)}$$
Here, there is an open-loop pole in the RHP at $s = +1$. Therefore, $P = 1$.
For the closed-loop system to be stable, we require $Z = 0$, which mandates:
$$N = P - Z = 1 - 0 = +1 \quad (\text{meaning } 1 \text{ counter-clockwise encirclement of } -1+j0, N_{ccw} = 1)$$
Evaluating $G(j\omega)H(j\omega)$ along the imaginary axis $s = j\omega$:
$$G(j\omega)H(j\omega) = \frac{K(j\omega + 2)}{(j\omega - 1)(j\omega + 4)}$$
At $\omega = 0$:
$$G(0)H(0) = \frac{K(2)}{(-1)(4)} = -\frac{K}{2}$$
The low-frequency intercept lies on the negative real axis at $-\frac{K}{2}$.
As $\omega \to \infty$:
$$G(j\omega)H(j\omega) \to \frac{K j\omega}{(j\omega)^2} = \frac{K}{j\omega} \to 0 \angle -90^\circ$$
The locus terminates at the origin from the fourth quadrant.
The real-axis intercept at $\omega = 0$ is $-\frac{K}{2}$.
If $-\frac{K}{2} < -1 \implies K > 2$, the point $(-1 + j0)$ falls inside the loop formed by the Nyquist locus and its infinite semicircle, resulting in exactly one counter-clockwise encirclement ($N_{ccw} = 1$).
Under this condition:
$$Z = P - N_{ccw} = 1 - 1 = 0$$
Thus, for $K > 2$, the closed-loop system is completely stable! If $K < 2$, the critical point $(-1 + j0)$ is not encircled ($N = 0$), which gives $Z = P - 0 = 1$, leaving one closed-loop pole in the RHP and causing instability. This elegant result demonstrates how feedback with sufficient gain can stabilize an inherently open-loop unstable dynamic plant.
"""
    }
]
