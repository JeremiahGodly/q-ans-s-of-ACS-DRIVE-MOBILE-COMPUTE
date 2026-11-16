# -*- coding: utf-8 -*-
"""
Module 1 for Power System II (EET304)
Symmetrical Faults and Z-bus Formulation
"""

M1_QUESTIONS = [
    {
        "qid": "ps2-q1",
        "marks": 3,
        "type": "Short Answer",
        "title": "Transmission Line Transients: Short-Circuit on RL Circuit and DC Offset",
        "yt_query": "transmission line short circuit transients RL circuit DC offset doubling effect",
        "img_path": "images/ps2/rl_circuit_fault_transients.png",
        "img_caption": "Figure 1.1: Transmission Line Short-Circuit Current Showing AC and Decaying DC Components",
        "answer": r"""
A short-circuit fault on a power transmission line produces severe electromagnetic transients governed by the series resistance $R$ and inductance $L$ of the line conductors. To analyze this transient behavior, consider a series RL circuit energized by a sinusoidal voltage source $v(t) = V_m \sin(\omega t + \alpha)$, where $\alpha$ is the switching angle determining the exact point on the voltage wave when the short-circuit occurs at $t = 0$.

Applying Kirchhoff's Voltage Law (KVL) to the faulted loop for $t \ge 0$:
$$L \frac{di(t)}{dt} + R i(t) = V_m \sin(\omega t + \alpha)$$
This is a first-order non-homogeneous linear differential equation. Its total solution consists of the sum of the complementary function (transient natural response $i_{tr}(t)$) and the particular integral (steady-state forced response $i_{ss}(t)$):
$$i(t) = i_{tr}(t) + i_{ss}(t) = A e^{-\frac{R}{L}t} + \frac{V_m}{|Z|} \sin(\omega t + \alpha - \theta)$$
where $|Z| = \sqrt{R^2 + \omega^2 L^2}$ is the circuit impedance and $\theta = \tan^{-1}\left(\frac{\omega L}{R}\right)$ is the impedance angle.

To evaluate the arbitrary constant $A$, we enforce the initial physical boundary condition: because the transmission line possesses magnetic inductance, current cannot change instantaneously. Assuming the pre-fault current is zero ($i(0^-) = 0$):
$$i(0) = A e^0 + \frac{V_m}{|Z|} \sin(\alpha - \theta) = 0 \implies A = -\frac{V_m}{|Z|} \sin(\alpha - \theta)$$
Substituting constant $A$ back into the total current expression:
$$i(t) = \frac{V_m}{|Z|} \sin(\omega t + \alpha - \theta) - \frac{V_m}{|Z|} \sin(\alpha - \theta) e^{-t/\tau}$$
where $\tau = \frac{L}{R}$ is the circuit time constant.

The total short-circuit current consists of two distinct components:
1. Symmetrical AC Component ($i_{ac}(t)$): A sinusoidal current of constant peak amplitude $\frac{V_m}{|Z|}$ oscillating at system frequency $\omega$.
2. Decaying DC Offset Component ($i_{dc}(t)$): An exponential unidirectional current initialized at $-\frac{V_m}{|Z|} \sin(\alpha - \theta)$ decaying to zero with time constant $\tau = L/R$.

The magnitude of the DC offset depends entirely on the switching angle $\alpha$:
- Case 1 (Zero DC Offset): If the fault occurs when $\alpha - \theta = 0$ or $\pi$ (i.e., at voltage maximum for a purely inductive line), the DC offset is identically zero ($i_{dc}(t) = 0$), and the fault current is completely symmetrical from $t = 0$.
- Case 2 (Maximum DC Offset / The Doubling Effect): If the fault occurs when $\alpha - \theta = -\frac{\pi}{2}$ (i.e., at voltage zero crossing for an inductive line where $\theta \approx 90^\circ$ and $\alpha = 0$), the initial DC offset reaches its theoretical maximum:
$$i_{dc}(0) = -\frac{V_m}{|Z|} \sin\left(-\frac{\pi}{2}\right) = +\frac{V_m}{|Z|}$$
At the first positive half-cycle peak ($\omega t = \pi$):
$$i_{total}(\pi/\omega) = \frac{V_m}{|Z|}\sin(\pi - \pi/2) + \frac{V_m}{|Z|} e^{-\frac{\pi}{\omega\tau}} \approx \frac{V_m}{|Z|} + \frac{V_m}{|Z|} = 2 \frac{V_m}{|Z|}$$
This doubling of peak current is termed the Doubling Effect. Circuit breakers must be mechanically rated to withstand this immense peak momentary electromechanical force.
"""
    },
    {
        "qid": "ps2-q2",
        "marks": 7,
        "type": "Long Derivation",
        "title": "Symmetrical Fault on Synchronous Machine: Reactances and Internal Voltages",
        "yt_query": "synchronous machine symmetrical 3 phase short circuit subtransient transient reactance",
        "img_path": "images/ps2/synchronous_machine_reactances.png",
        "img_caption": "Figure 1.2: Symmetrical Fault Current Envelope of Synchronous Generator Showing Subtransient and Transient Regions",
        "answer": r"""
When a symmetrical three-phase short circuit occurs at the terminals of an energized synchronous generator, the fault current undergoes a profound transient evolution that is fundamentally different from a static RL circuit. The effective internal reactance of the machine does not remain constant; instead, it varies progressively through three distinct operating regimes governed by the magnetic flux coupling between the stator armature windings, rotor field winding, and rotor damper (amortisseur) windings.

Physical Phenomena During Machine Short Circuit:
Prior to the fault, the air gap flux is produced entirely by the rotor DC field excitation. When the three-phase fault strikes, heavy, lagging demagnetizing armature currents immediately flow through the stator windings. By Lenz's law, magnetic flux linkages cannot change instantaneously. To oppose the sudden penetration of this demagnetizing armature reaction flux:
1. Induced currents surge instantaneously in both the low-resistance rotor damper bars and the main field winding.
2. Because the damper windings have a very small leakage inductance and close proximity to the stator surface, they force the initial armature flux into high-reluctance leakage paths between the stator and rotor teeth, severely restricting the mutual air-gap flux.
3. As the damper currents decay rapidly according to their short subtransient time constant $T_d''$ (typically 0.02 to 0.05 seconds), the flux penetrates into the main field winding.
4. The field winding induced currents decay more slowly according to the transient time constant $T_d'$ (typically 0.5 to 2.0 seconds).
5. Finally, after all rotor eddy currents dissipate, the machine reaches the steady-state condition where the armature reaction flux fully counteracts the field MMF, leaving only the steady-state air-gap flux.

Classification of Generator Reactances:
Based on this time-varying flux penetration, three distinct machine reactances are defined:
1. Subtransient Reactance ($X_d''$): The effective reactance during the first few cycles ($0 \le t \le 3$ cycles) while both damper and field windings carry induced currents. It represents the smallest internal reactance ($X_d'' < X_d' < X_d$), resulting in the highest initial RMS current:
$$I'' = \frac{E_g}{X_d''}$$
2. Transient Reactance ($X_d'$): The effective reactance after damper currents have fully decayed but field currents still resist flux changes ($3 \text{ cycles} \le t \le 30$ cycles):
$$I' = \frac{E_g}{X_d'}$$
3. Steady-State Synchronous Reactance ($X_d$): The continuous reactance after all transients have ceased, comprising armature leakage reactance $X_l$ and armature reaction reactance $X_{ar}$:
$$X_d = X_l + X_{ar}, \quad I = \frac{E_g}{X_d}$$

Internal Voltages Under Loaded Conditions:
If the generator is supplying a steady pre-fault load current $I_L$ at terminal voltage $V_t$ with power factor angle $\theta$:
1. Subtransient Internal Voltage ($E''$):
$$E'' = V_t + j I_L X_d''$$
The subtransient fault current injected into a terminal fault is:
$$I_{f}'' = \frac{E''}{X_d''}$$
2. Transient Internal Voltage ($E'$):
$$E' = V_t + j I_L X_d'$$
The transient fault current is:
$$I_{f}' = \frac{E'}{X_d'}$$
3. Steady-State Excitation EMF ($E_g$):
$$E_g = V_t + j I_L X_d$$

Oscillographic Analysis:
By plotting the symmetrical envelope of the fault current oscillogram on semi-logarithmic paper, the total AC envelope current is expressed mathematically as:
$$i_{ac}(t) = \sqrt{2} \left[ (I'' - I') e^{-t/T_d''} + (I' - I) e^{-t/T_d'} + I \right] \cos(\omega t)$$
This analytical decomposition enables protection engineers to select circuit breakers whose interrupting capabilities precisely match the decaying short-circuit current at the moment of contact separation.
"""
    },
    {
        "qid": "ps2-q3",
        "marks": 3,
        "type": "Short Answer",
        "title": "Short Circuit MVA and Symmetrical vs Momentary Circuit Breaker Ratings",
        "yt_query": "short circuit MVA calculation circuit breaker rating momentary interrupting capacity",
        "img_path": "images/ps2/circuit_breaker_ratings.png",
        "img_caption": "Figure 1.3: Circuit Breaker Contact Separation Timeline Dictating Interrupting Duties",
        "answer": r"""
In power system design, the severity of a prospective fault at a given bus is quantified by the Short Circuit MVA (also known as fault level). The short circuit MVA defines the total apparent power entering a bolted three-phase symmetrical fault.

The three-phase Short Circuit MVA is mathematically defined as:
$$SCMVA = \sqrt{3} \times V_{L,rated} \times I_{sc} \times 10^{-6} \text{ MVA}$$
where $V_{L,rated}$ is the nominal line-to-line operating voltage in volts, and $I_{sc}$ is the symmetrical RMS short-circuit current in amperes.
In the per-unit system:
$$I_{sc,pu} = \frac{V_{th,pu}}{X_{th,pu}} \approx \frac{1.0}{X_{th,pu}}$$
where $X_{th,pu}$ is the positive-sequence Thevenin reactance of the power network viewed from the fault point on the chosen system base MVA ($MVA_{base}$).
Multiplying per-unit fault current by base MVA yields the direct formula:
$$SCMVA = \frac{MVA_{base}}{X_{th,pu}}$$

Circuit Breaker Selection Criteria:
Circuit breakers are electromechanical protective switches that must perform two distinct physical duties during a fault:
1. Momentary (Making) Current Rating:
When a breaker closes onto an existing fault, its contacts must withstand the peak mechanical electromagnetic forces ($F \propto i^2$) produced by the initial peak current during the first half-cycle. Because the fault may contain the maximum possible DC offset (doubling effect), the rated making current is defined as:
$$I_{making,peak} = 1.6 \times \sqrt{2} \times I_{sc,sym} \approx 2.55 \times I_{sc,sym}$$
where the factor $\sqrt{2}$ converts RMS to peak, and the factor $1.6$ accounts for the decaying DC offset present at $t = 10 \text{ ms}$ (in a $50 \text{ Hz}$ system).

2. Symmetrical Interrupting Current Rating:
When a breaker opens to extinguish the fault arc, contact separation occurs after a finite operating delay comprising relay pickup time plus breaker mechanical parting time (typically 2 to 5 cycles, corresponding to 40 to 100 ms). Because the high-frequency subtransient DC and AC components have partially decayed during this interval, the required interrupting current is evaluated using generator transient reactances modified by standard IEEE/ANSI multiplying factors:
- For 2-cycle breaker: Multiplying factor = $1.4 \times I_{sc,sym}$
- For 3-cycle breaker: Multiplying factor = $1.2 \times I_{sc,sym}$
- For 5-cycle breaker: Multiplying factor = $1.1 \times I_{sc,sym}$
- For 8-cycle breaker: Multiplying factor = $1.0 \times I_{sc,sym}$

The rated interrupting MVA of the circuit breaker is specified as:
$$MVA_{interrupting} = \sqrt{3} \times V_{L,rated} \times I_{interrupting,sym}$$
Breakers must be selected such that both their making current and interrupting MVA exceed the maximum calculated fault duty at their installation bus.
"""
    },
    {
        "qid": "ps2-q4",
        "marks": 7,
        "type": "Long Derivation",
        "title": "Bus Impedance Matrix (Z_bus) Building Algorithm and Kron Reduction",
        "yt_query": "Z bus building algorithm step by step power systems kron reduction",
        "img_path": "images/ps2/z_bus_building_algorithm.png",
        "img_caption": "Figure 1.4: Four Canonical Branch Addition Modifications in Z_bus Formulation",
        "answer": r"""
The Bus Impedance Matrix ($Z_{bus}$) is the inverse of the Bus Admittance Matrix ($Y_{bus}$). While $Y_{bus}$ is sparse and easily formed by inspection, $Z_{bus}$ is a dense matrix whose elements directly provide the driving-point Thevenin impedances and transfer impedances essential for fault studies. The $Z_{bus}$ building algorithm synthesizes the matrix branch-by-branch without requiring matrix inversion.

Let an existing power network consist of $m$ independent buses plus reference bus $0$, characterized by the known impedance relationship:
$$V_{bus} = Z_{bus} I_{bus}$$
When a new branch of impedance $z_b$ is connected, the matrix is updated according to four fundamental topological modifications:

Type 1 Modification: Adding branch $z_b$ from a new bus $p$ to reference bus $0$.
- A new bus $p = m + 1$ is added. Because this new bus is connected only to the reference, its voltage is unaffected by currents injected into existing buses:
$$Z_{pi} = Z_{ip} = 0 \quad \forall i = 1, 2, \dots, m$$
$$Z_{pp} = z_b$$
The augmented matrix grows in dimension by one:
$$Z_{bus}^{new} = \begin{bmatrix} Z_{bus}^{old} & 0 \\ 0 & z_b \end{bmatrix}$$

Type 2 Modification: Adding branch $z_b$ from a new bus $p$ to an existing bus $k$.
- The current $I_p$ injected into new bus $p$ must flow entirely through branch $z_b$ into existing bus $k$. Hence, the voltage of new bus $p$ is $V_p = V_k + z_b I_p$:
$$Z_{pi} = Z_{ip} = Z_{ki} \quad \forall i = 1, 2, \dots, m$$
$$Z_{pp} = Z_{kk} + z_b$$
The matrix grows to $(m+1) \times (m+1)$:
$$Z_{bus}^{new} = \begin{bmatrix} Z_{bus}^{old} & Z_{col, k} \\ Z_{row, k} & Z_{kk} + z_b \end{bmatrix}$$

Type 3 Modification: Adding branch $z_b$ from an existing bus $k$ to reference bus $0$.
- No new bus is introduced, but a closed loop is formed. We temporarily treat reference bus $0$ as a fictitious new bus $q$, creating an intermediate $(m+1) \times (m+1)$ matrix using the Type 2 rule:
$$Z_{qi} = Z_{iq} = Z_{ki}, \quad Z_{qq} = Z_{kk} + z_b$$
Because bus $q$ is actually the reference bus, its potential must be zero: $V_q = 0$.
The $(m+1)$-th row equation is:
$$V_q = 0 = \sum_{j=1}^m Z_{qj} I_j + Z_{qq} I_q \implies I_q = -\frac{1}{Z_{qq}} \sum_{j=1}^m Z_{qj} I_j$$
Substituting $I_q$ back into the first $m$ bus voltage equations eliminates the fictitious $(m+1)$-th row and column via Kron Reduction:
$$Z_{ij}^{new} = Z_{ij}^{old} - \frac{Z_{iq} Z_{qj}}{Z_{qq}} = Z_{ij}^{old} - \frac{Z_{ik} Z_{kj}}{Z_{kk} + z_b} \quad \forall i, j = 1, \dots, m$$

Type 4 Modification: Adding branch $z_b$ between two existing buses $j$ and $k$.
- This closes an internal mesh loop without creating a new physical bus. We temporarily create a fictitious loop bus $q$, where the voltage drop across the new branch satisfies $V_j - V_k + z_b I_q = 0$.
The intermediate column and row entries are:
$$Z_{qi} = Z_{iq} = Z_{ji} - Z_{ki} \quad \forall i = 1, \dots, m$$
$$Z_{qq} = Z_{jj} + Z_{kk} - 2 Z_{jk} + z_b$$
Eliminating the fictitious loop current $I_q$ via Kron Reduction restores the $m \times m$ dimension:
$$Z_{il}^{new} = Z_{il}^{old} - \frac{Z_{iq} Z_{ql}}{Z_{qq}} = Z_{il}^{old} - \frac{(Z_{ij} - Z_{ik})(Z_{jl} - Z_{kl})}{Z_{jj} + Z_{kk} - 2 Z_{jk} + z_b}$$

Application to Fault Analysis:
The diagonal element $Z_{kk}$ represents the driving-point Thevenin impedance directly at bus $k$. For a bolted three-phase fault at bus $k$ with pre-fault voltage $V_k(0) = 1.0 \text{ pu}$:
$$I_{f,k} = \frac{V_k(0)}{Z_{kk}} = \frac{1.0}{Z_{kk}}$$
The post-fault voltage at any other bus $i$ during the fault at bus $k$ is determined algebraically in a single line:
$$V_i^{fault} = V_i(0) - Z_{ik} I_{f,k} = V_i(0) - \frac{Z_{ik}}{Z_{kk}} V_k(0)$$
This demonstrates the tremendous computational superiority of $Z_{bus}$ for automated short-circuit analysis.
"""
    },
    {
        "qid": "ps2-q5",
        "marks": 7,
        "type": "Long Derivation",
        "title": "Comprehensive Numerical Problem: 3-Phase Symmetrical Fault on Interconnected System",
        "yt_query": "3 phase symmetrical fault calculation per unit reactance diagram solved example",
        "img_path": "images/ps2/symmetrical_fault_numerical_system.png",
        "img_caption": "Figure 1.5: Single-Line Reactance Network for Three-Phase Symmetrical Fault Calculation",
        "answer": r"""
Consider a classic KTU university examination problem:
A three-phase power system consists of two synchronous generators $G_1$ and $G_2$ feeding a transmission network through step-up transformers $T_1$ and $T_2$. The equipment ratings are:
- Generator $G_1$: $100 \text{ MVA}, 15 \text{ kV}, X_d'' = 15\%$ ($0.15 \text{ pu}$).
- Generator $G_2$: $50 \text{ MVA}, 15 \text{ kV}, X_d'' = 20\%$ ($0.20 \text{ pu}$).
- Transformer $T_1$: $100 \text{ MVA}, 15 / 132 \text{ kV}, X = 10\%$ ($0.10 \text{ pu}$).
- Transformer $T_2$: $50 \text{ MVA}, 15 / 132 \text{ kV}, X = 8\%$ ($0.08 \text{ pu}$).
- Transmission line connecting the high-voltage sides of $T_1$ and $T_2$ has a total series reactance of $X_{line} = 25 \ \Omega$.

A symmetrical three-phase bolted short-circuit occurs at the high-voltage terminals of transformer $T_1$ (Bus 1). The system is initially operating unloaded at rated voltage ($132 \text{ kV}$).
Select a common system base of $100 \text{ MVA}$ and $132 \text{ kV}$ on the transmission line.
Determine:
(i) The per-unit reactance diagram.
(ii) The Thevenin equivalent reactance at the fault point.
(iii) The total fault current in kA and fault MVA.
(iv) The individual short-circuit current contributions from generators $G_1$ and $G_2$.

Step 1: Determine Base Quantities:
- Common Base Power: $MVA_{base} = 100 \text{ MVA}$.
- Transmission line base voltage: $kV_{base, line} = 132 \text{ kV}$.
- Generator side base voltage:
  $$kV_{base, gen} = 132 \times \frac{15}{132} = 15 \text{ kV}$$
- Base impedance on $132 \text{ kV}$ line:
  $$Z_{base, line} = \frac{(kV_{base, line})^2}{MVA_{base}} = \frac{132^2}{100} = \frac{17424}{100} = 174.24 \ \Omega$$
- Base current on $132 \text{ kV}$ line:
  $$I_{base, line} = \frac{MVA_{base} \times 10^3}{\sqrt{3} \times kV_{base, line}} = \frac{100 \times 10^3}{\sqrt{3} \times 132} = \frac{100000}{228.63} = 437.38 \text{ A} = 0.4374 \text{ kA}$$

Step 2: Convert all reactances to the common $100 \text{ MVA}$ base:
Using the standard conversion formula:
$$X_{new, pu} = X_{old, pu} \times \left(\frac{MVA_{base, new}}{MVA_{base, old}}\right) \times \left(\frac{kV_{base, old}}{kV_{base, new}}\right)^2$$
- For Generator $G_1$: Rated on $100 \text{ MVA}, 15 \text{ kV}$:
  $$X_{G1} = 0.15 \text{ pu}$$
- For Generator $G_2$: Rated on $50 \text{ MVA}, 15 \text{ kV}$:
  $$X_{G2} = 0.20 \times \left(\frac{100}{50}\right) \times \left(\frac{15}{15}\right)^2 = 0.20 \times 2 = 0.40 \text{ pu}$$
- For Transformer $T_1$: Rated on $100 \text{ MVA}$:
  $$X_{T1} = 0.10 \text{ pu}$$
- For Transformer $T_2$: Rated on $50 \text{ MVA}$:
  $$X_{T2} = 0.08 \times \left(\frac{100}{50}\right) = 0.08 \times 2 = 0.16 \text{ pu}$$
- For Transmission Line ($25 \ \Omega$):
  $$X_{line, pu} = \frac{X_{actual}}{Z_{base, line}} = \frac{25}{174.24} = 0.1435 \text{ pu}$$

Step 3: Construct Per-Unit Reactance Diagram:
- Branch 1 (from Generator $G_1$ to Fault Bus 1):
  $$X_{branch1} = X_{G1} + X_{T1} = 0.15 + 0.10 = 0.25 \text{ pu}$$
- Branch 2 (from Generator $G_2$ through $T_2$ and Line to Fault Bus 1):
  $$X_{branch2} = X_{G2} + X_{T2} + X_{line} = 0.40 + 0.16 + 0.1435 = 0.7035 \text{ pu}$$

Step 4: Calculate Thevenin Impedance at Fault Point (Bus 1):
Because the generators operate in parallel with neutral references connected together:
$$X_{th} = X_{branch1} \parallel X_{branch2} = \frac{X_{branch1} \times X_{branch2}}{X_{branch1} + X_{branch2}} = \frac{0.25 \times 0.7035}{0.25 + 0.7035} = \frac{0.175875}{0.9535} = 0.1844 \text{ pu}$$

Step 5: Calculate Fault Current and Short-Circuit MVA:
Pre-fault voltage at Bus 1 is $V_f = 1.0 \angle 0^\circ \text{ pu}$.
- Total fault current in per-unit:
  $$I_{f, pu} = \frac{V_f}{j X_{th}} = \frac{1.0}{j 0.1844} = -j 5.422 \text{ pu}$$
- Total physical fault current:
  $$I_f = |I_{f, pu}| \times I_{base, line} = 5.422 \times 0.4374 \text{ kA} = 2.371 \text{ kA} \quad (2371 \text{ A})$$
- Short-Circuit MVA ($SCMVA$):
  $$SCMVA = \frac{MVA_{base}}{X_{th}} = \frac{100}{0.1844} = 542.3 \text{ MVA}$$

Step 6: Generator Fault Current Contributions:
Using the current divider rule on the two parallel branches:
- Contribution from Generator $G_1$ path:
  $$I_{f1, pu} = I_{f, pu} \times \frac{X_{branch2}}{X_{branch1} + X_{branch2}} = 5.422 \times \frac{0.7035}{0.9535} = 4.000 \text{ pu}$$
  Physical current in $132 \text{ kV}$ line from $T_1$:
  $$I_{f1} = 4.000 \times 0.4374 = 1.750 \text{ kA}$$
- Contribution from Generator $G_2$ path:
  $$I_{f2, pu} = I_{f, pu} \times \frac{X_{branch1}}{X_{branch1} + X_{branch2}} = 5.422 \times \frac{0.25}{0.9535} = 1.422 \text{ pu}$$
  Physical current from $G_2$:
  $$I_{f2} = 1.422 \times 0.4374 = 0.622 \text{ kA}$$
Check: $I_{f1} + I_{f2} = 1.750 + 0.622 = 2.372 \text{ kA} \approx I_f$.
This rigorous step-by-step working provides the complete solution expected in KTU university evaluations.
"""
    }
]
