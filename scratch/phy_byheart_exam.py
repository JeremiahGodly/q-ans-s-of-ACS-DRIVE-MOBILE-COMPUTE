# -*- coding: utf-8 -*-
"""
Byheart Data and Exam Questions for Engineering Physics A (PHT100)
Covers phy-q1 to phy-q26
"""

PHYSICS_BYHEART = {
    "phy-q1": {
        "eq": r"$$\frac{d^2 x}{dt^2} + 2\gamma \frac{dx}{dt} + \omega_0^2 x = 0 \implies x(t) = A e^{-\gamma t}\cos(\omega t - \phi), \quad \omega = \sqrt{\omega_0^2 - \gamma^2}$$",
        "text": r"<strong>Damped Motion Equation:</strong> $\ddot{x} + 2\gamma\dot{x} + \omega_0^2 x = 0$, where $\gamma = b/2m$ and $\omega_0 = \sqrt{k/m}$.<br><strong>Three Regimes:</strong><br>1. <strong>Overdamped ($\gamma > \omega_0$):</strong> Deadbeat exponential return without oscillation.<br>2. <strong>Critically Damped ($\gamma = \omega_0$):</strong> Fastest return to equilibrium without overshoot ($x = (C_1 + C_2 t)e^{-\gamma t}$).<br>3. <strong>Underdamped ($\gamma < \omega_0$):</strong> Oscillatory motion with decaying amplitude $A(t) = A_0 e^{-\gamma t}$ and frequency $\omega = \sqrt{\omega_0^2 - \gamma^2}$.<br><strong>Relaxation Time:</strong> $\tau = 1/\gamma = 2m/b$."
    },
    "phy-q2": {
        "eq": r"$$A = \frac{f_0}{\sqrt{(\omega_0^2 - \omega^2)^2 + 4\gamma^2 \omega^2}}, \quad \tan\phi = \frac{2\gamma \omega}{\omega_0^2 - \omega^2}$$",
        "text": r"<strong>Steady-State Solution:</strong> $x(t) = A \sin(\omega t - \phi)$.<br><strong>Phase Angle Across Frequencies:</strong><br>1. $\omega \ll \omega_0 \implies \phi \to 0$ (displacement in phase with driving force, stiffness-controlled).<br>2. $\omega = \omega_0 \implies \phi = \pi/2$ (displacement lags force by $90^\circ$, force in phase with velocity, velocity resonance).<br>3. $\omega \gg \omega_0 \implies \phi \to \pi$ (displacement lags force by $180^\circ$, inertia-controlled)."
    },
    "phy-q3": {
        "eq": r"$$\omega_r = \sqrt{\omega_0^2 - 2\gamma^2}, \quad Q = \frac{\omega_0}{2\gamma} = \frac{\omega_0}{\Delta \omega}, \quad \delta = \gamma T = \frac{\pi}{Q}$$",
        "text": r"<strong>Resonant Frequency:</strong> Amplitude resonance occurs at $\omega_r = \sqrt{\omega_0^2 - 2\gamma^2} < \omega_0$.<br><strong>Quality Factor ($Q$):</strong> $Q = 2\pi \frac{\text{Energy Stored}}{\text{Energy Lost / Cycle}} = \frac{\omega_0}{\text{Bandwidth }\Delta\omega}$. Higher $Q$ means sharper resonance and lower damping.<br><strong>Logarithmic Decrement ($\delta$):</strong> $\delta = \ln(A_n / A_{n+1}) = \gamma T = \pi / Q$."
    },
    "phy-q4": {
        "eq": r"$$\frac{\partial^2 y}{\partial t^2} = v^2 \frac{\partial^2 y}{\partial x^2}, \quad \text{where } v = \sqrt{\frac{T}{\mu}}$$",
        "text": r"<strong>1D Wave Equation:</strong> Relates local acceleration to spatial curvature in a continuous elastic medium.<br><strong>Wave Velocity on Stretched String:</strong> $v = \sqrt{T/\mu}$, where $T$ is tension and $\mu$ is linear mass density.<br><strong>D'Alembert Solution:</strong> $y(x,t) = f(x - vt) + g(x + vt)$."
    },
    "phy-q5": {
        "eq": r"$$f_n = \frac{n v}{2L} = \frac{n}{2L}\sqrt{\frac{T}{\mu}}, \quad \lambda_n = \frac{2L}{n}, \quad n = 1, 2, 3, \dots$$",
        "text": r"<strong>Standing Wave Modes:</strong> Fixed ends require nodes at $x = 0$ and $x = L$, giving quantized wave vectors $k_n = n\pi / L$.<br><strong>Harmonics:</strong> Supports all harmonics $f_n = n f_1$ ($f_1 = \frac{1}{2L}\sqrt{T/\mu}$).<br><strong>Mersenne's Laws:</strong> $f \propto 1/L$, $f \propto \sqrt{T}$, $f \propto 1/\sqrt{\mu}$."
    },
    "phy-q6": {
        "eq": r"$$\Delta = 2\mu t \cos r - \frac{\lambda}{2} \implies \text{Bright: } 2\mu t \cos r = (2n + 1)\frac{\lambda}{2}, \quad \text{Dark: } 2\mu t \cos r = n\lambda$$",
        "text": r"<strong>Geometric Path Difference:</strong> $\Delta_{geom} = 2\mu t \cos r$.<br><strong>Stokes' Phase Shift:</strong> Reflection at an optically denser medium introduces an equivalent path difference of $\lambda/2$.<br><strong>Zero Thickness ($t \to 0$):</strong> Effective path difference $\Delta = -\lambda/2$, causing destructive interference across all visible wavelengths (very thin film appears pitch black)."
    },
    "phy-q7": {
        "eq": r"$$\beta = \frac{\lambda L}{2d} \implies d = \frac{\lambda L}{2\beta}$$",
        "text": r"<strong>Air Wedge Fringe Width:</strong> $\beta = \frac{\lambda}{2\theta} = \frac{\lambda L}{2d}$, producing equidistant, straight, parallel fringes.<br><strong>Apex Line of Contact:</strong> Always a dark fringe ($2t = 0 \cdot \lambda$).<br><strong>Wire Diameter ($d$):</strong> Measured using travelling microscope: $d = \frac{\lambda L}{2\beta}$."
    },
    "phy-q8": {
        "eq": r"$$D_n^2 = 4n R \lambda \text{ (Dark)}, \quad \lambda = \frac{D_{n+p}^2 - D_n^2}{4 p R}, \quad \mu = \frac{(D_{n+p}^2 - D_n^2)_{air}}{(D_{n+p}^2 - D_n^2)_{liquid}}$$",
        "text": r"<strong>Air Film Thickness:</strong> $t = r^2 / 2R$.<br><strong>Dark Ring Diameters:</strong> $D_n \propto \sqrt{n}$ ($D_n = 2\sqrt{n R \lambda}$); center is dark ($D_0 = 0$).<br><strong>Bright Ring Diameters:</strong> $D_n \propto \sqrt{2n - 1}$.<br><strong>Liquid Film:</strong> Fringes contract when liquid of index $\mu > 1$ is introduced ($D_n \propto 1/\sqrt{\mu}$)."
    },
    "phy-q9": {
        "eq": r"$$I(\theta) = I_0 \left(\frac{\sin\alpha}{\alpha}\right)^2, \quad \alpha = \frac{\pi a \sin\theta}{\lambda}, \quad \text{Minima: } a \sin\theta = m\lambda$$",
        "text": r"<strong>Fraunhofer Single Slit:</strong> Sinc-squared intensity pattern.<br><strong>Central Maximum:</strong> Width $2\theta_1 = 2\lambda/a$, contains $>90\%$ of total optical energy.<br><strong>Diffraction Minima:</strong> $a \sin\theta = \pm m\lambda$ ($m = 1, 2, 3, \dots$).<br><strong>Secondary Maxima:</strong> Occur at $\tan\alpha = \alpha$ with rapidly falling intensities ($I_1 \approx 4.7\% I_0, I_2 \approx 1.65\% I_0$)."
    },
    "phy-q10": {
        "eq": r"$$(a + b)\sin\theta = n\lambda, \quad \frac{d\theta}{d\lambda} = \frac{n}{(a+b)\cos\theta}, \quad R = \frac{\lambda}{d\lambda} = n N$$",
        "text": r"<strong>Grating Equation:</strong> $(a + b)\sin\theta = n\lambda$, where $d = a + b$ is the grating element.<br><strong>Max Order:</strong> $n_{max} = \lfloor (a+b)/\lambda \rfloor$.<br><strong>Dispersive Power:</strong> $\frac{d\theta}{d\lambda} = \frac{n}{(a+b)\cos\theta}$ (linear normal spectrum).<br><strong>Resolving Power:</strong> $R = \lambda / d\lambda = n N$ (Rayleigh's criterion, product of order $n$ and total rulings $N$)."
    },
    "phy-q11": {
        "eq": r"$$\lambda = \frac{h}{\sqrt{2mE}} = \frac{h}{\sqrt{2mqV}} = \frac{1.227}{\sqrt{V}}\text{ nm}, \quad \Delta x \cdot \Delta p_x \ge \frac{\hbar}{2}$$",
        "text": r"<strong>Matter Waves:</strong> De Broglie relation $\lambda = h/p$. Accelerated electron: $\lambda = 1.227/\sqrt{V}\text{ nm}$.<br><strong>Uncertainty Principle:</strong> $\Delta x \cdot \Delta p_x \ge \hbar / 2$.<br><strong>Non-Existence of Electron in Nucleus:</strong> For nuclear confinement ($\Delta x \approx 2\times 10^{-14}\text{ m}$), $E_k \ge 5\text{ to } 20\text{ MeV}$, far exceeding observed beta decay energies ($<4\text{ MeV}$)."
    },
    "phy-q12": {
        "eq": r"$$P(x,t) = |\psi(x,t)|^2 = \psi^* \psi, \quad \int_{-\infty}^{+\infty} |\psi(x,t)|^2 dx = 1$$",
        "text": r"<strong>Physical Meaning:</strong> Wavefunction $\psi$ is complex and unobservable; $|\psi|^2$ represents position probability density.<br><strong>Acceptable Wavefunction Criteria:</strong> Must be finite, single-valued, and continuous everywhere with a continuous first spatial derivative.<br><strong>Normalization:</strong> Total probability across all space must equal 1."
    },
    "phy-q13": {
        "eq": r"$$i\hbar \frac{\partial \Psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2} + V(x)\Psi, \quad \frac{d^2 \psi}{dx^2} + \frac{2m}{\hbar^2}(E - V)\psi = 0$$",
        "text": r"<strong>Quantum Operators:</strong> Momentum operator $\hat{p} = -i\hbar \frac{\partial}{\partial x}$, Energy operator $\hat{E} = i\hbar \frac{\partial}{\partial t}$.<br><strong>Time-Dependent:</strong> Governs non-stationary states: $\hat{H}\Psi = i\hbar \frac{\partial \Psi}{\partial t}$.<br><strong>Time-Independent:</strong> Eigenvalue equation $\hat{H}\psi = E\psi$ for conservative stationary states ($V = V(x)$)."
    },
    "phy-q14": {
        "eq": r"$$E_n = \frac{n^2 h^2}{8m L^2}, \quad \psi_n(x) = \sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right), \quad n = 1, 2, 3, \dots$$",
        "text": r"<strong>Boundary Conditions:</strong> $\psi(0) = 0$ and $\psi(L) = 0$, giving quantized wave vector $k_n = n\pi / L$.<br><strong>Energy Quantization:</strong> $E_n \propto n^2$.<br><strong>Zero-Point Energy:</strong> $E_1 = \frac{h^2}{8mL^2} \neq 0$ (quantum mechanical requirement of uncertainty principle).<br><strong>Eigenfunctions:</strong> Normalization constant is $\sqrt{2/L}$."
    },
    "phy-q15": {
        "eq": r"$$E_g(d) = E_{g,bulk} + \frac{h^2}{8\mu d^2} - \frac{1.8 e^2}{4\pi\epsilon d}, \quad \text{DOS: } 0D \to \delta(E), \; 1D \to E^{-1/2}, \; 2D \to \text{Step}$$",
        "text": r"<strong>Quantum Confinement:</strong> Spatial dimensions $\le 100\text{ nm}$ comparable to exciton Bohr radius widen effective bandgap ($E_g \propto 1/d^2$).<br><strong>Dimensionality:</strong> 0D (Quantum Dots, 3 confined axes), 1D (Nanowires, 2 confined axes), 2D (Quantum Wells, 1 confined axis).<br><strong>Synthesis:</strong> Sol-Gel (hydrolysis $\to$ condensation $\to$ sol $\to$ gel $\to$ sintering) and CVD (gaseous precursors cracking on heated catalytic substrate)."
    },
    "phy-q16": {
        "eq": r"$$f = \frac{p}{2 t} \sqrt{\frac{Y}{\rho}}, \quad f_1 = \frac{1}{2 t}\sqrt{\frac{Y}{\rho}}$$",
        "text": r"<strong>Converse Piezoelectric Effect:</strong> Applying alternating high-frequency voltage across electrical faces induces mechanical vibrations along mechanical faces.<br><strong>Crystal Cut:</strong> $X$-cut quartz vibrates in thickness mode.<br><strong>Resonance Condition:</strong> $LC$ oscillator tuned to quartz natural frequency.<br><strong>Frequency:</strong> $f \propto 1/t$ ($1\text{ mm}$ quartz $\implies \approx 2.73\text{ MHz}$)."
    },
    "phy-q17": {
        "eq": r"$$f = \frac{1}{2 l} \sqrt{\frac{Y}{\rho}}, \quad \text{Operating Range: } 20\text{ kHz to } 100\text{ kHz}$$",
        "text": r"<strong>Magnetostrictive Joule Effect:</strong> Ferromagnetic rod changes length in longitudinal magnetic field regardless of field sign.<br><strong>DC Polarizing Field:</strong> Required to eliminate frequency doubling ($2f \to f$).<br><strong>Resonance:</strong> Midpoint clamping produces central node and terminal antinodes.<br><strong>Limitation:</strong> Upper frequency limited to $<300\text{ kHz}$ by eddy current and hysteresis losses."
    },
    "phy-q18": {
        "eq": r"$$d = \frac{v \cdot t_f}{2}, \quad T = \frac{v \cdot t_b}{2}, \quad R = \left(\frac{Z_2 - Z_1}{Z_2 + Z_1}\right)^2$$",
        "text": r"<strong>Acoustic Impedance Mismatch:</strong> $Z = \rho v$; air crack interface in metal reflects almost $100\%$ ($R \approx 1.0$).<br><strong>A-Scan Display:</strong> Displays Initial Pulse ($P_0$), Flaw Echo ($P_f$), and Back-Wall Echo ($P_b$).<br><strong>Flaw Depth:</strong> $d = \frac{v t_f}{2} = (\frac{t_f}{t_b})T$."
    },
    "phy-q19": {
        "eq": r"$$T = \frac{0.161 V}{A} = \frac{0.161 V}{\sum a_i S_i}$$",
        "text": r"<strong>Reverberation Time ($T$):</strong> Time for acoustic energy density to drop by $60\text{ dB}$ ($10^{-6}$ of steady-state value).<br><strong>Absorption Unit:</strong> Sabin / Open Window Unit (OWU).<br><strong>Energy Balance:</strong> $V \frac{d\rho}{dt} = P - \frac{c A \rho}{4}$, leading to decay $\rho(t) = \rho_0 e^{-\frac{c A t}{4V}}$. Setting $\rho / \rho_0 = 10^{-6}$ yields $T \approx \frac{0.161 V}{A}$."
    },
    "phy-q20": {
        "eq": r"$$T_{\text{opt}} \approx 0.8\text{ to } 1.2\text{ s (Speech)}, \quad 1.5\text{ to } 2.2\text{ s (Music)}, \quad \text{Echo Threshold: } \Delta t > 0.05\text{ s}$$",
        "text": r"<strong>Acoustic Defects & Remedies:</strong><br>1. <strong>Excess Reverberation:</strong> Deploy acoustic absorbent panels/curtains.<br>2. <strong>Echoes:</strong> Tilt/splay rear walls, add absorbent cladding.<br>3. <strong>Flutter Echoes:</strong> Splay parallel walls by $5-8^\circ$ or install convex acoustic diffusers.<br>4. <strong>Sound Focusing:</strong> Eliminate concave domes; install convex reflective baffles.<br>5. <strong>Resonance Modes:</strong> Avoid integer room ratios; use Golden proportions."
    },
    "phy-q21": {
        "eq": r"$$B_{12} = B_{21}, \quad \frac{A_{21}}{B_{21}} = \frac{8\pi h \nu^3}{c^3}, \quad \frac{R_{sp}}{R_{stim}} = e^{h\nu / k_B T} - 1$$",
        "text": r"<strong>Einstein's Relations:</strong> Equating transition balance to Planck's radiation law proves $B_{12} = B_{21}$ and $A_{21}/B_{21} = 8\pi h\nu^3 / c^3$.<br><strong>Frequency Dependence:</strong> Spontaneous emission scales with $\nu^3$, dominating in the optical spectrum under thermal equilibrium.<br><strong>Laser Condition:</strong> Population inversion ($N_2 > N_1$) is mandatory for stimulated emission to outpace absorption."
    },
    "phy-q22": {
        "eq": r"$$\lambda = 694.3\text{ nm (Pulsed Red)}, \quad \text{Active Medium: } Al_2O_3 : Cr^{3+} (0.05\%)$$",
        "text": r"<strong>3-Level Laser System:</strong> Ground state $^4A_2$ ($E_1$), pump bands $^4F_1, ^4F_2$ ($E_3$), metastable state $^2E$ ($E_2$, lifetime $\approx 3\text{ ms}$).<br><strong>Pumping:</strong> Xenon helical flash lamp ($550\text{ nm}$ green band).<br><strong>Fast Decay:</strong> $E_3 \to E_2$ non-radiative phonon decay.<br><strong>Drawback:</strong> High threshold pumping power since $>50\%$ of all ground atoms must be excited for inversion."
    },
    "phy-q23": {
        "eq": r"$$\lambda = 632.8\text{ nm (Continuous Wave Red)}, \quad \text{He : Ne Ratio} = 10 : 1$$",
        "text": r"<strong>4-Level Gas Laser:</strong> Continuous wave (CW) operation.<br><strong>Pumping:</strong> Electric discharge excites He atoms to metastable $2^1S_0$ ($20.61\text{ eV}$) and $2^3S_1$ ($19.82\text{ eV}$).<br><strong>Resonant Collisions:</strong> Transfer energy to Ne $3s$ ($20.66\text{ eV}$) and $2s$ ($19.78\text{ eV}$) levels.<br><strong>Laser Transition:</strong> Ne $3s \to 2p$ ($632.8\text{ nm}$). Narrow bore ($2-4\text{ mm}$) ensures wall-collision de-excitation."
    },
    "phy-q24": {
        "eq": r"$$\lambda \approx \frac{1.24}{E_g\text{ (in eV)}}\ \mu\text{m}, \quad (E_{Fn} - E_{Fp}) > h\nu > E_g, \quad \text{GaAs: } \lambda \approx 873\text{ nm}$$",
        "text": r"<strong>Direct Bandgap Requirement:</strong> Direct electron-hole recombination conserves crystal momentum ($k = 0$).<br><strong>Degenerate Doping:</strong> Heavy $p^{++}$ and $n^{++}$ doping shifts Fermi levels into valence/conduction bands.<br><strong>Population Inversion:</strong> Forward bias injects high-density minority carriers into active depletion layer.<br><strong>Cavity:</strong> Cleaved natural $(110)$ crystal facets provide $\approx 32\%$ Fresnel reflection."
    },
    "phy-q25": {
        "eq": r"$$\theta_a = \sin^{-1}\left(\sqrt{n_1^2 - n_2^2}\right), \quad NA = \sin\theta_a = \sqrt{n_1^2 - n_2^2} \approx n_1 \sqrt{2\Delta}$$",
        "text": r"<strong>Total Internal Reflection (TIR):</strong> Requires $n_1 > n_2$ and incidence angle $\phi \ge \phi_c = \sin^{-1}(n_2/n_1)$.<br><strong>Acceptance Angle ($\theta_a$):</strong> Maximum semi-cone launch angle for TIR: $\sin\theta_a = \sqrt{n_1^2 - n_2^2}$.<br><strong>Numerical Aperture ($NA$):</strong> Light-collecting capacity: $NA = n_1 \sqrt{2\Delta}$, where $\Delta = (n_1 - n_2)/n_1$."
    },
    "phy-q26": {
        "eq": r"$$V = \frac{2\pi a}{\lambda}\sqrt{n_1^2 - n_2^2} \le 2.405\text{ (Single Mode)}, \quad \alpha = \frac{10}{L}\log_{10}\left(\frac{P_{in}}{P_{out}}\right), \quad \alpha_{\text{Rayleigh}} \propto \frac{1}{\lambda^4}$$",
        "text": r"<strong>Index Profiles:</strong> Step-Index (abrupt step) vs Graded-Index (parabolic profile, minimizes intermodal dispersion).<br><strong>Modes:</strong> Single-Mode ($V \le 2.405$, $8-10\ \mu\text{m}$ core, zero intermodal dispersion) vs Multimode ($V > 2.405$, $50-62.5\ \mu\text{m}$ core).<br><strong>Losses:</strong> Absorption (UV electronic, IR lattice, $OH^-$ peaks at $1.38\ \mu\text{m}$), Rayleigh scattering ($\propto 1/\lambda^4$), and bending losses (macrobending & microbending)."
    }
}

PHYSICS_EXAM_QUESTIONS = {
    "phy-q1": "Derive the differential equation of damped harmonic oscillations. Obtain the general solution and discuss the three cases of damping: overdamped, critically damped, and underdamped.",
    "phy-q2": "Derive the differential equation for forced harmonic oscillations. Obtain the expressions for the steady-state amplitude and phase difference, and discuss their variation with driving frequency.",
    "phy-q3": "Explain the phenomenon of amplitude resonance in forced oscillations. Derive expressions for resonant frequency, sharpness of resonance, Quality factor, and logarithmic decrement.",
    "phy-q4": "Derive the one-dimensional differential wave equation for the propagation of transverse waves on a stretched flexible string from fundamental principles.",
    "phy-q5": "Apply rigid boundary conditions to obtain the standing wave modes and quantized natural frequencies of transverse vibrations on a stretched string fixed at both ends. State Mersenne's laws.",
    "phy-q6": "Derive the expression for the optical path difference between reflected rays in a thin parallel transparent film. Deduce the conditions for constructive and destructive interference, and explain why an extremely thin film appears dark.",
    "phy-q7": "Explain the formation of interference fringes in an air wedge. Derive the expression for fringe width and explain how the diameter of a thin wire is measured experimentally.",
    "phy-q8": "Explain the theory of Newton's rings in reflected light. Derive expressions for the diameters of dark and bright rings, and explain how the wavelength of sodium light and the refractive index of a liquid are determined.",
    "phy-q9": "Derive the expression for the intensity distribution in Fraunhofer diffraction at a single slit. Obtain the conditions for central maximum, secondary maxima, and diffraction minima, and deduce the angular width of the central maximum.",
    "phy-q10": "State and prove the plane transmission diffraction grating equation. Derive expressions for the maximum observable order of spectra, dispersive power, and resolving power of the grating based on Rayleigh's criterion.",
    "phy-q11": "State de Broglie hypothesis and derive expressions for de Broglie wavelength for a particle of energy E and an electron accelerated through potential V. State Heisenberg's uncertainty principle and prove that free electrons cannot exist inside an atomic nucleus.",
    "phy-q12": "Explain the physical significance of the wave function psi. Discuss Born's statistical interpretation, the normalization condition, and the necessary mathematical criteria for an acceptable wave function.",
    "phy-q13": "Derive both the one-dimensional Time-Dependent and Time-Independent Schrödinger wave equations for a particle moving in a conservative potential field.",
    "phy-q14": "Solve the one-dimensional time-independent Schrödinger equation for a particle trapped in an infinite potential well of width L. Derive expressions for the quantized energy eigenvalues, zero-point energy, and normalized wave functions.",
    "phy-q15": "Explain the quantum confinement effect in nanomaterials. Classify nanomaterials as 0D, 1D, and 2D with examples. Describe the synthesis of nanomaterials using the Sol-Gel technique and Chemical Vapor Deposition (CVD).",
    "phy-q16": "Explain the piezoelectric method of generating ultrasonic waves with a neat circuit diagram. State the converse piezoelectric effect and derive the formula for the resonant frequency of a vibrating quartz crystal plate.",
    "phy-q17": "Explain the principle, circuit diagram, and working of a magnetostriction ultrasonic generator. Derive the expression for the resonant frequency of the ferromagnetic rod and state its operating frequency limits.",
    "phy-q18": "Explain the principle and working of Ultrasonic Non-Destructive Testing (NDT) using the pulse-echo method. Draw a typical A-scan display and derive the formula for determining the depth of an internal flaw.",
    "phy-q19": "Define reverberation and reverberation time. State and derive Sabine's formula for the reverberation time of an auditorium based on the growth and decay of acoustic energy density.",
    "phy-q20": "Discuss the essential architectural acoustic requirements of an auditorium. Explain common acoustic defects such as echoes, flutter echoes, sound focusing, and resonance, along with their engineering remedies.",
    "phy-q21": "Explain the three radiation-matter interaction processes. Derive the relations between Einstein's A and B coefficients, and explain why population inversion is necessary for laser action.",
    "phy-q22": "Describe the construction and working of a Ruby laser with a neat schematic and three-level energy band diagram. Explain why ruby lasers operate in pulsed mode.",
    "phy-q23": "Explain the construction and four-level working of a Helium-Neon (He-Ne) gas laser with an energy level diagram. Explain the mechanism of resonant collision energy transfer and continuous-wave emission at 632.8 nm.",
    "phy-q24": "Explain the working principle of a semiconductor diode laser (GaAs). Explain how population inversion is achieved across a degenerately doped p-n junction under forward bias and how the optical cavity is formed.",
    "phy-q25": "Explain the principle of light propagation in an optical fiber by total internal reflection. Derive expressions for the acceptance angle and Numerical Aperture of a step-index optical fiber.",
    "phy-q26": "Classify optical fibers based on refractive index profile and mode of propagation. Explain the fundamental attenuation mechanisms in optical fibers: absorption, Rayleigh scattering, and bending losses."
}
