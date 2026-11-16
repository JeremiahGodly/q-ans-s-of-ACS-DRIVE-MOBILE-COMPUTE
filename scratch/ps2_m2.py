# -*- coding: utf-8 -*-
"""
Module 2 for Power System II (EET304)
Symmetrical Components and Unsymmetrical Faults
"""

M2_QUESTIONS = [
    {
        "qid": "ps2-q6",
        "marks": 3,
        "type": "Short Answer",
        "title": "Symmetrical Components Transformation, the a-Operator, and Complex Power Invariance",
        "yt_query": "symmetrical components fortescue theorem a operator power invariance",
        "img_path": "images/ps2/symmetrical_components_phasors.png",
        "img_caption": "Figure 2.1: Resolution of Unbalanced Three-Phase Phasors into Symmetrical Sequence Components",
        "answer": r"""
In 1918, Dr. C. L. Fortescue introduced the method of symmetrical components, which revolutionized the mathematical analysis of unbalanced polyphase electrical networks. Fortescue's Theorem states that any unbalanced set of $N$ related phase vectors can be uniquely decomposed into $N$ symmetrical components consisting of balanced systems of vectors.

For a three-phase power system with phase variables $V_a, V_b, V_c$, the phasors are resolved into three symmetrical sets:
1. Positive Sequence Components ($V_{a1}, V_{b1}, V_{c1}$): Balanced three-phase phasors of equal magnitude, displaced mutually by $120^\circ$, possessing the identical phase sequence ($a-b-c$) as the original system:
$$V_{b1} = a^2 V_{a1}, \quad V_{c1} = a V_{a1}$$
2. Negative Sequence Components ($V_{a2}, V_{b2}, V_{c2}$): Balanced three-phase phasors of equal magnitude, displaced by $120^\circ$, but possessing the reversed phase sequence ($a-c-b$):
$$V_{b2} = a V_{a2}, \quad V_{c2} = a^2 V_{a2}$$
3. Zero Sequence Components ($V_{a0}, V_{b0}, V_{c0}$): Three uniphase phasors of strictly equal magnitude and identical phase angle, displaced by $0^\circ$:
$$V_{a0} = V_{b0} = V_{c0}$$

The Complex Operator $a$:
The operator $a$ is a unit phasor defined by a counter-clockwise rotation of $120^\circ$ ($2\pi/3 \text{ radians}$) in the complex plane:
$$a = 1 \angle 120^\circ = e^{j 2\pi/3} = -\frac{1}{2} + j \frac{\sqrt{3}}{2} = -0.5 + j 0.866$$
$$a^2 = 1 \angle 240^\circ = 1 \angle -120^\circ = -\frac{1}{2} - j \frac{\sqrt{3}}{2} = -0.5 - j 0.866$$
$$a^3 = 1 \angle 360^\circ = 1 \angle 0^\circ = 1$$
Fundamental identities of the $a$-operator include:
$$1 + a + a^2 = 1 + (-0.5 + j0.866) + (-0.5 - j0.866) = 0$$
$$a - a^2 = (-0.5 + j0.866) - (-0.5 - j0.866) = j\sqrt{3} = \sqrt{3}\angle 90^\circ$$
$$a^2 - a = -j\sqrt{3} = \sqrt{3}\angle -90^\circ$$

Transformation Matrices:
Expressing the phase voltages as the superposition of sequence components:
$$V_a = V_{a0} + V_{a1} + V_{a2}$$
$$V_b = V_{b0} + V_{b1} + V_{b2} = V_{a0} + a^2 V_{a1} + a V_{a2}$$
$$V_c = V_{c0} + V_{c1} + V_{c2} = V_{a0} + a V_{a1} + a^2 V_{a2}$$
In vector-matrix form:
$$\begin{bmatrix} V_a \\ V_b \\ V_c \end{bmatrix} = \begin{bmatrix} 1 & 1 & 1 \\ 1 & a^2 & a \\ 1 & a & a^2 \end{bmatrix} \begin{bmatrix} V_{a0} \\ V_{a1} \\ V_{a2} \end{bmatrix} \implies V_{abc} = A V_{012}$$
where $A$ is the symmetrical component transformation matrix.
Inverting matrix $A$ yields the symmetrical component sequence extraction matrix:
$$V_{012} = A^{-1} V_{abc} = \frac{1}{3} \begin{bmatrix} 1 & 1 & 1 \\ 1 & a & a^2 \\ 1 & a^2 & a \end{bmatrix} \begin{bmatrix} V_a \\ V_b \\ V_c \end{bmatrix}$$
Identical transformation matrices apply to phase and sequence currents ($I_{abc} = A I_{012}$).

Invariance of Complex Power:
Total three-phase complex power is $S_{3\phi} = V_{abc}^T I_{abc}^*$. Substituting $V_{abc} = A V_{012}$ and $I_{abc}^* = (A I_{012})^* = A^* I_{012}^*$:
$$S_{3\phi} = (A V_{012})^T (A^* I_{012}^*) = V_{012}^T (A^T A^*) I_{012}^*$$
Evaluating $A^T A^*$:
$$A^T A^* = \begin{bmatrix} 1 & 1 & 1 \\ 1 & a^2 & a \\ 1 & a & a^2 \end{bmatrix} \begin{bmatrix} 1 & 1 & 1 \\ 1 & a & a^2 \\ 1 & a^2 & a \end{bmatrix} = \begin{bmatrix} 3 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 3 \end{bmatrix} = 3 I$$
Therefore, the total three-phase complex power expressed in symmetrical components is:
$$S_{3\phi} = 3 \left( V_{a0} I_{a0}^* + V_{a1} I_{a1}^* + V_{a2} I_{a2}^* \right)$$
This proves that complex power can be evaluated independently in the three decoupled sequence networks and summed with a scaling factor of 3.
"""
    },
    {
        "qid": "ps2-q7",
        "marks": 7,
        "type": "Long Derivation",
        "title": "Sequence Networks and Impedances of Power System Equipment",
        "yt_query": "sequence networks synchronous generator transformer transmission line power systems",
        "img_path": "images/ps2/sequence_networks_equipment.png",
        "img_caption": "Figure 2.2: Sequence Networks for Synchronous Generator, Transformer Core Types, and Ground Connections",
        "answer": r"""
To calculate unsymmetrical faults, power systems are transformed into three uncoupled single-phase sequence networks: the Positive-Sequence Network, the Negative-Sequence Network, and the Zero-Sequence Network. The physical characteristics and sequence impedances of the core equipment are formulated as follows:

1. Synchronous Generator:
- Positive Sequence Network: The rotor rotates synchronously in the identical direction as the positive-sequence stator MMF. The air-gap flux is stationary relative to the rotor field poles. Hence, the positive-sequence impedance is simply the machine reactance ($Z_1 = jX_d''$ or $jX_d'$). Because the generator produces balanced positive-sequence internal EMFs, an internal source $E_a$ is present:
$$V_{a1} = E_a - I_{a1} Z_1$$
- Negative Sequence Network: The negative-sequence stator currents set up a magnetic field rotating at synchronous speed in the direction opposite to rotor rotation. This field sweeps past the rotor at twice synchronous speed ($2\omega_s$), inducing high-frequency eddy currents in the damper bars and rotor surface. These eddy currents heavily choke the penetration of flux, yielding a small negative-sequence impedance ($Z_2 \approx j \frac{X_d'' + X_q''}{2}$). Because the machine generates no negative-sequence voltages, no internal EMF source exists:
$$V_{a2} = -I_{a2} Z_2$$
- Zero Sequence Network: Zero-sequence currents in the three stator phases are identical in magnitude and time phase ($I_{a0} = I_{b0} = I_{c0}$). The MMFs produced in the three spatially displaced windings cancel in the main air gap, producing no net fundamental air-gap flux. Only slot and end-turn leakage fluxes exist, resulting in a very small internal zero-sequence impedance $Z_{g0}$.
If the generator neutral is grounded through an impedance $Z_n$, the total current entering ground is $I_n = I_a + I_b + I_c = 3 I_{a0}$. The neutral potential with respect to ground is $V_n = -I_n Z_n = -3 I_{a0} Z_n$.
The phase-to-ground zero-sequence voltage drop is:
$$V_{a0} = -I_{a0} Z_{g0} - 3 I_{a0} Z_n = -I_{a0}(Z_{g0} + 3 Z_n) = -I_{a0} Z_0$$
Thus, the total zero-sequence impedance is:
$$Z_0 = Z_{g0} + 3 Z_n$$

2. Three-Phase Transformers:
Because a transformer is a static electromagnetic device, phase rotation does not affect core reluctance or leakage flux paths. Therefore:
$$Z_1 = Z_2 = Z_{leakage}$$
The Zero-Sequence Network of a transformer depends critically on its winding connections and neutral grounding:
- Core Rules for Zero Sequence Flow:
  1. Zero-sequence current can flow into a star ($Y$) winding if and only if the neutral is connected to ground. If ungrounded, zero-sequence current is physically blocked ($I_0 = 0$, open circuit).
  2. If the neutral is grounded through $Z_n$, an impedance $3Z_n$ is inserted in series with the leakage impedance.
  3. A delta ($\Delta$) winding provides a closed circulating path for zero-sequence currents ($I_{a0} + I_{b0} + I_{c0}$ circulate inside the delta mesh), but zero-sequence current cannot enter or leave the external line terminals. Thus, delta windings isolate zero-sequence currents between primary and secondary sides.
- Common Configurations:
  - Star Grounded - Delta ($Y_g - \Delta$): Zero-sequence current can flow from the power system into the $Y_g$ side and to ground; the $\Delta$ side forms a path to ground reference on the secondary, but isolates the secondary line terminals (shunt path to reference).
  - Star Grounded - Star Grounded ($Y_g - Y_g$): A complete through-path exists from primary lines to secondary lines, provided both neutrals are grounded and return paths exist.
  - Star Ungrounded - Delta ($Y - \Delta$): Open circuit on star side, shunt closed loop on delta side.
  - Delta - Delta ($\Delta - \Delta$): Both line terminals are completely open-circuited to zero-sequence current; circulating currents are confined within both delta meshes.

3. Transmission Lines:
For completely transposed overhead transmission lines, self impedance is $Z_s$ and mutual coupling between conductors is $Z_m$.
- Positive Sequence Impedance:
  $$Z_1 = Z_s - Z_m$$
- Negative Sequence Impedance:
  $$Z_2 = Z_s - Z_m = Z_1$$
- Zero Sequence Impedance: Zero-sequence currents return through the earth or ground wires. Due to high earth resistivity and large loop return distance:
  $$Z_0 = Z_s + 2 Z_m + 3 Z_e$$
In typical high-voltage lines, $Z_0$ is significantly larger than $Z_1$, usually in the ratio $Z_0 \approx 2.5 \text{ to } 3.5 \times Z_1$.
"""
    },
    {
        "qid": "ps2-q8",
        "marks": 7,
        "type": "Long Derivation",
        "title": "Single Line-to-Ground (LG) Fault Analysis: Sequence Interconnection and Derivation",
        "yt_query": "single line to ground fault derivation sequence network series connection power systems",
        "img_path": "images/ps2/lg_fault_sequence_connection.png",
        "img_caption": "Figure 2.3: Series Interconnection of Sequence Networks for Single Line-to-Ground Fault",
        "answer": r"""
The Single Line-to-Ground (LG) fault is by far the most frequent unsymmetrical fault in electrical power systems, accounting for approximately 70% to 80% of all system disturbances. It occurs when one phase conductor contacts the ground or a grounded tower structure, often initiated by lightning flashover or tree contact.

Consider a balanced three-phase synchronous generator operating with internal sequence voltages: positive-sequence source $E_a$, $E_b = a^2 E_a$, $E_c = a E_a$, with zero negative- and zero-sequence generated EMFs. Let an LG fault occur on phase $a$ through a fault impedance $Z_f$ to ground.

Step 1: Formulate the Physical Boundary Conditions at the Fault Point:
Because phases $b$ and $c$ are healthy and open-circuited at the fault point:
$$I_b = 0$$
$$I_c = 0$$
The terminal voltage of the faulted phase $a$ is dropped across the fault impedance:
$$V_a = I_a Z_f$$

Step 2: Determine Sequence Currents from Symmetrical Components:
Applying the inverse transformation $I_{012} = A^{-1} I_{abc}$:
$$\begin{bmatrix} I_{a0} \\ I_{a1} \\ I_{a2} \end{bmatrix} = \frac{1}{3} \begin{bmatrix} 1 & 1 & 1 \\ 1 & a & a^2 \\ 1 & a^2 & a \end{bmatrix} \begin{bmatrix} I_a \\ 0 \\ 0 \end{bmatrix}$$
Carrying out the matrix multiplication:
$$I_{a0} = \frac{1}{3}(I_a + 0 + 0) = \frac{1}{3} I_a$$
$$I_{a1} = \frac{1}{3}(I_a + a(0) + a^2(0)) = \frac{1}{3} I_a$$
$$I_{a2} = \frac{1}{3}(I_a + a^2(0) + a(0)) = \frac{1}{3} I_a$$
This yields the fundamental sequence current identity:
$$I_{a0} = I_{a1} = I_{a2} = \frac{1}{3} I_a$$
The physical fact that all three sequence currents are strictly identical in magnitude and phase indicates that the three sequence networks must be connected in Series!

Step 3: Relate Sequence Voltages and Sequence Currents:
The terminal sequence voltages expressed in terms of Thevenin sequence impedances are:
$$V_{a0} = -I_{a0} Z_0$$
$$V_{a1} = E_a - I_{a1} Z_1$$
$$V_{a2} = -I_{a2} Z_2$$

Step 4: Enforce the Voltage Boundary Condition:
Expressing the faulted phase voltage in terms of its sequence components:
$$V_a = V_{a0} + V_{a1} + V_{a2} = I_a Z_f$$
Substituting $I_a = 3 I_{a1}$:
$$V_{a0} + V_{a1} + V_{a2} = 3 I_{a1} Z_f$$
Substituting the sequence voltage expressions:
$$(-I_{a0} Z_0) + (E_a - I_{a1} Z_1) + (-I_{a2} Z_2) = 3 I_{a1} Z_f$$
Since $I_{a0} = I_{a2} = I_{a1}$:
$$-I_{a1} Z_0 + E_a - I_{a1} Z_1 - I_{a1} Z_2 = 3 I_{a1} Z_f$$
Rearranging terms to isolate $E_a$:
$$E_a = I_{a1} Z_1 + I_{a1} Z_2 + I_{a1} Z_0 + 3 I_{a1} Z_f = I_{a1} \left( Z_1 + Z_2 + Z_0 + 3 Z_f \right)$$
Solving explicitly for the sequence current $I_{a1}$:
$$I_{a1} = \frac{E_a}{Z_1 + Z_2 + Z_0 + 3 Z_f}$$

Step 5: Determine Total Fault Current:
The total physical fault current entering the ground is $I_f = I_a = 3 I_{a1}$:
$$I_f = I_a = \frac{3 E_a}{Z_1 + Z_2 + Z_0 + 3 Z_f}$$
For a bolted dead-ground fault ($Z_f = 0$):
$$I_f = \frac{3 E_a}{Z_1 + Z_2 + Z_0}$$

Sequence Network Interconnection:
To satisfy both $I_{a0} = I_{a1} = I_{a2}$ and $E_a - I_{a1}(Z_1 + Z_2 + Z_0 + 3Z_f) = 0$, the positive-, negative-, and zero-sequence Thevenin networks are connected in a single closed Series loop with an added impedance $3Z_f$ inserted in the return path.
"""
    },
    {
        "qid": "ps2-q9",
        "marks": 7,
        "type": "Long Derivation",
        "title": "Line-to-Line (LL) Fault Analysis: Sequence Interconnection and Derivation",
        "yt_query": "line to line fault derivation sequence network parallel connection power systems",
        "img_path": "images/ps2/ll_fault_sequence_connection.png",
        "img_caption": "Figure 2.4: Parallel Interconnection of Positive and Negative Sequence Networks for Line-to-Line Fault",
        "answer": r"""
A Line-to-Line (LL) fault occurs when two phase conductors make physical contact or become bridged by an electric arc without involving ground. LL faults represent approximately 15% of all power system faults.

Let a line-to-line fault occur between phases $b$ and $c$ through an arc fault impedance $Z_f$. The system is excited by positive-sequence internal EMF $E_a$.

Step 1: Formulate the Physical Boundary Conditions at the Fault Point:
1. Phase $a$ remains healthy and unfaulted:
$$I_a = 0$$
2. Because current flows out of phase $b$ directly into phase $c$ through impedance $Z_f$ with no connection to ground:
$$I_b = -I_c \implies I_b + I_c = 0$$
3. The potential difference between the faulted phases equals the voltage drop across $Z_f$:
$$V_b - V_c = I_b Z_f$$

Step 2: Evaluate Symmetrical Component Currents:
Using the inverse symmetrical component transformation:
- Zero sequence current:
$$I_{a0} = \frac{1}{3}(I_a + I_b + I_c) = \frac{1}{3}(0 + I_b - I_b) = 0$$
Because zero sequence current is identically zero, the zero-sequence network is completely open and inactive during an LL fault!
- Positive sequence current:
$$I_{a1} = \frac{1}{3}(I_a + a I_b + a^2 I_c) = \frac{1}{3}(0 + a I_b + a^2(-I_b)) = \frac{1}{3}(a - a^2) I_b$$
Using the operator identity $a - a^2 = j\sqrt{3}$:
$$I_{a1} = \frac{j\sqrt{3}}{3} I_b = \frac{j}{\sqrt{3}} I_b \implies I_b = \frac{\sqrt{3}}{j} I_{a1} = -j\sqrt{3} I_{a1}$$
- Negative sequence current:
$$I_{a2} = \frac{1}{3}(I_a + a^2 I_b + a I_c) = \frac{1}{3}(0 + a^2 I_b + a(-I_b)) = \frac{1}{3}(a^2 - a) I_b$$
Using $a^2 - a = -j\sqrt{3}$:
$$I_{a2} = -\frac{j\sqrt{3}}{3} I_b = -\frac{j}{\sqrt{3}} I_b = -I_{a1}$$
This establishes the vital sequence current relationship:
$$I_{a1} = -I_{a2}, \quad I_{a0} = 0$$

Step 3: Evaluate Sequence Voltage Relationship:
Expressing the phase voltages $V_b$ and $V_c$ in terms of sequence components:
$$V_b = V_{a0} + a^2 V_{a1} + a V_{a2}$$
$$V_c = V_{a0} + a V_{a1} + a^2 V_{a2}$$
Subtracting $V_c$ from $V_b$:
$$V_b - V_c = (a^2 - a) V_{a1} + (a - a^2) V_{a2} = (a^2 - a)(V_{a1} - V_{a2}) = -j\sqrt{3}(V_{a1} - V_{a2})$$
Equating this to the boundary condition $V_b - V_c = I_b Z_f = (-j\sqrt{3} I_{a1}) Z_f$:
$$-j\sqrt{3}(V_{a1} - V_{a2}) = -j\sqrt{3} I_{a1} Z_f$$
Dividing both sides by $-j\sqrt{3}$:
$$V_{a1} - V_{a2} = I_{a1} Z_f$$

Step 4: Solve for Sequence Currents and Fault Current:
Substituting the Thevenin voltage equations $V_{a1} = E_a - I_{a1} Z_1$ and $V_{a2} = -I_{a2} Z_2 = -(-I_{a1}) Z_2 = I_{a1} Z_2$:
$$(E_a - I_{a1} Z_1) - (I_{a1} Z_2) = I_{a1} Z_f$$
$$E_a = I_{a1} Z_1 + I_{a1} Z_2 + I_{a1} Z_f = I_{a1} (Z_1 + Z_2 + Z_f)$$
Solving for $I_{a1}$:
$$I_{a1} = \frac{E_a}{Z_1 + Z_2 + Z_f}$$
The physical fault current in phase $b$ is:
$$I_f = I_b = -j\sqrt{3} I_{a1} = \frac{-j\sqrt{3} E_a}{Z_1 + Z_2 + Z_f} = \frac{\sqrt{3} E_a}{Z_1 + Z_2 + Z_f} \angle -90^\circ$$
For a bolted dead-short fault ($Z_f = 0$):
$$I_f = \frac{\sqrt{3} E_a}{Z_1 + Z_2}$$
Assuming $Z_1 \approx Z_2$, the magnitude of line-to-line fault current is:
$$|I_{f, LL}| = \frac{\sqrt{3} E_a}{2 Z_1} = \frac{\sqrt{3}}{2} \left(\frac{E_a}{Z_1}\right) \approx 0.866 \times I_{f, 3\phi}$$
The line-to-line fault current is approximately 86.6% of the symmetrical three-phase fault current.

Sequence Network Interconnection:
Because $I_{a1} = -I_{a2}$ and $V_{a1} - V_{a2} = I_{a1} Z_f$, the positive-sequence network and negative-sequence network are connected in Parallel opposition through the fault impedance $Z_f$. The zero-sequence network remains completely disconnected.
"""
    },
    {
        "qid": "ps2-q10",
        "marks": 7,
        "type": "Long Derivation",
        "title": "Double Line-to-Ground (LLG) Fault Analysis: Sequence Interconnection and Derivation",
        "yt_query": "double line to ground fault derivation sequence network parallel connection power systems",
        "img_path": "images/ps2/llg_fault_sequence_connection.png",
        "img_caption": "Figure 2.5: Parallel Interconnection of All Three Sequence Networks for Double Line-to-Ground Fault",
        "answer": r"""
A Double Line-to-Ground (LLG) fault occurs when two phase conductors simultaneously contact each other and fall to ground, or when two phases contact a grounded metallic structure. LLG faults constitute roughly 10% of all power system faults.

Let the fault occur on phases $b$ and $c$ through a common ground impedance $Z_f$.

Step 1: Formulate the Physical Boundary Conditions at the Fault Point:
1. Phase $a$ is healthy and open-circuited:
$$I_a = 0$$
2. Phases $b$ and $c$ are tied together to ground through impedance $Z_f$:
$$V_b = V_c = (I_b + I_c) Z_f$$
For a bolted fault ($Z_f = 0$):
$$V_b = 0, \quad V_c = 0$$

Step 2: Symmetrical Component Voltage Relationships:
Using the inverse transformation $V_{012} = A^{-1} V_{abc}$ for $V_b = V_c$:
$$\begin{bmatrix} V_{a0} \\ V_{a1} \\ V_{a2} \end{bmatrix} = \frac{1}{3} \begin{bmatrix} 1 & 1 & 1 \\ 1 & a & a^2 \\ 1 & a^2 & a \end{bmatrix} \begin{bmatrix} V_a \\ V_b \\ V_b \end{bmatrix}$$
Evaluating sequence voltages:
$$V_{a0} = \frac{1}{3}(V_a + 2 V_b)$$
$$V_{a1} = \frac{1}{3}(V_a + (a + a^2) V_b) = \frac{1}{3}(V_a - V_b)$$
$$V_{a2} = \frac{1}{3}(V_a + (a^2 + a) V_b) = \frac{1}{3}(V_a - V_b)$$
Notice that:
$$V_{a1} = V_{a2}$$
For a bolted fault ($V_b = 0$):
$$V_{a0} = V_{a1} = V_{a2} = \frac{1}{3} V_a$$
When fault impedance $Z_f$ is present, the total ground return current is:
$$I_n = I_b + I_c = (I_a + I_b + I_c) = 3 I_{a0}$$
The voltage of the faulted phases with respect to true ground is:
$$V_b = V_c = 3 I_{a0} Z_f$$
Substituting this back yields the sequence voltage relation:
$$V_{a1} = V_{a2} = V_{a0} - 3 I_{a0} Z_f$$
This condition proves that the sequence voltages are identical across all three networks, mandating a Parallel Interconnection of positive, negative, and zero sequence networks!

Step 3: Current Boundary Condition in Sequence Domain:
Since $I_a = 0$:
$$I_a = I_{a0} + I_{a1} + I_{a2} = 0 \implies I_{a1} = -(I_{a2} + I_{a0})$$
This exactly matches Kirchhoff's Current Law at the parallel junction of the three networks.

Step 4: Solve for Sequence Currents and Total Fault Current:
Viewing the system from the positive-sequence source $E_a$, the negative-sequence impedance $Z_2$ and the modified zero-sequence impedance $(Z_0 + 3Z_f)$ appear in parallel:
$$Z_{parallel} = Z_2 \parallel (Z_0 + 3 Z_f) = \frac{Z_2 (Z_0 + 3 Z_f)}{Z_2 + Z_0 + 3 Z_f}$$
The positive-sequence current entering the parallel combination is:
$$I_{a1} = \frac{E_a}{Z_1 + Z_{parallel}} = \frac{E_a}{Z_1 + \frac{Z_2 (Z_0 + 3 Z_f)}{Z_2 + Z_0 + 3 Z_f}}$$

Using the current divider rule, the negative-sequence and zero-sequence currents are:
$$I_{a2} = -I_{a1} \left( \frac{Z_0 + 3 Z_f}{Z_2 + Z_0 + 3 Z_f} \right)$$
$$I_{a0} = -I_{a1} \left( \frac{Z_2}{Z_2 + Z_0 + 3 Z_f} \right)$$

Total Fault Current Entering Ground:
The total current flowing through the earth return path is:
$$I_f = I_b + I_c = 3 I_{a0} = -3 I_{a1} \left( \frac{Z_2}{Z_2 + Z_0 + 3 Z_f} \right)$$
For a bolted LLG fault ($Z_f = 0$):
$$I_{a1} = \frac{E_a}{Z_1 + \frac{Z_2 Z_0}{Z_2 + Z_0}}$$
$$I_f = 3 I_{a0} = -3 I_{a1} \left(\frac{Z_2}{Z_2 + Z_0}\right)$$

Sequence Network Interconnection:
The positive-sequence network, negative-sequence network, and zero-sequence network (with an additional branch $3Z_f$ in series with $Z_0$) are connected in Parallel across their respective sequence terminals.
"""
    }
]
