# -*- coding: utf-8 -*-
"""
Module 2 for Basics of Electrical & Electronics Engineering (EST130 / BEEE)
AC Fundamentals & Magnetic Circuits
KTU 2019 Scheme Electrical & Electronics Engineering
"""

MODULE_2 = {
    "module_id": "beee-m2",
    "module_num": "Module 2",
    "module_title": "AC Fundamentals & Magnetic Circuits",
    "questions": [
        {
            "qid": "beee-q6",
            "marks": 5,
            "type": "Short Answer",
            "title": "Generation of Sinusoidal AC Voltage, Fundamental Terminology, and Phasor Representation",
            "yt_query": "generation sinusoidal ac voltage ac fundamentals phasor representation",
            "img_path": "images/beee/ac_sine_generation_phasor.png",
            "img_caption": "Figure 2.1: Coil Rotating in Magnetic Field Generating Sinusoidal EMF and Phasor Projection",
            "answer": r"""
Sinusoidal alternating voltage is generated fundamentally on the principle of Faraday's law of electromagnetic induction. When a planar rectangular conductor loop of $N$ turns and cross-sectional area $A$ rotates at a uniform angular velocity $\omega$ radians per second within a uniform, stationary magnetic field of flux density $B$ Teslas, the magnetic flux linkage through the coil varies continuously as a function of time.

At any instant of time $t$, let $\theta = \omega t$ denote the angle between the normal vector to the coil plane and the magnetic field vector. The instantaneous magnetic flux linked with the coil is:
$$\Phi(t) = B \cdot A \cos(\omega t)$$
According to Faraday's law, the electromotive force (EMF) induced across the coil terminals is equal to the negative rate of change of magnetic flux linkages:
$$e(t) = -N \frac{d\Phi}{dt} = -N \frac{d}{dt}\left[ B A \cos(\omega t) \right] = N B A \omega \sin(\omega t)$$
Defining the peak or maximum induced voltage as $V_m = N B A \omega$, the standard mathematical equation for an alternating sinusoidal voltage is:
$$v(t) = V_m \sin(\omega t)$$

The fundamental parameters governing this alternating waveform are defined as follows:
1. Instantaneous Value ($v$ or $i$): The magnitude of voltage or current measured at any specific time instant $t$, expressed as $v(t) = V_m \sin(\omega t \pm \phi)$.
2. Amplitude / Peak Value ($V_m$ or $I_m$): The maximum instantaneous value attained by the waveform during either the positive or negative half-cycle. The total excursion between positive and negative peaks is the Peak-to-Peak value ($V_{p-p} = 2 V_m$).
3. Cycle: One complete sequence of positive and negative variations of the alternating quantity, repeated continuously at uniform intervals.
4. Time Period ($T$): The duration in seconds required by the waveform to complete one full cycle. In terms of angular velocity:
$$T = \frac{2\pi}{\omega}\text{ seconds}$$
5. Frequency ($f$): The number of complete cycles executed per second, measured in Hertz ($\text{Hz}$):
$$f = \frac{1}{T} = \frac{\omega}{2\pi} \iff \omega = 2\pi f\text{ rad/s}$$
6. Phase and Phase Difference: Phase defines the fractional part of a period that has elapsed relative to an arbitrary reference origin, expressed as an angle $\phi$. If two sinusoidal quantities of the same frequency are given by $v_1(t) = V_{m1}\sin(\omega t)$ and $v_2(t) = V_{m2}\sin(\omega t - \phi)$, $v_2$ is said to lag $v_1$ by phase angle $\phi$ (or $v_1$ leads $v_2$ by $\phi$).

Phasor Representation:
Because analyzing sinusoidal waveforms in the time domain involves cumbersome trigonometric identities, alternating quantities are represented in electrical engineering by Phasors. A phasor is a directed line segment (vector) of length proportional to the RMS value (or peak value) of the sinusoidal wave, rotating counterclockwise in the complex plane at angular frequency $\omega$. The vertical projection of this rotating vector onto the imaginary axis at any instant $t$ precisely reproduces the instantaneous value $V_m \sin(\omega t + \phi)$. In complex notation, a sinusoidal voltage $v(t) = V_m \sin(\omega t + \phi)$ is expressed in polar form as $\mathbf{V} = V_{\text{rms}} \angle \phi$ or in rectangular form as $\mathbf{V} = V_{\text{rms}}(\cos\phi + j\sin\phi)$, enabling AC network analysis via basic complex algebra.
"""
        },
        {
            "qid": "beee-q7",
            "marks": 7,
            "type": "Long Derivation",
            "title": "Mathematical Derivation of RMS and Average Values, Form Factor, and Peak Factor",
            "yt_query": "rms value average value form factor peak factor sine wave derivation",
            "img_path": "images/beee/rms_average_derivation.png",
            "img_caption": "Figure 2.2: Symmetrical Sine Wave Showing Half-Cycle Average and Effective Heating RMS Level",
            "answer": r"""
The quantitative assessment of alternating voltages and currents requires standard scalar metrics that relate time-varying quantities to equivalent steady DC levels.

1. Average Value ($V_{avg}$):
The average value of an alternating quantity over a time interval $T$ is the arithmetic mean of all instantaneous values over that period:
$$V_{avg} = \frac{1}{T} \int_{0}^{T} v(t)\,dt$$
For a symmetrical sinusoidal waveform $v(t) = V_m \sin\theta$ (where $\theta = \omega t$), the positive and negative half-cycles are identical in shape but opposite in sign. Integrating over a full period ($0$ to $2\pi$) yields identically zero. Therefore, by international convention, the average value of a symmetrical AC wave is evaluated strictly over one half-cycle ($0$ to $\pi$):
$$V_{avg} = \frac{1}{\pi} \int_{0}^{\pi} V_m \sin\theta\,d\theta = \frac{V_m}{\pi} \left[ -\cos\theta \right]_0^\pi$$
Evaluating the limits:
$$V_{avg} = \frac{V_m}{\pi} \left[ -\cos(\pi) - (-\cos(0)) \right] = \frac{V_m}{\pi} \left[ -(-1) - (-1) \right] = \frac{V_m}{\pi} [1 + 1] = \frac{2 V_m}{\pi}$$
Substituting $\pi \approx 3.14159$:
$$V_{avg} = \frac{2}{\pi} V_m \approx 0.6366 V_m$$

2. Root Mean Square (RMS) / Effective Value ($V_{rms}$):
The RMS or effective value of an alternating current is defined on the basis of heating effect (Joule's law): it is that steady direct current (DC) which, when flowing through a given resistance for a specified time, produces exactly the same amount of heat energy as produced by the alternating current flowing through the same resistance for the same duration.
Heat produced by an instantaneous current $i(t)$ in resistance $R$ over an infinitesimal duration $dt$ is $dH = i^2(t) R dt$. Over one full cycle of period $T$:
$$H_{AC} = \int_{0}^{T} i^2(t) R\,dt$$
The heat produced by an equivalent direct current $I_{rms}$ over the same period is:
$$H_{DC} = I_{rms}^2 R T$$
Equating both expressions:
$$I_{rms}^2 R T = R \int_{0}^{T} i^2(t)\,dt \implies I_{rms} = \sqrt{\frac{1}{T}\int_{0}^{T} i^2(t)\,dt}$$
Applying this definition to a sinusoidal voltage $v(\theta) = V_m \sin\theta$ over period $T = 2\pi$:
$$V_{rms}^2 = \frac{1}{2\pi} \int_{0}^{2\pi} V_m^2 \sin^2\theta\,d\theta$$
Using the trigonometric identity $\sin^2\theta = \frac{1 - \cos(2\theta)}{2}$:
$$V_{rms}^2 = \frac{V_m^2}{2\pi} \int_{0}^{2\pi} \frac{1 - \cos(2\theta)}{2}\,d\theta = \frac{V_m^2}{4\pi} \left[ \int_{0}^{2\pi} 1\,d\theta - \int_{0}^{2\pi} \cos(2\theta)\,d\theta \right]$$
The integral of $\cos(2\theta)$ over its full period of $2\pi$ is zero:
$$V_{rms}^2 = \frac{V_m^2}{4\pi} \left[ \theta \right]_0^{2\pi} - 0 = \frac{V_m^2}{4\pi} [2\pi - 0] = \frac{V_m^2}{4\pi} \cdot 2\pi = \frac{V_m^2}{2}$$
Taking the square root:
$$V_{rms} = \sqrt{\frac{V_m^2}{2}} = \frac{V_m}{\sqrt{2}} \approx 0.7071 V_m$$

3. Form Factor ($K_f$):
The form factor is defined as the mathematical ratio of the RMS value to the half-cycle average value of the alternating waveform:
$$K_f = \frac{V_{rms}}{V_{avg}} = \frac{\frac{V_m}{\sqrt{2}}}{\frac{2 V_m}{\pi}} = \frac{\pi}{2\sqrt{2}} = \frac{3.14159}{2 \times 1.4142} = \frac{3.14159}{2.8284} \approx 1.11$$
The value $1.11$ is the universal form factor for pure sinusoidal waves, appearing prominently in transformer EMF equations.

4. Peak Factor / Crest Factor ($K_p$):
The peak factor is defined as the ratio of the peak (maximum) value to the RMS value:
$$K_p = \frac{V_m}{V_{rms}} = \frac{V_m}{\frac{V_m}{\sqrt{2}}} = \sqrt{2} \approx 1.414$$
The peak factor is vital for insulation design, specifying the dielectric breakdown voltage required to withstand peak stresses for a given nominal RMS operating voltage.
"""
        },
        {
            "qid": "beee-q8",
            "marks": 7,
            "type": "Numerical Problem",
            "title": "Analysis of Series R-L and R-C Circuits: Impedance Triangle, Power Factor, and Power Triangles",
            "yt_query": "series rl circuit rc circuit impedance triangle power factor active reactive apparent power",
            "img_path": "images/beee/rl_rc_impedance_power_triangle.png",
            "img_caption": "Figure 2.3: Phasor Diagrams, Impedance Triangles, and Complex Power Triangles for R-L and R-C Circuits",
            "answer": r"""
When linear passive elements are excited by a steady-state sinusoidal voltage $v(t) = V_m \sin(\omega t)$, their dynamic responses depend on the nature of their energy storage mechanisms.

In a Series R-L Circuit comprising a resistor $R$ and inductor $L$ carrying common loop current $i(t) = I_m \sin(\omega t)$:
The voltage across the resistor is in phase with the current: $\mathbf{V}_R = I R \angle 0^\circ$.
The voltage across the ideal inductor leads the current by $90^\circ$ due to Lenz's law: $\mathbf{V}_L = I X_L \angle 90^\circ = j I X_L$, where inductive reactance is $X_L = \omega L = 2\pi f L\,\Omega$.
By Kirchhoff's voltage law, the total supply phasor voltage is:
$$\mathbf{V} = \mathbf{V}_R + \mathbf{V}_L = I R + j I X_L = I (R + j X_L) = I \mathbf{Z}$$
The complex impedance is $\mathbf{Z} = R + j X_L$, with magnitude and phase angle:
$$|\mathbf{Z}| = \sqrt{R^2 + X_L^2}, \quad \phi = \tan^{-1}\left( \frac{X_L}{R} \right)$$
Because $\mathbf{V}$ leads $\mathbf{I}$ by $\phi$, the current lags the supply voltage by phase angle $\phi$.

In a Series R-C Circuit comprising a resistor $R$ and capacitor $C$:
The capacitive reactance is $X_C = \frac{1}{\omega C} = \frac{1}{2\pi f C}\,\Omega$.
The voltage across the capacitor lags the current by $90^\circ$: $\mathbf{V}_C = -j I X_C = I X_C \angle -90^\circ$.
The supply voltage is:
$$\mathbf{V} = \mathbf{V}_R + \mathbf{V}_C = I(R - j X_C) = I \mathbf{Z}$$
The complex impedance is $\mathbf{Z} = R - j X_C$, with magnitude $|\mathbf{Z}| = \sqrt{R^2 + X_C^2}$ and phase angle $\phi = -\tan^{-1}\left( \frac{X_C}{R} \right)$.
In an R-C circuit, current leads the supply voltage by phase angle $|\phi|$.

Power Definitions and Power Triangle:
1. Real / Active Power ($P$): The net rate of usable energy consumed by the resistive element, measured in Watts ($\text{W}$):
$$P = V_{rms} I_{rms} \cos\phi = I_{rms}^2 R$$
2. Reactive Power ($Q$): The peak rate of energy oscillating back and forth between the magnetic/electric fields and the source, doing no net work, measured in Volt-Amperes Reactive ($\text{VAR}$):
$$Q = V_{rms} I_{rms} \sin\phi = I_{rms}^2 X$$
3. Apparent Power ($S$): The total complex power capacity supplied by the source, measured in Volt-Amperes ($\text{VA}$):
$$S = V_{rms} I_{rms} = \sqrt{P^2 + Q^2}$$
4. Power Factor ($pf$): The cosine of the phase angle between voltage and current:
$$pf = \cos\phi = \frac{P}{S} = \frac{R}{|\mathbf{Z}|}$$
Power factor is lagging for inductive circuits and leading for capacitive circuits.

Complete Worked Numerical Problem:
A non-inductive resistor $R = 30\,\Omega$ is connected in series with an inductive coil of inductance $L = 0.1273\text{ H}$ across a $230\text{ V}, 50\text{ Hz}$ single-phase AC supply.
Calculate: (i) Inductive reactance, (ii) Total circuit impedance, (iii) RMS current, (iv) Power factor, (v) Active power, (vi) Reactive power, and (vii) Apparent power.

Step 1: Inductive reactance:
$$X_L = 2\pi f L = 2 \times 3.14159 \times 50 \times 0.1273 = 100 \times 3.14159 \times 0.1273 = 40.0\,\Omega$$

Step 2: Total impedance:
$$\mathbf{Z} = R + j X_L = 30 + j 40\,\Omega$$
$$|\mathbf{Z}| = \sqrt{R^2 + X_L^2} = \sqrt{30^2 + 40^2} = \sqrt{900 + 1600} = \sqrt{2500} = 50.0\,\Omega$$
$$\phi = \tan^{-1}\left( \frac{X_L}{R} \right) = \tan^{-1}\left( \frac{40}{30} \right) = \tan^{-1}(1.333) \approx 53.13^\circ$$

Step 3: RMS circuit current:
$$I = \frac{V}{|\mathbf{Z}|} = \frac{230}{50} = 4.60\text{ A}$$

Step 4: Power factor:
$$pf = \cos\phi = \cos(53.13^\circ) = \frac{R}{|\mathbf{Z}|} = \frac{30}{50} = 0.60\text{ lagging}$$

Step 5: Active power dissipated:
$$P = V I \cos\phi = 230 \times 4.60 \times 0.60 = 634.8\text{ W}$$
Alternatively: $P = I^2 R = (4.60)^2 \times 30 = 21.16 \times 30 = 634.8\text{ W}$.

Step 6: Reactive power:
$$\sin\phi = \sin(53.13^\circ) = 0.80$$
$$Q = V I \sin\phi = 230 \times 4.60 \times 0.80 = 846.4\text{ VAR}$$

Step 7: Apparent power:
$$S = V I = 230 \times 4.60 = 1058.0\text{ VA}$$
Verification: $\sqrt{P^2 + Q^2} = \sqrt{634.8^2 + 846.4^2} = \sqrt{402971 + 716393} = \sqrt{1119364} = 1058.0\text{ VA}$.
"""
        },
        {
            "qid": "beee-q9",
            "marks": 7,
            "type": "Long Derivation",
            "title": "Series Resonance in RLC Circuit: Resonant Frequency, Quality Factor, and Bandwidth Derivation",
            "yt_query": "series resonance rlc circuit resonant frequency quality factor bandwidth derivation",
            "img_path": "images/beee/series_resonance_curves.png",
            "img_caption": "Figure 2.4: Resonance Characteristics Showing Impedance Minimum, Current Peak, and Half-Power Bandwidth",
            "answer": r"""
A series R-L-C circuit consists of a resistor $R$, an inductor $L$, and a capacitor $C$ connected in series across an alternating sinusoidal voltage source $\mathbf{V} = V \angle 0^\circ$.
The total complex impedance of the circuit as a function of angular frequency $\omega$ is:
$$\mathbf{Z}(\omega) = R + j\left( \omega L - \frac{1}{\omega C} \right) = R + j X_{net}$$
The net reactance of the circuit is $X_{net} = X_L - X_C = \omega L - \frac{1}{\omega C}$.

Condition for Series Resonance:
Electrical resonance occurs when the supply frequency is tuned such that the inductive reactance exactly balances and cancels the capacitive reactance:
$$X_L = X_C \implies \omega L = \frac{1}{\omega C}$$
At this specific frequency, denoted as the resonant angular frequency $\omega_r$:
$$\omega_r^2 = \frac{1}{L C} \implies \omega_r = \frac{1}{\sqrt{L C}}\text{ rad/s}$$
The resonant frequency in Hertz ($f_r$) is:
$$f_r = \frac{\omega_r}{2\pi} = \frac{1}{2\pi\sqrt{L C}}\text{ Hz}$$

Salient Characteristics at Series Resonance:
1. Minimum Impedance: The net reactive component vanishes ($X_{net} = 0$). The circuit impedance is purely resistive and reaches its absolute minimum:
$$\mathbf{Z}_r = R + j 0 = R$$
2. Maximum Current: Because impedance is minimal, the loop current reaches its maximum possible amplitude and is strictly in phase with the supply voltage:
$$\mathbf{I}_{0} = \frac{\mathbf{V}}{R} \angle 0^\circ$$
3. Unity Power Factor: The phase angle is $\phi = 0^\circ$, meaning the power factor is $\cos(0^\circ) = 1.0$.
4. Voltage Magnification: While the net reactive voltage is zero ($\mathbf{V}_L + \mathbf{V}_C = 0$), the individual voltages across the inductor and capacitor can be enormously higher than the supply voltage:
$$V_L = I_0 X_L = \left(\frac{V}{R}\right) \omega_r L = Q \cdot V$$
$$V_C = I_0 X_C = \left(\frac{V}{R}\right) \frac{1}{\omega_r C} = Q \cdot V$$
where $Q$ is the circuit Quality Factor. For this reason, series resonance is also termed Voltage Resonance.

Quality Factor ($Q$-Factor):
The Quality Factor ($Q$) quantifies the sharpness of resonance and frequency selectivity. It is defined fundamentally as $2\pi$ times the ratio of maximum energy stored in reactive components to the energy dissipated per cycle in the resistance:
$$Q = 2\pi \frac{\text{Maximum Energy Stored}}{\text{Energy Dissipated per Cycle}} = \frac{\omega_r L}{R} = \frac{1}{\omega_r C R}$$
Substituting $\omega_r = \frac{1}{\sqrt{LC}}$:
$$Q = \frac{1}{\sqrt{LC}} \frac{L}{R} = \frac{1}{R} \sqrt{\frac{L}{C}}$$

Half-Power Frequencies and Bandwidth ($BW$):
The half-power frequencies $\omega_1$ (lower cutoff) and $\omega_2$ (upper cutoff) are the operating frequencies at which the circuit current drops to $\frac{1}{\sqrt{2}}$ ($70.7\%$) of its peak resonant value $I_0$, causing power dissipation to drop to exactly half ($P = I^2 R = \frac{1}{2} I_0^2 R$).
At these frequencies:
$$|\mathbf{Z}| = \sqrt{R^2 + X_{net}^2} = \sqrt{2} R \implies R^2 + X_{net}^2 = 2 R^2 \implies X_{net} = \pm R$$
$$\omega L - \frac{1}{\omega C} = \pm R$$
Solving this quadratic equation yields:
$$\omega_1 = -\frac{R}{2L} + \sqrt{\left(\frac{R}{2L}\right)^2 + \frac{1}{LC}}, \quad \omega_2 = +\frac{R}{2L} + \sqrt{\left(\frac{R}{2L}\right)^2 + \frac{1}{LC}}$$
The resonant frequency is the geometric mean of the cutoff frequencies: $\omega_r = \sqrt{\omega_1 \omega_2}$.
The Bandwidth ($BW$ or $\Delta \omega$) is the frequency span between the upper and lower half-power frequencies:
$$\Delta \omega = \omega_2 - \omega_1 = \frac{R}{L}\text{ rad/s}$$
In Hertz:
$$BW = f_2 - f_1 = \frac{R}{2\pi L}\text{ Hz}$$
Dividing both sides by $f_r$:
$$\frac{BW}{f_r} = \frac{R / (2\pi L)}{\omega_r / (2\pi)} = \frac{R}{\omega_r L} = \frac{1}{Q} \implies BW = \frac{f_r}{Q}$$
This fundamental relationship proves that a high-Q circuit possesses a narrow bandwidth and superior selectivity, which is indispensable for tuning radio receivers and filtering out adjacent interfering communication channels.
"""
        },
        {
            "qid": "beee-q10",
            "marks": 7,
            "type": "Short Answer",
            "title": "Magnetic Circuits: Fundamental Quantities, B-H Curve, Electric-Magnetic Analogy, and Series Calculations",
            "yt_query": "magnetic circuits mmf flux reluctance bh curve electric magnetic analogy",
            "img_path": "images/beee/magnetic_circuit_bh_curve.png",
            "img_caption": "Figure 2.5: Magnetic Toroid Circuit, B-H Hysteresis Loop, and Electric-Magnetic Circuit Analogy",
            "answer": r"""
A magnetic circuit is a closed path followed by magnetic flux lines. The behavior of magnetic fields in ferromagnetic media mirrors electric circuits, governed by direct physical analogies.

Fundamental Magnetic Quantities:
1. Magnetomotive Force (MMF, $\mathcal{F}$): The magnetic pressure that drives magnetic flux through a magnetic circuit, generated by an electric current $I$ flowing through an $N$-turn coil:
$$\mathcal{F} = N \cdot I\text{ (measured in Ampere-turns, AT)}$$
2. Magnetic Flux ($\Phi$): The total number of magnetic lines of force passing through a specified cross-sectional area, measured in Webers ($\text{Wb}$).
3. Reluctance ($S$ or $\mathcal{R}$): The opposition offered by the magnetic material to the establishment of magnetic flux:
$$S = \frac{l}{\mu A} = \frac{l}{\mu_0 \mu_r A}\text{ (measured in AT/Wb or H}^{-1}\text{)}$$
where $l$ is the mean length of the magnetic path in meters, $A$ is the cross-sectional area in $\text{m}^2$, $\mu_0 = 4\pi \times 10^{-7}\text{ H/m}$ is the absolute permeability of free space, and $\mu_r$ is the dimensionless relative permeability of the medium.
4. Permeance ($\mathcal{P}$): The reciprocal of reluctance, representing the ease with which flux is established: $\mathcal{P} = \frac{1}{S} = \frac{\mu A}{l}\text{ (Henries, H)}$.
5. Magnetic Flux Density ($B$): Flux per unit perpendicular area: $B = \frac{\Phi}{A}\text{ (Tesla, T or Wb/m}^2\text{)}$.
6. Magnetic Field Intensity ($H$): MMF per unit length along the path: $H = \frac{\mathcal{F}}{l} = \frac{N I}{l}\text{ (AT/m)}$.
The constitutive relationship linking $B$ and $H$ is:
$$B = \mu H = \mu_0 \mu_r H$$

Comparison Between Electric and Magnetic Circuits:
1. Driving Force: In an electric circuit, Electromotive Force (EMF, $V$ in Volts) drives current. In a magnetic circuit, Magnetomotive Force (MMF, $\mathcal{F}$ in AT) establishes flux.
2. Flow/Field Quantity: Current $I = \frac{\text{EMF}}{R}$ (Amperes) represents physical flow of charge carriers. Magnetic flux $\Phi = \frac{\text{MMF}}{S}$ (Webers) represents a state of magnetic stress in the medium; no physical particles flow.
3. Opposition: Resistance $R = \rho \frac{l}{A} = \frac{l}{\sigma A}\,\Omega$. Reluctance $S = \frac{l}{\mu_0 \mu_r A}\text{ AT/Wb}$.
4. Constitutive Laws: Ohm's law $J = \sigma E$. Magnetic law $B = \mu H$.
5. Energy Dissipation: Continuous electrical power $I^2 R$ is dissipated as heat as long as DC current flows. In contrast, once a steady magnetic flux is established in a magnetic circuit, zero energy is required to maintain it (energy is only consumed in the resistance of the exciting coil and during cyclic hysteresis).
6. Linearity: Electrical resistance $R$ of metallic conductors is independent of current density at constant temperature. Conversely, magnetic reluctance $S$ is non-linear because $\mu_r$ depends heavily on flux density $B$ due to magnetic saturation.

The B-H Curve and Magnetic Hysteresis:
When an unmagnetized ferromagnetic core is subjected to increasing magnetic field intensity $H$, the resulting flux density $B$ does not increase linearly. Initially, $B$ rises slowly (domain wall displacement), followed by a steep near-linear increase (domain rotation), and finally saturates at $B_{sat}$ where all magnetic dipoles are fully aligned.
When $H$ is subsequently reduced to zero, the material retains a residual flux density known as Retentivity or Remanence ($B_r$). To reduce the flux density back to zero, a reverse magnetic field intensity must be applied; this opposing field is termed the Coercive Force ($H_c$). Cycled under alternating excitation, the closed $B-H$ trajectory forms a Hysteresis Loop. The area enclosed by the loop represents the hysteresis energy loss per unit volume per cycle, dissipated as heat:
$$W_h = \eta_{Steinmetz} B_{\max}^{1.6} f\text{ W/m}^3$$

Series Magnetic Circuit with Air Gap:
Consider a cast steel ring of mean circumference $l_c = 0.5\text{ m}$, cross-sectional area $A = 0.001\text{ m}^2$, and $\mu_r = 1000$, cut with an air gap of length $l_g = 0.001\text{ m}$ ($1\text{ mm}$). An $N = 500$ turn coil is wound on the ring. Calculate the exciting current $I$ required to establish a flux of $\Phi = 0.001\text{ Wb}$ ($1\text{ mWb}$).
The core flux density is:
$$B = \frac{\Phi}{A} = \frac{0.001}{0.001} = 1.0\text{ T}$$
Reluctance of the iron core:
$$S_{\text{iron}} = \frac{l_c}{\mu_0 \mu_r A} = \frac{0.5}{(4\pi \times 10^{-7}) \times 1000 \times 0.001} = \frac{0.5}{4\pi \times 10^{-7}} = \frac{0.5}{1.2566 \times 10^{-6}} \approx 397,887\text{ AT/Wb}$$
Reluctance of the air gap (neglecting fringing):
$$S_{\text{gap}} = \frac{l_g}{\mu_0 (1) A} = \frac{0.001}{(4\pi \times 10^{-7}) \times 1 \times 0.001} = \frac{1}{4\pi \times 10^{-7}} \approx 795,775\text{ AT/Wb}$$
Total reluctance:
$$S_{total} = S_{\text{iron}} + S_{\text{gap}} = 397,887 + 795,775 = 1,193,662\text{ AT/Wb}$$
Total MMF required:
$$\mathcal{F} = \Phi \cdot S_{total} = 0.001 \times 1,193,662 \approx 1193.66\text{ AT}$$
Exciting current required in the 500-turn coil:
$$I = \frac{\mathcal{F}}{N} = \frac{1193.66}{500} \approx 2.387\text{ A}$$
Notice that the tiny $1\text{ mm}$ air gap contributes roughly two-thirds of the total circuit reluctance, demanding significant exciting current.
"""
        }
    ]
}
