# -*- coding: utf-8 -*-
"""
Content generator for Subject 1: Advanced Control Systems (EET401)
KTU 2019 Scheme Syllabus Comprehensive Question Bank.
All answers are elaborated in paragraph format without bullet points.
All strings are raw strings (r\"\"\"...\"\"\") to prevent any LaTeX escape corruptions.
"""

ACS_MODULES = [
    {
        "module_id": "acs-m1",
        "module_num": "Module 1",
        "module_title": "State Space Analysis Basics, Modeling & Canonical Forms",
        "questions": [
            {
                "qid": "acs-q1",
                "marks": 3,
                "type": "Short Answer",
                "title": "State Space Concepts: State, State Variables, State Vector, and State Space",
                "yt_query": "state space analysis state variables state vector state space control systems",
                "img_path": "images/acs/state_space_concept.png",
                "img_caption": "Figure 1.1: Multi-dimensional State Space Representation with Trajectory Vector",
                "answer": r"""
In the foundational analysis of continuous and discrete dynamic systems, the state of a dynamical system is defined as the minimal set of variables such that the knowledge of these variables at an initial time instant, together with the complete specification of the input excitation for all subsequent times, completely determines the future state and output behavior of the system. Rather than treating physical systems as high-order input-output 'black boxes' as done in classical transfer function techniques, the state concept provides a comprehensive internal view of the system energy storage dynamics. Every physical system possesses inherent energy storage mechanisms, such as inductors and capacitors in electrical circuits, or masses and springs in mechanical structures. The state variables directly quantify the energy stored in these elements at any given instant.

State variables are formally chosen as the smallest possible subset of physical or mathematical variables that capture the complete historical accumulation of energy in the system. If a system contains $n$ independent energy storage components, exactly $n$ state variables, denoted by $x_1(t), x_2(t), \dots, x_n(t)$, are required to fully model the internal system dynamics. For example, in an electrical network, the current flowing through an inductor and the potential difference across a capacitor naturally constitute state variables because neither magnetic flux nor electric charge can change discontinuously in physical circuits. These state variables do not need to be physically measurable directly, although choosing measurable physical quantities is highly advantageous for practical controller implementation.

When these individual state variables are grouped together in a structured column array, they form the state vector, mathematically expressed as $x(t) = \begin{bmatrix} x_1(t) & x_2(t) & \dots & x_n(t) \end{bmatrix}^T$. The geometric space spanned by these $n$ mutually independent coordinate axes is known as the state space. In this $n$-dimensional Euclidean space $\mathbb{R}^n$, the operating condition of the system at any given moment in time corresponds to a single point, known as the state point. As time elapses and the system evolves under its internal dynamics and external control excitations, this state point traces out a continuous path called the state trajectory. State space analysis therefore transforms the solution of high-order scalar differential equations into the intuitive geometric study of first-order vector trajectories, accommodating multiple-input multiple-output (MIMO) architectures and time-varying parameters with mathematical elegance.
"""
            },
            {
                "qid": "acs-q2",
                "marks": 3,
                "type": "Short Answer",
                "title": "Phase Variables and Continuous-Time Input-Output Formulation",
                "yt_query": "phase variables state space modeling control systems",
                "img_path": "images/acs/phase_variables_flow.png",
                "img_caption": "Figure 1.2: Successive Integrator Chain Generating Phase Variables",
                "answer": r"""
Phase variables represent a particular mathematical choice of state variables where each successive state variable is defined as the exact time derivative of the preceding state variable. When an $n$-th order linear physical system is described by a single scalar differential equation relating the output $y(t)$ to the control input $u(t)$, the output variable itself is chosen as the first state variable, denoted $x_1(t) = y(t)$. The second state variable is selected as the first derivative of the output, $x_2(t) = \dot{y}(t) = \dot{x}_1(t)$, the third state variable becomes the second derivative $x_3(t) = \ddot{y}(t) = \dot{x}_2(t)$, and this pattern proceeds systematically until the $n$-th state variable is defined as the $(n-1)$-th time derivative of the output, $x_n(t) = y^{(n-1)}(t) = \dot{x}_{n-1}(t)$.

The mathematical significance of phase variables lies in the resulting structure of the state transition matrix and system dynamics. Because each state equation simply equates the derivative of one state variable to the next state variable, the state equation takes on the famous companion form. In this realization, the first $n-1$ rows of the state matrix $A$ consist solely of zeros with ones along the superdiagonal, while the final $n$-th row contains the negative coefficients of the system characteristic equation. This structure is universally employed in modern control engineering because it directly maps an input-output transfer function into a state model without requiring internal knowledge of physical electrical or mechanical components.

However, phase variables possess distinct characteristics compared to physical state variables. While physical state variables are associated with real energy-storing quantities like voltages and currents, phase variables are often mathematical abstractions representing higher-order rates of change. In noisy real-world environments, obtaining accurate higher-order derivatives like jerk or second-derivative terms is extremely susceptible to high-frequency sensor noise. Consequently, while phase variable canonical forms are exceptionally convenient for mathematical derivations, state feedback control synthesis, and computer simulation, state observers are frequently required in physical practice to reconstruct these derivative states reliably.
"""
            },
            {
                "qid": "acs-q3",
                "marks": 3,
                "type": "Short Answer",
                "title": "Block Diagram Illustration of Continuous-Time LTI State and Output Equations",
                "yt_query": "block diagram state equation continuous time LTI system",
                "img_path": "images/acs/lti_state_block_diagram.png",
                "img_caption": "Figure 1.3: Standard Integrator-Based Block Diagram of Continuous LTI System",
                "answer": r"""
A continuous-time linear time-invariant dynamical system is mathematically governed by two fundamental matrix equations, namely the state differential equation $\dot{x}(t) = A x(t) + B u(t)$ and the algebraic output measurement equation $y(t) = C x(t) + D u(t)$. In this formulation, $x(t) \in \mathbb{R}^n$ represents the internal state vector, $u(t) \in \mathbb{R}^m$ denotes the control input vector, and $y(t) \in \mathbb{R}^p$ represents the observed system output vector. The system matrix $A$ dictates internal unforced dynamics, the input matrix $B$ couples external control inputs into state changes, the output matrix $C$ translates internal states into measurable outputs, and the direct transmission matrix $D$ represents instantaneous direct feedthrough from input to output.

To represent this system visually in block diagram form, the central operational block consists of a bank of $n$ parallel integrators, collectively represented as an integrator block with transfer matrix $\frac{1}{s} I$ in the Laplace domain. The input to this integrator block is the state derivative vector $\dot{x}(t)$, and the output resulting from integration is the state vector $x(t)$. The state derivative is synthesized by summing two distinct vector signals at a summing junction: the internal state feedback term obtained by multiplying the state vector $x(t)$ through the matrix block $A$, and the forced control term obtained by processing the external input vector $u(t)$ through the input matrix block $B$.

Simultaneously, the system output vector $y(t)$ is generated at a separate summing junction by adding two contributions. The primary contribution arises from the internal state vector $x(t)$ routed through the observation matrix $C$. The secondary contribution is the direct feedthrough component formed by passing the input vector $u(t)$ through the matrix $D$. In the vast majority of physical engineering systems, where the transfer function is strictly proper, there is no direct instantaneous feedthrough, causing matrix $D$ to be zero. This block diagram clearly illustrates that integrators serve as the sole dynamic memory elements of the system, while the matrix blocks $A, B, C, D$ function as pure static algebraic gains.
"""
            },
            {
                "qid": "acs-q4",
                "marks": 3,
                "type": "Short Answer",
                "title": "Justification of Non-Uniqueness of State Space Models via Similarity Transformation",
                "yt_query": "non uniqueness of state space similarity transformation",
                "img_path": "images/acs/similarity_transformation.png",
                "img_caption": "Figure 1.4: Linear Coordinate Transformation between State Bases",
                "answer": r"""
The state space representation of any physical dynamic system is inherently non-unique, which means that an infinite variety of different state space models can represent the identical input-output physical behavior. The fundamental physical reality of a system—such as its input-output transfer function, impulse response, and natural dynamic modes—remains completely invariant regardless of the coordinate system chosen to describe the internal states. Because the state vector essentially represents a set of basis coordinates in an $n$-dimensional vector space, any non-singular linear coordinate transformation produces an equally valid alternative state space description.

Mathematically, let the original state space model be described by the pair of equations $\dot{x}(t) = A x(t) + B u(t)$ and $y(t) = C x(t) + D u(t)$. If we define a transformed state vector $z(t)$ through an invertible similarity transformation matrix $P$ such that $x(t) = P z(t)$, or equivalently $z(t) = P^{-1} x(t)$, substituting this into the original state equation yields $P \dot{z}(t) = A P z(t) + B u(t)$. Premultiplying both sides by the matrix inverse $P^{-1}$ yields the transformed state equation $\dot{z}(t) = \bar{A} z(t) + \bar{B} u(t)$, where the new system matrix is $\bar{A} = P^{-1} A P$ and the new input matrix is $\bar{B} = P^{-1} B$. Substituting the transformation into the output equation similarly produces $y(t) = \bar{C} z(t) + D u(t)$, where $\bar{C} = C P$.

Although the numerical values of the matrices $\bar{A}, \bar{B}, \bar{C}$ change under this transformation, the input-output transfer function is strictly invariant. The transfer function of the transformed system is given by $\bar{G}(s) = \bar{C}(sI - \bar{A})^{-1}\bar{B} + D = C P (s P^{-1} P - P^{-1} A P)^{-1} P^{-1} B + D = C P [P^{-1}(sI - A)P]^{-1} P^{-1} B + D = C P P^{-1}(sI - A)^{-1} P P^{-1} B + D = C(sI - A)^{-1}B + D = G(s)$. Furthermore, the eigenvalues of matrix $\bar{A}$ are identical to those of matrix $A$ because $\det(sI - P^{-1}AP) = \det[P^{-1}(sI - A)P] = \det(P^{-1})\det(sI - A)\det(P) = \det(sI - A)$. This confirms that system poles and stability characteristics are invariant under coordinate transformations, providing control engineers the freedom to transform systems into convenient canonical forms like controllable, observable, or diagonal canonical realizations.
"""
            },
            {
                "qid": "acs-q4b",
                "marks": 3,
                "type": "Short Answer",
                "title": "Derivation of Transfer Function from State Space Equations",
                "yt_query": "derivation of transfer function from state space model C(sI-A)^-1B+D",
                "img_path": "images/acs/transfer_function_derivation.png",
                "img_caption": "Figure 1.4B: Resolvent Matrix Mapping State Equations to Input-Output Transfer Function",
                "answer": r"""
The mathematical derivation connecting the internal state space description to the classical external input-output transfer function represents a cornerstone of linear system theory. Consider a continuous-time linear time-invariant system governed by the standard matrix differential state equation $\dot{x}(t) = A x(t) + B u(t)$ and the static algebraic output equation $y(t) = C x(t) + D u(t)$, where $x(t) \in \mathbb{R}^n$ is the state vector, $u(t) \in \mathbb{R}^m$ is the control input, and $y(t) \in \mathbb{R}^p$ is the observed output. By fundamental definition, the transfer function $G(s)$ is the ratio of the Laplace transform of the output $Y(s)$ to the Laplace transform of the input $U(s)$, under the strict assumption that all initial state conditions are identically zero ($x(0) = 0$).

Taking the unilateral Laplace transform on both sides of the state differential equation yields $s X(s) - x(0) = A X(s) + B U(s)$. Imposing relaxed initial conditions $x(0) = 0$ simplifies this equation to $s X(s) - A X(s) = B U(s)$. Factoring out the state transform vector $X(s)$ gives $(sI - A)X(s) = B U(s)$, where $I$ represents the $n \times n$ identity matrix. Provided that the complex frequency variable $s$ is not an eigenvalue of matrix $A$, the characteristic matrix $(sI - A)$ is strictly non-singular and invertible. Premultiplying both sides by the matrix inverse $(sI - A)^{-1}$, designated as the resolvent matrix $\Phi(s)$, yields the algebraic frequency-domain expression for the internal state vector:
$$X(s) = (sI - A)^{-1} B U(s)$$

Next, we take the Laplace transform of the output measurement equation: $Y(s) = C X(s) + D U(s)$. Substituting the derived state transform expression $X(s)$ directly into this output relationship yields:
$$Y(s) = C \left[ (sI - A)^{-1} B U(s) \right] + D U(s) = \left[ C (sI - A)^{-1} B + D \right] U(s)$$
Dividing by the scalar input transform $U(s)$ yields the celebrated matrix transfer function formula:
$$G(s) = \frac{Y(s)}{U(s)} = C (sI - A)^{-1} B + D = \frac{C \text{ adj}(sI - A) B}{\det(sI - A)} + D$$
This formulation reveals that the poles of the transfer function $G(s)$ are precisely the roots of the characteristic polynomial $\det(sI - A) = 0$, meaning that the natural system poles are identical to the eigenvalues of the state matrix $A$ (unless pole-zero cancellations occur due to uncontrollable or unobservable modes).
"""
            },
            {
                "qid": "acs-q5",
                "marks": 7,
                "type": "Long Derivation",
                "title": "Comprehensive State-Space Modeling of a Series RLC Circuit",
                "yt_query": "state space modeling series RLC circuit derivation",
                "img_path": "images/acs/series_rlc_circuit.png",
                "img_caption": "Figure 1.5: Schematic and State Space Flow of Series RLC Circuit",
                "answer": r"""
To establish the complete state-space mathematical model of an electrical network, one must identify the independent energy-storing elements and associate their physical variables with system states. Consider a classical series RLC circuit excited by an external time-varying voltage source $v(t)$, consisting of a resistor of resistance $R$, an inductor of inductance $L$, and a capacitor of capacitance $C$ all connected in a closed series loop. In any electrical circuit, the magnetic field energy stored in an inductor is given by $E_L = \frac{1}{2} L i_L^2$ and the electric field energy stored in a capacitor is given by $E_C = \frac{1}{2} C v_C^2$. Because electric charge and magnetic flux linkages cannot change instantaneously without requiring infinite power, the inductor current $i_L(t)$ and the capacitor voltage $v_C(t)$ represent the natural physical state variables of the electrical network.

We begin by formally designating the state vector components as $x_1(t) = i_L(t)$ and $x_2(t) = v_C(t)$, with the input excitation defined as $u(t) = v(t)$. Applying Kirchhoff's Voltage Law (KVL) around the single closed series loop, the algebraic sum of potential drops across all components must equal the applied source voltage:
$$v(t) = v_R(t) + v_L(t) + v_C(t)$$
Using the fundamental elemental constitutive relationships, the voltage across the resistor is governed by Ohm's law as $v_R(t) = R i_L(t)$, and the voltage across the inductor is proportional to the time rate of change of its current, $v_L(t) = L \frac{d i_L(t)}{dt}$. Substituting these constitutive equations into the KVL loop equation produces the governing dynamic differential equation:
$$L \frac{d i_L(t)}{dt} + R i_L(t) + v_C(t) = v(t)$$
Rearranging this equation to express the first state derivative $\dot{x}_1(t) = \frac{d i_L}{dt}$ in terms of the state variables and the external voltage input yields:
$$\frac{d i_L(t)}{dt} = -\frac{R}{L} i_L(t) - \frac{1}{L} v_C(t) + \frac{1}{L} v(t)$$
$$\dot{x}_1(t) = -\frac{R}{L} x_1(t) - \frac{1}{L} x_2(t) + \frac{1}{L} u(t)$$

Next, we establish the second state differential equation by examining the current flowing through the capacitor. Because all elements are connected strictly in series, the identical current $i_L(t)$ flows through both the inductor and the capacitor. According to the constitutive law of capacitance, the current entering a capacitor is directly proportional to the time rate of change of the voltage across its terminals, given by $i_C(t) = C \frac{d v_C(t)}{dt}$. Equating the capacitor current to the loop current yields:
$$C \frac{d v_C(t)}{dt} = i_L(t)$$
Dividing by capacitance $C$ and expressing this relation in state variable notation yields our second first-order state equation:
$$\frac{d v_C(t)}{dt} = \frac{1}{C} i_L(t)$$
$$\dot{x}_2(t) = \frac{1}{C} x_1(t) + 0 \cdot x_2(t) + 0 \cdot u(t)$$

Grouping these two first-order coupled differential equations into standard matrix-vector format $\dot{x}(t) = A x(t) + B u(t)$ produces:
$$\begin{bmatrix} \dot{x}_1(t) \\ \dot{x}_2(t) \end{bmatrix} = \begin{bmatrix} -\frac{R}{L} & -\frac{1}{L} \\ \frac{1}{C} & 0 \end{bmatrix} \begin{bmatrix} x_1(t) \\ x_2(t) \end{bmatrix} + \begin{bmatrix} \frac{1}{L} \\ 0 \end{bmatrix} u(t)$$
Here, the state matrix $A$ and the input matrix $B$ are defined explicitly as:
$$A = \begin{bmatrix} -\frac{R}{L} & -\frac{1}{L} \\ \frac{1}{C} & 0 \end{bmatrix}, \quad B = \begin{bmatrix} \frac{1}{L} \\ 0 \end{bmatrix}$$
The characteristic polynomial of the unforced system is obtained from $\det(sI - A) = s\left(s + \frac{R}{L}\right) + \frac{1}{LC} = s^2 + \frac{R}{L}s + \frac{1}{LC}$, which exactly matches the classical second-order characteristic equation with natural frequency $\omega_n = \frac{1}{\sqrt{LC}}$ and damping ratio $\zeta = \frac{R}{2}\sqrt{\frac{C}{L}}$.

Finally, we formulate the output measurement equation $y(t) = C_{out} x(t) + D u(t)$. Depending on the specific engineering instrumentation requirement, if the output of interest is chosen as the voltage across the capacitor, $y(t) = v_C(t) = x_2(t)$, the output matrices become $C_{out} = \begin{bmatrix} 0 & 1 \end{bmatrix}$ and $D = 0$. Alternatively, if the output is measured across the resistor, $y(t) = v_R(t) = R i_L(t) = R x_1(t)$, the output matrices become $C_{out} = \begin{bmatrix} R & 0 \end{bmatrix}$ and $D = 0$. In the event that the output is taken across the inductor, $y(t) = v_L(t) = v(t) - R i_L(t) - v_C(t) = -R x_1(t) - x_2(t) + u(t)$, resulting in $C_{out} = \begin{bmatrix} -R & -1 \end{bmatrix}$ and a direct feedthrough scalar $D = 1$. This demonstrates how state space formulations effortlessly handle any desired system output variable without modifying the core state matrix $A$.
"""
            },
            {
                "qid": "acs-q6",
                "marks": 7,
                "type": "Long Derivation",
                "title": "Electromechanical Derivation of the State Model of an Armature-Controlled DC Motor",
                "yt_query": "state model armature controlled DC motor derivation",
                "img_path": "images/acs/armature_dc_motor.png",
                "img_caption": "Figure 1.6: Electromechanical Schematic and State Flow Diagram of Armature-Controlled DC Motor",
                "answer": r"""
An armature-controlled direct-current (DC) motor represents one of the most prominent electromechanical actuators in industrial servomechanisms, robotics, and precision position control. In this operational mode, the field current is held strictly constant by a permanent magnet or a fixed DC field excitation source, ensuring that the magnetic flux per pole $\phi$ remains constant throughout operation. The speed and position of the motor are controlled entirely by varying the armature terminal voltage $e_a(t)$. The system comprises two distinct yet deeply coupled physical domains: an electrical circuit domain governing armature current flow, and a mechanical rotational domain governing rotor acceleration, inertia, and frictional resistance.

The electrical subsystem is described by writing Kirchhoff's Voltage Law across the armature circuit. The applied armature voltage $e_a(t)$ must overcome the resistive voltage drop across armature resistance $R_a$, the inductive drop across armature winding inductance $L_a$, and the generated rotational back electromotive force (EMF) $e_b(t)$ induced in the rotor conductors as they rotate through the magnetic field:
$$e_a(t) = R_a i_a(t) + L_a \frac{d i_a(t)}{dt} + e_b(t)$$
Because the magnetic field flux is constant, the back-EMF is directly proportional to the rotational angular velocity of the rotor shaft $\omega_m(t)$, governed by the physical relationship $e_b(t) = K_b \omega_m(t)$, where $K_b$ is the motor back-EMF constant expressed in volts per radian per second. Substituting this constitutive relationship into the armature voltage loop yields:
$$L_a \frac{d i_a(t)}{dt} + R_a i_a(t) + K_b \omega_m(t) = e_a(t)$$
Rearranging this differential equation to express the rate of change of armature current yields our first state equation:
$$\frac{d i_a(t)}{dt} = -\frac{R_a}{L_a} i_a(t) - \frac{K_b}{L_a} \omega_m(t) + \frac{1}{L_a} e_a(t)$$

The mechanical rotational subsystem is modeled using Newton's second law for angular motion. The electromechanical torque $T_m(t)$ generated by the motor rotor is directly proportional to the armature current, governed by $T_m(t) = K_t i_a(t)$, where $K_t$ is the motor torque constant in Newton-meters per ampere. In SI units, the torque constant $K_t$ and the back-EMF constant $K_b$ are numerically identical. This electrodynamic torque accelerates the rotor shaft, overcoming the effective combined moment of inertia $J_m$ of the rotor and coupled load, the viscous damping friction coefficient $B_m$, and any external load disturbance torque $T_L(t)$:
$$T_m(t) = J_m \frac{d \omega_m(t)}{dt} + B_m \omega_m(t) + T_L(t)$$
Assuming for nominal design that the external disturbance load torque $T_L(t) = 0$, and substituting the torque relationship $T_m(t) = K_t i_a(t)$ into the equation of mechanical equilibrium yields:
$$J_m \frac{d \omega_m(t)}{dt} + B_m \omega_m(t) = K_t i_a(t)$$
Rearranging this differential equation to isolate the angular acceleration yields our second state equation:
$$\frac{d \omega_m(t)}{dt} = \frac{K_t}{J_m} i_a(t) - \frac{B_m}{J_m} \omega_m(t)$$

When the control objective is angular position control rather than purely speed control, an additional kinematic relationship is required linking the shaft angular position $\theta_m(t)$ to the angular velocity $\omega_m(t)$. By fundamental definition of rotational velocity, the time derivative of angular position is velocity, giving the third state equation:
$$\frac{d \theta_m(t)}{dt} = \omega_m(t)$$
We define our state vector as $x(t) = \begin{bmatrix} x_1(t) & x_2(t) & x_3(t) \end{bmatrix}^T = \begin{bmatrix} i_a(t) & \omega_m(t) & \theta_m(t) \end{bmatrix}^T$, and the control input excitation as $u(t) = e_a(t)$. Expressing the three coupled first-order differential equations in standard state-space matrix notation $\dot{x}(t) = A x(t) + B u(t)$ yields:
$$\begin{bmatrix} \dot{i}_a(t) \\ \dot{\omega}_m(t) \\ \dot{\theta}_m(t) \end{bmatrix} = \begin{bmatrix} -\frac{R_a}{L_a} & -\frac{K_b}{L_a} & 0 \\ \frac{K_t}{J_m} & -\frac{B_m}{J_m} & 0 \\ 0 & 1 & 0 \end{bmatrix} \begin{bmatrix} i_a(t) \\ \omega_m(t) \\ \theta_m(t) \end{bmatrix} + \begin{bmatrix} \frac{1}{L_a} \\ 0 \\ 0 \end{bmatrix} e_a(t)$$

To complete the model, the output equation $y(t) = C x(t) + D u(t)$ is established based on the measured physical quantity. If the actuator system is configured as a speed governor where the output of interest is the angular velocity, $y(t) = \omega_m(t) = x_2(t)$, the observation matrices become $C = \begin{bmatrix} 0 & 1 & 0 \end{bmatrix}$ and $D = 0$. If the system is deployed as a position servomechanism where output is shaft position, $y(t) = \theta_m(t) = x_3(t)$, the observation matrices become $C = \begin{bmatrix} 0 & 0 & 1 \end{bmatrix}$ and $D = 0$. The physical significance of each state variable is profound: $i_a(t)$ quantifies electrical energy stored in the armature magnetic field, $\omega_m(t)$ quantifies kinetic energy stored in the rotating mass, and $\theta_m(t)$ represents the accumulated geometric displacement. This state model serves as the universal foundation for modern speed regulation and robotic trajectory tracking.
"""
            },
            {
                "qid": "acs-q7",
                "marks": 7,
                "type": "Long Derivation",
                "title": "Canonical Forms: Derivation of Diagonal and Controllable Forms from Transfer Functions",
                "yt_query": "diagonal canonical form transfer function state space",
                "img_path": "images/acs/diagonal_canonical_form.png",
                "img_caption": "Figure 1.7: Analog Simulation Block Diagram for Diagonal Canonical Realization",
                "answer": r"""
The transformation of input-output transfer functions into structured canonical state space realizations is a central technique in modern control theory. Canonical forms reveal fundamental structural properties of dynamical systems, such as controllability, observability, and pole decoupling. Consider a third-order continuous-time dynamic system described by the rational transfer function:
$$G(s) = \frac{Y(s)}{U(s)} = \frac{4}{(s+1)(s+2)(s+3)} = \frac{4}{s^3 + 6s^2 + 11s + 6}$$
This system possesses three distinct real poles located at $s = -1, s = -2$, and $s = -3$. We demonstrate the complete analytical derivation of two vital canonical realizations: the Controllable Phase Variable Canonical Form and the Diagonal (Modal) Canonical Form.

To construct the Controllable Phase Variable Form, we express the input-output differential equation in the time domain by cross-multiplying the transfer function denominator and numerator:
$$(s^3 + 6s^2 + 11s + 6)Y(s) = 4 U(s)$$
$$\frac{d^3y(t)}{dt^3} + 6 \frac{d^2y(t)}{dt^2} + 11 \frac{dy(t)}{dt} + 6 y(t) = 4 u(t)$$
We define the phase state variables as the output and its successive time derivatives: $x_1(t) = y(t)$, $x_2(t) = \dot{y}(t) = \dot{x}_1(t)$, and $x_3(t) = \ddot{y}(t) = \dot{x}_2(t)$. Differentiating the third state variable and substituting from the governing differential equation yields $\dot{x}_3(t) = \frac{d^3y}{dt^3} = -6 x_1(t) - 11 x_2(t) - 6 x_3(t) + 4 u(t)$. Writing these relations in standard matrix format yields the companion controllable state model:
$$\begin{bmatrix} \dot{x}_1 \\ \dot{x}_2 \\ \dot{x}_3 \end{bmatrix} = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -6 & -11 & -6 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} + \begin{bmatrix} 0 \\ 0 \\ 4 \end{bmatrix} u(t), \quad y(t) = \begin{bmatrix} 1 & 0 & 0 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}$$
In this realization, the system matrix exhibits the classical companion structure, with ones along the superdiagonal and the negative coefficients of the characteristic polynomial along the bottom row.

To derive the Diagonal (Modal) Canonical Form, we decompose the transfer function into simple partial fractions. Because all three system poles are distinct, the partial fraction expansion is written as:
$$G(s) = \frac{Y(s)}{U(s)} = \frac{R_1}{s+1} + \frac{R_2}{s+2} + \frac{R_3}{s+3}$$
The residues $R_1, R_2, R_3$ are evaluated analytically using the Heaviside cover-up method:
$$R_1 = \lim_{s \to -1} (s+1) G(s) = \frac{4}{(-1+2)(-1+3)} = \frac{4}{(1)(2)} = 2$$
$$R_2 = \lim_{s \to -2} (s+2) G(s) = \frac{4}{(-2+1)(-2+3)} = \frac{4}{(-1)(1)} = -4$$
$$R_3 = \lim_{s \to -3} (s+3) G(s) = \frac{4}{(-3+1)(-3+2)} = \frac{4}{(-2)(-1)} = 2$$
Thus, the partial fraction expansion of the system response is expressed as:
$$Y(s) = \frac{2}{s+1} U(s) - \frac{4}{s+2} U(s) + \frac{2}{s+3} U(s)$$

We now define three decoupled internal modal state variables in the Laplace domain such that each state variable corresponds to the output of an individual first-order pole subsystem excited by the common input $U(s)$:
$$Z_1(s) = \frac{1}{s+1} U(s) \implies (s+1)Z_1(s) = U(s) \implies \dot{z}_1(t) = -z_1(t) + u(t)$$
$$Z_2(s) = \frac{1}{s+2} U(s) \implies (s+2)Z_2(s) = U(s) \implies \dot{z}_2(t) = -2z_2(t) + u(t)$$
$$Z_3(s) = \frac{1}{s+3} U(s) \implies (s+3)Z_3(s) = U(s) \implies \dot{z}_3(t) = -3z_3(t) + u(t)$$
Expressing the total system output $Y(s) = 2 Z_1(s) - 4 Z_2(s) + 2 Z_3(s)$ in the time domain yields the algebraic output equation $y(t) = 2 z_1(t) - 4 z_2(t) + 2 z_3(t)$.

Assembling these decoupled first-order differential equations into standard matrix form produces the Diagonal Canonical Realization:
$$\begin{bmatrix} \dot{z}_1 \\ \dot{z}_2 \\ \dot{z}_3 \end{bmatrix} = \begin{bmatrix} -1 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & -3 \end{bmatrix} \begin{bmatrix} z_1 \\ z_2 \\ z_3 \end{bmatrix} + \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} u(t)$$
$$y(t) = \begin{bmatrix} 2 & -4 & 2 \end{bmatrix} \begin{bmatrix} z_1 \\ z_2 \\ z_3 \end{bmatrix}$$
The beauty of the diagonal canonical form is immediately evident: the system matrix is purely diagonal, containing the system eigenvalues directly along its main diagonal. This decouples the multi-variable differential equation system into independent scalar first-order systems that can be integrated analytically without matrix inversions. Furthermore, the input matrix $\bar{B}$ and output matrix $\bar{C}$ directly exhibit Gilbert's criterion: because no row of $\bar{B}$ is zero and no column of $\bar{C}$ is zero, all three dynamic modes are completely controllable and observable.
"""
            },
            {
                "qid": "acs-q7b",
                "marks": 7,
                "type": "Long Derivation",
                "title": "State-Space Modeling of a Field-Controlled DC Servomotor",
                "yt_query": "field controlled DC motor state space model derivation",
                "img_path": "images/acs/field_controlled_dc_motor.png",
                "img_caption": "Figure 1.7B: Electromechanical Schematic and State Flow of Field-Controlled DC Motor",
                "answer": r"""
In specialized precision instrumentation, low-power position controllers, and aerospace tracking servos, field-controlled direct-current (DC) motors are employed when the power demands of the control amplifier must be minimized. In this operational configuration, the armature circuit is supplied with a strictly constant direct current $I_a$, typically provided by a regulated DC current source. Motion control is achieved entirely by varying the field winding excitation voltage $e_f(t)$, which modulates the field current $i_f(t)$ and consequently controls the magnetic flux per pole $\phi(t)$. Because the field circuit operates at significantly lower current and power levels than the armature circuit, field control requires a much smaller and less expensive power electronic control amplifier.

The electrical subsystem of the motor is governed by applying Kirchhoff's Voltage Law across the field winding circuit. The applied control voltage $e_f(t)$ must overcome the resistive voltage drop across the field winding resistance $R_f$ and the inductive drop across the field winding self-inductance $L_f$:
$$e_f(t) = R_f i_f(t) + L_f \frac{d i_f(t)}{dt}$$
Rearranging this differential equation to isolate the time derivative of the field current yields our first first-order state equation:
$$\frac{d i_f(t)}{dt} = -\frac{R_f}{L_f} i_f(t) + \frac{1}{L_f} e_f(t)$$
Because the magnetic core operates in the linear, un-saturated region of its B-H magnetization curve, the magnetic flux per pole is directly proportional to the field current, governed by $\phi(t) = K_f i_f(t)$, where $K_f$ is a magnetic core proportionality constant.

The mechanical rotational subsystem is described by Newton's second law for angular motion. The developed electromechanical motor torque is proportional to the product of armature current and magnetic flux: $T_m(t) = K_t' \phi(t) I_a$. Because the armature current $I_a$ is held strictly constant, substituting $\phi(t) = K_f i_f(t)$ yields a linear relationship where motor torque is directly proportional to field current:
$$T_m(t) = K_t' K_f I_a i_f(t) = K_{mf} i_f(t)$$
where $K_{mf} = K_t' K_f I_a$ represents the motor torque constant in field control. This driving torque accelerates the total effective rotor and load inertia $J_m$ against the viscous friction damping coefficient $B_m$ and any external disturbance load torque $T_L(t)$:
$$J_m \frac{d \omega_m(t)}{dt} + B_m \omega_m(t) + T_L(t) = K_{mf} i_f(t)$$
Assuming for nominal tracking that the load disturbance is zero ($T_L = 0$), isolating the angular acceleration yields the second state equation:
$$\frac{d \omega_m(t)}{dt} = \frac{K_{mf}}{J_m} i_f(t) - \frac{B_m}{J_m} \omega_m(t)$$

When the control objective is angular position tracking $\theta_m(t)$, the kinematic relation linking position to angular velocity provides the third state equation:
$$\frac{d \theta_m(t)}{dt} = \omega_m(t)$$
We define the state vector as $x(t) = \begin{bmatrix} x_1 & x_2 & x_3 \end{bmatrix}^T = \begin{bmatrix} i_f(t) & \omega_m(t) & \theta_m(t) \end{bmatrix}^T$ and the control input as $u(t) = e_f(t)$. Expressing the coupled first-order differential equations in standard state-space matrix notation $\dot{x}(t) = A x(t) + B u(t)$ yields:
$$\begin{bmatrix} \dot{i}_f(t) \\ \dot{\omega}_m(t) \\ \dot{\theta}_m(t) \end{bmatrix} = \begin{bmatrix} -\frac{R_f}{L_f} & 0 & 0 \\ \frac{K_{mf}}{J_m} & -\frac{B_m}{J_m} & 0 \\ 0 & 1 & 0 \end{bmatrix} \begin{bmatrix} i_f(t) \\ \omega_m(t) \\ \theta_m(t) \end{bmatrix} + \begin{bmatrix} \frac{1}{L_f} \\ 0 \\ 0 \end{bmatrix} e_f(t)$$

Notice a profound structural difference between the armature-controlled DC motor and the field-controlled DC motor: in the field-controlled motor, the $(1, 2)$ element of matrix $A$ is identically zero because the induced rotational back-EMF $e_b(t)$ is generated in the armature circuit, not in the field circuit! Consequently, there is no back-EMF feedback loop from rotor speed into the electrical state derivative $\dot{i}_f(t)$. The electrical time constant $\tau_f = \frac{L_f}{R_f}$ is typically large due to the high inductance of the multi-turn field winding, which makes the transient dynamic response of field-controlled motors somewhat more sluggish than armature-controlled servomotors, while offering high power amplification efficiency.
"""
            }
        ]
    },
    {
        "module_id": "acs-m2",
        "module_num": "Module 2",
        "module_title": "Solution of State Equations, State Transition Matrix & Discrete Systems",
        "questions": [
            {
                "qid": "acs-q8",
                "marks": 3,
                "type": "Short Answer",
                "title": "Derivation of Solution of Autonomous State Equations using Laplace Transforms",
                "yt_query": "solution autonomous state equation laplace transform resolvent matrix",
                "img_path": "images/acs/autonomous_response_flow.png",
                "img_caption": "Figure 2.1: Resolvent Matrix and Laplace Transform Inversion Flow",
                "answer": r"""
An autonomous or unforced continuous-time linear time-invariant dynamical system is governed by the homogeneous vector differential equation $\dot{x}(t) = A x(t)$, subject to an initial state vector specification $x(0) = x_0$ at time $t = 0$. Because external control excitation is absent ($u(t) = 0$), the entire subsequent trajectory of the system is determined exclusively by the dissipation or redistribution of its internally stored initial energy. Solving this vector differential equation using the Laplace transform technique transforms the calculus of coupled derivatives into linear matrix algebra.

Taking the unilateral Laplace transform on both sides of the vector differential equation yields $\mathcal{L}\{\dot{x}(t)\} = \mathcal{L}\{A x(t)\}$. Applying the standard derivative theorem of Laplace transforms yields $s X(s) - x(0) = A X(s)$, where $X(s)$ represents the Laplace transform vector of the state trajectory $x(t)$. Collecting all terms containing $X(s)$ on the left-hand side gives $s X(s) - A X(s) = x(0)$. Factoring out the state vector yields $(sI - A)X(s) = x(0)$, where $I$ represents the $n \times n$ identity matrix. The matrix $(sI - A)$ is known as the characteristic matrix of the dynamical system.

Provided that the complex variable $s$ does not coincide with any eigenvalue of matrix $A$, the characteristic matrix is invertible. Premultiplying both sides by the inverse matrix $(sI - A)^{-1}$, designated as the resolvent matrix $\Phi(s)$, produces the algebraic frequency-domain solution $X(s) = (sI - A)^{-1} x(0)$. Taking the inverse Laplace transform on both sides yields the time-domain state trajectory $x(t) = \mathcal{L}^{-1}\{(sI - A)^{-1}\} x(0)$. By definition, the matrix inverse Laplace transform $\mathcal{L}^{-1}\{(sI - A)^{-1}\}$ is identical to the matrix exponential $e^{At}$, formally defined as the State Transition Matrix $\Phi(t)$. Thus, the unforced solution is elegantly expressed as $x(t) = \Phi(t) x(0) = e^{At} x_0$, directly mapping initial conditions into future states.
"""
            },
            {
                "qid": "acs-q9",
                "marks": 3,
                "type": "Short Answer",
                "title": "Properties of the State Transition Matrix: Statement and Proofs",
                "yt_query": "properties of state transition matrix proof control systems",
                "img_path": "images/acs/stm_properties.png",
                "img_caption": "Figure 2.2: Composition and Inversion Geometry of State Transition Matrix",
                "answer": r"""
The state transition matrix $\Phi(t) = e^{At}$ is the fundamental matrix operator that governs the transition of state trajectories in linear time-invariant systems. By definition, the matrix exponential is represented by the infinite power series expansion $e^{At} = I + A t + \frac{A^2 t^2}{2!} + \frac{A^3 t^3}{3!} + \dots = \sum_{k=0}^{\infty} \frac{A^k t^k}{k!}$, which converges uniformly for all finite matrices $A$ and time intervals $t$. This matrix operator exhibits several profound mathematical properties that reflect the physical reversibility and temporal invariance of linear dynamic systems.

The first fundamental property is the Identity Property at time origin, stated as $\Phi(0) = I$. To prove this, we evaluate the power series definition of the state transition matrix at $t = 0$. Substituting $t = 0$ yields $\Phi(0) = e^{A \cdot 0} = I + A(0) + \frac{A^2(0)^2}{2!} + \dots = I$. From a physical perspective, this proves that over zero elapsed time, no state transition occurs, and the state vector remains identically equal to its initial value, meaning $x(0) = \Phi(0)x(0) = I x(0) = x(0)$.

The second fundamental property is the Group Composition or Semi-Group Property, stated as $\Phi(t_1 + t_2) = \Phi(t_1)\Phi(t_2) = \Phi(t_2)\Phi(t_1)$. To prove this, consider a trajectory starting from $x(0)$ and evolving to time $t_1$, giving $x(t_1) = \Phi(t_1)x(0)$. If the trajectory continues for an additional time duration $t_2$, the state at $t_1 + t_2$ is obtained by treating $x(t_1)$ as the initial state, yielding $x(t_1 + t_2) = \Phi(t_2)x(t_1) = \Phi(t_2)\Phi(t_1)x(0)$. Alternatively, computing the transition directly from $t = 0$ over the combined interval $t_1 + t_2$ yields $x(t_1 + t_2) = \Phi(t_1 + t_2)x(0)$. Because this relation holds for arbitrary initial conditions $x(0)$, it follows that $\Phi(t_1 + t_2) = \Phi(t_1)\Phi(t_2)$. Analytically, multiplying the exponential series $e^{A t_1} e^{A t_2} = e^{A(t_1 + t_2)}$ confirms the result because the matrices $A t_1$ and $A t_2$ commute.

The third fundamental property is the Inversion Property, stated as $\Phi(-t) = [\Phi(t)]^{-1}$. This property can be derived directly from the composition property by setting $t_1 = t$ and $t_2 = -t$. Substituting these values yields $\Phi(t - t) = \Phi(0) = \Phi(t)\Phi(-t)$. Because $\Phi(0) = I$, we obtain $\Phi(t)\Phi(-t) = I$. Premultiplying both sides by $[\Phi(t)]^{-1}$ proves that $\Phi(-t) = [\Phi(t)]^{-1}$. Physically, this property demonstrates that the state transition matrix is always non-singular, meaning that dynamic transitions in continuous LTI systems are completely reversible in time: one can always reconstruct past state vectors uniquely from current state measurements by projecting backward along $\Phi(-t)$.
"""
            },
            {
                "qid": "acs-q9b",
                "marks": 3,
                "type": "Short Answer",
                "title": "Discrete-Time State Space Analysis: Pulse Transfer Function and State Equations",
                "yt_query": "discrete time state space pulse transfer function difference equation",
                "img_path": "images/acs/discrete_state_model.png",
                "img_caption": "Figure 2.2B: Discrete Delay Elements and State Transition in Sampled Data Systems",
                "answer": r"""
In modern computer-controlled and sampled-data control systems, digital computers execute control algorithms at discrete, periodic sampling instants $t = k T$, where $T$ is the sampling interval and $k \in \{0, 1, 2, \dots\}$. A linear time-invariant discrete-time dynamical system is mathematically described by a pair of vector difference equations: the state transition difference equation $x(k+1) = A_d x(k) + B_d u(k)$, and the algebraic output equation $y(k) = C_d x(k) + D_d u(k)$. Here, $x(k) \in \mathbb{R}^n$ is the discrete state vector, $u(k) \in \mathbb{R}^m$ is the sampled control sequence, and $y(k) \in \mathbb{R}^p$ is the discrete output sequence. The fundamental memory element in discrete state systems is the unit delay operator $z^{-1}$, which replaces the continuous-time integrator $\frac{1}{s}$.

Taking the unilateral $\mathcal{Z}$-transform on both sides of the discrete state equation under zero initial conditions ($x(0) = 0$) yields $z X(z) = A_d X(z) + B_d U(z)$. Collecting state terms yields $(zI - A_d)X(z) = B_d U(z)$. Premultiplying by the matrix inverse $(zI - A_d)^{-1}$ yields the frequency-domain discrete state vector $X(z) = (zI - A_d)^{-1} B_d U(z)$. Substituting this into the $\mathcal{Z}$-transform of the output equation $Y(z) = C_d X(z) + D_d U(z)$ produces:
$$Y(z) = \left[ C_d (zI - A_d)^{-1} B_d + D_d \right] U(z)$$
The pulse transfer function matrix is therefore defined as $G(z) = \frac{Y(z)}{U(z)} = C_d (zI - A_d)^{-1} B_d + D_d$.

The discrete-time state transition matrix $\Phi(k)$ maps the initial state $x(0)$ to any future discrete instant $k$, governed by $x(k) = A_d^k x(0) = \Phi(k) x(0)$. In the complex $z$-plane, this matrix is computed by taking the inverse $\mathcal{Z}$-transform of the discrete resolvent matrix: $\Phi(k) = \mathcal{Z}^{-1}\{(zI - A_d)^{-1} z\}$. For system stability, all poles of the discrete pulse transfer function (the eigenvalues of matrix $A_d$) must reside strictly inside the unit circle of the complex $z$-plane ($|\lambda_i| < 1$).
"""
            },
            {
                "qid": "acs-q10",
                "marks": 7,
                "type": "Long Derivation",
                "title": "Computation of State Transition Matrix using Cayley-Hamilton Theorem for Systems with Repeated and Distinct Eigenvalues",
                "yt_query": "cayley hamilton theorem state transition matrix 2x2 3x3 step by step",
                "img_path": "images/acs/cayley_hamilton_method.png",
                "img_caption": "Figure 2.3: Mapping Characteristic Polynomial to Matrix Exponential via Cayley-Hamilton",
                "answer": r"""
The Cayley-Hamilton theorem represents one of the most powerful analytical methods for evaluating matrix functions without resorting to infinite series expansions or inverse Laplace transforms of high-order rational fractions. The theorem states that every square matrix satisfies its own characteristic equation. If the characteristic polynomial of an $n \times n$ matrix $A$ is given by $\Delta(\lambda) = \det(\lambda I - A) = \lambda^n + a_{n-1}\lambda^{n-1} + \dots + a_1\lambda + a_0 = 0$, substituting the matrix $A$ in place of the scalar variable $\lambda$ yields the matrix identity $A^n + a_{n-1}A^{n-1} + \dots + a_1 A + a_0 I = [0]$. This profound result enables any matrix power $A^m$ (where $m \ge n$), and consequently any analytic matrix function such as the exponential $e^{At}$, to be expressed as a finite polynomial in $A$ of degree at most $n-1$:
$$e^{At} = \alpha_0(t) I + \alpha_1(t) A + \alpha_2(t) A^2 + \dots + \alpha_{n-1}(t) A^{n-1}$$
The scalar time-dependent coefficients $\alpha_0(t), \alpha_1(t), \dots, \alpha_{n-1}(t)$ are determined by recognizing that the identical scalar relationship must hold for each eigenvalue $\lambda_i$ of matrix $A$: $e^{\lambda_i t} = \sum_{k=0}^{n-1} \alpha_k(t) \lambda_i^k$.

To illustrate this method in depth, consider first the university exam problem where the system matrix possesses repeated eigenvalues:
$$A = \begin{bmatrix} 2 & 0 \\ 1 & 2 \end{bmatrix}$$
The characteristic polynomial is computed as $\det(\lambda I - A) = \det\begin{bmatrix} \lambda - 2 & 0 \\ -1 & \lambda - 2 \end{bmatrix} = (\lambda - 2)^2 = \lambda^2 - 4\lambda + 4 = 0$. This yields a repeated eigenvalue of multiplicity two, $\lambda_1 = \lambda_2 = 2$. Because the matrix is of order $n = 2$, the finite polynomial representation of the state transition matrix is:
$$e^{At} = \alpha_0(t) I + \alpha_1(t) A$$
Substituting the eigenvalue $\lambda = 2$ into the scalar equation $e^{\lambda t} = \alpha_0 + \alpha_1 \lambda$ yields our first scalar equation:
$$e^{2t} = \alpha_0(t) + 2\alpha_1(t)$$

Because the eigenvalue is repeated, a second linearly independent equation is required. According to matrix analysis, when an eigenvalue $\lambda$ has multiplicity $m$, the derivatives with respect to $\lambda$ up to order $m-1$ must also satisfy the relationship: $\frac{d}{d\lambda}[e^{\lambda t}] = \frac{d}{d\lambda}[\alpha_0 + \alpha_1 \lambda]$. Evaluating the derivatives yields $t e^{\lambda t} = \alpha_1$. Substituting $\lambda = 2$ yields our second scalar equation directly:
$$\alpha_1(t) = t e^{2t}$$
Substituting $\alpha_1(t)$ back into the first equation enables us to solve for $\alpha_0(t)$:
$$\alpha_0(t) = e^{2t} - 2\alpha_1(t) = e^{2t} - 2 t e^{2t} = (1 - 2t)e^{2t}$$

Now, we substitute the determined scalar functions $\alpha_0(t)$ and $\alpha_1(t)$ back into the matrix equation $e^{At} = \alpha_0 I + \alpha_1 A$:
$$e^{At} = (1 - 2t)e^{2t} \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} + t e^{2t} \begin{bmatrix} 2 & 0 \\ 1 & 2 \end{bmatrix}$$
$$e^{At} = \begin{bmatrix} (1 - 2t)e^{2t} + 2t e^{2t} & 0 \\ t e^{2t} & (1 - 2t)e^{2t} + 2t e^{2t} \end{bmatrix} = \begin{bmatrix} e^{2t} & 0 \\ t e^{2t} & e^{2t} \end{bmatrix}$$
To verify this result, we test the boundary condition at $t = 0$: $\Phi(0) = \begin{bmatrix} e^0 & 0 \\ 0 \cdot e^0 & e^0 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = I$, confirming the mathematical correctness of the derived state transition matrix.

To demonstrate the versatility of the Cayley-Hamilton method on a third-order system, consider the second problem from the university papers:
$$A = \begin{bmatrix} 0 & 0 & -2 \\ 0 & 1 & 0 \\ 1 & 0 & 3 \end{bmatrix}$$
Evaluating the characteristic polynomial yields $\det(\lambda I - A) = \det\begin{bmatrix} \lambda & 0 & 2 \\ 0 & \lambda - 1 & 0 \\ -1 & 0 & \lambda - 3 \end{bmatrix}$. Expanding along the second row gives $(\lambda - 1)[\lambda(\lambda - 3) + 2] = (\lambda - 1)(\lambda^2 - 3\lambda + 2) = (\lambda - 1)(\lambda - 1)(\lambda - 2) = (\lambda - 1)^2(\lambda - 2) = 0$. The eigenvalues are $\lambda_1 = 1$ (multiplicity two) and $\lambda_2 = 2$ (distinct). For $n = 3$, the Cayley-Hamilton expansion is $e^{At} = \alpha_0 I + \alpha_1 A + \alpha_2 A^2$.

The scalar equations corresponding to the eigenvalues are:
1. For distinct eigenvalue $\lambda = 2$: $e^{2t} = \alpha_0 + 2\alpha_1 + 4\alpha_2$
2. For repeated eigenvalue $\lambda = 1$: $e^{t} = \alpha_0 + \alpha_1 + \alpha_2$
3. Differentiating with respect to $\lambda$ and substituting $\lambda = 1$: $t e^{t} = \alpha_1 + 2\alpha_2$
Subtracting equation (2) from equation (1) yields $e^{2t} - e^t = \alpha_1 + 3\alpha_2$. Subtracting equation (3) from this intermediate result gives $\alpha_2(t) = e^{2t} - e^t - t e^t$. Substituting $\alpha_2(t)$ back into equation (3) yields $\alpha_1(t) = t e^t - 2(e^{2t} - e^t - t e^t) = -2e^{2t} + 2e^t + 3t e^t$. Finally, substituting into equation (2) yields $\alpha_0(t) = e^t - \alpha_1 - \alpha_2 = 2e^{2t} - e^t - 2t e^t$.

Computing the matrix square:
$$A^2 = \begin{bmatrix} 0 & 0 & -2 \\ 0 & 1 & 0 \\ 1 & 0 & 3 \end{bmatrix} \begin{bmatrix} 0 & 0 & -2 \\ 0 & 1 & 0 \\ 1 & 0 & 3 \end{bmatrix} = \begin{bmatrix} -2 & 0 & -6 \\ 0 & 1 & 0 \\ 3 & 0 & 7 \end{bmatrix}$$
Substituting $\alpha_0, \alpha_1, \alpha_2, I, A, A^2$ into $e^{At} = \alpha_0 I + \alpha_1 A + \alpha_2 A^2$ yields the complete closed-form state transition matrix:
$$e^{At} = \begin{bmatrix} -e^{2t} + 2e^t - 2t e^t & 0 & -2e^{2t} + 2e^t \\ 0 & e^t & 0 \\ e^{2t} - e^t & 0 & 2e^{2t} - e^t + t e^t \end{bmatrix}$$
Evaluating at $t = 0$ yields $e^{A \cdot 0} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} = I$, validating that the Cayley-Hamilton method provides an exact, rigorous solution for arbitrary linear systems.
"""
            },
            {
                "qid": "acs-q11",
                "marks": 7,
                "type": "Long Derivation",
                "title": "Complete Solution of Non-Homogeneous State Equations and Step Response Calculation",
                "yt_query": "complete solution non homogeneous state equation convolution integral step response",
                "img_path": "images/acs/convolution_integral.png",
                "img_caption": "Figure 2.4: Superposition of Zero-Input and Zero-State Convolution Integral Responses",
                "answer": r"""
The total dynamic response of a continuous-time linear time-invariant system subjected to both non-zero initial conditions and external control excitations is governed by the complete non-homogeneous vector differential equation $\dot{x}(t) = A x(t) + B u(t)$, with initial state vector $x(0) = x_0$. Because the system is linear, the principle of superposition applies rigorously, ensuring that the total response can be partitioned into two mutually exclusive components: the Zero-Input Response (ZIR), which reflects the natural transient decay or oscillation driven entirely by initial energy storage, and the Zero-State Response (ZSR), which characterizes the forced motion driven by the control input when starting from completely relaxed initial conditions ($x(0) = 0$).

To derive the complete mathematical solution in the time domain, we employ the integrating factor technique from matrix calculus. Rearranging the state equation yields $\dot{x}(t) - A x(t) = B u(t)$. Premultiplying every term by the matrix integrating factor $e^{-At}$ produces:
$$e^{-At} \dot{x}(t) - e^{-At} A x(t) = e^{-At} B u(t)$$
Recognizing that the left-hand side is the exact derivative of the matrix product $\frac{d}{dt}[e^{-At} x(t)]$, we obtain:
$$\frac{d}{dt}\left[e^{-At} x(t)\right] = e^{-At} B u(t)$$
Integrating both sides of this matrix differential equation with respect to a dummy time variable $\tau$ from initial time $\tau = 0$ to current time $\tau = t$ yields:
$$\int_0^t \frac{d}{d\tau}\left[e^{-A\tau} x(\tau)\right] d\tau = \int_0^t e^{-A\tau} B u(\tau) d\tau$$
$$e^{-At} x(t) - e^{-A \cdot 0} x(0) = \int_0^t e^{-A\tau} B u(\tau) d\tau$$
Because $e^{0} = I$, rearranging and isolating the term $e^{-At} x(t)$ gives:
$$e^{-At} x(t) = x(0) + \int_0^t e^{-A\tau} B u(\tau) d\tau$$

Premultiplying both sides by the inverse matrix $[e^{-At}]^{-1} = e^{At}$, and moving $e^{At}$ inside the integral because the integration is with respect to $\tau$, yields the celebrated continuous-time state response formula:
$$x(t) = e^{At} x(0) + \int_0^t e^{A(t-\tau)} B u(\tau) d\tau = \Phi(t) x(0) + \int_0^t \Phi(t-\tau) B u(\tau) d\tau$$
Substituting this state vector into the algebraic measurement equation $y(t) = C x(t) + D u(t)$ yields the complete system output response:
$$y(t) = C e^{At} x(0) + C \int_0^t e^{A(t-\tau)} B u(\tau) d\tau + D u(t)$$
The first term represents the Zero-Input Response $y_{ZIR}(t)$, while the second and third terms collectively constitute the Zero-State Response $y_{ZSR}(t)$ in the form of a matrix convolution integral.

To demonstrate the full numerical execution of this formula, consider the specific problem from the university examination:
$$\dot{x}(t) = \begin{bmatrix} -1 & 0 \\ 0 & -10 \end{bmatrix} x(t) + \begin{bmatrix} 0 \\ 10 \end{bmatrix} u(t), \quad y(t) = \begin{bmatrix} 1 & 0 \end{bmatrix} x(t)$$
subjected to a unit step input $u(t) = 1$ for $t \ge 0$, with initial conditions $x(0) = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$.

Because the system matrix $A = \begin{bmatrix} -1 & 0 \\ 0 & -10 \end{bmatrix}$ is purely diagonal, the state transition matrix is obtained by exponentiating the diagonal elements:
$$\Phi(t) = e^{At} = \begin{bmatrix} e^{-t} & 0 \\ 0 & e^{-10t} \end{bmatrix}$$
The Zero-Input Response of the state vector is evaluated by multiplying $\Phi(t)$ by the initial condition vector $x(0)$:
$$x_{ZIR}(t) = \Phi(t) x(0) = \begin{bmatrix} e^{-t} & 0 \\ 0 & e^{-10t} \end{bmatrix} \begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} e^{-t} \\ 0 \end{bmatrix}$$

Next, we evaluate the Zero-State Response via the convolution integral:
$$x_{ZSR}(t) = \int_0^t \begin{bmatrix} e^{-(t-\tau)} & 0 \\ 0 & e^{-10(t-\tau)} \end{bmatrix} \begin{bmatrix} 0 \\ 10 \end{bmatrix} (1) d\tau = \int_0^t \begin{bmatrix} 0 \\ 10 e^{-10(t-\tau)} \end{bmatrix} d\tau$$
The first component integral is identically zero: $x_{1,ZSR}(t) = 0$. The second component integral evaluates to:
$$x_{2,ZSR}(t) = 10 e^{-10t} \int_0^t e^{10\tau} d\tau = 10 e^{-10t} \left[\frac{e^{10\tau}}{10}\right]_0^t = e^{-10t}(e^{10t} - 1) = 1 - e^{-10t}$$
Thus, the forced zero-state vector is $x_{ZSR}(t) = \begin{bmatrix} 0 \\ 1 - e^{-10t} \end{bmatrix}$.

Combining the natural zero-input response and the forced zero-state response yields the complete state trajectory:
$$x(t) = x_{ZIR}(t) + x_{ZSR}(t) = \begin{bmatrix} e^{-t} \\ 0 \end{bmatrix} + \begin{bmatrix} 0 \\ 1 - e^{-10t} \end{bmatrix} = \begin{bmatrix} e^{-t} \\ 1 - e^{-10t} \end{bmatrix}$$
Finally, we compute the measured output response $y(t)$:
$$y(t) = C x(t) = \begin{bmatrix} 1 & 0 \end{bmatrix} \begin{bmatrix} e^{-t} \\ 1 - e^{-10t} \end{bmatrix} = e^{-t}$$
This result illustrates an important physical insight: although the control input excites state variable $x_2(t)$, the observation matrix $C$ only monitors state variable $x_1(t)$. Because matrix $A$ is decoupled and input $u(t)$ does not enter the first state derivative equation ($B_1 = 0$), the control input has zero influence on the output $y(t)$. The output response consists entirely of the natural decay of the initial condition $x_1(0) = 1$, illustrating the practical role of controllability and observability in determining system input-output behavior.
"""
            }
        ]
    },
    {
        "module_id": "acs-m3",
        "module_num": "Module 3",
        "module_title": "Controllability, Observability & State Feedback Controller / Observer Design",
        "questions": [
            {
                "qid": "acs-q12",
                "marks": 3,
                "type": "Short Answer",
                "title": "Kalman's Duality Principle between Controllability and Observability",
                "yt_query": "kalman duality principle controllability observability proof",
                "img_path": "images/acs/kalman_duality.png",
                "img_caption": "Figure 3.1: Dual Mapping between Controllability and Observability Matrices",
                "answer": r"""
Kalman's Duality Principle establishes a profound mathematical and structural symmetry between the concept of controllability and the concept of observability in linear dynamical systems. Formulated by Rudolf Kalman, the principle asserts that a system described by the pair $(A, B)$ is completely state controllable if and only if its dual transposed system described by the pair $(A^T, C^T)$ is completely state observable. In physical terms, controllability addresses the capability of external control inputs to transfer the internal state of a system to any desired configuration, whereas observability addresses the inverse problem of reconstructing the internal state of a system from measurements of external outputs.

The mathematical proof of this duality is readily demonstrated by comparing the algebraic rank conditions of Kalman's controllability and observability test matrices. For an $n$-th order continuous-time linear system with matrices $A, B$, the state controllability matrix is constructed as $Q_c = \begin{bmatrix} B & AB & A^2B & \dots & A^{n-1}B \end{bmatrix}$. Complete controllability requires that the rank of this matrix satisfies $\text{rank}(Q_c) = n$. Now consider a dual system whose system matrix is chosen as $A^* = A^T$ and whose output observation matrix is chosen as $C^* = B^T$. The observability matrix of this dual system is defined as $Q_o^* = \begin{bmatrix} (C^*)^T & (A^*)^T(C^*)^T & \dots & ((A^*)^T)^{n-1}(C^*)^T \end{bmatrix}^T$.

Substituting $A^* = A^T$ and $C^* = B^T$ into the observability matrix expression yields $Q_o^* = \begin{bmatrix} B & AB & \dots & A^{n-1}B \end{bmatrix}^T = Q_c^T$. Because matrix transposition preserves matrix rank—meaning that the rank of any matrix is identically equal to the rank of its transpose ($\text{rank}(Q_c^T) = \text{rank}(Q_c)$)—it follows directly that $Q_c$ has full rank $n$ if and only if $Q_o^*$ has full rank $n$. Consequently, any mathematical algorithm developed for solving state feedback controller design via pole placement can be directly transposed to solve state observer design problems without developing separate mathematical machinery.
"""
            },
            {
                "qid": "acs-q13",
                "marks": 3,
                "type": "Short Answer",
                "title": "Gilbert's Method for Testing Controllability and Observability",
                "yt_query": "gilberts method controllability observability distinct repeated eigenvalues",
                "img_path": "images/acs/gilbert_method.png",
                "img_caption": "Figure 3.2: Modal Decoupling and Gilbert's Diagonal Row/Column Inspection",
                "answer": r"""
Gilbert's method provides an intuitive, computationally efficient modal approach for testing the state controllability and observability of linear continuous-time systems without calculating high-order matrix powers or determinants. The method is rooted in transforming the system state space model into its canonical diagonal form (for systems with distinct eigenvalues) or Jordan canonical form (for systems with repeated eigenvalues). By decoupling the system into independent modal subsystems, Gilbert's criterion inspects the structural coupling between the external inputs and individual modes, as well as between individual modes and the external outputs.

For a system possessing $n$ distinct eigenvalues $\lambda_1, \lambda_2, \dots, \lambda_n$, the system matrix $A$ can be diagonalized via a modal transformation matrix $M$ whose columns are the linearly independent eigenvectors of $A$. Defining the transformed state vector as $z(t) = M^{-1} x(t)$ transforms the original model into diagonal canonical form: $\dot{z}(t) = \Lambda z(t) + \bar{B} u(t)$ and $y(t) = \bar{C} z(t)$, where $\Lambda = M^{-1} A M = \text{diag}(\lambda_1, \lambda_2, \dots, \lambda_n)$, $\bar{B} = M^{-1} B$, and $\bar{C} = C M$. According to Gilbert's criterion for distinct eigenvalues, the system is completely state controllable if and only if the transformed input matrix $\bar{B}$ contains no row that is identically zero. If the $i$-th row of $\bar{B}$ contains all zeros, the control input cannot excite the $i$-th natural mode $\lambda_i$, rendering that mode uncontrollable.

Similarly, Gilbert's criterion asserts that the system is completely state observable if and only if the transformed output observation matrix $\bar{C}$ contains no column that is identically zero. If the $j$-th column of $\bar{C}$ consists entirely of zeros, the $j$-th dynamic mode $\lambda_j$ produces zero contribution to the observed output vector $y(t)$, making that mode unobservable. In the case of repeated eigenvalues where the system matrix transforms into a Jordan canonical form consisting of Jordan blocks $J_k(\lambda)$, Gilbert's generalized criterion requires inspecting only the rows of $\bar{B}$ corresponding to the last row of each Jordan block, and the columns of $\bar{C}$ corresponding to the first column of each Jordan block, providing a straightforward structural test.
"""
            },
            {
                "qid": "acs-q13b",
                "marks": 3,
                "type": "Short Answer",
                "title": "Popov-Belevitch-Hautus (PBH) Rank Tests for Controllability and Observability",
                "yt_query": "PBH rank test controllability observability Hautus test",
                "img_path": "images/acs/pbh_rank_test.png",
                "img_caption": "Figure 3.2B: Modal Partitioning in Popov-Belevitch-Hautus (PBH) Algebraic Rank Test",
                "answer": r"""
The Popov-Belevitch-Hautus (PBH) rank tests represent an elegant, algebraically direct frequency-domain method for evaluating the controllability and observability of individual dynamic modes without computing powers of the state matrix $A$ or executing coordinate diagonalization. Formulated independently by V. M. Popov, V. Belevitch, and M. L. J. Hautus, the PBH test focuses directly on the system matrix pencil evaluated at the eigenvalues of the system.

According to the PBH Controllability Test, an $n$-th order continuous LTI system pair $(A, B)$ is completely state controllable if and only if:
$$\text{rank}\begin{bmatrix} sI - A & B \end{bmatrix} = n \quad \text{for all complex numbers } s \in \mathbb{C}$$
In practical application, this rank condition only needs to be verified at the finite set of distinct eigenvalues $\lambda_i$ of matrix $A$ (since for any $s \ne \lambda_i$, the matrix $(sI - A)$ has full rank $n$ automatically). If $\text{rank}\begin{bmatrix} \lambda_i I - A & B \end{bmatrix} < n$ for any eigenvalue $\lambda_i$, the dynamic mode associated with $\lambda_i$ is uncontrollable. In terms of eigenvectors, a mode $\lambda_i$ is uncontrollable if and only if there exists a non-zero left eigenvector $v \ne 0$ satisfying $v^T A = \lambda_i v^T$ such that $v^T B = 0$.

Dually, the PBH Observability Test asserts that the system pair $(A, C)$ is completely state observable if and only if:
$$\text{rank}\begin{bmatrix} sI - A \\ C \end{bmatrix} = n \quad \text{for all complex numbers } s \in \mathbb{C}$$
Evaluating this rank at each eigenvalue $\lambda_i$, if $\text{rank}\begin{bmatrix} \lambda_i I - A \\ C \end{bmatrix} < n$, the corresponding dynamic mode is unobservable. In eigenvector terminology, a mode is unobservable if there exists a right eigenvector $w \ne 0$ such that $A w = \lambda_i w$ with $C w = 0$. The PBH test is exceptionally valuable for testing the stabilizability and detectability of high-dimensional multi-variable systems.
"""
            },
            {
                "qid": "acs-q14",
                "marks": 7,
                "type": "Long Derivation",
                "title": "State Feedback Controller Design by Pole Placement using Ackermann's Formula",
                "yt_query": "state feedback controller design pole placement ackermann formula example",
                "img_path": "images/acs/state_feedback_regulator.png",
                "img_caption": "Figure 3.3: Closed-Loop State Feedback Regulator Architecture with Gain Vector K",
                "answer": r"""
State feedback control represents the cornerstone of modern state-space synthesis, enabling control engineers to alter the dynamic response of an open-loop plant arbitrarily by placing closed-loop poles at pre-specified locations in the complex $s$-plane. In state feedback design, the control input is synthesized as a linear combination of all system state variables: $u(t) = -K x(t) + r(t)$, where $K = \begin{bmatrix} k_1 & k_2 & \dots & k_n \end{bmatrix}$ is the state feedback gain vector and $r(t)$ is an external reference setpoint. Substituting this control law into the open-loop state equation $\dot{x} = A x + B u$ yields the closed-loop autonomous system $\dot{x} = (A - B K)x$. The fundamental theorem of pole placement asserts that if and only if the system pair $(A, B)$ is completely state controllable, an arbitrary set of closed-loop eigenvalues can be realized through a unique feedback gain vector $K$.

To derive Ackermann's formula, let the desired closed-loop poles be designated as $\mu_1, \mu_2, \dots, \mu_n$. The desired closed-loop characteristic equation is expressed as:
$$\alpha_d(s) = (s - \mu_1)(s - \mu_2)\dots(s - \mu_n) = s^n + \alpha_{n-1}s^{n-1} + \dots + \alpha_1 s + \alpha_0 = 0$$
According to the Cayley-Hamilton theorem, the closed-loop system matrix $(A - B K)$ must satisfy its own characteristic equation, meaning $\alpha_d(A - B K) = [0]$. Through rigorous matrix algebraic expansion, Ackermann demonstrated that the required state feedback gain vector can be evaluated directly without solving simultaneous algebraic equations using the closed-form formula:
$$K = \begin{bmatrix} 0 & 0 & \dots & 0 & 1 \end{bmatrix} Q_c^{-1} \alpha_d(A)$$
where $Q_c = \begin{bmatrix} B & AB & A^2B & \dots & A^{n-1}B \end{bmatrix}$ is the controllability matrix and $\alpha_d(A) = A^n + \alpha_{n-1}A^{n-1} + \dots + \alpha_1 A + \alpha_0 I$ is the desired characteristic polynomial matrix evaluated at $A$.

To execute this design method on the problem presented in the university examination, consider an uncompensated plant described by the open-loop transfer function:
$$G(s) = \frac{Y(s)}{U(s)} = \frac{20(s+5)}{s(s+1)(s+4)} = \frac{20s + 100}{s^3 + 5s^2 + 4s}$$
The system specifications require designing a state feedback controller such that the closed-loop dominant poles provide a percentage overshoot of $M_p = 9.5\%$ and a settling time (2% criterion) of $t_s = 0.74\text{ seconds}$.

We begin by translating the transient response time-domain specifications into desired closed-loop pole locations. The damping ratio $\zeta$ is determined from the peak overshoot specification:
$$M_p = e^{-\frac{\zeta\pi}{\sqrt{1 - \zeta^2}}} = 0.095 \implies \frac{\zeta\pi}{\sqrt{1 - \zeta^2}} = \ln\left(\frac{1}{0.095}\right) = \ln(10.526) \approx 2.3538$$
$$\frac{\zeta^2\pi^2}{1 - \zeta^2} = 5.5407 \implies \zeta^2(\pi^2 + 5.5407) = 5.5407 \implies \zeta = \sqrt{\frac{5.5407}{9.8696 + 5.5407}} = \sqrt{0.3595} \approx 0.60$$
Next, the undamped natural frequency $\omega_n$ is obtained from the settling time formula:
$$t_s = \frac{4}{\zeta \omega_n} = 0.74 \implies \zeta \omega_n = \frac{4}{0.74} \approx 5.405 \implies \omega_n = \frac{5.405}{0.60} \approx 9.0 \text{ rad/s}$$
The pair of dominant complex-conjugate poles is therefore given by:
$$s_{1,2} = -\zeta\omega_n \pm j \omega_n\sqrt{1 - \zeta^2} = -5.4 \pm j 9(0.8) = -5.4 \pm j 7.2$$
The corresponding dominant second-order factor is:
$$(s + 5.4 - j7.2)(s + 5.4 + j7.2) = (s + 5.4)^2 + 7.2^2 = s^2 + 10.8s + 29.16 + 51.84 = s^2 + 10.8s + 81$$

Because the plant is of third order, a third pole $s_3 = -\gamma$ must be selected. To preserve the dominant second-order transient response characteristics, the third pole is chosen far to the left of the dominant poles (typically 5 times deeper into the left half-plane). Choosing $\gamma = 25$ yields the desired third-order closed-loop characteristic polynomial:
$$\alpha_d(s) = (s^2 + 10.8s + 81)(s + 25) = s^3 + 35.8s^2 + 351s + 2025$$

Next, we establish the controllable phase variable state model from the plant differential equation:
$$\frac{d^3y}{dt^3} + 5\frac{d^2y}{dt^2} + 4\frac{dy}{dt} = 20\frac{du}{dt} + 100u$$
The open-loop system matrix $A$ and input matrix $B$ in controllable canonical form are:
$$A = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & -4 & -5 \end{bmatrix}, \quad B = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$$
The open-loop characteristic polynomial is $\det(sI - A) = s^3 + 5s^2 + 4s + 0$.
The closed-loop system matrix with state feedback is:
$$A - BK = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & -4 & -5 \end{bmatrix} - \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}\begin{bmatrix} k_1 & k_2 & k_3 \end{bmatrix} = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -k_1 & -4 - k_2 & -5 - k_3 \end{bmatrix}$$
The closed-loop characteristic polynomial is directly written by inspecting the bottom row:
$$\det[sI - (A - BK)] = s^3 + (5 + k_3)s^2 + (4 + k_2)s + k_1$$

Equating the coefficients of this closed-loop polynomial to the desired polynomial $\alpha_d(s) = s^3 + 35.8s^2 + 351s + 2025$ yields three simple linear algebraic equations:
$$k_1 = 2025$$
$$4 + k_2 = 351 \implies k_2 = 351 - 4 = 347$$
$$5 + k_3 = 35.8 \implies k_3 = 35.8 - 5 = 30.8$$
The required state feedback gain vector is:
$$K = \begin{bmatrix} 2025 & 347 & 30.8 \end{bmatrix}$$
Applying this feedback gain vector shifts all three closed-loop poles to the exact target locations, guaranteeing that the closed-loop system satisfies the overshoot and settling time specifications.
"""
            },
            {
                "qid": "acs-q15",
                "marks": 7,
                "type": "Long Derivation",
                "title": "Full-Order State Observer Design and Error Dynamics Derivation",
                "yt_query": "full order observer design luenberger error dynamics example",
                "img_path": "images/acs/state_observer_block_diagram.png",
                "img_caption": "Figure 3.4: Complete Architecture of Plant Coupled with Full-Order Luenberger State Observer",
                "answer": r"""
In the practical implementation of state feedback control systems, measuring every component of the state vector directly using physical sensors is often technically impossible, prohibitively expensive, or corrupted by severe measurement noise. To overcome this fundamental practical limitation, David Luenberger introduced the concept of a state observer (or state estimator). A full-order state observer is a deterministic dynamic algorithm running in real-time software that reconstructs an asymptotic estimate $\hat{x}(t)$ of the internal, unmeasurable state vector $x(t)$, utilizing only the known control input history $u(t)$ and the measured output history $y(t)$.

The mathematical formulation of a full-order Luenberger observer incorporates an internal mathematical copy of the plant dynamics, augmented by an innovation correction term proportional to the estimation error between the real measured output $y(t)$ and the estimated output $\hat{y}(t) = C \hat{x}(t)$:
$$\dot{\hat{x}}(t) = A \hat{x}(t) + B u(t) + L [y(t) - C \hat{x}(t)]$$
Here, $L$ is an $n \times p$ observer gain matrix that must be designed. To establish the convergence properties of the observer, we define the state estimation error vector as $e(t) = x(t) - \hat{x}(t)$. Differentiating this error vector with respect to time yields:
$$\dot{e}(t) = \dot{x}(t) - \dot{\hat{x}}(t) = [A x(t) + B u(t)] - [A \hat{x}(t) + B u(t) + L(C x(t) - C \hat{x}(t))]$$
Notice that the external control input $B u(t)$ cancels out completely. Collecting common terms yields the governing observer error differential equation:
$$\dot{e}(t) = (A - LC) e(t)$$
This is an autonomous linear system whose solution is $e(t) = e^{(A - LC)t} e(0)$. To guarantee that the estimation error decays asymptotically to zero regardless of initial estimation errors ($\lim_{t \to \infty} e(t) = 0$), the matrix $(A - LC)$ must be strictly Hurwitz, meaning that all its eigenvalues must reside strictly in the open left half of the complex $s$-plane. If the pair $(A, C)$ is completely observable, these observer poles can be placed arbitrarily fast.

To demonstrate the full analytical execution of observer design, consider the problem from the university examination:
$$A = \begin{bmatrix} 0 & 1 \\ -6 & -5 \end{bmatrix}, \quad B = \begin{bmatrix} 0 \\ 10 \end{bmatrix}, \quad C = \begin{bmatrix} 1 & 0 \end{bmatrix}$$
The design specification requires synthesizing a full-order observer such that the observer poles are placed at the complex conjugate locations $s_{1,2} = -1 \pm j$.

First, we verify the observability of the plant by constructing Kalman's observability matrix:
$$Q_o = \begin{bmatrix} C \\ CA \end{bmatrix} = \begin{bmatrix} \begin{bmatrix} 1 & 0 \end{bmatrix} \\ \begin{bmatrix} 1 & 0 \end{bmatrix}\begin{bmatrix} 0 & 1 \\ -6 & -5 \end{bmatrix} \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$$
The determinant of $Q_o$ is $\det(Q_o) = (1)(1) - (0)(0) = 1 \ne 0$, confirming that $\text{rank}(Q_o) = 2 = n$. Hence, the system is completely observable, guaranteeing that the observer poles can be placed arbitrarily.

Second, we determine the desired observer characteristic polynomial $\alpha_e(s)$ from the specified pole locations $s = -1 \pm j$:
$$\alpha_e(s) = [s - (-1 + j)][s - (-1 - j)] = [(s + 1) - j][(s + 1) + j] = (s + 1)^2 - j^2 = s^2 + 2s + 1 + 1 = s^2 + 2s + 2$$

Third, let the observer gain matrix be denoted as $L = \begin{bmatrix} l_1 \\ l_2 \end{bmatrix}$. We evaluate the observer system matrix $(A - LC)$:
$$A - LC = \begin{bmatrix} 0 & 1 \\ -6 & -5 \end{bmatrix} - \begin{bmatrix} l_1 \\ l_2 \end{bmatrix}\begin{bmatrix} 1 & 0 \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ -6 & -5 \end{bmatrix} - \begin{bmatrix} l_1 & 0 \\ l_2 & 0 \end{bmatrix} = \begin{bmatrix} -l_1 & 1 \\ -6 - l_2 & -5 \end{bmatrix}$$
We compute the characteristic polynomial of $(A - LC)$:
$$\det[sI - (A - LC)] = \det\begin{bmatrix} s + l_1 & -1 \\ 6 + l_2 & s + 5 \end{bmatrix} = (s + l_1)(s + 5) - (-1)(6 + l_2) = s^2 + (5 + l_1)s + 5l_1 + 6 + l_2$$

Equating the coefficients of this characteristic polynomial to the desired polynomial $\alpha_e(s) = s^2 + 2s + 2$ yields two linear algebraic equations:
$$5 + l_1 = 2 \implies l_1 = 2 - 5 = -3$$
$$5l_1 + 6 + l_2 = 2 \implies 5(-3) + 6 + l_2 = 2 \implies -15 + 6 + l_2 = 2 \implies -9 + l_2 = 2 \implies l_2 = 11$$
Therefore, the unique observer gain vector is:
$$L = \begin{bmatrix} -3 \\ 11 \end{bmatrix}$$

Substituting this gain vector into the observer architecture yields the complete real-time estimator equations:
$$\begin{bmatrix} \dot{\hat{x}}_1 \\ \dot{\hat{x}}_2 \end{bmatrix} = \begin{bmatrix} 3 & 1 \\ -17 & -5 \end{bmatrix} \begin{bmatrix} \hat{x}_1 \\ \hat{x}_2 \end{bmatrix} + \begin{bmatrix} 0 \\ 10 \end{bmatrix} u(t) + \begin{bmatrix} -3 \\ 11 \end{bmatrix} y(t)$$
According to the celebrated Separation Principle, when this observer is combined with a state feedback regulator ($u = -K \hat{x}$), the eigenvalues of the closed-loop system consist of the union of the controller eigenvalues and the observer eigenvalues, proving that the controller and observer can be designed independently.
"""
            }
        ]
    },
    {
        "module_id": "acs-m4",
        "module_num": "Module 4",
        "module_title": "Non-Linear Systems & Describing Function Analysis",
        "questions": [
            {
                "qid": "acs-q16",
                "marks": 3,
                "type": "Short Answer",
                "title": "Characteristics of Non-Linear Systems: Distinct Physical Phenomena",
                "yt_query": "characteristics of non linear systems jump resonance limit cycles",
                "img_path": "images/acs/nonlinear_phenomena.png",
                "img_caption": "Figure 4.1: Distinctive Non-Linear Dynamic Phenomena (Jump Resonance & Hysteresis)",
                "answer": r"""
Non-linear dynamical systems exhibit a rich tapestry of complex behaviors that have no counterpart in linear system theory. The foundational cornerstone of linear systems—the principle of superposition, which asserts that the response to a combination of inputs is simply the sum of individual responses—fails completely in non-linear systems. Consequently, the stability, transient response, and frequency response of non-linear systems depend intimately on the amplitude and waveform of the excitation signal, rather than being exclusive properties of the system parameters. A non-linear system may be well-damped and asymptotically stable for small disturbance amplitudes, yet become wildly unstable when perturbed beyond a critical threshold.

One prominent phenomenon exclusive to non-linear systems is jump resonance, frequently observed in feedback systems containing saturation or non-linear springs (Duffing oscillators). When subjected to a sinusoidal input of fixed amplitude and slowly varying frequency, the output amplitude follows a continuous curve until a critical frequency is reached. At this critical frequency, the system response experiences a sudden, discontinuous vertical jump in amplitude and phase angle. When the frequency is swept in the reverse direction, the jump occurs at a different frequency, producing a pronounced hysteresis loop. This multi-valued amplitude response signifies that multiple stable operating states co-exist for the identical excitation frequency.

Another fundamental non-linear phenomenon is the autonomous generation of limit cycles, which are self-sustained periodic oscillations that arise in unforced systems without any external sinusoidal excitation. Unlike the marginally stable sinusoidal oscillations of undamped linear systems (which depend entirely on initial energy and can take any arbitrary amplitude), limit cycles possess fixed, robust amplitudes and frequencies determined solely by the balance between energy generation and dissipation within the non-linear element. Furthermore, non-linear systems can generate subharmonic oscillations (frequencies at rational fractions of input frequency), frequency entrainment (locking to external signals), and deterministic chaos, none of which can occur in linear dynamics.
"""
            },
            {
                "qid": "acs-q16b",
                "marks": 3,
                "type": "Short Answer",
                "title": "Describing Function of Ideal Relay and Relay with Dead-Zone",
                "yt_query": "describing function ideal relay relay with dead zone derivation",
                "img_path": "images/acs/relay_describing_function.png",
                "img_caption": "Figure 4.1B: Ideal Relay and Dead-Zone Relay Switching Characteristics and Output Square Waves",
                "answer": r"""
The describing function of an ideal relay (on-off switching element) represents one of the most fundamental non-linear analytical models in control theory, frequently found in bang-bang thermal governors, position servomechanisms, and switched-mode power converters. An ideal relay produces an output $y(t) = +M$ whenever the input $x(t) > 0$, and $y(t) = -M$ whenever $x(t) < 0$, where $M$ represents the maximum output drive magnitude. When subjected to a sinusoidal input $x(t) = X \sin(\omega t)$, the output is an odd-symmetric, zero-mean square wave alternating between $+M$ and $-M$ with the identical fundamental frequency $\omega$.

Because the output waveform exhibits quarter-wave odd symmetry, only the fundamental sine Fourier coefficient $B_1$ is non-zero, evaluated as:
$$B_1 = \frac{4}{\pi} \int_0^{\pi/2} M \sin(\theta) d\theta = \frac{4M}{\pi} [-\cos(\theta)]_0^{\pi/2} = \frac{4M}{\pi}[0 - (-1)] = \frac{4M}{\pi}$$
Dividing this fundamental output amplitude by the input sinusoid amplitude $X$ yields the celebrated describing function of an ideal relay:
$$N(X) = \frac{B_1}{X} = \frac{4M}{\pi X}$$
This equation shows that the effective gain of an ideal relay is purely real and decreases inversely with input amplitude $X$. For tiny inputs ($X \to 0$), the gain approaches infinity, which reflects the steep infinite slope across zero; as amplitude grows, the effective gain rolls off toward zero.

When the relay incorporates a dead-band (dead-zone) of width $D$, the relay produces zero output ($y = 0$) whenever $|x(t)| \le D$. When the input exceeds the dead-zone ($X > D$), switching occurs at the threshold angle $\theta_1 = \sin^{-1}(D/X)$. The output is a truncated square wave active only for $\theta_1 \le \theta \le \pi - \theta_1$. Evaluating the Fourier integral yields:
$$B_1 = \frac{4}{\pi} \int_{\theta_1}^{\pi/2} M \sin(\theta) d\theta = \frac{4M}{\pi} \cos(\theta_1) = \frac{4M}{\pi} \sqrt{1 - \left(\frac{D}{X}\right)^2}$$
The describing function for a relay with dead-zone is therefore $N(X) = \frac{4M}{\pi X}\sqrt{1 - (D/X)^2}$ for $X > D$, and $N(X) = 0$ for $X \le D$. The dead-zone introduces a threshold below which the relay is completely inactive, eliminating high-frequency chatter around zero at the cost of steady-state error.
"""
            },
            {
                "qid": "acs-q17",
                "marks": 7,
                "type": "Long Derivation",
                "title": "Derivation of the Describing Function for Symmetrical Saturation Non-Linearity",
                "yt_query": "describing function derivation saturation nonlinearity step by step",
                "img_path": "images/acs/saturation_describing_function.png",
                "img_caption": "Figure 4.2: Symmetrical Saturation Characteristic and Truncated Output Waveform",
                "answer": r"""
The describing function method is an approximate frequency-domain technique developed to analyze self-sustained oscillations and limit cycles in feedback systems containing a single, isolated, memoryless or memory-dependent non-linear element cascaded with a linear plant. The theoretical validity of the method rests upon the Low-Pass Filtering Hypothesis: because the linear plant $G(s)$ in physical engineering systems acts as a strong low-pass filter (having significantly higher attenuation at higher harmonic frequencies), when the non-linear element is driven by a sinusoidal input $x(t) = X \sin(\omega t)$, the higher harmonic components generated by the non-linearity are heavily attenuated as they circulate around the feedback loop. Therefore, only the fundamental harmonic component of the non-linear output is fed back, allowing the non-linear element to be replaced by an equivalent complex gain $N(X, \omega)$.

For an odd-symmetric, memoryless non-linearity, the output waveform $y(t)$ contains no DC component and no even harmonics, and the fundamental harmonic is purely in-phase with the input. The output is expressed by its Fourier series as $y(t) = Y_1 \sin(\omega t) = (A_1 \cos(\omega t) + B_1 \sin(\omega t))$, where $A_1 = 0$ due to odd symmetry. The describing function is formally defined as the ratio of the fundamental output phasor to the input sinusoidal phasor:
$$N(X) = \frac{Y_1 \angle 0^\circ}{X \angle 0^\circ} = \frac{B_1}{X}$$
where the Fourier coefficient $B_1$ is evaluated by integrating over a full cycle:
$$B_1 = \frac{1}{\pi} \int_0^{2\pi} y(t) \sin(\omega t) d(\omega t) = \frac{4}{\pi} \int_0^{\pi/2} y(t) \sin(\theta) d\theta$$
where $\theta = \omega t$, exploiting quarter-wave symmetry.

Consider a symmetrical saturation non-linearity having a linear slope $k$ in the linear range, and a saturation threshold level $S$. The piecewise mathematical relationship between input $x$ and output $y$ is:
$$y = \begin{cases} k x & \text{for } |x| \le S \\ k S \text{ sgn}(x) & \text{for } |x| > S \end{cases}$$
When the input sinusoid $x(t) = X \sin(\theta)$ is applied, two operational regimes must be analyzed based on the input amplitude $X$.

Case 1: When the input amplitude is less than or equal to the saturation limit ($X \le S$), the input never exceeds the linear threshold. The non-linear element operates entirely within its linear zone for all $\theta$, yielding $y(t) = k X \sin(\theta)$. Evaluating the Fourier integral yields:
$$B_1 = \frac{4}{\pi} \int_0^{\pi/2} k X \sin^2(\theta) d\theta = \frac{4 k X}{\pi} \left[\frac{\theta}{2} - \frac{\sin(2\theta)}{4}\right]_0^{\pi/2} = \frac{4 k X}{\pi}\left(\frac{\pi}{4}\right) = k X$$
The describing function is therefore:
$$N(X) = \frac{B_1}{X} = \frac{k X}{X} = k \quad \text{for } X \le S$$
This confirms that for small input amplitudes, the describing function is a constant scalar equal to the linear slope $k$.

Case 2: When the input amplitude exceeds the saturation threshold ($X > S$), the output waveform clips at the saturation level $k S$. Let $\theta_1$ represent the saturation transition angle at which the input sinusoid reaches the threshold:
$$X \sin(\theta_1) = S \implies \theta_1 = \sin^{-1}\left(\frac{S}{X}\right)$$
Over the quarter-cycle from $\theta = 0$ to $\theta = \pi/2$, the output waveform is defined in two intervals:
$$y(\theta) = \begin{cases} k X \sin(\theta) & \text{for } 0 \le \theta \le \theta_1 \\ k S & \text{for } \theta_1 < \theta \le \pi/2 \end{cases}$$
We evaluate the Fourier integral by partitioning it into these two regions:
$$B_1 = \frac{4}{\pi} \left[ \int_0^{\theta_1} k X \sin^2(\theta) d\theta + \int_{\theta_1}^{\pi/2} k S \sin(\theta) d\theta \right]$$
Evaluating the first integral using the trigonometric identity $\sin^2(\theta) = \frac{1 - \cos(2\theta)}{2}$:
$$\int_0^{\theta_1} k X \sin^2(\theta) d\theta = k X \left[\frac{\theta}{2} - \frac{\sin(2\theta)}{4}\right]_0^{\theta_1} = k X \left[\frac{\theta_1}{2} - \frac{2\sin(\theta_1)\cos(\theta_1)}{4}\right] = \frac{k X \theta_1}{2} - \frac{k X}{2} \sin(\theta_1)\cos(\theta_1)$$
Evaluating the second integral:
$$\int_{\theta_1}^{\pi/2} k S \sin(\theta) d\theta = k S [-\cos(\theta)]_{\theta_1}^{\pi/2} = k S [-\cos(\pi/2) + \cos(\theta_1)] = k S \cos(\theta_1)$$
Substituting the threshold relation $k S = k X \sin(\theta_1)$ into the second integral yields:
$$\int_{\theta_1}^{\pi/2} k S \sin(\theta) d\theta = k X \sin(\theta_1)\cos(\theta_1)$$
Combining both integrals gives:
$$B_1 = \frac{4}{\pi} \left[ \frac{k X \theta_1}{2} - \frac{k X}{2} \sin(\theta_1)\cos(\theta_1) + k X \sin(\theta_1)\cos(\theta_1) \right] = \frac{4}{\pi} \left[ \frac{k X \theta_1}{2} + \frac{k X}{2} \sin(\theta_1)\cos(\theta_1) \right]$$
$$B_1 = \frac{2 k X}{\pi} \left[ \theta_1 + \sin(\theta_1)\cos(\theta_1) \right]$$

Using the trigonometric identity $\cos(\theta_1) = \sqrt{1 - \sin^2(\theta_1)} = \sqrt{1 - (S/X)^2}$, and substituting $\theta_1 = \sin^{-1}(S/X)$ and $\sin(\theta_1) = S/X$:
$$B_1 = \frac{2 k X}{\pi} \left[ \sin^{-1}\left(\frac{S}{X}\right) + \frac{S}{X}\sqrt{1 - \left(\frac{S}{X}\right)^2} \right]$$
Dividing by the input amplitude $X$ yields the final closed-form expression for the describing function of symmetrical saturation:
$$N(X) = \frac{2 k}{\pi} \left[ \sin^{-1}\left(\frac{S}{X}\right) + \frac{S}{X}\sqrt{1 - \left(\frac{S}{X}\right)^2} \right] \quad \text{for } X > S$$
This equation reveals that as the input amplitude $X$ increases far beyond the saturation limit ($X \to \infty$), the argument $S/X \to 0$, causing $\sin^{-1}(0) = 0$ and $N(X) \to 0$. Physically, saturation acts as an amplitude-dependent gain that decreases monotonically from $k$ toward zero as the signal amplitude grows, providing the natural stabilizing mechanism that quenches unstable oscillations into stable limit cycles.
"""
            },
            {
                "qid": "acs-q17b",
                "marks": 7,
                "type": "Long Derivation",
                "title": "Derivation of the Describing Function for Dead-Zone Non-Linearity",
                "yt_query": "describing function dead zone non linearity derivation step by step",
                "img_path": "images/acs/dead_zone_describing_function.png",
                "img_caption": "Figure 4.2B: Symmetrical Dead-Zone Non-Linearity Characteristic and Output Waveform",
                "answer": r"""
Dead-zone non-linearity (also known as dead-band or threshold non-linearity) is an inherent physical phenomenon commonly encountered in servomotors, hydraulic control valves, mechanical gear trains with backlash, and electronic operational amplifier input stages. In a system possessing dead-zone, the actuator produces absolutely zero output until the input magnitude exceeds a critical threshold $D$. Once the input magnitude exceeds $D$, the output responds linearly with slope $k$. The piecewise mathematical definition of symmetrical dead-zone is expressed as:
$$y = \begin{cases} 0 & \text{for } |x| \le D \\ k(x - D) & \text{for } x > D \\ k(x + D) & \text{for } x < -D \end{cases}$$
When excited by a sinusoidal input $x(t) = X \sin(\omega t) = X \sin(\theta)$, where $\theta = \omega t$, we evaluate the fundamental Fourier component of the resulting output waveform $y(\theta)$.

Because the non-linearity is memoryless and odd-symmetric, the fundamental cosine coefficient $A_1 = 0$, and the output possesses quarter-wave symmetry. The describing function is given by $N(X) = \frac{B_1}{X}$, where the Fourier sine coefficient is evaluated over the quarter-cycle:
$$B_1 = \frac{4}{\pi} \int_0^{\pi/2} y(\theta) \sin(\theta) d\theta$$

Case 1: When the input amplitude is less than or equal to the dead-band width ($X \le D$), the input signal never crosses the dead-zone threshold. The output remains identically zero for all $\theta \in [0, 2\pi]$ ($y(\theta) = 0$). Consequently, the Fourier coefficient $B_1 = 0$, and the describing function is:
$$N(X) = 0 \quad \text{for } X \le D$$
This confirms that for small signals, the dead-zone completely blocks transmission, rendering the feedback loop effectively open.

Case 2: When the input amplitude exceeds the dead-band width ($X > D$), the signal breaks through the threshold. Let $\theta_1$ denote the angle at which the input reaches $D$:
$$X \sin(\theta_1) = D \implies \theta_1 = \sin^{-1}\left(\frac{D}{X}\right)$$
During the quarter-cycle from $\theta = 0$ to $\theta = \pi/2$, the output is zero for $0 \le \theta \le \theta_1$, and is active for $\theta_1 < \theta \le \pi/2$ as $y(\theta) = k(X \sin(\theta) - D)$. We partition the Fourier integral into these intervals:
$$B_1 = \frac{4}{\pi} \int_{\theta_1}^{\pi/2} k(X \sin(\theta) - D) \sin(\theta) d\theta = \frac{4k}{\pi} \left[ X \int_{\theta_1}^{\pi/2} \sin^2(\theta) d\theta - D \int_{\theta_1}^{\pi/2} \sin(\theta) d\theta \right]$$

Evaluating the first trigonometric integral:
$$\int_{\theta_1}^{\pi/2} \sin^2(\theta) d\theta = \left[\frac{\theta}{2} - \frac{\sin(2\theta)}{4}\right]_{\theta_1}^{\pi/2} = \left(\frac{\pi}{4} - 0\right) - \left(\frac{\theta_1}{2} - \frac{\sin(\theta_1)\cos(\theta_1)}{2}\right) = \frac{\pi}{4} - \frac{\theta_1}{2} + \frac{1}{2}\sin(\theta_1)\cos(\theta_1)$$
Evaluating the second integral:
$$\int_{\theta_1}^{\pi/2} \sin(\theta) d\theta = [-\cos(\theta)]_{\theta_1}^{\pi/2} = 0 - (-\cos(\theta_1)) = \cos(\theta_1)$$
Substituting both evaluations into the expression for $B_1$:
$$B_1 = \frac{4k}{\pi} \left[ X\left(\frac{\pi}{4} - \frac{\theta_1}{2} + \frac{1}{2}\sin(\theta_1)\cos(\theta_1)\right) - D \cos(\theta_1) \right]$$
Using the threshold relation $D = X \sin(\theta_1)$, the second term becomes $D \cos(\theta_1) = X \sin(\theta_1)\cos(\theta_1)$. Substituting this back gives:
$$B_1 = \frac{4k}{\pi} \left[ \frac{\pi X}{4} - \frac{X \theta_1}{2} + \frac{X}{2}\sin(\theta_1)\cos(\theta_1) - X \sin(\theta_1)\cos(\theta_1) \right]$$
$$B_1 = \frac{4k X}{\pi} \left[ \frac{\pi}{4} - \frac{\theta_1}{2} - \frac{1}{2}\sin(\theta_1)\cos(\theta_1) \right] = k X \left[ 1 - \frac{2\theta_1}{\pi} - \frac{2}{\pi}\sin(\theta_1)\cos(\theta_1) \right]$$

Substituting $\theta_1 = \sin^{-1}(D/X)$, $\sin(\theta_1) = D/X$, and $\cos(\theta_1) = \sqrt{1 - (D/X)^2}$, and dividing by input amplitude $X$ yields the final closed-form describing function for dead-zone non-linearity:
$$N(X) = k \left[ 1 - \frac{2}{\pi}\sin^{-1}\left(\frac{D}{X}\right) - \frac{2 D}{\pi X}\sqrt{1 - \left(\frac{D}{X}\right)^2} \right] \quad \text{for } X > D$$
This analytical result reveals that as input amplitude $X$ grows very large compared to the dead-band ($X \gg D$), the term $D/X \to 0$, causing $\sin^{-1}(0) = 0$ and $N(X) \to k$, returning the system to its full linear slope. Conversely, as $X$ decreases toward $D$, $N(X) \to 0$. Dead-zone introduces severe steady-state tracking dead-bands and can interact with integrating plants to induce sustained limit cycles.
"""
            },
            {
                "qid": "acs-q18",
                "marks": 7,
                "type": "Long Derivation",
                "title": "Limit Cycle Determination and Stability Analysis for Saturating Feedback Systems",
                "yt_query": "limit cycle stability analysis describing function nyquist plot example",
                "img_path": "images/acs/limit_cycle_nyquist.png",
                "img_caption": "Figure 4.3: Intersection of Linear Nyquist Locus G(jω) and Non-Linear Locus -1/N(X)",
                "answer": r"""
In non-linear control engineering, the determination of limit cycles and the assessment of their orbital stability is accomplished by extending the classical Nyquist stability criterion through describing function analysis. Consider a closed-loop negative feedback system consisting of a non-linear element described by describing function $N(X)$ in cascade with a linear transfer function $G(s)$. The closed-loop characteristic equation is given by $1 + N(X) G(s) = 0$, which can be rearranged into the harmonic balance condition:
$$G(j\omega) = -\frac{1}{N(X)}$$
This equation signifies that a periodic limit cycle can exist if and only if the frequency response locus of the linear plant $G(j\omega)$ in the complex plane intersects the negative inverse describing function locus $-\frac{1}{N(X)}$. The point of intersection directly yields both the oscillation frequency $\omega$ (from the frequency calibration along $G(j\omega)$) and the limit cycle amplitude $X$ (from the amplitude calibration along $-\frac{1}{N(X)}$).

To determine whether an identified limit cycle is orbitally stable or unstable, Loeb's Criterion is applied. If a small perturbation increases the amplitude $X$, the operating point moves along the $-\frac{1}{N(X)}$ locus. If this new point is not encircled by the $G(j\omega)$ curve, the linear system becomes stable, causing the oscillation amplitude to decay back toward the intersection point. Conversely, if an amplitude reduction moves the point into an encircled region, the system becomes unstable, causing the oscillation amplitude to grow back toward the equilibrium. In graphical terms, a limit cycle is orbitally stable if the direction of increasing $X$ on the $-\frac{1}{N(X)}$ curve crosses the $G(j\omega)$ curve from the right-hand side to the left-hand side when looking in the direction of increasing frequency $\omega$.

To demonstrate the full mathematical execution of this technique, consider the problem from the university examination: A unity feedback system contains a saturating amplifier with linear gain $K$ and saturation threshold $S = 1$, driving a linear plant described by:
$$G(s) = \frac{1}{s(1 + 0.5s)(1 + 4s)}$$
We must determine the maximum value of gain $K$ for which the closed-loop system remains stable, and compute the frequency and amplitude of the sustained limit cycle when the gain is set to $K = 2.5$.

First, we analyze the linear stability limit where the amplifier operates entirely in its linear range ($X \le S = 1$), where $N(X) = K$. The open-loop transfer function is:
$$G_{ol}(s) = \frac{K}{s(1 + 0.5s)(1 + 4s)} = \frac{K}{s(2s^2 + 4.5s + 1)} = \frac{K}{2s^3 + 4.5s^2 + s}$$
The closed-loop characteristic equation is:
$$2s^3 + 4.5s^2 + s + K = 0$$
We construct the Routh-Hurwitz stability array:
$$\begin{array}{c|cc}
s^3 & 2 & 1 \\
s^2 & 4.5 & K \\
s^1 & \frac{4.5(1) - 2K}{4.5} = \frac{4.5 - 2K}{4.5} & 0 \\
s^0 & K & 0
\end{array}$$
For system stability, all elements in the first column must be strictly positive. From the $s^1$ row:
$$4.5 - 2K > 0 \implies 2K < 4.5 \implies K < 2.25$$
Hence, the maximum linear gain for which the system remains asymptotically stable is $K_{max} = 2.25$.

Second, when the gain is increased beyond this critical stability threshold to $K = 2.5$, the linear system becomes unstable at small amplitudes ($X \le 1$). As perturbations grow, the signal enters the saturation regime ($X > 1$), where the effective describing function gain $N(X)$ decreases below $K$. A stable limit cycle is established when the effective gain is reduced precisely to the marginal stability value:
$$N(X) = K_{critical} = 2.25$$
The frequency of this sustained oscillation is determined from the auxiliary equation formed by the $s^2$ row of the Routh array at marginal stability:
$$4.5 s^2 + K_{critical} = 0 \implies 4.5(-\omega^2) + 2.25 = 0 \implies \omega^2 = \frac{2.25}{4.5} = 0.5$$
$$\omega = \sqrt{0.5} \approx 0.7071 \text{ rad/s}$$

Third, we determine the amplitude $X$ of the limit cycle. The describing function of the amplifier with gain $K = 2.5$ and saturation threshold $S = 1$ is:
$$N(X) = \frac{2(2.5)}{\pi} \left[ \sin^{-1}\left(\frac{1}{X}\right) + \frac{1}{X}\sqrt{1 - \left(\frac{1}{X}\right)^2} \right] = 2.25$$
Dividing both sides by $\frac{5}{\pi} \approx 1.5915$:
$$\sin^{-1}\left(\frac{1}{X}\right) + \frac{1}{X}\sqrt{1 - \frac{1}{X^2}} = \frac{2.25 \pi}{5} = 0.45 \pi \approx 1.4137$$
Let $\theta_1 = \sin^{-1}(1/X)$, which gives $\sin(\theta_1) = 1/X$ and $\cos(\theta_1) = \sqrt{1 - 1/X^2}$. The equation becomes:
$$\theta_1 + \sin(\theta_1)\cos(\theta_1) = \theta_1 + \frac{1}{2}\sin(2\theta_1) = 1.4137$$
We solve this transcendental equation numerically:
- If $\theta_1 = \frac{\pi}{2} \approx 1.5708$, the value is $\pi/2 \approx 1.5708$.
- For $\theta_1 = 1.0\text{ rad}$ ($57.3^\circ$): $1.0 + \frac{1}{2}\sin(2.0) = 1.0 + \frac{1}{2}(0.9093) = 1.4546$.
- For $\theta_1 = 0.94\text{ rad}$ ($53.86^\circ$): $0.94 + \frac{1}{2}\sin(1.88) = 0.94 + \frac{1}{2}(0.9526) = 0.94 + 0.4763 = 1.4163 \approx 1.4137$.
Taking $\theta_1 \approx 0.936\text{ radians}$:
$$\frac{1}{X} = \sin(0.936) \approx 0.805 \implies X = \frac{1}{0.805} \approx 1.242$$
Thus, for gain $K = 2.5$, the system establishes a sustained, stable limit cycle with an angular frequency of $\omega = 0.707\text{ rad/s}$ and an amplitude of $X \approx 1.24$. Because any increase in amplitude further decreases $N(X)$ below 2.25 (moving into the stable linear region) and any decrease raises $N(X)$ above 2.25 (moving into the unstable region), Loeb's criterion confirms that this limit cycle is completely stable and self-regulating.
"""
            }
        ]
    },
    {
        "module_id": "acs-m5",
        "module_num": "Module 5",
        "module_title": "Phase Plane Analysis & Lyapunov Stability",
        "questions": [
            {
                "qid": "acs-q19",
                "marks": 3,
                "type": "Short Answer",
                "title": "Phase Plane Concepts, Phase Trajectories, and Singular Points Classification",
                "yt_query": "phase plane analysis singular points classification node focus saddle",
                "img_path": "images/acs/singular_points_types.png",
                "img_caption": "Figure 5.1: Classification of Singular Points in Phase Plane (Nodes, Foci, Centers, Saddle Points)",
                "answer": r"""
Phase plane analysis is a graphical state-space technique tailored for studying second-order continuous-time autonomous systems, whether linear or highly non-linear. The phase plane is a two-dimensional Cartesian coordinate plane whose axes correspond to the two state variables of the system, typically chosen as the system output position $x_1 = y$ along the horizontal axis and its first time derivative velocity $x_2 = \dot{y} = \dot{x}_1$ along the vertical axis. A single operational state at any given instant is represented by a coordinate point $(x_1, x_2)$, and the continuous locus traced by this state point as time advances from an initial condition is designated as a phase trajectory. The comprehensive family of all phase trajectories originating from various initial conditions forms the phase portrait, which reveals global stability, limit cycles, and transient dynamics without requiring closed-form analytical integration.

In this phase space, equilibrium states where all dynamic motion ceases are known as singular points (or critical points). Mathematically, a point $(x_{1e}, x_{2e})$ is a singular point if both state velocity components vanish simultaneously: $\dot{x}_1 = f_1(x_1, x_2) = 0$ and $\dot{x}_2 = f_2(x_1, x_2) = 0$. At singular points, the slope of the phase trajectory $\frac{dx_2}{dx_1} = \frac{f_2(x_1, x_2)}{f_1(x_1, x_2)} = \frac{0}{0}$ becomes mathematically indeterminate, indicating that multiple trajectories can converge toward or radiate away from this equilibrium.

Singular points are classified into distinct topological categories based on the eigenvalues of the linearized Jacobian matrix evaluated at the singularity. If both eigenvalues are real, distinct, and of the same sign, the singularity is a node (a stable node if both eigenvalues are negative, where trajectories enter monotonically; an unstable node if both are positive). If the eigenvalues are complex conjugates with non-zero real parts, the singularity is a focus (a stable focus if the real part is negative, yielding inward spiraling trajectories; an unstable focus if positive, spiraling outward). If the eigenvalues are purely imaginary ($\pm j\omega$), the singularity is a center or vortex point, surrounded by concentric closed elliptical trajectories indicating sustained non-decaying oscillations. Finally, if the eigenvalues are real but have opposite signs (one positive, one negative), the singularity is a saddle point, which is inherently unstable because trajectories diverge away along an unstable manifold for almost all initial conditions.
"""
            },
            {
                "qid": "acs-q20",
                "marks": 3,
                "type": "Short Answer",
                "title": "Sign Definiteness of Scalar Functions and Sylvester's Criterion",
                "yt_query": "sign definiteness sylvester criterion positive definite quadratic form",
                "img_path": "images/acs/sylvester_definiteness.png",
                "img_caption": "Figure 5.2: Geometric Energy Bowl of Positive Definite Function V(x)",
                "answer": r"""
In the stability analysis of dynamical systems using Lyapunov's direct method, the concept of sign definiteness of a scalar function $V(x)$ serves as the mathematical foundation for generalizing physical energy. A continuous scalar function $V(x) = V(x_1, x_2, \dots, x_n)$ defined in a region $\Omega$ containing the origin is said to be positive definite if it satisfies two strict conditions: $V(0) = 0$ at the origin, and $V(x) > 0$ for all non-zero state vectors $x \ne 0$ in $\Omega$. Geometrically, a positive definite scalar function resembles a multi-dimensional bowl that reaches its absolute unique minimum strictly at the origin and rises continuously in all directions. If the function is non-negative everywhere ($V(x) \ge 0$), but can equal zero at points other than the origin, it is categorized as positive semi-definite.

Conversely, a scalar function $V(x)$ is defined as negative definite if $-V(x)$ is positive definite, meaning $V(0) = 0$ and $V(x) < 0$ for all $x \ne 0$. It is classified as negative semi-definite if $V(0) = 0$ and $V(x) \le 0$ throughout the region. If $V(x)$ can assume both positive and negative values within any arbitrarily small neighborhood surrounding the origin, the function is designated as indefinite. Testing the definiteness of general non-linear functions often involves evaluating candidate energy functions. For example, considering the function $V(x) = (x_1 + x_2)^2 + x_3^2$, setting $x_1 = 1, x_2 = -1, x_3 = 0$ results in $V(1, -1, 0) = (1 - 1)^2 + 0^2 = 0$ at a non-zero point, proving that while this function is never negative, it is only positive semi-definite rather than strictly positive definite.

For quadratic forms expressed mathematically as $V(x) = x^T P x = \sum_{i=1}^n \sum_{j=1}^n p_{ij} x_i x_j$, where $P$ is a real symmetric $n \times n$ matrix ($P = P^T$), sign definiteness is evaluated definitively using Sylvester's Criterion. Sylvester's theorem states that a quadratic form $x^T P x$ is positive definite if and only if all successive principal leading minors of matrix $P$ are strictly positive:
$$\Delta_1 = p_{11} > 0, \quad \Delta_2 = \det\begin{bmatrix} p_{11} & p_{12} \\ p_{21} & p_{22} \end{bmatrix} > 0, \quad \dots, \quad \Delta_n = \det(P) > 0$$
Furthermore, a quadratic form is negative definite if and only if its leading principal minors alternate in sign, starting with a negative first minor: $\Delta_1 < 0, \Delta_2 > 0, \Delta_3 < 0$, and generally $(-1)^k \Delta_k > 0$. Sylvester's criterion provides an indispensable algebraic tool for constructing and validating Lyapunov candidate functions.
"""
            },
            {
                "qid": "acs-q20b",
                "marks": 3,
                "type": "Short Answer",
                "title": "Generation of Lyapunov Functions: Krasovskii's and Variable Gradient Methods",
                "yt_query": "krasovskii method variable gradient method lyapunov function generation",
                "img_path": "images/acs/krasovskii_variable_gradient.png",
                "img_caption": "Figure 5.2B: Gradient Vector Field Integration to Synthesize Lyapunov Function V(x)",
                "answer": r"""
While Lyapunov's Direct Method provides an unshakeable mathematical proof of stability, its chief practical difficulty in non-linear systems is that there exists no universal algorithmic formula for constructing a valid Lyapunov candidate function $V(x)$. Two prominent systematic analytical methods developed to generate Lyapunov functions for non-linear systems $\dot{x} = f(x)$ are Krasovskii's Method and the Variable Gradient Method.

Krasovskii's Method proposes a candidate function based on the system state velocity vector: $V(x) = f^T(x) P f(x)$, where $P$ is a chosen positive definite symmetric matrix (frequently chosen as identity $I$). Computing the time derivative along system trajectories yields $\dot{V}(x) = \dot{f}^T(x) P f(x) + f^T(x) P \dot{f}(x)$. Using the chain rule, $\dot{f}(x) = J(x)\dot{x} = J(x) f(x)$, where $J(x) = \frac{\partial f}{\partial x}$ is the non-linear Jacobian matrix. Substituting this gives $\dot{V}(x) = f^T(x) [J^T(x) P + P J(x)] f(x) = f^T(x) \hat{F}(x) f(x)$. Krasovskii's theorem states that if the symmetric matrix $\hat{F}(x) = J^T(x)P + PJ(x)$ is negative definite throughout a neighborhood of the origin, then the equilibrium state $x = 0$ is asymptotically stable, and $V(x) = f^T(x)Pf(x)$ serves as the valid Lyapunov function.

The Variable Gradient Method, formulated by Schultz and Gibson, approaches the problem by working backwards from the gradient vector $\nabla V(x) = \begin{bmatrix} \frac{\partial V}{\partial x_1} & \dots & \frac{\partial V}{\partial x_n} \end{bmatrix}^T$. By the chain rule of calculus, the time derivative is $\dot{V}(x) = (\nabla V)^T \dot{x} = \sum_{i=1}^n \frac{\partial V}{\partial x_i} f_i(x)$. An assumed gradient vector with variable coefficients $\frac{\partial V}{\partial x_i} = \sum_{j=1}^n \alpha_{ij} x_j$ is selected such that $\dot{V}(x)$ is forced to be strictly negative definite. Then, the curl-free integrability conditions of vector calculus ($\frac{\partial^2 V}{\partial x_i \partial x_j} = \frac{\partial^2 V}{\partial x_j \partial x_i}$) are enforced to determine the unknown coefficients $\alpha_{ij}$. Once integrability is satisfied, the scalar Lyapunov function $V(x)$ is computed via a line integral from the origin: $V(x) = \int_0^x (\nabla V)^T dx$, yielding a customized, valid Lyapunov function.
"""
            },
            {
                "qid": "acs-q21",
                "marks": 7,
                "type": "Long Derivation",
                "title": "Singular Points Analysis and Phase Portrait Construction of a Non-Linear System",
                "yt_query": "singular points phase portrait nonlinear system linearization jacobian",
                "img_path": "images/acs/singular_points_phase_portrait.png",
                "img_caption": "Figure 5.3: Phase Portrait Sketch showing Singular Points (Unstable Focus and Saddle Point)",
                "answer": r"""
The systematic investigation of non-linear differential equations in the phase plane requires identifying all equilibrium singular points, linearizing the system dynamics in the immediate neighborhood of each singularity, classifying their local stability, and constructing the global phase portrait. Consider the non-linear second-order autonomous dynamical equation presented in the university examination:
$$\ddot{y} - 0.1\dot{y} + y + y^2 = 0$$
We define the canonical phase state variables as the output displacement $x_1 = y$ and the output velocity $x_2 = \dot{y} = \dot{x}_1$. Expressing the second-order equation as a set of two coupled first-order state differential equations yields:
$$\dot{x}_1 = x_2 = f_1(x_1, x_2)$$
$$\dot{x}_2 = 0.1 x_2 - x_1 - x_1^2 = f_2(x_1, x_2)$$

To determine all singular points of the system, we set both state derivatives simultaneously to zero:
$$f_1(x_1, x_2) = x_2 = 0$$
$$f_2(x_1, x_2) = 0.1(0) - x_1 - x_1^2 = -x_1(1 + x_1) = 0$$
From the second equation, $x_1 = 0$ or $x_1 = -1$. Because $x_2 = 0$ for both solutions, the system possesses exactly two distinct physical singular points in the phase plane:
$$\text{Singular Point 1: } P_1 = (0, 0)$$
$$\text{Singular Point 2: } P_2 = (-1, 0)$$

To classify each singular point, we linearize the non-linear vector field by evaluating the Jacobian matrix $J = \begin{bmatrix} \frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} \\ \frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} \end{bmatrix}$. Computing the partial derivatives:
$$\frac{\partial f_1}{\partial x_1} = 0, \quad \frac{\partial f_1}{\partial x_2} = 1, \quad \frac{\partial f_2}{\partial x_1} = -1 - 2x_1, \quad \frac{\partial f_2}{\partial x_2} = 0.1$$
Thus, the general Jacobian matrix for this system is:
$$J(x_1, x_2) = \begin{bmatrix} 0 & 1 \\ -1 - 2x_1 & 0.1 \end{bmatrix}$$

We now evaluate the Jacobian matrix and its characteristic roots at each singular point:
Analysis of Singular Point $P_1(0, 0)$:
Substituting $(x_1, x_2) = (0, 0)$ into the Jacobian matrix yields:
$$J_1 = \begin{bmatrix} 0 & 1 \\ -1 & 0.1 \end{bmatrix}$$
The characteristic polynomial is computed as:
$$\det(\lambda I - J_1) = \det\begin{bmatrix} \lambda & -1 \\ 1 & \lambda - 0.1 \end{bmatrix} = \lambda(\lambda - 0.1) + 1 = \lambda^2 - 0.1\lambda + 1 = 0$$
Solving for the eigenvalues using the quadratic formula:
$$\lambda_{1,2} = \frac{0.1 \pm \sqrt{(-0.1)^2 - 4(1)(1)}}{2} = \frac{0.1 \pm \sqrt{0.01 - 4}}{2} = \frac{0.1 \pm \sqrt{-3.99}}{2} = 0.05 \pm j 0.9987$$
The eigenvalues are complex conjugates with a strictly positive real part ($\sigma = +0.05 > 0$). Consequently, Singular Point $P_1(0, 0)$ is classified as an Unstable Focus. In the physical phase plane, phase trajectories in the vicinity of the origin spiral continuously outward away from the origin in a clockwise direction as time advances, indicating that small perturbations will trigger growing oscillatory transients.

Analysis of Singular Point $P_2(-1, 0)$:
Substituting $(x_1, x_2) = (-1, 0)$ into the Jacobian matrix yields:
$$J_2 = \begin{bmatrix} 0 & 1 \\ -1 - 2(-1) & 0.1 \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ 1 & 0.1 \end{bmatrix}$$
The characteristic polynomial is computed as:
$$\det(\lambda I - J_2) = \det\begin{bmatrix} \lambda & -1 \\ -1 & \lambda - 0.1 \end{bmatrix} = \lambda(\lambda - 0.1) - 1 = \lambda^2 - 0.1\lambda - 1 = 0$$
Solving for the eigenvalues:
$$\lambda_{1,2} = \frac{0.1 \pm \sqrt{(-0.1)^2 - 4(1)(-1)}}{2} = \frac{0.1 \pm \sqrt{0.01 + 4}}{2} = \frac{0.1 \pm \sqrt{4.01}}{2} = \frac{0.1 \pm 2.0025}{2}$$
$$\lambda_1 = \frac{0.1 + 2.0025}{2} \approx +1.051, \quad \lambda_2 = \frac{0.1 - 2.0025}{2} \approx -0.951$$
The eigenvalues are real and possess opposite algebraic signs ($\lambda_1 > 0$ and $\lambda_2 < 0$). Consequently, Singular Point $P_2(-1, 0)$ is classified as a Saddle Point. In the phase plane, saddle points are fundamentally unstable. There exist two specific trajectories (the stable manifolds or separatrices) that approach $(-1, 0)$ as $t \to \infty$, while all other trajectories are deflected away along the unstable manifold.

To synthesize the global phase portrait, the isocline method is employed. The slope of any trajectory at an arbitrary point $(x_1, x_2)$ is given by the differential slope equation:
$$\frac{dx_2}{dx_1} = \frac{\dot{x}_2}{\dot{x}_1} = \frac{0.1 x_2 - x_1 - x_1^2}{x_2} = m$$
where $m$ denotes a constant slope value. Rearranging this relationship yields the algebraic equation for the isoclines:
$$0.1 x_2 - x_1 - x_1^2 = m x_2 \implies (m - 0.1)x_2 = -x_1(1 + x_1) \implies x_2 = -\frac{x_1(1 + x_1)}{m - 0.1}$$
For each chosen numerical slope $m$, this equation defines a parabola in the phase plane along which every crossing trajectory has the exact slope $m$. For example, setting $m = 0$ yields the zero-slope isocline $x_2 = 10 x_1(1 + x_1)$, where all trajectories have purely horizontal tangents. Plotting these directional slope line segments reveals the complete portrait: trajectories originate near the unstable focus $(0, 0)$, spiral outward clockwise, and are bounded on the left by the separatrix of the saddle point at $(-1, 0)$, providing a complete global understanding of system dynamics.
"""
            },
            {
                "qid": "acs-q22",
                "marks": 7,
                "type": "Long Derivation",
                "title": "Lyapunov's Direct Method: Stability Theorems and Solution of Matrix Equation A^T P + P A = -Q",
                "yt_query": "lyapunov stability direct method solve matrix equation ATP+PA=-Q example",
                "img_path": "images/acs/lyapunov_stability_contours.png",
                "img_caption": "Figure 5.4: State Trajectory Penetrating Inward across Lyapunov Contours V(x) = C",
                "answer": r"""
Lyapunov's Direct (or Second) Method represents the most universal and profound analytical framework for determining the stability of linear and non-linear dynamic systems without solving the underlying differential equations. Proposed by Aleksandr Lyapunov in 1892, the method generalizes the fundamental physical concept of energy: if a physical system has a state of minimum potential energy (the origin), and if the total rate of energy dissipation is continuously negative along every possible trajectory, the system must eventually shed all its energy and come to rest at the equilibrium point.

The foundational theorems of Lyapunov's Direct Method for an autonomous system $\dot{x} = f(x)$ with an isolated equilibrium at the origin ($f(0) = 0$) are formulated as follows:
Theorem 1 (Lyapunov Stability): If there exists a scalar function $V(x)$ that is continuously differentiable, positive definite ($V(0) = 0$ and $V(x) > 0$ for all $x \ne 0$) in a domain $\Omega$ containing the origin, and whose time derivative along system trajectories is negative semi-definite ($\dot{V}(x) \le 0$ for all $x \in \Omega$), then the origin is stable in the sense of Lyapunov.
Theorem 2 (Asymptotic Stability): If the candidate function $V(x)$ is positive definite and its time derivative along system trajectories is strictly negative definite ($\dot{V}(x) < 0$ for all $x \ne 0$), then the origin is asymptotically stable, ensuring that all trajectories converge to the origin as $t \to \infty$.
Theorem 3 (Global Asymptotic Stability): If the conditions for asymptotic stability hold across the entire state space $\mathbb{R}^n$, and in addition the candidate function is radially unbounded (meaning $V(x) \to \infty$ as $\|x\| \to \infty$), then the origin is globally asymptotically stable.

For continuous-time linear time-invariant systems described by $\dot{x} = A x$, Lyapunov stability can be determined with complete algorithmic precision. We choose a quadratic Lyapunov candidate function $V(x) = x^T P x$, where $P$ is a real, symmetric, positive definite matrix ($P = P^T > 0$). Computing the total time derivative of $V(x)$ along the linear trajectories:
$$\dot{V}(x) = \dot{x}^T P x + x^T P \dot{x} = (A x)^T P x + x^T P (A x) = x^T A^T P x + x^T P A x = x^T (A^T P + P A) x$$
For $\dot{V}(x)$ to be strictly negative definite for all $x \ne 0$, the bracketed matrix must be strictly negative definite. Defining a positive definite symmetric matrix $Q = Q^T > 0$, we set:
$$A^T P + P A = -Q$$
This matrix relationship is known as the Lyapunov Matrix Equation. Lyapunov's linear stability theorem asserts that a continuous LTI system matrix $A$ is asymptotically stable (Hurwitz) if and only if, for any arbitrarily chosen positive definite symmetric matrix $Q$, there exists a unique positive definite symmetric matrix $P$ that satisfies $A^T P + P A = -Q$. In standard practice, $Q$ is chosen as the identity matrix $I$.

To demonstrate the full analytical execution of this method, consider the system matrix presented in the university examination:
$$\dot{x} = A x = \begin{bmatrix} 0 & 1 \\ -2 & -3 \end{bmatrix} x$$
We select the identity matrix as our positive definite matrix: $Q = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = I$.
Let the unknown symmetric matrix $P$ be represented as:
$$P = \begin{bmatrix} p_{11} & p_{12} \\ p_{12} & p_{22} \end{bmatrix}$$
We compute the matrix terms in the Lyapunov equation:
$$A^T P = \begin{bmatrix} 0 & -2 \\ 1 & -3 \end{bmatrix} \begin{bmatrix} p_{11} & p_{12} \\ p_{12} & p_{22} \end{bmatrix} = \begin{bmatrix} -2p_{12} & -2p_{22} \\ p_{11} - 3p_{12} & p_{12} - 3p_{22} \end{bmatrix}$$
$$P A = (A^T P)^T = \begin{bmatrix} -2p_{12} & p_{11} - 3p_{12} \\ -2p_{22} & p_{12} - 3p_{22} \end{bmatrix}$$
Summing these two matrices yields:
$$A^T P + P A = \begin{bmatrix} -4p_{12} & p_{11} - 3p_{12} - 2p_{22} \\ p_{11} - 3p_{12} - 2p_{22} & 2p_{12} - 6p_{22} \end{bmatrix} = \begin{bmatrix} -1 & 0 \\ 0 & -1 \end{bmatrix}$$

This matrix equality yields three simultaneous linear algebraic equations:
$$-4p_{12} = -1 \implies p_{12} = \frac{1}{4} = 0.25$$
$$2p_{12} - 6p_{22} = -1 \implies 2\left(\frac{1}{4}\right) - 6p_{22} = -1 \implies \frac{1}{2} - 6p_{22} = -1 \implies 6p_{22} = \frac{3}{2} \implies p_{22} = \frac{3}{12} = \frac{1}{4} = 0.25$$
$$p_{11} - 3p_{12} - 2p_{22} = 0 \implies p_{11} = 3p_{12} + 2p_{22} = 3\left(\frac{1}{4}\right) + 2\left(\frac{1}{4}\right) = \frac{5}{4} = 1.25$$
Thus, the unique matrix $P$ is:
$$P = \begin{bmatrix} \frac{5}{4} & \frac{1}{4} \\ \frac{1}{4} & \frac{1}{4} \end{bmatrix} = \begin{bmatrix} 1.25 & 0.25 \\ 0.25 & 0.25 \end{bmatrix}$$

We now verify the positive definiteness of matrix $P$ using Sylvester's criterion:
The first leading principal minor is $\Delta_1 = p_{11} = \frac{5}{4} = 1.25 > 0$.
The second leading principal minor is the determinant:
$$\Delta_2 = \det(P) = \left(\frac{5}{4}\right)\left(\frac{1}{4}\right) - \left(\frac{1}{4}\right)^2 = \frac{5}{16} - \frac{1}{16} = \frac{4}{16} = \frac{1}{4} = 0.25 > 0$$
Because both leading principal minors are strictly positive, matrix $P$ is strictly positive definite. Therefore, the Lyapunov candidate function $V(x) = x^T P x = 1.25 x_1^2 + 0.5 x_1 x_2 + 0.25 x_2^2$ is positive definite, and its time derivative $\dot{V}(x) = -x^T Q x = -(x_1^2 + x_2^2)$ is strictly negative definite. By Lyapunov's Direct Theorem, the system is unconditionally asymptotically stable in the large.
"""
            }
        ]
    }
]
