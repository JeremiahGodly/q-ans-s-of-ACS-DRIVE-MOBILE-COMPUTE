# -*- coding: utf-8 -*-
"""
Module 1 for Basics of Electrical & Electronics Engineering (EST130 / BEEE)
DC Circuits & Network Theorems
KTU 2019 Scheme Electrical & Electronics Engineering
"""

MODULE_1 = {
    "module_id": "beee-m1",
    "module_num": "Module 1",
    "module_title": "DC Circuits & Network Theorems",
    "questions": [
        {
            "qid": "beee-q1",
            "marks": 5,
            "type": "Short Answer",
            "title": "Kirchhoff's Laws (KCL & KVL), Sign Conventions, and Mesh/Nodal Formulation",
            "yt_query": "kirchhoff laws kcl kvl sign convention mesh nodal dc circuits",
            "img_path": "images/beee/kcl_kvl_conventions.png",
            "img_caption": "Figure 1.1: Kirchhoff's Current and Voltage Laws with Algebraic Sign Conventions",
            "answer": r"""
Kirchhoff's laws form the bedrock of electric circuit analysis, derived directly from the fundamental conservation laws of classical physics. Kirchhoff's Current Law (KCL) is a direct consequence of the principle of conservation of electric charge. It states that the algebraic sum of all electric currents entering and leaving any node (or junction) in an electrical network is identically zero at every instant of time:
$$\sum_{k=1}^{n} I_k = 0$$
In applying KCL, the standard sign convention designates currents directed toward the node as positive ($+I$) and currents directed away from the node as negative ($-I$), or equivalently, the total incoming current equals the total outgoing current:
$$\sum I_{\text{in}} = \sum I_{\text{out}}$$
Because an electrical node cannot accumulate or store electric charge over time, any charge arriving at a junction must immediately depart through the connected branches, guaranteeing strict charge conservation.

Kirchhoff's Voltage Law (KVL) is the circuit-theoretic expression of the law of conservation of energy. It states that the algebraic sum of all branch voltages (electromotive forces and potential differences across passive elements) around any closed loop or mesh in an electric network is identically zero:
$$\sum_{k=1}^{m} V_k = 0$$
When tracing a closed path clockwise or counterclockwise, a consistent potential sign convention must be maintained. Traversing an element from its negative terminal to its positive terminal represents a potential rise, which is assigned a positive algebraic sign ($+V$). Conversely, traversing from a positive terminal to a negative terminal corresponds to a potential drop, which is assigned a negative algebraic sign ($-V$). Across an ideal resistor of resistance $R$ carrying branch current $I$, the potential drop in the direction of assumed current flow is $-I R$, while traversing against the assumed current represents a potential rise of $+I R$.

In systematic circuit analysis, KVL forms the mathematical foundation of Mesh Current Analysis, where closed planar loops are assigned circulating mesh currents, generating a set of simultaneous linear algebraic equations in terms of loop impedances and source voltages:
$$\mathbf{R} \cdot \mathbf{I} = \mathbf{V}$$
Conversely, KCL forms the mathematical foundation of Nodal Voltage Analysis, where one node is designated as the reference datum (ground at $0\text{ V}$) and KCL equations are written at all remaining non-reference nodes in terms of node voltages and branch conductances:
$$\mathbf{G} \cdot \mathbf{V} = \mathbf{I}$$
Together with Ohm's law ($V = I R$), these two topological conservation laws allow the complete determination of all branch voltages, currents, and power distributions in any linear bilateral DC network.
"""
        },
        {
            "qid": "beee-q2",
            "marks": 7,
            "type": "Numerical Problem",
            "title": "Nodal Voltage Analysis with Independent Sources and the Supernode Concept",
            "yt_query": "nodal analysis supernode independent sources step by step solved example",
            "img_path": "images/beee/nodal_supernode_circuit.png",
            "img_caption": "Figure 1.2: DC Resistive Network Illustrating Standard Nodes and Supernode Boundary",
            "answer": r"""
Nodal voltage analysis provides an algorithmic, computationally efficient method to solve for all branch voltages and currents by expressing Kirchhoff's Current Law in terms of node potentials. In a circuit with $N$ principal nodes, one node is selected as the common reference datum ($0\text{ V}$), and the remaining $(N-1)$ node voltages are defined with respect to this datum. When an ideal independent or dependent voltage source is connected between two non-reference nodes, the current flowing through that voltage source branch cannot be determined directly from Ohm's law. To circumvent this singularity, the two nodes connected by the voltage source, along with the source itself, are enclosed within a generalized boundary called a Supernode.

To illustrate this method completely with rigorous step-by-step working, consider a standard university examination network consisting of three essential nodes plus a ground reference node. Let Node 0 be the ground reference ($V_0 = 0\text{ V}$). An independent voltage source of $V_s = 20\text{ V}$ is connected between Node 1 and Node 2 such that $V_1 - V_2 = 20\text{ V}$. An independent current source of $I_s = 5\text{ A}$ enters Node 1. Resistors are connected as follows: $R_1 = 4\,\Omega$ from Node 1 to ground, $R_2 = 2\,\Omega$ from Node 2 to Node 3, $R_3 = 8\,\Omega$ from Node 2 to ground, and $R_4 = 4\,\Omega$ from Node 3 to ground. A constant current source of $2\text{ A}$ is directed out of Node 3 into ground.

Step 1: Constraint Equation for the Supernode (formed by Node 1 and Node 2):
The independent $20\text{ V}$ source directly fixes the potential difference between Node 1 and Node 2:
$$V_1 - V_2 = 20 \implies V_1 = V_2 + 20$$

Step 2: KCL Equation at the Supernode (Nodes 1 and 2 combined):
Summing all currents leaving the supernode boundary:
$$\frac{V_1 - 0}{R_1} - 5 + \frac{V_2 - 0}{R_3} + \frac{V_2 - V_3}{R_2} = 0$$
Substituting the numerical component values $R_1 = 4\,\Omega$, $R_2 = 2\,\Omega$, and $R_3 = 8\,\Omega$:
$$\frac{V_1}{4} - 5 + \frac{V_2}{8} + \frac{V_2 - V_3}{2} = 0$$
Multiplying the entire equation by the common denominator $8$:
$$2 V_1 - 40 + V_2 + 4(V_2 - V_3) = 0 \implies 2 V_1 + 5 V_2 - 4 V_3 = 40$$
Substituting the constraint equation $V_1 = V_2 + 20$:
$$2(V_2 + 20) + 5 V_2 - 4 V_3 = 40 \implies 2 V_2 + 40 + 5 V_2 - 4 V_3 = 40$$
$$7 V_2 - 4 V_3 = 0 \implies V_3 = \frac{7}{4} V_2 = 1.75 V_2$$

Step 3: KCL Equation at Node 3:
Summing all currents leaving Node 3:
$$\frac{V_3 - V_2}{R_2} + \frac{V_3 - 0}{R_4} + 2 = 0$$
Substituting $R_2 = 2\,\Omega$ and $R_4 = 4\,\Omega$:
$$\frac{V_3 - V_2}{2} + \frac{V_3}{4} + 2 = 0$$
Multiplying through by $4$:
$$2(V_3 - V_2) + V_3 + 8 = 0 \implies -2 V_2 + 3 V_3 = -8$$

Step 4: Solving for Node Voltages:
Substitute $V_3 = 1.75 V_2$ into the Node 3 equation:
$$-2 V_2 + 3(1.75 V_2) = -8 \implies -2 V_2 + 5.25 V_2 = -8$$
$$3.25 V_2 = -8 \implies V_2 = -\frac{8}{3.25} = -\frac{32}{13} \approx -2.4615\text{ V}$$
Now calculate $V_1$ using the supernode constraint:
$$V_1 = V_2 + 20 = -2.4615 + 20 = +17.5385\text{ V}$$
Now calculate $V_3$:
$$V_3 = 1.75 V_2 = 1.75(-2.4615) = -4.3077\text{ V}$$

Step 5: Determining Branch Currents:
The current through the $4\,\Omega$ resistor connected to Node 1 is:
$$I_{R1} = \frac{V_1}{4} = \frac{17.5385}{4} = 4.3846\text{ A}$$
The current flowing from Node 2 to Node 3 through the $2\,\Omega$ resistor is:
$$I_{R2} = \frac{V_2 - V_3}{R_2} = \frac{-2.4615 - (-4.3077)}{2} = \frac{1.8462}{2} = 0.9231\text{ A}$$
The current through the $8\,\Omega$ resistor connected to Node 2 is:
$$I_{R3} = \frac{V_2}{8} = \frac{-2.4615}{8} = -0.3077\text{ A}$$
This rigorous calculation confirms that all node potentials and branch currents are uniquely determined by combining KCL with the supernode constraint.
"""
        },
        {
            "qid": "beee-q3",
            "marks": 7,
            "type": "Numerical Problem",
            "title": "Superposition Theorem: Statement, Principle, and Step-by-Step Multi-Source Solution",
            "yt_query": "superposition theorem solved numerical problems circuit analysis",
            "img_path": "images/beee/superposition_subcircuits.png",
            "img_caption": "Figure 1.3: Superposition Decomposition with Individual Source Contributions",
            "answer": r"""
The Superposition Theorem is a direct manifestation of mathematical linearity in electric networks containing bilateral linear circuit elements (resistors, inductors, and capacitors) and independent energy sources. The theorem states: In any linear bilateral electric network energized by two or more independent sources, the resultant voltage across or current through any circuit element is equal to the algebraic sum of the individual voltages or currents produced by each independent source acting alone, with all other independent sources deactivated (turned off).

To deactivate independent sources:
1. An ideal independent voltage source is deactivated by reducing its terminal potential difference to zero, which corresponds to replacing it with a short circuit ($V_s = 0\text{ V}$).
2. An ideal independent current source is deactivated by reducing its branch current to zero, which corresponds to replacing it with an open circuit ($I_s = 0\text{ A}$).
Dependent (controlled) sources cannot be deactivated; their control dependencies must remain fully active in every sub-circuit analysis. Furthermore, the superposition theorem applies strictly to linear quantities (voltages and currents) and cannot be applied directly to calculate power ($P = I^2 R$ or $P = V^2 / R$) because power is a quadratic, non-linear function of electrical state variables.

To demonstrate the full mathematical execution of the Superposition Theorem, consider the classic KTU university problem: Determine the current $I_L$ flowing from Node A to Node B through a load resistor $R_L = 6\,\Omega$ connected in a network energized simultaneously by a $V_1 = 30\text{ V}$ DC voltage source, a $V_2 = 18\text{ V}$ DC voltage source, and an independent current source $I_s = 3\text{ A}$. The circuit topology is as follows: Source $V_1 = 30\text{ V}$ is in series with resistor $R_1 = 3\,\Omega$ connected to Node A. Source $V_2 = 18\text{ V}$ is in series with resistor $R_2 = 6\,\Omega$ connected to Node A. Current source $I_s = 3\text{ A}$ is connected in parallel across the branch between Node A and Node B, directed into Node A. Resistor $R_L = 6\,\Omega$ is connected between Node A and Node B, and Node B is connected to the common ground reference ($0\text{ V}$).

Step 1: Response due to $V_1 = 30\text{ V}$ acting alone:
Deactivate $V_2$ (short circuit) and deactivate $I_s$ (open circuit).
At Node A, resistor $R_1 = 3\,\Omega$ connects to the $30\text{ V}$ source.
The other two parallel paths connected from Node A to ground are $R_2 = 6\,\Omega$ and $R_L = 6\,\Omega$.
The equivalent parallel resistance of $R_2$ and $R_L$ is:
$$R_{p1} = \frac{R_2 \cdot R_L}{R_2 + R_L} = \frac{6 \times 6}{6 + 6} = \frac{36}{12} = 3\,\Omega$$
The total equivalent resistance seen by the $30\text{ V}$ source is:
$$R_{eq1} = R_1 + R_{p1} = 3 + 3 = 6\,\Omega$$
The total current supplied by the $30\text{ V}$ source into Node A is:
$$I_{total1} = \frac{V_1}{R_{eq1}} = \frac{30}{6} = 5\text{ A}$$
By current division between identical parallel resistors $R_2 = 6\,\Omega$ and $R_L = 6\,\Omega$, the contribution of $V_1$ to the load current is:
$$I_L' = I_{total1} \left( \frac{R_2}{R_2 + R_L} \right) = 5 \times \frac{6}{6 + 6} = 5 \times 0.5 = 2.5\text{ A (flowing downwards)}$$

Step 2: Response due to $V_2 = 18\text{ V}$ acting alone:
Deactivate $V_1$ (short circuit) and deactivate $I_s$ (open circuit).
At Node A, resistor $R_2 = 6\,\Omega$ connects to the $18\text{ V}$ source.
The parallel paths from Node A to ground are $R_1 = 3\,\Omega$ and $R_L = 6\,\Omega$.
The equivalent parallel resistance of $R_1$ and $R_L$ is:
$$R_{p2} = \frac{R_1 \cdot R_L}{R_1 + R_L} = \frac{3 \times 6}{3 + 6} = \frac{18}{9} = 2\,\Omega$$
The total resistance seen by the $18\text{ V}$ source is:
$$R_{eq2} = R_2 + R_{p2} = 6 + 2 = 8\,\Omega$$
The total current supplied by source $V_2$ into Node A is:
$$I_{total2} = \frac{V_2}{R_{eq2}} = \frac{18}{8} = 2.25\text{ A}$$
By current division between $R_1 = 3\,\Omega$ and $R_L = 6\,\Omega$, the contribution of $V_2$ to the load current is:
$$I_L'' = I_{total2} \left( \frac{R_1}{R_1 + R_L} \right) = 2.25 \times \frac{3}{3 + 6} = 2.25 \times \frac{1}{3} = 0.75\text{ A (flowing downwards)}$$

Step 3: Response due to $I_s = 3\text{ A}$ acting alone:
Deactivate $V_1$ (short circuit to ground) and deactivate $V_2$ (short circuit to ground).
All three resistors $R_1 = 3\,\Omega$, $R_2 = 6\,\Omega$, and $R_L = 6\,\Omega$ are connected in parallel between Node A and Node B (ground).
The equivalent resistance of $R_1$ and $R_2$ in parallel is:
$$R_{12} = \frac{R_1 \cdot R_2}{R_1 + R_2} = \frac{3 \times 6}{3 + 6} = 2\,\Omega$$
The current source $I_s = 3\text{ A}$ pumps current directly into Node A, which divides between the parallel branch $R_{12} = 2\,\Omega$ and the load branch $R_L = 6\,\Omega$.
By current division, the current through $R_L$ is:
$$I_L''' = I_s \left( \frac{R_{12}}{R_{12} + R_L} \right) = 3 \times \frac{2}{2 + 6} = 3 \times \frac{2}{8} = 3 \times 0.25 = 0.75\text{ A (flowing downwards)}$$

Step 4: Algebraic Summation of Individual Responses:
Because all three component currents $I_L'$, $I_L''$, and $I_L'''$ flow in the identical direction (downwards from Node A to Node B):
$$I_L = I_L' + I_L'' + I_L''' = 2.5\text{ A} + 0.75\text{ A} + 0.75\text{ A} = 4.0\text{ A}$$
The final total load current flowing through $R_L = 6\,\Omega$ is exactly:
$$I_L = 4.0\text{ A}$$
"""
        },
        {
            "qid": "beee-q4",
            "marks": 7,
            "type": "Numerical Problem",
            "title": "Thevenin's and Norton's Theorems: Principles, Dual Equivalence, and Bridge Circuit Solution",
            "yt_query": "thevenins norton theorem bridge circuit solved step by step",
            "img_path": "images/beee/thevenin_norton_bridge.png",
            "img_caption": "Figure 1.4: Original Bridge Circuit and its Thevenin / Norton Equivalent Representations",
            "answer": r"""
Thevenin's and Norton's theorems provide powerful network reduction techniques that transform any complex, multi-source linear bilateral active network into an ultra-simple two-terminal equivalent circuit.

Thevenin's Theorem states: Any linear bilateral active two-terminal network containing resistance elements and energy sources can be completely replaced, as viewed from its load terminals A-B, by an equivalent circuit consisting of a single independent voltage source $V_{th}$ connected in series with an equivalent resistance $R_{th}$.
Here, $V_{th}$ (Thevenin voltage) is the open-circuit potential difference measured across terminals A-B when the load resistor is disconnected ($V_{th} = V_{oc}$).
$R_{th}$ (Thevenin resistance) is the equivalent input resistance seen looking back into terminals A-B with the load removed and all independent energy sources deactivated (voltage sources replaced by short circuits, current sources replaced by open circuits).

Norton's Theorem is the exact source-transformation dual of Thevenin's theorem. It states: Any linear bilateral active two-terminal network can be replaced, across terminals A-B, by an equivalent circuit consisting of a single independent current source $I_N$ connected in parallel with an equivalent resistance $R_N$.
Here, $I_N$ (Norton current) is the short-circuit current that flows when terminals A-B are bridged by a zero-resistance conductor ($I_N = I_{sc}$).
The Norton equivalent resistance is identical to the Thevenin equivalent resistance:
$$R_N = R_{th}$$
The algebraic bridge linking both theorems is Ohm's law:
$$V_{th} = I_N \cdot R_{th} \iff I_N = \frac{V_{th}}{R_{th}}$$

To illustrate the complete procedure, consider an unbalanced Wheatstone bridge network energized by a DC voltage source $V_s = 100\text{ V}$. The bridge branches are: Arm AC has $R_1 = 20\,\Omega$, Arm CB has $R_2 = 30\,\Omega$, Arm AD has $R_3 = 40\,\Omega$, and Arm DB has $R_4 = 10\,\Omega$. The source $100\text{ V}$ is connected across diagonal terminals A and B. A galvanometer or load resistor $R_L = 15\,\Omega$ is connected across the detector terminals C and D. We wish to determine the Thevenin and Norton equivalent circuits across terminals C-D, and calculate the current flowing through $R_L$.

Step 1: Determination of Thevenin Voltage $V_{th} = V_{CD(oc)}$:
Disconnect load resistor $R_L$ between terminals C and D.
Because terminals C and D are open-circuited, branch ACB and branch ADB act as two isolated parallel voltage dividers connected directly across the $100\text{ V}$ supply.
The potential of node C with respect to reference terminal B is:
$$V_C = V_s \left( \frac{R_2}{R_1 + R_2} \right) = 100 \times \left( \frac{30}{20 + 30} \right) = 100 \times \frac{30}{50} = 60\text{ V}$$
The potential of node D with respect to reference terminal B is:
$$V_D = V_s \left( \frac{R_4}{R_3 + R_4} \right) = 100 \times \left( \frac{10}{40 + 10} \right) = 100 \times \frac{10}{50} = 20\text{ V}$$
The open-circuit Thevenin voltage between terminals C and D is:
$$V_{th} = V_C - V_D = 60\text{ V} - 20\text{ V} = +40\text{ V}$$
with terminal C positive with respect to terminal D.

Step 2: Determination of Thevenin Resistance $R_{th}$:
Deactivate the independent voltage source $V_s = 100\text{ V}$ by replacing it with a short circuit between terminal A and terminal B.
Looking into terminals C and D:
Arm AC ($R_1 = 20\,\Omega$) and Arm CB ($R_2 = 30\,\Omega$) are now connected in parallel between terminal C and the common node A-B:
$$R_{p1} = \frac{R_1 \cdot R_2}{R_1 + R_2} = \frac{20 \times 30}{20 + 30} = \frac{600}{50} = 12\,\Omega$$
Similarly, Arm AD ($R_3 = 40\,\Omega$) and Arm DB ($R_4 = 10\,\Omega$) are connected in parallel between terminal D and the common node A-B:
$$R_{p2} = \frac{R_3 \cdot R_4}{R_3 + R_4} = \frac{40 \times 10}{40 + 10} = \frac{400}{50} = 8\,\Omega$$
The total Thevenin equivalent resistance between terminals C and D is the series combination of these two parallel pairs:
$$R_{th} = R_{p1} + R_{p2} = 12\,\Omega + 8\,\Omega = 20\,\Omega$$

Step 3: Norton Equivalent Representation:
The Norton equivalent resistance is:
$$R_N = R_{th} = 20\,\Omega$$
The Norton short-circuit current is:
$$I_N = \frac{V_{th}}{R_{th}} = \frac{40\text{ V}}{20\,\Omega} = 2.0\text{ A}$$

Step 4: Load Current and Power Calculation:
Reconnecting the load resistor $R_L = 15\,\Omega$ across the Thevenin equivalent terminals C-D:
$$I_L = \frac{V_{th}}{R_{th} + R_L} = \frac{40}{20 + 15} = \frac{40}{35} = \frac{8}{7} \approx 1.1429\text{ A}$$
Using the Norton equivalent circuit with current division:
$$I_L = I_N \left( \frac{R_N}{R_N + R_L} \right) = 2.0 \times \left( \frac{20}{20 + 15} \right) = 2.0 \times \frac{20}{35} = \frac{40}{35} \approx 1.1429\text{ A}$$
Both equivalent models yield identical physical results, confirming the theorem.
"""
        },
        {
            "qid": "beee-q5",
            "marks": 7,
            "type": "Long Derivation",
            "title": "Maximum Power Transfer Theorem: Mathematical Proof, Efficiency, and Numerical Verification",
            "yt_query": "maximum power transfer theorem proof derivation efficiency numerical problem",
            "img_path": "images/beee/mptt_derivation_curve.png",
            "img_caption": "Figure 1.5: Load Power versus Resistance Ratio Exhibiting Peak at R_L = R_th",
            "answer": r"""
The Maximum Power Transfer Theorem is of paramount importance in communication systems, instrumentation, and audio engineering, where the primary objective is to maximize the transfer of energy from a signal source to a load rather than maximizing transmission efficiency.

Statement:
The Maximum Power Transfer Theorem states that a linear bilateral active DC network delivers the maximum possible electrical power to a variable load resistance $R_L$ when the value of the load resistance is set exactly equal to the Thevenin equivalent resistance of the network as viewed from the load terminals:
$$R_L = R_{th}$$

Mathematical Proof:
Consider an active linear network replaced across its output terminals A-B by its Thevenin equivalent circuit comprising an open-circuit voltage $V_{th}$ and series internal resistance $R_{th}$. A variable load resistor $R_L$ is connected across terminals A-B.
The loop current flowing through the circuit is given by Ohm's law:
$$I_L = \frac{V_{th}}{R_{th} + R_L}$$
The active power dissipated in the load resistor is:
$$P_L = I_L^2 \cdot R_L = \left( \frac{V_{th}}{R_{th} + R_L} \right)^2 \cdot R_L = \frac{V_{th}^2 \cdot R_L}{(R_{th} + R_L)^2}$$
To find the value of $R_L$ that maximizes $P_L$, we differentiate $P_L$ with respect to the independent variable $R_L$ and set the first derivative to zero:
$$\frac{dP_L}{dR_L} = 0$$
Applying the quotient rule of differential calculus, $\frac{d}{dx}\left[\frac{u}{v}\right] = \frac{v \frac{du}{dx} - u \frac{dv}{dx}}{v^2}$:
Let $u = V_{th}^2 \cdot R_L \implies \frac{du}{dR_L} = V_{th}^2$
Let $v = (R_{th} + R_L)^2 \implies \frac{dv}{dR_L} = 2(R_{th} + R_L)$
Substituting into the quotient derivative:
$$\frac{dP_L}{dR_L} = \frac{(R_{th} + R_L)^2 \cdot V_{th}^2 - V_{th}^2 \cdot R_L \cdot 2(R_{th} + R_L)}{(R_{th} + R_L)^4}$$
Factoring out the non-zero common term $V_{th}^2 (R_{th} + R_L)$:
$$\frac{dP_L}{dR_L} = \frac{V_{th}^2 (R_{th} + R_L) \left[ (R_{th} + R_L) - 2 R_L \right]}{(R_{th} + R_L)^4} = \frac{V_{th}^2 (R_{th} - R_L)}{(R_{th} + R_L)^3}$$
Setting $\frac{dP_L}{dR_L} = 0$:
$$\frac{V_{th}^2 (R_{th} - R_L)}{(R_{th} + R_L)^3} = 0 \implies R_{th} - R_L = 0 \implies R_L = R_{th}$$
To confirm that this condition corresponds to a mathematical maximum and not a minimum, we verify the second derivative $\frac{d^2 P_L}{dR_L^2}$ at $R_L = R_{th}$:
$$\left. \frac{d^2 P_L}{dR_L^2} \right|_{R_L = R_{th}} = -\frac{V_{th}^2}{8 R_{th}^3} < 0$$
Because the second derivative is strictly negative, $R_L = R_{th}$ guarantees the global maximum power transfer.

Maximum Power Formula:
Substituting the condition $R_L = R_{th}$ back into the power expression:
$$P_{\max} = \frac{V_{th}^2 \cdot R_{th}}{(R_{th} + R_{th})^2} = \frac{V_{th}^2 \cdot R_{th}}{(2 R_{th})^2} = \frac{V_{th}^2 \cdot R_{th}}{4 R_{th}^2} = \frac{V_{th}^2}{4 R_{th}}$$

Efficiency Analysis:
At the maximum power condition, the total power supplied by the source is:
$$P_{total} = I_L^2 (R_{th} + R_L) = I_L^2 (2 R_{th}) = 2 P_{\max}$$
The electrical power transmission efficiency $\eta$ is:
$$\eta = \frac{P_L}{P_{total}} \times 100\% = \frac{I_L^2 R_L}{I_L^2 (R_{th} + R_L)} \times 100\% = \frac{R_{th}}{2 R_{th}} \times 100\% = 50\%$$
This proves that under maximum power transfer, exactly half ($50\%$) of the total energy generated by the source is dissipated as heat inside the source's own internal resistance $R_{th}$, while only $50\%$ reaches the load. For this reason, power utility transmission systems never operate at maximum power transfer, but instead operate at $R_L \gg R_{th}$ to achieve high transmission efficiencies exceeding $90\%$.

Worked Numerical Problem:
A DC source of $V_s = 60\text{ V}$ with internal resistance $R_1 = 12\,\Omega$ is connected across a bridge-T resistive network with series arm $R_2 = 8\,\Omega$ and parallel shunt arm $R_3 = 20\,\Omega$. Find the value of load resistance $R_L$ connected at the output terminals for maximum power transfer, and calculate the maximum power delivered.
First, determine $V_{th}$:
$$V_{th} = V_s \left( \frac{R_3}{R_1 + R_3} \right) = 60 \times \left( \frac{20}{12 + 20} \right) = 60 \times \frac{20}{32} = 37.5\text{ V}$$
Next, determine $R_{th}$ looking back from the output with $V_s$ short-circuited:
$$R_{th} = R_2 + (R_1 \parallel R_3) = 8 + \frac{12 \times 20}{12 + 20} = 8 + \frac{240}{32} = 8 + 7.5 = 15.5\,\Omega$$
For maximum power transfer, the load resistance must be set to:
$$R_L = R_{th} = 15.5\,\Omega$$
The maximum power delivered to $R_L$ is:
$$P_{\max} = \frac{V_{th}^2}{4 R_{th}} = \frac{(37.5)^2}{4 \times 15.5} = \frac{1406.25}{62} \approx 22.68\text{ W}$$
"""
        }
    ]
}
