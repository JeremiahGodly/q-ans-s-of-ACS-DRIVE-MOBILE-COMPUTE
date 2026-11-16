# -*- coding: utf-8 -*-
"""
Module 1 for Linear Control Systems (EET302)
Mathematical Modeling of Control Systems
"""

M1_QUESTIONS = [
    {
        "qid": "lcs-q1",
        "marks": 3,
        "type": "Short Answer",
        "title": "Open-Loop vs Closed-Loop Control Systems and Sensitivity Analysis",
        "yt_query": "open loop vs closed loop control system sensitivity analysis",
        "img_path": "images/lcs/open_closed_loop_comparison.png",
        "img_caption": "Figure 1.1: Functional Block Diagrams of Open-Loop and Closed-Loop Control Systems",
        "answer": r"""
A control system is an interconnection of physical components assembled to direct, guide, or regulate itself or another physical device. In classical control theory, systems are categorized into two fundamental architectures: open-loop control systems and closed-loop (feedback) control systems. 

In an open-loop control system, the control action is entirely independent of the output response of the process. The controller generates an actuation signal strictly based on a preset reference command without measuring or comparing the actual process output. A domestic washing machine or an automated traffic timer exemplifies open-loop operation: the machine executes a pre-timed cycle regardless of whether the clothes are genuinely clean. These systems offer simple construction, low capital cost, and unconditional internal stability because no feedback signal exists to cause closed-loop oscillation. However, open-loop systems cannot reject external environmental disturbances or compensate for internal parameter drift, resulting in degraded steady-state precision.

In contrast, a closed-loop control system continuously measures the physical output variable, feeds this information back via a sensor element, and compares it against the desired setpoint at a summing junction. The resulting error signal drives the controller to adjust the plant input, reducing the difference between reference and output toward zero. Examples include automatic room air conditioning, DC motor speed governors, and missile autopilot guidance systems. Closed-loop feedback provides outstanding tracking accuracy, broad operational bandwidth, and robust disturbance rejection. Its primary engineering trade-offs include higher installation cost, sensor noise corruption, and the potential risk of dynamic instability if the loop gain and phase margin are poorly tuned.

The influence of feedback on parameter variation is quantified mathematically by the concept of sensitivity. Let $T(s)$ denote the closed-loop complementary transfer function relating output $C(s)$ to reference $R(s)$:
$$T(s) = \frac{C(s)}{R(s)} = \frac{G(s)}{1 + G(s)H(s)}$$
The system sensitivity with respect to changes in the forward plant transfer function $G(s)$ is defined as the ratio of percentage change in $T(s)$ to the percentage change in $G(s)$:
$$S^T_G = \frac{\partial T / T}{\partial G / G} = \frac{\partial T}{\partial G} \cdot \frac{G}{T}$$
Differentiating $T(s)$ with respect to $G(s)$ using the quotient rule:
$$\frac{\partial T}{\partial G} = \frac{[1 + G(s)H(s)](1) - G(s)[H(s)]}{[1 + G(s)H(s)]^2} = \frac{1}{[1 + G(s)H(s)]^2}$$
Substituting this derivative back into the sensitivity definition:
$$S^T_G = \frac{1}{[1 + G(s)H(s)]^2} \cdot \frac{G}{\frac{G}{1 + G(s)H(s)}} = \frac{1}{1 + G(s)H(s)}$$
Equation above proves that negative feedback suppresses the impact of forward plant parameter drifts by the loop return difference factor $1 + G(s)H(s)$. If the loop gain $|G(s)H(s)| \gg 1$, the sensitivity $S^T_G$ approaches zero. Conversely, the sensitivity of the closed-loop system with respect to the feedback sensor transfer function $H(s)$ is evaluated as:
$$\frac{\partial T}{\partial H} = \frac{0 - G(s)[G(s)]}{[1 + G(s)H(s)]^2} = \frac{-G^2(s)}{[1 + G(s)H(s)]^2}$$
$$S^T_H = \frac{\partial T}{\partial H} \cdot \frac{H}{T} = \frac{-G^2(s)}{[1 + G(s)H(s)]^2} \cdot \frac{H(s)}{\frac{G(s)}{1 + G(s)H(s)}} = \frac{-G(s)H(s)}{1 + G(s)H(s)}$$
When the open-loop gain is large, $|S^T_H| \approx 1$. This derivation demonstrates that feedback control makes the system performance insensitive to plant variations, but demands high precision and environmental stability in the feedback sensor components.
"""
    },
    {
        "qid": "lcs-q2",
        "marks": 3,
        "type": "Short Answer",
        "title": "Mechanical-Electrical Analogies: Force-Voltage and Force-Current Formulations",
        "yt_query": "force voltage force current analogy control systems",
        "img_path": "images/lcs/mechanical_electrical_analogies.png",
        "img_caption": "Figure 1.2: Mechanical-Electrical Equivalences for Translational Systems",
        "answer": r"""
Mechanical and electrical systems often exhibit identical mathematical descriptions despite their different physical forms. The dynamic equations of translational mechanical systems derived from Newton's second law or D'Alembert's principle have exact structural analogs in Kirchhoff's loop and nodal laws of electrical networks. Establishing these mechanical-electrical analogies allows engineers to analyze complex mechanical vibrations using familiar circuit theorems and electrical simulation software.

Consider a fundamental translational mechanical element consisting of a mass $M$, a linear viscous dashpot damper $B$, and a spring of stiffness $K$, excited by an external time-varying force $F(t)$. Under an instantaneous displacement $x(t)$ and velocity $v(t) = \frac{dx}{dt}$, D'Alembert's dynamic equilibrium equation balances applied force against internal inertial, frictional, and restorative reaction forces:
$$F(t) = M \frac{d^2x(t)}{dt^2} + B \frac{dx(t)}{dt} + K x(t)$$
Expressing this governing dynamic balance directly in terms of linear velocity $v(t)$:
$$F(t) = M \frac{dv(t)}{dt} + B v(t) + K \int v(t) \, dt$$

The first formal mapping is the Force-Voltage (F-V) Analogy, often called Maxwell's loop analogy. Consider a series RLC circuit energized by an instantaneous voltage source $e(t)$ with a resulting loop current $i(t)$ and electric charge $q(t) = \int i(t) dt$. Applying Kirchhoff's Voltage Law (KVL) around the closed mesh:
$$e(t) = L \frac{di(t)}{dt} + R i(t) + \frac{1}{C} \int i(t) \, dt = L \frac{d^2q(t)}{dt^2} + R \frac{dq(t)}{dt} + \frac{1}{C} q(t)$$
Direct term-by-term comparison between the mechanical velocity equation and the KVL series loop equation establishes the following one-to-one analog pairs:
$$F(t) \longleftrightarrow e(t) \quad (\text{Force } \longleftrightarrow \text{ Voltage})$$
$$v(t) \longleftrightarrow i(t) \quad (\text{Velocity } \longleftrightarrow \text{ Current})$$
$$x(t) \longleftrightarrow q(t) \quad (\text{Displacement } \longleftrightarrow \text{ Charge})$$
$$M \longleftrightarrow L \quad (\text{Mass } \longleftrightarrow \text{ Inductance})$$
$$B \longleftrightarrow R \quad (\text{Viscous Friction } \longleftrightarrow \text{ Resistance})$$
$$K \longleftrightarrow \frac{1}{C} \quad (\text{Spring Constant } \longleftrightarrow \text{ Elastance / Reciprocal Capacitance})$$

The second mapping is the Force-Current (F-I) Analogy, known as Firestone's nodal analogy. Consider a parallel G-C-L electrical network excited by an independent current source $j(t)$, developing an instantaneous node voltage $v_n(t)$ with magnetic flux linkage $\phi(t) = \int v_n(t) dt$. Applying Kirchhoff's Current Law (KCL) at the independent node:
$$j(t) = C \frac{dv_n(t)}{dt} + G v_n(t) + \frac{1}{L} \int v_n(t) \, dt = C \frac{d^2\phi(t)}{dt^2} + G \frac{d\phi(t)}{dt} + \frac{1}{L} \phi(t)$$
where $G = 1/R$ is the electrical conductance. Comparing the mechanical velocity equation directly with the nodal KCL equation yields the alternative analog equivalences:
$$F(t) \longleftrightarrow j(t) \quad (\text{Force } \longleftrightarrow \text{ Current Source})$$
$$v(t) \longleftrightarrow v_n(t) \quad (\text{Velocity } \longleftrightarrow \text{ Node Voltage})$$
$$x(t) \longleftrightarrow \phi(t) \quad (\text{Displacement } \longleftrightarrow \text{ Magnetic Flux Linkage})$$
$$M \longleftrightarrow C \quad (\text{Mass } \longleftrightarrow \text{ Capacitance})$$
$$B \longleftrightarrow G = \frac{1}{R} \quad (\text{Viscous Friction } \longleftrightarrow \text{ Conductance})$$
$$K \longleftrightarrow \frac{1}{L} \quad (\text{Spring Constant } \longleftrightarrow \text{ Reciprocal Inductance})$$

In practical network synthesis, the Force-Current analogy offers a distinct topological benefit: two mechanical masses sharing a common displacement connect in parallel to ground, matching how two capacitors in an electrical circuit share a common nodal voltage with respect to ground reference.
"""
    },
    {
        "qid": "lcs-q3",
        "marks": 7,
        "type": "Long Derivation",
        "title": "Mathematical Modeling and Transfer Function of a Coupled Two-Mass Mechanical System",
        "yt_query": "mathematical modeling translational mechanical system transfer function two mass",
        "img_path": "images/lcs/two_mass_mechanical_system.png",
        "img_caption": "Figure 1.3: Two-Degree-of-Freedom Translational Mechanical System with Free-Body Diagrams",
        "answer": r"""
Consider a classical two-degree-of-freedom translational mechanical vibration system frequently encountered in KTU university examinations. The system comprises two rigid bodies of masses $M_1$ and $M_2$. Mass $M_1$ is connected to a rigid reference frame through a spring of stiffness $K_1$ and a viscous damper of coefficient $B_1$. Mass $M_1$ is simultaneously coupled to mass $M_2$ via an intermediate spring of stiffness $K_2$ and an intermediate damper of coefficient $B_2$. Mass $M_2$ is connected to a fixed wall via a damper $B_3$. An external dynamic driving force $F(t)$ is applied directly to mass $M_1$. The displacements of masses $M_1$ and $M_2$ from their static equilibrium positions are designated as $x_1(t)$ and $x_2(t)$, respectively.

We begin by establishing the free-body diagrams for each mass under the physical convention that $x_1(t) > x_2(t)$ and $\dot{x}_1(t) > \dot{x}_2(t)$. 

For Mass $M_1$:
The external driving force $F(t)$ acts in the positive direction of motion. Resisting forces acting opposite to the acceleration $\ddot{x}_1(t)$ include:
1. Inertial force of mass $M_1$: $f_{i1} = M_1 \frac{d^2 x_1(t)}{dt^2}$
2. Damper force connecting $M_1$ to ground: $f_{b1} = B_1 \frac{dx_1(t)}{dt}$
3. Restoring spring force connecting $M_1$ to ground: $f_{k1} = K_1 x_1(t)$
4. Coupling damper force between $M_1$ and $M_2$: $f_{b2} = B_2 \left(\frac{dx_1(t)}{dt} - \frac{dx_2(t)}{dt}\right)$
5. Coupling spring force between $M_1$ and $M_2$: $f_{k2} = K_2 [x_1(t) - x_2(t)]$

Applying Newton's second law of motion ($\sum F_{ext} = \sum F_{opposing}$) on Mass $M_1$:
$$M_1 \frac{d^2 x_1}{dt^2} + B_1 \frac{dx_1}{dt} + K_1 x_1 + B_2 \left(\frac{dx_1}{dt} - \frac{dx_2}{dt}\right) + K_2 (x_1 - x_2) = F(t)$$
Regrouping terms associated with coordinates $x_1(t)$ and $x_2(t)$:
$$M_1 \frac{d^2 x_1}{dt^2} + (B_1 + B_2) \frac{dx_1}{dt} + (K_1 + K_2) x_1 - B_2 \frac{dx_2}{dt} - K_2 x_2 = F(t) \quad \text{--- (Equation 1)}$$

For Mass $M_2$:
No external active force is applied directly to mass $M_2$. The coupling elements transmit dynamic forces driven by the relative displacement and relative velocity $(x_1 - x_2)$. Opposing forces acting on mass $M_2$ are:
1. Inertial force of mass $M_2$: $f_{i2} = M_2 \frac{d^2 x_2(t)}{dt^2}$
2. Ground damper force on $M_2$: $f_{b3} = B_3 \frac{dx_2(t)}{dt}$
3. Transmitted coupling damper force: $f_{b2} = B_2 \left(\frac{dx_2}{dt} - \frac{dx_1}{dt}\right)$
4. Transmitted coupling spring force: $f_{k2} = K_2 (x_2 - x_1)$

Applying Newton's second law on Mass $M_2$:
$$M_2 \frac{d^2 x_2}{dt^2} + B_3 \frac{dx_2}{dt} + B_2 \left(\frac{dx_2}{dt} - \frac{dx_1}{dt}\right) + K_2 (x_2 - x_1) = 0$$
Regrouping terms:
$$-B_2 \frac{dx_1}{dt} - K_2 x_1 + M_2 \frac{d^2 x_2}{dt^2} + (B_2 + B_3) \frac{dx_2}{dt} + K_2 x_2 = 0 \quad \text{--- (Equation 2)}$$

Assuming zero initial conditions ($x_1(0) = \dot{x}_1(0) = x_2(0) = \dot{x}_2(0) = 0$) and taking the unilateral Laplace transform on both differential equations:
$$\left[M_1 s^2 + (B_1 + B_2)s + (K_1 + K_2)\right] X_1(s) - (B_2 s + K_2) X_2(s) = F(s) \quad \text{--- (Eq. 3)}$$
$$-(B_2 s + K_2) X_1(s) + \left[M_2 s^2 + (B_2 + B_3)s + K_2\right] X_2(s) = 0 \quad \text{--- (Eq. 4)}$$

We can cast these simultaneous algebraic equations into compact matrix form:
$$\begin{bmatrix} M_1 s^2 + (B_1 + B_2)s + (K_1 + K_2) & -(B_2 s + K_2) \\ -(B_2 s + K_2) & M_2 s^2 + (B_2 + B_3)s + K_2 \end{bmatrix} \begin{bmatrix} X_1(s) \\ X_2(s) \end{bmatrix} = \begin{bmatrix} F(s) \\ 0 \end{bmatrix}$$

Let $\Delta(s)$ denote the determinant of the mechanical impedance matrix:
$$\Delta(s) = \left[M_1 s^2 + (B_1 + B_2)s + (K_1 + K_2)\right]\left[M_2 s^2 + (B_2 + B_3)s + K_2\right] - (B_2 s + K_2)^2$$
Expanding this characteristic determinant:
$$\Delta(s) = M_1 M_2 s^4 + \left[M_1(B_2 + B_3) + M_2(B_1 + B_2)\right] s^3 + \left[M_1 K_2 + M_2(K_1 + K_2) + (B_1 + B_2)(B_2 + B_3) - B_2^2\right] s^2 + \left[(B_1 + B_2)K_2 + (B_2 + B_3)(K_1 + K_2) - 2 B_2 K_2\right] s + \left[(K_1 + K_2)K_2 - K_2^2\right]$$
Simplifying the constant and linear coefficients:
$$\Delta(s) = M_1 M_2 s^4 + \left[M_1(B_2 + B_3) + M_2(B_1 + B_2)\right] s^3 + \left[M_1 K_2 + M_2(K_1 + K_2) + B_1 B_2 + B_1 B_3 + B_2 B_3\right] s^2 + \left[B_1 K_2 + B_2 K_1 + B_3(K_1 + K_2)\right] s + K_1 K_2$$

Using Cramer's rule to find the output displacement of the unforced secondary mass $X_2(s)$:
$$X_2(s) = \frac{\det \begin{bmatrix} M_1 s^2 + (B_1 + B_2)s + (K_1 + K_2) & F(s) \\ -(B_2 s + K_2) & 0 \end{bmatrix}}{\Delta(s)} = \frac{(B_2 s + K_2) F(s)}{\Delta(s)}$$
The overall transfer function governing the displacement response of mass $M_2$ with respect to the input force $F(s)$ is:
$$\frac{X_2(s)}{F(s)} = \frac{B_2 s + K_2}{\Delta(s)}$$
Similarly, the driving-point transfer function for mass $M_1$ is:
$$\frac{X_1(s)}{F(s)} = \frac{M_2 s^2 + (B_2 + B_3)s + K_2}{\Delta(s)}$$
These transfer functions clearly reveal that the poles of the system are determined exclusively by the roots of the system determinant $\Delta(s) = 0$, governing the natural frequencies and damping ratios of the mechanical structure.
"""
    },
    {
        "qid": "lcs-q4",
        "marks": 7,
        "type": "Long Derivation",
        "title": "Block Diagram Reduction Algebra Rules and Step-by-Step System Reduction",
        "yt_query": "block diagram reduction rules step by step solved problem control systems",
        "img_path": "images/lcs/block_diagram_reduction_steps.png",
        "img_caption": "Figure 1.4: Multi-Loop Control System Block Diagram and Successive Reduction Stages",
        "answer": r"""
A complex linear feedback control system can be visually represented by a block diagram consisting of unidirectional operational blocks, summing junctions, and branch (take-off) points. Block diagram algebra provides a systematic algebraic mechanism for simplifying intricate multi-loop configurations into a single equivalent closed-loop transfer function.

The fundamental canonical transformation rules are derived as follows:
1. Cascaded (Series) Blocks: When two blocks with transfer functions $G_1(s)$ and $G_2(s)$ are connected in series such that the output of $G_1$ enters $G_2$ without loading effects:
$$X_2(s) = G_1(s) X_1(s), \quad Y(s) = G_2(s) X_2(s) \implies Y(s) = G_1(s) G_2(s) X_1(s)$$
The equivalent transfer function is the direct product: $G_{eq}(s) = G_1(s) G_2(s)$.

2. Parallel Blocks: When an identical input signal $X(s)$ branches into two parallel paths summed together:
$$Y(s) = G_1(s) X(s) \pm G_2(s) X(s) = [G_1(s) \pm G_2(s)] X(s) \implies G_{eq}(s) = G_1(s) \pm G_2(s)$$

3. Moving a Summing Point Ahead of a Block: Moving a summing point from the input of block $G(s)$ to its output requires inserting a block $G(s)$ into the secondary input path so that the signal entering the sum is properly scaled by $G(s)$:
$$Y(s) = G(s)[X_1(s) \pm X_2(s)] = G(s) X_1(s) \pm G(s) X_2(s)$$

4. Moving a Summing Point Behind a Block: Moving a summing point from the output of block $G(s)$ to its input requires introducing a block with transfer function $\frac{1}{G(s)}$ in the secondary incoming line.

5. Moving a Take-off Point Ahead of a Block: When a branch point situated before block $G(s)$ is moved to its output, the branched signal would otherwise be magnified by $G(s)$. To preserve the original signal, a block $\frac{1}{G(s)}$ must be placed in the newly tapped branch.

6. Moving a Take-off Point Behind a Block: Moving a pick-off point from after block $G(s)$ to before it requires placing a block $G(s)$ in the tapped line.

7. Canonical Negative Feedback Loop Closure: Consider a forward path $G(s)$ and a feedback element $H(s)$ connected to a summing junction with reference input $R(s)$:
The actuating error signal is $E(s) = R(s) - B(s) = R(s) - H(s) C(s)$.
The forward path output is:
$$C(s) = G(s) E(s) = G(s)[R(s) - H(s) C(s)] = G(s) R(s) - G(s) H(s) C(s)$$
Collecting output terms on the left-hand side:
$$C(s)[1 + G(s) H(s)] = G(s) R(s)$$
Dividing both sides by $[1 + G(s)H(s)] R(s)$ yields the celebrated closed-loop feedback formula:
$$\frac{C(s)}{R(s)} = \frac{G(s)}{1 + G(s) H(s)}$$
For positive feedback, the denominator becomes $1 - G(s)H(s)$.

Now consider a typical KTU university examination multi-loop problem:
A system has forward path blocks $G_1, G_2, G_3, G_4$ connected in series, with three overlapping feedback loops:
- An internal minor feedback loop $H_1$ around block $G_3$.
- An intermediate feedback loop $H_2$ originating after $G_4$ and feeding back to a summing point between $G_1$ and $G_2$.
- An overall unity negative feedback loop ($H_3 = 1$) from output $C(s)$ to the primary input summing junction.

We reduce the system systematically in four distinct stages:
Stage 1 (Eliminate the internal loop around $G_3$):
The minor loop contains forward block $G_3$ and feedback block $H_1$ with negative feedback. Replacing this loop with its equivalent single block $G_{a}$:
$$G_a(s) = \frac{G_3(s)}{1 + G_3(s) H_1(s)}$$

Stage 2 (Combine cascaded blocks in forward branch):
Block $G_2$, the newly simplified block $G_a$, and block $G_4$ are now connected strictly in series. Multiplying their transfer functions produces:
$$G_b(s) = G_2(s) \cdot G_a(s) \cdot G_4(s) = \frac{G_2(s) G_3(s) G_4(s)}{1 + G_3(s) H_1(s)}$$

Stage 3 (Eliminate the secondary feedback loop with $H_2$):
The forward path of this intermediate loop is $G_b(s)$ and its feedback path is $H_2(s)$. Applying the closed-loop reduction formula:
$$G_c(s) = \frac{G_b(s)}{1 + G_b(s) H_2(s)} = \frac{\frac{G_2 G_3 G_4}{1 + G_3 H_1}}{1 + \left(\frac{G_2 G_3 G_4}{1 + G_3 H_1}\right) H_2} = \frac{G_2 G_3 G_4}{1 + G_3 H_1 + G_2 G_3 G_4 H_2}$$

Stage 4 (Combine with forward block $G_1$ and resolve overall unity feedback):
Block $G_1$ is in cascade with $G_c(s)$, creating the overall forward transfer function $G(s)$:
$$G(s) = G_1(s) G_c(s) = \frac{G_1 G_2 G_3 G_4}{1 + G_3 H_1 + G_2 G_3 G_4 H_2}$$
Finally, eliminating the overall unity feedback loop ($H_3 = 1$):
$$\frac{C(s)}{R(s)} = \frac{G(s)}{1 + G(s)(1)} = \frac{\frac{G_1 G_2 G_3 G_4}{1 + G_3 H_1 + G_2 G_3 G_4 H_2}}{1 + \frac{G_1 G_2 G_3 G_4}{1 + G_3 H_1 + G_2 G_3 G_4 H_2}}$$
$$\frac{C(s)}{R(s)} = \frac{G_1 G_2 G_3 G_4}{1 + G_3 H_1 + G_2 G_3 G_4 H_2 + G_1 G_2 G_3 G_4}$$
This explicit final expression gives the closed-loop transfer function of the complete multi-loop control system.
"""
    },
    {
        "qid": "lcs-q5",
        "marks": 7,
        "type": "Long Derivation",
        "title": "Signal Flow Graphs and Mason's Gain Formula with Comprehensive Application",
        "yt_query": "mason gain formula signal flow graph control systems solved example",
        "img_path": "images/lcs/signal_flow_graph_masons_rule.png",
        "img_caption": "Figure 1.5: Topological Signal Flow Graph with Forward Paths and Non-Touching Feedback Loops",
        "answer": r"""
A Signal Flow Graph (SFG), originated by S. J. Mason, is a directed topological network consisting of nodes interconnected by directed branches. It provides an alternative graphical representation of linear algebraic equations describing dynamic systems. Unlike block diagram reduction which requires step-by-step graphical transformations, Mason's Gain Formula allows direct inspection of the graph topology to calculate the overall system transfer function in a single analytical step.

The foundational topological definitions of a Signal Flow Graph are:
1. Node: A point representing a system variable or signal. An input node (source) has only outgoing branches. An output node (sink) has only incoming branches. A mixed node has both incoming and outgoing branches.
2. Branch: A directed line segment connecting two nodes. The signal traversing the branch is multiplied by the branch gain, termed transmittance.
3. Forward Path: A continuous directed path originating at an input node and terminating at an output node along which no individual node is traversed more than once. The forward path gain $P_k$ is the product of all branch transmittances along path $k$.
4. Loop: A closed continuous path that starts and ends at the exact same node, encountering no other node more than once along its path. The loop gain $L_m$ is the product of all transmittances forming the closed loop.
5. Non-Touching Loops: Two or more loops are said to be non-touching if they share absolutely no common physical nodes.

Mason's Gain Formula expresses the overall graph transmittance (closed-loop transfer function) $T = \frac{C(s)}{R(s)}$ as:
$$T = \frac{C(s)}{R(s)} = \frac{1}{\Delta} \sum_{k=1}^N P_k \Delta_k$$
where:
- $N$ is the total number of distinct forward paths from input to output.
- $P_k$ is the path gain of the $k$-th forward path.
- $\Delta$ is the system graph determinant, defined by the alternating series:
$$\Delta = 1 - \sum L_a + \sum L_b L_c - \sum L_d L_e L_f + \dots$$
  - $\sum L_a$ = sum of all individual loop gains.
  - $\sum L_b L_c$ = sum of the gain products of all possible combinations of two non-touching loops.
  - $\sum L_d L_e L_f$ = sum of the gain products of all possible combinations of three non-touching loops.
- $\Delta_k$ is the path cofactor of the $k$-th forward path. It is evaluated as the determinant of that portion of the signal flow graph that does not touch any node of the $k$-th forward path (obtained by crossing out all loops touching the $k$-th forward path).

To demonstrate the full mathematical execution of Mason's Gain Formula, consider a representative KTU examination problem with the following branch transmittances between nodes $y_1$ (input $R$) to $y_6$ (output $C$):
Nodes: $y_1, y_2, y_3, y_4, y_5, y_6$.
Branches:
- $y_1 \to y_2$ with gain $1$
- $y_2 \to y_3$ with gain $G_1$
- $y_3 \to y_4$ with gain $G_2$
- $y_4 \to y_5$ with gain $G_3$
- $y_5 \to y_6$ with gain $G_4$
Feedforward Branch:
- $y_2 \to y_5$ with gain $G_5$
Feedback Branches:
- $y_4 \to y_3$ with gain $-H_1$
- $y_5 \to y_4$ with gain $-H_2$
- $y_6 \to y_2$ with gain $-H_3$

Step 1: Identify all forward paths and determine their gains:
- Path 1: $y_1 \to y_2 \to y_3 \to y_4 \to y_5 \to y_6$
  $$P_1 = (1)(G_1)(G_2)(G_3)(G_4) = G_1 G_2 G_3 G_4$$
- Path 2: $y_1 \to y_2 \to y_5 \to y_6$
  $$P_2 = (1)(G_5)(G_4) = G_4 G_5$$
Total number of forward paths $N = 2$.

Step 2: Identify all individual closed loops and their gains:
- Loop 1 ($y_3 \to y_4 \to y_3$):
  $$L_1 = (G_2)(-H_1) = -G_2 H_1$$
- Loop 2 ($y_4 \to y_5 \to y_4$):
  $$L_2 = (G_3)(-H_2) = -G_3 H_2$$
- Loop 3 ($y_2 \to y_3 \to y_4 \to y_5 \to y_6 \to y_2$):
  $$L_3 = (G_1)(G_2)(G_3)(G_4)(-H_3) = -G_1 G_2 G_3 G_4 H_3$$
- Loop 4 ($y_2 \to y_5 \to y_6 \to y_2$):
  $$L_4 = (G_5)(G_4)(-H_3) = -G_4 G_5 H_3$$

Step 3: Identify pairs of non-touching loops:
Checking nodes:
- Loop 1 has nodes $\{y_3, y_4\}$.
- Loop 2 has nodes $\{y_4, y_5\}$. They touch at node $y_4$.
- Loop 3 has nodes $\{y_2, y_3, y_4, y_5, y_6\}$. It touches all loops.
- Loop 4 has nodes $\{y_2, y_5, y_6\}$. It shares node $y_5$ with Loop 2, and shares nodes $y_2, y_5, y_6$ with Loop 3.
However, compare Loop 1 $\{y_3, y_4\}$ and Loop 4 $\{y_2, y_5, y_6\}$:
They share no common nodes ($\{y_3, y_4\} \cap \{y_2, y_5, y_6\} = \emptyset$).
Therefore, there exists exactly one pair of non-touching loops:
$$L_1 L_4 = (-G_2 H_1)(-G_4 G_5 H_3) = G_1 G_4 G_5 H_1 H_3 \quad \text{Wait, } L_1 L_4 = G_2 G_4 G_5 H_1 H_3$$
There are no combinations of three non-touching loops.

Step 4: Compute the graph determinant $\Delta$:
$$\Delta = 1 - (L_1 + L_2 + L_3 + L_4) + (L_1 L_4)$$
$$\Delta = 1 - (-G_2 H_1 - G_3 H_2 - G_1 G_2 G_3 G_4 H_3 - G_4 G_5 H_3) + (G_2 G_4 G_5 H_1 H_3)$$
$$\Delta = 1 + G_2 H_1 + G_3 H_2 + G_1 G_2 G_3 G_4 H_3 + G_4 G_5 H_3 + G_2 G_4 G_5 H_1 H_3$$

Step 5: Determine path cofactors $\Delta_1$ and $\Delta_2$:
- For Path 1 ($P_1 = G_1 G_2 G_3 G_4$): This path contains nodes $\{y_1, y_2, y_3, y_4, y_5, y_6\}$. Every single loop in the graph touches at least one node of Path 1. Therefore:
  $$\Delta_1 = 1 - 0 = 1$$
- For Path 2 ($P_2 = G_4 G_5$): Path 2 traverses nodes $\{y_1, y_2, y_5, y_6\}$. 
  Examining the loops:
  - Loop 2, Loop 3, Loop 4 all touch nodes $y_2, y_5,$ or $y_6$.
  - Loop 1 has nodes $\{y_3, y_4\}$, neither of which is touched by Path 2.
  Therefore, Loop 1 does not touch Path 2!
  $$\Delta_2 = 1 - L_1 = 1 - (-G_2 H_1) = 1 + G_2 H_1$$

Step 6: Calculate the overall closed-loop transfer function:
$$\frac{C(s)}{R(s)} = \frac{P_1 \Delta_1 + P_2 \Delta_2}{\Delta} = \frac{(G_1 G_2 G_3 G_4)(1) + (G_4 G_5)(1 + G_2 H_1)}{1 + G_2 H_1 + G_3 H_2 + G_1 G_2 G_3 G_4 H_3 + G_4 G_5 H_3 + G_2 G_4 G_5 H_1 H_3}$$
Expanding the numerator:
$$\frac{C(s)}{R(s)} = \frac{G_1 G_2 G_3 G_4 + G_4 G_5 + G_2 G_4 G_5 H_1}{1 + G_2 H_1 + G_3 H_2 + G_1 G_2 G_3 G_4 H_3 + G_4 G_5 H_3 + G_2 G_4 G_5 H_1 H_3}$$
This shows how Mason's Gain formula evaluates the transfer function of complex feedback architectures without any block-shifting algebraic manipulations.
"""
    }
]
