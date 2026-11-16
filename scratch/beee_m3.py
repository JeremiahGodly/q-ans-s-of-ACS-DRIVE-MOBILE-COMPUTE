# -*- coding: utf-8 -*-
"""
Module 3 for Basics of Electrical & Electronics Engineering (EST130 / BEEE)
Transformers, DC Machines, 3-Phase Systems & Wiring
KTU 2019 Scheme Electrical & Electronics Engineering
"""

MODULE_3 = {
    "module_id": "beee-m3",
    "module_num": "Module 3",
    "module_title": "Transformers, DC Machines, 3-Phase Systems & Wiring",
    "questions": [
        {
            "qid": "beee-q11",
            "marks": 7,
            "type": "Long Derivation",
            "title": "Single-Phase Transformer: Construction, Working, EMF Equation, Losses, and Maximum Efficiency Condition",
            "yt_query": "single phase transformer construction emf equation losses maximum efficiency derivation",
            "img_path": "images/beee/transformer_construction_efficiency.png",
            "img_caption": "Figure 3.1: Core vs Shell Transformer Topologies, Mutual Induction Principle, and Efficiency vs Load Curve",
            "answer": r"""
A single-phase transformer is a static electromagnetic device that transfers alternating electrical energy from one circuit to another at identical frequency through the medium of mutual magnetic flux, usually with transformed values of voltage and current.

Constructional Classification:
1. Core-Type Transformer: The magnetic circuit consists of two vertical limbs (legs) connected by top and bottom horizontal yokes. The primary and secondary windings are split into halves and wound concentrically on both limbs, with the low-voltage (LV) winding placed innermost next to the laminated silicon-steel core to minimize insulation requirements, and the high-voltage (HV) winding wound outside. Core-type transformers feature a single magnetic loop, longer mean magnetic path, and excellent natural cooling accessibility.
2. Shell-Type Transformer: The magnetic circuit possesses three limbs: a central limb with double the cross-sectional area and two outer limbs that each carry half of the total magnetic flux ($\Phi_m / 2$). Both primary and secondary windings are wound sandwich-fashion onto the central limb. Shell-type construction offers superior mechanical bracing against short-circuit electromagnetic forces and lower leakage reactance, making it ideal for low-voltage, high-current industrial applications.
To minimize eddy current losses, transformer cores are constructed from thin cold-rolled grain-oriented (CRGO) silicon steel laminations ($0.35\text{ mm}$ to $0.5\text{ mm}$ thick) insulated from each other by varnish or oxide coating.

Working Principle:
When the primary winding of $N_1$ turns is connected to a sinusoidal alternating voltage supply $v_1(t) = V_{m1} \sin(\omega t)$, an alternating magnetizing current flows, establishing an alternating magnetic flux $\Phi(t) = \Phi_m \sin(\omega t)$ in the core. This flux links completely with both the primary winding and the secondary winding of $N_2$ turns, inducing electromotive forces $e_1$ and $e_2$ by Faraday's law of electromagnetic induction.

Derivation of the Transformer EMF Equation:
Let the alternating mutual flux in the core be:
$$\Phi(t) = \Phi_m \sin(\omega t)$$
According to Faraday's law, the instantaneous EMF induced in the primary winding of $N_1$ turns is:
$$e_1(t) = -N_1 \frac{d\Phi}{dt} = -N_1 \frac{d}{dt}\left[ \Phi_m \sin(\omega t) \right] = -N_1 \Phi_m \omega \cos(\omega t)$$
Using the trigonometric identity $-\cos(\theta) = \sin(\theta - 90^\circ)$:
$$e_1(t) = N_1 \Phi_m (2\pi f) \sin\left(\omega t - \frac{\pi}{2}\right) = 2\pi f N_1 \Phi_m \sin\left(\omega t - \frac{\pi}{2}\right)$$
The maximum (peak) induced primary EMF is:
$$E_{m1} = 2\pi f N_1 \Phi_m$$
Because the induced EMF is purely sinusoidal, its RMS value is obtained by dividing the peak value by $\sqrt{2}$:
$$E_1 = \frac{E_{m1}}{\sqrt{2}} = \frac{2\pi}{\sqrt{2}} f N_1 \Phi_m = \sqrt{2}\pi f N_1 \Phi_m$$
Substituting $\pi \approx 3.14159$ and $\sqrt{2} \approx 1.41421$:
$$\sqrt{2}\pi = 1.41421 \times 3.14159 = 4.44288 \approx 4.44$$
Therefore, the RMS primary induced EMF is:
$$E_1 = 4.44 f N_1 \Phi_m = 4.44 f N_1 B_m A$$
Similarly, the RMS secondary induced EMF is:
$$E_2 = 4.44 f N_2 \Phi_m = 4.44 f N_2 B_m A$$
Dividing the two equations yields the Voltage Transformation Ratio $K$:
$$K = \frac{E_2}{E_1} = \frac{N_2}{N_1} \approx \frac{V_2}{V_1} = \frac{I_1}{I_2}$$
where $K > 1$ represents a step-up transformer, and $K < 1$ represents a step-down transformer.

Transformer Losses and Efficiency:
Total power loss in a transformer consists of:
1. Core / Iron Losses ($W_i$): Constant losses independent of load current, comprising hysteresis loss ($W_h = \eta B_m^{1.6} f$) and eddy current loss ($W_e = k_e B_m^2 f^2 t^2$).
2. Copper / Ohmic Losses ($W_{cu}$): Variable losses caused by winding resistances, proportional to the square of load current:
$$W_{cu} = I_1^2 R_1 + I_2^2 R_2 = I_2^2 R_{02} = x^2 W_{cu(FL)}$$
where $x$ is the fraction of full-load rating ($x = I_2 / I_{2(FL)}$).
The commercial efficiency of a transformer at load fraction $x$ and power factor $\cos\phi_2$ is:
$$\eta = \frac{\text{Output Power}}{\text{Input Power}} = \frac{x S \cos\phi_2}{x S \cos\phi_2 + W_i + x^2 W_{cu(FL)}}$$
where $S$ is the rated apparent power in VA.

Condition for Maximum Efficiency:
To find the load current $I_2$ (or fraction $x$) that maximizes efficiency at constant voltage and power factor, we rewrite $\eta$ in terms of $I_2$:
$$\eta = \frac{V_2 I_2 \cos\phi_2}{V_2 I_2 \cos\phi_2 + W_i + I_2^2 R_{02}} = \frac{1}{1 + \frac{W_i}{V_2 I_2 \cos\phi_2} + \frac{I_2 R_{02}}{V_2 \cos\phi_2}}$$
Maximizing $\eta$ is equivalent to minimizing the denominator $D(I_2)$:
$$D(I_2) = 1 + \frac{W_i}{V_2 I_2 \cos\phi_2} + \frac{I_2 R_{02}}{V_2 \cos\phi_2}$$
Differentiating $D(I_2)$ with respect to $I_2$ and setting to zero:
$$\frac{d D(I_2)}{d I_2} = -\frac{W_i}{V_2 I_2^2 \cos\phi_2} + \frac{R_{02}}{V_2 \cos\phi_2} = 0$$
$$\frac{W_i}{V_2 I_2^2 \cos\phi_2} = \frac{R_{02}}{V_2 \cos\phi_2} \implies W_i = I_2^2 R_{02} = W_{cu}$$
Thus, maximum efficiency occurs when the variable copper loss equals the constant iron loss:
$$W_{cu} = W_i$$
The fraction of full load $x_m$ at which maximum efficiency occurs is:
$$x_m = \sqrt{\frac{W_i}{W_{cu(FL)}}}$$
"""
        },
        {
            "qid": "beee-q12",
            "marks": 7,
            "type": "Long Derivation",
            "title": "DC Generator: Constructional Details, Operating Principle, and Derivation of the EMF Equation",
            "yt_query": "dc generator construction working principle emf equation derivation lap wave winding",
            "img_path": "images/beee/dc_generator_construction_emf.png",
            "img_caption": "Figure 3.2: Cutaway Cross-Section of DC Machine and Conductors Under P Magnetic Poles",
            "answer": r"""
A DC generator is a rotating electrical machine that converts mechanical power supplied by a prime mover into direct current (DC) electrical power through dynamic electromagnetic induction.

Constructional Components of a DC Machine:
1. Yoke (Magnetic Frame): The outer cylindrical cast iron or rolled steel ring that provides mechanical protection for internal components and serves as the return magnetic path carrying half of the pole flux ($\Phi/2$).
2. Pole Cores and Pole Shoes: Laminated silicon-steel poles bolted to the inner periphery of the yoke. The curved pole shoe spreads the magnetic flux uniformly over the armature periphery and mechanically supports the field exciting coils.
3. Field (Exciting) Winding: Copper coils wound on pole cores that produce working magnetic flux $\Phi$ when energized by DC current.
4. Armature Core: A cylindrical drum keyed to the shaft, assembled from thin ($0.5\text{ mm}$) slotted silicon-steel circular laminations coated with insulating varnish to minimize eddy current losses. The slots accommodate the insulated copper armature conductors.
5. Armature Winding: Insulated copper conductors connected in closed circuits, arranged in two standard configurations:
   - Lap Winding: Finishes of coils are connected to adjacent commutator segments; number of parallel paths equals the number of poles ($A = P$). Lap winding is used for low-voltage, heavy-current machines.
   - Wave Winding: Coils progress around the armature in a wave-like pattern; number of parallel paths is always two ($A = 2$), regardless of the number of poles. Wave winding is used for high-voltage, low-current machines.
6. Commutator: A mechanical cylindrical assembly composed of hard-drawn wedge-shaped copper segments insulated from each other by thin mica sheets ($0.7\text{ mm}$). It serves as a mechanical rectifier, converting the alternating EMF induced internally in armature conductors into unidirectional direct EMF at the external brushes.
7. Carbon Brushes and Bearings: Spring-loaded high-conductivity carbon/graphite blocks riding on the commutator surface to collect load current with minimal sparking and friction.

Working Principle:
When the armature is driven by a prime mover at speed $N$ RPM within the magnetic field produced by the field poles, the armature conductors physically cut the stationary magnetic flux lines. According to Faraday's law of electromagnetic induction, a motional EMF is dynamically induced in each conductor. The direction of this induced EMF is determined by Fleming's Right-Hand Rule: stretch the thumb, forefinger, and middle finger of the right hand mutually perpendicular; if the forefinger points along the magnetic field ($N \to S$) and the thumb points in the direction of conductor motion, the middle finger indicates the direction of induced EMF.

Derivation of the DC Generator EMF Equation:
Let the machine parameters be defined as follows:
- $P$: Total number of magnetic field poles.
- $\Phi$: Useful magnetic flux per pole, in Webers ($\text{Wb}$).
- $Z$: Total number of active armature conductors.
- $N$: Rotational speed of the armature, in revolutions per minute ($\text{RPM}$).
- $A$: Number of parallel electrical paths through the armature winding ($A = P$ for lap winding, $A = 2$ for wave winding).

Consider a single armature conductor rotating through one complete revolution:
The time required to complete one revolution ($t_{rev}$) is:
$$t_{rev} = \frac{60}{N}\text{ seconds}$$
In one complete revolution, the conductor sweeps past all $P$ poles. The total magnetic flux cut by the conductor in one revolution is:
$$d\Phi = P \cdot \Phi\text{ Webers}$$
According to Faraday's law of electromagnetic induction, the average EMF induced in a single conductor is:
$$e_{avg} = \frac{d\Phi}{dt} = \frac{P \cdot \Phi}{\frac{60}{N}} = \frac{\Phi P N}{60}\text{ Volts}$$

The total of $Z$ armature conductors is distributed equally among $A$ parallel paths. Therefore, the number of conductors connected in series in each parallel path is:
$$\text{Conductors in series per path} = \frac{Z}{A}$$
Because all conductors in a path are connected in series, the total generated electromotive force ($E_g$) measured across the armature terminals is the product of the average EMF induced per conductor and the number of conductors in series per path:
$$E_g = e_{avg} \times \left( \frac{Z}{A} \right) = \left( \frac{\Phi P N}{60} \right) \times \left( \frac{Z}{A} \right)$$
Rearranging terms yields the universally celebrated DC Generator EMF Equation:
$$E_g = \frac{\Phi Z N P}{60 A}\text{ Volts}$$

For a Lap-Wound armature ($A = P$):
$$E_g(\text{lap}) = \frac{\Phi Z N P}{60 P} = \frac{\Phi Z N}{60}\text{ Volts}$$
For a Wave-Wound armature ($A = 2$):
$$E_g(\text{wave}) = \frac{\Phi Z N P}{60 \times 2} = \frac{\Phi Z N P}{120}\text{ Volts}$$
This mathematical proof confirms that a wave-wound machine produces a much higher terminal voltage than an identical lap-wound machine operating at the same speed and flux.
"""
        },
        {
            "qid": "beee-q13",
            "marks": 7,
            "type": "Long Derivation",
            "title": "DC Motor: Working Principle, Significance of Back-EMF, Torque Equation, and Speed Relation",
            "yt_query": "dc motor working principle back emf significance torque equation speed derivation",
            "img_path": "images/beee/dc_motor_back_emf_torque.png",
            "img_caption": "Figure 3.3: DC Motor Armature Circuit Model with Back-EMF and Fleming's Left-Hand Rule",
            "answer": r"""
A DC motor converts direct current electrical power into mechanical rotational power. Its operation is governed by the Lorentz force principle: when a current-carrying conductor is placed in a magnetic field, it experiences a mechanical force perpendicular to both the conductor and the magnetic flux lines.

Operating Principle and Fleming's Left-Hand Rule:
When DC supply voltage $V$ is applied to the armature through the commutator brushes, current $I_a$ flows through the armature conductors situated under the magnetic poles. According to the Lorentz force equation, each conductor of active length $l$ carrying current $I$ in a magnetic field of flux density $B$ experiences a force:
$$F = B \cdot I \cdot l\text{ Newtons}$$
The direction of this mechanical force is determined by Fleming's Left-Hand Rule: orient the thumb, forefinger, and middle finger of the left hand mutually at right angles; if the forefinger points along the magnetic field ($N \to S$) and the middle finger points in the direction of current, the thumb indicates the direction of mechanical force and rotor motion. The forces on conductors on opposite sides of the shaft create a continuous electromagnetic torque that drives the rotor.

Concept and Significance of Back-EMF ($E_b$):
As the motor armature rotates under electromagnetic torque, its conductors physically cut the magnetic flux lines of the field poles. By Faraday's law of electromagnetic induction, an electromotive force is dynamically induced in the rotating armature conductors, exactly as in a DC generator. According to Lenz's law, the direction of this induced EMF must oppose the cause producing it—namely, the applied terminal voltage $V$. Consequently, this induced potential is termed the Back-EMF or Counter-EMF, denoted by $E_b$.
The magnitude of back-EMF is given by the generator equation:
$$E_b = \frac{\Phi Z N P}{60 A}\text{ Volts}$$
The fundamental voltage equation of a DC motor is obtained by applying KVL to the armature circuit:
$$V = E_b + I_a R_a \implies I_a = \frac{V - E_b}{R_a}$$
where $R_a$ is the armature winding resistance.

Physical Significance of Back-EMF as a Self-Regulating Governor:
Back-EMF makes the DC motor an inherently self-regulating machine:
1. At Starting ($N = 0$): Because speed is zero, $E_b = 0$. Since armature resistance $R_a$ is extremely small (typically $< 0.5\,\Omega$), the starting current is dangerously large: $I_{a(start)} = \frac{V}{R_a} \approx 10 \text{ to } 20 \times I_{a(FL)}$. This massive surge can burn the windings and damage the commutator, necessitating the use of an external 3-point or 4-point starter to insert current-limiting resistance during startup.
2. During Load Application: When mechanical load increases, the motor momentarily slows down ($N \downarrow$). Because $E_b \propto N$, back-EMF decreases ($E_b \downarrow$). This increases the voltage drop $(V - E_b)$, causing armature current $I_a = \frac{V - E_b}{R_a}$ to rise sharply. The increased current boosts electromagnetic torque ($T \propto \Phi I_a$) until motor torque balances the increased load torque at a slightly reduced speed. Conversely, if load is removed, the motor speeds up, $E_b$ rises, $I_a$ drops, and equilibrium is restored automatically.

Derivation of the DC Motor Armature Torque Equation:
Multiplying the armature voltage equation by $I_a$:
$$V I_a = E_b I_a + I_a^2 R_a$$
where:
- $V I_a$ is the total electrical power input to the armature.
- $I_a^2 R_a$ is the copper power loss dissipated as heat in armature resistance.
- $E_b I_a$ is the net electrical power converted into gross mechanical power:
$$P_m = E_b I_a$$
Mechanical power developed by a rotating shaft at angular velocity $\omega = \frac{2\pi N}{60}\text{ rad/s}$ under electromagnetic torque $T_a$ is:
$$P_m = T_a \cdot \omega = T_a \left( \frac{2\pi N}{60} \right)$$
Equating mechanical power to electrical power converted:
$$T_a \left( \frac{2\pi N}{60} \right) = E_b I_a$$
Substitute the back-EMF formula $E_b = \frac{\Phi Z N P}{60 A}$:
$$T_a \left( \frac{2\pi N}{60} \right) = \left( \frac{\Phi Z N P}{60 A} \right) I_a$$
Canceling the common factor $\frac{N}{60}$ from both sides:
$$T_a (2\pi) = \frac{\Phi Z P I_a}{A} \implies T_a = \frac{1}{2\pi} \left( \frac{P Z}{A} \right) \Phi I_a\text{ N}\cdot\text{m}$$
Evaluating the numerical constant $\frac{1}{2\pi} = \frac{1}{2 \times 3.14159} \approx 0.15915$:
$$T_a = 0.159 \left( \frac{P Z}{A} \right) \Phi I_a\text{ N}\cdot\text{m}$$
For a given manufactured machine, $P, Z,$ and $A$ are fixed constants ($K_t = \frac{P Z}{2\pi A}$), yielding the fundamental proportionality:
$$T_a \propto \Phi I_a$$

Speed Equation and Regulation:
From $E_b = \frac{\Phi Z N P}{60 A}$ and $E_b = V - I_a R_a$:
$$N = \frac{60 A}{P Z} \left( \frac{E_b}{\Phi} \right) = K \frac{V - I_a R_a}{\Phi} \implies N \propto \frac{E_b}{\Phi}$$
This proves that motor speed can be controlled smoothly by either varying the applied armature voltage $V$ (armature control below rated speed) or varying the field flux $\Phi$ (field weakening control above rated speed).
"""
        },
        {
            "qid": "beee-q14",
            "marks": 7,
            "type": "Long Derivation",
            "title": "Three-Phase AC Systems: Star and Delta Connections, Line vs Phase Relations, and Power Expression",
            "yt_query": "three phase star delta connection line phase voltage current relationship power derivation",
            "img_path": "images/beee/star_delta_phasors.png",
            "img_caption": "Figure 3.4: Balanced Star (Y) and Delta (Δ) Circuits with Phasor Relationship Geometries",
            "answer": r"""
Three-phase AC systems dominate worldwide electric power generation, transmission, and heavy industrial distribution due to compelling engineering advantages: constant instantaneous power delivery (no pulsating torque in polyphase motors), higher power transmission capacity per kilogram of conductor material, smaller generator frame sizes for identical ratings, and self-starting rotating magnetic fields.

Generation of Three-Phase Voltages:
A balanced three-phase generator has three identical coils displaced spatially by $120^\circ$ electrical degrees along the stator periphery. When rotated through a magnetic field, three sinusoidal voltages are induced of equal RMS magnitude ($V_{ph}$) and frequency, mutually displaced in time phase by $120^\circ$:
$$v_R(t) = \sqrt{2} V_{ph} \sin(\omega t)$$
$$v_Y(t) = \sqrt{2} V_{ph} \sin(\omega t - 120^\circ)$$
$$v_B(t) = \sqrt{2} V_{ph} \sin(\omega t - 240^\circ) = \sqrt{2} V_{ph} \sin(\omega t + 120^\circ)$$

1. Star (Wye, Y) Connected Balanced System:
In a star connection, similar terminals (finishes $R_2, Y_2, B_2$) of the three phase windings are joined together at a common junction called the Neutral Point ($N$). The remaining three terminals ($R_1, Y_1, B_1$) form the line conductors R, Y, and B.

Line vs Phase Current Relationship:
Because each line conductor is directly in series with its corresponding phase winding, the current flowing in the transmission line ($I_L$) is identically the current flowing in the phase winding ($I_{ph}$):
$$I_L = I_{ph}$$

Line vs Phase Voltage Derivation:
Phase voltages measured between lines and neutral are $\mathbf{V}_R = V_{ph} \angle 0^\circ$, $\mathbf{V}_Y = V_{ph} \angle -120^\circ$, and $\mathbf{V}_B = V_{ph} \angle 120^\circ$.
Line voltage $V_{RY}$ is the potential difference between line R and line Y:
$$\mathbf{V}_{RY} = \mathbf{V}_R - \mathbf{V}_Y = \mathbf{V}_R + (-\mathbf{V}_Y)$$
Phasor $-\mathbf{V}_Y$ has magnitude $V_{ph}$ oriented at $+60^\circ$ relative to $\mathbf{V}_R$.
The angle between $\mathbf{V}_R$ and $-\mathbf{V}_Y$ is exactly $60^\circ$.
Applying the parallelogram law of vector addition:
$$|\mathbf{V}_{RY}| = \sqrt{V_R^2 + V_Y^2 + 2 V_R V_Y \cos(60^\circ)}$$
Since $V_R = V_Y = V_{ph}$ and $\cos(60^\circ) = 0.5$:
$$V_L = \sqrt{V_{ph}^2 + V_{ph}^2 + 2 V_{ph}^2 (0.5)} = \sqrt{3 V_{ph}^2} = \sqrt{3} V_{ph}$$
Furthermore, the line voltage $\mathbf{V}_{RY}$ leads the phase voltage $\mathbf{V}_R$ by an angle:
$$\alpha = \tan^{-1}\left( \frac{V_{ph} \sin 60^\circ}{V_{ph} + V_{ph} \cos 60^\circ} \right) = \tan^{-1}\left( \frac{\frac{\sqrt{3}}{2}}{1 + \frac{1}{2}} \right) = \tan^{-1}\left(\frac{\sqrt{3}}{3}\right) = 30^\circ$$
Thus, in a balanced Star-connected system:
$$V_L = \sqrt{3} V_{ph} \approx 1.732 V_{ph}, \quad I_L = I_{ph}$$

2. Delta (Mesh, $\Delta$) Connected Balanced System:
In a delta connection, the three phase windings are connected end-to-end in a closed loop (start of one phase to finish of the preceding: $R_2$ to $Y_1$, $Y_2$ to $B_1$, $B_2$ to $R_1$).

Line vs Phase Voltage Relationship:
Because each line-to-line pair connects directly across one individual phase winding, the line voltage is identically equal to the phase voltage:
$$V_L = V_{ph}$$

Line vs Phase Current Derivation:
Applying KCL at node R:
$$\mathbf{I}_R = \mathbf{I}_{RY} - \mathbf{I}_{BR} = \mathbf{I}_{RY} + (-\mathbf{I}_{BR})$$
The angle between phase current $\mathbf{I}_{RY}$ and reversed current $-\mathbf{I}_{BR}$ is $60^\circ$.
By the parallelogram law of vectors:
$$I_L = \sqrt{I_{ph}^2 + I_{ph}^2 + 2 I_{ph}^2 \cos(60^\circ)} = \sqrt{3} I_{ph}$$
Thus, in a balanced Delta-connected system:
$$V_L = V_{ph}, \quad I_L = \sqrt{3} I_{ph} \approx 1.732 I_{ph}$$

Three-Phase Power Expression (Universal for both Star and Delta):
The total active real power $P$ consumed by a balanced 3-phase load is the sum of powers in all three phases:
$$P = 3 \times P_{ph} = 3 \times (V_{ph} I_{ph} \cos\phi)$$
For Star connection: substitute $V_{ph} = \frac{V_L}{\sqrt{3}}$ and $I_{ph} = I_L$:
$$P = 3 \times \left( \frac{V_L}{\sqrt{3}} \right) I_L \cos\phi = \sqrt{3} V_L I_L \cos\phi\text{ Watts}$$
For Delta connection: substitute $V_{ph} = V_L$ and $I_{ph} = \frac{I_L}{\sqrt{3}}$:
$$P = 3 \times V_L \left( \frac{I_L}{\sqrt{3}} \right) \cos\phi = \sqrt{3} V_L I_L \cos\phi\text{ Watts}$$
Similarly, total reactive power is $Q = \sqrt{3} V_L I_L \sin\phi\text{ VAR}$, and apparent power is $S = \sqrt{3} V_L I_L\text{ VA}$.
"""
        },
        {
            "qid": "beee-q15",
            "marks": 7,
            "type": "Short Answer",
            "title": "Domestic Electrical Installation: Distribution Board, Staircase Wiring, Earthing Methods, and Protective Devices",
            "yt_query": "residential distribution board staircase wiring pipe plate earthing mcb elcb fuse",
            "img_path": "images/beee/wiring_earthing_protective_devices.png",
            "img_caption": "Figure 3.5: Layout of Consumer Unit, Staircase Two-Way Control Schematic, and Pipe Earthing Installation",
            "answer": r"""
A safe, reliable domestic electrical installation distributes electric power from the utility service mains through systematic isolation, metering, sub-circuit branching, earthing, and overcurrent protection.

1. Layout of Residential Distribution Board (Consumer Unit):
Electrical energy enters a building via an overhead service drop or underground cable consisting of Phase (Live, $L$), Neutral ($N$), and Earth ($E$).
The sequence of equipment is:
1. Electricity Board Service Fuse and Neutral Link: Sealed high-rupturing capacity fuse protecting service cables.
2. Energy Meter: Calibrated kilowatt-hour (kWh) induction or smart digital meter recording total energy consumption.
3. Main Switch / Isolator: Double-pole switch (DPST, $32\text{ A}$ to $63\text{ A}$) that simultaneously disconnects both Phase and Neutral for complete maintenance isolation.
4. Earth Leakage Circuit Breaker (ELCB / RCCB): A high-sensitivity ($30\text{ mA}$ residual trip) device protecting human occupants against fatal electric shock.
5. Distribution Busbars and Miniature Circuit Breakers (MCBs): The live busbar feeds multiple branch sub-circuits protected by individual MCBs ($6\text{ A}$ for lighting/fan circuits, $16\text{ A} - 25\text{ A}$ for heavy appliances like air conditioners, geysers, and refrigerators). Neutral wires connect to an insulated common neutral busbar, and all bare green/yellow earth conductors terminate at a solid copper earth busbar.

2. Two-Way Control of a Lamp (Staircase Wiring):
Staircase wiring allows a single lamp to be turned ON or OFF independently from two separate locations (e.g., bottom and top of a staircase) using two Two-Way Single-Pole Double-Throw (SPDT) switches, designated as Switch $S_1$ and Switch $S_2$.
Each two-way switch has three terminals: a common central terminal ($C$) and two strapping traveler terminals ($T_1$ and $T_2$).
Wiring Connections:
The Phase wire from the AC supply is connected directly to the common terminal $C_1$ of switch $S_1$.
Traveler terminal $T_1$ of $S_1$ is strapped to traveler terminal $T_1$ of $S_2$.
Traveler terminal $T_2$ of $S_1$ is strapped to traveler terminal $T_2$ of $S_2$.
The common terminal $C_2$ of switch $S_2$ is connected to one terminal of the lamp socket.
The second terminal of the lamp is connected to the Neutral supply wire.

Operational Truth Table:
- State 1: Both switches up ($C_1 \to T_1$ and $C_2 \to T_1$). Circuit is closed; Lamp is **ON**.
- State 2: Switch 1 toggled down ($C_1 \to T_2$), Switch 2 stays up ($C_2 \to T_1$). Circuit is open; Lamp is **OFF**.
- State 3: Switch 1 down ($C_1 \to T_2$), Switch 2 toggled down ($C_2 \to T_2$). Circuit is closed; Lamp is **ON**.
- State 4: Switch 1 up ($C_1 \to T_1$), Switch 2 down ($C_2 \to T_2$). Circuit is open; Lamp is **OFF**.
Either switch can change the lamp state from dark to illuminated or vice versa.

3. Electrical Earthing (Necessity and Methods):
Earthing is the process of electrically bonding all non-current-carrying metallic enclosures of electrical equipment to the general mass of the earth via a low-resistance conducting path ($< 5\,\Omega$ for domestic, $< 1\,\Omega$ for substations). If an insulation breakdown occurs, touching the live metal frame causes a dangerous fault current to divert harmlessly through the low-resistance ground path rather than through the human body, immediately tripping protective fuses or MCBs.
- Pipe Earthing: A perforated galvanized iron (GI) pipe of diameter $38\text{ mm}$ and length $2.5\text{ m}$ is placed vertically in a permanently moist earth pit ($3\text{ m}$ to $4\text{ m}$ deep). The pipe is surrounded by alternating concentric layers of crushed charcoal (coke) and common salt ($15\text{ cm}$ thick) to enhance soil conductivity and retain moisture. A funnel with wire mesh is provided at the top for periodic water pouring during dry summer months.
- Plate Earthing: A copper plate ($60\text{ cm} \times 60\text{ cm} \times 3.18\text{ mm}$) or GI plate ($60\text{ cm} \times 60\text{ cm} \times 6.35\text{ mm}$) is buried vertically in an excavation at least $3\text{ m}$ deep, embedded in layers of charcoal and salt. A copper or GI earth lead is securely bolted to the plate with brazed brass bolts.

4. Comparison of Protective Devices:
- Rewirable / Cartridge Fuse: Employs a low-melting-point tin-lead alloy wire ($63\%\text{ Sn}, 37\%\text{ Pb}$) that melts via $I^2 R t$ Joule heating during sustained overcurrents or short circuits. Extremely cheap, but requires manual re-wiring, exhibits non-repeatable clearing times, and risks fire hazards from improper wire gauge replacement.
- Miniature Circuit Breaker (MCB): An electromechanical switching device that automatically interrupts fault currents. It utilizes an internal bimetallic strip for inverse-time thermal overload protection and an electromagnetic solenoid for instantaneous (sub-$10\text{ ms}$) magnetic short-circuit tripping. MCBs can be reset immediately by flipping a toggle switch, guarantee precision calibration, and prevent single-phasing.
- Earth Leakage Circuit Breaker (ELCB) / Residual Current Circuit Breaker (RCCB): Protects specifically against earth leakage faults and electrocution. It incorporates a Core Balance Current Transformer (CBCT) through which Phase and Neutral conductors pass. Under normal conditions, $I_L + I_N = 0$, producing zero net magnetic flux. If an insulation failure causes leakage to ground, the current imbalance ($I_{residual} = I_L - I_N > 30\text{ mA}$) induces an EMF in the sensing coil, energizing a polarized relay to unlatch the circuit within $20\text{ ms}$ to $40\text{ ms}$, saving human life.
"""
        }
    ]
}
