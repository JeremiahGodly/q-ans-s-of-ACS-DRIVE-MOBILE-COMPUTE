# -*- coding: utf-8 -*-
"""
Module 5: Lasers and Optical Communication (phy-q21 to phy-q26)
KTU 2019 Scheme Engineering Physics A (PHT100)
"""

MODULE_5 = {
    "module_id": "phy-m5",
    "module_num": "Module 5",
    "module_title": "Lasers and Fiber Optics",
    "questions": [
        {
            "qid": "phy-q21",
            "marks": 7,
            "type": "Derivation",
            "title": "Einstein's A and B Coefficients: Derivation and Physical Significance",
            "yt_query": "einsteins A and B coefficients derivation relation planck radiation laser physics",
            "img_path": "images/physics/einstein_coefficients.png",
            "img_caption": "Figure 5.1: Three Fundamental Radiation Interaction Mechanisms (Absorption, Spontaneous, and Stimulated Emission)",
            "answer": r"""
The acronym LASER stands for Light Amplification by Stimulated Emission of Radiation. The theoretical foundation of laser operation was established by Albert Einstein in 1917 through his thermodynamic analysis of the interaction between atomic energy states and an ambient electromagnetic radiation field.

Three Fundamental Radiation-Matter Interaction Processes:
Consider an ensemble of identical atoms having two quantized non-degenerate energy levels: lower state $E_1$ with atomic population density $N_1$, and upper state $E_2$ with population density $N_2$. Let the system be immersed in an electromagnetic radiation field of spectral energy density $\rho(\nu)$ at frequency $\nu = \frac{E_2 - E_1}{h}$.

1. Induced (Stimulated) Absorption: An atom in lower state $E_1$ absorbs a photon of energy $h\nu$ from the external field and transitions to higher state $E_2$. The rate of stimulated absorption is directly proportional to the number of atoms in the lower state $N_1$ and the radiation energy density $\rho(\nu)$:
$$R_{abs} = B_{12} N_1 \rho(\nu)$$
where $B_{12}$ is Einstein's coefficient of stimulated absorption.
2. Spontaneous Emission: An atom residing in the excited state $E_2$ decays spontaneously to ground state $E_1$ without external influence, emitting a photon of energy $h\nu$. This decay is entirely random in direction, phase, and polarization. The rate of spontaneous emission depends solely on the population of the upper level $N_2$:
$$R_{sp} = A_{21} N_2$$
where $A_{21}$ is Einstein's coefficient of spontaneous emission.
3. Stimulated (Induced) Emission: An incident photon of energy $h\nu$ interacts with an atom already in excited state $E_2$, triggering it to drop to lower state $E_1$. In doing so, the atom emits a second photon that is identical to the incident photon in frequency, phase, direction of propagation, and polarization state. The rate of stimulated emission is proportional to the excited state population $N_2$ and the ambient radiation density $\rho(\nu)$:
$$R_{stim} = B_{21} N_2 \rho(\nu)$$
where $B_{21}$ is Einstein's coefficient of stimulated emission.

Mathematical Derivation of Einstein's Relations:
In thermodynamic equilibrium at temperature $T$, the rate of upward transitions must equal the rate of downward transitions:
$$R_{abs} = R_{sp} + R_{stim}$$
Substituting the respective rate expressions:
$$B_{12} N_1 \rho(\nu) = A_{21} N_2 + B_{21} N_2 \rho(\nu)$$
Grouping terms involving radiation density $\rho(\nu)$ on the left-hand side:
$$\left[ B_{12} N_1 - B_{21} N_2 \right] \rho(\nu) = A_{21} N_2$$
Dividing by $N_2$:
$$\left[ B_{12} \left(\frac{N_1}{N_2}\right) - B_{21} \right] \rho(\nu) = A_{21}$$
Solving for the radiation energy density $\rho(\nu)$:
$$\rho(\nu) = \frac{A_{21}}{B_{12} \left(\frac{N_1}{N_2}\right) - B_{21}} = \frac{A_{21} / B_{21}}{\left(\frac{B_{12}}{B_{21}}\right)\left(\frac{N_1}{N_2}\right) - 1} \quad \text{--- (Equation 1)}$$

According to the classical Maxwell-Boltzmann statistical distribution, the ratio of equilibrium atomic populations between energy states $E_1$ and $E_2$ at absolute temperature $T$ is:
$$\frac{N_1}{N_2} = \frac{e^{-E_1 / k_B T}}{e^{-E_2 / k_B T}} = e^{(E_2 - E_1) / k_B T} = e^{h\nu / k_B T}$$
where $k_B$ is the Boltzmann constant. Substituting this into Equation 1:
$$\rho(\nu) = \frac{A_{21} / B_{21}}{\left(\frac{B_{12}}{B_{21}}\right) e^{h\nu / k_B T} - 1} \quad \text{--- (Equation 2)}$$

Under thermal equilibrium, the radiation field inside the atomic cavity behaves as an ideal blackbody radiator. Planck's Blackbody Radiation Law gives the spectral energy density as:
$$\rho(\nu) = \frac{8\pi h \nu^3}{c^3} \frac{1}{e^{h\nu / k_B T} - 1} \quad \text{--- (Equation 3)}$$
where $c$ is the velocity of light in vacuum.
Comparing Equation 2 directly with Planck's theoretical formula in Equation 3:
1. Equating the coefficients in the exponential denominator:
$$\frac{B_{12}}{B_{21}} = 1 \implies B_{12} = B_{21}$$
This proves that the probability of stimulated absorption is identical to the probability of stimulated emission for transitions between the same pair of energy levels.
2. Equating the pre-factors:
$$\frac{A_{21}}{B_{21}} = \frac{8\pi h \nu^3}{c^3}$$
These two equalities are known as Einstein's Relations.

Physical Significance of the Ratio:
The ratio of the rate of spontaneous emission to the rate of stimulated emission is:
$$\frac{R_{sp}}{R_{stim}} = \frac{A_{21} N_2}{B_{21} N_2 \rho(\nu)} = \frac{A_{21}}{B_{21} \rho(\nu)} = e^{h\nu / k_B T} - 1$$
1. Strong Frequency Dependence: The ratio $\frac{A_{21}}{B_{21}}$ scales with the cube of frequency ($\nu^3$). At optical frequencies ($\nu \approx 10^{14}\text{ Hz}$), spontaneous emission heavily dominates over stimulated emission under normal thermal equilibrium, explaining why conventional light sources emit incoherent spontaneous light.
2. Achieving Coherent Laser Action: For stimulated emission to dominate and produce net coherent amplification ($R_{stim} > R_{abs}$), we require:
$$B_{21} N_2 \rho(\nu) > B_{12} N_1 \rho(\nu) \implies N_2 > N_1$$
This non-equilibrium condition is known as Population Inversion. Because $E_2 > E_1$, population inversion can never be achieved in thermal equilibrium, requiring an external energy source (optical pumping, electrical discharge) to pump atoms into a metastable upper state.
"""
        },
        {
            "qid": "phy-q22",
            "marks": 7,
            "type": "Theory & Application",
            "title": "Ruby Laser: Construction, Energy Level Diagram, and Working Principle",
            "yt_query": "ruby laser construction working energy level diagram engineering physics",
            "img_path": "images/physics/ruby_laser.png",
            "img_caption": "Figure 5.2: Three-Level Energy Diagram and Schematic of the Pulsed Ruby Laser System",
            "answer": r"""
The ruby laser, demonstrated by Theodore Maiman in 1960, was the world's first functioning optical laser. It is a solid-state three-level laser that emits intense, coherent pulses of deep red light at a wavelength of $\lambda = 694.3\text{ nm}$.

Construction and Structural Components:
The ruby laser consists of three core components:
1. Active Medium (Ruby Crystal Rod): The gain medium is a synthetic crystalline cylindrical rod of corundum or sapphire (aluminum oxide, $Al_2O_3$), in which approximately $0.05\%$ of the $Al^{3+}$ aluminum atoms are replaced by chromium ions ($Cr^{3+}$). These $Cr^{3+}$ dopants give ruby its pinkish-red hue and serve as the active lasing ions. A typical ruby rod is $5\text{ to } 10\text{ cm}$ in length and $0.5\text{ to } 1\text{ cm}$ in diameter.
2. Optical Resonator Cavity: Both flat end faces of the ruby rod are ground and polished optically flat and parallel to within a fraction of a wavelength. One end face is heavily silvered to provide $100\%$ total internal reflection, while the opposite end is partially silvered ($90\%\text{ to } 95\%$ reflectivity) to serve as the output coupler.
3. Optical Pumping System: A helical xenon flash discharge tube surrounds the ruby rod coaxially. The flash lamp is connected to a high-voltage power supply through a capacitor bank. When fired, it emits intense white/green-blue flashes of light of duration $\approx 1\text{ ms}$, delivering high-intensity optical pumping radiation.
4. Cooling System: Because flash pumping generates substantial thermal dissipation, the rod is cooled using circulating liquid nitrogen or forced chilled air to prevent thermal detuning of the laser wavelength.

Three-Level Energy Level Diagram and Working Principle:
The laser operation of $Cr^{3+}$ ions in ruby is described by a three-level quantum system:
1. Ground State ($E_1$): Designated as the $^4A_2$ ground level. Under unpumped thermal equilibrium, almost all $Cr^{3+}$ ions occupy this ground state ($N_1 \approx N_{total}$).
2. Pump Bands ($E_3$): Two broad absorption energy bands: the green band ($^4F_2$ centered around $550\text{ nm}$) and the blue band ($^4F_1$ centered around $410\text{ nm}$).
3. Metastable State ($E_2$): Designated as the $^2E$ doublet state, located approximately $1.79\text{ eV}$ above the ground state.

Operational Sequence:
1. Optical Pumping: When the xenon lamp flashes, it emits green and blue photons matching the energy gaps $E_3 - E_1$. The $Cr^{3+}$ ions absorb this radiation and are elevated from ground state $E_1$ to pump bands $E_3$ via stimulated absorption:
$$Cr^{3+}(E_1) + h\nu_{pump} \longrightarrow Cr^{3+}(E_3)$$
2. Non-Radiative Fast Decay: The lifetime of ions in pump bands $E_3$ is extremely brief (less than $10^{-8}\text{ seconds}$). The excited ions decay rapidly to the intermediate metastable state $E_2$ via non-radiative phonon transitions, dissipating excess energy as crystal lattice vibrations (heat).
3. Population Inversion ($N_2 > N_1$): The metastable state $E_2$ has an exceptionally long spontaneous lifetime of approximately $3\text{ milliseconds}$ ($3 \times 10^{-3}\text{ s}$), which is roughly $10^5$ times longer than the lifetime of level $E_3$. Because ions arrive in level $E_2$ much faster than they decay from it, chromium ions accumulate in level $E_2$. When more than half of the total $Cr^{3+}$ ground-state population has been pumped into $E_2$, population inversion is established between metastable level $E_2$ and ground state $E_1$:
$$N_2 > N_1$$
4. Lasing Action and Optical Amplification: A few $Cr^{3+}$ ions in level $E_2$ eventually decay spontaneously to ground state $E_1$, emitting random photons of wavelength:
$$\lambda = \frac{h c}{E_2 - E_1} = 694.3\text{ nm}$$
Photons that travel parallel to the longitudinal axis of the ruby rod reflect back and forth between the parallel mirrors. As they traverse the inverted ruby crystal, they trigger an avalanche of stimulated emissions, producing millions of identical, phase-locked, in-step photons.
5. Laser Output: When optical gain exceeds internal cavity losses, an intense pulse of monochromatic, highly directional, coherent red laser light exits through the partially silvered mirror.

Inherent Engineering Drawback of Ruby Laser:
Because the lower laser level is the ground state ($E_1$), more than $50\%$ of all atoms in the crystal must be pumped into the excited state just to reach the threshold for population inversion ($N_2 > N_1$). This requires an extremely high pumping energy threshold, making continuous-wave (CW) operation very difficult. Consequently, ruby lasers operate almost exclusively in pulsed mode.
"""
        },
        {
            "qid": "phy-q23",
            "marks": 7,
            "type": "Theory & Application",
            "title": "Helium-Neon (He-Ne) Gas Laser: Construction, Resonant Energy Transfer, and 4-Level Working",
            "yt_query": "helium neon laser construction working energy level diagram 4 level laser engineering physics",
            "img_path": "images/physics/hene_laser.png",
            "img_caption": "Figure 5.3: He-Ne Laser Discharge Tube Construction and Four-Level Resonant Collision Diagram",
            "answer": r"""
The Helium-Neon (He-Ne) laser, developed by Ali Javan, William Bennett, and Donald Herriott at Bell Labs in 1961, was the first gas laser and the first continuous-wave (CW) laser. It operates as a four-level laser system, emitting a continuous, highly stable, monochromatic red beam at a wavelength of $\lambda = 632.8\text{ nm}$.

Construction and Apparatus:
The He-Ne laser system comprises four functional assemblies:
1. Gas Discharge Tube: A long, narrow capillary bore tube made of fused silica or pyrex glass, typically $10\text{ to } 50\text{ cm}$ in length with a narrow internal bore diameter of $2\text{ to } 4\text{ mm}$. The narrow bore is essential to facilitate atom de-excitation via collisions with the tube walls.
2. Active Lasing Gas Mixture: The tube is filled with a mixture of helium (He) and neon (Ne) gas in a typical partial pressure ratio of $10:1$ (roughly $85-90\%$ Helium and $10-15\%$ Neon) at a low total pressure of about $1\text{ Torr}$ ($133\text{ Pa}$). Although neon atoms provide the active lasing transitions, helium atoms are required for the pumping mechanism.
3. Brewster Windows: The ends of the discharge capillary tube are sealed with optical windows oriented at Brewster's angle:
$$\theta_B = \tan^{-1}(n)$$
where $n$ is the refractive index of the window glass. Light polarized parallel to the plane of incidence passes through the windows with zero reflection losses, ensuring that the output laser beam is linearly polarized.
4. Optical Resonator Cavity: Formed by two external dielectric mirrors: one concave mirror with $99.9\%$ reflectivity, and an output coupler mirror with approximately $98-99\%$ reflectivity.
5. Electrical Pumping Supply: An anode and a cathode are sealed into the tube, connected to a high-voltage DC power supply ($1\text{ to } 2\text{ kV}$, with an ignition pulse $> 4\text{ kV}$).

Four-Level Energy Level Diagram and Working Mechanism:
The laser action involves resonant collisional energy transfer between excited helium atoms and ground-state neon atoms.

1. Electrical Discharge Excitation of Helium:
When high voltage is applied across the electrodes, electrons accelerated by the electric field collide inelastically with ground-state helium atoms ($1^1S_0$), exciting them to two long-lived metastable states:
$$e^- + \text{He}(1^1S_0) \longrightarrow \text{He}^*(2^3S_1) + e^- \quad (\text{Energy } = 19.82\text{ eV})$$
$$e^- + \text{He}(1^1S_0) \longrightarrow \text{He}^*(2^1S_0) + e^- \quad (\text{Energy } = 20.61\text{ eV})$$
Direct radiative transition from these levels back to the helium ground state is forbidden by quantum selection rules, causing excited helium atoms to accumulate in these metastable states.

2. Resonant Collision Energy Transfer:
Neon has energy states that match the helium metastable levels very closely:
- The He $2^3S_1$ level ($19.82\text{ eV}$) closely matches the Ne $2s$ level ($19.78\text{ eV}$, difference only $0.04\text{ eV}$).
- The He $2^1S_0$ level ($20.61\text{ eV}$) closely matches the Ne $3s$ level ($20.66\text{ eV}$, difference only $0.05\text{ eV}$).
During inelastic collisions between energetic helium atoms and ground-state neon atoms, energy is transferred with high efficiency:
$$\text{He}^*(2^1S_0) + \text{Ne}(\text{ground}) \longrightarrow \text{He}(1^1S_0) + \text{Ne}^*(3s) \pm \Delta E$$
$$\text{He}^*(2^3S_1) + \text{Ne}(\text{ground}) \longrightarrow \text{He}(1^1S_0) + \text{Ne}^*(2s) \pm \Delta E$$
This mechanism populates the Ne $3s$ and $2s$ levels rapidly.

3. Establishment of Population Inversion:
Because ground-state neon atoms are pumped selectively into levels $3s$ and $2s$, while lower levels $3p$ and $2p$ remain sparsely populated, population inversion is achieved between:
- Level $3s$ and level $2p$ (yielding $\lambda = 632.8\text{ nm}$ in the visible red spectrum)
- Level $2s$ and level $2p$ (yielding $\lambda = 1.15\ \mu\text{m}$ in the near-infrared)
- Level $3s$ and level $3p$ (yielding $\lambda = 3.39\ \mu\text{m}$ in the mid-infrared)
The dielectric cavity mirrors are coated to maximize reflectivity at $632.8\text{ nm}$, suppressing the infrared transitions and selecting the prominent red laser line.

4. Lasing and Ground De-excitation:
Stimulated emission produces the $632.8\text{ nm}$ red laser beam:
$$\text{Ne}^*(3s) \longrightarrow \text{Ne}^*(2p) + h\nu \quad (\lambda = 632.8\text{ nm})$$
From the $2p$ state, neon atoms undergo rapid spontaneous radiative decay to the lower $1s$ level, emitting incoherent orange-yellow photons.
From the $1s$ metastable level, neon atoms must be de-excited back to the ground state. If atoms accumulate in $1s$, absorption transitions ($1s \to 2p$) can repopulate the lower laser level and quench population inversion. De-excitation from $1s$ occurs primarily via non-radiative collisions with the narrow capillary tube walls:
$$\text{Ne}(1s) + \text{Tube Wall} \longrightarrow \text{Ne}(\text{ground}) + \text{phonons (heat)}$$
This is why the discharge bore must remain narrow ($2-4\text{ mm}$), ensuring frequent wall collisions to sustain continuous laser action.
"""
        },
        {
            "qid": "phy-q24",
            "marks": 7,
            "type": "Theory & Application",
            "title": "Semiconductor Diode Laser: Direct Bandgap Principle, Population Inversion, and Working",
            "yt_query": "semiconductor laser diode GaAs population inversion homojunction heterojunction working",
            "img_path": "images/physics/semiconductor_laser.png",
            "img_caption": "Figure 5.4: Heavily Doped p-n Junction Energy Band Diagram Under Forward Bias Showing Inversion Zone",
            "answer": r"""
The semiconductor diode laser (injection laser) is a solid-state optoelectronic device that converts electrical energy directly into coherent laser radiation with high quantum efficiency. Demonstrated in 1962 using Gallium Arsenide (GaAs), semiconductor lasers form the physical foundation of modern fiber-optic communications, optical disc drives (CD/DVD/Blu-ray), and barcode scanners due to their compact footprint (microscopic size), direct current modulation capabilities, and low operating voltages.

Physical Working Principle:
Semiconductor lasers require a direct bandgap semiconductor (such as Gallium Arsenide, GaAs, or Indium Phosphide, InP), where the conduction band minimum and valence band maximum align at the same electron crystal momentum ($k = 0$). In direct bandgap crystals, an electron recombines with a hole directly, releasing energy primarily as a photon of light:
$$h\nu \approx E_g \implies \lambda \approx \frac{h c}{E_g} \approx \frac{1.24}{E_g\text{ (in eV)}}\ \mu\text{m}$$
In indirect bandgap materials like Silicon ($Si$) and Germanium ($Ge$), momentum conservation requires emission or absorption of a lattice phonon (phonon-assisted recombination), dissipating energy as heat rather than light. Hence, silicon cannot be used for efficient laser emission.

Heavy Doping and Degenerate Semiconductor States:
To achieve population inversion, the semiconductor diode must be degenerately doped on both sides:
1. The $n$-region is heavily doped with donor impurities (e.g., Tellurium or Silicon) to concentrations exceeding $10^{18}\text{ atoms/cm}^3$. This pushes the Fermi level $E_{Fn}$ up into the conduction band.
2. The $p$-region is heavily doped with acceptor impurities (e.g., Zinc) to similar concentrations, pushing the Fermi level $E_{Fp}$ down into the valence band.
Under zero-bias thermal equilibrium, a built-in potential barrier prevents carrier recombination, and the depletion layer is very thin ($\approx 0.1\ \mu\text{m}$).

Mechanism of Population Inversion via Forward Bias Injection:
When a strong forward-bias voltage $V$ is applied across the junction such that $e V \ge E_g$:
1. The potential barrier across the junction collapses.
2. Huge densities of electrons are injected from the $n$-side into the conduction band of the active depletion zone, and high densities of holes are injected from the $p$-side into the valence band.
3. This creates a narrow active transition zone ($\approx 1\ \mu\text{m}$ thick) containing simultaneously an extremely high density of electrons in the conduction band and an extremely high density of empty states (holes) in the valence band.
4. The condition for population inversion and net stimulated optical gain, known as the Bernard-Duraffourg Condition, is:
$$(E_{Fn} - E_{Fp}) > h\nu > E_g$$
where $E_{Fn}$ and $E_{Fp}$ are the quasi-Fermi levels of the conduction and valence bands under bias. When this threshold is satisfied, stimulated emission exceeds stimulated absorption.

Optical Resonator Cavity Construction:
A semiconductor diode laser uses the crystalline semiconductor itself as the optical resonator cavity:
1. The two front and back faces perpendicular to the junction plane are cleaved along natural crystallographic cleavage planes (e.g., $(110)$ planes), creating mirror-smooth, parallel surfaces.
2. Because GaAs has a high refractive index ($n \approx 3.6$), Fresnel reflection at the semiconductor-air boundary is:
$$R = \left(\frac{n - 1}{n + 1}\right)^2 = \left(\frac{3.6 - 1}{3.6 + 1}\right)^2 = \left(\frac{2.6}{4.6}\right)^2 \approx 0.32 \implies 32\% \text{ Reflectivity}$$
This reflectivity is sufficient to provide the optical feedback necessary for sustained laser oscillation without requiring external mirrors. The remaining sides are intentionally roughened or sawn to eliminate stray transverse laser modes.

Threshold Current and Lasing Dynamics:
At low forward currents ($I < I_{th}$), spontaneous electron-hole recombination dominates, and the diode behaves as an ordinary Light Emitting Diode (LED), emitting low-intensity, incoherent light.
When the injection current is increased above the critical threshold current $I_{th}$ (threshold current density $J_{th}$), stimulated emissions outpace optical absorption and mirror transmission losses. The device abruptly switches into laser oscillation mode, emitting a narrow-linewidth, directional, coherent beam.
For a standard Gallium Arsenide (GaAs) homojunction laser ($E_g \approx 1.42\text{ eV}$ at $300\text{ K}$):
$$\lambda = \frac{1.24}{1.42} \approx 0.873\ \mu\text{m} = 873\text{ nm}$$
emitting in the near-infrared spectrum. Heterostructure lasers (e.g., $GaAs / AlGaAs$ or $InGaAsP / InP$) use bandgap engineering to confine both electrons and photons within the active layer, reducing threshold current densities by orders of magnitude to enable continuous operation at room temperature.
"""
        },
        {
            "qid": "phy-q25",
            "marks": 7,
            "type": "Derivation",
            "title": "Optical Fiber Light Propagation: Total Internal Reflection, Acceptance Angle, and Numerical Aperture",
            "yt_query": "optical fiber numerical aperture acceptance angle derivation total internal reflection",
            "img_path": "images/physics/fiber_numerical_aperture.png",
            "img_caption": "Figure 5.5: Ray Trajectory through Optical Fiber Core Showing Acceptance Cone and TIR at Boundary",
            "answer": r"""
An optical fiber is a cylindrical dielectric waveguide designed to guide electromagnetic energy at optical frequencies along its axis over long distances with minimal attenuation. A basic optical fiber consists of three concentric layers:
1. Inner Core: A central transparent cylindrical dielectric glass or plastic filament of refractive index $n_1$.
2. Outer Cladding: A concentric glass layer surrounding the core having a slightly lower refractive index $n_2$ ($n_2 < n_1$).
3. Protective Buffer Jacket: An outer polymer coating that provides mechanical shielding against abrasion and moisture.

Principle: Total Internal Reflection (TIR):
Light guidance inside the optical fiber relies on Total Internal Reflection (TIR) at the core-cladding interface. According to Snell's law, when a light ray propagating in an optically denser medium of refractive index $n_1$ strikes the boundary of an optically rarer medium of refractive index $n_2$ ($n_1 > n_2$), the refracted ray bends away from the normal. As the angle of incidence $\phi$ increases, the angle of refraction approaches $90^\circ$.
The critical angle of incidence $\phi_c$ is defined as the angle of incidence for which the angle of refraction is exactly $90^\circ$:
$$n_1 \sin\phi_c = n_2 \sin(90^\circ) = n_2 \implies \sin\phi_c = \frac{n_2}{n_1}$$
For Total Internal Reflection to occur:
1. The light ray must travel from the denser medium (core, $n_1$) toward the rarer medium (cladding, $n_2$).
2. The angle of incidence $\phi$ at the core-cladding boundary must equal or exceed the critical angle: $\phi \ge \phi_c$.
Under these conditions, zero energy refracts into the cladding; the ray is reflected back into the core, guiding optical power along the fiber.

Derivation of Acceptance Angle ($\theta_a$) and Numerical Aperture ($NA$):
Consider an optical fiber with core refractive index $n_1$ and cladding refractive index $n_2$ ($n_1 > n_2$). Let the fiber be surrounded by an external launching medium (typically air) of refractive index $n_0 \approx 1.0$.

1. Refraction at the Launching Fiber End Face:
Let a light ray $OA$ enter the flat entrance face of the fiber core at point $A$ at an angle of incidence $\theta_i$ with respect to the fiber's central longitudinal axis.
The ray refracts into the core at an angle of refraction $r$. Applying Snell's law at the air-core entrance interface:
$$n_0 \sin\theta_i = n_1 \sin r \quad \text{--- (Equation 1)}$$

2. Reflection at the Core-Cladding Boundary:
The refracted ray traverses the core and strikes the core-cladding interface at point $B$ at an angle of incidence $\phi$.
From the right-angled triangle formed inside the core by the interface normal and the central axis:
$$r + \phi = 90^\circ \implies \phi = 90^\circ - r$$
For the ray to undergo total internal reflection at point $B$, the angle $\phi$ must satisfy:
$$\phi \ge \phi_c \implies \sin\phi \ge \sin\phi_c$$
Substituting $\phi = 90^\circ - r$ and $\sin\phi_c = \frac{n_2}{n_1}$:
$$\sin(90^\circ - r) \ge \frac{n_2}{n_1} \implies \cos r \ge \frac{n_2}{n_1} \quad \text{--- (Equation 2)}$$

3. Connecting Entrance Angle to Critical Condition:
Using the fundamental trigonometric identity $\sin r = \sqrt{1 - \cos^2 r}$:
$$\sin r \le \sqrt{1 - \left(\frac{n_2}{n_1}\right)^2} = \sqrt{\frac{n_1^2 - n_2^2}{n_1^2}} = \frac{\sqrt{n_1^2 - n_2^2}}{n_1}$$
Substituting this expression for $\sin r$ back into Equation 1:
$$n_0 \sin\theta_i = n_1 \sin r \le n_1 \left( \frac{\sqrt{n_1^2 - n_2^2}}{n_1} \right) = \sqrt{n_1^2 - n_2^2}$$
Dividing by $n_0$:
$$\sin\theta_i \le \frac{\sqrt{n_1^2 - n_2^2}}{n_0}$$
For air as the launching medium, $n_0 = 1.0$:
$$\sin\theta_i \le \sqrt{n_1^2 - n_2^2}$$
The maximum incident launch angle $\theta_{max}$ for which rays undergo total internal reflection and are guided down the fiber is called the Acceptance Angle ($\theta_a$):
$$\theta_a = \sin^{-1}\left(\sqrt{n_1^2 - n_2^2}\right)$$
Any light ray launched within a conical funnel of half-angle $\theta_a$ (total apex angle $2\theta_a$, called the Acceptance Cone) will propagate through the fiber via continuous total internal reflections. Rays launched outside this cone ($\theta_i > \theta_a$) strike the cladding at $\phi < \phi_c$, refracting into the cladding and leaking away.

Numerical Aperture ($NA$):
The Numerical Aperture ($NA$) of an optical fiber is a dimensionless figure of merit that quantifies its light-gathering or light-collecting ability:
$$NA = \sin\theta_a = \sqrt{n_1^2 - n_2^2}$$
We can also express $NA$ in terms of the fractional refractive index difference $\Delta$:
$$\Delta = \frac{n_1 - n_2}{n_1} \implies n_1 - n_2 = n_1 \Delta$$
Factoring the difference of squares:
$$n_1^2 - n_2^2 = (n_1 - n_2)(n_1 + n_2) = (n_1 \Delta)(n_1 + n_2)$$
Because $n_1 \approx n_2$, we can approximate $n_1 + n_2 \approx 2 n_1$:
$$n_1^2 - n_2^2 \approx (n_1 \Delta)(2 n_1) = 2 n_1^2 \Delta$$
Taking the square root gives the standard approximation for Numerical Aperture:
$$NA \approx \sqrt{2 n_1^2 \Delta} = n_1 \sqrt{2\Delta}$$
This formula demonstrates that $NA$ depends solely on the refractive indices of the core and cladding and is independent of fiber dimensions.
"""
        },
        {
            "qid": "phy-q26",
            "marks": 7,
            "type": "Theory & Classification",
            "title": "Classification of Optical Fibers and Attenuation Mechanisms: Absorption, Scattering, and Bending Losses",
            "yt_query": "optical fibers classification step index graded index single multimode attenuation absorption scattering",
            "img_path": "images/physics/fiber_classification_losses.png",
            "img_caption": "Figure 5.6: Index Profiles and Ray Paths in SI/GRIN Fibers and Attenuation Loss Mechanisms",
            "answer": r"""
Optical fibers are deployed in telecommunications, sensor networks, medical endoscopy, and high-speed data interconnects. To match specific performance and bandwidth requirements, fibers are categorized according to their material composition, refractive index profiles, and the number of spatial electromagnetic modes they support.

1. Classification Based on Refractive Index Profile:
- Step-Index (SI) Fiber: In a step-index fiber, the refractive index of the core $n_1$ is uniform and constant throughout its radius, dropping abruptly in a single step to a lower uniform index $n_2$ at the core-cladding interface:
$$n(r) = \begin{cases} n_1 & \text{for } 0 \le r \le a \quad (\text{Core}) \\ n_2 & \text{for } r > a \quad (\text{Cladding}) \end{cases}$$
Light rays propagate along zig-zag trajectories via total internal reflection. In multimode step-index fibers, rays taking steep zig-zag paths travel greater distances than axial rays, causing severe intermodal dispersion that limits data rates.
- Graded-Index (GRIN) Fiber: In a graded-index fiber, the core refractive index is not constant; it peaks along the central optical axis ($r = 0$) and decreases smoothly in a parabolic profile toward the cladding boundary:
$$n(r) = \begin{cases} n_1 \sqrt{1 - 2\Delta \left(\frac{r}{a}\right)^\alpha} & \text{for } 0 \le r \le a \\ n_2 = n_1 \sqrt{1 - 2\Delta} & \text{for } r \ge a \end{cases}$$
where $\alpha \approx 2$ is the parabolic profile grading parameter. Because light travels faster in regions of lower refractive index ($v = c/n$), rays taking longer curved paths through outer radii travel at higher speeds, arriving at the receiving end almost simultaneously with axial rays. This minimizes intermodal dispersion and provides significantly higher bandwidth.

2. Classification Based on Number of Guided Modes:
The number of guided modes is determined by the Normalized Frequency or $V$-number:
$$V = \frac{2\pi a}{\lambda} NA = \frac{2\pi a}{\lambda}\sqrt{n_1^2 - n_2^2}$$
where $a$ is the core radius and $\lambda$ is operating wavelength.
- Single-Mode Fiber (SMF): When $V \le 2.405$, only the fundamental transverse mode ($HE_{11}$) can propagate. SMFs feature a tiny core diameter ($8\text{ to } 10\ \mu\text{m}$) and cladding diameter of $125\ \mu\text{m}$. Because only one optical path exists, intermodal dispersion is eliminated. SMFs offer broad bandwidth ($>100\text{ GHz}\cdot\text{km}$) and are standard for long-haul undersea and continental telecom trunks.
- Multimode Fiber (MMF): When $V > 2.405$, the fiber supports multiple propagation modes (typically hundreds). MMFs have larger core diameters ($50\text{ to } 62.5\ \mu\text{m}$), simplifying connector splicing and allowing coupling to inexpensive LED sources. They are widely used for short-range local area networks (LANs) and enterprise data centers.

Attenuation Mechanisms in Optical Fibers:
Attenuation (signal loss) measures the reduction in optical power as light propagates down the fiber. It is quantified by the attenuation coefficient $\alpha$ (in $\text{dB/km}$):
$$\alpha = \frac{10}{L} \log_{10}\left(\frac{P_{in}}{P_{out}}\right)$$
where $P_{in}$ is input optical power, $P_{out}$ is output power, and $L$ is fiber length in kilometers. Three physical mechanisms contribute to attenuation:

1. Material Absorption Losses:
- Intrinsic Absorption: Caused by fundamental electronic band transitions in the ultraviolet spectrum ($h\nu > E_g$) and atomic lattice vibrational resonances ($Si-O$ bonds) in the infrared region ($\lambda > 1.6\ \mu\text{m}$).
- Extrinsic Absorption: Caused by trace chemical impurities embedded during glass fabrication, notably transition metal ions ($Fe^{2+}, Cu^{2+}, Cr^{3+}$) and hydroxyl ($OH^-$) water radicals. Residual $OH^-$ ions produce strong harmonic absorption peaks around $950\text{ nm}$, $1240\text{ nm}$, and $1383\text{ nm}$. Modern vapor axial deposition (VAD) reduces $OH^-$ concentrations below 1 part per billion, eliminating the $1383\text{ nm}$ water peak.

2. Rayleigh Scattering Losses:
Rayleigh scattering is the dominant intrinsic loss mechanism in the low-loss optical telecom windows ($1310\text{ nm}$ and $1550\text{ nm}$).
- Origin: Silica glass is an amorphous solid formed by quenching molten glass. Microscopic thermodynamic density fluctuations and random compositional variations become frozen into the silica matrix. These sub-wavelength refractive index variations scatter light omnidirectionally.
- Wavelength Dependence: Scattered power is inversely proportional to the fourth power of wavelength:
$$\alpha_{\text{Rayleigh}} \propto \frac{1}{\lambda^4}$$
Consequently, scattering losses drop dramatically at longer infrared wavelengths: $\alpha \approx 2.5\text{ dB/km}$ at $820\text{ nm}$, $0.35\text{ dB/km}$ at $1310\text{ nm}$, and reaches the fundamental silica minimum of $\approx 0.18\text{ dB/km}$ at $1550\text{ nm}$.

3. Bending Radiation Losses:
- Macrobending Losses: Radiative leakage occurring when a fiber undergoes macroscopic physical curving with a bend radius comparable to a few centimeters. Guided rays striking the outer curved boundary encounter angles of incidence shallower than the critical angle ($\phi < \phi_c$), refracting power out into the cladding.
- Microbending Losses: Microscopic geometric imperfections, surface irregularities, or compressive stresses along the fiber axis (e.g., from protective cabling jackets) that produce random micro-bends on the order of microns. Microbending couples energy from guided core modes into lossy radiation and cladding modes.
"""
        }
    ]
}
