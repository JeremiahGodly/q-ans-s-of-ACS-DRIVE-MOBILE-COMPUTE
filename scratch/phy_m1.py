# -*- coding: utf-8 -*-
"""
Module 1: Oscillations and Waves (phy-q1 to phy-q5)
KTU 2019 Scheme Engineering Physics A (PHT100)
"""

MODULE_1 = {
    "module_id": "phy-m1",
    "module_num": "Module 1",
    "module_title": "Oscillations, Resonance and Wave Motion",
    "questions": [
        {
            "qid": "phy-q1",
            "marks": 7,
            "type": "Derivation",
            "title": "Damped Harmonic Oscillations: Differential Equation and Damping Regimes",
            "yt_query": "damped harmonic oscillations differential equation overdamped critically damped underdamped",
            "img_path": "images/physics/damped_oscillations.png",
            "img_caption": "Figure 1.1: Time Displacement Curves for Overdamped, Critically Damped, and Underdamped Oscillators",
            "answer": r"""
When an oscillating mechanical system moves through a viscous medium, resistive dissipative forces oppose its motion. These damping forces arise from internal molecular friction or medium viscosity, progressively depleting mechanical energy and converting it into thermal energy. Consider a particle of mass $m$ oscillating along the $x$-axis. It experiences two concurrent forces: a linear elastic restoring force and a velocity-dependent viscous damping force.

According to Hooke's law, the restoring force is directed towards the mean equilibrium position:
$$F_r = -k x$$
where $k$ represents the spring constant or force stiffness, and $x$ denotes the instantaneous displacement. Assuming viscous damping at moderate velocities, the dissipative damping force is directly proportional to the instantaneous velocity:
$$F_d = -b \frac{dx}{dt} = -b \dot{x}$$
where $b$ is the damping coefficient. Applying Newton's second law of motion to the oscillating particle yields:
$$m \frac{d^2 x}{dt^2} = F_r + F_d = -k x - b \frac{dx}{dt}$$
Rearranging all terms to the left-hand side gives:
$$m \frac{d^2 x}{dt^2} + b \frac{dx}{dt} + k x = 0$$
Dividing throughout by mass $m$:
$$\frac{d^2 x}{dt^2} + \frac{b}{m} \frac{dx}{dt} + \frac{k}{m} x = 0$$
To express this differential equation in standard form, we define the damping constant $\gamma = \frac{b}{2m}$ and the undamped natural angular frequency $\omega_0 = \sqrt{\frac{k}{m}}$. The equation becomes:
$$\frac{d^2 x}{dt^2} + 2\gamma \frac{dx}{dt} + \omega_0^2 x = 0$$

This is a homogeneous linear second-order differential equation with constant coefficients. Assuming a trial solution of the exponential form $x(t) = C e^{r t}$, its first and second time derivatives are $\frac{dx}{dt} = C r e^{rt}$ and $\frac{d^2 x}{dt^2} = C r^2 e^{rt}$. Substituting these into the differential equation yields the characteristic algebraic equation:
$$r^2 + 2\gamma r + \omega_0^2 = 0$$
Solving for the characteristic roots using the quadratic formula:
$$r = -\gamma \pm \sqrt{\gamma^2 - \omega_0^2}$$
The general solution is therefore the linear combination of the two independent solutions:
$$x(t) = C_1 e^{\left(-\gamma + \sqrt{\gamma^2 - \omega_0^2}\right)t} + C_2 e^{\left(-\gamma - \sqrt{\gamma^2 - \omega_0^2}\right)t} = e^{-\gamma t} \left[ C_1 e^{\sqrt{\gamma^2 - \omega_0^2}\,t} + C_2 e^{-\sqrt{\gamma^2 - \omega_0^2}\,t} \right]$$
The physical nature of the resulting motion depends entirely on the sign of the discriminant $(\gamma^2 - \omega_0^2)$, giving rise to three distinct physical regimes:

Case 1: Overdamped Motion (Heavy Damping, $\gamma > \omega_0$). The quantity $(\gamma^2 - \omega_0^2)$ is positive, so the square root $\beta = \sqrt{\gamma^2 - \omega_0^2}$ is a real number less than $\gamma$. Both roots $r_1 = -\gamma + \beta$ and $r_2 = -\gamma - \beta$ are purely real and negative. The displacement equation is:
$$x(t) = e^{-\gamma t} \left( C_1 e^{\beta t} + C_2 e^{-\beta t} \right)$$
The displacement decays exponentially towards zero without ever crossing the equilibrium position more than once. The motion is completely non-oscillatory (deadbeat). A practical example is the motion of a door damper filled with heavy oil or a deadbeat moving-coil galvanometer.

Case 2: Critically Damped Motion ($\gamma = \omega_0$). The discriminant vanishes ($\gamma^2 - \omega_0^2 = 0$), yielding two identical repeated real roots $r_1 = r_2 = -\gamma$. The general solution for repeated roots takes the form:
$$x(t) = (C_1 + C_2 t) e^{-\gamma t}$$
In this critical threshold regime, the displaced system returns to its equilibrium position in the absolute minimum possible time without overshooting. Critical damping is engineered into vehicle shock absorbers and sensitive measuring instruments to guarantee rapid, vibration-free settling.

Case 3: Underdamped Motion (Light Damping, $\gamma < \omega_0$). The discriminant $(\gamma^2 - \omega_0^2)$ is negative, making $\sqrt{\gamma^2 - \omega_0^2} = i \sqrt{\omega_0^2 - \gamma^2} = i \omega$, where $\omega = \sqrt{\omega_0^2 - \gamma^2}$ represents the modified angular frequency of damped oscillations. Using Euler's identity $e^{\pm i \omega t} = \cos(\omega t) \pm i \sin(\omega t)$, the general solution simplifies to:
$$x(t) = A e^{-\gamma t} \cos(\omega t - \phi)$$
where $A$ is the initial amplitude and $\phi$ is the initial phase angle, both determined by initial displacement and velocity conditions. The system executes true oscillatory motion, but the envelope of maximum amplitude decays exponentially according to $A(t) = A_0 e^{-\gamma t}$. The time required for the amplitude to drop to $1/e$ of its initial value is the relaxation time $\tau = \frac{1}{\gamma} = \frac{2m}{b}$.
"""
        },
        {
            "qid": "phy-q2",
            "marks": 7,
            "type": "Derivation",
            "title": "Forced Harmonic Oscillations: Steady-State Amplitude and Phase Derivation",
            "yt_query": "forced harmonic oscillations steady state amplitude phase derivation",
            "img_path": "images/physics/forced_oscillations.png",
            "img_caption": "Figure 1.2: Mechanical Frequency Response Showing Resonance Peak and Phase Lag",
            "answer": r"""
In real physical systems, damped oscillations eventually die out due to energy dissipation. To sustain oscillations indefinitely, an external periodic driving force must continuously inject energy into the system. A forced harmonic oscillator is governed by three forces: a linear restoring force $-kx$, a viscous damping force $-b \dot{x}$, and an external harmonic driving force $F(t) = F_0 \sin(\omega t)$, where $F_0$ is the driving force amplitude and $\omega$ is the driving angular frequency.

Applying Newton's second law of motion to the forced oscillating particle yields:
$$m \frac{d^2 x}{dt^2} = -k x - b \frac{dx}{dt} + F_0 \sin(\omega t)$$
Transposing all displacement-dependent terms to the left-hand side:
$$m \frac{d^2 x}{dt^2} + b \frac{dx}{dt} + k x = F_0 \sin(\omega t)$$
Dividing throughout by the mass $m$:
$$\frac{d^2 x}{dt^2} + \frac{b}{m} \frac{dx}{dt} + \frac{k}{m} x = \frac{F_0}{m} \sin(\omega t)$$
Substituting the standard parameters $\gamma = \frac{b}{2m}$, $\omega_0^2 = \frac{k}{m}$, and driving acceleration amplitude $f_0 = \frac{F_0}{m}$, we obtain the canonical non-homogeneous differential equation of forced harmonic motion:
$$\frac{d^2 x}{dt^2} + 2\gamma \frac{dx}{dt} + \omega_0^2 x = f_0 \sin(\omega t)$$

The complete mathematical solution consists of two components: the complementary function $x_c(t)$ (the transient response) and the particular integral $x_p(t)$ (the steady-state response). Because the transient response contains the exponential decay factor $e^{-\gamma t}$, it rapidly diminishes to zero over time. In steady-state operation, the system oscillates exclusively at the driving frequency $\omega$ with a phase lag $\phi$ behind the driving force. We propose a steady-state trial solution:
$$x(t) = A \sin(\omega t - \phi)$$
Differentiating this trial displacement with respect to time gives:
$$\frac{dx}{dt} = A \omega \cos(\omega t - \phi)$$
$$\frac{d^2 x}{dt^2} = -A \omega^2 \sin(\omega t - \phi)$$
Substituting these expressions into the differential equation:
$$-A \omega^2 \sin(\omega t - \phi) + 2\gamma A \omega \cos(\omega t - \phi) + \omega_0^2 A \sin(\omega t - \phi) = f_0 \sin(\omega t)$$
Regrouping terms:
$$A (\omega_0^2 - \omega^2) \sin(\omega t - \phi) + 2\gamma \omega A \cos(\omega t - \phi) = f_0 \sin[(\omega t - \phi) + \phi]$$
Expanding the right-hand side using the trigonometric addition formula $\sin(A + B) = \sin A \cos B + \cos A \sin B$:
$$A (\omega_0^2 - \omega^2) \sin(\omega t - \phi) + 2\gamma \omega A \cos(\omega t - \phi) = f_0 \cos\phi \sin(\omega t - \phi) + f_0 \sin\phi \cos(\omega t - \phi)$$
Equating coefficients of the orthogonal functions $\sin(\omega t - \phi)$ and $\cos(\omega t - \phi)$ on both sides:
$$A (\omega_0^2 - \omega^2) = f_0 \cos\phi \quad \text{--- (Equation 1)}$$
$$2\gamma \omega A = f_0 \sin\phi \quad \text{--- (Equation 2)}$$

To determine the steady-state amplitude $A$, we square both equations and add them together:
$$A^2 (\omega_0^2 - \omega^2)^2 + 4\gamma^2 \omega^2 A^2 = f_0^2 (\cos^2\phi + \sin^2\phi) = f_0^2$$
Factoring out $A^2$:
$$A^2 \left[ (\omega_0^2 - \omega^2)^2 + 4\gamma^2 \omega^2 \right] = f_0^2$$
Taking the square root gives the steady-state amplitude expression:
$$A = \frac{f_0}{\sqrt{(\omega_0^2 - \omega^2)^2 + 4\gamma^2 \omega^2}} = \frac{F_0}{\sqrt{m^2(\omega_0^2 - \omega^2)^2 + b^2 \omega^2}}$$
To obtain the phase lag $\phi$, we divide Equation 2 by Equation 1:
$$\tan\phi = \frac{f_0 \sin\phi}{f_0 \cos\phi} = \frac{2\gamma \omega}{\omega_0^2 - \omega^2} \implies \phi = \tan^{-1}\left(\frac{2\gamma \omega}{\omega_0^2 - \omega^2}\right)$$

Physical interpretation of phase angle across excitation frequencies:
1. Low driving frequencies ($\omega \ll \omega_0$): The denominator $(\omega_0^2 - \omega^2) \approx \omega_0^2 > 0$ and the numerator is nearly zero. Thus $\tan\phi \to 0 \implies \phi \approx 0$. The displacement is almost perfectly in phase with the driving force, and the motion is stiffness-controlled.
2. Natural frequency excitation ($\omega = \omega_0$): The denominator vanishes while the numerator is positive. Thus $\tan\phi \to \infty \implies \phi = \frac{\pi}{2}$. The displacement lags the driving force by exactly $90^\circ$, meaning the driving force is perfectly aligned in phase with oscillator velocity $\dot{x}(t)$, ensuring maximum rate of mechanical energy transfer.
3. High driving frequencies ($\omega \gg \omega_0$): The denominator becomes large and negative. Thus $\tan\phi \to -0 \implies \phi \to \pi$. The displacement oscillates completely out of phase ($180^\circ$ lag) with the driving force, and motion is inertia-controlled.
"""
        },
        {
            "qid": "phy-q3",
            "marks": 7,
            "type": "Derivation",
            "title": "Resonance, Sharpness of Resonance, Quality Factor, and Logarithmic Decrement",
            "yt_query": "sharpness of resonance quality factor logarithmic decrement engineering physics",
            "img_path": "images/physics/resonance_qfactor.png",
            "img_caption": "Figure 1.3: Amplitude Resonance Curves for Low, Medium, and High Damping Factors",
            "answer": r"""
Resonance is the physical phenomenon where an oscillating system driven by an external periodic force responds with maximum amplitude when the excitation frequency approaches the system's natural frequency. Depending on the physical parameter observed, we distinguish between amplitude resonance (maximum displacement) and velocity resonance (maximum velocity).

To find the condition for amplitude resonance, we determine the driving frequency $\omega$ that maximizes the steady-state amplitude:
$$A(\omega) = \frac{f_0}{\sqrt{(\omega_0^2 - \omega^2)^2 + 4\gamma^2 \omega^2}}$$
Maximizing $A(\omega)$ is equivalent to minimizing the radicand function $f(\omega) = (\omega_0^2 - \omega^2)^2 + 4\gamma^2 \omega^2$ with respect to $\omega$. Differentiating and equating to zero:
$$\frac{df}{d\omega} = 2(\omega_0^2 - \omega^2)(-2\omega) + 8\gamma^2 \omega = 0$$
Since $\omega \neq 0$, dividing by $4\omega$ gives:
$$-(\omega_0^2 - \omega^2) + 2\gamma^2 = 0 \implies \omega^2 = \omega_0^2 - 2\gamma^2$$
Therefore, the amplitude resonant angular frequency is:
$$\omega_r = \sqrt{\omega_0^2 - 2\gamma^2}$$
Notice that amplitude resonance occurs at a frequency strictly lower than the undamped natural frequency $\omega_0$. For resonance to be physically possible, $\omega_0^2 - 2\gamma^2 > 0 \implies \gamma < \frac{\omega_0}{\sqrt{2}}$. Substituting $\omega_r$ back into the amplitude formula gives the peak resonant amplitude:
$$A_{max} = \frac{f_0}{\sqrt{\left[\omega_0^2 - (\omega_0^2 - 2\gamma^2)\right]^2 + 4\gamma^2(\omega_0^2 - 2\gamma^2)}} = \frac{f_0}{\sqrt{4\gamma^4 + 4\gamma^2 \omega_0^2 - 8\gamma^4}} = \frac{f_0}{2\gamma \sqrt{\omega_0^2 - \gamma^2}}$$
For negligible or light damping ($\gamma \ll \omega_0$), this peak value simplifies to $A_{max} \approx \frac{f_0}{2\gamma \omega_0}$.

Sharpness of resonance refers to the rate at which the response amplitude falls off on either side of the resonant peak as the excitation frequency deviates from $\omega_0$. If a small shift away from resonance causes a steep decline in amplitude, the resonance is described as sharp; if the response varies sluggishly over a wide frequency band, the resonance is flat. Damping directly governs sharpness: low damping yields a narrow, tall peak, while heavy damping flattens the curve.

The sharpness of resonance is quantitatively measured by the Quality Factor ($Q$-factor). By fundamental definition, the $Q$-factor is $2\pi$ times the ratio of the total energy stored in the oscillator to the energy dissipated per cycle:
$$Q = 2\pi \frac{\text{Stored Energy}}{\text{Energy Dissipated Per Cycle}} = \frac{\omega_0}{2\gamma} = \frac{m \omega_0}{b}$$
In the frequency domain, the $Q$-factor is expressed in terms of the resonant frequency $\omega_0$ and the half-power bandwidth $\Delta \omega = \omega_2 - \omega_1$:
$$Q = \frac{\omega_0}{\Delta \omega} = \frac{f_0}{f_2 - f_1}$$
where $\omega_1$ and $\omega_2$ are the lower and upper half-power cut-off frequencies at which the power absorbed drops to half its maximum value, or equivalently where displacement amplitude falls to $\frac{1}{\sqrt{2}} A_{max}$. A higher $Q$-factor indicates superior frequency selectivity and low energy loss per oscillation cycle.

In decaying underdamped oscillations, the rate of amplitude attenuation is quantified by the Logarithmic Decrement ($\delta$). It is defined as the natural logarithm of the ratio of any two consecutive peak amplitudes separated by one full time period $T$:
$$\delta = \ln\left(\frac{A_n}{A_{n+1}}\right)$$
Since consecutive peak amplitudes follow the exponential envelope $A(t) = A_0 e^{-\gamma t}$, their ratio is:
$$\frac{A_n}{A_{n+1}} = \frac{A_0 e^{-\gamma t}}{A_0 e^{-\gamma (t + T)}} = e^{\gamma T}$$
Taking the natural logarithm yields:
$$\delta = \ln(e^{\gamma T}) = \gamma T = \frac{\gamma \cdot 2\pi}{\omega}$$
For light damping where $\omega \approx \omega_0$, substituting $\gamma = \frac{\omega_0}{2Q}$ gives the direct relation:
$$\delta = \left(\frac{\omega_0}{2Q}\right)\left(\frac{2\pi}{\omega_0}\right) = \frac{\pi}{Q}$$
This equation shows that the logarithmic decrement is inversely proportional to the Quality factor.
"""
        },
        {
            "qid": "phy-q4",
            "marks": 7,
            "type": "Derivation",
            "title": "One-Dimensional Wave Equation: Derivation from Fundamental Principles",
            "yt_query": "one dimensional wave equation derivation transverse waves stretched string",
            "img_path": "images/physics/wave_equation_segment.png",
            "img_caption": "Figure 1.4: Differential String Element Showing Tensile Forces and Slopes",
            "answer": r"""
A mechanical wave is a disturbance that travels through an elastic continuous medium, transferring momentum and energy without the permanent bulk transport of matter. When a stretched flexible string is displaced transversely from its equilibrium position, the tension in the string generates an elastic restoring force that pulls displaced elements back towards equilibrium.

Consider a perfectly flexible, uniform string under constant tension $T$ having a linear mass density (mass per unit length) $\mu$. In its undisturbed equilibrium configuration, the string lies horizontally along the $x$-axis. When plucked, transverse displacements $y(x,t)$ are produced in the vertical $y$-direction. We analyze an infinitesimal segment of the string bounded between spatial coordinates $x$ and $x + \Delta x$. We adopt two standard physical assumptions: the transverse displacements and slopes $\frac{\partial y}{\partial x}$ are sufficiently small such that the tension $T$ remains uniform and constant throughout the motion, and string elements move purely in the vertical transverse direction without longitudinal displacement.

At coordinate $x$, the tension force $T$ acts tangentially to the string at an angle $\theta$ to the horizontal. At coordinate $x + \Delta x$, the tension $T$ acts tangentially at an angle $\theta + \Delta \theta$. Resolving these tension forces into horizontal and vertical components:
Horizontal forces:
$$\Sigma F_x = T \cos(\theta + \Delta \theta) - T \cos\theta$$
For small angular deflections, $\cos\theta \approx 1$, meaning horizontal forces cancel out and there is zero net horizontal acceleration.
Vertical forces:
$$\Sigma F_y = T \sin(\theta + \Delta \theta) - T \sin\theta$$
For small angles $\theta$, we apply the small-angle approximation $\sin\theta \approx \tan\theta = \frac{\partial y}{\partial x}$. The net vertical transverse force acting on the segment becomes:
$$\Sigma F_y = T \left[ \tan(\theta + \Delta \theta) - \tan\theta \right] = T \left[ \left(\frac{\partial y}{\partial x}\right)_{x + \Delta x} - \left(\frac{\partial y}{\partial x}\right)_x \right]$$
Using Taylor series expansion or the fundamental definition of the spatial derivative:
$$\left(\frac{\partial y}{\partial x}\right)_{x + \Delta x} - \left(\frac{\partial y}{\partial x}\right)_x = \frac{\partial}{\partial x}\left(\frac{\partial y}{\partial x}\right) \Delta x = \frac{\partial^2 y}{\partial x^2} \Delta x$$
Substituting this into the vertical force expression yields:
$$\Sigma F_y = T \frac{\partial^2 y}{\partial x^2} \Delta x$$

Now we apply Newton's second law of motion to this differential string element. The mass of the segment is $\Delta m = \mu \Delta x$, and its transverse acceleration is $\frac{\partial^2 y}{\partial t^2}$. Therefore:
$$\Sigma F_y = \Delta m \frac{\partial^2 y}{\partial t^2} = (\mu \Delta x) \frac{\partial^2 y}{\partial t^2}$$
Equating the dynamic inertia force to the net elastic transverse tension force:
$$\mu \Delta x \frac{\partial^2 y}{\partial t^2} = T \frac{\partial^2 y}{\partial x^2} \Delta x$$
Dividing both sides by $\Delta x$:
$$\mu \frac{\partial^2 y}{\partial t^2} = T \frac{\partial^2 y}{\partial x^2} \implies \frac{\partial^2 y}{\partial t^2} = \frac{T}{\mu} \frac{\partial^2 y}{\partial x^2}$$
Defining the wave propagation velocity $v = \sqrt{\frac{T}{\mu}}$, this differential relationship takes the canonical form of the Classical One-Dimensional Wave Equation:
$$\frac{\partial^2 y}{\partial t^2} = v^2 \frac{\partial^2 y}{\partial x^2} \quad \text{or} \quad \frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2}\frac{\partial^2 y}{\partial t^2}$$

This partial differential equation connects the temporal acceleration of any medium point to the spatial curvature of the wave profile at that instant. According to D'Alembert's theorem, the general solution of this equation is given by the superposition of two arbitrary traveling wave profiles:
$$y(x,t) = f(x - vt) + g(x + vt)$$
where $f(x - vt)$ represents a non-dispersive wave travelling in the positive $x$-direction at speed $v$, and $g(x + vt)$ represents a wave travelling in the negative $x$-direction at the same speed.
"""
        },
        {
            "qid": "phy-q5",
            "marks": 7,
            "type": "Derivation",
            "title": "Transverse Vibrations of a Stretched String: Boundary Conditions and Harmonics",
            "yt_query": "transverse vibrations stretched string standing waves harmonics mersenne laws",
            "img_path": "images/physics/standing_waves_string.png",
            "img_caption": "Figure 1.5: Standing Wave Modes on a Stretched String (Fundamental, 2nd, and 3rd Harmonics)",
            "answer": r"""
When two identical transverse harmonic waves of the same frequency and amplitude travel along a stretched string in mutually opposite directions, their linear superposition forms a stationary or standing wave. In a standing wave, energy is trapped within the medium, producing fixed spatial points with zero motion (nodes) and alternating points of maximum oscillation amplitude (antinodes).

Consider a uniform string of length $L$ stretched under tension $T$ with linear mass density $\mu$, rigidly clamped at both ends $x = 0$ and $x = L$. The governing one-dimensional wave equation is:
$$\frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2}\frac{\partial^2 y}{\partial t^2}, \quad \text{where } v = \sqrt{\frac{T}{\mu}}$$
Using the method of separation of variables, we express the transverse displacement as a product of a purely spatial function $X(x)$ and a purely temporal function $T(t)$:
$$y(x,t) = X(x) \cdot T(t)$$
Differentiating and substituting into the wave equation:
$$X''(x) T(t) = \frac{1}{v^2} X(x) \ddot{T}(t) \implies \frac{X''(x)}{X(x)} = \frac{1}{v^2}\frac{\ddot{T}(t)}{T(t)} = -k^2$$
where $-k^2$ is a negative separation constant necessary for oscillatory behavior. This yields two ordinary differential equations:
$$X''(x) + k^2 X(x) = 0$$
$$\ddot{T}(t) + \omega^2 T(t) = 0 \quad (\text{where } \omega = v k)$$
The spatial solution is:
$$X(x) = C_1 \cos(kx) + C_2 \sin(kx)$$
Now we apply the rigid boundary conditions at the clamped ends of the string:
1. At the left clamped end ($x = 0$): The string cannot move, so $y(0,t) = 0 \implies X(0) = 0$.
$$X(0) = C_1 \cos(0) + C_2 \sin(0) = C_1 = 0$$
Thus $C_1 = 0$, leaving $X(x) = C_2 \sin(kx)$.
2. At the right clamped end ($x = L$): The displacement must also be zero, so $y(L,t) = 0 \implies X(L) = 0$.
$$X(L) = C_2 \sin(k L) = 0$$
For non-trivial oscillations ($C_2 \neq 0$), the sine argument must be an integer multiple of $\pi$:
$$k L = n \pi \implies k_n = \frac{n \pi}{L}, \quad n = 1, 2, 3, \dots$$
Since wave vector $k = \frac{2\pi}{\lambda}$, the allowed stationary wavelengths are quantized:
$$\lambda_n = \frac{2L}{n}$$

The corresponding quantized natural frequencies of vibration are obtained from $f_n = \frac{v}{\lambda_n}$:
$$f_n = \frac{n v}{2L} = \frac{n}{2L}\sqrt{\frac{T}{\mu}}, \quad n = 1, 2, 3, \dots$$
Analysis of harmonic vibrational modes:
1. Fundamental Mode ($n = 1$): This is the fundamental frequency or first harmonic:
$$f_1 = \frac{1}{2L}\sqrt{\frac{T}{\mu}}$$
The string vibrates in a single loop with nodes at the ends ($x = 0, x = L$) and a single antinode at the center ($x = L/2$).
2. Second Harmonic ($n = 2$): Known as the first overtone:
$$f_2 = \frac{2}{2L}\sqrt{\frac{T}{\mu}} = 2 f_1$$
The string vibrates in two loops with three nodes ($x = 0, L/2, L$) and two antinodes ($x = L/4, 3L/4$).
3. Third Harmonic ($n = 3$): Known as the second overtone:
$$f_3 = \frac{3}{2L}\sqrt{\frac{T}{\mu}} = 3 f_1$$
In general, $f_n = n f_1$. A stretched string fixed at both ends supports all integer harmonics (both odd and even), creating a rich musical acoustic spectrum.

From the fundamental frequency equation $f = \frac{1}{2L}\sqrt{\frac{T}{\mu}}$, Mersenne formulated the three fundamental empirical laws of transverse vibrations:
1. Law of Length: The fundamental frequency is inversely proportional to the vibrating length: $f \propto \frac{1}{L}$ (for constant $T, \mu$).
2. Law of Tension: The fundamental frequency is directly proportional to the square root of tension: $f \propto \sqrt{T}$ (for constant $L, \mu$).
3. Law of Mass: The fundamental frequency is inversely proportional to the square root of linear mass density: $f \propto \frac{1}{\sqrt{\mu}}$ (for constant $L, T$). If the wire has radius $r$ and density $\rho$, $\mu = \pi r^2 \rho$, leading to $f \propto \frac{1}{r \sqrt{\rho}}$.
"""
        }
    ]
}
