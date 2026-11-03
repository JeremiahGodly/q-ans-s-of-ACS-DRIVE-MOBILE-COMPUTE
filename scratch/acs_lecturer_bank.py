# scratch/acs_lecturer_bank.py
# Complete KTU Exam-Ready Answers for Subject 1: Advanced Control Systems (EET401)
# Written in simple, direct local English with rich core content, clear bullet points,
# step-by-step mathematical working, and intuitive everyday engineering analogies.

ACS_ANSWERS = {
    # =========================================================================
    # MODULE 1: State Space Analysis Basics, Modeling & Canonical Forms
    # =========================================================================
    'acs-q1': {
        "title": "State Space Concepts: State, State Variables, State Vector, and State Space",
        "marks": 3,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$\dot{\mathbf{x}}(t) = A\mathbf{x}(t) + B\mathbf{u}(t), \quad \mathbf{y}(t) = C\mathbf{x}(t) + D\mathbf{u}(t)$$",
            "text": "State = Minimum set of variables at $t_0$ needed to predict the future behavior of the system."
        },
        "exam_answer": r"""
<p><strong>1. State of a System:</strong></p>
<ul>
    <li>The <strong>state</strong> of a dynamic system is defined as the minimal set of variables $\{x_1(t), x_2(t), \dots, x_n(t)\}$ such that the knowledge of these variables at any initial time $t = t_0$, together with the knowledge of input excitation $u(t)$ for all $t \ge t_0$, completely determines the future state and output of the system for any time $t > t_0$.</li>
    <li>It represents the internal dynamic memory of the system.</li>
</ul>

<p><strong>2. State Variables:</strong></p>
<ul>
    <li>The individual variables that make up the state are called <strong>state variables</strong>.</li>
    <li>They are the minimum number of linearly independent variables that represent all independent energy storage elements in the system.</li>
    <li><strong>Examples:</strong>
        <ul>
            <li>In electrical systems: Inductor current $i_L(t)$ (magnetic energy) and capacitor voltage $v_C(t)$ (electric energy).</li>
            <li>In mechanical systems: Displacement $y(t)$ (potential energy) and velocity $\dot{y}(t)$ (kinetic energy).</li>
        </ul>
    </li>
</ul>

<p><strong>3. State Vector:</strong></p>
<ul>
    <li>If an $n$-th order system requires $n$ state variables, they are grouped together into an $n \times 1$ column vector called the <strong>state vector</strong> $\mathbf{x}(t)$:
    $$\mathbf{x}(t) = \begin{bmatrix} x_1(t) \\ x_2(t) \\ \vdots \\ x_n(t) \end{bmatrix} \in \mathbb{R}^n$$</li>
</ul>

<p><strong>4. State Space:</strong></p>
<ul>
    <li>The $n$-dimensional vector space whose coordinate axes are the individual state variables $x_1, x_2, \dots, x_n$ is called the <strong>state space</strong>.</li>
    <li>At any time instant $t$, the operating condition of the system is represented by a single point called the <strong>state point</strong>.</li>
    <li>As time progresses, this point moves and traces a continuous curve called the <strong>state trajectory</strong>.</li>
</ul>
""",
        "understand_simply": r"""
<p>Think of tracking a cricket ball in flight. If you know its current position $(x, y, z)$ and its velocity $(v_x, v_y, v_z)$ right now, plus gravity and wind, you can predict its entire path. You don't need to know where the bowler was standing 10 minutes ago!</p>
<p>Here, position and velocity are the <strong>state variables</strong>. Together they form the <strong>state vector</strong>. The 3D space in which the ball flies is the <strong>state space</strong>, and the arc traced by the ball is the <strong>state trajectory</strong>.</p>
"""
    },

    'acs-q2': {
        "title": "Phase Variables and Continuous-Time State-Space Formulation",
        "marks": 3,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$x_1 = y, \quad x_2 = \dot{y}, \quad \dots, \quad x_n = y^{(n-1)}$$",
            "text": "Phase variables are chosen by setting the output as first state and each next state as its derivative."
        },
        "exam_answer": r"""
<p><strong>1. Definition of Phase Variables:</strong></p>
<ul>
    <li>Phase variables are a particular set of state variables where each successive state variable is defined as the exact time derivative of the previous variable, starting with the system output $y(t)$:
    $$x_1 = y(t)$$
    $$x_2 = \dot{y}(t) = \dot{x}_1$$
    $$x_3 = \ddot{y}(t) = \dot{x}_2$$
    $$\vdots$$
    $$x_n = y^{(n-1)}(t) = \dot{x}_{n-1}$$</li>
</ul>

<p><strong>2. State-Space Formulation from Differential Equation:</strong></p>
<p>Consider a general $n$-th order linear differential equation with constant coefficients:
$$y^{(n)} + a_{n-1}y^{(n-1)} + \dots + a_1\dot{y} + a_0 y = b_0 u(t)$$</p>
<p>Express the highest derivative $\dot{x}_n = y^{(n)}$ in terms of other state variables and input:
$$\dot{x}_n = -a_0 x_1 - a_1 x_2 - \dots - a_{n-1} x_n + b_0 u(t)$$</p>

<p><strong>3. Matrix Representation (Companion Form):</strong></p>
$$\begin{bmatrix} \dot{x}_1 \\ \dot{x}_2 \\ \vdots \\ \dot{x}_{n-1} \\ \dot{x}_n \end{bmatrix} = \begin{bmatrix} 0 & 1 & 0 & \dots & 0 \\ 0 & 0 & 1 & \dots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \dots & 1 \\ -a_0 & -a_1 & -a_2 & \dots & -a_{n-1} \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_{n-1} \\ x_n \end{bmatrix} + \begin{bmatrix} 0 \\ 0 \\ \vdots \\ 0 \\ b_0 \end{bmatrix} u(t)$$
$$y(t) = \begin{bmatrix} 1 & 0 & \dots & 0 \end{bmatrix} \mathbf{x}(t)$$
<p><strong>Key Advantages:</strong> Matrix $A$ is in Bush form (Companion form). The last row directly gives the coefficients of the characteristic equation, which makes checking controllability very simple.</p>
""",
        "understand_simply": r"""
<p>If you have an equation with position, speed, and acceleration (like a moving car), phase variables simply say: let $x_1$ be position, let $x_2$ be speed ($\dot{x}_1$), and let $x_3$ be acceleration ($\dot{x}_2$). It converts one complicated high-order equation into a ladder of simple first-order integrator steps!</p>
"""
    },

    'acs-q3': {
        "title": "Block Diagram Representation of Continuous-Time LTI State-Space System",
        "marks": 3,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$\dot{\mathbf{x}} = A\mathbf{x} + B\mathbf{u}, \quad \mathbf{y} = C\mathbf{x} + D\mathbf{u}$$",
            "text": "Core element: Bank of integrators $\\frac{1}{s}$ converts $\\dot{\\mathbf{x}}$ into $\\mathbf{x}$."
        },
        "exam_answer": r"""
<p><strong>1. Governing Equations:</strong></p>
<p>Any continuous-time Linear Time-Invariant (LTI) system is represented in state-space by:
$$\dot{\mathbf{x}}(t) = A\mathbf{x}(t) + B\mathbf{u}(t) \quad \text{--- [State Equation]}$$
$$\mathbf{y}(t) = C\mathbf{x}(t) + D\mathbf{u}(t) \quad \text{--- [Output Equation]}$$</p>

<p><strong>2. Description of Block Diagram Elements:</strong></p>
<ul>
    <li><strong>Integrator Block ($\int$ or $\frac{1}{s}$):</strong> The heart of the diagram. The input to the integrator is the state derivative vector $\dot{\mathbf{x}}(t)$, and its output is the state vector $\mathbf{x}(t)$. For an $n$-th order system, it represents $n$ parallel integrators.</li>
    <li><strong>State Matrix $A$ ($n \times n$):</strong> Feedback gain block feeding $\mathbf{x}(t)$ back to the summer to calculate internal dynamics $A\mathbf{x}(t)$.</li>
    <li><strong>Input Matrix $B$ ($n \times m$):</strong> Multiplies input vector $\mathbf{u}(t)$ to couple external inputs into state derivatives $B\mathbf{u}(t)$.</li>
    <li><strong>Output Matrix $C$ ($p \times n$):</strong> Multiplies state vector $\mathbf{x}(t)$ to determine how internal states contribute to measured outputs $C\mathbf{x}(t)$.</li>
    <li><strong>Direct Transmission Matrix $D$ ($p \times m$):</strong> Direct feedthrough gain connecting input $\mathbf{u}(t)$ directly to output $\mathbf{y}(t)$ without passing through integrators (often zero in physical systems).</li>
    <li><strong>Summing Points:</strong> One summer adds $A\mathbf{x} + B\mathbf{u} = \dot{\mathbf{x}}$, and another summer adds $C\mathbf{x} + D\mathbf{u} = \mathbf{y}$.</li>
</ul>
""",
        "understand_simply": r"""
<p>Think of the integrator as a water bucket. The water flowing in is the rate of change ($\dot{\mathbf{x}}$), and the water level inside the bucket is the state ($\mathbf{x}$). The matrix $A$ tells how much water leaks back into the inlet, $B$ is the external tap adding water, and $C$ is the meter measuring the level.</p>
"""
    },

    'acs-q4': {
        "title": "Non-Uniqueness of State Space Models via Similarity Transformation",
        "marks": 3,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$\bar{A} = P^{-1}AP, \quad \bar{B} = P^{-1}B, \quad \bar{C} = CP, \quad \bar{D} = D$$",
            "text": "State-space models are not unique; an infinite number of representations exist by changing state coordinates via non-singular matrix $P$."
        },
        "exam_answer": r"""
<p><strong>1. Principle of Non-Uniqueness:</strong></p>
<ul>
    <li>While the input-output transfer function of a physical system is unique, its state-space representation is <strong>not unique</strong>.</li>
    <li>There are an infinite number of valid state-space models for the same system because state variables can be chosen in infinitely many coordinate systems.</li>
</ul>

<p><strong>2. Mathematical Proof via Similarity Transformation:</strong></p>
<p>Let the original state model be:
$$\dot{\mathbf{x}} = A\mathbf{x} + B\mathbf{u}, \quad \mathbf{y} = C\mathbf{x} + D\mathbf{u}$$
Define a new state vector $\mathbf{z}(t)$ through a non-singular transformation matrix $P$ ($n \times n$ with $\det(P) \ne 0$):
$$\mathbf{x}(t) = P\mathbf{z}(t) \implies \mathbf{z}(t) = P^{-1}\mathbf{x}(t)$$
Differentiating both sides with respect to time:
$$\dot{\mathbf{x}}(t) = P\dot{\mathbf{z}}(t)$$
Substitute $\mathbf{x} = P\mathbf{z}$ and $\dot{\mathbf{x}} = P\dot{\mathbf{z}}$ into the original state equation:
$$P\dot{\mathbf{z}}(t) = A(P\mathbf{z}(t)) + B\mathbf{u}(t)$$
Premultiplying both sides by $P^{-1}$:
$$\dot{\mathbf{z}}(t) = \left(P^{-1}AP\right)\mathbf{z}(t) + \left(P^{-1}B\right)\mathbf{u}(t)$$
Now substitute $\mathbf{x} = P\mathbf{z}$ into the output equation:
$$\mathbf{y}(t) = \left(CP\right)\mathbf{z}(t) + D\mathbf{u}(t)$$
Thus, the new transformed system matrices are:
$$\bar{A} = P^{-1}AP, \quad \bar{B} = P^{-1}B, \quad \bar{C} = CP, \quad \bar{D} = D$$
<strong>Invariance Property:</strong> The eigenvalues and the transfer function $G(s) = \bar{C}(sI - \bar{A})^{-1}\bar{B} + \bar{D} = C(sI - A)^{-1}B + D$ remain strictly identical under any valid transformation $P$.</p>
""",
        "understand_simply": r"""
<p>Say you want to specify a location in Kochi. You can use latitude/longitude, or you can use distance from Marine Drive in kilometers. The physical spot is the same, but the coordinate numbers look totally different. That is all similarity transformation does: it rotates the coordinate axes without changing the actual physical system.</p>
"""
    },

    'acs-q4b': {
        "title": "Transfer Function Matrix Derivation from State Space Model",
        "marks": 7,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$G(s) = C(sI - A)^{-1}B + D = \frac{C \operatorname{adj}(sI - A) B}{\det(sI - A)} + D$$",
            "text": "Poles of $G(s)$ are the eigenvalues of matrix $A$ (roots of $\\det(sI - A) = 0$)."
        },
        "exam_answer": r"""
<p><strong>1. Given State-Space Equations:</strong><br>
Consider a continuous-time linear time-invariant (LTI) system:
$$\dot{\mathbf{x}}(t) = A\mathbf{x}(t) + B\mathbf{u}(t) \quad \text{--- (1) [State Equation]}$$
$$\mathbf{y}(t) = C\mathbf{x}(t) + D\mathbf{u}(t) \quad \text{--- (2) [Output Equation]}$$
where $\mathbf{x}(t) \in \mathbb{R}^n$, $\mathbf{u}(t) \in \mathbb{R}^m$, $\mathbf{y}(t) \in \mathbb{R}^p$.</p>

<p><strong>2. Assumption:</strong><br>
By definition, transfer function is defined under <strong>zero initial conditions</strong> ($\mathbf{x}(0) = \mathbf{0}$).</p>

<p><strong>3. Step-by-Step Derivation:</strong></p>
<p><strong>Step 1: Take Laplace Transform of the State Equation</strong><br>
$$\mathcal{L}\{\dot{\mathbf{x}}(t)\} = s\mathbf{X}(s) - \mathbf{x}(0) = A\mathbf{X}(s) + B\mathbf{U}(s)$$
Substituting $\mathbf{x}(0) = \mathbf{0}$:
$$s\mathbf{X}(s) - A\mathbf{X}(s) = B\mathbf{U}(s)$$
$$(sI - A)\mathbf{X}(s) = B\mathbf{U}(s)$$
where $I$ is the $n \times n$ identity matrix.</p>

<p><strong>Step 2: Solve for State Vector $\mathbf{X}(s)$</strong><br>
Premultiplying both sides by the inverse matrix $(sI - A)^{-1}$ (the resolvent matrix):
$$\mathbf{X}(s) = (sI - A)^{-1} B \mathbf{U}(s) \quad \text{--- (3)}$$</p>

<p><strong>Step 3: Take Laplace Transform of Output Equation</strong><br>
$$\mathbf{Y}(s) = C\mathbf{X}(s) + D\mathbf{U}(s) \quad \text{--- (4)}$$</p>

<p><strong>Step 4: Substitute Equation (3) into Equation (4)</strong><br>
$$\mathbf{Y}(s) = C\left[(sI - A)^{-1} B \mathbf{U}(s)\right] + D\mathbf{U}(s)$$
Factoring out the input transform $\mathbf{U}(s)$:
$$\mathbf{Y}(s) = \left[ C(sI - A)^{-1} B + D \right] \mathbf{U}(s)$$</p>

<p><strong>4. Final Transfer Function Matrix:</strong><br>
$$G(s) = \frac{\mathbf{Y}(s)}{\mathbf{U}(s)} = C(sI - A)^{-1} B + D$$
Using the matrix inverse formula $(sI - A)^{-1} = \frac{\operatorname{adj}(sI - A)}{\det(sI - A)}$:
$$G(s) = \frac{C \operatorname{adj}(sI - A) B}{\det(sI - A)} + D$$
<strong>Significance:</strong> The denominator of $G(s)$ is the characteristic polynomial $\det(sI - A) = 0$. Therefore, the poles of the transfer function are the eigenvalues of state matrix $A$.</p>
""",
        "understand_simply": r"""
<p>Classical transfer function treats the system like a sealed black box (input goes in, output comes out). State space looks inside the box at the energy variables $\mathbf{X}(s)$. This derivation is simply using algebra to eliminate $\mathbf{X}(s)$ from the middle and connect input $\mathbf{U}(s)$ directly to output $\mathbf{Y}(s)$.</p>
"""
    },

    'acs-q5': {
        "title": "Comprehensive State-Space Modeling of a Series RLC Circuit",
        "marks": 7,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$\begin{bmatrix} \dot{i}_L \\ \dot{v}_C \end{bmatrix} = \begin{bmatrix} -R/L & -1/L \\ 1/C & 0 \end{bmatrix} \begin{bmatrix} i_L \\ v_C \end{bmatrix} + \begin{bmatrix} 1/L \\ 0 \end{bmatrix} v(t)$$",
            "text": "Choose inductor current $i_L$ and capacitor voltage $v_C$ as states because they govern stored energy."
        },
        "exam_answer": r"""
<p><strong>1. Identification of State Variables &amp; Inputs:</strong></p>
<ul>
    <li>Consider a series RLC circuit excited by an applied voltage source $v(t)$.</li>
    <li>The independent energy-storing elements are:
        <ul>
            <li>Inductor $L$: Stores magnetic energy $E_L = \frac{1}{2} L i_L^2 \implies$ State variable $x_1(t) = i_L(t)$.</li>
            <li>Capacitor $C$: Stores electric energy $E_C = \frac{1}{2} C v_C^2 \implies$ State variable $x_2(t) = v_C(t)$.</li>
        </ul>
    </li>
    <li>Input: $u(t) = v(t)$ (source voltage).</li>
    <li>Output: Let output $y(t) = v_C(t)$ (voltage across capacitor).</li>
</ul>

<p><strong>2. Derivation of State Equations:</strong></p>
<p><strong>Equation 1 (Using KVL around the series loop):</strong><br>
$$v(t) = v_R(t) + v_L(t) + v_C(t)$$
Using component relationships $v_R = R i_L$ and $v_L = L \frac{d i_L}{dt}$:
$$L \frac{d i_L(t)}{dt} + R i_L(t) + v_C(t) = v(t)$$
Rearranging for $\frac{d i_L}{dt} = \dot{x}_1$:
$$\frac{d i_L}{dt} = -\frac{R}{L} i_L - \frac{1}{L} v_C + \frac{1}{L} v(t)$$
$$\dot{x}_1(t) = -\frac{R}{L} x_1(t) - \frac{1}{L} x_2(t) + \frac{1}{L} u(t) \quad \text{--- (1)}$$</p>

<p><strong>Equation 2 (Using Capacitor Current Relation):</strong><br>
Because elements are in series, current through capacitor is $i_L$:
$$i_C(t) = C \frac{d v_C(t)}{dt} = i_L(t)$$
Rearranging for $\frac{d v_C}{dt} = \dot{x}_2$:
$$\dot{x}_2(t) = \frac{1}{C} x_1(t) \quad \text{--- (2)}$$</p>

<p><strong>3. Final Vector-Matrix State-Space Model:</strong><br>
Combining Equations (1) and (2) into $\dot{\mathbf{x}} = A\mathbf{x} + B\mathbf{u}$:
$$\begin{bmatrix} \dot{x}_1(t) \\ \dot{x}_2(t) \end{bmatrix} = \begin{bmatrix} -\frac{R}{L} & -\frac{1}{L} \\ \frac{1}{C} & 0 \end{bmatrix} \begin{bmatrix} x_1(t) \\ x_2(t) \end{bmatrix} + \begin{bmatrix} \frac{1}{L} \\ 0 \end{bmatrix} u(t)$$
Output equation for $y(t) = v_C(t) = x_2(t)$:
$$y(t) = \begin{bmatrix} 0 & 1 \end{bmatrix} \begin{bmatrix} x_1(t) \\ x_2(t) \end{bmatrix} + [0] u(t)$$
Here:
$$A = \begin{bmatrix} -R/L & -1/L \\ 1/C & 0 \end{bmatrix}, \quad B = \begin{bmatrix} 1/L \\ 0 \end{bmatrix}, \quad C = \begin{bmatrix} 0 & 1 \end{bmatrix}, \quad D = [0]$$</p>
""",
        "understand_simply": r"""
<p>An electrical circuit is like a water system: the inductor is like a heavy water wheel that keeps spinning due to inertia (current $i_L$), and the capacitor is like an elastic tank that stores water pressure (voltage $v_C$). To know the state of the circuit at any second, you only need to know how fast the wheel is turning ($i_L$) and how pressurized the tank is ($v_C$).</p>
"""
    },

    'acs-q6': {
        "title": "State-Space Model of an Armature-Controlled DC Motor",
        "marks": 7,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$\begin{bmatrix} \dot{i}_a \\ \dot{\omega}_m \end{bmatrix} = \begin{bmatrix} -R_a/L_a & -K_b/L_a \\ K_t/J & -B/J \end{bmatrix} \begin{bmatrix} i_a \\ \omega_m \end{bmatrix} + \begin{bmatrix} 1/L_a \\ 0 \end{bmatrix} v_a(t)$$",
            "text": "Armature current $i_a$ and rotor speed $\\omega_m$ form the electromechanical state variables."
        },
        "exam_answer": r"""
<p><strong>1. System Description &amp; Variables:</strong></p>
<ul>
    <li>In an armature-controlled DC motor, field current $I_f$ is kept constant, so field flux $\Phi$ is constant.</li>
    <li>Input: Armature voltage $u(t) = v_a(t)$.</li>
    <li>State Variables:
        <ul>
            <li>Electrical state: Armature current $x_1(t) = i_a(t)$.</li>
            <li>Mechanical state: Rotor angular speed $x_2(t) = \omega_m(t)$ (or position $\theta$).</li>
        </ul>
    </li>
    <li>Output: Rotor speed $y(t) = \omega_m(t)$.</li>
</ul>

<p><strong>2. Governing Differential Equations:</strong></p>
<p><strong>Electrical Equation (Armature Loop KVL):</strong><br>
$$v_a(t) = R_a i_a(t) + L_a \frac{d i_a(t)}{dt} + e_b(t)$$
where back-EMF is proportional to speed: $e_b(t) = K_b \omega_m(t) = K_b x_2(t)$.<br>
Rearranging for $\dot{i}_a = \dot{x}_1$:
$$\dot{x}_1(t) = -\frac{R_a}{L_a} x_1(t) - \frac{K_b}{L_a} x_2(t) + \frac{1}{L_a} u(t) \quad \text{--- (1)}$$</p>

<p><strong>Mechanical Equation (Torque Balance):</strong><br>
Developed electromagnetic torque: $T(t) = K_t i_a(t) = K_t x_1(t)$.<br>
Newton's second law for rotor dynamics:
$$T(t) = J \frac{d\omega_m(t)}{dt} + B \omega_m(t) + T_L$$
Assuming load torque $T_L = 0$ (unloaded motor):
$$J \frac{d\omega_m}{dt} + B \omega_m = K_t i_a$$
Rearranging for $\dot{\omega}_m = \dot{x}_2$:
$$\dot{x}_2(t) = \frac{K_t}{J} x_1(t) - \frac{B}{J} x_2(t) \quad \text{--- (2)}$$</p>

<p><strong>3. Matrix State-Space Formulation:</strong><br>
Combining Equations (1) and (2):
$$\begin{bmatrix} \dot{x}_1 \\ \dot{x}_2 \end{bmatrix} = \begin{bmatrix} -\frac{R_a}{L_a} & -\frac{K_b}{L_a} \\ \frac{K_t}{J} & -\frac{B}{J} \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} + \begin{bmatrix} \frac{1}{L_a} \\ 0 \end{bmatrix} u(t)$$
Output equation:
$$y(t) = \begin{bmatrix} 0 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$$
where $J$ is rotor moment of inertia ($\text{kg}\cdot\text{m}^2$), $B$ is viscous friction coefficient ($\text{N}\cdot\text{m}\cdot\text{s/rad}$), $R_a$ is armature resistance ($\Omega$), $L_a$ is armature inductance ($\text{H}$), $K_t$ is torque constant ($\text{N}\cdot\text{m/A}$), and $K_b$ is back-EMF constant ($\text{V}\cdot\text{s/rad}$).</p>
""",
        "understand_simply": r"""
<p>A DC motor is part electrical and part mechanical. The electrical part takes in voltage and pushes armature current $i_a$ against coil resistance and back-EMF. That current creates magnetic torque, which spins the mechanical rotor inertia $J$ up to speed $\omega_m$. So the motor has two states: electrical current $i_a$ and mechanical speed $\omega_m$.</p>
"""
    },

    'acs-q7': {
        "title": "Derivation of Controllable and Diagonal (Jordan) Canonical Forms",
        "marks": 7,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$A_{\text{controllable}} = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -a_0 & -a_1 & -a_2 \end{bmatrix}, \quad A_{\text{diagonal}} = \begin{bmatrix} \lambda_1 & 0 & 0 \\ 0 & \lambda_2 & 0 \\ 0 & 0 & \lambda_3 \end{bmatrix}$$",
            "text": "Canonical forms standardize state space for easy controllability, observability, and pole placement."
        },
        "exam_answer": r"""
<p><strong>1. Introduction:</strong><br>
Canonical forms are standardized state-space representations derived from transfer functions that highlight specific system properties (controllability, observability, or natural modes).</p>

<p>Consider a general 3rd-order transfer function:
$$G(s) = \frac{Y(s)}{U(s)} = \frac{b_2 s^2 + b_1 s + b_0}{s^3 + a_2 s^2 + a_1 s + a_0}$$</p>

<p><strong>2. Controllable Canonical Form (CCF):</strong></p>
<ul>
    <li>Directly obtained from phase-variable realization:
    $$\begin{bmatrix} \dot{x}_1 \\ \dot{x}_2 \\ \dot{x}_3 \end{bmatrix} = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -a_0 & -a_1 & -a_2 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} + \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} u(t)$$
    $$y(t) = \begin{bmatrix} b_0 & b_1 & b_2 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}$$</li>
    <li><strong>Significance:</strong> Controllability matrix $Q_c = [B \ AB \ A^2B]$ always has full rank ($3$), guaranteeing that the system is controllable. Ideal for pole placement controller design.</li>
</ul>

<p><strong>3. Diagonal Canonical Form (Jordan Canonical Form):</strong></p>
<ul>
    <li>Obtained by partial fraction expansion of $G(s)$ when poles $\lambda_1, \lambda_2, \lambda_3$ are distinct:
    $$G(s) = \frac{c_1}{s - \lambda_1} + \frac{c_2}{s - \lambda_2} + \frac{c_3}{s - \lambda_3}$$</li>
    <li>Assign state variables to each decoupled pole mode: $X_i(s) = \frac{1}{s - \lambda_i} U(s) \implies \dot{x}_i = \lambda_i x_i + u(t)$.</li>
    <li>Matrix Representation:
    $$\begin{bmatrix} \dot{x}_1 \\ \dot{x}_2 \\ \dot{x}_3 \end{bmatrix} = \begin{bmatrix} \lambda_1 & 0 & 0 \\ 0 & \lambda_2 & 0 \\ 0 & 0 & \lambda_3 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} + \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} u(t)$$
    $$y(t) = \begin{bmatrix} c_1 & c_2 & c_3 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}$$</li>
    <li><strong>Significance:</strong> Matrix $A$ is completely uncoupled (diagonal). Controllability and observability can be inspected directly: if any element in $B$ is zero, that mode is uncontrollable; if any element in $C$ is zero, that mode is unobservable.</li>
</ul>
""",
        "understand_simply": r"""
<p>If three workers are working together on a car assembly line, <strong>Controllable Form</strong> is like an assembly line where worker 1 passes parts to worker 2, who passes to worker 3. <strong>Diagonal Form</strong> is like giving each worker their own independent table where they work in parallel without touching each other's parts. Both build the same car, but Diagonal Form lets you immediately spot which worker is slacking off!</p>
"""
    },

    'acs-q7b': {
        "title": "State-Space Modeling of a Field-Controlled DC Servomotor",
        "marks": 7,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$\begin{bmatrix} \dot{i}_f \\ \dot{\omega}_m \end{bmatrix} = \begin{bmatrix} -R_f/L_f & 0 \\ K_{tf}/J & -B/J \end{bmatrix} \begin{bmatrix} i_f \\ \omega_m \end{bmatrix} + \begin{bmatrix} 1/L_f \\ 0 \end{bmatrix} v_f(t)$$",
            "text": "Armature current $I_a$ is constant; control input is applied to the field winding $v_f(t)$."
        },
        "exam_answer": r"""
<p><strong>1. Operating Principle:</strong></p>
<ul>
    <li>In a field-controlled DC motor, the armature current $I_a$ is supplied by a constant current source.</li>
    <li>The control input voltage $u(t) = v_f(t)$ is applied to the field circuit.</li>
    <li>Torque developed is proportional to field current: $T(t) = K_f I_a i_f(t) = K_{tf} i_f(t)$.</li>
    <li>Advantage: Field winding requires much less power than the heavy armature circuit.</li>
</ul>

<p><strong>2. Governing Differential Equations:</strong></p>
<p><strong>Field Circuit KVL:</strong><br>
$$v_f(t) = R_f i_f(t) + L_f \frac{d i_f(t)}{dt}$$
where $R_f$ is field winding resistance and $L_f$ is field inductance.<br>
Rearranging for $\dot{i}_f$:
$$\frac{d i_f}{dt} = -\frac{R_f}{L_f} i_f(t) + \frac{1}{L_f} v_f(t) \quad \text{--- (1)}$$</p>

<p><strong>Mechanical Torque Balance Equation:</strong><br>
$$T(t) = J \frac{d\omega_m(t)}{dt} + B\omega_m(t)$$
Substituting $T(t) = K_{tf} i_f(t)$:
$$J \frac{d\omega_m}{dt} + B\omega_m = K_{tf} i_f$$
Rearranging for $\dot{\omega}_m$:
$$\frac{d\omega_m}{dt} = \frac{K_{tf}}{J} i_f(t) - \frac{B}{J} \omega_m(t) \quad \text{--- (2)}$$</p>

<p><strong>3. Matrix State-Space Formulation:</strong><br>
Define states $x_1(t) = i_f(t)$, $x_2(t) = \omega_m(t)$, input $u(t) = v_f(t)$:
$$\begin{bmatrix} \dot{x}_1 \\ \dot{x}_2 \end{bmatrix} = \begin{bmatrix} -\frac{R_f}{L_f} & 0 \\ \frac{K_{tf}}{J} & -\frac{B}{J} \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} + \begin{bmatrix} \frac{1}{L_f} \\ 0 \end{bmatrix} u(t)$$
Output equation for rotor speed:
$$y(t) = \begin{bmatrix} 0 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$$
<strong>Key Difference from Armature Control:</strong> Notice $A_{12} = 0$ because there is no back-EMF term in the field circuit! The field dynamics are completely independent of the mechanical speed.</p>
""",
        "understand_simply": r"""
<p>In field control, you leave the main motor power running constant and only adjust the small magnetic coil on the side. It's like driving a car with the gas pedal floored, but controlling your speed by turning an electromagnet that pulls on the clutch. Because field coils are small, you need only tiny control signals to run the motor!</p>
"""
    },

    # =========================================================================
    # MODULE 2: Solution of State Equations, STM & Discrete Systems
    # =========================================================================
    'acs-q8': {
        "title": "Derivation of Solution of Autonomous State Equations using Laplace Transforms",
        "marks": 3,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$\dot{\mathbf{x}}(t) = A\mathbf{x}(t) \implies \mathbf{x}(t) = \mathcal{L}^{-1}\{(sI - A)^{-1}\}\mathbf{x}(0) = e^{At}\mathbf{x}(0)$$",
            "text": "Unforced solution depends purely on initial state energy $\\mathbf{x}(0)$ modulated by transition matrix $\\Phi(t)$."
        },
        "exam_answer": r"""
<p><strong>1. Problem Statement:</strong><br>
An unforced (homogeneous/autonomous) LTI continuous system has zero input ($\mathbf{u}(t) = \mathbf{0}$) and non-zero initial conditions $\mathbf{x}(0)$:
$$\dot{\mathbf{x}}(t) = A\mathbf{x}(t), \quad t \ge 0$$</p>

<p><strong>2. Step-by-Step Derivation:</strong></p>
<ul>
    <li>Take the unilateral Laplace transform on both sides:
    $$\mathcal{L}\{\dot{\mathbf{x}}(t)\} = s\mathbf{X}(s) - \mathbf{x}(0) = A\mathbf{X}(s)$$</li>
    <li>Rearrange to group the state transform $\mathbf{X}(s)$:
    $$s\mathbf{X}(s) - A\mathbf{X}(s) = \mathbf{x}(0)$$
    $$(sI - A)\mathbf{X}(s) = \mathbf{x}(0)$$</li>
    <li>Premultiply both sides by the inverse $(sI - A)^{-1}$:
    $$\mathbf{X}(s) = (sI - A)^{-1}\mathbf{x}(0)$$</li>
    <li>Take the inverse Laplace transform:
    $$\mathbf{x}(t) = \mathcal{L}^{-1}\left\{(sI - A)^{-1}\right\} \mathbf{x}(0)$$</li>
</ul>
<p><strong>Final Solution:</strong>
$$\mathbf{x}(t) = e^{At} \mathbf{x}(0) = \Phi(t) \mathbf{x}(0)$$
where $\Phi(t) = e^{At} = \mathcal{L}^{-1}\{(sI - A)^{-1}\}$ is the <strong>State Transition Matrix (STM)</strong>.</p>
""",
        "understand_simply": r"""
<p>Think of plucking a guitar string and letting go ($u=0$). The string vibrates and slowly dies out. How it vibrates depends only on how hard you plucked it initially ($\mathbf{x}(0)$) and the natural stiffness and dampening of the string ($e^{At}$).</p>
"""
    },

    'acs-q9': {
        "title": "Properties of the State Transition Matrix: Statement and Proofs",
        "marks": 3,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$\Phi(t) = e^{At} = \sum_{k=0}^{\infty} \frac{A^k t^k}{k!}$$",
            "text": "Core properties: $\\Phi(0) = I$, $\\Phi(-t) = \\Phi^{-1}(t)$, $\\Phi(t_1+t_2) = \\Phi(t_1)\\Phi(t_2)$, $[\\Phi(t)]^k = \\Phi(kt)$."
        },
        "exam_answer": r"""
<p><strong>Definition:</strong> The State Transition Matrix $\Phi(t) = e^{At}$ maps the initial state $\mathbf{x}(0)$ to state $\mathbf{x}(t)$ in an unforced continuous system: $\mathbf{x}(t) = \Phi(t)\mathbf{x}(0)$.</p>

<p><strong>Four Important Properties with Proofs:</strong></p>
<ol>
    <li><strong>Identity Property at $t = 0$:</strong>
    $$\Phi(0) = e^{A \cdot 0} = I$$
    <em>Proof:</em> At $t = 0$, $\mathbf{x}(0) = \Phi(0)\mathbf{x}(0) \implies \Phi(0) = I$.</li>
    <li><strong>Inverse Transition Property:</strong>
    $$\Phi(-t) = [\Phi(t)]^{-1} = e^{-At}$$
    <em>Proof:</em> $\Phi(t)\Phi(-t) = e^{At} e^{-At} = e^{A(t - t)} = e^0 = I \implies \Phi(-t) = [\Phi(t)]^{-1}$.</li>
    <li><strong>Semi-Group Composition Property:</strong>
    $$\Phi(t_1 + t_2) = \Phi(t_1)\Phi(t_2) = \Phi(t_2)\Phi(t_1)$$
    <em>Proof:</em> $\Phi(t_1 + t_2) = e^{A(t_1 + t_2)} = e^{At_1} e^{At_2} = \Phi(t_1)\Phi(t_2)$.</li>
    <li><strong>Power Multiplication Property:</strong>
    $$[\Phi(t)]^k = \Phi(kt) \quad \text{for any integer } k$$
    <em>Proof:</em> $[e^{At}]^k = e^{A(kt)} = \Phi(kt)$.</li>
</ol>
""",
        "understand_simply": r"""
<p>The state transition matrix is a time machine for dynamic systems: $\Phi(1)$ tells you where the system will be in 1 second. Moving forward 2 seconds ($\Phi(2)$) is the exact same as moving 1 second twice ($\Phi(1) \cdot \Phi(1)$). And rewinding 1 second in time is simply the mathematical inverse matrix ($\Phi(-1) = \Phi(1)^{-1}$).</p>
"""
    },

    'acs-q9b': {
        "title": "Discrete-Time State Space Analysis: Pulse Transfer Function and State Equations",
        "marks": 3,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$\mathbf{x}(k+1) = G\mathbf{x}(k) + H\mathbf{u}(k), \quad G(z) = C(zI - G)^{-1}H + D$$",
            "text": "Discrete state equations use difference equations; $z$-transform replaces Laplace transform."
        },
        "exam_answer": r"""
<p><strong>1. Discrete-Time State-Space Equations:</strong><br>
When a continuous system is sampled with period $T$, it is modeled by linear difference equations:
$$\mathbf{x}(k+1) = G\mathbf{x}(k) + H\mathbf{u}(k) \quad \text{--- [State Equation]}$$
$$\mathbf{y}(k) = C\mathbf{x}(k) + D\mathbf{u}(k) \quad \text{--- [Output Equation]}$$
where $\mathbf{x}(k)$ is the state vector at sampling instant $t = kT$, and:
$$G = e^{AT}, \quad H = \left(\int_0^T e^{At} dt\right) B$$</p>

<p><strong>2. Pulse Transfer Function Derivation via Z-Transform:</strong></p>
<ul>
    <li>Take the $z$-transform on both sides assuming zero initial states ($\mathbf{x}(0) = \mathbf{0}$):
    $$\mathcal{Z}\{\mathbf{x}(k+1)\} = z\mathbf{X}(z) = G\mathbf{X}(z) + H\mathbf{U}(z)$$
    $$(zI - G)\mathbf{X}(z) = H\mathbf{U}(z) \implies \mathbf{X}(z) = (zI - G)^{-1} H \mathbf{U}(z)$$</li>
    <li>Substitute $\mathbf{X}(z)$ into output equation $\mathbf{Y}(z) = C\mathbf{X}(z) + D\mathbf{U}(z)$:
    $$\mathbf{Y}(z) = \left[ C(zI - G)^{-1} H + D \right] \mathbf{U}(z)$$</li>
</ul>
<p><strong>Final Pulse Transfer Function:</strong>
$$G(z) = \frac{\mathbf{Y}(z)}{\mathbf{U}(z)} = C(zI - G)^{-1} H + D$$</p>
""",
        "understand_simply": r"""
<p>Continuous systems flow smoothly like an analog clock. But a microcontroller cannot watch continuous time—it takes snapshots every $T$ milliseconds (like a digital clock ticking). Discrete state space simply updates the state at tick $k+1$ using the state at tick $k$.</p>
"""
    },

    'acs-q10': {
        "title": "Computation of State Transition Matrix using Cayley-Hamilton Theorem",
        "marks": 7,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$e^{At} = \sum_{k=0}^{n-1} \alpha_k(t) A^k, \quad e^{\lambda_i t} = \sum_{k=0}^{n-1} \alpha_k(t) \lambda_i^k$$",
            "text": "Every square matrix satisfies its characteristic polynomial; reduces infinite matrix series $e^{At}$ to a degree $(n-1)$ polynomial."
        },
        "exam_answer": r"""
<p><strong>1. Statement of Cayley-Hamilton Theorem:</strong><br>
Every square matrix $A$ of order $n \times n$ satisfies its own characteristic equation:
$$\Delta(\lambda) = \det(\lambda I - A) = \lambda^n + a_{n-1}\lambda^{n-1} + \dots + a_1\lambda + a_0 = 0$$
$$\implies A^n + a_{n-1}A^{n-1} + \dots + a_1 A + a_0 I = \mathbf{0}$$</p>

<p><strong>2. Theoretical Principle:</strong><br>
The matrix exponential is an infinite series: $e^{At} = I + At + \frac{A^2 t^2}{2!} + \dots$<br>
Using Cayley-Hamilton, any higher power $A^k$ ($k \ge n$) can be expressed as a linear combination of lower powers $I, A, A^2, \dots, A^{n-1}$.<br>
Therefore, $e^{At}$ reduces to a finite polynomial of degree $(n-1)$:
$$e^{At} = \alpha_0(t)I + \alpha_1(t)A + \alpha_2(t)A^2 + \dots + \alpha_{n-1}(t)A^{n-1} \quad \text{--- (1)}$$
where $\alpha_0(t), \alpha_1(t), \dots, \alpha_{n-1}(t)$ are scalar functions of time.</p>

<p><strong>3. Step-by-Step Procedure:</strong></p>
<ol>
    <li><strong>Find Eigenvalues:</strong> Solve characteristic equation $\det(\lambda I - A) = 0$ to get $n$ eigenvalues $\lambda_1, \lambda_2, \dots, \lambda_n$.</li>
    <li><strong>Form Scalar Equation:</strong> The scalar function $e^{\lambda t}$ satisfies the same polynomial:
    $$e^{\lambda_i t} = \alpha_0(t) + \alpha_1(t)\lambda_i + \alpha_2(t)\lambda_i^2 + \dots + \alpha_{n-1}(t)\lambda_i^{n-1}$$</li>
    <li><strong>Case I (Distinct Eigenvalues):</strong> Substitute each distinct $\lambda_i$ into the scalar equation. This gives $n$ equations in $n$ unknowns ($\alpha_0, \dots, \alpha_{n-1}$). Solve this linear algebraic system.</li>
    <li><strong>Case II (Repeated Eigenvalues):</strong> If eigenvalue $\lambda_1$ is repeated with multiplicity $m$, differentiate with respect to $\lambda$:
    $$\frac{d^k}{d\lambda^k}\left[e^{\lambda t}\right]_{\lambda = \lambda_1} = \frac{d^k}{d\lambda^k}\left[\sum_{j=0}^{n-1} \alpha_j(t)\lambda^j\right]_{\lambda = \lambda_1}, \quad k = 1, 2, \dots, m-1$$</li>
    <li><strong>Substitute back into Matrix Formula:</strong> Put computed scalar functions $\alpha_k(t)$ into Equation (1) to get the final matrix $e^{At}$.</li>
</ol>
""",
        "understand_simply": r"""
<p>Calculating $e^{At}$ directly means multiplying matrices an infinite number of times—impossible! The Cayley-Hamilton theorem gives a massive shortcut: for a $2 \times 2$ matrix, $A^2$ can always be rewritten in terms of $A$ and $I$. So the infinite series collapses into just two terms: $\alpha_0 I + \alpha_1 A$. You only have to find two numbers $\alpha_0$ and $\alpha_1$ using simple high-school algebra on the eigenvalues!</p>
"""
    },

    'acs-q11': {
        "title": "Complete Solution of Non-Homogeneous State Equations",
        "marks": 7,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$\mathbf{x}(t) = e^{At}\mathbf{x}(0) + \int_0^t e^{A(t-\tau)}B\mathbf{u}(\tau)d\tau$$",
            "text": "Total Response = Zero-Input Response (ZIR) + Zero-State Response (ZSR via convolution integral)."
        },
        "exam_answer": r"""
<p><strong>1. Problem Statement:</strong><br>
Consider the complete continuous-time state equation with non-zero input $\mathbf{u}(t)$ and initial condition $\mathbf{x}(0)$:
$$\dot{\mathbf{x}}(t) = A\mathbf{x}(t) + B\mathbf{u}(t), \quad t \ge 0$$</p>

<p><strong>2. Derivation using Integrating Factor:</strong></p>
<ul>
    <li>Rearrange the state equation:
    $$\dot{\mathbf{x}}(t) - A\mathbf{x}(t) = B\mathbf{u}(t)$$</li>
    <li>Premultiply both sides by the integrating factor $e^{-At}$:
    $$e^{-At}\dot{\mathbf{x}}(t) - e^{-At}A\mathbf{x}(t) = e^{-At}B\mathbf{u}(t)$$</li>
    <li>Notice that the left-hand side is the exact derivative of a product:
    $$\frac{d}{dt}\left[ e^{-At}\mathbf{x}(t) \right] = e^{-At}B\mathbf{u}(t)$$</li>
    <li>Integrate both sides from $\tau = 0$ to $\tau = t$:
    $$\int_0^t \frac{d}{d\tau}\left[ e^{-A\tau}\mathbf{x}(\tau) \right] d\tau = \int_0^t e^{-A\tau}B\mathbf{u}(\tau) d\tau$$
    $$e^{-At}\mathbf{x}(t) - e^{-A(0)}\mathbf{x}(0) = \int_0^t e^{-A\tau}B\mathbf{u}(\tau) d\tau$$
    Since $e^0 = I$:
    $$e^{-At}\mathbf{x}(t) = \mathbf{x}(0) + \int_0^t e^{-A\tau}B\mathbf{u}(\tau) d\tau$$</li>
    <li>Premultiply all terms by $e^{At}$:
    $$\mathbf{x}(t) = e^{At}\mathbf{x}(0) + e^{At} \int_0^t e^{-A\tau}B\mathbf{u}(\tau) d\tau$$
    Moving $e^{At}$ inside the integral (since integration is with respect to $\tau$):
    $$\mathbf{x}(t) = e^{At}\mathbf{x}(0) + \int_0^t e^{A(t-\tau)}B\mathbf{u}(\tau) d\tau$$</li>
</ul>

<p><strong>3. Structure of the Complete Solution:</strong></p>
$$\mathbf{x}(t) = \underbrace{e^{At}\mathbf{x}(0)}_{\text{Zero-Input Response (ZIR)}} + \underbrace{\int_0^t e^{A(t-\tau)}B\mathbf{u}(\tau) d\tau}_{\text{Zero-State Response (ZSR)}}$$
<p><strong>Output Response:</strong>
$$\mathbf{y}(t) = C\mathbf{x}(t) + D\mathbf{u}(t) = C e^{At}\mathbf{x}(0) + C \int_0^t e^{A(t-\tau)}B\mathbf{u}(\tau) d\tau + D\mathbf{u}(t)$$</p>
""",
        "understand_simply": r"""
<p>When you drive a car, its total movement comes from two things: (1) where the car was already rolling due to its past momentum (Zero-Input Response), plus (2) how hard you are pressing the gas pedal right now (Zero-State Response). The convolution integral simply sums up the effect of every tap of your foot from time $0$ to time $t$.</p>
"""
    },

    # =========================================================================
    # MODULE 3: Controllability, Observability & Controller / Observer Design
    # =========================================================================
    'acs-q12': {
        "title": "Kalman's Duality Principle between Controllability and Observability",
        "marks": 3,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$\text{Controllability of } (A, B) \iff \text{Observability of } (A^T, C^T)$$",
            "text": "Controllability and observability are mathematical duals; transpose matrices to switch between them."
        },
        "exam_answer": r"""
<p><strong>1. Statement of Kalman's Duality Principle:</strong></p>
<ul>
    <li>Kalman's duality principle states that a system $S_1$ described by the pair $(A, B)$ is <strong>completely state controllable</strong> if and only if its dual system $S_2$ described by the pair $(A^T, B^T)$ is <strong>completely state observable</strong>.</li>
    <li>Conversely, a system $(A, C)$ is completely state observable if and only if its dual system $(A^T, C^T)$ is completely state controllable.</li>
</ul>

<p><strong>2. Mathematical Proof using Rank Conditions:</strong></p>
<ul>
    <li>The Controllability Matrix for $(A, B)$ is:
    $$Q_c = \begin{bmatrix} B & AB & A^2B & \dots & A^{n-1}B \end{bmatrix}$$</li>
    <li>The Observability Matrix for $(A, C)$ is:
    $$Q_0 = \begin{bmatrix} C \\ CA \\ CA^2 \\ \vdots \\ CA^{n-1} \end{bmatrix}$$</li>
    <li>Taking the transpose of $Q_0$:
    $$Q_0^T = \begin{bmatrix} C^T & A^T C^T & (A^T)^2 C^T & \dots & (A^T)^{n-1} C^T \end{bmatrix}$$</li>
    <li>Notice that $Q_0^T$ has the exact same mathematical form as the controllability matrix of the dual pair $(A^T, C^T)$. Since the rank of any matrix equals the rank of its transpose ($\operatorname{rank}(Q_0) = \operatorname{rank}(Q_0^T)$):
    $$\operatorname{rank}(Q_c) = n \iff \operatorname{rank}(Q_0) = n$$</li>
</ul>
<p><strong>Practical Engineering Use:</strong> Controller design algorithms (like pole placement feedback $K$) can be directly converted into state observer design algorithms (observer gain $L$) by replacing $A \to A^T$ and $B \to C^T$.</p>
""",
        "understand_simply": r"""
<p>Controllability means: "Can my steering wheel reach and move every part of the car?" Observability means: "Can my dashboard gauges see and measure every part of the car?" Kalman proved that mathematically, steering a system forward is the exact mirror-image (transpose) of watching a system backward!</p>
"""
    },

    'acs-q13': {
        "title": "Gilbert's Method for Testing Controllability and Observability",
        "marks": 3,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$\dot{\mathbf{z}} = \Lambda \mathbf{z} + \bar{B}\mathbf{u}, \quad \mathbf{y} = \bar{C}\mathbf{z}$$",
            "text": "In diagonalized form: Controllable if $\\bar{B}$ has no zero rows; Observable if $\\bar{C}$ has no zero columns."
        },
        "exam_answer": r"""
<p><strong>1. Gilbert's Method Principle:</strong><br>
Gilbert's method tests controllability and observability by converting the system into a diagonal canonical form using an eigenvector modal matrix $M$.</p>

<p><strong>2. Condition for Distinct Eigenvalues:</strong></p>
<ol>
    <li>Find the eigenvalues $\lambda_1, \lambda_2, \dots, \lambda_n$ of matrix $A$. Assume all eigenvalues are distinct.</li>
    <li>Construct the modal matrix $M = \begin{bmatrix} \mathbf{v}_1 & \mathbf{v}_2 & \dots & \mathbf{v}_n \end{bmatrix}$ whose columns are the eigenvectors of $A$.</li>
    <li>Transform the system into diagonal form $\mathbf{x} = M\mathbf{z}$:
    $$\Lambda = M^{-1}AM = \operatorname{diag}(\lambda_1, \lambda_2, \dots, \lambda_n)$$
    $$\bar{B} = M^{-1}B, \quad \bar{C} = CM$$</li>
    <li><strong>Controllability Test:</strong> The system is completely state controllable if and only if the transformed input matrix $\bar{B}$ has <strong>no row containing all zeros</strong>. (If row $i$ of $\bar{B}$ is zero, mode $\lambda_i$ cannot be affected by any input).</li>
    <li><strong>Observability Test:</strong> The system is completely state observable if and only if the transformed output matrix $\bar{C}$ has <strong>no column containing all zeros</strong>. (If column $j$ of $\bar{C}$ is zero, mode $\lambda_j$ has zero contribution to the output).</li>
</ol>
""",
        "understand_simply": r"""
<p>Imagine 3 independent electric motors. Gilbert's method simply asks two common-sense questions: (1) Does every motor have a power wire connected to the throttle ($\bar{B}$ has no empty rows)? If yes, you can control all of them. (2) Does every motor have a speed sensor reporting to the screen ($\bar{C}$ has no empty columns)? If yes, you can observe all of them.</p>
"""
    },

    'acs-q13b': {
        "title": "Popov-Belevitch-Hautus (PBH) Rank Tests for Controllability and Observability",
        "marks": 3,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$\operatorname{rank}[sI - A \quad B] = n, \quad \operatorname{rank}\begin{bmatrix} sI - A \\ C \end{bmatrix} = n \quad \forall s = \lambda_i$$",
            "text": "PBH test checks matrix rank only at the eigenvalues $\\lambda_i$ of matrix $A$."
        },
        "exam_answer": r"""
<p><strong>1. PBH Controllability Test:</strong></p>
<ul>
    <li>The continuous-time LTI system $(A, B)$ is completely state controllable if and only if:
    $$\operatorname{rank}\begin{bmatrix} sI - A & B \end{bmatrix} = n \quad \text{for all complex } s \in \mathbb{C}$$</li>
    <li>Since $(sI - A)$ has full rank $n$ for any $s$ that is not an eigenvalue, we only need to test this rank condition at the eigenvalues $\lambda_1, \dots, \lambda_n$ of matrix $A$:
    $$\operatorname{rank}\begin{bmatrix} \lambda_i I - A & B \end{bmatrix} = n, \quad \forall i = 1, 2, \dots, n$$</li>
</ul>

<p><strong>2. PBH Observability Test:</strong></p>
<ul>
    <li>The continuous-time LTI system $(A, C)$ is completely state observable if and only if:
    $$\operatorname{rank}\begin{bmatrix} sI - A \\ C \end{bmatrix} = n \quad \text{for all complex } s \in \mathbb{C}$$</li>
    <li>Equivalently, evaluated only at each eigenvalue $\lambda_i$:
    $$\operatorname{rank}\begin{bmatrix} \lambda_i I - A \\ C \end{bmatrix} = n, \quad \forall i = 1, 2, \dots, n$$</li>
</ul>
<p><strong>Major Advantage over Kalman Test:</strong> When an eigenvalue fails the rank condition, PBH identifies the exact uncontrollable or unobservable dynamic mode without computing matrix powers $A^2, A^3, \dots, A^{n-1}$.</p>
""",
        "understand_simply": r"""
<p>Kalman's test computes massive matrix multiplications ($A^2, A^3, \dots$) which can cause big numerical rounding errors. The PBH test is like a doctor testing specific pressure points: you plug in only the natural frequencies (eigenvalues $\lambda_i$) of the system and check if the matrix stays healthy (full rank).</p>
"""
    },

    'acs-q14': {
        "title": "State Feedback Controller Design by Pole Placement (Ackermann's Formula)",
        "marks": 7,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$K = \begin{bmatrix} 0 & 0 & \dots & 1 \end{bmatrix} Q_c^{-1} \alpha_c(A), \quad u(t) = -K\mathbf{x}(t) + r(t)$$",
            "text": "Pole placement shifts open-loop poles to desired locations; requires controllability matrix $Q_c$ to have full rank $n$."
        },
        "exam_answer": r"""
<p><strong>1. Control Objective:</strong><br>
Design a state feedback gain vector $K = \begin{bmatrix} k_1 & k_2 & \dots & k_n \end{bmatrix}$ such that the control law $u(t) = -K\mathbf{x}(t) + r(t)$ places the closed-loop system poles at arbitrarily chosen locations $\mu_1, \mu_2, \dots, \mu_n$.</p>

<p><strong>2. Prerequisite Condition:</strong><br>
The system must be completely state controllable:
$$\operatorname{rank}(Q_c) = \operatorname{rank}\begin{bmatrix} B & AB & A^2 B & \dots & A^{n-1}B \end{bmatrix} = n$$</p>

<p><strong>3. Step-by-Step Design Procedure using Ackermann's Formula:</strong></p>
<ol>
    <li><strong>Specify Desired Closed-Loop Poles:</strong> Choose desired locations $\mu_1, \mu_2, \dots, \mu_n$ based on transient specifications (settling time $t_s$, peak overshoot $M_p$).</li>
    <li><strong>Formulate Desired Characteristic Polynomial:</strong>
    $$\alpha_c(s) = (s - \mu_1)(s - \mu_2)\dots(s - \mu_n) = s^n + \alpha_{n-1}s^{n-1} + \dots + \alpha_1 s + \alpha_0$$</li>
    <li><strong>Evaluate Matrix Polynomial $\alpha_c(A)$:</strong>
    Substitute matrix $A$ into the desired polynomial:
    $$\alpha_c(A) = A^n + \alpha_{n-1}A^{n-1} + \dots + \alpha_1 A + \alpha_0 I$$</li>
    <li><strong>Calculate Controllability Matrix &amp; Inverse:</strong>
    $$Q_c = \begin{bmatrix} B & AB & A^2 B & \dots & A^{n-1}B \end{bmatrix}_{n \times n} \implies \text{Compute } Q_c^{-1}$$</li>
    <li><strong>Compute Feedback Gain Vector $K$ using Ackermann's Formula:</strong>
    $$K = \begin{bmatrix} 0 & 0 & \dots & 0 & 1 \end{bmatrix}_{1 \times n} Q_c^{-1} \alpha_c(A)$$</li>
    <li><strong>Closed-Loop Verification:</strong>
    The closed-loop state matrix is $A_{\text{cl}} = (A - BK)$. Verify that $\det(sI - (A - BK)) = \alpha_c(s)$.</li>
</ol>
""",
        "understand_simply": r"""
<p>Think of balancing an inverted broom on your palm. Without moving your hand, the broom falls over (unstable pole in right-half plane). But if you watch the broom's angle and angular speed ($\mathbf{x}$) and react by moving your hand ($u = -K\mathbf{x}$), you can keep it standing upright! Ackermann's formula gives you the exact sensitivity knob $K$ so the broom responds with the speed and smoothness you want.</p>
"""
    },

    'acs-q15': {
        "title": "Full-Order State Observer Design and Error Dynamics Derivation",
        "marks": 7,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$\dot{\hat{\mathbf{x}}} = A\hat{\mathbf{x}} + B\mathbf{u} + L(\mathbf{y} - C\hat{\mathbf{x}}), \quad \dot{\mathbf{e}} = (A - LC)\mathbf{e}$$",
            "text": "Observer reconstructs unmeasurable internal states; error $\\mathbf{e}(t) \\to \\mathbf{0}$ if $(A - LC)$ is designed to be asymptotically stable."
        },
        "exam_answer": r"""
<p><strong>1. Purpose of a State Observer:</strong></p>
<ul>
    <li>State feedback control requires knowing all state variables $\mathbf{x}(t)$. In practice, many states (like internal flux or winding temperature) cannot be measured directly due to cost or physical constraints.</li>
    <li>A <strong>full-order observer</strong> is a software algorithm running in parallel with the plant that estimates all $n$ state variables $\hat{\mathbf{x}}(t)$ using only measured inputs $\mathbf{u}(t)$ and outputs $\mathbf{y}(t)$.</li>
</ul>

<p><strong>2. Observer Mathematical Structure:</strong><br>
$$\dot{\hat{\mathbf{x}}}(t) = A\hat{\mathbf{x}}(t) + B\mathbf{u}(t) + L\left( \mathbf{y}(t) - \hat{\mathbf{y}}(t) \right)$$
$$\hat{\mathbf{y}}(t) = C\hat{\mathbf{x}}(t)$$
where $\hat{\mathbf{x}}(t)$ is the estimated state vector, and $L$ is the $n \times 1$ observer gain matrix.</p>

<p><strong>3. Derivation of Observer Error Dynamics:</strong></p>
<ul>
    <li>Define state estimation error as: $\mathbf{e}(t) = \mathbf{x}(t) - \hat{\mathbf{x}}(t)$.</li>
    <li>Differentiate with respect to time:
    $$\dot{\mathbf{e}}(t) = \dot{\mathbf{x}}(t) - \dot{\hat{\mathbf{x}}}(t)$$</li>
    <li>Substitute plant equations and observer equations:
    $$\dot{\mathbf{e}}(t) = [A\mathbf{x} + B\mathbf{u}] - [A\hat{\mathbf{x}} + B\mathbf{u} + L(\mathbf{y} - C\hat{\mathbf{x}})]$$
    $$\dot{\mathbf{e}}(t) = A(\mathbf{x} - \hat{\mathbf{x}}) - L(C\mathbf{x} - C\hat{\mathbf{x}}) = A\mathbf{e} - LC\mathbf{e}$$
    $$\dot{\mathbf{e}}(t) = (A - LC)\mathbf{e}(t)$$</li>
</ul>
<p><strong>4. Design Condition &amp; Ackermann's Observer Formula:</strong></p>
<ul>
    <li>For the estimation error to decay rapidly to zero ($\mathbf{e}(t) \to \mathbf{0}$ as $t \to \infty$), the observer matrix $(A - LC)$ must be asymptotically stable.</li>
    <li>The system must be completely state observable ($\operatorname{rank}(Q_0) = n$).</li>
    <li>Using duality, the observer gain $L$ is calculated using Ackermann's formula:
    $$L = \alpha_0(A) Q_0^{-1} \begin{bmatrix} 0 \\ 0 \\ \vdots \\ 1 \end{bmatrix}_{n \times 1}$$
    <em>Rule of thumb:</em> Observer poles are designed to be 3 to 5 times faster than controller poles so that state estimates converge before control action takes effect.</li>
</ul>
""",
        "understand_simply": r"""
<p>An observer is like a co-pilot running a flight simulator inside the computer. The simulator copies the plane's flight physics. Every millisecond, the simulator checks its simulated altitude against the real altitude sensor. If there is an error, it uses gain $L$ to nudge the simulated numbers until the simulation matches reality perfectly!</p>
"""
    },

    # =========================================================================
    # MODULE 4: Non-Linear Systems & Describing Function Analysis
    # =========================================================================
    'acs-q16': {
        "title": "Characteristics and Physical Phenomena of Non-Linear Control Systems",
        "marks": 3,
        "remember_this": {
            "title": "Remember This",
            "eq": None,
            "text": "Superposition fails; exhibits limit cycles, jump resonance, subharmonic oscillations, and frequency-dependent stability."
        },
        "exam_answer": r"""
<p>Non-linear systems do not satisfy the principle of superposition and exhibit unique physical phenomena that never occur in linear systems:</p>
<ol>
    <li><strong>Failure of Superposition Principle:</strong> Homogeneity and additivity fail ($f(x_1 + x_2) \ne f(x_1) + f(x_2)$). System response depends strongly on the amplitude of input excitation, not just its frequency.</li>
    <li><strong>Limit Cycles:</strong> Stable or unstable self-sustained periodic oscillations of fixed amplitude and frequency that occur without any external periodic input (e.g., relay chattering in thermostats).</li>
    <li><strong>Jump Resonance:</strong> Discontinuous jump in output amplitude and phase when excitation frequency is smoothly swept across a critical resonant band (commonly seen in saturating iron-core inductors).</li>
    <li><strong>Subharmonic Oscillations:</strong> The system produces output frequencies that are integer fractions of the input frequency ($\frac{\omega}{2}, \frac{\omega}{3}$).</li>
    <li><strong>Multiple Equilibrium States:</strong> While linear systems have a single isolated equilibrium point at the origin, non-linear systems can have multiple stable and unstable equilibrium points.</li>
</ol>
""",
        "understand_simply": r"""
<p>If you push a swing gently, it moves a little; if you push twice as hard, a linear system says it goes twice as high. But in reality, if you push too hard, the chains go slack or the swing flips over the top bar! That's non-linearity: doubling the input does not double the result, and strange things like sudden jumps or permanent rattling (limit cycles) appear.</p>
"""
    },

    'acs-q16b': {
        "title": "Describing Function of Ideal Relay and Relay with Dead-Zone",
        "marks": 3,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$N(X)_{\text{ideal}} = \frac{4M}{\pi X}, \quad N(X)_{\text{deadzone}} = \frac{4M}{\pi X}\sqrt{1 - \left(\frac{D}{X}\right)^2}$$",
            "text": "Describing function $N(X) = Y_1 / X$; represents equivalent fundamental harmonic gain of non-linearity."
        },
        "exam_answer": r"""
<p><strong>1. Concept of Describing Function:</strong><br>
The describing function $N(X)$ approximates a non-linear element by the ratio of the fundamental harmonic component of its output $y_1(t)$ to a sinusoidal input $x(t) = X \sin\omega t$:
$$N(X) = \frac{Y_1 \angle \phi_1}{X} = \frac{A_1 + j B_1}{X}$$</p>

<p><strong>2. Ideal Relay (On-Off Element):</strong></p>
<ul>
    <li>Output jumps between $+M$ and $-M$. The output waveform is a symmetrical square wave of amplitude $M$.</li>
    <li>Fourier analysis yields fundamental peak $Y_1 = \frac{4M}{\pi}$ with zero phase shift ($\phi_1 = 0$):
    $$N(X) = \frac{4M}{\pi X}$$</li>
    <li>Gain drops inversely with input amplitude $X$.</li>
</ul>

<p><strong>3. Relay with Dead-Zone:</strong></p>
<ul>
    <li>For input $|x(t)| \le D$, output is zero. For $|x(t)| > D$, output is $+M$ or $-M$.</li>
    <li>Switching angle: $\theta = \sin^{-1}\left(\frac{D}{X}\right)$ (requires $X > D$ for any output).</li>
    <li>Describing Function:
    $$N(X) = \frac{4M}{\pi X} \cos\theta = \frac{4M}{\pi X} \sqrt{1 - \left(\frac{D}{X}\right)^2} \quad \text{for } X \ge D$$
    $$N(X) = 0 \quad \text{for } X < D$$</li>
</ul>
""",
        "understand_simply": r"""
<p>An ideal relay is like a light switch: you flip it slightly, and BAM, it clicks fully ON. A relay with a dead-zone is like a loose light switch: you have to push it past a loose wiggle zone ($D$) before it finally clicks ON. The describing function calculates the "effective gain" of this switch when excited by a sine wave.</p>
"""
    },

    'acs-q17': {
        "title": "Derivation of the Describing Function for Symmetrical Saturation",
        "marks": 7,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$N(X) = \frac{2k}{\pi} \left[ \sin^{-1}\left(\frac{S}{X}\right) + \frac{S}{X}\sqrt{1 - \left(\frac{S}{X}\right)^2} \right] \quad (X > S)$$",
            "text": r"For $X \le S$, element is linear with $N(X) = k$; for $X > S$, equivalent gain decreases monotonically as $1/X$."
        },
        "exam_answer": r"""
<p><strong>1. Non-Linear Characteristic:</strong><br>
Consider a symmetrical saturation non-linearity with linear slope $k$ and saturation limit $S$:</p>
$$y(t) = \begin{cases} k x(t), & -S \le x(t) \le S \\ k S, & x(t) > S \\ -k S, & x(t) < -S \end{cases}$$

<p><strong>2. Applied Sinusoidal Excitation:</strong><br>
Let input be $x(t) = X \sin\theta$, where $\theta = \omega t$.<br>
If $X \le S$, the system operates purely in the linear region, so $N(X) = k$.<br>
If $X > S$, the output saturates when $X \sin\theta_1 = S \implies \theta_1 = \sin^{-1}\left(\frac{S}{X}\right)$.</p>

<p><strong>3. Fourier Fundamental Component Derivation:</strong><br>
Due to odd quarter-wave symmetry ($y(\theta) = -y(-\theta)$ and $y(\pi - \theta) = y(\theta)$):
$$A_1 = 0 \quad \text{(zero phase shift)}$$
$$B_1 = \frac{4}{\pi} \int_0^{\pi/2} y(\theta) \sin\theta \, d\theta$$
Split the integration interval into the linear zone ($0 \to \theta_1$) and the saturation zone ($\theta_1 \to \pi/2$):
$$B_1 = \frac{4}{\pi} \left[ \int_0^{\theta_1} (k X \sin\theta) \sin\theta \, d\theta + \int_{\theta_1}^{\pi/2} (k S) \sin\theta \, d\theta \right]$$

<p><strong>Step 1: Evaluate First Integral (Linear Zone):</strong><br>
$$\int_0^{\theta_1} \sin^2\theta \, d\theta = \left[ \frac{\theta}{2} - \frac{\sin 2\theta}{4} \right]_0^{\theta_1} = \frac{\theta_1}{2} - \frac{\sin\theta_1 \cos\theta_1}{2}$$</p>

<p><strong>Step 2: Evaluate Second Integral (Saturation Zone):</strong><br>
$$\int_{\theta_1}^{\pi/2} \sin\theta \, d\theta = [-\cos\theta]_{\theta_1}^{\pi/2} = \cos\theta_1$$</p>

<p><strong>Step 3: Combine and Substitute $S = X \sin\theta_1$:</strong><br>
$$B_1 = \frac{4k X}{\pi} \left[ \frac{\theta_1}{2} - \frac{\sin\theta_1 \cos\theta_1}{2} \right] + \frac{4k (X \sin\theta_1)}{\pi} \cos\theta_1$$
$$B_1 = \frac{2k X}{\pi} \theta_1 - \frac{2k X}{\pi} \sin\theta_1 \cos\theta_1 + \frac{4k X}{\pi} \sin\theta_1 \cos\theta_1$$
$$B_1 = \frac{2k X}{\pi} \left[ \theta_1 + \sin\theta_1 \cos\theta_1 \right]$$

<p><strong>4. Final Describing Function:</strong><br>
Since $\sin\theta_1 = \frac{S}{X}$ and $\cos\theta_1 = \sqrt{1 - (S/X)^2}$:
$$N(X) = \frac{B_1}{X} = \frac{2k}{\pi} \left[ \sin^{-1}\left(\frac{S}{X}\right) + \frac{S}{X}\sqrt{1 - \left(\frac{S}{X}\right)^2} \right] \quad \text{for } X > S$$
$$N(X) = k \quad \text{for } X \le S$$</p>
""",
        "understand_simply": r"""
<p>Think of an audio amplifier. If you speak softly, your voice comes out louder without distortion ($N(X) = k$). But if you shout into the microphone, the speaker clips the sound peaks flat (saturation). The describing function mathematically calculates how much the "effective amplification gain" drops as you push the speaker further into distortion.</p>
"""
    },

    'acs-q17b': {
        "title": "Derivation of the Describing Function for Dead-Zone Non-Linearity",
        "marks": 7,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$N(X) = k - \frac{2k}{\pi} \left[ \sin^{-1}\left(\frac{D}{X}\right) + \frac{D}{X}\sqrt{1 - \left(\frac{D}{X}\right)^2} \right] \quad (X > D)$$",
            "text": "Dead-zone describing function is complementary to saturation: $N(X)_{\\text{deadzone}} = k - N(X)_{\\text{saturation}}$."
        },
        "exam_answer": r"""
<p><strong>1. Dead-Zone Characteristic:</strong><br>
A dead-zone non-linearity with threshold $D$ and linear slope $k$ is defined by:
$$y(t) = \begin{cases} 0, & -D \le x(t) \le D \\ k(x - D), & x(t) > D \\ k(x + D), & x(t) < -D \end{cases}$$</p>

<p><strong>2. Input Excitation:</strong><br>
Apply sinusoidal input $x(t) = X \sin\theta$, where $\theta = \omega t$.<br>
If $X \le D$, the output is identically zero, so $N(X) = 0$.<br>
If $X > D$, output conducts when input exceeds $D$: $\theta_1 = \sin^{-1}\left(\frac{D}{X}\right)$.</p>

<p><strong>3. Fourier Fundamental Coefficient Derivation:</strong><br>
By symmetry, $A_1 = 0$ (no phase shift). The fundamental sine coefficient is:
$$B_1 = \frac{4}{\pi} \int_{\theta_1}^{\pi/2} k (X \sin\theta - D) \sin\theta \, d\theta$$
$$B_1 = \frac{4k X}{\pi} \int_{\theta_1}^{\pi/2} \sin^2\theta \, d\theta - \frac{4k D}{\pi} \int_{\theta_1}^{\pi/2} \sin\theta \, d\theta$$
Using standard integrals:
$$\int_{\theta_1}^{\pi/2} \sin^2\theta \, d\theta = \left[ \frac{\theta}{2} - \frac{\sin 2\theta}{4} \right]_{\theta_1}^{\pi/2} = \left(\frac{\pi}{4}\right) - \left(\frac{\theta_1}{2} - \frac{\sin\theta_1 \cos\theta_1}{2}\right)$$
$$\int_{\theta_1}^{\pi/2} \sin\theta \, d\theta = [-\cos\theta]_{\theta_1}^{\pi/2} = \cos\theta_1$$

<p>Substitute $D = X \sin\theta_1$:
$$B_1 = \frac{4k X}{\pi} \left[ \frac{\pi}{4} - \frac{\theta_1}{2} + \frac{\sin\theta_1 \cos\theta_1}{2} \right] - \frac{4k X \sin\theta_1 \cos\theta_1}{\pi}$$
$$B_1 = k X - \frac{2k X}{\pi} \left[ \theta_1 + \sin\theta_1 \cos\theta_1 \right]$$

<p><strong>4. Final Describing Function:</strong><br>
$$N(X) = \frac{B_1}{X} = k \left( 1 - \frac{2}{\pi} \left[ \sin^{-1}\left(\frac{D}{X}\right) + \frac{D}{X}\sqrt{1 - \left(\frac{D}{X}\right)^2} \right] \right) \quad \text{for } X > D$$
$$N(X) = 0 \quad \text{for } X \le D$$</p>
""",
        "understand_simply": r"""
<p>Think of an old car steering wheel with play in the middle. If you wiggle the wheel slightly within $\pm D$, the wheels don't turn at all ($N(X) = 0$). Only when you turn past the dead-zone do the front tires start responding. As you make larger and larger turns ($X \gg D$), the loose wiggle becomes negligible, and the steering behaves almost like a normal linear wheel ($N(X) \to k$).</p>
"""
    },

    'acs-q18': {
        "title": "Limit Cycle Determination and Stability Analysis via Describing Functions",
        "marks": 7,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$G(j\omega) = -\frac{1}{N(X)}$$",
            "text": "Intersection of linear Nyquist plot $G(j\\omega)$ and non-linear curve $-1/N(X)$ determines limit cycle amplitude $X$ and frequency $\\omega$."
        },
        "exam_answer": r"""
<p><strong>1. Limit Cycle Condition:</strong><br>
Consider a closed-loop system with linear plant $G(s)$ in feedback with a non-linear element $N(X)$.<br>
The characteristic equation of the harmonic balance is:
$$1 + N(X) G(j\omega) = 0 \implies G(j\omega) = -\frac{1}{N(X)}$$</p>

<p><strong>2. Graphical Determination:</strong></p>
<ul>
    <li>Plot the Nyquist polar plot of the linear plant $G(j\omega)$ for $\omega: 0 \to \infty$.</li>
    <li>Plot the critical locus $-\frac{1}{N(X)}$ on the same complex plane as amplitude $X$ varies from $0 \to \infty$.</li>
    <li><strong>Limit Cycle Existence:</strong> If the two curves intersect at a point $P$, a limit cycle exists!
        <ul>
            <li>The frequency of the limit cycle $\omega_0$ is read from the $G(j\omega)$ curve at intersection $P$.</li>
            <li>The amplitude of the limit cycle $X_0$ is read from the $-\frac{1}{N(X)}$ curve at intersection $P$.</li>
        </ul>
    </li>
</ul>

<p><strong>3. Stability Criterion for Limit Cycles:</strong></p>
<ul>
    <li>According to the extended Nyquist stability criterion, a point is stable if it is not encircled by the $G(j\omega)$ plot.</li>
    <li><strong>Stable Limit Cycle Criterion:</strong> As amplitude $X$ increases along the $-\frac{1}{N(X)}$ curve through intersection point $P$, if the curve moves from the <em>encircled region</em> (unstable zone) to the <em>unencircled region</em> (stable zone), the limit cycle is <strong>stable</strong>.
    <ul>
        <li><em>Physical Explanation:</em> If a disturbance increases $X > X_0$, the system enters the stable region, causing oscillations to decay back to $X_0$. If $X < X_0$, it enters the unstable region, causing oscillations to grow back to $X_0$.</li>
    </ul>
    </li>
    <li><strong>Unstable Limit Cycle:</strong> If increasing $X$ moves from the unencircled region into the encircled region, any disturbance causes the oscillation either to blow up or collapse to zero.</li>
</ul>
""",
        "understand_simply": r"""
<p>A limit cycle is like your home refrigerator clicking on and off at regular intervals. It settles into a permanent rhythmic heartbeat. Describing function analysis finds the exact meeting point between the cooling coils ($G(j\omega)$) and the thermostat switch ($-1/N(X)$), telling you exactly how loud ($X$) and how fast ($\omega$) the refrigerator will cycle.</p>
"""
    },

    # =========================================================================
    # MODULE 5: Phase Plane Analysis & Lyapunov Stability
    # =========================================================================
    'acs-q19': {
        "title": "Phase Plane Concepts, Trajectories, and Singular Points Classification",
        "marks": 3,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$\frac{dx_2}{dx_1} = \frac{f_2(x_1, x_2)}{f_1(x_1, x_2)}$$",
            "text": "Singular points occur where slope is $0/0$ ($f_1 = f_2 = 0$). Types: Node, Saddle, Focus, Center."
        },
        "exam_answer": r"""
<p><strong>1. Phase Plane &amp; Phase Trajectories:</strong></p>
<ul>
    <li>The <strong>phase plane</strong> is a 2D state space where coordinates are the state variables $x_1$ (displacement) and $x_2 = \dot{x}_1$ (velocity).</li>
    <li>A curve traced by $(x_1(t), x_2(t))$ from an initial state is called a <strong>phase trajectory</strong>. A collection of trajectories is a <strong>phase portrait</strong>.</li>
    <li>Slope of trajectory at any point: $\frac{dx_2}{dx_1} = \frac{\dot{x}_2}{\dot{x}_1} = \frac{f_2(x_1, x_2)}{f_1(x_1, x_2)}$.</li>
</ul>

<p><strong>2. Singular Points (Equilibrium Points):</strong></p>
<ul>
    <li>Points where both state velocities are zero: $f_1(x_1, x_2) = 0$ and $f_2(x_1, x_2) = 0$. The slope $\frac{dx_2}{dx_1} = \frac{0}{0}$ is indeterminate.</li>
</ul>

<table class="exam-table">
    <thead>
        <tr>
            <th>Singular Point</th>
            <th>Eigenvalues of Linearized Matrix $A$</th>
            <th>Stability Nature</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Stable Node</strong></td>
            <td>Real, unequal, both negative ($\lambda_2 < \lambda_1 < 0$).</td>
            <td>Asymptotically stable; trajectories enter point without oscillation.</td>
        </tr>
        <tr>
            <td><strong>Unstable Node</strong></td>
            <td>Real, unequal, both positive ($\lambda_1 > \lambda_2 > 0$).</td>
            <td>Unstable; trajectories diverge outward to infinity.</td>
        </tr>
        <tr>
            <td><strong>Saddle Point</strong></td>
            <td>Real, opposite signs ($\lambda_1 > 0, \lambda_2 < 0$).</td>
            <td>Always unstable; trajectories approach along one axis and shoot away.</td>
        </tr>
        <tr>
            <td><strong>Stable Focus</strong></td>
            <td>Complex conjugate with negative real part ($\sigma \pm j\omega, \sigma < 0$).</td>
            <td>Stable; trajectories spiral inward toward the origin.</td>
        </tr>
        <tr>
            <td><strong>Center (Vortex)</strong></td>
            <td>Purely imaginary ($\pm j\omega, \sigma = 0$).</td>
            <td>Marginally stable; trajectories form closed concentric ellipses (undamped oscillation).</td>
        </tr>
    </tbody>
</table>
""",
        "understand_simply": r"""
<p>Imagine dropping a marble on different terrains: on a bowl, it rolls to the bottom and stops (Stable Node). In a swirling drain, it spirals inward to the center (Stable Focus). On a mountain peak, it rolls off and accelerates away (Unstable Node). On a horse saddle, it rolls towards the middle from the sides, but immediately slips off the front or back (Saddle Point)!</p>
"""
    },

    'acs-q20': {
        "title": "Sign Definiteness of Scalar Functions and Sylvester's Criterion",
        "marks": 3,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$V(\mathbf{x}) = \mathbf{x}^T P \mathbf{x} > 0 \iff \Delta_1 > 0, \Delta_2 > 0, \dots, \Delta_n > 0$$",
            "text": "Sylvester's test: Matrix $P$ is positive definite if all leading principal minors are strictly positive."
        },
        "exam_answer": r"""
<p><strong>1. Sign Definiteness of Scalar Function $V(\mathbf{x})$:</strong></p>
<ul>
    <li><strong>Positive Definite:</strong> $V(\mathbf{0}) = 0$, and $V(\mathbf{x}) > 0$ for all $\mathbf{x} \ne \mathbf{0}$. (Represents stored energy).</li>
    <li><strong>Positive Semi-Definite:</strong> $V(\mathbf{0}) = 0$, and $V(\mathbf{x}) \ge 0$ for all $\mathbf{x}$. It can equal zero at points other than the origin.</li>
    <li><strong>Negative Definite:</strong> $-V(\mathbf{x})$ is positive definite ($V(\mathbf{x}) < 0$ for all $\mathbf{x} \ne \mathbf{0}$).</li>
    <li><strong>Indefinite:</strong> $V(\mathbf{x})$ takes both positive and negative values depending on direction of $\mathbf{x}$.</li>
</ul>

<p><strong>2. Sylvester's Criterion for Quadratic Forms:</strong><br>
Let $V(\mathbf{x}) = \mathbf{x}^T P \mathbf{x}$, where $P$ is a real symmetric $n \times n$ matrix:
$$P = \begin{bmatrix} p_{11} & p_{12} & \dots & p_{1n} \\ p_{21} & p_{22} & \dots & p_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ p_{n1} & p_{n2} & \dots & p_{nn} \end{bmatrix}$$
$V(\mathbf{x})$ is <strong>positive definite</strong> if and only if all $n$ leading principal minors $\Delta_k$ of $P$ are strictly positive:
$$\Delta_1 = p_{11} > 0$$
$$\Delta_2 = \begin{vmatrix} p_{11} & p_{12} \\ p_{21} & p_{22} \end{vmatrix} > 0$$
$$\Delta_3 = \begin{vmatrix} p_{11} & p_{12} & p_{13} \\ p_{21} & p_{22} & p_{23} \\ p_{31} & p_{32} & p_{33} \end{vmatrix} > 0, \quad \dots \quad \Delta_n = \det(P) > 0$$
<strong>Negative Definite Condition:</strong> Minors alternate in sign: $\Delta_1 < 0, \Delta_2 > 0, \Delta_3 < 0, \dots$</p>
""",
        "understand_simply": r"""
<p>Think of $V(\mathbf{x})$ as a physical bowl. If it is positive definite, the bowl curves upward in every direction—the only lowest point is the exact bottom at the origin ($0, 0$). If you drop a ball anywhere inside, it has positive potential energy and will slide toward the center.</p>
"""
    },

    'acs-q20b': {
        "title": "Generation of Lyapunov Functions: Krasovskii's and Variable Gradient Methods",
        "marks": 3,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$V(\mathbf{x}) = \mathbf{f}(\mathbf{x})^T P \mathbf{f}(\mathbf{x}) \quad \text{[Krasovskii]}, \quad \nabla V = \mathbf{g}(\mathbf{x}) \implies \frac{\partial g_i}{\partial x_j} = \frac{\partial g_j}{\partial x_i} \quad \text{[Var. Gradient]}$$",
            "text": "Systematic methods to construct energy-like scalar functions $V(\\mathbf{x})$ for non-linear stability proofs."
        },
        "exam_answer": r"""
<p>Constructing a valid Lyapunov function $V(\mathbf{x})$ for non-linear systems $\dot{\mathbf{x}} = \mathbf{f}(\mathbf{x})$ is challenging. Two systematic methods exist:</p>

<p><strong>1. Krasovskii's Method:</strong></p>
<ul>
    <li>Proposes a candidate Lyapunov function based on the system vector field $\mathbf{f}(\mathbf{x})$:
    $$V(\mathbf{x}) = \mathbf{f}(\mathbf{x})^T P \mathbf{f}(\mathbf{x})$$
    where $P$ is a symmetric positive definite matrix (often chosen as $P = I$).</li>
    <li>Define the Jacobian matrix $J(\mathbf{x}) = \frac{\partial \mathbf{f}}{\partial \mathbf{x}}$. The derivative is:
    $$\dot{V}(\mathbf{x}) = \mathbf{f}^T \left( J^T P + P J \right) \mathbf{f} = \mathbf{f}^T F(\mathbf{x}) \mathbf{f}$$</li>
    <li><strong>Theorem:</strong> If matrix $F(\mathbf{x}) = J^T P + P J$ is negative definite in a neighborhood around origin, the equilibrium point is asymptotically stable.</li>
</ul>

<p><strong>2. Variable Gradient Method (Schultz-Gibson Method):</strong></p>
<ul>
    <li>Assumes the gradient vector $\nabla V = \mathbf{g}(\mathbf{x}) = \begin{bmatrix} g_1 & g_2 & \dots & g_n \end{bmatrix}^T$.</li>
    <li>Enforces curl-free integrability conditions:
    $$\frac{\partial g_i}{\partial x_j} = \frac{\partial g_j}{\partial x_i} \quad \forall i, j$$</li>
    <li>Computes $\dot{V} = \mathbf{g}(\mathbf{x})^T \dot{\mathbf{x}} = \sum g_i f_i$ and selects coefficients to make $\dot{V}$ negative semi-definite or negative definite.</li>
    <li>Integrates $\mathbf{g}(\mathbf{x})$ along a spatial path to reconstruct the scalar Lyapunov function $V(\mathbf{x}) = \int_0^{\mathbf{x}} \mathbf{g}^T d\mathbf{x}$.</li>
</ul>
""",
        "understand_simply": r"""
<p>Finding a Lyapunov function by guessing is like looking for a lost key in the dark. Krasovskii's method builds a key automatically from the system's own equations. The Variable Gradient method works backwards: it draws the slope (gradient) of the energy bowl first to ensure the ball always rolls downward, then reconstructs the bowl by integration.</p>
"""
    },

    'acs-q21': {
        "title": "Singular Points Analysis and Phase Portrait Construction of Non-Linear Systems",
        "marks": 7,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$J = \begin{bmatrix} \partial f_1/\partial x_1 & \partial f_1/\partial x_2 \\ \partial f_2/\partial x_1 & \partial f_2/\partial x_2 \end{bmatrix}_{\mathbf{x}_0}$$",
            "text": "Linearize non-linear system at each equilibrium point $\\mathbf{x}_0$ using Jacobian matrix $J$; classify singular points from eigenvalues of $J$."
        },
        "exam_answer": r"""
<p><strong>1. Non-Linear Autonomous System:</strong><br>
Consider a second-order non-linear system:
$$\dot{x}_1 = f_1(x_1, x_2), \quad \dot{x}_2 = f_2(x_1, x_2)$$</p>

<p><strong>2. Step-by-Step Construction Procedure:</strong></p>
<ol>
    <li><strong>Step 1: Determine Equilibrium (Singular) Points:</strong><br>
    Set $\dot{x}_1 = 0$ and $\dot{x}_2 = 0$:
    $$f_1(x_1, x_2) = 0 \quad \text{and} \quad f_2(x_1, x_2) = 0$$
    Solve these simultaneous algebraic equations to find singular points $(x_{1e}, x_{2e})$.</li>
    <li><strong>Step 2: Linearize around each Singular Point:</strong><br>
    Evaluate the Jacobian matrix at each singular point:
    $$J = \begin{bmatrix} \frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} \\ \frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} \end{bmatrix}_{(x_{1e}, x_{2e})}$$
    The linearized local dynamics are: $\dot{\mathbf{\Delta x}} = J \mathbf{\Delta x}$.</li>
    <li><strong>Step 3: Calculate Eigenvalues &amp; Classify Singular Points:</strong><br>
    Solve characteristic equation $\det(\lambda I - J) = 0 \implies \lambda^2 - \operatorname{Tr}(J)\lambda + \det(J) = 0$:
    <ul>
        <li>$\det(J) < 0 \implies$ <strong>Saddle Point</strong> (always unstable).</li>
        <li>$\det(J) > 0, \operatorname{Tr}(J) < 0, (\operatorname{Tr})^2 - 4\det \ge 0 \implies$ <strong>Stable Node</strong>.</li>
        <li>$\det(J) > 0, \operatorname{Tr}(J) > 0, (\operatorname{Tr})^2 - 4\det \ge 0 \implies$ <strong>Unstable Node</strong>.</li>
        <li>$\det(J) > 0, \operatorname{Tr}(J) < 0, (\operatorname{Tr})^2 - 4\det < 0 \implies$ <strong>Stable Focus</strong> (inward spiral).</li>
        <li>$\det(J) > 0, \operatorname{Tr}(J) = 0 \implies$ <strong>Center / Vortex</strong> (closed periodic orbit).</li>
    </ul></li>
    <li><strong>Step 4: Sketch Trajectories (Isocline Method):</strong><br>
    Find curves of constant slope $m = \frac{dx_2}{dx_1} = \frac{f_2(x_1, x_2)}{f_1(x_1, x_2)}$. Draw slope direction markers along each isocline.</li>
    <li><strong>Step 5: Connect Trajectories:</strong><br>
    Connect directional markers smoothly, respecting arrow directions corresponding to time progression ($\dot{x}_1 > 0 \implies$ move right; $\dot{x}_1 < 0 \implies$ move left).</li>
</ol>
""",
        "understand_simply": r"""
<p>Mapping a non-linear phase portrait is like drawing a weather wind map over Kerala. First, you locate the calm eye of the storms (singular points where wind speed is zero). Next, you check if wind spirals into the center (cyclone/focus) or blows away. Then you draw the wind arrows across the map to see the overall flow of weather!</p>
"""
    },

    'acs-q22': {
        "title": "Lyapunov's Direct Method and Solution of Matrix Equation A^T P + P A = -Q",
        "marks": 7,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$A^T P + P A = -Q, \quad V(\mathbf{x}) = \mathbf{x}^T P \mathbf{x} > 0 \implies \dot{V}(\mathbf{x}) = -\mathbf{x}^T Q \mathbf{x} < 0$$",
            "text": "For linear systems $\\dot{\\mathbf{x}} = A\\mathbf{x}$: Asymptotically stable if unique positive definite $P$ exists for any positive definite $Q$ (e.g. $Q = I$)."
        },
        "exam_answer": r"""
<p><strong>1. Lyapunov's Direct (Second) Method Theorems:</strong><br>
Consider an autonomous system $\dot{\mathbf{x}} = \mathbf{f}(\mathbf{x})$ with equilibrium at the origin $\mathbf{f}(\mathbf{0}) = \mathbf{0}$. Let $V(\mathbf{x})$ be a continuously differentiable scalar function:</p>
<ul>
    <li><strong>Theorem 1 (Stability):</strong> If $V(\mathbf{x})$ is positive definite ($V(\mathbf{0})=0, V(\mathbf{x})>0$ for $\mathbf{x}\ne\mathbf{0}$) and its time derivative is negative semi-definite ($\dot{V}(\mathbf{x}) \le 0$), the origin is <strong>stable in the sense of Lyapunov</strong>.</li>
    <li><strong>Theorem 2 (Asymptotic Stability):</strong> If $V(\mathbf{x})$ is positive definite and its time derivative is strictly negative definite ($\dot{V}(\mathbf{x}) < 0$ for all $\mathbf{x} \ne \mathbf{0}$), the origin is <strong>asymptotically stable</strong>.</li>
    <li><strong>Theorem 3 (Instability):</strong> If $V(\mathbf{x})$ is positive definite and $\dot{V}(\mathbf{x})$ is strictly positive definite, the origin is <strong>unstable</strong>.</li>
</ul>

<p><strong>2. Application to Linear Systems ($\dot{\mathbf{x}} = A\mathbf{x}$):</strong></p>
<p>Choose a quadratic candidate Lyapunov function:
$$V(\mathbf{x}) = \mathbf{x}^T P \mathbf{x}$$
where $P$ is an $n \times n$ real symmetric positive definite matrix ($P = P^T, P > 0$).</p>

<p><strong>3. Derivation of the Lyapunov Matrix Equation:</strong><br>
Take the time derivative of $V(\mathbf{x})$ along system trajectories:
$$\dot{V}(\mathbf{x}) = \dot{\mathbf{x}}^T P \mathbf{x} + \mathbf{x}^T P \dot{\mathbf{x}}$$
Substitute $\dot{\mathbf{x}} = A\mathbf{x}$ and $\dot{\mathbf{x}}^T = \mathbf{x}^T A^T$:
$$\dot{V}(\mathbf{x}) = (A\mathbf{x})^T P \mathbf{x} + \mathbf{x}^T P (A\mathbf{x}) = \mathbf{x}^T A^T P \mathbf{x} + \mathbf{x}^T P A \mathbf{x}$$
$$\dot{V}(\mathbf{x}) = \mathbf{x}^T \left( A^T P + P A \right) \mathbf{x}$$
For asymptotic stability, we require $\dot{V}(\mathbf{x})$ to be negative definite:
$$\dot{V}(\mathbf{x}) = -\mathbf{x}^T Q \mathbf{x} < 0$$
where $Q$ is any chosen positive definite symmetric matrix (commonly $Q = I$).</p>
<p>Equating terms yields the famous <strong>Lyapunov Matrix Equation</strong>:
$$A^T P + P A = -Q$$</p>

<p><strong>4. Verification Procedure:</strong></p>
<ol>
    <li>Choose an arbitrary positive definite matrix $Q$ (usually the identity matrix $Q = I$).</li>
    <li>Solve the linear matrix equation $A^T P + P A = -Q$ for symmetric matrix $P$.</li>
    <li>Test matrix $P$ using Sylvester's criterion: if all leading principal minors of $P$ are strictly positive ($P > 0$), the linear system is <strong>asymptotically stable</strong>.</li>
</ol>
""",
        "understand_simply": r"""
<p>Lyapunov's direct method is the universal "energy test" for stability. If a mechanical system has positive stored energy ($V > 0$), and friction constantly drains that energy away ($\dot{V} < 0$), the system <em>must</em> eventually stop moving and settle down at rest. The beauty of this method is that you prove stability without ever solving the differential equations!</p>
"""
    }
}
