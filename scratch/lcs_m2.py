# -*- coding: utf-8 -*-
"""
Module 2 for Linear Control Systems (EET302)
Time Domain Analysis and Controllers
"""

M2_QUESTIONS = [
    {
        "qid": "lcs-q6",
        "marks": 3,
        "type": "Short Answer",
        "title": "Standard Test Signals and Transient Response of First-Order Systems",
        "yt_query": "standard test signals step response first order control system",
        "img_path": "images/lcs/first_order_step_response.png",
        "img_caption": "Figure 2.1: First-Order Exponential Step Response and Time Constant Tangent",
        "answer": r"""
In practical control systems, actual operating inputs cannot be predicted in advance because they are often random and non-deterministic. To enable objective comparison of dynamic performance across different systems, control engineers evaluate system responses using standardized mathematical test signals whose frequency content and rates of variation excite different aspects of the system dynamics.

The four primary standard test signals are defined as follows:
1. Unit Impulse Function $\delta(t)$: A mathematical singularity function defined as $\delta(t) = 0$ for all $t \ne 0$ and $\int_{-\infty}^{\infty} \delta(t) \, dt = 1$. It models an abrupt shock excitation of infinite amplitude and infinitesimal duration with a Laplace transform $R(s) = \mathcal{L}\{\delta(t)\} = 1$.
2. Unit Step Function $u(t)$: Defined as $u(t) = 0$ for $t < 0$ and $u(t) = 1$ for $t \ge 0$. It represents an instantaneous finite change in reference command, having a Laplace transform $R(s) = \frac{1}{s}$.
3. Unit Ramp Function $r(t)$: Defined as $r(t) = 0$ for $t < 0$ and $r(t) = t$ for $t \ge 0$. It models an input command varying at a constant velocity, with Laplace transform $R(s) = \frac{1}{s^2}$.
4. Unit Parabolic Function $p(t)$: Defined as $p(t) = 0$ for $t < 0$ and $p(t) = \frac{1}{2} t^2$ for $t \ge 0$. It represents an input command having constant acceleration, with Laplace transform $R(s) = \frac{1}{s^3}$.

Now consider a standard continuous-time first-order linear system characterized by the closed-loop transfer function:
$$\frac{C(s)}{R(s)} = \frac{1}{1 + sT}$$
where $T$ is the physical time constant of the system having units of seconds. When excited by a unit step command $R(s) = \frac{1}{s}$, the Laplace transform of the output response is:
$$C(s) = \frac{1}{s(1 + sT)} = \frac{1/T}{s(s + 1/T)}$$
Resolving $C(s)$ into partial fractions:
$$C(s) = \frac{A}{s} + \frac{B}{s + 1/T}$$
Evaluating the residues:
$$A = \lim_{s \to 0} [s C(s)] = \lim_{s \to 0} \frac{1}{1 + sT} = 1$$
$$B = \lim_{s \to -1/T} [(s + 1/T) C(s)] = \lim_{s \to -1/T} \frac{1/T}{s} = \frac{1/T}{-1/T} = -1$$
Substituting residues back yields:
$$C(s) = \frac{1}{s} - \frac{1}{s + 1/T}$$
Taking the inverse Laplace transform for $t \ge 0$:
$$c(t) = \mathcal{L}^{-1}\left\{\frac{1}{s} - \frac{1}{s + 1/T}\right\} = 1 - e^{-t/T}, \quad t \ge 0$$

The time constant $T$ represents the fundamental parameter dictating the speed of the exponential response. Evaluating the output at specific time intervals:
- At $t = 0$: $c(0) = 1 - e^0 = 0$.
- At $t = T$: $c(T) = 1 - e^{-1} = 1 - 0.3679 = 0.6321$ (63.2% of its final steady-state value).
- At $t = 2T$: $c(2T) = 1 - e^{-2} = 1 - 0.1353 = 0.8647$ (86.5%).
- At $t = 3T$: $c(3T) = 1 - e^{-3} = 1 - 0.0498 = 0.9502$ (95.0%).
- At $t = 4T$: $c(4T) = 1 - e^{-4} = 1 - 0.0183 = 0.9817$ (98.2%, entering the standard $\pm 2\%$ tolerance band).
Furthermore, the initial slope of the response curve is given by:
$$\left.\frac{dc(t)}{dt}\right|_{t=0} = \left.\frac{1}{T} e^{-t/T}\right|_{t=0} = \frac{1}{T}$$
This geometric property proves that if the system were to maintain its initial rate of response, it would reach its final steady-state value of unity in exactly one time constant $T$.
"""
    },
    {
        "qid": "lcs-q7",
        "marks": 7,
        "type": "Long Derivation",
        "title": "Mathematical Derivation of the Step Response of an Underdamped Second-Order System",
        "yt_query": "step response underdamped second order system derivation control systems",
        "img_path": "images/lcs/second_order_underdamped_response.png",
        "img_caption": "Figure 2.2: Unit Step Response of Second-Order Underdamped System Showing Transient Peaks",
        "answer": r"""
The standard canonical closed-loop transfer function of a second-order linear control system is universally expressed as:
$$\frac{C(s)}{R(s)} = \frac{\omega_n^2}{s^2 + 2\zeta \omega_n s + \omega_n^2}$$
where $\omega_n$ is the undamped natural frequency of oscillation (in rad/s) and $\zeta$ is the dimensionless damping ratio. In practical servo and regulation systems, the damping ratio is deliberately selected in the underdamped regime, where $0 < \zeta < 1$, ensuring a fast transient rise at the expense of slight damped oscillations.

For an underdamped system, the characteristic equation roots are complex conjugates:
$$s_{1,2} = -\zeta \omega_n \pm j \omega_n \sqrt{1 - \zeta^2} = -\zeta \omega_n \pm j \omega_d$$
where $\omega_d = \omega_n \sqrt{1 - \zeta^2}$ is the damped natural frequency.

When excited by a unit step command $R(s) = \frac{1}{s}$, the output transform becomes:
$$C(s) = \frac{\omega_n^2}{s(s^2 + 2\zeta \omega_n s + \omega_n^2)}$$
Completing the square in the quadratic denominator term:
$$s^2 + 2\zeta \omega_n s + \omega_n^2 = (s + \zeta \omega_n)^2 + \omega_n^2(1 - \zeta^2) = (s + \zeta \omega_n)^2 + \omega_d^2$$
We perform a partial fraction expansion:
$$C(s) = \frac{A}{s} + \frac{B s + D}{(s + \zeta \omega_n)^2 + \omega_d^2}$$
Multiplying through by $s[(s + \zeta \omega_n)^2 + \omega_d^2]$ yields the algebraic identity:
$$\omega_n^2 = A\left[(s + \zeta \omega_n)^2 + \omega_d^2\right] + (Bs + D)s = A(s^2 + 2\zeta \omega_n s + \omega_n^2) + B s^2 + D s$$
Equating coefficients of matching powers of $s$:
- For $s^0$ (constant term):
  $$\omega_n^2 = A \omega_n^2 \implies A = 1$$
- For $s^2$:
  $$0 = A + B \implies B = -A = -1$$
- For $s^1$:
  $$0 = 2 A \zeta \omega_n + D \implies D = -2\zeta \omega_n$$
Substituting these coefficients into $C(s)$:
$$C(s) = \frac{1}{s} - \frac{s + 2\zeta \omega_n}{(s + \zeta \omega_n)^2 + \omega_d^2}$$
We decompose the second term to match the standard Laplace transform pairs $\mathcal{L}^{-1}\left\{\frac{s+\alpha}{(s+\alpha)^2 + \omega^2}\right\} = e^{-\alpha t}\cos(\omega t)$ and $\mathcal{L}^{-1}\left\{\frac{\omega}{(s+\alpha)^2 + \omega^2}\right\} = e^{-\alpha t}\sin(\omega t)$:
$$C(s) = \frac{1}{s} - \frac{s + \zeta \omega_n}{(s + \zeta \omega_n)^2 + \omega_d^2} - \frac{\zeta \omega_n}{(s + \zeta \omega_n)^2 + \omega_d^2}$$
Multiplying and dividing the third term by $\omega_d = \omega_n \sqrt{1 - \zeta^2}$:
$$C(s) = \frac{1}{s} - \frac{s + \zeta \omega_n}{(s + \zeta \omega_n)^2 + \omega_d^2} - \frac{\zeta}{\sqrt{1 - \zeta^2}} \cdot \frac{\omega_d}{(s + \zeta \omega_n)^2 + \omega_d^2}$$
Taking the inverse Laplace transform on both sides for $t \ge 0$:
$$c(t) = 1 - e^{-\zeta \omega_n t} \cos(\omega_d t) - \frac{\zeta}{\sqrt{1 - \zeta^2}} e^{-\zeta \omega_n t} \sin(\omega_d t)$$
Factoring out the term $\frac{e^{-\zeta \omega_n t}}{\sqrt{1 - \zeta^2}}$:
$$c(t) = 1 - \frac{e^{-\zeta \omega_n t}}{\sqrt{1 - \zeta^2}} \left[\sqrt{1 - \zeta^2} \cos(\omega_d t) + \zeta \sin(\omega_d t)\right]$$
Constructing a right-angled reference triangle where the adjacent side is $\zeta$ and the opposite side is $\sqrt{1 - \zeta^2}$, the hypotenuse is $\sqrt{\zeta^2 + (1 - \zeta^2)} = 1$. Defining the angle $\theta$:
$$\cos\theta = \zeta, \quad \sin\theta = \sqrt{1 - \zeta^2}, \quad \theta = \tan^{-1}\left(\frac{\sqrt{1 - \zeta^2}}{\zeta}\right)$$
Substituting $\cos\theta$ and $\sin\theta$ into the bracketed expression:
$$\sqrt{1 - \zeta^2} \cos(\omega_d t) + \zeta \sin(\omega_d t) = \sin\theta \cos(\omega_d t) + \cos\theta \sin(\omega_d t) = \sin(\omega_d t + \theta)$$
This yields the final closed-form time-domain step response expression:
$$c(t) = 1 - \frac{e^{-\zeta \omega_n t}}{\sqrt{1 - \zeta^2}} \sin(\omega_d t + \theta), \quad t \ge 0$$
This fundamental result reveals that the transient response consists of a constant steady-state target of $1$, enveloped by an exponentially decaying sinusoidal oscillation whose decay envelope is governed by $e^{-\zeta \omega_n t}$ and whose frequency of oscillation is strictly the damped frequency $\omega_d$.
"""
    },
    {
        "qid": "lcs-q8",
        "marks": 7,
        "type": "Long Derivation",
        "title": "Comprehensive Derivations of Time Domain Performance Specifications",
        "yt_query": "time domain specifications rise time peak time peak overshoot settling time derivation",
        "img_path": "images/lcs/time_domain_specifications.png",
        "img_caption": "Figure 2.3: Transient Step Response Graph Defining td, tr, tp, Mp, and ts",
        "answer": r"""
The dynamic performance of a feedback control system is formally specified in the time domain by transient response metrics evaluated for a unit step input. For an underdamped second-order system with step response:
$$c(t) = 1 - \frac{e^{-\zeta \omega_n t}}{\sqrt{1 - \zeta^2}} \sin(\omega_d t + \theta)$$
we derive the exact mathematical formulas for the key time-domain specifications:

1. Delay Time ($t_d$):
The delay time is defined as the time required for the response to reach 50% of its final steady-state value on its very first rise. Setting $c(t_d) = 0.5$ leads to a transcendental equation that is accurately approximated by the linear empirical relationship:
$$t_d \approx \frac{1 + 0.7\zeta}{\omega_n}$$

2. Rise Time ($t_r$):
The rise time is defined as the time taken for the response to rise from 0% to 100% of its final steady-state value (for underdamped systems). At $t = t_r$, the response reaches unity: $c(t_r) = 1$.
$$1 - \frac{e^{-\zeta \omega_n t_r}}{\sqrt{1 - \zeta^2}} \sin(\omega_d t_r + \theta) = 1$$
$$\implies \frac{e^{-\zeta \omega_n t_r}}{\sqrt{1 - \zeta^2}} \sin(\omega_d t_r + \theta) = 0$$
Because the exponential decay term $e^{-\zeta \omega_n t_r} \ne 0$ for finite time, the sinusoidal term must vanish:
$$\sin(\omega_d t_r + \theta) = 0 \implies \omega_d t_r + \theta = \pi \implies \omega_d t_r = \pi - \theta$$
Solving explicitly for $t_r$:
$$t_r = \frac{\pi - \theta}{\omega_d} = \frac{\pi - \tan^{-1}\left(\frac{\sqrt{1-\zeta^2}}{\zeta}\right)}{\omega_n \sqrt{1 - \zeta^2}} \quad (\theta \text{ in radians})$$

3. Peak Time ($t_p$):
The peak time is the exact time instant at which the response attains its absolute first and highest peak overshoot. The local maxima occur when the time derivative of $c(t)$ vanishes: $\left.\frac{dc(t)}{dt}\right|_{t = t_p} = 0$.
Differentiating $c(t)$ using the product rule:
$$\frac{dc(t)}{dt} = -\frac{1}{\sqrt{1 - \zeta^2}} \left[(-\zeta \omega_n) e^{-\zeta \omega_n t} \sin(\omega_d t + \theta) + e^{-\zeta \omega_n t} \omega_d \cos(\omega_d t + \theta)\right]$$
Factoring out $\omega_n e^{-\zeta \omega_n t}$:
$$\frac{dc(t)}{dt} = \frac{\omega_n e^{-\zeta \omega_n t}}{\sqrt{1 - \zeta^2}} \left[\zeta \sin(\omega_d t + \theta) - \sqrt{1 - \zeta^2} \cos(\omega_d t + \theta)\right]$$
Substituting $\zeta = \cos\theta$ and $\sqrt{1 - \zeta^2} = \sin\theta$:
$$\zeta \sin(\omega_d t + \theta) - \sqrt{1 - \zeta^2} \cos(\omega_d t + \theta) = \cos\theta \sin(\omega_d t + \theta) - \sin\theta \cos(\omega_d t + \theta) = \sin[(\omega_d t + \theta) - \theta] = \sin(\omega_d t)$$
Thus, the time derivative simplifies to the remarkably elegant expression:
$$\frac{dc(t)}{dt} = \frac{\omega_n}{\sqrt{1 - \zeta^2}} e^{-\zeta \omega_n t} \sin(\omega_d t)$$
Setting this derivative to zero to locate extrema:
$$\sin(\omega_d t) = 0 \implies \omega_d t = n \pi, \quad n = 1, 2, 3, \dots$$
The very first peak ($n = 1$) corresponds to the maximum overshoot:
$$t_p = \frac{\pi}{\omega_d} = \frac{\pi}{\omega_n \sqrt{1 - \zeta^2}}$$

4. Maximum Percent Overshoot ($M_p$):
The maximum percent overshoot quantifies the peak deviation of the output beyond the steady-state final value, expressed as a percentage:
$$M_p = \frac{c(t_p) - c(\infty)}{c(\infty)} \times 100\% = [c(t_p) - 1] \times 100\%$$
Evaluating $c(t)$ at $t = t_p = \frac{\pi}{\omega_d}$:
$$c(t_p) = 1 - \frac{e^{-\zeta \omega_n (\pi/\omega_d)}}{\sqrt{1 - \zeta^2}} \sin\left(\omega_d \cdot \frac{\pi}{\omega_d} + \theta\right) = 1 - \frac{e^{-\frac{\pi \zeta \omega_n}{\omega_n \sqrt{1 - \zeta^2}}}}{\sqrt{1 - \zeta^2}} \sin(\pi + \theta)$$
Using the trigonometric identity $\sin(\pi + \theta) = -\sin\theta = -\sqrt{1 - \zeta^2}$:
$$c(t_p) = 1 - \frac{e^{-\frac{\pi \zeta}{\sqrt{1 - \zeta^2}}}}{\sqrt{1 - \zeta^2}} (-\sqrt{1 - \zeta^2}) = 1 + e^{-\frac{\pi \zeta}{\sqrt{1 - \zeta^2}}}$$
Subtracting the final value $1$ and multiplying by $100\%$:
$$M_p = e^{-\frac{\pi \zeta}{\sqrt{1 - \zeta^2}}} \times 100\%$$
This proves that maximum overshoot depends solely on the damping ratio $\zeta$, completely independent of the natural frequency $\omega_n$.

5. Settling Time ($t_s$):
The settling time is the time required for the response curve to reach and remain within a specified error tolerance band around the steady-state value. The transient oscillations are bounded by the decaying exponential envelope curves:
$$\text{Envelope} = 1 \pm \frac{e^{-\zeta \omega_n t}}{\sqrt{1 - \zeta^2}} \approx 1 \pm e^{-\zeta \omega_n t}$$
- For a $\pm 2\%$ tolerance band:
  $$e^{-\zeta \omega_n t_s} = 0.02 \implies -\zeta \omega_n t_s = \ln(0.02) \approx -3.912 \approx -4 \implies t_s = \frac{4}{\zeta \omega_n} = 4\tau$$
- For a $\pm 5\%$ tolerance band:
  $$e^{-\zeta \omega_n t_s} = 0.05 \implies -\zeta \omega_n t_s = \ln(0.05) \approx -2.996 \approx -3 \implies t_s = \frac{3}{\zeta \omega_n} = 3\tau$$
where $\tau = \frac{1}{\zeta \omega_n}$ is the effective transient time constant of the second-order system.
"""
    },
    {
        "qid": "lcs-q9",
        "marks": 3,
        "type": "Short Answer",
        "title": "Steady-State Error Analysis, Final Value Theorem, and Static Error Constants",
        "yt_query": "steady state error static error constants Kp Kv Ka type number control systems",
        "img_path": "images/lcs/steady_state_error_constants.png",
        "img_caption": "Figure 2.4: Tracking Errors for Step, Ramp, and Parabolic Inputs across System Types",
        "answer": r"""
Steady-state error is a fundamental measure of the tracking accuracy of a feedback control system as time approaches infinity. Consider a canonical unity feedback control system where the forward path has open-loop transfer function $G(s)$ and feedback path $H(s) = 1$. The actuating error signal $e(t)$ is the difference between reference input $r(t)$ and output $c(t)$:
$$e(t) = r(t) - c(t)$$
In the Laplace domain, output is $C(s) = G(s) E(s)$. Substituting this into the error equation:
$$E(s) = R(s) - C(s) = R(s) - G(s) E(s) \implies E(s)[1 + G(s)] = R(s) \implies E(s) = \frac{R(s)}{1 + G(s)}$$
For non-unity feedback systems with feedback transfer function $H(s)$, the generalized actuating error is:
$$E(s) = \frac{R(s)}{1 + G(s)H(s)}$$

Assuming that the closed-loop system is strictly stable (so that all poles of $s E(s)$ lie strictly in the open left half of the s-plane), the steady-state error $e_{ss}$ is determined using the Final Value Theorem of Laplace transforms:
$$e_{ss} = \lim_{t \to \infty} e(t) = \lim_{s \to 0} s E(s) = \lim_{s \to 0} \frac{s R(s)}{1 + G(s)H(s)}$$

The open-loop transfer function is characterized by its Type number $N$, defined as the number of pure open-loop integrators (poles at the origin $s=0$):
$$G(s)H(s) = \frac{K (1 + sT_a)(1 + sT_b)\dots}{s^N (1 + sT_1)(1 + sT_2)\dots}$$

We define three classical static error constants based on the standard test inputs:
1. Positional Error Constant ($K_p$): Evaluated for a unit step input $R(s) = \frac{1}{s}$:
   $$e_{ss} = \lim_{s \to 0} \frac{s(1/s)}{1 + G(s)H(s)} = \frac{1}{1 + \lim_{s \to 0} G(s)H(s)} = \frac{1}{1 + K_p}$$
   $$K_p = \lim_{s \to 0} G(s)H(s)$$

2. Velocity Error Constant ($K_v$): Evaluated for a unit ramp input $R(s) = \frac{1}{s^2}$:
   $$e_{ss} = \lim_{s \to 0} \frac{s(1/s^2)}{1 + G(s)H(s)} = \lim_{s \to 0} \frac{1}{s + s G(s)H(s)} = \frac{1}{\lim_{s \to 0} s G(s)H(s)} = \frac{1}{K_v}$$
   $$K_v = \lim_{s \to 0} s G(s)H(s)$$

3. Acceleration Error Constant ($K_a$): Evaluated for a unit parabolic input $R(s) = \frac{1}{s^3}$:
   $$e_{ss} = \lim_{s \to 0} \frac{s(1/s^3)}{1 + G(s)H(s)} = \frac{1}{\lim_{s \to 0} s^2 G(s)H(s)} = \frac{1}{K_a}$$
   $$K_a = \lim_{s \to 0} s^2 G(s)H(s)$$

The steady-state error behavior across system types is summarized in the universal matrix:
- Type 0 Systems ($N = 0$):
  - Step input: $K_p = K$, $e_{ss} = \frac{1}{1 + K}$ (finite constant error).
  - Ramp input: $K_v = 0$, $e_{ss} = \infty$ (error grows without bound).
  - Parabolic input: $K_a = 0$, $e_{ss} = \infty$.
- Type 1 Systems ($N = 1$):
  - Step input: $K_p = \infty$, $e_{ss} = 0$ (perfect tracking).
  - Ramp input: $K_v = K$, $e_{ss} = \frac{1}{K}$ (finite constant tracking lag).
  - Parabolic input: $K_a = 0$, $e_{ss} = \infty$.
- Type 2 Systems ($N = 2$):
  - Step input: $K_p = \infty$, $e_{ss} = 0$.
  - Ramp input: $K_v = \infty$, $e_{ss} = 0$.
  - Parabolic input: $K_a = K$, $e_{ss} = \frac{1}{K}$ (finite acceleration lag).

This analysis proves that increasing the system type eliminates steady-state errors for lower-order inputs, but adding integrators introduces negative phase shift that degrades closed-loop stability.
"""
    },
    {
        "qid": "lcs-q10",
        "marks": 7,
        "type": "Long Derivation",
        "title": "Industrial Controllers: Characteristics and Effects of P, PI, PD, and PID Schemes",
        "yt_query": "P PI PD PID controllers control systems effects on stability and steady state error",
        "img_path": "images/lcs/industrial_pid_controllers.png",
        "img_caption": "Figure 2.5: Parallel Block Topology and Bode Phase Profiles of P, PI, PD, and PID Controllers",
        "answer": r"""
Industrial process control universally relies on standard three-term controllers: Proportional (P), Integral (I), and Derivative (D). These control actions can be deployed individually or combined in various permutations to shape both the transient response and steady-state precision of feedback systems.

1. Proportional (P) Controller:
In a pure proportional controller, the actuation control signal $u(t)$ is directly proportional to the instantaneous error $e(t)$:
$$u(t) = K_p e(t) \iff G_c(s) = \frac{U(s)}{E(s)} = K_p$$
where $K_p$ is the adjustable proportional gain.
- Influence on System Dynamics: Increasing $K_p$ magnifies the forward loop gain, accelerating the speed of response and reducing the steady-state tracking error $e_{ss} = \frac{1}{1 + K_p}$. However, higher gain pushes closed-loop poles closer to the imaginary axis, reducing damping ratio $\zeta$, increasing overshoot $M_p$, and potentially causing dynamic instability. A pure P controller cannot completely eliminate steady-state error without requiring infinite gain.

2. Proportional-Integral (PI) Controller:
The PI controller supplements proportional action with an integral of past accumulated error:
$$u(t) = K_p e(t) + K_i \int_0^t e(\tau) \, d\tau = K_p \left[e(t) + \frac{1}{T_i} \int_0^t e(\tau) \, d\tau\right]$$
Taking the Laplace transform yields the controller transfer function:
$$G_c(s) = K_p + \frac{K_i}{s} = \frac{K_p s + K_i}{s} = K_p \left(\frac{s + 1/T_i}{s}\right)$$
where $T_i = K_p / K_i$ is the integral reset time.
- Influence on System Dynamics: The PI controller introduces a pole at the origin ($s = 0$) and a zero in the left half of the s-plane at $s = -1/T_i$. Introducing an open-loop integrator increments the system Type number by one (e.g., converting a Type 0 system into a Type 1 system). Consequently, the steady-state error to a step command is completely eliminated ($e_{ss} = 0$). However, the pole at $s = 0$ introduces $90^\circ$ of phase lag, reducing the system phase margin, lowering damping, and increasing transient settling time and peak overshoot.

3. Proportional-Derivative (PD) Controller:
The PD controller generates control action proportional to both the error and its time rate of change:
$$u(t) = K_p e(t) + K_d \frac{de(t)}{dt} = K_p \left[e(t) + T_d \frac{de(t)}{dt}\right]$$
In the Laplace domain:
$$G_c(s) = K_p + K_d s = K_p (1 + s T_d) = K_d \left(s + \frac{K_p}{K_d}\right)$$
where $T_d = K_d / K_p$ is the derivative time constant.
- Influence on System Dynamics: The PD controller introduces a real zero at $s = -K_p / K_d$ without adding a pole at the origin. This introduces phase lead into the forward path. In an underdamped second-order system $\frac{\omega_n^2}{s(s + 2\zeta \omega_n)}$, cascading with a PD controller $(K_p + K_d s)$ yields the modified characteristic equation:
$$s^2 + (2\zeta \omega_n + \omega_n^2 K_d)s + \omega_n^2 K_p = 0$$
Comparing coefficients shows that the effective damping term increases from $2\zeta \omega_n$ to $(2\zeta \omega_n + \omega_n^2 K_d)$. Hence, PD control significantly increases the system damping ratio $\zeta$, suppresses peak overshoot $M_p$, accelerates settling time $t_s$, and widens stability margins. However, pure derivative action acts as a high-pass filter that amplifies high-frequency measurement noise, and because it adds no pole at $s=0$, it does not change the system Type number or eliminate steady-state error.

4. Proportional-Integral-Derivative (PID) Controller:
The full PID controller combines all three operational terms to exploit their individual strengths:
$$u(t) = K_p e(t) + K_i \int_0^t e(\tau) \, d\tau + K_d \frac{de(t)}{dt} = K_p \left[e(t) + \frac{1}{T_i}\int_0^t e(\tau)\,d\tau + T_d \frac{de(t)}{dt}\right]$$
Taking the Laplace transform:
$$G_c(s) = K_p + \frac{K_i}{s} + K_d s = \frac{K_d s^2 + K_p s + K_i}{s} = \frac{K_d (s + z_1)(s + z_2)}{s}$$
- Influence on System Dynamics: The PID controller provides two configurable zeros and one pole at the origin. The pole at $s=0$ provides infinite DC gain, raising system Type by one and forcing steady-state error to zero for step commands. Simultaneously, the two zeros can be positioned in the complex plane to provide phase lead compensation, neutralizing the destabilizing phase lag of the integral term, dampening transient oscillations, and expanding the operational bandwidth.
"""
    }
]
