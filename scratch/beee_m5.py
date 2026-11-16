# -*- coding: utf-8 -*-
"""
Module 5 for Basics of Electrical & Electronics Engineering (EST130 / BEEE)
Operational Amplifiers & Digital Electronics
KTU 2019 Scheme Electrical & Electronics Engineering
"""

MODULE_5 = {
    "module_id": "beee-m5",
    "module_num": "Module 5",
    "module_title": "Operational Amplifiers & Digital Electronics",
    "questions": [
        {
            "qid": "beee-q21",
            "marks": 5,
            "type": "Short Answer",
            "title": "Operational Amplifier (Op-Amp): Architecture, IC 741 Pinout, Ideal Parameters, and Virtual Ground",
            "yt_query": "op amp internal architecture ic 741 pinout ideal characteristics virtual ground concept",
            "img_path": "images/beee/opamp_internal_and_pinout.png",
            "img_caption": "Figure 5.1: Op-Amp Four-Stage Block Architecture, IC 741 8-Pin DIP Layout, and Virtual Short",
            "answer": r"""
An Operational Amplifier (Op-Amp) is a direct-coupled, high-gain, integrated differential voltage amplifier capable of performing a wide spectrum of mathematical analog operations (addition, subtraction, integration, differentiation, and logarithmic scaling).

1. Internal Block Architecture of an Op-Amp:
Internally, a standard IC op-amp consists of four cascaded functional stages:
1. Input Differential Stage: A dual-input, balanced-output differential amplifier. It provides high differential voltage gain, very high input impedance, and high Common-Mode Rejection Ratio (CMRR).
2. Intermediate High-Gain Stage: A second differential or common-emitter amplifier stage that provides the bulk of overall open-loop voltage amplification ($A_{OL} \sim 10^5$).
3. Level-Shifter Stage: Because the preceding stages are direct-coupled, the DC quiescent voltage drifts above ground. An emitter follower or complementary transistor level shifter steps down the DC bias level to exactly zero volts relative to ground under quiescent zero-input conditions.
4. Output Buffer Stage: A Class-AB complementary push-pull emitter follower amplifier. It provides very low output impedance ($< 75\,\Omega$), high output current drive capability, and large output voltage swings without crossover distortion.

2. Pin Configuration of 8-Pin Dual-in-Line Package (DIP) IC 741:
- Pin 1: Offset Null (used with external potentiometer to balance input differential pair).
- Pin 2: Inverting Input ($V_-$ or $In^-$).
- Pin 3: Non-Inverting Input ($V_+$ or $In^+$).
- Pin 4: Negative DC Power Supply ($V_{EE} = -15\text{ V}$).
- Pin 5: Offset Null (second terminal of balance network).
- Pin 6: Output Terminal ($V_{out}$).
- Pin 7: Positive DC Power Supply ($V_{CC} = +15\text{ V}$).
- Pin 8: No Connection (NC).

3. Comparison of Ideal versus Practical (IC 741) Characteristics:
- Open-Loop Voltage Gain ($A_{OL}$): Ideal is $\infty$; Practical IC 741 is $2 \times 10^5$ ($106\text{ dB}$).
- Input Impedance ($R_{in}$): Ideal is $\infty$; Practical IC 741 is $2\text{ M}\Omega$ (BJT input) or $> 10^{12}\,\Omega$ (FET input).
- Output Impedance ($R_{out}$): Ideal is $0\,\Omega$; Practical IC 741 is $75\,\Omega$.
- Bandwidth ($BW$): Ideal is $\infty$ (amplifies from DC to $\infty\text{ Hz}$); Practical unity-gain bandwidth ($UGB$) is $1\text{ MHz}$.
- Common-Mode Rejection Ratio ($CMRR$): Ideal is $\infty$; Practical IC 741 is $90\text{ dB}$.
- Slew Rate ($SR$): Ideal is $\infty\text{ V/}\mu\text{s}$; Practical IC 741 is $0.5\text{ V/}\mu\text{s}$.
- Input Offset Voltage ($V_{os}$): Ideal is $0\text{ V}$; Practical IC 741 is $1\text{ to } 5\text{ mV}$.

4. Concept of Virtual Ground and Virtual Short:
Consider an op-amp operating with negative feedback in a linear closed-loop circuit. The output voltage is governed by the differential input:
$$V_{out} = A_{OL}(V_+ - V_-)$$
Solving for the differential input voltage $V_d = V_+ - V_-$:
$$V_d = V_+ - V_- = \frac{V_{out}}{A_{OL}}$$
Because the op-amp output is physically clamped between its DC supply rails (typically $-15\text{ V} \le V_{out} \le +15\text{ V}$), the numerator is finite (e.g., $10\text{ V}$).
For an ideal op-amp, the open-loop gain is infinite ($A_{OL} \to \infty$):
$$V_+ - V_- = \lim_{A_{OL} \to \infty} \frac{V_{out}}{A_{OL}} = 0 \implies V_+ = V_-$$
This equality is known as the **Virtual Short** principle: negative feedback forces the inverting terminal potential ($V_-$) to track the non-inverting terminal potential ($V_+$) identically, as though they were short-circuited together.
Furthermore, because the ideal input impedance is infinite ($R_{in} = \infty$), zero physical current can enter either input terminal:
$$I_+ = I_- = 0\text{ A}$$
If the non-inverting terminal is connected directly to ground ($V_+ = 0\text{ V}$), the virtual short condition forces the inverting terminal to also sit at zero potential:
$$V_- = V_+ = 0\text{ V}$$
The inverting node behaves as if it is grounded, yet no physical connection to ground exists and no current flows to ground from that node. This profound property is termed the **Virtual Ground**.
"""
        },
        {
            "qid": "beee-q22",
            "marks": 7,
            "type": "Long Derivation",
            "title": "Inverting, Non-Inverting, and Voltage Follower Op-Amp Configurations: Closed-Loop Gain Derivations",
            "yt_query": "inverting non inverting amplifier derivation voltage follower op amp closed loop gain",
            "img_path": "images/beee/inverting_noninverting_circuits.png",
            "img_caption": "Figure 5.2: Inverting, Non-Inverting, and Voltage Follower Closed-Loop Configurations",
            "answer": r"""
Applying negative feedback through passive resistors around an operational amplifier stabilizes the closed-loop voltage gain, eliminates distortion, broadens bandwidth, and makes performance completely independent of op-amp internal parameter variations.

1. Inverting Amplifier Configuration:
In the inverting amplifier, input signal $V_{in}$ is fed to the inverting terminal through input resistor $R_1$, feedback resistor $R_f$ is connected between output $V_{out}$ and the inverting terminal, and the non-inverting terminal is connected directly to ground ($V_+ = 0\text{ V}$).

Derivation of Closed-Loop Voltage Gain ($A_{v(inv)}$):
By the virtual ground principle:
$$V_- = V_+ = 0\text{ V}$$
Because ideal op-amp input impedance is infinite, the current entering the inverting terminal is zero ($I_- = 0$).
Applying Kirchhoff's Current Law at the inverting node (Node 2):
$$\sum I = 0 \implies I_1 = I_f$$
where $I_1$ is current entering through $R_1$, and $I_f$ is current leaving through $R_f$.
Expressing currents in terms of node potentials via Ohm's law:
$$I_1 = \frac{V_{in} - V_-}{R_1} = \frac{V_{in} - 0}{R_1} = \frac{V_{in}}{R_1}$$
$$I_f = \frac{V_- - V_{out}}{R_f} = \frac{0 - V_{out}}{R_f} = -\frac{V_{out}}{R_f}$$
Equating both currents:
$$\frac{V_{in}}{R_1} = -\frac{V_{out}}{R_f} \implies V_{out} = -\left( \frac{R_f}{R_1} \right) V_{in}$$
The closed-loop voltage gain is:
$$A_v = \frac{V_{out}}{V_{in}} = -\frac{R_f}{R_1}$$
The negative sign indicates that the output signal undergoes an exact $180^\circ$ phase inversion relative to the input.
The input impedance of this configuration is $Z_{in} = R_1$ (since the node is at virtual ground).

2. Non-Inverting Amplifier Configuration:
In the non-inverting amplifier, input signal $V_{in}$ is applied directly to the non-inverting terminal ($V_+ = V_{in}$). Feedback resistor $R_f$ connects output $V_{out}$ to the inverting terminal, and resistor $R_1$ connects the inverting terminal to ground.

Derivation of Closed-Loop Voltage Gain ($A_{v(non-inv)}$):
By the virtual short principle, the inverting terminal tracks the input:
$$V_- = V_+ = V_{in}$$
Applying KCL at the inverting node:
$$I_1 = I_f$$
where $I_1$ flows from ground through $R_1$ toward the node, and $I_f$ flows from the node through $R_f$ to the output:
$$\frac{0 - V_-}{R_1} + \frac{V_{out} - V_-}{R_f} = 0 \implies \frac{V_{out} - V_-}{R_f} = \frac{V_-}{R_1}$$
Substituting $V_- = V_{in}$:
$$\frac{V_{out}}{R_f} - \frac{V_{in}}{R_f} = \frac{V_{in}}{R_1} \implies \frac{V_{out}}{R_f} = V_{in}\left( \frac{1}{R_1} + \frac{1}{R_f} \right)$$
Multiplying through by $R_f$:
$$V_{out} = V_{in}\left( \frac{R_f}{R_1} + 1 \right) = \left( 1 + \frac{R_f}{R_1} \right) V_{in}$$
The closed-loop voltage gain is:
$$A_v = \frac{V_{out}}{V_{in}} = 1 + \frac{R_f}{R_1}$$
Key observations:
1. The gain is strictly positive, meaning input and output signals are in phase ($0^\circ$ phase shift).
2. The gain is always strictly greater than or equal to unity ($A_v \ge 1$).
3. Because the input signal connects directly to the non-inverting gate, the input impedance is extraordinarily high: $Z_{in} \approx R_{in(opamp)}(1 + A_{OL}\beta) \sim 10^{10}\,\Omega$, drawing virtually zero current from the signal source.

3. Voltage Follower (Buffer / Unity-Gain Amplifier):
The voltage follower is a special limiting case of the non-inverting amplifier where feedback resistor is replaced by a direct short circuit ($R_f = 0\,\Omega$) and resistor $R_1$ is omitted ($R_1 = \infty\,\Omega$).
Substituting $R_f = 0$ into the non-inverting gain equation:
$$A_v = 1 + \frac{0}{\infty} = 1.0 \implies V_{out} = V_{in}$$
Physical Application:
Although the voltage gain is exactly unity ($0\text{ dB}$), the voltage follower is an indispensable circuit in analog systems. It possesses an extremely high input impedance ($> 10^9\,\Omega$) and an ultra-low output impedance ($< 0.1\,\Omega$). When placed between a high-impedance sensor (e.g., pH probe or piezoelectric crystal) and a low-impedance load, it acts as a perfect Isolation Buffer, completely eliminating loading effects and impedance mismatch errors.
"""
        },
        {
            "qid": "beee-q23",
            "marks": 7,
            "type": "Long Derivation",
            "title": "Op-Amp Applications: Summing Amplifier, Difference Amplifier, Integrator, and Differentiator",
            "yt_query": "op amp summing amplifier difference amplifier integrator differentiator derivation",
            "img_path": "images/beee/opamp_applications_math.png",
            "img_caption": "Figure 5.3: Schematic Circuits of Summing Amplifier, Difference Amplifier, Integrator, and Differentiator",
            "answer": r"""
The versatility of the operational amplifier is demonstrated by its ability to execute precise mathematical operations through selected feedback networks.

1. Summing Amplifier (Inverting Adder):
A summing amplifier combines multiple independent input voltages ($V_1, V_2, V_3$) into a single output voltage. The non-inverting terminal is grounded ($V_+ = 0\text{ V}$). The input signals are fed through separate input resistors $R_1, R_2, R_3$ to the common inverting terminal, with a single feedback resistor $R_f$ connected from output to the inverting node.
By the virtual ground principle: $V_- = V_+ = 0\text{ V}$.
Applying KCL at the inverting summing junction:
$$I_1 + I_2 + I_3 = I_f$$
Expressing each current in terms of node voltages:
$$\frac{V_1 - 0}{R_1} + \frac{V_2 - 0}{R_2} + \frac{V_3 - 0}{R_3} = \frac{0 - V_{out}}{R_f}$$
$$\frac{V_1}{R_1} + \frac{V_2}{R_2} + \frac{V_3}{R_3} = -\frac{V_{out}}{R_f}$$
Solving for output voltage $V_{out}$:
$$V_{out} = -\left[ \left(\frac{R_f}{R_1}\right)V_1 + \left(\frac{R_f}{R_2}\right)V_2 + \left(\frac{R_f}{R_3}\right)V_3 \right]$$
If all input resistors are chosen equal ($R_1 = R_2 = R_3 = R$):
$$V_{out} = -\frac{R_f}{R}(V_1 + V_2 + V_3)$$
If $R_f = R$, the circuit performs direct algebraic addition: $V_{out} = -(V_1 + V_2 + V_3)$.
If $R_f / R = 1/3$, the circuit computes the arithmetic average: $V_{out} = -\frac{V_1 + V_2 + V_3}{3}$.

2. Difference Amplifier (Subtractor):
A difference amplifier produces an output voltage proportional to the difference between two input voltages ($V_2$ applied to non-inverting branch, $V_1$ applied to inverting branch).
Resistor $R_1$ connects $V_1$ to the inverting input, with feedback resistor $R_f$ to output.
Resistor $R_2$ connects $V_2$ to the non-inverting input, with resistor $R_g$ to ground.
By voltage division at the non-inverting terminal:
$$V_+ = V_2 \left( \frac{R_g}{R_2 + R_g} \right)$$
By superposition or nodal analysis at the inverting terminal:
$$V_- = V_+ = V_2 \left( \frac{R_g}{R_2 + R_g} \right)$$
Applying KCL at the inverting node:
$$\frac{V_1 - V_-}{R_1} = \frac{V_- - V_{out}}{R_f} \implies V_{out} = V_-\left( 1 + \frac{R_f}{R_1} \right) - V_1\left( \frac{R_f}{R_1} \right)$$
Choosing balanced resistor ratios: $\frac{R_f}{R_1} = \frac{R_g}{R_2}$:
$$V_{out} = \frac{R_f}{R_1}(V_2 - V_1)$$
The circuit rejects common-mode noise and amplifies strictly the differential signal.

3. Op-Amp Integrator:
An integrator produces an output voltage proportional to the time integral of the input voltage. An input resistor $R$ connects $V_{in}(t)$ to the inverting node, while a capacitor $C$ replaces the feedback resistor. Non-inverting terminal is grounded ($V_+ = 0\text{ V}$).
By virtual ground: $V_- = 0\text{ V}$.
The input current flowing through resistor $R$ is:
$$i(t) = \frac{V_{in}(t) - 0}{R} = \frac{V_{in}(t)}{R}$$
Because $I_- = 0$, this exact current must charge the feedback capacitor:
$$i(t) = C \frac{d V_C(t)}{dt} = C \frac{d(0 - V_{out}(t))}{dt} = -C \frac{d V_{out}(t)}{dt}$$
Equating both expressions:
$$\frac{V_{in}(t)}{R} = -C \frac{d V_{out}(t)}{dt} \implies \frac{d V_{out}(t)}{dt} = -\frac{1}{R C} V_{in}(t)$$
Integrating both sides with respect to time from $t = 0$ to $t$:
$$V_{out}(t) = -\frac{1}{R C} \int_{0}^{t} V_{in}(\tau)\,d\tau + V_{out}(0)$$
where $R C = \tau$ is the integrator time constant.
If input is a DC step of $+V$, the output ramps down linearly with slope $-V / RC$. If input is a square wave, output is a triangular wave.
Practical Limitation: At DC ($f = 0$), capacitor impedance is infinite ($X_C \to \infty$). The op-amp operates in open loop, causing tiny input offset voltages to saturate the output to the supply rail. To stabilize DC gain, a large bleed resistor $R_f$ is placed in parallel with $C$.

4. Op-Amp Differentiator:
A differentiator produces an output proportional to the time rate of change of the input. Capacitor $C$ is placed at the input, and resistor $R$ is in the feedback path.
The current through capacitor $C$ is:
$$i(t) = C \frac{d(V_{in}(t) - 0)}{dt} = C \frac{d V_{in}(t)}{dt}$$
This current flows through feedback resistor $R$:
$$i(t) = \frac{0 - V_{out}(t)}{R} = -\frac{V_{out}(t)}{R}$$
Equating currents:
$$-\frac{V_{out}(t)}{R} = C \frac{d V_{in}(t)}{dt} \implies V_{out}(t) = -R C \frac{d V_{in}(t)}{dt}$$
If input is a triangular wave, output is a square wave.
Practical Limitation: The gain $|A_v| = \omega R C = 2\pi f R C$ increases linearly with frequency. Consequently, high-frequency sensor noise is massively amplified, destabilizing the amplifier. A small series resistor $R_1$ is added at the input to clamp high-frequency gain.
"""
        },
        {
            "qid": "beee-q24",
            "marks": 5,
            "type": "Numerical Problem",
            "title": "Digital Number Systems, Radix Conversions, 1's and 2's Complement Arithmetic",
            "yt_query": "number systems conversion decimal binary octal hexadecimal 2s complement subtraction",
            "img_path": "images/beee/number_systems_twos_complement.png",
            "img_caption": "Figure 5.4: Radix Conversion Pathways and Two's Complement Subtraction Flow",
            "answer": r"""
Digital computing systems process binary information where numbers are represented using positional notation with arbitrary radix (base) $r$:
$$N = \sum_{k=-m}^{n-1} d_k \cdot r^k$$
where $d_k \in \{0, 1, \dots, r-1\}$ represents the digit at position $k$.

1. Radix Conversion Demonstrations:
- Decimal to Binary Conversion:
Convert $(53.625)_{10}$ to binary:
Integer part (successive division by 2, recording remainders from bottom to top):
$53 \div 2 = 26$ remainder $1$ (LSB)
$26 \div 2 = 13$ remainder $0$
$13 \div 2 = 6$ remainder $1$
$6 \div 2 = 3$ remainder $0$
$3 \div 2 = 1$ remainder $1$
$1 \div 2 = 0$ remainder $1$ (MSB)
$$(53)_{10} = (110101)_2$$
Fractional part (successive multiplication by 2, recording integer bits top to bottom):
$0.625 \times 2 = 1.250 \implies \text{integer } 1$
$0.250 \times 2 = 0.500 \implies \text{integer } 0$
$0.500 \times 2 = 1.000 \implies \text{integer } 1$
$$(0.625)_{10} = (0.101)_2$$
Combining both parts:
$$(53.625)_{10} = (110101.101)_2$$

- Binary to Hexadecimal Conversion:
Group bits in sets of 4 from the binary point:
$$(0011 \; 0101 . 1010)_2 \implies 0011_2 = 3_{16}, \quad 0101_2 = 5_{16}, \quad 1010_2 = A_{16}$$
$$(53.625)_{10} = (35.A)_{16}$$

- Hexadecimal to Decimal Conversion:
Convert $(2F.8)_{16}$ to decimal:
$$(2F.8)_{16} = 2 \times 16^1 + 15 \times 16^0 + 8 \times 16^{-1} = 32 + 15 + 0.5 = (47.5)_{10}$$

2. Signed Number Representations:
In digital microprocessors, negative binary numbers are represented using three formats:
1. Sign-Magnitude: MSB is the sign bit ($0$ for positive, $1$ for negative), remaining bits represent absolute magnitude. Suffers from two distinct representations of zero ($+0$ and $-0$) and complex arithmetic hardware.
2. 1's Complement: Obtained by inverting every bit of the positive number ($0 \to 1, 1 \to 0$). Also contains dual zeros ($+0 = 0000_2, -0 = 1111_2$).
3. 2's Complement: Obtained by adding $1$ to the 1's complement:
$$\text{2's Complement} = \text{1's Complement} + 1$$
Advantages of 2's Complement:
1. Unique representation of zero ($00000000_2$).
2. Subtraction is performed seamlessly using standard adder circuits by computing $A - B = A + (\text{2's complement of } B)$.
3. An $n$-bit 2's complement system represents integers in the asymmetric range:
$$-2^{n-1} \le N \le +2^{n-1} - 1$$
For $8$ bits: $-128 \le N \le +127$.

3. Step-by-Step 2's Complement Subtraction Examples:
Case 1: Subtract smaller number from larger ($A - B$, where $A > B$).
Compute $(28)_{10} - (13)_{10}$ using 8-bit 2's complement:
$$(28)_{10} = 00011100_2$$
$$(13)_{10} = 00001101_2$$
Step 1: Find 2's complement of $B = 13$:
$$\text{1's complement of } 13 = 11110010_2$$
$$\text{2's complement of } 13 = 11110010 + 1 = 11110011_2$$
Step 2: Add $A$ and 2's complement of $B$:
$$\begin{array}{r@{\quad}l}
  00011100 & (28) \\
+ 11110011 & (-13) \\
\hline
(1)\,00001111 & (+15)
\end{array}$$
Step 3: Analyze End-Around Carry:
There is an end carry generated out of the MSB ($(1)$). In 2's complement arithmetic, an end carry indicates that the result is POSITIVE and already in true binary form. Discard the end carry:
$$\text{Result} = 00001111_2 = +(8 + 4 + 2 + 1) = +(15)_{10}$$

Case 2: Subtract larger number from smaller ($A - B$, where $A < B$).
Compute $(13)_{10} - (28)_{10}$ using 8-bit 2's complement:
$A = 00001101_2$, $B = 00011100_2$.
Step 1: 2's complement of $B = 28$:
$$\text{1's complement of } 28 = 11100011_2$$
$$\text{2's complement of } 28 = 11100011 + 1 = 11100100_2$$
Step 2: Add $A$ and 2's complement of $B$:
$$\begin{array}{r@{\quad}l}
  00001101 & (13) \\
+ 11100100 & (-28) \\
\hline
  11110001 &
\end{array}$$
Step 3: Analyze End Carry:
There is NO end carry. The absence of an end carry signifies that the answer is NEGATIVE and stored in 2's complement form.
To find the true magnitude, take the 2's complement of the result:
$$\text{1's complement of } 11110001 = 00001110_2$$
$$\text{2's complement} = 00001110 + 1 = 00001111_2 = 15_{10}$$
Affixing the negative sign gives the exact answer:
$$\text{Result} = -(15)_{10}$$
"""
        },
        {
            "qid": "beee-q25",
            "marks": 7,
            "type": "Short Answer",
            "title": "Logic Gates, Universal Gates Realizations, Boolean Theorems, and De Morgan's Laws",
            "yt_query": "logic gates universal gates nand nor realizations boolean algebra de morgans laws",
            "img_path": "images/beee/logic_gates_and_de_morgans.png",
            "img_caption": "Figure 5.5: Universal NAND/NOR Gate Synthesis and Truth Table Verification of De Morgan's Laws",
            "answer": r"""
Logic gates are fundamental electronic switching circuits that implement elementary Boolean logic operations on two-state binary variables ($0$ and $1$, representing low and high voltage levels).

1. Basic, Universal, and Exclusive Logic Gates:
- Basic Gates:
  - AND Gate: $Y = A \cdot B$. Output is $1$ only when all inputs are $1$.
  - OR Gate: $Y = A + B$. Output is $1$ when at least one input is $1$.
  - NOT Gate (Inverter): $Y = \bar{A}$. Inverts input logic level.
- Universal Gates:
  A universal gate is a logic gate that can implement any arbitrary Boolean function without requiring any other gate type. NAND and NOR are universal gates because all three elementary operations (NOT, AND, OR) can be synthesized exclusively from them.
  - NAND Gate: $Y = \overline{A \cdot B}$. Output is $0$ only when all inputs are $1$.
  - NOR Gate: $Y = \overline{A + B}$. Output is $1$ only when all inputs are $0$.
- Exclusive Gates:
  - XOR Gate (Exclusive-OR): $Y = A \oplus B = \bar{A} B + A \bar{B}$. Output is $1$ when inputs are different (odd parity detector).
  - XNOR Gate (Equivalence Gate): $Y = \overline{A \oplus B} = A B + \bar{A} \bar{B}$. Output is $1$ when inputs are identical.

2. Realization of Basic Gates using Universal NAND Gates:
1. NOT Gate from NAND: Connect both inputs of a NAND gate together:
$$Y = \overline{A \cdot A} = \bar{A}$$
Requires exactly 1 NAND gate.
2. AND Gate from NAND: Pass the output of a NAND gate through a NAND inverter:
$$Y = \overline{\overline{A \cdot B}} = A \cdot B$$
Requires exactly 2 NAND gates.
3. OR Gate from NAND: Invert each input using NAND inverters, then pass both inverted signals into a third NAND gate:
$$Y = \overline{\bar{A} \cdot \bar{B}} = \overline{\bar{A}} + \overline{\bar{B}} = A + B$$
Requires exactly 3 NAND gates.

3. Realization of Basic Gates using Universal NOR Gates:
1. NOT Gate from NOR: Tie both inputs together: $Y = \overline{A + A} = \bar{A}$ (1 NOR gate).
2. OR Gate from NOR: Invert the output of a NOR gate with a NOR inverter: $Y = \overline{\overline{A + B}} = A + B$ (2 NOR gates).
3. AND Gate from NOR: Invert inputs before applying to a third NOR gate: $Y = \overline{\bar{A} + \bar{B}} = A \cdot B$ (3 NOR gates).

4. De Morgan's Laws:
De Morgan's laws establish mathematical duality between the logical conjunction (AND) and disjunction (OR) operations, forming the primary mathematical tool for simplifying digital expressions.

First Law: The complement of a product (AND) of variables is equal to the sum (OR) of their individual complements:
$$\overline{A \cdot B} = \bar{A} + \bar{B}$$
Second Law: The complement of a sum (OR) of variables is equal to the product (AND) of their individual complements:
$$\overline{A + B} = \bar{A} \cdot \bar{B}$$

Truth Table Proof of De Morgan's Laws:
Consider all possible input combinations of binary variables $A$ and $B$:
$$\begin{array}{|c|c||c|c|c||c|c||c|c|}
\hline
A & B & \bar{A} & \bar{B} & A \cdot B & \overline{A \cdot B} & \bar{A} + \bar{B} & A + B & \overline{A + B} & \bar{A} \cdot \bar{B} \\
\hline
0 & 0 & 1 & 1 & 0 & 1 & 1 & 0 & 1 & 1 \\
0 & 1 & 1 & 0 & 0 & 1 & 1 & 1 & 0 & 0 \\
1 & 0 & 0 & 1 & 0 & 1 & 1 & 1 & 0 & 0 \\
1 & 1 & 0 & 0 & 1 & 0 & 0 & 1 & 0 & 0 \\
\hline
\end{array}$$
Inspection of the truth table confirms:
Column 6 ($\overline{A \cdot B}$) is identical to Column 7 ($\bar{A} + \bar{B}$), proving the First Law.
Column 9 ($\overline{A + B}$) is identical to Column 10 ($\bar{A} \cdot \bar{B}$), proving the Second Law.
In gate-level hardware, De Morgan's laws establish that a NAND gate is logically equivalent to a Bubbled OR gate, and a NOR gate is equivalent to a Bubbled AND gate.
"""
        },
        {
            "qid": "beee-q26",
            "marks": 7,
            "type": "Long Derivation",
            "title": "Combinational Logic Circuits: Half Adder and Full Adder Design, Truth Tables, K-Maps, and Hardware Realization",
            "yt_query": "combinational circuits half adder full adder truth table k map realization logic gates",
            "img_path": "images/beee/half_full_adder_logic.png",
            "img_caption": "Figure 5.6: Half Adder and Full Adder Logic Schematics with Two-Half-Adder Synthesis",
            "answer": r"""
Combinational logic circuits are digital networks whose instantaneous outputs depend strictly and solely on the present combination of input logic levels, with no memory elements (flip-flops) or internal feedback loops. Arithmetic adders form the core execution unit within the Arithmetic Logic Unit (ALU) of all digital microprocessors.

1. Half Adder:
A Half Adder is an arithmetic combinational circuit that computes the binary addition of two single-bit operands, $A$ and $B$, generating two outputs: Sum ($S$) and Carry ($C$).

Truth Table for Half Adder:
$$\begin{array}{|c|c||c|c|}
\hline
A & B & \text{Sum } (S) & \text{Carry } (C) \\
\hline
0 & 0 & 0 & 0 \\
0 & 1 & 1 & 0 \\
1 & 0 & 1 & 0 \\
1 & 1 & 0 & 1 \\
\hline
\end{array}$$

Boolean Expressions:
From the truth table:
Sum output $S$ is high when inputs are different:
$$S = \bar{A} B + A \bar{B} = A \oplus B$$
Carry output $C$ is high only when both inputs are simultaneously high:
$$C = A \cdot B$$
Hardware Implementation:
A Half Adder is constructed using exactly one 2-input XOR gate to generate the Sum bit $S$, and one 2-input AND gate to generate the Carry bit $C$.
Limitation: The Half Adder cannot accept an incoming carry bit generated from a preceding lower-significant bit stage. Hence, it can only be used for adding the least significant bit (LSB) position.

2. Full Adder:
A Full Adder is a combinational circuit that performs arithmetic addition of three one-bit inputs: two operand bits $A$ and $B$, and an incoming carry bit $C_{in}$ from the preceding lower-order bit position. It generates two outputs: Sum ($S$) and Carry Out ($C_{out}$).

Truth Table for Full Adder:
$$\begin{array}{|c|c|c||c|c|}
\hline
A & B & C_{in} & \text{Sum } (S) & \text{Carry Out } (C_{out}) \\
\hline
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 1 & 0 \\
0 & 1 & 0 & 1 & 0 \\
0 & 1 & 1 & 0 & 1 \\
1 & 0 & 0 & 1 & 0 \\
1 & 0 & 1 & 0 & 1 \\
1 & 1 & 0 & 0 & 1 \\
1 & 1 & 1 & 1 & 1 \\
\hline
\end{array}$$

Karnaugh Map (K-Map) Minimization:
- For Sum Output ($S$):
Minterms for $S$: $\sum m(1, 2, 4, 7)$.
In a 3-variable K-map, these minterms form a checkerboard pattern with no adjacent groupable cells:
$$S = \bar{A} \bar{B} C_{in} + \bar{A} B \bar{C}_{in} + A \bar{B} \bar{C}_{in} + A B C_{in}$$
Factoring terms:
$$S = C_{in}(\bar{A} \bar{B} + A B) + \bar{C}_{in}(\bar{A} B + A \bar{B})$$
Using identity $\overline{A \oplus B} = \bar{A} \bar{B} + A B$:
$$S = C_{in}(\overline{A \oplus B}) + \bar{C}_{in}(A \oplus B) = (A \oplus B) \oplus C_{in}$$
$$S = A \oplus B \oplus C_{in}$$

- For Carry Out ($C_{out}$):
Minterms for $C_{out}$: $\sum m(3, 5, 6, 7)$.
Group 1 (cells 3, 7): $B C_{in}$
Group 2 (cells 5, 7): $A C_{in}$
Group 3 (cells 6, 7): $A B$
Combining groups:
$$C_{out} = A B + B C_{in} + A C_{in} = A B + C_{in}(A + B)$$
Alternatively, in terms of XOR logic:
$$C_{out} = A B + C_{in}(A \oplus B)$$
Proof of equivalence:
$$A B + C_{in}(A \oplus B) = A B + C_{in}(\bar{A} B + A \bar{B}) = A B + \bar{A} B C_{in} + A \bar{B} C_{in}$$
$$= B(A + \bar{A} C_{in}) + A \bar{B} C_{in} = B(A + C_{in}) + A \bar{B} C_{in} = A B + B C_{in} + A C_{in}(\bar{B} + B) = A B + B C_{in} + A C_{in}$$

Realization of Full Adder Using Two Half Adders and an OR Gate:
Let Half Adder 1 (HA-1) have inputs $A$ and $B$:
$$S_1 = A \oplus B, \quad C_1 = A \cdot B$$
Let Half Adder 2 (HA-2) have inputs $S_1$ and $C_{in}$:
$$S_2 = S_1 \oplus C_{in} = (A \oplus B) \oplus C_{in} = S$$
$$C_2 = S_1 \cdot C_{in} = (A \oplus B) C_{in}$$
Combining the individual carries $C_1$ and $C_2$ through a final 2-input OR gate:
$$C_{out} = C_1 + C_2 = A B + (A \oplus B) C_{in}$$
This realization proves that a Full Adder is synthesized using exactly two 2-input XOR gates, two 2-input AND gates, and one 2-input OR gate.
"""
        }
    ]
}
