# -*- coding: utf-8 -*-
"""
Content generator for Subject 10: Basics of Electrical & Electronics Engineering (EST130 / BEEE)
KTU 2019 Scheme Electrical & Electronics Engineering Comprehensive Question Bank.
All answers are written from the perspective of an experienced engineering professor:
clear, direct, mathematically rigorous, with step-by-step intermediate equations.
All strings are raw multiline strings (r'...' or r"...") to prevent LaTeX backslash corruption.
"""

BEEE_MODULES = [
    {
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
    },
    {
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
    },
    {
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
    },
    {
        "module_id": "beee-m4",
        "module_num": "Module 4",
        "module_title": "Semiconductor Electronics & BJTs",
        "questions": [
            {
                "qid": "beee-q16",
                "marks": 7,
                "type": "Short Answer",
                "title": "Semiconductor Physics, PN Junction Diode Formation, Biasing, and V-I Characteristics",
                "yt_query": "pn junction diode working forward reverse bias vi characteristics energy band",
                "img_path": "images/beee/pn_junction_characteristics.png",
                "img_caption": "Figure 4.1: Energy Band Diagram of PN Junction, Depletion Layer Formation, and Complete V-I Curve",
                "answer": r"""
    Semiconductors are materials whose electrical conductivity lies intermediate between metallic conductors ($\sigma \sim 10^7\text{ S/m}$) and electrical insulators ($\sigma < 10^{-10}\text{ S/m}$), characterized by an energy bandgap $E_g$ on the order of $1\text{ eV}$ ($E_g = 1.12\text{ eV}$ for Silicon, $0.67\text{ eV}$ for Germanium at room temperature).

    1. Intrinsic and Extrinsic Semiconductors:
    An intrinsic semiconductor is a chemically pure crystalline tetravalent semiconductor (such as Silicon or Germanium) with four valence electrons participating in covalent bonds. At absolute zero ($0\text{ K}$), all valence electrons are tightly bound in covalent lattices, rendering the material a perfect insulator. At room temperature ($300\text{ K}$), thermal energy breaks a small fraction of covalent bonds, generating equal concentrations of mobile conduction electrons in the conduction band and vacant electron states, termed 'holes', in the valence band:
    $$n_i = p_i = 1.5 \times 10^{16}\text{ m}^{-3}\text{ (for Silicon at } 300\text{ K)}$$
    Because intrinsic carrier concentrations are exceedingly low, pure semiconductors are doped with controlled impurities (doping ratio $\sim 1 : 10^6$) to produce extrinsic semiconductors:
    - N-Type Semiconductor: Formed by doping pure silicon with pentavalent donor impurities (Phosphorus, Arsenic, Antimony). Four valence electrons form covalent bonds, while the loosely bound fifth electron easily enters the conduction band at room temperature, donating a free electron and leaving behind an immobile, positively charged donor ion. Electrons are majority carriers ($n_n \approx N_D$), and holes are minority carriers ($p_n \approx n_i^2 / N_D$).
    - P-Type Semiconductor: Formed by doping with trivalent acceptor impurities (Boron, Gallium, Indium). Three valence electrons form bonds, leaving a vacant bond site that readily captures an adjacent electron, creating a mobile hole and an immobile, negatively charged acceptor ion. Holes are majority carriers ($p_p \approx N_A$), and electrons are minority carriers ($n_p \approx n_i^2 / N_A$).

    2. Formation of PN Junction and Depletion Region:
    When P-type and N-type regions are fabricated within a continuous single monocrystalline semiconductor wafer:
    A steep carrier concentration gradient exists across the metallurgical junction. Holes diffuse from the P-region into the N-region, while free electrons diffuse from the N-region into the P-region.
    Near the metallurgical interface, diffusing electrons and holes recombine and annihilate each other.
    This recombination uncovers uncompensated immobile ions in the crystal lattice: negatively charged acceptor ions ($-q$) on the P-side and positively charged donor ions ($+q$) on the N-side.
    This narrow space-charge layer, devoid of mobile charge carriers, is called the Depletion Region (or space-charge layer, typically $0.5\,\mu\text{m}$ to $1\,\mu\text{m}$ wide).
    The exposed donor and acceptor ions establish an internal built-in electric field $\mathbf{E}$ directed from the positive N-side to the negative P-side. This electric field drives a drift current of minority carriers that opposes further majority carrier diffusion.
    In thermal equilibrium with no external bias applied, the diffusion current exactly balances the drift current, resulting in net zero current. The line integral of the built-in electric field creates a contact potential difference called the Barrier Potential ($V_0$):
    $$V_0 = V_T \ln\left( \frac{N_A N_D}{n_i^2} \right)$$
    where $V_T = \frac{k T}{q}$ is the thermal voltage ($V_T \approx 26\text{ mV}$ at $300\text{ K}$). At room temperature, $V_0 \approx 0.7\text{ V}$ for Silicon and $V_0 \approx 0.3\text{ V}$ for Germanium.

    3. Biasing and V-I Characteristics:
    - Forward Bias: The external DC source connects with positive terminal to P-side and negative terminal to N-side. The applied voltage $V_F$ opposes the internal barrier potential, reducing the net junction potential to $(V_0 - V_F)$ and narrowing the depletion width. Once $V_F$ exceeds the Knee Voltage ($V_\gamma \approx 0.7\text{ V}$ for Si), the potential barrier is overcome, allowing majority carriers to inject across the junction en masse. Current rises exponentially according to the Shockley Diode Equation:
    $$I = I_0 \left( e^{\frac{V}{\eta V_T}} - 1 \right)$$
    where $I_0$ is the reverse saturation current ($10^{-12}\text{ A}$ to $10^{-9}\text{ A}$), and $\eta$ is the ideality factor ($\eta = 1$ for Ge, $\eta \approx 1 \text{ to } 2$ for Si).
    - Reverse Bias: The external source connects positive terminal to N-side and negative terminal to P-side. The applied reverse voltage $V_R$ reinforces the internal barrier potential, increasing the junction barrier to $(V_0 + V_R)$ and widening the depletion region. Majority carrier flow is completely blocked. Only thermally generated minority carriers (electrons in P-region, holes in N-region) are swept across the junction by the electric field, producing an extremely minute, temperature-dependent Reverse Saturation Current ($I_0$).
    The dynamic (AC) resistance of the diode under forward bias is:
    $$r_d = \frac{d V}{d I} = \frac{\eta V_T}{I + I_0} \approx \frac{26\text{ mV}}{I_F\text{ (mA)}}$$
    At $I_F = 10\text{ mA}$, $r_d = \frac{26}{10} = 2.6\,\Omega$, confirming high forward conductance.
    """
            },
            {
                "qid": "beee-q17",
                "marks": 7,
                "type": "Long Derivation",
                "title": "Half-Wave and Full-Wave Bridge Rectifiers: Operation, Derivations of V_dc, V_rms, Efficiency, and Ripple Factor",
                "yt_query": "half wave full wave bridge rectifier derivation vdc vrms efficiency ripple factor capacitor filter",
                "img_path": "images/beee/rectifier_topologies_waveforms.png",
                "img_caption": "Figure 4.2: Full-Wave Bridge Rectifier Circuit Diagram, Conduction Paths, and Output Waveforms",
                "answer": r"""
    Rectification is the process of converting bidirectional alternating current (AC) into unidirectional pulsating direct current (DC) using non-linear semiconductor diodes.

    1. Half-Wave Rectifier (HWR):
    A single diode is connected in series with an AC secondary voltage $v_s(\theta) = V_m \sin\theta$ and load resistor $R_L$.
    During the positive half-cycle ($0 \le \theta \le \pi$), the diode anode is positive relative to cathode; the diode forward biases (ON) and conducts current $i_L(\theta) = I_m \sin\theta$, where $I_m = \frac{V_m}{R_f + R_L} \approx \frac{V_m}{R_L}$.
    During the negative half-cycle ($\pi \le \theta \le 2\pi$), the diode is reverse biased (OFF), and $i_L(\theta) = 0$.

    Mathematical Derivations for HWR:
    - Average / DC Output Current and Voltage:
    $$I_{dc} = \frac{1}{2\pi} \int_{0}^{2\pi} i_L(\theta)\,d\theta = \frac{1}{2\pi} \int_{0}^{\pi} I_m \sin\theta\,d\theta = \frac{I_m}{2\pi} [-\cos\theta]_0^\pi = \frac{I_m}{2\pi}[1 - (-1)] = \frac{I_m}{\pi}$$
    $$V_{dc} = I_{dc} R_L = \frac{V_m}{\pi} \approx 0.318 V_m$$
    - RMS Load Current:
    $$I_{rms}^2 = \frac{1}{2\pi} \int_{0}^{\pi} I_m^2 \sin^2\theta\,d\theta = \frac{I_m^2}{4\pi} \int_{0}^{\pi} (1 - \cos 2\theta)\,d\theta = \frac{I_m^2}{4\pi}[\pi] = \frac{I_m^2}{4} \implies I_{rms} = \frac{I_m}{2}$$
    $$V_{rms} = \frac{V_m}{2} = 0.5 V_m$$
    - Rectification Efficiency ($\eta_{HWR}$):
    $$\eta = \frac{P_{dc}}{P_{ac}} = \frac{I_{dc}^2 R_L}{I_{rms}^2 (r_f + R_L)} \approx \frac{\left(\frac{I_m}{\pi}\right)^2 R_L}{\left(\frac{I_m}{2}\right)^2 R_L} = \frac{4}{\pi^2} = \frac{4}{9.8696} \approx 0.406 = 40.6\%$$
    - Ripple Factor ($\gamma_{HWR}$):
    $$\gamma = \sqrt{\left(\frac{I_{rms}}{I_{dc}}\right)^2 - 1} = \sqrt{\left(\frac{I_m / 2}{I_m / \pi}\right)^2 - 1} = \sqrt{\left(\frac{\pi}{2}\right)^2 - 1} = \sqrt{2.4674 - 1} = \sqrt{1.4674} \approx 1.21$$
    The Peak Inverse Voltage (PIV) rating of the diode is $V_m$.

    2. Full-Wave Bridge Rectifier (FWR):
    A bridge rectifier utilizes four diodes ($D_1, D_2, D_3, D_4$) arranged in a closed diamond network, eliminating the need for an expensive center-tapped transformer.
    - During the positive half-cycle ($0 \le \theta \le \pi$), terminal A is positive with respect to terminal B. Diodes $D_1$ and $D_3$ are forward biased and conduct load current from top to bottom through $R_L$, while $D_2$ and $D_4$ remain reverse biased.
    - During the negative half-cycle ($\pi \le \theta \le 2\pi$), terminal B is positive with respect to terminal A. Diodes $D_2$ and $D_4$ are forward biased and conduct current in the exact same downward direction through $R_L$, while $D_1$ and $D_3$ are reverse biased.
    Thus, load current is unidirectional over both half-cycles with period $\pi$.

    Mathematical Derivations for Full-Wave Rectifier:
    - Average / DC Output Current and Voltage:
    $$I_{dc} = \frac{1}{\pi} \int_{0}^{\pi} I_m \sin\theta\,d\theta = \frac{I_m}{\pi} [-\cos\theta]_0^\pi = \frac{2 I_m}{\pi}$$
    $$V_{dc} = I_{dc} R_L = \frac{2 V_m}{\pi} \approx 0.637 V_m$$
    - RMS Load Current and Voltage:
    $$I_{rms}^2 = \frac{1}{\pi} \int_{0}^{\pi} I_m^2 \sin^2\theta\,d\theta = \frac{I_m^2}{2\pi} \int_{0}^{\pi} (1 - \cos 2\theta)\,d\theta = \frac{I_m^2}{2\pi}[\pi] = \frac{I_m^2}{2} \implies I_{rms} = \frac{I_m}{\sqrt{2}}$$
    $$V_{rms} = \frac{V_m}{\sqrt{2}} \approx 0.707 V_m$$
    - Rectification Efficiency ($\eta_{FWR}$):
    $$\eta = \frac{P_{dc}}{P_{ac}} = \frac{I_{dc}^2 R_L}{I_{rms}^2 R_L} = \frac{\left(\frac{2 I_m}{\pi}\right)^2}{\left(\frac{I_m}{\sqrt{2}}\right)^2} = \frac{\frac{4 I_m^2}{\pi^2}}{\frac{I_m^2}{2}} = \frac{8}{\pi^2} = \frac{8}{9.8696} \approx 0.812 = 81.2\%$$
    - Ripple Factor ($\gamma_{FWR}$):
    $$\gamma = \sqrt{\left(\frac{I_{rms}}{I_{dc}}\right)^2 - 1} = \sqrt{\left(\frac{I_m / \sqrt{2}}{2 I_m / \pi}\right)^2 - 1} = \sqrt{\left(\frac{\pi}{2\sqrt{2}}\right)^2 - 1} = \sqrt{(1.11)^2 - 1} = \sqrt{1.2321 - 1} = \sqrt{0.2321} \approx 0.482$$
    For the bridge rectifier, Peak Inverse Voltage per diode is $PIV = V_m$ (compared to $2 V_m$ for a center-tapped rectifier).

    Shunt Capacitor Filter:
    To smooth out pulsating DC variations, a large electrolytic capacitor $C$ is connected in parallel with the load resistance $R_L$. During conduction, the capacitor charges rapidly to peak secondary voltage $V_m$. When the rectified voltage falls below the capacitor voltage, diodes turn off, and the capacitor discharges slowly through $R_L$ with long time constant $\tau = R_L C \gg T/2$.
    The approximate peak-to-peak ripple voltage and ripple factor for a full-wave rectifier with capacitor filter are:
    $$V_r = \frac{I_{dc}}{2 f C} = \frac{V_{dc}}{2 f R_L C}, \quad \gamma = \frac{V_{r(rms)}}{V_{dc}} = \frac{1}{4\sqrt{3} f C R_L}$$
    This equation shows that increasing capacitance $C$ or load resistance $R_L$ drastically reduces ripple, providing nearly flat DC voltage.
    """
            },
            {
                "qid": "beee-q18",
                "marks": 7,
                "type": "Short Answer",
                "title": "Zener Diode: Breakdown Mechanisms (Avalanche vs Zener), Characteristics, and Shunt Voltage Regulator",
                "yt_query": "zener diode working shunt voltage regulator avalanche breakdown line load regulation",
                "img_path": "images/beee/zener_regulator_circuit.png",
                "img_caption": "Figure 4.3: Zener Diode V-I Curve, Shunt Regulator Circuit Topology, and Operational Limits",
                "answer": r"""
    A Zener diode is a heavily doped silicon PN junction diode designed specifically to operate safely in the reverse breakdown region without sustaining thermal damage, maintaining an almost strictly constant terminal voltage despite wide variations in load current or unregulated input voltage.

    1. Reverse Breakdown Mechanisms:
    When a reverse bias is applied across a PN junction, two distinct breakdown phenomena can occur depending on doping concentration and junction electric field strength:
    - Zener Breakdown (Direct Field Ionization): Occurs in diodes with very heavy doping ($> 1 : 10^4$). Heavy doping causes the depletion region to be extremely narrow (typically $< 10\text{ nm}$). Consequently, even a modest reverse voltage ($< 5\text{ V}$) establishes an intense electric field across the junction exceeding $3 \times 10^7\text{ V/m}$. This electric field exerts sufficient force to tear valence electrons directly out of their covalent bonds, creating an immense surge of electron-hole pairs. Zener breakdown occurs below $5\text{ V}$ and possesses a Negative Temperature Coefficient of breakdown voltage (thermal lattice expansion reduces bond strength, lowering breakdown voltage).
    - Avalanche Breakdown (Impact Ionization): Occurs in lightly or moderately doped diodes where the depletion region is relatively wide. At higher reverse voltages ($> 6\text{ V}$), thermally generated minority carriers entering the depletion region are accelerated to high kinetic velocities by the electric field. These energetic carriers collide with stationary crystal atoms, breaking covalent bonds and liberating new carrier pairs. The newly freed carriers are also accelerated, liberating further carriers in a geometric multiplication cascade known as avalanche multiplication. Avalanche breakdown possesses a Positive Temperature Coefficient (increased lattice vibrations impede carrier acceleration, requiring a higher reverse voltage to trigger breakdown).
    At approximately $5.6\text{ V}$, both mechanisms contribute equally, yielding a near-zero temperature coefficient.

    2. Working of Zener Diode as a Shunt Voltage Regulator:
    In voltage regulation, the Zener diode is connected in parallel (shunt) with the load resistance $R_L$, reverse biased, with an external series current-limiting resistor $R_s$ connected between the unregulated DC input source $V_{in}$ and the cathode.
    Applying Kirchhoff's Current Law at the cathode junction:
    $$I_s = I_Z + I_L$$
    where $I_s$ is the total supply current flowing through $R_s$, $I_Z$ is the Zener operating current, and $I_L = \frac{V_Z}{R_L}$ is the load current.
    Applying KVL around the input loop:
    $$V_{in} = I_s R_s + V_Z \implies R_s = \frac{V_{in} - V_Z}{I_s} = \frac{V_{in} - V_Z}{I_Z + I_L}$$

    Regulation Mechanisms:
    - Line Regulation (Variation in $V_{in}$ at constant $R_L$):
    If unregulated input voltage $V_{in}$ increases, supply current $I_s = \frac{V_{in} - V_Z}{R_s}$ increases. Since $V_Z$ is clamped constant, the load current $I_L = \frac{V_Z}{R_L}$ remains unchanged. The extra current is entirely shunted through the Zener diode ($I_Z \uparrow$). The increased voltage drop $(I_s R_s)$ across resistor $R_s$ absorbs the entire input surge, maintaining load voltage $V_L = V_Z$ strictly constant.
    - Load Regulation (Variation in $R_L$ at constant $V_{in}$):
    If load resistance $R_L$ decreases, the required load current $I_L$ increases. Because $V_{in}$ is constant, total supply current $I_s$ remains fixed. The Zener diode automatically decreases its own internal conduction current by the exact amount needed ($I_Z \downarrow$), such that the sum $(I_Z + I_L = I_s)$ is preserved, keeping $V_L = V_Z$ rock-steady.

    Design Constraints for Series Resistor $R_s$:
    For proper regulation, the Zener current must never fall below its minimum knee current ($I_{Z\min}$, typically $5\text{ mA}$) to stay out of the cut-off region, and must never exceed its maximum rated current ($I_{Z\max} = \frac{P_{Z\max}}{V_Z}$) to prevent thermal destruction.
    $$R_{s\max} = \frac{V_{in(\min)} - V_Z}{I_L(\max) + I_{Z\min}}$$
    $$R_{s\min} = \frac{V_{in(\max)} - V_Z}{I_L(\min) + I_{Z\max}}$$
    Choosing $R_s$ within this interval guarantees unconditional regulation across all line and load variations.
    """
            },
            {
                "qid": "beee-q19",
                "marks": 7,
                "type": "Short Answer",
                "title": "Bipolar Junction Transistor (BJT): Structure, CE Characteristics, Operating Regions, and Current Gains",
                "yt_query": "bipolar junction transistor bjt ce configuration input output characteristics active saturation cutoff",
                "img_path": "images/beee/bjt_ce_characteristics.png",
                "img_caption": "Figure 4.4: NPN BJT Structure, CE Input Characteristics, and CE Output Characteristics with Operating Regions",
                "answer": r"""
    A Bipolar Junction Transistor (BJT) is a three-terminal, two-junction current-controlled semiconductor device capable of signal amplification and high-speed electrical switching. It is termed 'bipolar' because conduction involves both majority and minority charge carriers (electrons and holes).

    1. Physical Structure and Biasing Principles:
    A BJT comprises three doped regions forming two back-to-back PN junctions: the Emitter-Base Junction (EBJ) and the Collector-Base Junction (CBJ).
    - Emitter (E): Heavily doped to inject a massive concentration of majority carriers into the base. Moderate physical size.
    - Base (B): Extremely thin (typically $< 1\,\mu\text{m}$) and very lightly doped ($< 1\%$ of emitter doping) to minimize carrier recombination, allowing over $98\%$ of injected carriers to diffuse across into the collector.
    - Collector (C): Moderately doped, with the largest physical cross-sectional area to dissipate heat generated by carrier collection.
    By Kirchhoff's current law, the total terminal currents satisfy:
    $$I_E = I_B + I_C$$
    where $I_E$ is emitter current, $I_B$ is small base recombination current ($1-5\%$), and $I_C$ is collector current ($95-99\%$).

    2. Common Emitter (CE) Configuration Characteristics:
    The CE configuration is universally favored in amplifier design because it provides simultaneous high voltage gain ($A_v$), high current gain ($A_i$), and the highest power gain ($A_p = A_v \cdot A_i$).
    The emitter terminal is connected common to both input (base-emitter) and output (collector-emitter) circuits.

    Input Characteristics ($I_B$ versus $V_{BE}$ for constant $V_{CE}$):
    The input characteristics resemble the forward-biased V-I curve of an ordinary silicon PN diode.
    Below the knee voltage ($V_{BE} < 0.6\text{ V}$), base current is negligible.
    Once $V_{BE} \ge 0.7\text{ V}$, base current $I_B$ rises steeply.
    As $V_{CE}$ is increased from $1\text{ V}$ to $10\text{ V}$, the output CBJ becomes more strongly reverse biased, which widens the depletion layer into the lightly doped base. This reduction in effective base width (Early Effect or Base-Width Modulation) reduces base recombination, shifting the curve slightly to the right for higher $V_{CE}$.
    Input dynamic resistance is:
    $$R_{in} = \left. \frac{\Delta V_{BE}}{\Delta I_B} \right|_{V_{CE} = \text{const}} \sim 1\text{ k}\Omega \text{ to } 3\text{ k}\Omega$$

    Output Characteristics ($I_C$ versus $V_{CE}$ for constant $I_B$):
    Plotting collector current $I_C$ against collector-emitter voltage $V_{CE}$ for a family of constant base currents $I_B$ reveals three distinct operational regimes:
    1. Cut-off Region: Both EBJ and CBJ are reverse-biased ($V_{BE} \le 0\text{ V}, I_B = 0$). Collector current is reduced to the tiny reverse leakage current $I_{CEO} = (\beta + 1)I_{CBO}$. The transistor behaves as an open switch.
    2. Active (Linear) Region: EBJ is forward-biased ($V_{BE} \approx 0.7\text{ V}$) and CBJ is reverse-biased ($V_{CE} \ge 1\text{ V}$). Curves are nearly horizontal and evenly spaced, showing that collector current is linearly controlled by base current: $I_C = \beta I_B$, essentially independent of $V_{CE}$. This region is utilized for analog signal amplification. The slight upward slope of the curves reflects the Early effect; extending the curves backward locates the Early voltage ($V_A \approx 50\text{ V} - 100\text{ V}$).
    3. Saturation Region: Both EBJ and CBJ are forward-biased ($V_{CE} < 0.2\text{ V}$). Collector current rises very steeply with small increments in $V_{CE}$, bounded by the external collector load resistance. The collector-emitter saturation voltage is $V_{CE(sat)} \approx 0.2\text{ V}$ for Silicon. The transistor behaves as a closed switch.

    3. Current Gain Relationships:
    - Common Base Current Gain ($\alpha$): Ratio of collector current to emitter current:
    $$\alpha = \frac{I_C}{I_E}$$
    Typically, $\alpha$ ranges between $0.95$ and $0.998$.
    - Common Emitter Current Gain ($\beta$ or $h_{FE}$): Ratio of collector current to base current:
    $$\beta = \frac{I_C}{I_B}$$
    Typically, $\beta$ ranges between $50$ and $300$.
    Mathematical Interrelation between $\alpha$ and $\beta$:
    Since $I_E = I_B + I_C$, dividing by $I_C$:
    $$\frac{I_E}{I_C} = \frac{I_B}{I_C} + 1 \implies \frac{1}{\alpha} = \frac{1}{\beta} + 1 = \frac{1 + \beta}{\beta}$$
    Inverting both sides:
    $$\alpha = \frac{\beta}{1 + \beta}$$
    Solving for $\beta$:
    $$\alpha(1 + \beta) = \beta \implies \alpha + \alpha \beta = \beta \implies \alpha = \beta(1 - \alpha) \implies \beta = \frac{\alpha}{1 - \alpha}$$
    For example, if $\alpha = 0.99$:
    $$\beta = \frac{0.99}{1 - 0.99} = \frac{0.99}{0.01} = 99$$
    This high current gain $\beta$ forms the basis of all transistor amplification.
    """
            },
            {
                "qid": "beee-q20",
                "marks": 7,
                "type": "Short Answer",
                "title": "Transistor Applications: BJT as a Switch and Single-Stage Common Emitter (CE) Voltage Amplifier",
                "yt_query": "bjt as switch cut off saturation ce amplifier voltage divider circuit phase reversal",
                "img_path": "images/beee/bjt_switch_and_ce_amplifier.png",
                "img_caption": "Figure 4.5: Transistor Switching States and Voltage-Divider Biased Single-Stage CE Amplifier",
                "answer": r"""
    Bipolar junction transistors operate in two broad engineering paradigms: non-linear digital switching (alternating between Cut-off and Saturation) and linear analog amplification (biased strictly within the Active region).

    1. BJT as a Digital Switch:
    When used as a switch, the transistor controls an external load (such as a relay coil, lamp, or DC motor) connected in series with the collector supply $V_{CC}$ and collector resistor $R_C$.
    - OFF State (Cut-off Region): When input control voltage $V_{in} \le 0\text{ V}$ (or below $0.5\text{ V}$), the base-emitter junction is reverse-biased or unbiased. Base current is zero ($I_B = 0$). Consequently, collector current is negligible ($I_C = 0$). By KVL:
    $$V_{out} = V_{CE} = V_{CC} - I_C R_C = V_{CC} - 0 = V_{CC}$$
    The transistor acts as an OPEN switch between collector and emitter; zero current flows through the load.
    - ON State (Saturation Region): When input voltage is driven high ($V_{in} \gg V_{BE}$), sufficient base current $I_B$ is pumped into the base to drive the transistor deep into saturation. The collector current reaches its maximum value, determined by the external collector circuit:
    $$I_{C(sat)} = \frac{V_{CC} - V_{CE(sat)}}{R_C} \approx \frac{V_{CC}}{R_C}$$
    The collector-to-emitter voltage drops to its minimum saturation potential:
    $$V_{out} = V_{CE(sat)} \approx 0.2\text{ V}$$
    The transistor acts as a CLOSED switch. To ensure robust saturation regardless of transistor production variations in $\beta$, the circuit designer must guarantee the Overdrive Condition:
    $$I_B \ge \frac{I_{C(sat)}}{\beta_{\min}} \iff \beta_{\text{forced}} = \frac{I_{C(sat)}}{I_B} < \beta_{\min}$$
    Typically, an overdrive factor of $2$ to $5$ is applied ($I_B \approx 2 \times I_{B(\min)}$).

    2. Single-Stage Common Emitter (CE) Voltage Amplifier:
    To amplify weak alternating signals linearly, the transistor must be biased at a stable DC Operating Point (Q-Point) centered in the active region using Voltage Divider Biasing ($R_1, R_2, R_C, R_E$).

    Circuit Components and Functions:
    1. Voltage Divider ($R_1$ and $R_2$): Establishes a rock-stable DC base potential $V_B = V_{CC} \frac{R_2}{R_1 + R_2}$, independent of ambient temperature and transistor $\beta$.
    2. Emitter Resistor ($R_E$): Provides negative thermal DC feedback. If temperature rises, collector current $I_C$ increases, boosting emitter current $I_E$ and the emitter voltage drop $V_E = I_E R_E$. Consequently, base-emitter voltage $V_{BE} = V_B - V_E$ decreases, forcing base current $I_B$ and collector current $I_C$ back down, stabilizing the Q-point.
    3. Input Coupling Capacitor ($C_{in}$ or $C_1$, $\sim 10\,\mu\text{F}$): Blocks DC from the AC signal source to avoid disturbing the Q-point, while coupling AC input signals into the base with negligible reactance ($X_C \to 0$ at signal frequencies).
    4. Output Coupling Capacitor ($C_{out}$ or $C_2$, $\sim 10\,\mu\text{F}$): Blocks the DC quiescent collector voltage from reaching the external load, passing only amplified AC output signals.
    5. Emitter Bypass Capacitor ($C_E$, $\sim 100\,\mu\text{F}$): Connected in parallel with $R_E$. At AC signal frequencies, $X_{CE} = \frac{1}{2\pi f C_E} \approx 0\,\Omega$, effectively grounding the emitter for AC signals. This prevents negative feedback at signal frequencies, maximizing AC voltage gain.

    Amplification and $180^\circ$ Phase Inversion:
    When a small sinusoidal AC input voltage $v_{in}$ is applied to the base:
    During the positive half-cycle of $v_{in}$, the net base-emitter voltage increases ($V_{BE} + v_{in}$).
    This causes base current $i_b$ to rise, which produces an amplified increase in collector current:
    $$i_c = \beta \cdot i_b$$
    By KVL in the collector loop, the instantaneous collector output voltage is:
    $$v_C = V_{CC} - i_c R_C$$
    As collector current $i_c$ increases, the voltage drop across $R_C$ ($i_c R_C$) increases substantially.
    Consequently, the output voltage $v_{out}$ swings strongly in the negative direction.
    Conversely, during the negative half-cycle of $v_{in}$, base-emitter voltage decreases, $i_c$ decreases, the drop across $R_C$ diminishes, and $v_{out}$ swings in the positive direction.
    Therefore, the output voltage is an amplified replica of the input signal, but exhibits an exact $180^\circ$ phase reversal (phase inversion) relative to the input.
    The small-signal voltage gain is:
    $$A_v = \frac{v_{out}}{v_{in}} = -\frac{g_m (R_C \parallel R_L)}{1} \approx -\frac{R_C \parallel R_L}{r_e'}$$
    where $r_e' = \frac{26\text{ mV}}{I_E}$ is the internal AC emitter resistance, and the minus sign mathematically represents the $180^\circ$ phase inversion.
    """
            }
        ]
    },
    {
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
]

BEEE_BYHEART = {
    'beee-q1': {
        "eq": r"""$$\sum I_{\text{in}} = \sum I_{\text{out}}, \quad \sum_{k=1}^m V_k = 0$$""",
        "text": r"""<strong>Kirchhoff’s Current Law (KCL):</strong> Conservation of electric charge; algebraic sum of currents entering and leaving any node is zero ($\sum I = 0$).<br><strong>Kirchhoff’s Voltage Law (KVL):</strong> Conservation of energy; algebraic sum of potential rises and drops around any closed loop is zero ($\sum V = 0$)."""
    },
    'beee-q2': {
        "eq": r"""$$V_1 - V_2 = V_s, \quad \sum I_{\text{supernode}} = 0$$""",
        "text": r"""<strong>Supernode:</strong> Formed when an ideal voltage source is connected between two non-reference nodes. Replace the source branch with an enclosed boundary and apply KCL to the combined supernode, augmented by the source constraint equation ($V_1 - V_2 = V_s$)."""
    },
    'beee-q3': {
        "eq": r"""$$I_L = I_L' + I_L'' + I_L''' + \dots = \sum_{k=1}^n I_L^{(k)}$$""",
        "text": r"""<strong>Superposition Theorem:</strong> In any linear bilateral network with multiple independent sources, the response in any branch is the algebraic sum of responses caused by each independent source acting alone, with all other voltage sources shorted ($V=0$) and current sources opened ($I=0$). Does not apply directly to power."""
    },
    'beee-q4': {
        "eq": r"""$$V_{th} = V_{oc}, \quad R_{th} = R_N, \quad I_N = \frac{V_{th}}{R_{th}}, \quad I_L = \frac{V_{th}}{R_{th} + R_L} = I_N \left(\frac{R_N}{R_N + R_L}\right)$$""",
        "text": r"""<strong>Thevenin’s Theorem:</strong> Replaces network across load terminals with open-circuit voltage $V_{th}$ in series with $R_{th}$.<br><strong>Norton’s Theorem:</strong> Replaces network with short-circuit current $I_N$ in parallel with $R_N = R_{th}$. Dual relationship: $V_{th} = I_N R_{th}$."""
    },
    'beee-q5': {
        "eq": r"""$$R_L = R_{th} \implies P_{\max} = \frac{V_{th}^2}{4 R_{th}}, \quad \eta = \frac{P_L}{P_{total}} \times 100\% = 50\%$$""",
        "text": r"""<strong>Maximum Power Transfer Theorem:</strong> Maximum power is delivered to a load when $R_L = R_{th}$, resulting in $P_{\max} = \frac{V_{th}^2}{4 R_{th}}$. The transmission efficiency at maximum power transfer is strictly $50\%$, with the remaining $50\%$ dissipated as heat in internal resistance."""
    },
    'beee-q6': {
        "eq": r"""$$v(t) = V_m \sin(\omega t \pm \phi), \quad \omega = 2\pi f = \frac{2\pi}{T}, \quad \mathbf{V} = V_{rms}\angle \phi$$""",
        "text": r"""<strong>Sinusoidal AC Generation:</strong> Derived from Faraday’s law $e(t) = -N \frac{d\Phi}{dt} = N B A \omega \sin(\omega t)$ for a coil rotating in a uniform magnetic field.<br><strong>Phasor:</strong> Directed vector rotating counterclockwise at angular velocity $\omega$, representing RMS magnitude and phase angle in the complex plane."""
    },
    'beee-q7': {
        "eq": r"""$$V_{rms} = \frac{V_m}{\sqrt{2}} \approx 0.707 V_m, \quad V_{avg} = \frac{2 V_m}{\pi} \approx 0.637 V_m, \quad K_f = \frac{V_{rms}}{V_{avg}} = 1.11, \quad K_p = \frac{V_m}{V_{rms}} = \sqrt{2} \approx 1.414$$""",
        "text": r"""<strong>RMS Value:</strong> Equivalent DC heating value ($V_m / \sqrt{2}$).<br><strong>Average Value:</strong> Half-cycle arithmetic mean ($2 V_m / \pi$).<br><strong>Form Factor:</strong> $K_f = 1.11$ for pure sine wave.<br><strong>Peak Factor:</strong> $K_p = 1.414$, governing dielectric insulation withstand limits."""
    },
    'beee-q8': {
        "eq": r"""$$\mathbf{Z} = R + j(X_L - X_C), \quad P = V I \cos\phi, \quad Q = V I \sin\phi, \quad S = V I = \sqrt{P^2 + Q^2}, \quad pf = \cos\phi = \frac{R}{|\mathbf{Z}|}$$""",
        "text": r"""<strong>Series R-L:</strong> Current lags voltage by $\phi = \tan^{-1}(X_L/R)$, lagging power factor.<br><strong>Series R-C:</strong> Current leads voltage by $\phi = \tan^{-1}(X_C/R)$, leading power factor.<br><strong>Power Triangle:</strong> Real active power $P$ (Watts), reactive power $Q$ (VAR), apparent power $S$ (VA)."""
    },
    'beee-q9': {
        "eq": r"""$$f_r = \frac{1}{2\pi\sqrt{LC}}, \quad |\mathbf{Z}_r| = R, \quad I_0 = \frac{V}{R}, \quad Q = \frac{1}{R}\sqrt{\frac{L}{C}}, \quad BW = f_2 - f_1 = \frac{f_r}{Q} = \frac{R}{2\pi L}$$""",
        "text": r"""<strong>Series Resonance:</strong> Occurs when $X_L = X_C$, giving purely resistive minimum impedance $|\mathbf{Z}| = R$, maximum in-phase current ($pf = 1.0$), and voltage magnification across $L$ and $C$ ($V_L = V_C = Q \cdot V$). Narrow bandwidth indicates high selectivity."""
    },
    'beee-q10': {
        "eq": r"""$$\mathcal{F} = N I, \quad \Phi = \frac{\mathcal{F}}{S}, \quad S = \frac{l}{\mu_0 \mu_r A}, \quad B = \mu H = \mu_0 \mu_r H, \quad W_h = \eta B_{\max}^{1.6} f$$""",
        "text": r"""<strong>Magnetic Circuits:</strong> MMF ($\mathcal{F} = NI$ in AT) drives flux ($\Phi = \mathcal{F}/S$ in Wb) against reluctance ($S = \frac{l}{\mu A}$). Electric-magnetic analogy: EMF $\leftrightarrow$ MMF, Current $\leftrightarrow$ Flux, Resistance $\leftrightarrow$ Reluctance. Hysteresis loop area represents Steinmetz core energy loss."""
    },
    'beee-q11': {
        "eq": r"""$$E_1 = 4.44 f N_1 \Phi_m, \quad K = \frac{E_2}{E_1} = \frac{N_2}{N_1}, \quad \eta = \frac{x S \cos\phi_2}{x S \cos\phi_2 + W_i + x^2 W_{cu(FL)}}, \quad W_{cu} = W_i \ (\eta_{\max})$$""",
        "text": r"""<strong>Transformer EMF Equation:</strong> Derived from mutual induction $e = -N \frac{d\Phi}{dt}$, yielding RMS $E = 4.44 f N \Phi_m$.<br><strong>Condition for Maximum Efficiency:</strong> Variable copper loss equals constant iron loss ($W_{cu} = W_i$), occurring at fraction $x_m = \sqrt{W_i / W_{cu(FL)}}$."""
    },
    'beee-q12': {
        "eq": r"""$$E_g = \frac{\Phi Z N P}{60 A}, \quad A = P \ (\text{Lap Winding}), \quad A = 2 \ (\text{Wave Winding})$$""",
        "text": r"""<strong>DC Generator EMF Equation:</strong> Generated voltage $E_g = \frac{\Phi Z N P}{60 A}$. Conductor cuts total flux $P\Phi$ in $60/N$ seconds; $Z/A$ conductors in series per path. Commutator acts as a mechanical rectifier converting internal AC EMF into external DC."""
    },
    'beee-q13': {
        "eq": r"""$$V = E_b + I_a R_a, \quad E_b = \frac{\Phi Z N P}{60 A}, \quad T_a = 0.159 \left(\frac{P Z}{A}\right)\Phi I_a \propto \Phi I_a, \quad N \propto \frac{E_b}{\Phi}$$""",
        "text": r"""<strong>DC Motor Operation:</strong> Conductor force $F = B I l$ (Fleming’s Left-Hand Rule).<br><strong>Back-EMF ($E_b$):</strong> Acts as an automatic governor regulating armature current $I_a = (V - E_b)/R_a$. Massive starting current requires starters. Armature torque $T_a \propto \Phi I_a$; speed $N \propto E_b / \Phi$."""
    },
    'beee-q14': {
        "eq": r"""$$\text{Star: } V_L = \sqrt{3} V_{ph}, \; I_L = I_{ph}; \quad \text{Delta: } V_L = V_{ph}, \; I_L = \sqrt{3} I_{ph}; \quad P = \sqrt{3} V_L I_L \cos\phi$$""",
        "text": r"""<strong>Balanced 3-Phase Systems:</strong> Star provides neutral point with $V_L = \sqrt{3} V_{ph}$; Delta provides closed mesh with $I_L = \sqrt{3} I_{ph}$. Total active power in both configurations is universally $P = \sqrt{3} V_L I_L \cos\phi\text{ W}$, and reactive power is $Q = \sqrt{3} V_L I_L \sin\phi\text{ VAR}$."""
    },
    'beee-q15': {
        "eq": r"""$$I_{\text{residual}} = |I_L - I_N| > 30\text{ mA} \implies \text{Trip}, \quad R_{\text{earth}} < 5\,\Omega \ (\text{Domestic})$$""",
        "text": r"""<strong>Wiring & Protection:</strong> Staircase wiring controls one lamp via two SPDT switches. Earthing (pipe/plate) diverts dangerous fault currents, keeping touch potential safe. MCB provides thermal overload and magnetic short-circuit protection; ELCB/RCCB senses core-balance current imbalance $> 30\text{ mA}$ to prevent electrocution."""
    },
    'beee-q16': {
        "eq": r"""$$I = I_0 \left(e^{\frac{V}{\eta V_T}} - 1\right), \quad V_T = \frac{k T}{q} \approx 26\text{ mV}, \quad r_d = \frac{\eta V_T}{I_F} \approx \frac{26\text{ mV}}{I_F\text{ (mA)}}$$""",
        "text": r"""<strong>PN Junction Diode:</strong> Depletion region uncovers immobile ions creating barrier potential ($0.7\text{ V}$ for Si). Forward bias narrows depletion width, triggering exponential diffusion current (Shockley equation). Dynamic resistance $r_d \approx 26 / I_F\text{ mA}$."""
    },
    'beee-q17': {
        "eq": r"""$$\text{HWR: } V_{dc} = \frac{V_m}{\pi}, \eta = 40.6\%, \gamma = 1.21; \quad \text{FWR: } V_{dc} = \frac{2 V_m}{\pi}, \eta = 81.2\%, \gamma = 0.482, \gamma_{cap} \approx \frac{1}{4\sqrt{3} f C R_L}$$""",
        "text": r"""<strong>Rectifiers:</strong> Full-wave bridge rectifier utilizes four diodes in bridge configuration, doubling DC voltage ($2 V_m / \pi$) and efficiency ($81.2\%$) compared to half-wave ($40.6\%$), with lower ripple factor ($\gamma = 0.482$). Shunt capacitor filter smooths ripple via $R_L C$ discharge."""
    },
    'beee-q18': {
        "eq": r"""$$V_L = V_Z, \quad I_s = I_Z + I_L = \frac{V_{in} - V_Z}{R_s}, \quad R_{s\max} = \frac{V_{in(\min)} - V_Z}{I_{L(\max)} + I_{Z\min}}$$""",
        "text": r"""<strong>Zener Diode Regulator:</strong> Operates in reverse breakdown ($V_Z$). Zener breakdown ($< 5\text{ V}$, field ionization, negative temp-co); Avalanche breakdown ($> 6\text{ V}$, impact ionization, positive temp-co). Shunts excess current through Zener, maintaining stable output voltage across line and load variations."""
    },
    'beee-q19': {
        "eq": r"""$$I_E = I_B + I_C, \quad I_C = \beta I_B + I_{CEO}, \quad \beta = \frac{\alpha}{1 - \alpha}, \quad \alpha = \frac{\beta}{1 + \beta}$$""",
        "text": r"""<strong>BJT Characteristics:</strong> Emitter heavily doped, base thin and lightly doped, collector large. CE configuration provides high current gain ($\beta = \frac{\alpha}{1-\alpha} \sim 100$) and power gain. Active region (EBJ forward, CBJ reverse) for amplification; Cut-off and Saturation for digital switching."""
    },
    'beee-q20': {
        "eq": r"""$$I_B \ge \frac{I_{C(sat)}}{\beta_{\min}}, \quad A_v = \frac{v_{out}}{v_{in}} \approx -\frac{R_C \parallel R_L}{r_e'}, \quad \phi = 180^\circ$$""",
        "text": r"""<strong>Transistor Applications:</strong> BJT as switch: OFF in cut-off ($V_{out} = V_{CC}$), ON in saturation ($V_{out} \approx 0.2\text{ V}$). Single-stage CE amplifier: Voltage divider bias stabilizes Q-point; bypass capacitor $C_E$ maximizes AC gain; output voltage exhibits an exact $180^\circ$ phase inversion."""
    },
    'beee-q21': {
        "eq": r"""$$V_+ = V_- \ (\text{Virtual Short}), \quad I_+ = I_- = 0\text{ A}, \quad A_{OL} = \infty, \; R_{in} = \infty, \; R_{out} = 0, \; CMRR = \infty$$""",
        "text": r"""<strong>Ideal Op-Amp & Virtual Ground:</strong> Infinite open-loop gain ($A_{OL} \to \infty$) with negative feedback forces differential input voltage $V_d = V_+ - V_- = 0$, establishing a virtual short. Infinite input impedance ensures zero terminal input current ($I_+ = I_- = 0$). Grounding non-inverting terminal creates a virtual ground at inverting node."""
    },
    'beee-q22': {
        "eq": r"""$$A_{v(inv)} = -\frac{R_f}{R_1}, \quad A_{v(non-inv)} = 1 + \frac{R_f}{R_1}, \quad A_{v(buffer)} = 1.0, \quad Z_{in(buffer)} \approx \infty, \; Z_{out(buffer)} \approx 0$$""",
        "text": r"""<strong>Op-Amp Configurations:</strong> Inverting amplifier provides stabilized gain $A_v = -R_f/R_1$ with $180^\circ$ phase inversion. Non-inverting amplifier provides in-phase gain $A_v = 1 + R_f/R_1 \ge 1$ with ultra-high input impedance. Voltage follower ($R_f=0$) provides unity gain for impedance buffer isolation."""
    },
    'beee-q23': {
        "eq": r"""$$V_{out} = -\left[\frac{R_f}{R_1}V_1 + \frac{R_f}{R_2}V_2\right], \quad V_{out(int)} = -\frac{1}{RC}\int V_{in}\,dt, \quad V_{out(diff)} = -RC \frac{dV_{in}}{dt}$$""",
        "text": r"""<strong>Mathematical Op-Amp Circuits:</strong> Summing amplifier adds input signals with weighted gains. Difference amplifier subtracts common-mode noise. Integrator (feedback capacitor $C$) ramps output proportional to input integral. Differentiator (input capacitor $C$) differentiates input rate of change."""
    },
    'beee-q24': {
        "eq": r"""$$A - B = A + (\text{2’s complement of } B), \quad \text{2’s Comp} = \text{1’s Comp} + 1, \quad \text{Range: } -2^{n-1} \le N \le +2^{n-1}-1$$""",
        "text": r"""<strong>2’s Complement Arithmetic:</strong> Subtraction $A - B$ executed by adding 2’s complement of $B$ to $A$. An end carry signifies a positive answer (discard end carry). Absence of end carry indicates negative answer in 2’s complement form (take 2’s complement of sum to obtain true magnitude)."""
    },
    'beee-q25': {
        "eq": r"""$$\overline{A \cdot B} = \bar{A} + \bar{B}, \quad \overline{A + B} = \bar{A} \cdot \bar{B}, \quad A \oplus B = \bar{A} B + A \bar{B}, \quad \text{NAND/NOR: Universal}$$""",
        "text": r"""<strong>Universal Gates & De Morgan’s Laws:</strong> Any logic function can be realized using solely NAND gates or solely NOR gates. De Morgan’s first law: NAND is equivalent to bubbled OR ($\overline{AB} = \bar{A}+\bar{B}$). De Morgan’s second law: NOR is equivalent to bubbled AND ($\overline{A+B} = \bar{A}\bar{B}$)."""
    },
    'beee-q26': {
        "eq": r"""$$\text{HA: } S = A \oplus B, C = AB; \quad \text{FA: } S = A \oplus B \oplus C_{in}, C_{out} = AB + C_{in}(A \oplus B)$$""",
        "text": r"""<strong>Arithmetic Adders:</strong> Half Adder computes sum and carry of two bits using one XOR gate and one AND gate. Full Adder computes sum and carry of three bits ($A, B, C_{in}$), synthesized using two half adders and one OR gate ($S = A \oplus B \oplus C_{in}$, $C_{out} = AB + C_{in}(A \oplus B)$)."""
    }
}

BEEE_EXAM_QUESTIONS = {
    "beee-q1": "State and explain Kirchhoff's Current Law (KCL) and Kirchhoff's Voltage Law (KVL) with algebraic sign conventions. Explain how they form the basis of mesh and nodal analysis.",
    "beee-q2": "Explain Nodal Voltage Analysis. Explain the supernode concept when an ideal independent voltage source is connected between two non-reference nodes, and solve a numerical problem.",
    "beee-q3": "State Superposition Theorem. Explain its conditions of applicability and limitations. Find the current through the load resistor in a multi-source DC network with independent voltage and current sources.",
    "beee-q4": "State Thevenin's and Norton's Theorems and derive their dual relationship. Find the Thevenin and Norton equivalent circuits across the detector terminals of an unbalanced bridge network.",
    "beee-q5": "State and prove Maximum Power Transfer Theorem for a DC network. Derive the expression for maximum power and show that the transmission efficiency at maximum power is 50%.",
    "beee-q6": "Explain the generation of sinusoidal alternating voltage by a coil rotating in a uniform magnetic field. Define instantaneous value, amplitude, time period, frequency, and phasor representation.",
    "beee-q7": "Derive the mathematical expressions for the RMS value, Average value, Form Factor, and Peak Factor of a pure sinusoidal alternating voltage waveform.",
    "beee-q8": "Derive the expressions for impedance, current, phase angle, and power in a series R-L and series R-C circuit excited by sinusoidal AC. Explain the impedance and power triangles with a numerical problem.",
    "beee-q9": "Derive the condition and expression for resonant frequency in a series R-L-C circuit. Derive the expressions for Quality factor (Q) and half-power bandwidth (BW).",
    "beee-q10": "Define MMF, magnetic flux, reluctance, permeance, and flux density. Compare electric and magnetic circuits in detail. Explain the B-H curve and solve a series magnetic circuit with an air gap.",
    "beee-q11": "Explain the construction and working principle of a single-phase transformer. Derive the EMF equation and the condition for maximum efficiency.",
    "beee-q12": "Explain the constructional details of a DC machine with a neat sketch. Explain the operating principle of a DC generator and derive the generator EMF equation.",
    "beee-q13": "Explain the working principle of a DC motor and the physical significance of Back-EMF. Derive the DC motor armature torque equation and speed relationship.",
    "beee-q14": "Derive the relationship between line and phase voltages and currents in balanced 3-phase Star (Y) and Delta (Δ) connected systems. Derive the expression for total 3-phase active power.",
    "beee-q15": "Draw the schematic layout of a residential distribution board. Explain the two-way control of a lamp (staircase wiring). Explain pipe earthing and compare Fuse, MCB, and ELCB/RCCB.",
    "beee-q16": "Distinguish between intrinsic and extrinsic semiconductors. Explain the formation of a PN junction, depletion layer, and barrier potential. Explain forward and reverse bias V-I characteristics.",
    "beee-q17": "Explain the working of half-wave and full-wave bridge rectifiers with circuit diagrams and waveforms. Derive expressions for V_dc, V_rms, rectification efficiency, and ripple factor. Explain the role of capacitor filter.",
    "beee-q18": "Explain the breakdown mechanisms in a PN junction: Avalanche breakdown versus Zener breakdown. Explain the operation of a Zener diode as a shunt voltage regulator with circuit diagram and design equations.",
    "beee-q19": "Describe the physical structure and operation of an NPN Bipolar Junction Transistor. Plot and explain the Common Emitter (CE) input and output characteristics, identifying all operating regions. Derive the relationship between α and β.",
    "beee-q20": "Explain the operation of a BJT as a digital switch with operating conditions. Draw the circuit diagram of a single-stage Common Emitter (CE) voltage amplifier with voltage-divider biasing and explain its operation and 180° phase inversion.",
    "beee-q21": "Explain the internal architectural block diagram of an operational amplifier and pinout of IC 741. List ideal op-amp characteristics and explain the concepts of Virtual Ground and Virtual Short.",
    "beee-q22": "Derive the closed-loop voltage gain expressions for Inverting and Non-Inverting op-amp configurations. Explain the Voltage Follower (Buffer) circuit and its practical application.",
    "beee-q23": "Explain the circuit operations and derive the output voltage expressions for an op-amp Summing Amplifier, Difference Amplifier, Integrator, and Differentiator.",
    "beee-q24": "Explain decimal, binary, octal, and hexadecimal number systems with radix conversion examples. Explain 1's and 2's complement representations and perform binary subtraction using 2's complement with overflow rules.",
    "beee-q25": "Explain basic and universal logic gates with symbols, Boolean expressions, and truth tables. Show how AND, OR, NOT gates are realized using only NAND gates and only NOR gates. State and prove De Morgan's laws.",
    "beee-q26": "Design a Half Adder and a Full Adder circuit. Write their truth tables, obtain minimized Boolean expressions using K-maps, and implement a Full Adder using two Half Adders and an OR gate."
}
