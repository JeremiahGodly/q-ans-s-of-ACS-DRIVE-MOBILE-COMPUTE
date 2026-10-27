# scratch/byheart_data.py
# High mark-weightage equations and core memorization sentences for all 94 exam questions.
# Heading: Sentence / (Equation) to Byhart

BYHEART_DATA = {
    'acs-q1': {
        "eq": r'$$\dot{\mathbf{x}}(t) = A \mathbf{x}(t) + B \mathbf{u}(t), \quad \mathbf{y}(t) = C \mathbf{x}(t) + D \mathbf{u}(t), \quad \mathbf{x}(t) \in \mathbb{R}^n$$',
        "text": r'<strong>(i) State:</strong> The minimal set of variables $x_1(t), \dots, x_n(t)$ whose values at $t_0$, together with input $u(t)$ for $t \ge t_0$, uniquely determine the system state and output for all future time $t > t_0$.<br><strong>(ii) State Variables:</strong> The smallest set of linearly independent variables $\{x_i(t)\}$ representing dynamic energy storage states (inductor currents, capacitor voltages, position, velocity).<br><strong>(iii) State Vector:</strong> Column vector $\mathbf{x}(t) = [x_1(t), x_2(t), \dots, x_n(t)]^T \in \mathbb{R}^n$ grouping all $n$ state variables.<br><strong>(iv) State Space:</strong> The $n$-dimensional Euclidean vector space $\mathbb{R}^n$ whose orthogonal coordinate axes are formed by the state variables $x_1, x_2, \dots, x_n$.'
    },
    'acs-q2': {
        "eq": r'$$x_1 = y, \; x_2 = \dot{y}, \; \dots, \; x_n = y^{(n-1)} \implies \dot{x}_n = -\sum_{i=0}^{n-1} a_i x_{i+1} + b_0 u$$',
        "text": r'<strong>Phase Variables Definition:</strong> State variables defined as the output variable and its successive $(n-1)$ time derivatives ($x_1=y, x_2=\dot{y}, \dots, x_n=y^{(n-1)}$).<br><strong>Companion Form:</strong> Produces companion matrix $A$ having 1s along the first super-diagonal and negated differential equation coefficients $[-a_0, -a_1, \dots, -a_{n-1}]$ along the bottom row.'
    },
    'acs-q3': {
        "eq": r'$$\dot{x}(t) = A x(t) + B u(t), \quad y(t) = C x(t) + D u(t)$$',
        "text": r'<strong>Integrators:</strong> State variables $x_i(t)$ are strictly the physical outputs of integrators ($1/s$), driven by derivative inputs $\dot{x}_i(t)$.<br><strong>Matrix Functions:</strong> Matrix $A$ ($n\times n$) provides internal state feedback, $B$ ($n\times m$) distributes external inputs, $C$ ($p\times n$) observes states to outputs, and $D$ ($p\times m$) provides direct feedthrough.'
    },
    'acs-q4': {
        "eq": r'$$\bar{A} = P^{-1} A P, \quad \bar{B} = P^{-1} B, \quad \bar{C} = C P, \quad \bar{D} = D \implies \det(sI - \bar{A}) = \det(sI - A)$$',
        "text": r'<strong>Non-Uniqueness:</strong> Any non-singular similarity transformation $x = P z$ creates an equivalent valid state space representation.<br><strong>System Invariants:</strong> System eigenvalues (roots of $\det(sI-A)=0$) and the transfer function $G(s) = C(sI-A)^{-1}B + D$ remain strictly invariant under coordinate transformations.'
    },
    'acs-q4b': {
        "eq": r'$$G(s) = \frac{Y(s)}{U(s)} = C (sI - A)^{-1} B + D = \frac{C \operatorname{adj}(sI - A) B}{\det(sI - A)} + D$$',
        "text": r'Applying Laplace transforms with zero initial conditions yields the transfer function $G(s)$, whose denominator roots $\det(sI - A) = 0$ directly define the invariant system poles and eigenvalues.'
    },
    'acs-q5': {
        "eq": r'$$\begin{bmatrix} \dot{i}_L \\ \dot{v}_C \end{bmatrix} = \begin{bmatrix} -R/L & -1/L \\ 1/C & 0 \end{bmatrix} \begin{bmatrix} i_L \\ v_C \end{bmatrix} + \begin{bmatrix} 1/L \\ 0 \end{bmatrix} v_{in}(t)$$',
        "text": r'State variables in electrical networks are naturally selected as the energy-storage states: inductor current $i_L(t)$ (magnetic energy) and capacitor voltage $v_C(t)$ (electrostatic energy), governed by $v_L = L \frac{di_L}{dt}$ and $i_C = C \frac{dv_C}{dt}$.'
    },
    'acs-q6': {
        "eq": r'$$\begin{bmatrix} \frac{di_a}{dt} \\ \frac{d\omega}{dt} \\ \frac{d\theta}{dt} \end{bmatrix} = \begin{bmatrix} -R_a/L_a & -K_b/L_a & 0 \\ K_t/J & -B/J & 0 \\ 0 & 1 & 0 \end{bmatrix} \begin{bmatrix} i_a \\ \omega \\ \theta \end{bmatrix} + \begin{bmatrix} 1/L_a \\ 0 \\ 0 \end{bmatrix} v_a(t)$$',
        "text": r'An armature-controlled DC motor couples electrical armature dynamics ($v_a = R_a i_a + L_a \frac{di_a}{dt} + e_b$) to mechanical rotor dynamics ($T_e = K_t i_a = J \dot{\omega} + B \omega$), with back-EMF feedback $e_b = K_b \omega$.'
    },
    'acs-q7': {
        "eq": r'$$\Lambda = M^{-1} A M = \operatorname{diag}(\lambda_1, \lambda_2, \dots, \lambda_n), \quad \dot{z} = \Lambda z + M^{-1} B u$$',
        "text": r'Controllable canonical form organizes coefficients into a companion matrix for direct pole-placement, whereas Diagonal (Jordan) canonical form decouples system modes using the modal matrix of eigenvectors $M = [v_1 \; v_2 \; \dots \; v_n]$.'
    },
    'acs-q7b': {
        "eq": r'$$\begin{bmatrix} \frac{di_f}{dt} \\ \frac{d\omega}{dt} \end{bmatrix} = \begin{bmatrix} -R_f/L_f & 0 \\ K_{tf}/J & -B/J \end{bmatrix} \begin{bmatrix} i_f \\ \omega \end{bmatrix} + \begin{bmatrix} 1/L_f \\ 0 \end{bmatrix} v_f(t)$$',
        "text": r'In field-controlled DC motors, armature current $I_a$ is held constant so torque $T_e = K_{tf} i_f$ is linearly driven by field current, completely eliminating back-EMF feedback into the electrical circuit.'
    },
    'acs-q8': {
        "eq": r'$$x(t) = \mathcal{L}^{-1}\{(sI - A)^{-1}\} x(0) = e^{At} x(0) = \Phi(t) x(0)$$',
        "text": r'The unforced (autonomous) state trajectory represents the Zero-Input Response (ZIR), computed by taking the inverse Laplace transform of the resolvent matrix $\Phi(s) = (sI - A)^{-1}$ multiplied by initial condition vector $x(0)$.'
    },
    'acs-q9': {
        "eq": r'$$\Phi(t) = e^{At} = \mathcal{L}^{-1}\{(sI - A)^{-1}\} = \sum_{k=0}^{\infty} \frac{A^k t^k}{k!}$$',
        "text": r'<strong>Key Properties of State Transition Matrix:</strong><br><strong>1. Identity:</strong> $\Phi(0) = e^0 = I$<br><strong>2. Inverse / Time Reversal:</strong> $\Phi^{-1}(t) = \Phi(-t)$<br><strong>3. Group Property:</strong> $\Phi(t_1 + t_2) = \Phi(t_1)\Phi(t_2)$<br><strong>4. Power Property:</strong> $[\Phi(t)]^k = \Phi(kt)$<br><strong>5. Derivative:</strong> $\dot{\Phi}(t) = A \Phi(t) = \Phi(t) A$'
    },
    'acs-q9b': {
        "eq": r'$$x(k+1) = G x(k) + H u(k), \quad G = e^{AT}, \quad H = \left(\int_0^T e^{A\tau} d\tau\right) B, \quad G(z) = C (zI - G)^{-1} H + D$$',
        "text": r'Discrete-time state equations discretized over sampling period $T$ with Zero-Order Hold (ZOH) are stable if and only if all eigenvalues of matrix $G$ lie strictly inside the unit circle $|\lambda_i| < 1$.'
    },
    'acs-q10': {
        "eq": r'$$e^{At} = \sum_{k=0}^{n-1} \alpha_k(t) A^k, \quad \text{where } e^{\lambda_i t} = \sum_{k=0}^{n-1} \alpha_k(t) \lambda_i^k \quad (\text{for all eigenvalues } \lambda_i)$$',
        "text": r'The Cayley-Hamilton theorem states that every square matrix satisfies its own characteristic equation, allowing any matrix exponential $e^{At}$ to be expressed as a finite polynomial of degree at most $(n-1)$.'
    },
    'acs-q11': {
        "eq": r'$$x(t) = \underbrace{e^{A(t-t_0)} x(t_0)}_{\text{Zero-Input Response (ZIR)}} + \underbrace{\int_{t_0}^t e^{A(t-\tau)} B u(\tau) d\tau}_{\text{Zero-State Response (ZSR)}}$$',
        "text": r'The complete solution of non-homogeneous LTI state equations is the linear superposition of the initial-condition response (ZIR) and the convolution integral of the forced input response (ZSR).'
    },
    'acs-q12': {
        "eq": r'$$\text{Pair } (A, B) \text{ is controllable} \iff \text{Dual pair } (A^T, C^T) \text{ is observable, where } Q_o(A, C) = [Q_c(A^T, C^T)]^T$$',
        "text": r"Kalman's Duality Principle proves that controllability and observability are mathematical duals, allowing any observer design algorithm to solve a state feedback control problem on the transpose system."
    },
    'acs-q13': {
        "eq": r'$$\dot{z} = \Lambda z + \tilde{B} u, \quad y = \tilde{C} z + D u, \quad \text{where } \tilde{B} = M^{-1}B, \quad \tilde{C} = CM$$',
        "text": r"By Gilbert's method, a diagonalized system with distinct eigenvalues is controllable if and only if matrix $\tilde{B}$ contains no all-zero rows, and observable if and only if matrix $\tilde{C}$ contains no all-zero columns."
    },
    'acs-q13b': {
        "eq": r'$$\operatorname{rank}[\lambda_i I - A \quad B] = n \quad (\text{Controllability}), \qquad \operatorname{rank}\begin{bmatrix} \lambda_i I - A \\ C \end{bmatrix} = n \quad (\text{Observability}) \quad \forall \lambda_i \in \sigma(A)$$',
        "text": r'The Popov-Belevitch-Hautus (PBH) test evaluates rank drop at each eigenvalue $\lambda_i$, identifying uncontrollable or unobservable modes directly without coordinate transformations.'
    },
    'acs-q14': {
        "eq": r'$$K = \begin{bmatrix} 0 & 0 & \dots & 1 \end{bmatrix} Q_c^{-1} \phi_d(A), \quad \text{where } \phi_d(A) = A^n + \alpha_{n-1} A^{n-1} + \dots + \alpha_0 I$$',
        "text": r"Ackermann's formula directly calculates the unique state feedback gain matrix $K$ that places all closed-loop eigenvalues of $(A - BK)$ at desired locations, provided the controllability matrix $Q_c$ has full rank $n$."
    },
    'acs-q15': {
        "eq": r'$$\dot{\hat{x}} = A \hat{x} + B u + L (y - C \hat{x}), \quad \dot{e}(t) = (A - LC) e(t), \quad L = \phi_d(A) Q_o^{-1} \begin{bmatrix} 0 \\ \vdots \\ 1 \end{bmatrix}$$',
        "text": r'A full-order Luenberger observer estimates internal states from measured outputs, with error dynamics decaying asymptotically to zero when observer gain matrix $L$ stabilizes $(A - LC)$.'
    },
    'acs-q16': {
        "eq": r'$$f(x_1 + x_2) \ne f(x_1) + f(x_2), \quad f(\alpha x) \ne \alpha f(x) \implies \text{Superposition Principle Fails}$$',
        "text": r'<strong>Distinct Non-Linear Physical Phenomena:</strong><br><strong>1. Limit Cycles:</strong> Isolated, self-sustained closed periodic orbits in state space (stable or unstable).<br><strong>2. Jump Resonance:</strong> Discontinuous jump in amplitude and phase during continuous sinusoidal frequency sweeps.<br><strong>3. Subharmonics:</strong> Generation of steady output responses at integer fractions ($f/2, f/3$) of input frequency.<br><strong>4. Amplitude-Dependent Stability:</strong> System stability depends on initial state or excitation amplitude, unlike linear systems.'
    },
    'acs-q16b': {
        "eq": r'$$N(X)_{\text{ideal}} = \frac{4M}{\pi X}, \qquad N(X)_{\text{deadzone}} = \frac{4M}{\pi X} \sqrt{1 - \left(\frac{D}{X}\right)^2} \quad (X > D)$$',
        "text": r'<strong>1. Ideal Relay:</strong> Output switches between $+M$ and $-M$; describing function $N(X) = \frac{4M}{\pi X}$ is pure real with zero phase shift ($\angle N(X) = 0^\circ$).<br><strong>2. Relay with Dead-Zone ($D$):</strong> Output is zero for input amplitude $X \le D$; for $X > D$, effective gain drops as amplitude increases with zero phase shift.'
    },
    'acs-q17': {
        "eq": r'$$N(X) = \frac{2k}{\pi} \left[ \arcsin\left(\frac{S}{X}\right) + \frac{S}{X}\sqrt{1 - \left(\frac{S}{X}\right)^2} \right] \quad (X \ge S), \qquad N(X) = k \quad (X < S)$$',
        "text": r'For sinusoidal input exceeding saturation threshold $S$, the effective gain $N(X)$ drops monotonically below slope $k$ as amplitude $X$ increases, introducing zero phase shift ($\angle N(X) = 0^\circ$).'
    },
    'acs-q17b': {
        "eq": r'$$N(X) = k \left[ 1 - \frac{2}{\pi}\arcsin\left(\frac{D}{X}\right) - \frac{2D}{\pi X}\sqrt{1 - \left(\frac{D}{X}\right)^2} \right] \quad (X > D), \qquad N(X) = 0 \quad (X \le D)$$',
        "text": r'Dead-zone non-linearity produces zero output until input amplitude exceeds dead-band $D$, beyond which the effective gain increases monotonically from 0 toward linear gain $k$ as $X \to \infty$.'
    },
    'acs-q18': {
        "eq": r'$$G(j\omega) = -\frac{1}{N(X)} \iff |G(j\omega)| \cdot |N(X)| = 1 \quad \text{and} \quad \angle G(j\omega) = -180^\circ - \angle N(X)$$',
        "text": r'A sustained limit cycle occurs at the intersection of the linear plant Nyquist plot $G(j\omega)$ with the $-1/N(X)$ locus; the cycle is stable if increasing amplitude $X$ moves the point into the stable region.'
    },
    'acs-q19': {
        "eq": r'$$\frac{dx_2}{dx_1} = \frac{f_2(x_1, x_2)}{f_1(x_1, x_2)} = \frac{0}{0} \quad \text{at equilibrium point } (x_1^*, x_2^*)$$',
        "text": r'<strong>Classification of Singular Points by Linearized Eigenvalues:</strong><br><strong>1. Stable / Unstable Node:</strong> Real eigenvalues of same sign ($\lambda_1, \lambda_2 \in \mathbb{R}, \lambda_1\lambda_2 > 0$).<br><strong>2. Saddle Point:</strong> Real eigenvalues of opposite sign ($\lambda_1 > 0, \lambda_2 < 0$) &mdash; <em>always unstable</em>!<br><strong>3. Stable / Unstable Focus:</strong> Complex conjugate eigenvalues with real part ($\sigma \pm j\omega, \sigma \ne 0$).<br><strong>4. Center (Vortex):</strong> Purely imaginary conjugate eigenvalues ($\pm j\omega, \sigma = 0$) &mdash; closed concentric periodic orbits.'
    },
    'acs-q20': {
        "eq": r'$$V(x) = x^T P x > 0 \quad (\forall x \ne 0) \iff \Delta_1 > 0, \; \Delta_2 > 0, \; \dots, \; \Delta_n > 0$$',
        "text": r'<strong>Sylvester Criterion for Positive Definiteness:</strong> A real symmetric matrix $P = P^T$ is positive definite if and only if all $n$ leading principal minors $\Delta_k = \det(P_{k\times k})$ are strictly positive ($\Delta_1 > 0, \Delta_2 > 0, \dots, \Delta_n > 0$).<br><strong>Negative Definite:</strong> If and only if leading principal minors alternate signs starting negative ($\Delta_1 < 0, \Delta_2 > 0, \Delta_3 < 0, \dots$).'
    },
    'acs-q20b': {
        "eq": r'$$V(x) = f(x)^T P f(x), \quad \dot{V}(x) = f(x)^T (J^T P + P J) f(x) < 0 \quad \text{where } J(x) = \frac{\partial f}{\partial x}$$',
        "text": r"Krasovskii's method constructs a valid Lyapunov function directly from system vector fields $f(x)$, guaranteeing asymptotic stability if the symmetric matrix $\hat{F} = J^T P + P J$ is negative definite."
    },
    'acs-q21': {
        "eq": r'$$\text{Slope } m = \frac{dx_2}{dx_1} = \frac{-x_1 - f(x_1, x_2)}{x_2} = N \implies x_2 = g(x_1, N) \quad (\text{Isocline Line})$$',
        "text": r'The method of isoclines plots curves of constant trajectory slope $m = N$, drawing direction tangents across each isocline to trace phase trajectories and locate isolated limit cycles.'
    },
    'acs-q22': {
        "eq": r'$$A^T P + P A = -Q, \quad V(x) = x^T P x > 0, \quad \dot{V}(x) = -x^T Q x < 0$$',
        "text": r"Lyapunov's direct theorem proves that a continuous LTI system $\dot{x} = Ax$ is asymptotically stable if and only if for any chosen symmetric positive definite matrix $Q > 0$, the Lyapunov equation yields a unique symmetric positive definite matrix $P > 0$."
    },
    'drive-q1': {
        "eq": r'$$\text{Source} \longrightarrow \text{Power Modulator} \longrightarrow \text{Electric Motor} \longrightarrow \text{Load} \quad (\text{Closed-Loop Control})$$',
        "text": r'<strong>Constituent Elements of an Electric Drive:</strong><br><strong>1. Power Source:</strong> 1-phase/3-phase AC utility grid or DC source/battery.<br><strong>2. Power Modulator:</strong> Regulates energy flow via converters/inverters (rectifiers, choppers, VSIs, cycloconverters).<br><strong>3. Electric Motor:</strong> Converts modulated electrical energy to controlled mechanical torque (DC, Induction, BLDC, Synchronous).<br><strong>4. Control & Sensing Unit:</strong> Measures current/speed/position and generates switching signals to enforce precision motion.'
    },
    'drive-q2': {
        "eq": r'$$\eta_{\text{electric}} > 90\%, \quad \text{Four-Quadrant Operation}, \quad \text{Zero Direct Tailpipe Emissions}$$',
        "text": r'Electric drives surpass mechanical/thermal drives with superior conversion efficiency, instantaneous torque response, clean zero-emission operation, regenerative braking capability, and digital automation integration.'
    },
    'drive-q3': {
        "eq": r'$$T_L = T_{L0} + C \left(\frac{\omega}{\omega_n}\right)^k, \quad k=0 \text{ (Hoist)}, \; k=1 \text{ (Calender)}, \; k=2 \text{ (Fan/Pump)}, \; k=-1 \text{ (Lathe)}$$',
        "text": r'<strong>Classification of Industrial Load Torques:</strong><br><strong>1. Active Load Torques:</strong> Torques that retain their sign/direction irrespective of rotation direction (e.g., gravitational torque in hoists $k=0$, tension in coilers).<br><strong>2. Passive Load Torques:</strong> Torques that always oppose motion (dry coulomb friction $k=0$, viscous friction $k=1$, centrifugal fans/pumps $T_L \propto \omega^2$ with $k=2$, constant power machine tools $T_L \propto 1/\omega$ with $k=-1$).'
    },
    'drive-q3b': {
        "eq": r'$$\omega_{\text{crit}} = \sqrt{\frac{K_{sh}(J_M + J_L)}{J_M \cdot J_L}}, \qquad |\omega_{\text{operating}} - \omega_{\text{crit}}| \ge 0.20 \, \omega_{\text{crit}}$$',
        "text": r'Critical speed occurs when rotational shaft speed excites the natural torsional frequency of the mechanical coupling, creating severe resonant torque oscillations and catastrophic shaft fracture.'
    },
    'drive-q4': {
        "eq": r'$$T - T_L = J \frac{d\omega_m}{dt} + \frac{1}{2} \omega_m^2 \frac{dJ}{dt} \approx J \frac{d\omega_m}{dt}$$',
        "text": r'The fundamental dynamic torque equation governs acceleration: positive dynamic torque ($T > T_L$) accelerates the motor, balanced torque ($T = T_L$) maintains steady speed, and negative torque ($T < T_L$) causes deceleration.'
    },
    'drive-q5': {
        "eq": r'$$P_m = T \cdot \omega_m \implies \begin{cases} \text{Q1: Forward Motoring } (+T, +\omega, P>0) & \text{Q2: Forward Braking } (-T, +\omega, P<0) \\ \text{Q3: Reverse Motoring } (-T, -\omega, P>0) & \text{Q4: Reverse Braking } (+T, -\omega, P<0) \end{cases}$$',
        "text": r'<strong>Four-Quadrant Operation of Hoist Drive:</strong><br><strong>Quadrant 1 (Forward Motoring):</strong> $+T, +\omega_m$ &mdash; Hoisting a loaded cage upward against gravity ($P_m > 0$).<br><strong>Quadrant 2 (Forward Braking):</strong> $-T, +\omega_m$ &mdash; Decelerating upward motion via regenerative braking ($P_m < 0$).<br><strong>Quadrant 3 (Reverse Motoring):</strong> $-T, -\omega_m$ &mdash; Driving an empty cage downward against friction ($P_m > 0$).<br><strong>Quadrant 4 (Reverse Braking):</strong> $+T, -\omega_m$ &mdash; Safely lowering a loaded cage under gravity with braking counter-torque ($P_m < 0$).'
    },
    'drive-q6': {
        "eq": r'$$\frac{dT_L}{d\omega_m} - \frac{dT}{d\omega_m} > 0 \iff \frac{dT_L}{d\omega_m} > \frac{dT}{d\omega_m} \quad (\text{at equilibrium } T = T_L)$$',
        "text": r'An electric drive operating point is steady-state stable if a small disturbance increase in speed creates a retarding net torque ($T_L > T$), naturally restoring the drive to equilibrium speed.'
    },
    'drive-q6b': {
        "eq": r'$$\theta(t) = \theta_{ss} (1 - e^{-t/\tau_h}) + \theta_0 e^{-t/\tau_h}, \quad \tau_h = \frac{C_{th}}{A \cdot h}, \quad P_{\text{rated}} \ge P_{\text{rms}} = \sqrt{\frac{\sum P_i^2 t_i}{\sum t_i}}$$',
        "text": r'Motor thermal selection ensures steady-state temperature rise $\theta_{ss} = P_{\text{loss}}/(A \cdot h)$ does not exceed the insulation class thermal rating ($B, F, H$) under continuous and fluctuating duty cycles.'
    },
    'drive-q7': {
        "eq": r'$$\omega_m = \frac{V_a - I_a R_a}{K \phi} \implies \begin{cases} \text{Below Base Speed: } V_a \text{ variation at rated } \phi \implies \text{Constant Torque Mode} \\ \text{Above Base Speed: } \phi \text{ reduction at rated } V_a \implies \text{Constant Power Mode} \end{cases}$$',
        "text": r'<strong>1. Armature Voltage Control (Below Base Speed):</strong> Variable $V_a$ with full rated flux $\phi$ provides <strong>Constant Torque</strong> ($T_{\max} = K \phi I_{a,\text{rated}}$), where power increases linearly with speed ($P \propto \omega$).<br><strong>2. Field Weakening Control (Above Base Speed):</strong> Rated $V_a$ with reduced field flux $\phi$ provides <strong>Constant Power</strong> ($P = V_a I_a = \text{constant}$), where developed torque decreases inversely with speed ($T \propto 1/\omega$).'
    },
    'drive-q7b': {
        "eq": r'$$V_{dc} = \frac{3\sqrt{3}V_m}{2\pi}(1 + \cos\alpha) \ge 0 \quad (\forall \alpha \in [0^\circ, 180^\circ])$$',
        "text": r'Semi-converters use freewheeling diodes that clamp the output voltage to non-negative values ($V_{dc} \ge 0$), restricting drive operation to single-quadrant motoring and preventing regenerative braking.'
    },
    'drive-q8': {
        "eq": r'$$V_a = \frac{2V_m}{\pi}\cos\alpha, \quad \omega_m = \frac{\frac{2V_m}{\pi}\cos\alpha - I_a R_a}{K_t \phi} \quad (\text{Continuous Conduction})$$',
        "text": r'A single-phase full converter allows two-quadrant operation: rectification/motoring for firing angle $\alpha < 90^\circ$ and inversion/regenerative braking into the AC mains for $\alpha > 90^\circ$ with reversed armature connections.'
    },
    'drive-q8b': {
        "eq": r'$$V_a = \frac{3\sqrt{3}V_m}{\pi}\cos\alpha, \quad \omega_m = \frac{\frac{3\sqrt{3}V_m}{\pi}\cos\alpha - I_a R_a}{K_t \phi}$$',
        "text": r'Three-phase full converters provide six-pulse output with high ripple frequency ($300\text{ Hz}$), maintaining continuous armature conduction across wide load ranges with lower harmonic heating and higher motor efficiency.'
    },
    'drive-q9': {
        "eq": r'$$V_a = \delta V_s = \left(\frac{t_{on}}{T}\right) V_s, \quad \omega_m = \frac{\delta V_s - I_a R_a}{K_t \phi} \quad (0 \le \delta \le 1)$$',
        "text": r'A Class-A step-down (buck) chopper controls motor speed smoothly in Quadrant 1 with high energy efficiency, rapid dynamic response, and low armature current ripple.'
    },
    'drive-q9b': {
        "eq": r'$$V_s = \frac{E_b}{1 - \delta} \implies I_a = \frac{E_b - (1-\delta)V_s}{R_a} \quad (\text{Quadrant 2 Operation})$$',
        "text": r'A Class-B step-up (boost) chopper uses the motor armature inductance to boost induced back-EMF $E_b$ above DC source voltage $V_s$, pumping regenerative braking energy back to the DC supply.'
    },
    'drive-q10': {
        "eq": r'$$V_a = \delta V_s \ge 0, \quad I_a > 0 \text{ (Motoring via } CH_1\text{-}D_2\text{)}, \quad I_a < 0 \text{ (Regeneration via } CH_2\text{-}D_1\text{)}$$',
        "text": r'A two-quadrant Class-C chopper achieves seamless forward motoring (Q1) and forward regenerative braking (Q2) by alternately switching two complementary chopper legs without mechanical contactor reversal.'
    },
    'drive-q10b': {
        "eq": r'$$V_a = (2\delta - 1)V_s, \quad -V_s \le V_a \le +V_s, \quad -I_{\max} \le I_a \le +I_{\max}$$',
        "text": r'A four-quadrant Class-E H-bridge chopper provides instantaneous bidirectional control of both armature voltage and current, enabling smooth forward/reverse motoring and regenerative braking.'
    },
    'drive-q11': {
        "eq": r'$$\tau_{\text{current}} \approx 1\text{--}2\text{ ms} \ll \tau_{\text{speed}} \approx 30\text{--}100\text{ ms} \implies \text{Cascaded Loops with Inner Current Clamping}$$',
        "text": r'Cascaded two-loop control uses an inner current loop to enforce instantaneous semiconductor overcurrent protection, nested inside a slower outer PI speed loop that ensures zero steady-state tracking error.'
    },
    'drive-q12': {
        "eq": r'$$T_e \propto V_s^2 \implies \text{Torque drops quadratically with stator voltage; } P_{cu2} = s P_g \implies \text{Severe Rotor Overheating}$$',
        "text": r'Stator voltage speed control is restricted to high-slip induction motors driving fan/pump loads over narrow speed ranges because motor torque collapses with $V_s^2$ and causes excessive rotor copper dissipation.'
    },
    'drive-q12b': {
        "eq": r'$$\text{VSI: DC voltage link with capacitor (PWM voltage output); } \quad \text{CSI: DC current link with large inductor (inherent regeneration)}$$',
        "text": r'VSI drives supply multiple parallel motors using fast IGBT switches with high power factor, whereas CSI drives provide rugged short-circuit ride-through and direct regenerative capability for high-power single motors.'
    },
    'drive-q13': {
        "eq": r'$$\phi_m \propto \frac{V_s}{f_s} = \text{constant} \implies T_{\max} = \frac{3}{2}\frac{V_s^2}{\omega_s (2\omega_s L_l)} \approx \text{constant breakdown torque}$$',
        "text": r'Maintaining a constant $V/f$ ratio preserves constant air-gap magnetic flux and prevents core saturation, guaranteeing maximum available breakdown torque across the entire base speed range.'
    },
    'drive-q14': {
        "eq": r'$$R_{eff} = R_{ext} (1 - \delta), \quad s \propto \frac{R_2 + R_{eff}}{V_s^2} \quad (0 \le \delta \le 1)$$',
        "text": r'Rotor resistance chopper control smooths slip variation in wound-rotor induction motors without mechanical resistor stepping, but dissipates slip power as heat in external resistors.'
    },
    'drive-q14b': {
        "eq": r'$$P_{\text{slip}} = s P_g; \quad \text{Kramer: Diode rectifier + line inverter (sub-synchronous); Scherbius: Cycloconverter (sub/super-synchronous)}$$',
        "text": r'Slip power recovery schemes recover rotor slip power $s P_g$ and inject it back into the AC mains, achieving high operating efficiency in large-capacity pumps, fans, and wind turbines.'
    },
    'drive-q15': {
        "eq": r'$$\text{True Sync: Inverter frequency set independently } \implies \text{Hunting/Stalling risk; Self-Controlled: Fired via Rotor Sensor } \implies \text{No Hunting}$$',
        "text": r'In self-controlled mode, inverter switching pulses are triggered directly by rotor position sensors (encoder/Hall sensors), eliminating hunting oscillations and preventing synchronous motor pull-out.'
    },
    'drive-q15b': {
        "eq": r'$$\text{Leading Power Factor } (\cos\phi > 0 \text{ leading}) \implies \text{Motor Back-EMF naturally commutates thyristor inverter switches}$$',
        "text": r'Load-Commutated Inverter (LCI) drives over-excite the synchronous motor to draw leading current, allowing generated machine back-EMF to naturally turn off the inverter thyristors without auxiliary commutation circuits.'
    },
    'drive-q16': {
        "eq": r'$$\begin{bmatrix} x_\alpha \\ x_\beta \end{bmatrix} = \frac{2}{3}\begin{bmatrix} 1 & -\frac{1}{2} & -\frac{1}{2} \\ 0 & \frac{\sqrt{3}}{2} & -\frac{\sqrt{3}}{2} \end{bmatrix}\begin{bmatrix} x_a \\ x_b \\ x_c \end{bmatrix}, \quad \begin{bmatrix} x_d \\ x_q \end{bmatrix} = \begin{bmatrix} \cos\theta_e & \sin\theta_e \\ -\sin\theta_e & \cos\theta_e \end{bmatrix}\begin{bmatrix} x_\alpha \\ x_\beta \end{bmatrix}$$',
        "text": r'Clarke transformation converts three-phase stationary $abc$ coordinates into two-phase stationary $\alpha\beta$ coordinates, and Park transformation rotates them into a synchronously rotating $dq$ reference frame.'
    },
    'drive-q17': {
        "eq": r'$$V_{ref} = \frac{T_1}{T_s}V_1 + \frac{T_2}{T_s}V_2 + \frac{T_0}{T_s}V_0, \quad V_{out,\max} = \frac{V_{dc}}{\sqrt{3}} \approx 0.577 V_{dc} \quad (15.5\% \text{ higher than SPWM})$$',
        "text": r'Space Vector PWM synthesizes rotating reference voltage vectors from adjacent stationary active and zero vectors, achieving 15.5% higher DC bus voltage utilization and significantly lower current THD than SPWM.'
    },
    'drive-q18': {
        "eq": r'$$\psi_{rq} = 0 \implies \psi_r = \psi_{rd} = L_m i_{sd}, \qquad T_e = \frac{3}{2} P \frac{L_m}{L_r} \psi_{rd} i_{sq} \propto i_{sd} \cdot i_{sq}$$',
        "text": r'Field-Oriented Control aligns the rotor flux vector strictly along the $d$-axis ($\psi_{rq} = 0$), decoupling AC induction motor control into independent flux regulation ($i_{sd}$) and torque regulation ($i_{sq}$).'
    },
    'mobile-q1': {
        "eq": r'$$\text{Mobile Client} \xleftrightarrow{\quad \text{Wireless Link} \quad} \text{Mobile Middleware / Gateway} \xleftrightarrow{\quad \text{High-Speed Backbone} \quad} \text{Enterprise Server}$$',
        "text": r'Mobile middleware bridges resource-constrained mobile devices and enterprise backend servers by abstracting protocol conversion, state caching, data transcoding, and offline synchronization.'
    },
    'mobile-q2': {
        "eq": r'$$\text{Care-of-Address (CoA)} \iff \text{Home Agent (HA) Encapsulation/Tunneling} \iff \text{Foreign Agent (FA) / Mobile Node}$$',
        "text": r'The Internet serves as the universal transport backbone for mobile computing, using Mobile IP tunneling to route packets seamlessly to mobile nodes regardless of their changing physical point of attachment.'
    },
    'mobile-q3': {
        "eq": r'$$\text{Access Network (Radio BS/AP)} \longrightarrow \text{Edge Network (MEC, Low-Latency Aggregation)} \longrightarrow \text{Core Network (HLR, GGSN/UPF)}$$',
        "text": r'Mobile networks partition infrastructure into Access (over-the-air radio link), Edge (localized edge computing and content caching), and Core (centralized mobility management, authentication, and packet routing).'
    },
    'mobile-q4': {
        "eq": r'$$\text{Primary Constraints: Limited Battery Life, Scarce Bandwidth, Multipath Fading, Intermittent Connectivity, Security Risks}$$',
        "text": r'Mobile computing environments are constrained by finite battery energy, highly variable wireless bandwidth, physical signal attenuation, frequent disconnections, and heightened physical and wireless security risks.'
    },
    'mobile-q5': {
        "eq": r'$$\text{Tier 1: Presentation (Thin/Smart Client)} \longleftrightarrow \text{Tier 2: Application / Middleware Logic} \longleftrightarrow \text{Tier 3: Enterprise Database}$$',
        "text": r'Three-tier architecture separates presentation on the mobile device from application processing on intermediate servers and persistent data storage on enterprise databases, optimizing network utilization.'
    },
    'mobile-q6': {
        "eq": r'$$\text{Key Axioms: Energy-Aware Scheduling, Adaptive Bandwidth Throttling, Offline Replication, End-to-End Security}$$',
        "text": r'Mobile software engineering requires cross-layer optimization prioritizing aggressive battery conservation, bandwidth adaptation, asynchronous offline transaction queuing, and lightweight cryptography.'
    },
    'mobile-q7': {
        "eq": r'$$\text{Context Tuple } \mathcal{C} = \langle \text{Location}, \text{Network Bandwidth}, \text{Battery Energy}, \text{Device Profile}, \text{User Activity} \rangle$$',
        "text": r'Context-aware systems dynamically modify application behavior, media fidelity, and security rules based on real-time awareness of user location, device battery state, and available network bandwidth.'
    },
    'mobile-q8': {
        "eq": r'$$\text{Transcoding: Modality Conversion (Text } \leftrightarrow \text{ Speech), Resolution Scaling, Format Compression (PNG } \to \text{ WebP)}$$',
        "text": r'Content adaptation dynamically transforms, compresses, or transcodes media at intermediary proxies to match the specific screen resolution, memory limits, and network throughput of the client handset.'
    },
    'mobile-q9': {
        "eq": r'$$\text{Seamless Mobility: Continuous Session State, Zero Packet Loss (Buffering/Bicasting), and Handover Latency } \le 50\text{ ms}$$',
        "text": r'Seamless communication preserves active TCP sessions, multimedia streams, and security contexts during cellular handoffs without packet drops or noticeable interruption to the user.'
    },
    'mobile-q10': {
        "eq": r'$$\text{GEO: } 35,786\text{ km (latency } \sim 250\text{ ms, 3 cover Earth); LEO: } 500\text{--}1500\text{ km (latency } \sim 20\text{ ms, dense constellation)}$$',
        "text": r'Geostationary (GEO) satellites provide stationary global coverage with high propagation delay, Medium Earth Orbit (MEO) serves GPS navigation, and Low Earth Orbit (LEO) delivers low-latency mobile broadband.'
    },
    'mobile-q11': {
        "eq": r'$$\text{IMEI (15-digit Handset ID)} \quad | \quad \text{IMSI (15-digit SIM ID)} \quad | \quad \text{MSISDN (Public Number)} \quad | \quad \text{TMSI (Temporary Air ID)}$$',
        "text": r'<strong>Mobile Station Identifiers:</strong><br><strong>1. IMEI:</strong> 15-digit hardware serial number uniquely identifying the physical mobile terminal hardware (TAC + FAC + SNR + Spare).<br><strong>2. IMSI:</strong> 15-digit subscriber identity stored in SIM and HLR/AUC (MCC + MNC + MSIN).<br><strong>3. MSISDN:</strong> Dialable public telephone number routed via PSTN (CC + NDC + SN).<br><strong>4. TMSI:</strong> Temporary identity assigned by VLR to prevent eavesdropping and protect subscriber anonymity over the air interface.'
    },
    'mobile-q12': {
        "eq": r'$$\text{SS7 ISUP Signaling: Initial Address Message (IAM) } \longrightarrow \text{ Address Complete Message (ACM / Ringback) } \longrightarrow \text{ Answer (ANM)}$$',
        "text": r'Call progress indication uses out-of-band telecom signaling messages to update the caller on setup phases (Dialing, Network Routing, Remote Ringing, Busy Tone, or Call Queued).'
    },
    'mobile-q13': {
        "eq": r'$$\text{Shannon: } C = B \log_2(1 + \text{SINR}); \quad \text{CDMA: Orthogonal Walsh Codes } \sum c_i(t)c_j(t) = 0 \text{ sharing time \& frequency}$$',
        "text": r'Multiple access schemes allocate radio resources by splitting frequency channels (FDMA), time slots (TDMA), unique mathematical spreading codes (CDMA), or directional antenna beams (SDMA).'
    },
    'mobile-q14': {
        "eq": r'$$\text{MS (Handset + SIM)} \longleftrightarrow \text{BSS (BTS + BSC)} \longleftrightarrow \text{NSS (MSC + HLR + VLR + AUC + EIR)} \longleftrightarrow \text{PSTN / ISDN}$$',
        "text": r'GSM architecture is divided into the Mobile Station (MS), Base Station Subsystem (BSS) for radio management, and Network and Switching Subsystem (NSS) for call routing, subscriber mobility, and authentication.'
    },
    'mobile-q15': {
        "eq": r'$$\text{MTC: GMSC queries HLR } \longrightarrow \text{ HLR requests MSRN from VLR } \longrightarrow \text{ GMSC routes call to serving MSC} \longrightarrow \text{ MS Paged}$$',
        "text": r'Mobile Originated Calls (MOC) are routed directly by the local serving MSC, whereas Mobile Terminated Calls (MTC) require querying the HLR to obtain a temporary Mobile Station Roaming Number (MSRN).'
    },
    'mobile-q16': {
        "eq": r'$$\text{Telecom Trunk (E1/T1/SIP) } \longrightarrow \text{ IVR Media Gateway (DTMF Decoder / TTS / ASR) } \longleftrightarrow \text{ Database Server}$$',
        "text": r'Interactive Voice Response (IVR) systems decode dual-tone multi-frequency (DTMF) keypad signals and spoken voice inputs to guide callers through interactive audio menus and query enterprise databases.'
    },
    'mobile-q17': {
        "eq": r'$$\text{Authentication: } \text{SRES} = A3(K_i, \text{RAND}), \quad \text{Key Gen: } K_c = A8(K_i, \text{RAND}), \quad \text{Encryption: } \text{Data} \oplus A5(K_c)$$',
        "text": r'<strong>GSM Security Triad Algorithms:</strong><br><strong>1. A3 Algorithm (Authentication):</strong> SIM computes 32-bit $\text{SRES}$ from 128-bit challenge $\text{RAND}$ and secret key $K_i$; network authenticates if $\text{SRES}$ matches AUC.<br><strong>2. A8 Algorithm (Ciphering Key Generation):</strong> Computes 64-bit session key $K_c$ on SIM from $\text{RAND}$ and $K_i$ ($K_i$ never transmitted over radio).<br><strong>3. A5 Algorithm (Air Encryption):</strong> Hardware stream cipher that encrypts/decrypts TDMA radio bursts using $K_c$ and frame number.'
    },
    'mobile-q18': {
        "eq": r'$$\text{SMS Transmission: Control Channels (SDCCH / SACCH) } \implies \text{Zero impact on dedicated traffic channels (TCH)}$$',
        "text": r'SMS operates as a store-and-forward signaling service, transferring short text messages over cellular signaling control channels without interrupting or reserving voice traffic channels.'
    },
    'mobile-q19': {
        "eq": r'$$\text{Max Throughput: } 171.2\text{ kbps (CS-4, 8 slots); Bottlenecks: Dynamic channel coding, high latency, voice priority pre-emption}$$',
        "text": r'GPRS packet data speeds are constrained by shared radio slot contention, distance-dependent channel coding schemes (CS-1 to CS-4), and circuit-switched voice calls preempting data channels.'
    },
    'mobile-q20': {
        "eq": r'$$\text{CDR Charging: S-CDR generated at SGSN (Radio/Mobility) } + \text{ G-CDR generated at GGSN (Data Volume \& External IP)}$$',
        "text": r'GPRS charges subscribers primarily for data volume transferred (megabytes) rather than connection duration, combining SGSN mobility records and GGSN volume records into unified billing files.'
    },
    'mobile-q21': {
        "eq": r'$$\text{SMS-MT Delivery: SMSC } \longrightarrow \text{ SMS-GMSC } \xrightarrow{\text{HLR Routing Info}} \text{ Serving MSC/VLR } \xrightarrow{\text{SDCCH Paging}} \text{ MS}$$',
        "text": r'SMS relies on the Short Message Service Center (SMSC) to store messages until the destination phone is reachable, querying the HLR for current location before delivering over signaling channels.'
    },
    'mobile-q22': {
        "eq": r'$$\text{MS} \xrightarrow{\text{Um (MAC/RLC)}} \text{BSS} \xrightarrow{\text{Gb (Frame Relay)}} \text{SGSN} \xrightarrow{\text{Gn (GTP/UDP/IP)}} \text{GGSN} \xrightarrow{\text{Gi}} \text{Public Internet}$$',
        "text": r'GPRS adds packet switching to GSM networks via the Serving GPRS Support Node (SGSN) for mobility tracking and ciphering, and Gateway GPRS Support Node (GGSN) for external IP routing.'
    },
    'mobile-q23': {
        "eq": r'$$\text{QoS Profile} = \langle \text{Service Precedence (1-3)}, \; \text{Delay Class (1-4)}, \; \text{Reliability Class (1-5)}, \; \text{Peak/Mean Throughput} \rangle$$',
        "text": r'GPRS negotiates QoS profiles between the mobile terminal and network to guarantee bounded packet delay, acceptable packet loss rates, and prioritized transmission for delay-critical traffic.'
    },
    'mobile-q24': {
        "eq": r'$$\text{Infrastructure BSS: Mobile nodes communicate via Access Point (AP); IBSS: Peer-to-peer ad-hoc communication without AP}$$',
        "text": r'Infrastructure WLAN connects mobile devices to wired networks through access points with centralized coordination, whereas IBSS forms spontaneous peer-to-peer networks without fixed infrastructure.'
    },
    'mobile-q25': {
        "eq": r'$$\text{Priority Hierarchy: } \text{SIFS} < \text{PIFS} < \text{DIFS} < \text{EIFS} \implies \text{Shorter waiting interval guarantees higher channel access priority}$$',
        "text": r'<strong>IEEE 802.11 Interframe Spaces (IFS):</strong><br><strong>1. SIFS (Shortest, 10 &mu;s):</strong> Highest priority for immediate response frames: ACK, CTS, and fragmented frames.<br><strong>2. PIFS (PCF IFS):</strong> Medium priority used exclusively by Access Point in Point Coordination Function for contention-free polling.<br><strong>3. DIFS (DCF IFS):</strong> Standard interval contending stations must wait after channel idle before initiating backoff counter in CSMA/CA.<br><strong>4. EIFS (Extended IFS):</strong> Longest waiting period applied whenever an invalid or corrupted packet frame is received.'
    },
    'mobile-q26': {
        "eq": r'$$\text{Wi-Fi: Unlicensed 2.4/5 GHz band, high local bit-rate, low range; 3G: Licensed spectrum, macrocells, QoS, seamless mobility}$$',
        "text": r'Wi-Fi provides low-cost, high-speed local broadband over unlicensed spectrum with contention-based access, while cellular networks provide high-mobility, licensed spectrum with deterministic QoS and handoff.'
    },
    'mobile-q27': {
        "eq": r'$$\text{Handshake: } \text{Sender} \xrightarrow{\text{RTS}} \text{Receiver} \xrightarrow{\text{CTS}} \text{Sender} \implies \text{Overcomes Hidden Terminal}; \quad \text{NAV (Network Allocation Vector)}$$',
        "text": r'RTS/CTS exchange reserves the wireless channel by broadcasting transmission duration in the Network Allocation Vector (NAV), silencing hidden neighbors and preventing carrier-sense collisions.'
    },
    'mobile-q28': {
        "eq": r'$$\text{PSTN Exchange } \longleftrightarrow \text{ Radio Base Station (RBS) } \xleftarrow{\text{Microwave / RF Link}} \text{ Fixed Wireless Terminal (FWT) at Subscriber Premise}$$',
        "text": r'WLL replaces traditional copper wire local loops with fixed point-to-multipoint microwave radio links, delivering rapid, cost-effective telephone and data deployment in rural and suburban areas.'
    },
    'mobile-q29': {
        "eq": r'$$\text{Evolution: WEP (Weak 24-bit IV, RC4) } \longrightarrow \text{ WPA (TKIP per-packet key) } \longrightarrow \text{ WPA2 (AES-CCMP 128-bit block cipher)}$$',
        "text": r'WEP was broken due to small 24-bit IV reuse; WPA introduced temporal key integrity (TKIP), and WPA2 established robust enterprise security via AES-CCMP and 802.1X EAP authentication.'
    },
    'mobile-q30': {
        "eq": r'$$\text{HIPERLAN/1: Non-preemptive Priority Multiple Access (EY-NPMA); HIPERLAN/2: TDMA/TDD centralized dynamic scheduling in 5 GHz band}$$',
        "text": r'HIPERLAN/1 utilizes Elimination-Yield contention access for peer-to-peer high-speed traffic, while HIPERLAN/2 employs connection-oriented TDMA/TDD frames with guaranteed ATM/Ethernet QoS.'
    },
    'mobile-q31': {
        "eq": r'$$\text{Security Pillars: Confidentiality (AES/RSA), Integrity (SHA-256/HMAC), Availability (DDoS Defense), Auth \& Non-Repudiation (DSA)}$$',
        "text": r'<strong>Foundational Information Security Pillars:</strong><br><strong>1. Confidentiality:</strong> Ensures sensitive transmitted data is unreadable to eavesdroppers via encryption.<br><strong>2. Integrity:</strong> Guarantees that data packets are not tampered with, altered, or injected in transit using cryptographic hash functions (SHA/HMAC).<br><strong>3. Availability:</strong> Assures that network services and spectrum remain accessible to legitimate users under peak load or attacks.<br><strong>4. Authenticity & Non-Repudiation:</strong> Verifies genuine claimant identity and prevents sender from denying authorship via digital signatures.'
    },
    'mobile-q32': {
        "eq": r'$$\text{Passive Attacks (Eavesdropping, Traffic Analysis) vs Active Attacks (Masquerade, Replay, Message Modification, Denial of Service)}$$',
        "text": r'Passive attacks threaten confidentiality by silently intercepting wireless transmissions without altering data, whereas active attacks compromise integrity and availability by injecting forged or altered packets.'
    },
    'mobile-q33': {
        "eq": r'$$\text{TLS Architecture: Handshake Protocol (mutual auth \& key exchange) + Record Protocol (symmetric encryption \& HMAC data integrity)}$$',
        "text": r'TLS operates above the transport layer providing authenticated end-to-end encryption, while WTLS adapts TLS for low-bandwidth mobile handsets using compact headers and elliptic curves.'
    },
    'mobile-q34': {
        "eq": r'$$n = p \cdot q, \quad \phi(n) = (p-1)(q-1), \quad e \cdot d \equiv 1 \pmod{\phi(n)}, \quad C = M^e \pmod n, \quad M = C^d \pmod n$$',
        "text": r'RSA security relies on the computational difficulty of factoring the product of two large prime numbers $n = pq$, using public encryption key $(e, n)$ and private decryption key $(d, n)$.'
    },
    'mobile-q35': {
        "eq": r'$$Y_A = \alpha^{X_A} \pmod q, \quad Y_B = \alpha^{X_B} \pmod q, \quad K = (Y_B)^{X_A} \pmod q = (Y_A)^{X_B} \pmod q = \alpha^{X_A X_B} \pmod q$$',
        "text": r'Diffie-Hellman enables two parties to establish a shared secret key $K$ over an insecure channel based on the discrete logarithm problem, vulnerable to Man-in-the-Middle if unauthenticated.'
    },
    'mobile-q36': {
        "eq": r'$$\Delta f = \frac{1}{T_{\text{sym}}}, \quad \int_0^{T_{\text{sym}}} \cos(2\pi f_i t)\cos(2\pi f_j t) dt = 0 \; (i \ne j), \quad T_{\text{total}} = T_{\text{sym}} + T_{CP}$$',
        "text": r'OFDM divides broadband channels into densely spaced orthogonal narrowband subcarriers, adding a Cyclic Prefix (CP) to eliminate Intersymbol Interference (ISI) and multipath fading.'
    },
    'mobile-q37': {
        "eq": r'$$\text{MBMS: Point-to-Multipoint transmission sharing single radio bearer; MPLS: Label Switched Path (LSP) fast packet forwarding via 32-bit labels}$$',
        "text": r'MBMS conserves cellular bandwidth by broadcasting multimedia data simultaneously to unlimited subscribers on a shared carrier, accelerated by MPLS label switching in the core.'
    },
    'mobile-q38': {
        "eq": r'$$\text{Evolution: 2G (Voice/TDMA, 64 kbps) } \to \text{ 3G (CDMA, 2 Mbps) } \to \text{ 4G (All-IP/OFDMA, 100 Mbps) } \to \text{ 5G (eMBB/URLLC/mMTC, 10-20 Gbps)}$$',
        "text": r'Mobile networks evolved from circuit-switched analog/digital voice (1G/2G) to wideband data (3G), flat All-IP OFDMA (4G LTE), and service-based network slicing supporting sub-millisecond URLLC and massive IoT (5G).'
    }
}

def get_byheart_card_html(qid, marks=3):
    item = BYHEART_DATA.get(qid)
    if not item:
        return ""
    eq_html = f'<div class="byheart-eq">{item["eq"]}</div>' if item.get("eq") else ""
    time_badge = '<span class="byheart-time-badge">⏱️ 5 Mins Writing Time</span>' if marks == 3 else '<span class="byheart-time-badge">⏱️ 12 Mins Writing Time</span>'
    return f"""
            <div class="byheart-card">
                <div class="byheart-header">
                    <div class="byheart-title-group">
                        <span class="byheart-icon">⚡</span>
                        <span class="byheart-title">Sentence / (Equation) to Byhart</span>
                    </div>
                    <div class="byheart-badges-group">
                        {time_badge}
                        <span class="byheart-badge">⭐ High Mark Weightage</span>
                    </div>
                </div>
                <div class="byheart-body">
                    {eq_html}
                    <p class="byheart-text">{item['text']}</p>
                </div>
            </div>"""
