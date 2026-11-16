# -*- coding: utf-8 -*-
"""
High mark-weightage equations and core memorization sentences for all 406 questions across 15 subjects.
Heading: Key Equation / Remember This
"""

BYHEART_DATA = {   'acs-q1': {   'eq': '$$\\dot{\\mathbf{x}}(t) = A \\mathbf{x}(t) + B \\mathbf{u}(t), \\quad \\mathbf{y}(t) = C '
                        '\\mathbf{x}(t) + D \\mathbf{u}(t), \\quad \\mathbf{x}(t) \\in \\mathbb{R}^n$$',
                  'text': '<strong>(i) State:</strong> The minimal set of variables $x_1(t), \\dots, x_n(t)$ whose '
                          'values at $t_0$, together with input $u(t)$ for $t \\ge t_0$, uniquely determine the system '
                          'state and output for all future time $t > t_0$.<br><strong>(ii) State Variables:</strong> '
                          'The smallest set of linearly independent variables $\\{x_i(t)\\}$ representing dynamic '
                          'energy storage states (inductor currents, capacitor voltages, position, '
                          'velocity).<br><strong>(iii) State Vector:</strong> Column vector $\\mathbf{x}(t) = [x_1(t), '
                          'x_2(t), \\dots, x_n(t)]^T \\in \\mathbb{R}^n$ grouping all $n$ state '
                          'variables.<br><strong>(iv) State Space:</strong> The $n$-dimensional Euclidean vector space '
                          '$\\mathbb{R}^n$ whose orthogonal coordinate axes are formed by the state variables $x_1, '
                          'x_2, \\dots, x_n$.'},
    'acs-q10': {   'eq': '$$e^{At} = \\sum_{k=0}^{n-1} \\alpha_k(t) A^k, \\quad \\text{where } e^{\\lambda_i t} = '
                         '\\sum_{k=0}^{n-1} \\alpha_k(t) \\lambda_i^k \\quad (\\text{for all eigenvalues } '
                         '\\lambda_i)$$',
                   'text': 'The Cayley-Hamilton theorem states that every square matrix satisfies its own '
                           'characteristic equation, allowing any matrix exponential $e^{At}$ to be expressed as a '
                           'finite polynomial of degree at most $(n-1)$.'},
    'acs-q11': {   'eq': '$$x(t) = \\underbrace{e^{A(t-t_0)} x(t_0)}_{\\text{Zero-Input Response (ZIR)}} + '
                         '\\underbrace{\\int_{t_0}^t e^{A(t-\\tau)} B u(\\tau) d\\tau}_{\\text{Zero-State Response '
                         '(ZSR)}}$$',
                   'text': 'The complete solution of non-homogeneous LTI state equations is the linear superposition '
                           'of the initial-condition response (ZIR) and the convolution integral of the forced input '
                           'response (ZSR).'},
    'acs-q12': {   'eq': '$$\\text{Pair } (A, B) \\text{ is controllable} \\iff \\text{Dual pair } (A^T, C^T) \\text{ '
                         'is observable, where } Q_o(A, C) = [Q_c(A^T, C^T)]^T$$',
                   'text': "Kalman's Duality Principle proves that controllability and observability are mathematical "
                           'duals, allowing any observer design algorithm to solve a state feedback control problem on '
                           'the transpose system.'},
    'acs-q13': {   'eq': '$$\\dot{z} = \\Lambda z + \\tilde{B} u, \\quad y = \\tilde{C} z + D u, \\quad \\text{where } '
                         '\\tilde{B} = M^{-1}B, \\quad \\tilde{C} = CM$$',
                   'text': "By Gilbert's method, a diagonalized system with distinct eigenvalues is controllable if "
                           'and only if matrix $\\tilde{B}$ contains no all-zero rows, and observable if and only if '
                           'matrix $\\tilde{C}$ contains no all-zero columns.'},
    'acs-q13b': {   'eq': '$$\\operatorname{rank}[\\lambda_i I - A \\quad B] = n \\quad (\\text{Controllability}), '
                          '\\qquad \\operatorname{rank}\\begin{bmatrix} \\lambda_i I - A \\\\ C \\end{bmatrix} = n '
                          '\\quad (\\text{Observability}) \\quad \\forall \\lambda_i \\in \\sigma(A)$$',
                    'text': 'The Popov-Belevitch-Hautus (PBH) test evaluates rank drop at each eigenvalue '
                            '$\\lambda_i$, identifying uncontrollable or unobservable modes directly without '
                            'coordinate transformations.'},
    'acs-q14': {   'eq': '$$K = \\begin{bmatrix} 0 & 0 & \\dots & 1 \\end{bmatrix} Q_c^{-1} \\phi_d(A), \\quad '
                         '\\text{where } \\phi_d(A) = A^n + \\alpha_{n-1} A^{n-1} + \\dots + \\alpha_0 I$$',
                   'text': "Ackermann's formula directly calculates the unique state feedback gain matrix $K$ that "
                           'places all closed-loop eigenvalues of $(A - BK)$ at desired locations, provided the '
                           'controllability matrix $Q_c$ has full rank $n$.'},
    'acs-q15': {   'eq': '$$\\dot{\\hat{x}} = A \\hat{x} + B u + L (y - C \\hat{x}), \\quad \\dot{e}(t) = (A - LC) '
                         'e(t), \\quad L = \\phi_d(A) Q_o^{-1} \\begin{bmatrix} 0 \\\\ \\vdots \\\\ 1 \\end{bmatrix}$$',
                   'text': 'A full-order Luenberger observer estimates internal states from measured outputs, with '
                           'error dynamics decaying asymptotically to zero when observer gain matrix $L$ stabilizes '
                           '$(A - LC)$.'},
    'acs-q16': {   'eq': '$$f(x_1 + x_2) \\ne f(x_1) + f(x_2), \\quad f(\\alpha x) \\ne \\alpha f(x) \\implies '
                         '\\text{Superposition Principle Fails}$$',
                   'text': '<strong>Distinct Non-Linear Physical Phenomena:</strong><br><strong>1. Limit '
                           'Cycles:</strong> Isolated, self-sustained closed periodic orbits in state space (stable or '
                           'unstable).<br><strong>2. Jump Resonance:</strong> Discontinuous jump in amplitude and '
                           'phase during continuous sinusoidal frequency sweeps.<br><strong>3. Subharmonics:</strong> '
                           'Generation of steady output responses at integer fractions ($f/2, f/3$) of input '
                           'frequency.<br><strong>4. Amplitude-Dependent Stability:</strong> System stability depends '
                           'on initial state or excitation amplitude, unlike linear systems.'},
    'acs-q16b': {   'eq': '$$N(X)_{\\text{ideal}} = \\frac{4M}{\\pi X}, \\qquad N(X)_{\\text{deadzone}} = '
                          '\\frac{4M}{\\pi X} \\sqrt{1 - \\left(\\frac{D}{X}\\right)^2} \\quad (X > D)$$',
                    'text': '<strong>1. Ideal Relay:</strong> Output switches between $+M$ and $-M$; describing '
                            'function $N(X) = \\frac{4M}{\\pi X}$ is pure real with zero phase shift ($\\angle N(X) = '
                            '0^\\circ$).<br><strong>2. Relay with Dead-Zone ($D$):</strong> Output is zero for input '
                            'amplitude $X \\le D$; for $X > D$, effective gain drops as amplitude increases with zero '
                            'phase shift.'},
    'acs-q17': {   'eq': '$$N(X) = \\frac{2k}{\\pi} \\left[ \\arcsin\\left(\\frac{S}{X}\\right) + \\frac{S}{X}\\sqrt{1 '
                         '- \\left(\\frac{S}{X}\\right)^2} \\right] \\quad (X \\ge S), \\qquad N(X) = k \\quad (X < '
                         'S)$$',
                   'text': 'For sinusoidal input exceeding saturation threshold $S$, the effective gain $N(X)$ drops '
                           'monotonically below slope $k$ as amplitude $X$ increases, introducing zero phase shift '
                           '($\\angle N(X) = 0^\\circ$).'},
    'acs-q17b': {   'eq': '$$N(X) = k \\left[ 1 - \\frac{2}{\\pi}\\arcsin\\left(\\frac{D}{X}\\right) - \\frac{2D}{\\pi '
                          'X}\\sqrt{1 - \\left(\\frac{D}{X}\\right)^2} \\right] \\quad (X > D), \\qquad N(X) = 0 '
                          '\\quad (X \\le D)$$',
                    'text': 'Dead-zone non-linearity produces zero output until input amplitude exceeds dead-band $D$, '
                            'beyond which the effective gain increases monotonically from 0 toward linear gain $k$ as '
                            '$X \\to \\infty$.'},
    'acs-q18': {   'eq': '$$G(j\\omega) = -\\frac{1}{N(X)} \\iff |G(j\\omega)| \\cdot |N(X)| = 1 \\quad \\text{and} '
                         '\\quad \\angle G(j\\omega) = -180^\\circ - \\angle N(X)$$',
                   'text': 'A sustained limit cycle occurs at the intersection of the linear plant Nyquist plot '
                           '$G(j\\omega)$ with the $-1/N(X)$ locus; the cycle is stable if increasing amplitude $X$ '
                           'moves the point into the stable region.'},
    'acs-q19': {   'eq': '$$\\frac{dx_2}{dx_1} = \\frac{f_2(x_1, x_2)}{f_1(x_1, x_2)} = \\frac{0}{0} \\quad \\text{at '
                         'equilibrium point } (x_1^*, x_2^*)$$',
                   'text': '<strong>Classification of Singular Points by Linearized '
                           'Eigenvalues:</strong><br><strong>1. Stable / Unstable Node:</strong> Real eigenvalues of '
                           'same sign ($\\lambda_1, \\lambda_2 \\in \\mathbb{R}, \\lambda_1\\lambda_2 > '
                           '0$).<br><strong>2. Saddle Point:</strong> Real eigenvalues of opposite sign ($\\lambda_1 > '
                           '0, \\lambda_2 < 0$) &mdash; <em>always unstable</em>!<br><strong>3. Stable / Unstable '
                           'Focus:</strong> Complex conjugate eigenvalues with real part ($\\sigma \\pm j\\omega, '
                           '\\sigma \\ne 0$).<br><strong>4. Center (Vortex):</strong> Purely imaginary conjugate '
                           'eigenvalues ($\\pm j\\omega, \\sigma = 0$) &mdash; closed concentric periodic orbits.'},
    'acs-q2': {   'eq': '$$x_1 = y, \\; x_2 = \\dot{y}, \\; \\dots, \\; x_n = y^{(n-1)} \\implies \\dot{x}_n = '
                        '-\\sum_{i=0}^{n-1} a_i x_{i+1} + b_0 u$$',
                  'text': '<strong>Phase Variables Definition:</strong> State variables defined as the output variable '
                          'and its successive $(n-1)$ time derivatives ($x_1=y, x_2=\\dot{y}, \\dots, '
                          'x_n=y^{(n-1)}$).<br><strong>Companion Form:</strong> Produces companion matrix $A$ having '
                          '1s along the first super-diagonal and negated differential equation coefficients $[-a_0, '
                          '-a_1, \\dots, -a_{n-1}]$ along the bottom row.'},
    'acs-q20': {   'eq': '$$V(x) = x^T P x > 0 \\quad (\\forall x \\ne 0) \\iff \\Delta_1 > 0, \\; \\Delta_2 > 0, \\; '
                         '\\dots, \\; \\Delta_n > 0$$',
                   'text': '<strong>Sylvester Criterion for Positive Definiteness:</strong> A real symmetric matrix $P '
                           '= P^T$ is positive definite if and only if all $n$ leading principal minors $\\Delta_k = '
                           '\\det(P_{k\\times k})$ are strictly positive ($\\Delta_1 > 0, \\Delta_2 > 0, \\dots, '
                           '\\Delta_n > 0$).<br><strong>Negative Definite:</strong> If and only if leading principal '
                           'minors alternate signs starting negative ($\\Delta_1 < 0, \\Delta_2 > 0, \\Delta_3 < 0, '
                           '\\dots$).'},
    'acs-q20b': {   'eq': '$$V(x) = f(x)^T P f(x), \\quad \\dot{V}(x) = f(x)^T (J^T P + P J) f(x) < 0 \\quad '
                          '\\text{where } J(x) = \\frac{\\partial f}{\\partial x}$$',
                    'text': "Krasovskii's method constructs a valid Lyapunov function directly from system vector "
                            'fields $f(x)$, guaranteeing asymptotic stability if the symmetric matrix $\\hat{F} = J^T '
                            'P + P J$ is negative definite.'},
    'acs-q21': {   'eq': '$$\\text{Slope } m = \\frac{dx_2}{dx_1} = \\frac{-x_1 - f(x_1, x_2)}{x_2} = N \\implies x_2 '
                         '= g(x_1, N) \\quad (\\text{Isocline Line})$$',
                   'text': 'The method of isoclines plots curves of constant trajectory slope $m = N$, drawing '
                           'direction tangents across each isocline to trace phase trajectories and locate isolated '
                           'limit cycles.'},
    'acs-q22': {   'eq': '$$A^T P + P A = -Q, \\quad V(x) = x^T P x > 0, \\quad \\dot{V}(x) = -x^T Q x < 0$$',
                   'text': "Lyapunov's direct theorem proves that a continuous LTI system $\\dot{x} = Ax$ is "
                           'asymptotically stable if and only if for any chosen symmetric positive definite matrix $Q '
                           '> 0$, the Lyapunov equation yields a unique symmetric positive definite matrix $P > 0$.'},
    'acs-q3': {   'eq': '$$\\dot{x}(t) = A x(t) + B u(t), \\quad y(t) = C x(t) + D u(t)$$',
                  'text': '<strong>Integrators:</strong> State variables $x_i(t)$ are strictly the physical outputs of '
                          'integrators ($1/s$), driven by derivative inputs $\\dot{x}_i(t)$.<br><strong>Matrix '
                          'Functions:</strong> Matrix $A$ ($n\\times n$) provides internal state feedback, $B$ '
                          '($n\\times m$) distributes external inputs, $C$ ($p\\times n$) observes states to outputs, '
                          'and $D$ ($p\\times m$) provides direct feedthrough.'},
    'acs-q4': {   'eq': '$$\\bar{A} = P^{-1} A P, \\quad \\bar{B} = P^{-1} B, \\quad \\bar{C} = C P, \\quad \\bar{D} = '
                        'D \\implies \\det(sI - \\bar{A}) = \\det(sI - A)$$',
                  'text': '<strong>Non-Uniqueness:</strong> Any non-singular similarity transformation $x = P z$ '
                          'creates an equivalent valid state space representation.<br><strong>System '
                          'Invariants:</strong> System eigenvalues (roots of $\\det(sI-A)=0$) and the transfer '
                          'function $G(s) = C(sI-A)^{-1}B + D$ remain strictly invariant under coordinate '
                          'transformations.'},
    'acs-q4b': {   'eq': '$$G(s) = \\frac{Y(s)}{U(s)} = C (sI - A)^{-1} B + D = \\frac{C \\operatorname{adj}(sI - A) '
                         'B}{\\det(sI - A)} + D$$',
                   'text': 'Applying Laplace transforms with zero initial conditions yields the transfer function '
                           '$G(s)$, whose denominator roots $\\det(sI - A) = 0$ directly define the invariant system '
                           'poles and eigenvalues.'},
    'acs-q5': {   'eq': '$$\\begin{bmatrix} \\dot{i}_L \\\\ \\dot{v}_C \\end{bmatrix} = \\begin{bmatrix} -R/L & -1/L '
                        '\\\\ 1/C & 0 \\end{bmatrix} \\begin{bmatrix} i_L \\\\ v_C \\end{bmatrix} + \\begin{bmatrix} '
                        '1/L \\\\ 0 \\end{bmatrix} v_{in}(t)$$',
                  'text': 'State variables in electrical networks are naturally selected as the energy-storage states: '
                          'inductor current $i_L(t)$ (magnetic energy) and capacitor voltage $v_C(t)$ (electrostatic '
                          'energy), governed by $v_L = L \\frac{di_L}{dt}$ and $i_C = C \\frac{dv_C}{dt}$.'},
    'acs-q6': {   'eq': '$$\\begin{bmatrix} \\frac{di_a}{dt} \\\\ \\frac{d\\omega}{dt} \\\\ \\frac{d\\theta}{dt} '
                        '\\end{bmatrix} = \\begin{bmatrix} -R_a/L_a & -K_b/L_a & 0 \\\\ K_t/J & -B/J & 0 \\\\ 0 & 1 & '
                        '0 \\end{bmatrix} \\begin{bmatrix} i_a \\\\ \\omega \\\\ \\theta \\end{bmatrix} + '
                        '\\begin{bmatrix} 1/L_a \\\\ 0 \\\\ 0 \\end{bmatrix} v_a(t)$$',
                  'text': 'An armature-controlled DC motor couples electrical armature dynamics ($v_a = R_a i_a + L_a '
                          '\\frac{di_a}{dt} + e_b$) to mechanical rotor dynamics ($T_e = K_t i_a = J \\dot{\\omega} + '
                          'B \\omega$), with back-EMF feedback $e_b = K_b \\omega$.'},
    'acs-q7': {   'eq': '$$\\Lambda = M^{-1} A M = \\operatorname{diag}(\\lambda_1, \\lambda_2, \\dots, \\lambda_n), '
                        '\\quad \\dot{z} = \\Lambda z + M^{-1} B u$$',
                  'text': 'Controllable canonical form organizes coefficients into a companion matrix for direct '
                          'pole-placement, whereas Diagonal (Jordan) canonical form decouples system modes using the '
                          'modal matrix of eigenvectors $M = [v_1 \\; v_2 \\; \\dots \\; v_n]$.'},
    'acs-q7b': {   'eq': '$$\\begin{bmatrix} \\frac{di_f}{dt} \\\\ \\frac{d\\omega}{dt} \\end{bmatrix} = '
                         '\\begin{bmatrix} -R_f/L_f & 0 \\\\ K_{tf}/J & -B/J \\end{bmatrix} \\begin{bmatrix} i_f \\\\ '
                         '\\omega \\end{bmatrix} + \\begin{bmatrix} 1/L_f \\\\ 0 \\end{bmatrix} v_f(t)$$',
                   'text': 'In field-controlled DC motors, armature current $I_a$ is held constant so torque $T_e = '
                           'K_{tf} i_f$ is linearly driven by field current, completely eliminating back-EMF feedback '
                           'into the electrical circuit.'},
    'acs-q8': {   'eq': '$$x(t) = \\mathcal{L}^{-1}\\{(sI - A)^{-1}\\} x(0) = e^{At} x(0) = \\Phi(t) x(0)$$',
                  'text': 'The unforced (autonomous) state trajectory represents the Zero-Input Response (ZIR), '
                          'computed by taking the inverse Laplace transform of the resolvent matrix $\\Phi(s) = (sI - '
                          'A)^{-1}$ multiplied by initial condition vector $x(0)$.'},
    'acs-q9': {   'eq': '$$\\Phi(t) = e^{At} = \\mathcal{L}^{-1}\\{(sI - A)^{-1}\\} = \\sum_{k=0}^{\\infty} \\frac{A^k '
                        't^k}{k!}$$',
                  'text': '<strong>Key Properties of State Transition Matrix:</strong><br><strong>1. '
                          'Identity:</strong> $\\Phi(0) = e^0 = I$<br><strong>2. Inverse / Time Reversal:</strong> '
                          '$\\Phi^{-1}(t) = \\Phi(-t)$<br><strong>3. Group Property:</strong> $\\Phi(t_1 + t_2) = '
                          '\\Phi(t_1)\\Phi(t_2)$<br><strong>4. Power Property:</strong> $[\\Phi(t)]^k = '
                          '\\Phi(kt)$<br><strong>5. Derivative:</strong> $\\dot{\\Phi}(t) = A \\Phi(t) = \\Phi(t) A$'},
    'acs-q9b': {   'eq': '$$x(k+1) = G x(k) + H u(k), \\quad G = e^{AT}, \\quad H = \\left(\\int_0^T e^{A\\tau} '
                         'd\\tau\\right) B, \\quad G(z) = C (zI - G)^{-1} H + D$$',
                   'text': 'Discrete-time state equations discretized over sampling period $T$ with Zero-Order Hold '
                           '(ZOH) are stable if and only if all eigenvalues of matrix $G$ lie strictly inside the unit '
                           'circle $|\\lambda_i| < 1$.'},
    'beee-q1': {   'eq': '$$\\sum I_{\\text{in}} = \\sum I_{\\text{out}}, \\quad \\sum_{k=1}^m V_k = 0$$',
                   'text': '<strong>Kirchhoff’s Current Law (KCL):</strong> Conservation of electric charge; algebraic '
                           'sum of currents entering and leaving any node is zero ($\\sum I = '
                           '0$).<br><strong>Kirchhoff’s Voltage Law (KVL):</strong> Conservation of energy; algebraic '
                           'sum of potential rises and drops around any closed loop is zero ($\\sum V = 0$).'},
    'beee-q10': {   'eq': '$$\\mathcal{F} = N I, \\quad \\Phi = \\frac{\\mathcal{F}}{S}, \\quad S = \\frac{l}{\\mu_0 '
                          '\\mu_r A}, \\quad B = \\mu H = \\mu_0 \\mu_r H, \\quad W_h = \\eta B_{\\max}^{1.6} f$$',
                    'text': '<strong>Magnetic Circuits:</strong> MMF ($\\mathcal{F} = NI$ in AT) drives flux ($\\Phi = '
                            '\\mathcal{F}/S$ in Wb) against reluctance ($S = \\frac{l}{\\mu A}$). Electric-magnetic '
                            'analogy: EMF $\\leftrightarrow$ MMF, Current $\\leftrightarrow$ Flux, Resistance '
                            '$\\leftrightarrow$ Reluctance. Hysteresis loop area represents Steinmetz core energy '
                            'loss.'},
    'beee-q11': {   'eq': '$$E_1 = 4.44 f N_1 \\Phi_m, \\quad K = \\frac{E_2}{E_1} = \\frac{N_2}{N_1}, \\quad \\eta = '
                          '\\frac{x S \\cos\\phi_2}{x S \\cos\\phi_2 + W_i + x^2 W_{cu(FL)}}, \\quad W_{cu} = W_i \\ '
                          '(\\eta_{\\max})$$',
                    'text': '<strong>Transformer EMF Equation:</strong> Derived from mutual induction $e = -N '
                            '\\frac{d\\Phi}{dt}$, yielding RMS $E = 4.44 f N \\Phi_m$.<br><strong>Condition for '
                            'Maximum Efficiency:</strong> Variable copper loss equals constant iron loss ($W_{cu} = '
                            'W_i$), occurring at fraction $x_m = \\sqrt{W_i / W_{cu(FL)}}$.'},
    'beee-q12': {   'eq': '$$E_g = \\frac{\\Phi Z N P}{60 A}, \\quad A = P \\ (\\text{Lap Winding}), \\quad A = 2 \\ '
                          '(\\text{Wave Winding})$$',
                    'text': '<strong>DC Generator EMF Equation:</strong> Generated voltage $E_g = \\frac{\\Phi Z N '
                            'P}{60 A}$. Conductor cuts total flux $P\\Phi$ in $60/N$ seconds; $Z/A$ conductors in '
                            'series per path. Commutator acts as a mechanical rectifier converting internal AC EMF '
                            'into external DC.'},
    'beee-q13': {   'eq': '$$V = E_b + I_a R_a, \\quad E_b = \\frac{\\Phi Z N P}{60 A}, \\quad T_a = 0.159 '
                          '\\left(\\frac{P Z}{A}\\right)\\Phi I_a \\propto \\Phi I_a, \\quad N \\propto '
                          '\\frac{E_b}{\\Phi}$$',
                    'text': '<strong>DC Motor Operation:</strong> Conductor force $F = B I l$ (Fleming’s Left-Hand '
                            'Rule).<br><strong>Back-EMF ($E_b$):</strong> Acts as an automatic governor regulating '
                            'armature current $I_a = (V - E_b)/R_a$. Massive starting current requires starters. '
                            'Armature torque $T_a \\propto \\Phi I_a$; speed $N \\propto E_b / \\Phi$.'},
    'beee-q14': {   'eq': '$$\\text{Star: } V_L = \\sqrt{3} V_{ph}, \\; I_L = I_{ph}; \\quad \\text{Delta: } V_L = '
                          'V_{ph}, \\; I_L = \\sqrt{3} I_{ph}; \\quad P = \\sqrt{3} V_L I_L \\cos\\phi$$',
                    'text': '<strong>Balanced 3-Phase Systems:</strong> Star provides neutral point with $V_L = '
                            '\\sqrt{3} V_{ph}$; Delta provides closed mesh with $I_L = \\sqrt{3} I_{ph}$. Total active '
                            'power in both configurations is universally $P = \\sqrt{3} V_L I_L \\cos\\phi\\text{ W}$, '
                            'and reactive power is $Q = \\sqrt{3} V_L I_L \\sin\\phi\\text{ VAR}$.'},
    'beee-q15': {   'eq': '$$I_{\\text{residual}} = |I_L - I_N| > 30\\text{ mA} \\implies \\text{Trip}, \\quad '
                          'R_{\\text{earth}} < 5\\,\\Omega \\ (\\text{Domestic})$$',
                    'text': '<strong>Wiring & Protection:</strong> Staircase wiring controls one lamp via two SPDT '
                            'switches. Earthing (pipe/plate) diverts dangerous fault currents, keeping touch potential '
                            'safe. MCB provides thermal overload and magnetic short-circuit protection; ELCB/RCCB '
                            'senses core-balance current imbalance $> 30\\text{ mA}$ to prevent electrocution.'},
    'beee-q16': {   'eq': '$$I = I_0 \\left(e^{\\frac{V}{\\eta V_T}} - 1\\right), \\quad V_T = \\frac{k T}{q} \\approx '
                          '26\\text{ mV}, \\quad r_d = \\frac{\\eta V_T}{I_F} \\approx \\frac{26\\text{ '
                          'mV}}{I_F\\text{ (mA)}}$$',
                    'text': '<strong>PN Junction Diode:</strong> Depletion region uncovers immobile ions creating '
                            'barrier potential ($0.7\\text{ V}$ for Si). Forward bias narrows depletion width, '
                            'triggering exponential diffusion current (Shockley equation). Dynamic resistance $r_d '
                            '\\approx 26 / I_F\\text{ mA}$.'},
    'beee-q17': {   'eq': '$$\\text{HWR: } V_{dc} = \\frac{V_m}{\\pi}, \\eta = 40.6\\%, \\gamma = 1.21; \\quad '
                          '\\text{FWR: } V_{dc} = \\frac{2 V_m}{\\pi}, \\eta = 81.2\\%, \\gamma = 0.482, \\gamma_{cap} '
                          '\\approx \\frac{1}{4\\sqrt{3} f C R_L}$$',
                    'text': '<strong>Rectifiers:</strong> Full-wave bridge rectifier utilizes four diodes in bridge '
                            'configuration, doubling DC voltage ($2 V_m / \\pi$) and efficiency ($81.2\\%$) compared '
                            'to half-wave ($40.6\\%$), with lower ripple factor ($\\gamma = 0.482$). Shunt capacitor '
                            'filter smooths ripple via $R_L C$ discharge.'},
    'beee-q18': {   'eq': '$$V_L = V_Z, \\quad I_s = I_Z + I_L = \\frac{V_{in} - V_Z}{R_s}, \\quad R_{s\\max} = '
                          '\\frac{V_{in(\\min)} - V_Z}{I_{L(\\max)} + I_{Z\\min}}$$',
                    'text': '<strong>Zener Diode Regulator:</strong> Operates in reverse breakdown ($V_Z$). Zener '
                            'breakdown ($< 5\\text{ V}$, field ionization, negative temp-co); Avalanche breakdown ($> '
                            '6\\text{ V}$, impact ionization, positive temp-co). Shunts excess current through Zener, '
                            'maintaining stable output voltage across line and load variations.'},
    'beee-q19': {   'eq': '$$I_E = I_B + I_C, \\quad I_C = \\beta I_B + I_{CEO}, \\quad \\beta = \\frac{\\alpha}{1 - '
                          '\\alpha}, \\quad \\alpha = \\frac{\\beta}{1 + \\beta}$$',
                    'text': '<strong>BJT Characteristics:</strong> Emitter heavily doped, base thin and lightly doped, '
                            'collector large. CE configuration provides high current gain ($\\beta = '
                            '\\frac{\\alpha}{1-\\alpha} \\sim 100$) and power gain. Active region (EBJ forward, CBJ '
                            'reverse) for amplification; Cut-off and Saturation for digital switching.'},
    'beee-q2': {   'eq': '$$V_1 - V_2 = V_s, \\quad \\sum I_{\\text{supernode}} = 0$$',
                   'text': '<strong>Supernode:</strong> Formed when an ideal voltage source is connected between two '
                           'non-reference nodes. Replace the source branch with an enclosed boundary and apply KCL to '
                           'the combined supernode, augmented by the source constraint equation ($V_1 - V_2 = V_s$).'},
    'beee-q20': {   'eq': '$$I_B \\ge \\frac{I_{C(sat)}}{\\beta_{\\min}}, \\quad A_v = \\frac{v_{out}}{v_{in}} '
                          "\\approx -\\frac{R_C \\parallel R_L}{r_e'}, \\quad \\phi = 180^\\circ$$",
                    'text': '<strong>Transistor Applications:</strong> BJT as switch: OFF in cut-off ($V_{out} = '
                            'V_{CC}$), ON in saturation ($V_{out} \\approx 0.2\\text{ V}$). Single-stage CE amplifier: '
                            'Voltage divider bias stabilizes Q-point; bypass capacitor $C_E$ maximizes AC gain; output '
                            'voltage exhibits an exact $180^\\circ$ phase inversion.'},
    'beee-q21': {   'eq': '$$V_+ = V_- \\ (\\text{Virtual Short}), \\quad I_+ = I_- = 0\\text{ A}, \\quad A_{OL} = '
                          '\\infty, \\; R_{in} = \\infty, \\; R_{out} = 0, \\; CMRR = \\infty$$',
                    'text': '<strong>Ideal Op-Amp & Virtual Ground:</strong> Infinite open-loop gain ($A_{OL} \\to '
                            '\\infty$) with negative feedback forces differential input voltage $V_d = V_+ - V_- = 0$, '
                            'establishing a virtual short. Infinite input impedance ensures zero terminal input '
                            'current ($I_+ = I_- = 0$). Grounding non-inverting terminal creates a virtual ground at '
                            'inverting node.'},
    'beee-q22': {   'eq': '$$A_{v(inv)} = -\\frac{R_f}{R_1}, \\quad A_{v(non-inv)} = 1 + \\frac{R_f}{R_1}, \\quad '
                          'A_{v(buffer)} = 1.0, \\quad Z_{in(buffer)} \\approx \\infty, \\; Z_{out(buffer)} \\approx '
                          '0$$',
                    'text': '<strong>Op-Amp Configurations:</strong> Inverting amplifier provides stabilized gain $A_v '
                            '= -R_f/R_1$ with $180^\\circ$ phase inversion. Non-inverting amplifier provides in-phase '
                            'gain $A_v = 1 + R_f/R_1 \\ge 1$ with ultra-high input impedance. Voltage follower '
                            '($R_f=0$) provides unity gain for impedance buffer isolation.'},
    'beee-q23': {   'eq': '$$V_{out} = -\\left[\\frac{R_f}{R_1}V_1 + \\frac{R_f}{R_2}V_2\\right], \\quad V_{out(int)} '
                          '= -\\frac{1}{RC}\\int V_{in}\\,dt, \\quad V_{out(diff)} = -RC \\frac{dV_{in}}{dt}$$',
                    'text': '<strong>Mathematical Op-Amp Circuits:</strong> Summing amplifier adds input signals with '
                            'weighted gains. Difference amplifier subtracts common-mode noise. Integrator (feedback '
                            'capacitor $C$) ramps output proportional to input integral. Differentiator (input '
                            'capacitor $C$) differentiates input rate of change.'},
    'beee-q24': {   'eq': '$$A - B = A + (\\text{2’s complement of } B), \\quad \\text{2’s Comp} = \\text{1’s Comp} + '
                          '1, \\quad \\text{Range: } -2^{n-1} \\le N \\le +2^{n-1}-1$$',
                    'text': '<strong>2’s Complement Arithmetic:</strong> Subtraction $A - B$ executed by adding 2’s '
                            'complement of $B$ to $A$. An end carry signifies a positive answer (discard end carry). '
                            'Absence of end carry indicates negative answer in 2’s complement form (take 2’s '
                            'complement of sum to obtain true magnitude).'},
    'beee-q25': {   'eq': '$$\\overline{A \\cdot B} = \\bar{A} + \\bar{B}, \\quad \\overline{A + B} = \\bar{A} \\cdot '
                          '\\bar{B}, \\quad A \\oplus B = \\bar{A} B + A \\bar{B}, \\quad \\text{NAND/NOR: '
                          'Universal}$$',
                    'text': '<strong>Universal Gates & De Morgan’s Laws:</strong> Any logic function can be realized '
                            'using solely NAND gates or solely NOR gates. De Morgan’s first law: NAND is equivalent to '
                            'bubbled OR ($\\overline{AB} = \\bar{A}+\\bar{B}$). De Morgan’s second law: NOR is '
                            'equivalent to bubbled AND ($\\overline{A+B} = \\bar{A}\\bar{B}$).'},
    'beee-q26': {   'eq': '$$\\text{HA: } S = A \\oplus B, C = AB; \\quad \\text{FA: } S = A \\oplus B \\oplus C_{in}, '
                          'C_{out} = AB + C_{in}(A \\oplus B)$$',
                    'text': '<strong>Arithmetic Adders:</strong> Half Adder computes sum and carry of two bits using '
                            'one XOR gate and one AND gate. Full Adder computes sum and carry of three bits ($A, B, '
                            'C_{in}$), synthesized using two half adders and one OR gate ($S = A \\oplus B \\oplus '
                            'C_{in}$, $C_{out} = AB + C_{in}(A \\oplus B)$).'},
    'beee-q3': {   'eq': "$$I_L = I_L' + I_L'' + I_L''' + \\dots = \\sum_{k=1}^n I_L^{(k)}$$",
                   'text': '<strong>Superposition Theorem:</strong> In any linear bilateral network with multiple '
                           'independent sources, the response in any branch is the algebraic sum of responses caused '
                           'by each independent source acting alone, with all other voltage sources shorted ($V=0$) '
                           'and current sources opened ($I=0$). Does not apply directly to power.'},
    'beee-q4': {   'eq': '$$V_{th} = V_{oc}, \\quad R_{th} = R_N, \\quad I_N = \\frac{V_{th}}{R_{th}}, \\quad I_L = '
                         '\\frac{V_{th}}{R_{th} + R_L} = I_N \\left(\\frac{R_N}{R_N + R_L}\\right)$$',
                   'text': '<strong>Thevenin’s Theorem:</strong> Replaces network across load terminals with '
                           'open-circuit voltage $V_{th}$ in series with $R_{th}$.<br><strong>Norton’s '
                           'Theorem:</strong> Replaces network with short-circuit current $I_N$ in parallel with $R_N '
                           '= R_{th}$. Dual relationship: $V_{th} = I_N R_{th}$.'},
    'beee-q5': {   'eq': '$$R_L = R_{th} \\implies P_{\\max} = \\frac{V_{th}^2}{4 R_{th}}, \\quad \\eta = '
                         '\\frac{P_L}{P_{total}} \\times 100\\% = 50\\%$$',
                   'text': '<strong>Maximum Power Transfer Theorem:</strong> Maximum power is delivered to a load when '
                           '$R_L = R_{th}$, resulting in $P_{\\max} = \\frac{V_{th}^2}{4 R_{th}}$. The transmission '
                           'efficiency at maximum power transfer is strictly $50\\%$, with the remaining $50\\%$ '
                           'dissipated as heat in internal resistance.'},
    'beee-q6': {   'eq': '$$v(t) = V_m \\sin(\\omega t \\pm \\phi), \\quad \\omega = 2\\pi f = \\frac{2\\pi}{T}, '
                         '\\quad \\mathbf{V} = V_{rms}\\angle \\phi$$',
                   'text': '<strong>Sinusoidal AC Generation:</strong> Derived from Faraday’s law $e(t) = -N '
                           '\\frac{d\\Phi}{dt} = N B A \\omega \\sin(\\omega t)$ for a coil rotating in a uniform '
                           'magnetic field.<br><strong>Phasor:</strong> Directed vector rotating counterclockwise at '
                           'angular velocity $\\omega$, representing RMS magnitude and phase angle in the complex '
                           'plane.'},
    'beee-q7': {   'eq': '$$V_{rms} = \\frac{V_m}{\\sqrt{2}} \\approx 0.707 V_m, \\quad V_{avg} = \\frac{2 V_m}{\\pi} '
                         '\\approx 0.637 V_m, \\quad K_f = \\frac{V_{rms}}{V_{avg}} = 1.11, \\quad K_p = '
                         '\\frac{V_m}{V_{rms}} = \\sqrt{2} \\approx 1.414$$',
                   'text': '<strong>RMS Value:</strong> Equivalent DC heating value ($V_m / '
                           '\\sqrt{2}$).<br><strong>Average Value:</strong> Half-cycle arithmetic mean ($2 V_m / '
                           '\\pi$).<br><strong>Form Factor:</strong> $K_f = 1.11$ for pure sine wave.<br><strong>Peak '
                           'Factor:</strong> $K_p = 1.414$, governing dielectric insulation withstand limits.'},
    'beee-q8': {   'eq': '$$\\mathbf{Z} = R + j(X_L - X_C), \\quad P = V I \\cos\\phi, \\quad Q = V I \\sin\\phi, '
                         '\\quad S = V I = \\sqrt{P^2 + Q^2}, \\quad pf = \\cos\\phi = \\frac{R}{|\\mathbf{Z}|}$$',
                   'text': '<strong>Series R-L:</strong> Current lags voltage by $\\phi = \\tan^{-1}(X_L/R)$, lagging '
                           'power factor.<br><strong>Series R-C:</strong> Current leads voltage by $\\phi = '
                           '\\tan^{-1}(X_C/R)$, leading power factor.<br><strong>Power Triangle:</strong> Real active '
                           'power $P$ (Watts), reactive power $Q$ (VAR), apparent power $S$ (VA).'},
    'beee-q9': {   'eq': '$$f_r = \\frac{1}{2\\pi\\sqrt{LC}}, \\quad |\\mathbf{Z}_r| = R, \\quad I_0 = \\frac{V}{R}, '
                         '\\quad Q = \\frac{1}{R}\\sqrt{\\frac{L}{C}}, \\quad BW = f_2 - f_1 = \\frac{f_r}{Q} = '
                         '\\frac{R}{2\\pi L}$$',
                   'text': '<strong>Series Resonance:</strong> Occurs when $X_L = X_C$, giving purely resistive '
                           'minimum impedance $|\\mathbf{Z}| = R$, maximum in-phase current ($pf = 1.0$), and voltage '
                           'magnification across $L$ and $C$ ($V_L = V_C = Q \\cdot V$). Narrow bandwidth indicates '
                           'high selectivity.'},
    'comp-q1': {   'eq': '$$R_L = R_{th}, \\quad P_{max} = \\frac{V_{th}^2}{4 R_{th}}, \\quad \\mathbf{Z}_L = '
                         '\\mathbf{Z}_{th}^* = R_{th} - jX_{th}, \\quad \\eta = 50\\%$$',
                   'text': '<strong>Maximum Power Transfer:</strong> In DC circuits, maximum power is delivered when '
                           '$R_L = R_{th}$ with $\\eta = 50\\%$. In AC circuits with complex load impedance, maximum '
                           'active power occurs under conjugate match $\\mathbf{Z}_L = \\mathbf{Z}_{th}^*$, '
                           'eliminating net loop reactance.'},
    'comp-q10': {   'eq': '$$E_{ph} = 4.44 k_p k_d f \\Phi T_{ph}, \\quad P = \\frac{E_0 V}{X_d}\\sin\\delta + '
                          '\\frac{V^2}{2}\\left(\\frac{1}{X_q} - \\frac{1}{X_d}\\right)\\sin 2\\delta$$',
                    'text': '<strong>Synchronous Machines:</strong> EMF method is pessimistic; MMF method is '
                            'optimistic. Two-reaction theory resolves salient-pole armature currents into $d$ and $q$ '
                            'axis components ($X_d > X_q$), producing reluctance torque proportional to $\\sin '
                            '2\\delta$.'},
    'comp-q11': {   'eq': '$$I_{a1} = \\frac{E_a}{Z_1 + Z_2 + Z_0 + 3Z_f} \\ (\\text{SLG}), \\quad '
                          '\\frac{2H}{\\omega_s}\\frac{d^2\\delta}{dt^2} = P_m - P_e, \\quad '
                          '\\int_{\\delta_0}^{\\delta_{cr}}(P_m - P_e)d\\delta = '
                          '\\int_{\\delta_{cr}}^{\\delta_{max}}(P_e - P_m)d\\delta$$',
                    'text': '<strong>Power Systems & Stability:</strong> Fortescue symmetrical components resolve '
                            'unsymmetrical faults (SLG: sequence networks in series). Swing equation governs '
                            'electromechanical dynamics. Equal Area Criterion determines critical clearing angle '
                            '$\\delta_{cr}$ without step integration.'},
    'comp-q12': {   'eq': '$$T(s) = \\frac{C(s)}{R(s)} = \\frac{\\sum_{k=1}^N P_k \\Delta_k}{\\Delta}, \\quad \\Delta '
                          '= 1 - \\sum L_1 + \\sum L_2 - \\sum L_3 + \\dots$$',
                    'text': "<strong>Transfer Function & Mason\\'s Rule:</strong> Block diagram algebra simplifies "
                            "interconnected systems. Mason\\'s gain formula evaluates closed-loop transfer functions "
                            'directly by determining forward paths $P_k$, loops $L_i$, and non-touching loop '
                            'determinants $\\Delta, \\Delta_k$.'},
    'comp-q13': {   'eq': '$$t_p = \\frac{\\pi}{\\omega_n\\sqrt{1-\\zeta^2}}, \\quad M_p = '
                          'e^{-\\frac{\\pi\\zeta}{\\sqrt{1-\\zeta^2}}}\\times 100\\%, \\quad t_s(2\\%) = '
                          '\\frac{4}{\\zeta\\omega_n}, \\quad e_{ss} = \\lim_{s\\to 0}\\frac{s R(s)}{1 + G(s)}$$',
                    'text': '<strong>Second-Order Time Specifications:</strong> Damping ratio $\\zeta$ dictates '
                            'maximum overshoot $M_p$ and transient oscillations. Settling time is $t_s \\approx '
                            '4/(\\zeta\\omega_n)$. Steady-state error depends on system type number and static error '
                            'constants ($K_p, K_v, K_a$).'},
    'comp-q14': {   'eq': '$$b_1 = \\frac{a_1 a_2 - a_0 a_3}{a_1}, \\quad \\angle G(s)H(s) = \\pm (2k+1)180^\\circ, '
                          '\\quad \\sigma_A = \\frac{\\sum P_i - \\sum Z_j}{P - Z}, \\quad \\frac{dK}{ds} = 0$$',
                    'text': '<strong>s-Domain Stability:</strong> Routh-Hurwitz criterion determines RHP roots from '
                            'sign changes in column 1. Root locus plots closed-loop pole trajectories as gain $K: 0 '
                            '\\to \\infty$; breakaway points satisfy $dK/ds = 0$ and asymptotes emanate from centroid '
                            '$\\sigma_A$.'},
    'comp-q15': {   'eq': '$$GM = -20\\log_{10}|G(j\\omega_{pc})|, \\quad PM = 180^\\circ + \\angle G(j\\omega_{gc}), '
                          '\\quad N = Z - P \\implies Z = N + P = 0$$',
                    'text': '<strong>Bode & Nyquist Stability:</strong> Bode plots provide gain margin ($GM$) and '
                            'phase margin ($PM$). Nyquist criterion maps the s-plane boundary around critical point '
                            '$(-1 + j0)$; closed-loop stability requires counter-clockwise encirclements equal to '
                            'open-loop RHP poles ($N = -P$).'},
    'comp-q16': {   'eq': '$$\\mathbf{\\dot{x}} = \\mathbf{A}\\mathbf{x} + \\mathbf{B}\\mathbf{u}, \\ '
                          '\\mathbf{\\Phi}(t) = e^{\\mathbf{A}t}, \\ \\text{rank}[\\mathbf{B} \\ \\mathbf{AB} \\dots] '
                          '= n, \\ L_x = R_2 R_3 C_4, \\ C_x = C_3 \\frac{R_4}{R_2}$$',
                    'text': '<strong>Modern Control & Bridges:</strong> State transition matrix $\\mathbf{\\Phi}(t) = '
                            '\\mathcal{L}^{-1}\\{(s\\mathbf{I}-\\mathbf{A})^{-1}\\}$. Kalman tests verify '
                            'controllability and observability. Maxwell-Wien bridge measures inductance; Schering '
                            'bridge measures capacitance and $\\tan\\delta$. CT secondaries must never be '
                            'open-circuited.'},
    'comp-q17': {   'eq': '$$V_{dc} = \\frac{2V_m}{\\pi}, \\ \\gamma = \\sqrt{\\left(\\frac{I_{rms}}{I_{dc}}\\right)^2 '
                          '- 1} = 0.482, \\ \\eta = 81.2\\%, \\ \\Delta V_r = \\frac{V_m}{2 f R_L C}, \\ R_s = '
                          '\\frac{V_{in} - V_Z}{I_Z + I_L}$$',
                    'text': '<strong>Rectifiers & Regulators:</strong> Full-wave bridge rectifier yields $V_{dc} = '
                            '2V_m/\\pi$, ripple factor $\\gamma = 0.482$, and efficiency $\\eta = 81.2\\%$. C-filter '
                            'smooths output voltage. Zener diode stabilizes load voltage across varying input voltages '
                            'and load currents.'},
    'comp-q18': {   'eq': '$$S = (1 + \\beta)\\frac{1 + R_{th}/R_E}{1 + \\beta + R_{th}/R_E}, \\quad A_v = -\\frac{R_C '
                          '\\parallel R_L}{r_e}, \\quad C_{M} = C_\\mu(1 + |A_v|)$$',
                    'text': '<strong>BJT Amplifiers:</strong> Voltage divider bias minimizes stability factor $S \\to '
                            '1$, preventing thermal runaway. Small-signal CE gain is $A_v = -g_m (R_C \\parallel R_L)$ '
                            'with $180^\\circ$ phase inversion. High-frequency roll-off is dominated by Miller effect '
                            'multiplication of $C_\\mu$.'},
    'comp-q19': {   'eq': '$$A_{v,inv} = -\\frac{R_f}{R_1}, \\quad A_{v,non} = 1 + \\frac{R_f}{R_1}, \\quad V_o = '
                          '\\left(1 + \\frac{2 R_1}{R_{gain}}\\right)\\left(\\frac{R_3}{R_2}\\right)(V_2 - V_1)$$',
                    'text': '<strong>Operational Amplifiers:</strong> Virtual short ($V^+ = V^-$) and zero input '
                            'current govern Op-Amp analysis. Practical integrators use feedback resistance $R_f$ to '
                            'prevent DC saturation. 3-Op-Amp instrumentation amplifier offers high CMRR, high input '
                            'impedance, and single resistor gain tuning.'},
    'comp-q2': {   'eq': '$$i(t) = \\frac{V_s}{R}(1 - e^{-t/\\tau}), \\ \\tau = \\frac{L}{R} \\text{ or } RC, \\quad '
                         's^2 + 2\\zeta\\omega_n s + \\omega_n^2 = 0, \\ \\zeta = \\frac{R}{2}\\sqrt{\\frac{C}{L}}$$',
                   'text': '<strong>RL, RC, RLC Transients:</strong> First-order time constants are $\\tau = L/R$ and '
                           '$\\tau = RC$. Second-order RLC circuit yields overdamped ($\\zeta > 1$), critically damped '
                           '($\\zeta = 1$), and underdamped oscillatory ($\\zeta < 1$) responses with $\\omega_d = '
                           '\\omega_n\\sqrt{1-\\zeta^2}$.'},
    'comp-q20': {   'eq': '$$t_H = 0.693(R_A + R_B)C, \\quad t_L = 0.693 R_B C, \\quad f = \\frac{1.44}{(R_A + 2 '
                          'R_B)C}, \\quad T_{mono} = 1.1 R_A C$$',
                    'text': '<strong>IC 555 Timer:</strong> Internal comparators switch at $(1/3)V_{CC}$ and '
                            '$(2/3)V_{CC}$. Astable multivibrator oscillates at $f = 1.44/((R_A + 2R_B)C)$ with duty '
                            'cycle $> 50\\%$. Monostable multivibrator generates one-shot pulses of duration $T = 1.1 '
                            'R_A C$.'},
    'comp-q21': {   'eq': '$$\\overline{A + B} = \\bar{A}\\bar{B}, \\ \\overline{A B} = \\bar{A} + \\bar{B}, \\ S = A '
                          '\\oplus B \\oplus C_{in}, \\ Q_{next} = J\\bar{Q} + \\bar{K}Q, \\ J_2 = K_2 = Q_1 Q_0$$',
                    'text': "<strong>Digital Logic & Counters:</strong> De Morgan\\'s laws simplify Boolean logic. "
                            'Full adders use $S = A\\oplus B\\oplus C_{in}$ and $C_{out} = AB + C_{in}(A\\oplus B)$. '
                            'Master-Slave JK flip-flops eliminate race-around conditions. Synchronous binary counter '
                            'design uses flip-flop excitation tables.'},
    'comp-q22': {   'eq': '$$I_A = \\frac{\\alpha_2 I_g + I_{CBO1} + I_{CBO2}}{1 - (\\alpha_1 + \\alpha_2)}, \\quad '
                          'I_L > I_H, \\quad \\text{MOSFET: } R_{DS(on)} \\propto T, \\quad \\text{IGBT: } V_{CE(sat)} '
                          '\\approx 1.5-2.5\\text{ V}$$',
                    'text': '<strong>Power Semiconductor Devices:</strong> SCR turns on regeneratively when loop gain '
                            '$(\\alpha_1 + \\alpha_2) \\to 1$. Latching current $I_L > I_H$. Power MOSFET provides '
                            'ultra-fast switching with positive temperature coefficient. IGBT combines MOS voltage '
                            'gate drive with bipolar low on-state drop.'},
    'comp-q23': {   'eq': '$$V_{dc,1\\phi} = \\frac{2 V_m}{\\pi}\\cos\\alpha, \\quad V_{dc,3\\phi} = \\frac{3 '
                          'V_{mL}}{\\pi}\\cos\\alpha = \\frac{3\\sqrt{3}V_m}{\\pi}\\cos\\alpha, \\quad \\alpha > '
                          '90^\\circ \\implies \\text{Inversion}$$',
                    'text': '<strong>Controlled Rectifiers:</strong> Fully controlled 1-phase bridge gives $V_{dc} = '
                            '(2V_m/\\pi)\\cos\\alpha$; 3-phase 6-pulse bridge gives $V_{dc} = '
                            '(3V_{mL}/\\pi)\\cos\\alpha$. Operating at $\\alpha > 90^\\circ$ enables line-commutated '
                            'synchronous inversion. Freewheeling diode prevents negative voltage spikes.'},
    'comp-q24': {   'eq': '$$V_o = D V_s \\ (\\text{Buck}), \\quad V_o = \\frac{V_s}{1 - D} \\ (\\text{Boost}), \\quad '
                          'V_o = -\\frac{D}{1 - D}V_s \\ (\\text{Buck-Boost}), \\quad \\langle v_L \\rangle = 0$$',
                    'text': '<strong>DC-DC Converters:</strong> Steady-state operation is governed by inductor '
                            'volt-second balance ($\\langle v_L \\rangle = 0$) and capacitor charge balance ($\\langle '
                            'i_C \\rangle = 0$). Buck steps down ($D$), Boost steps up ($1/(1-D)$), and Buck-Boost '
                            'inverts and scales ($D/(1-D)$).`'},
    'comp-q25': {   'eq': '$$V_{L1,rms}^{180^\\circ} = \\frac{\\sqrt{6}}{\\pi}V_{dc} \\approx 0.78 V_{dc}, \\quad '
                          'V_{L,rms}^{120^\\circ} = \\frac{V_{dc}}{\\sqrt{2}}, \\quad m_a = \\frac{V_m}{V_c}, \\quad '
                          'V_{L1,rms} \\approx 0.612 m_a V_{dc}$$',
                    'text': '<strong>Inverters & SPWM:</strong> 3-phase VSI operating in $180^\\circ$ conduction mode '
                            'yields 6-step staircase phase voltages; $120^\\circ$ mode provides $60^\\circ$ deadband '
                            'preventing shoot-through. Sinusoidal PWM compares sine reference with triangular carrier, '
                            'shifting harmonics to carrier sidebands.'},
    'comp-q26': {   'eq': '$$T_e - T_L = J\\frac{d\\omega_m}{dt} + B\\omega_m, \\quad \\omega_m = '
                          '\\frac{V_a}{K_a\\Phi} - \\frac{R_a}{(K_a\\Phi)^2}T_e, \\quad \\frac{V}{f} = \\text{const} '
                          '\\implies T_{max} = \\text{const}$$',
                    'text': '<strong>Electric Drives & Braking:</strong> 4-quadrant plane governs motoring and '
                            'braking. DC drives vary armature voltage via phase converters. $V/f$ constant '
                            'volts-per-hertz maintains rated induction motor flux and maximum torque. Electrical '
                            'braking includes regenerative, dynamic, and plugging.'},
    'comp-q3': {   'eq': '$$\\omega_0 = \\frac{1}{\\sqrt{LC}}, \\quad Q = \\frac{\\omega_0 L}{R} = '
                         '\\frac{1}{R}\\sqrt{\\frac{L}{C}}, \\quad BW = \\frac{\\omega_0}{Q} = \\frac{R}{L}, \\quad '
                         'Z_d = \\frac{L}{C R_L}$$',
                   'text': '<strong>AC Resonance:</strong> Series resonance yields minimum impedance $Z_0 = R$ and '
                           'maximum current with voltage magnification $Q V$. Parallel tank circuit yields maximum '
                           'dynamic impedance $Z_d = L/(C R_L)$ (anti-resonance) and minimum line current.'},
    'comp-q4': {   'eq': '$$V_L = \\sqrt{3}V_{ph}, \\quad P = W_1 + W_2 = \\sqrt{3}V_L I_L \\cos\\phi, \\quad '
                         '\\tan\\phi = \\sqrt{3}\\frac{W_1 - W_2}{W_1 + W_2}$$',
                   'text': '<strong>Three-Phase & Two-Wattmeter Method:</strong> Total 3-phase active power is the '
                           'algebraic sum $W_1 + W_2$. Load power factor is derived from $\\tan\\phi = \\sqrt{3}(W_1 - '
                           'W_2)/(W_1 + W_2)$. When $\\cos\\phi = 0.5$, $W_2 = 0$; when $\\cos\\phi < 0.5$, $W_2$ '
                           'deflects negative.'},
    'comp-q5': {   'eq': '$$\\nabla \\cdot \\mathbf{D} = \\rho_v, \\ \\nabla \\cdot \\mathbf{B} = 0, \\ \\nabla '
                         '\\times \\mathbf{E} = -\\frac{\\partial \\mathbf{B}}{\\partial t}, \\ \\nabla \\times '
                         '\\mathbf{H} = \\mathbf{J}_c + \\frac{\\partial \\mathbf{D}}{\\partial t}, \\ \\mathbf{S} = '
                         '\\mathbf{E} \\times \\mathbf{H}$$',
                   'text': "<strong>Maxwell\\'s Equations & Poynting Vector:</strong> Maxwell added displacement "
                           "current $\\mathbf{J}_d = \\partial \\mathbf{D}/\\partial t$ to Ampère\\'s law to satisfy "
                           'charge continuity. Electromagnetic waves propagate at $v = 1/\\sqrt{\\mu\\varepsilon}$ '
                           'with intrinsic impedance $\\eta = \\sqrt{\\mu/\\varepsilon} \\approx 377\\,\\Omega$. '
                           'Poynting vector $\\mathbf{S}$ denotes power flux density.'},
    'comp-q6': {   'eq': '$$E_b = \\frac{P \\Phi Z N}{60 A}, \\quad T_e = \\frac{P Z}{2\\pi A}\\Phi I_a, \\quad AT_d = '
                         '\\frac{Z I_a}{2 A P}\\left(\\frac{2\\theta_m}{180^\\circ}\\right), \\quad N = \\frac{V - I_a '
                         "R_a}{K\\' \\Phi}$$",
                   'text': '<strong>DC Machines:</strong> Induced EMF and torque equations dictate electromechanical '
                           'conversion. Armature reaction causes MNA shift and air-gap distortion; neutralized by '
                           'interpoles and compensating windings. Speed control uses armature voltage, field flux, or '
                           'Ward-Leonard drives.'},
    'comp-q7': {   'eq': '$$W_c = V I_{a0} - I_{a0}^2 R_a, \\quad P_{in,mains} = V I_1 = \\text{Total Losses of Both '
                         'Machines}, \\quad W_{stray} = \\frac{W_{stray,total}}{2}$$',
                   'text': "<strong>DC Machine Testing:</strong> Swinburne\\'s no-load test predetermines "
                           "motor/generator efficiency by isolating constant losses $W_c$. Hopkinson\\'s regenerative "
                           'back-to-back test tests two coupled machines at actual full load, drawing only net system '
                           'losses from mains.'},
    'comp-q8': {   'eq': '$$\\%VR = \\frac{I_2 R_{02}\\cos\\phi \\pm I_2 X_{02}\\sin\\phi}{V_2}\\times 100\\%, \\quad '
                         'x = \\sqrt{\\frac{P_i}{P_{cu,fl}}}, \\quad W_{auto} = (1 - k) W_{2-wdg}$$',
                   'text': '<strong>Transformers:</strong> OC test finds core loss $P_i$ and magnetizing parameters; '
                           'SC test finds copper loss $P_{cu,fl}$ and series leakage impedance. Maximum efficiency '
                           'occurs when $P_i = x^2 P_{cu,fl}$. Autotransformer saves $(1 - k)$ copper via conductive '
                           'power transfer.'},
    'comp-q9': {   'eq': '$$\\Phi_r = 1.5\\Phi_m, \\quad T_e = \\frac{3}{\\omega_s}\\frac{s E_2^2 R_2}{R_2^2 + s^2 '
                         'X_2^2}, \\quad s_{max} = \\frac{R_2}{X_2}, \\quad T_{max} = \\frac{3 E_2^2}{2\\omega_s X_2}, '
                         '\\quad I_{st,Y} = \\frac{1}{3}I_{st,\\Delta}$$',
                   'text': '<strong>Induction Motors:</strong> Balanced 3-phase stator currents produce an RMF of '
                           'constant magnitude $1.5\\Phi_m$ revolving at $N_s$. Breakdown torque $T_{max}$ is '
                           'independent of rotor resistance $R_2$. Star-delta starting reduces starting line current '
                           'and torque to $1/3$.'},
    'cprog-q1': {   'eq': '$$\\text{Source (.c)} \\xrightarrow{\\text{cpp}} \\text{Preprocessed (.i)} '
                          '\\xrightarrow{\\text{cc1}} \\text{Assembly (.s)} \\xrightarrow{\\text{as}} \\text{Object '
                          '(.o)} \\xrightarrow{\\text{ld}} \\text{Binary (a.out)}$$',
                    'text': 'C compilation pipeline consists of Preprocessor (macro expansion, header inclusion), '
                            'Compiler (parsing, assembly code generation), Assembler (relocatable machine code), '
                            'Linker (symbol resolution, library linking), and Loader.'},
    'cprog-q10': {   'eq': '$$\\text{char names}[M][N] \\implies M \\text{ strings, each max } N-1 \\text{ chars} + '
                           '\\backslash 0; \\quad \\text{Swap via strcpy(temp, arr[j])}$$',
                     'text': '2D character arrays store lists of strings. Sorting strings alphabetically employs '
                             'bubble sort using strcmp() for lexicographical comparison and strcpy() with temporary '
                             'buffer for swapping.'},
    'cprog-q11': {   'eq': '$$\\text{Call by Value: Copies value to callee stack}; \\quad \\text{Call by Reference: '
                           'Passes } \\&var \\text{ to pointer } *ptr$$',
                     'text': 'Call by value passes copies; caller variables remain unchanged. Call by reference passes '
                             'memory addresses (&x), enabling function to modify caller variables directly via '
                             'dereferencing (*ptr).'},
    'cprog-q12': {   'eq': '$$T(n) = 2T(n-1) + 1 = 2^n - 1, \\quad \\text{Base Condition Prevents Stack Overflow}$$',
                     'text': 'Recursion requires a base condition to terminate and an inductive step. Tower of Hanoi '
                             'requires $2^n - 1$ moves. Missing base condition causes call stack exhaustion and stack '
                             'overflow crash.'},
    'cprog-q13': {   'eq': '$$\\text{auto (Stack, Garbage)}; \\quad \\text{register (CPU)}; \\quad \\text{static '
                           '(Data/BSS, Zero, Lifetime=Program)}; \\quad \\text{extern (Global)}$$',
                     'text': 'Storage classes define location, default value, scope, and lifetime. static local '
                             'variables preserve state across function calls; static global restricts visibility to '
                             'current file.'},
    'cprog-q14': {   'eq': '$$p \\pm k = p \\pm (k \\times \\text{sizeof(Type)}), \\quad arr[i] \\equiv *(arr + i), '
                           '\\quad \\text{void* Generic; NULL: } (void*)0$$',
                     'text': 'Pointer arithmetic scales by data type size. Array names decay into base pointers. Void '
                             'pointers (void *) are generic; dangling pointers point to deallocated memory (neutralize '
                             'via ptr = NULL).'},
    'cprog-q15': {   'eq': '$$\\text{malloc: Uninitialized garbage}; \\quad \\text{calloc: Zero-initialized}; \\quad '
                           '\\text{realloc: Resizes}; \\quad \\text{free: Prevents Memory Leaks}$$',
                     'text': 'Dynamic Memory Allocation manages heap: malloc(size) allocates uninitialized bytes; '
                             'calloc(n, size) allocates zero-filled bytes; realloc resizes existing block; free(ptr) '
                             'prevents memory leaks.'},
    'cprog-q16': {   'eq': '$$\\text{Structure Padding: Word alignment inserts dummy bytes; } \\text{sizeof} = '
                           '\\text{multiple of largest member alignment}$$',
                     'text': 'Structures bundle heterogeneous data. Compiler inserts padding bytes to align multi-byte '
                             'data on word boundaries for fast bus access. Reordering members largest-to-smallest '
                             'minimizes padding.'},
    'cprog-q17': {   'eq': '$$ptr\\text{->}member \\equiv (*ptr).member, \\quad \\text{Array of Structs: Table of '
                           'records}$$',
                     'text': 'Structure pointers access members using the arrow operator (->). Arrays of structures '
                             'represent tabular database records. Pass structure pointers to functions to avoid stack '
                             'frame copying overhead.'},
    'cprog-q18': {   'eq': '$$\\text{struct Node } \\{ \\text{int data; struct Node *next; } \\}; \\quad \\text{Heap '
                           'Allocation via malloc}$$',
                     'text': 'Self-referential structures contain a pointer to their own structure type. Used to build '
                             'dynamic singly linked lists with dynamic heap nodes linked via next pointers terminated '
                             'by NULL.'},
    'cprog-q19': {   'eq': '$$\\text{sizeof(union)} = \\text{Size of largest member}; \\quad \\text{All members share '
                           'identical base memory address}$$',
                     'text': 'Structures allocate separate memory for every member; Unions share a single memory block '
                             'where only one member is active at a time. Bit-fields pack integer members into specific '
                             'bit counts.'},
    'cprog-q2': {   'eq': '$$\\text{char (1B)} \\to \\text{int (4B)} \\to \\text{long (8B)} \\to \\text{float (4B)} '
                          '\\to \\text{double (8B)} \\to \\text{long double (16B)}$$',
                    'text': 'Fundamental C types: char (1B, -128 to 127), int (4B, -2B to +2B), float (4B), double '
                            '(8B). Implicit type conversion promotes operands along promotion ladder; explicit casting '
                            'forces conversion via `(type)val`.'},
    'cprog-q20': {   'eq': '$$\\text{typedef: Compiler type alias}; \\quad \\text{\\#define: Preprocessor text '
                           'substitution}; \\quad \\text{\\#ifndef Header Guards}$$',
                     'text': 'typedef creates compiler-verified type aliases; enum defines named integer constants; '
                             '#define creates macros (use parentheses); #ifndef header guards prevent multiple '
                             'inclusion.'},
    'cprog-q21': {   'eq': '$$\\text{FILE *fp = fopen(name, mode); fclose(fp); Modes: "r", "w", "a", "r+", "w+", '
                           '"a+"}$$',
                     'text': 'File I/O uses FILE pointer streams. fopen() returns NULL on failure. Mode "r" reads '
                             'existing; "w" overwrites/creates; "a" appends. Binary modes append "b" ("rb", "wb") '
                             'without line translation.'},
    'cprog-q22': {   'eq': '$$\\text{fgetc/fputc (Char)}; \\quad \\text{fgets/fputs (Line/String)}; \\quad '
                           '\\text{fscanf/fprintf (Formatted Text)}$$',
                     'text': 'File text I/O: fgetc reads characters until EOF (-1); fgets safely reads string line '
                             'into buffer; fprintf and fscanf perform formatted reading and writing directly to disk '
                             'streams.'},
    'cprog-q23': {   'eq': '$$\\text{fwrite(ptr, size, count, fp); } \\quad \\text{fread(ptr, size, count, fp); } '
                           '\\quad \\text{Direct RAM-Disk Block Transfer}$$',
                     'text': 'Binary block I/O transfers raw memory bytes between RAM and disk without text '
                             'conversion: fwrite writes arrays/structures; fread reads raw blocks. Returns count of '
                             'items transferred.'},
    'cprog-q24': {   'eq': '$$\\text{fseek(fp, offset, SEEK\\_SET/SEEK\\_CUR/SEEK\\_END); } \\quad \\text{file\\_size} '
                           '= \\text{ftell(fp) after SEEK\\_END}$$',
                     'text': 'Random access repositioning: fseek sets byte offset from SEEK_SET (start), SEEK_CUR '
                             '(current), or SEEK_END (end). ftell returns current byte position; rewind resets to '
                             'start.'},
    'cprog-q25': {   'eq': '$$\\text{feof(fp): Non-zero after EOF read; ferror(fp): I/O error; perror(str): Prints '
                           'errno message}$$',
                     'text': 'feof() tests if EOF has been triggered; ferror() detects hardware I/O faults. perror() '
                             'and strerror(errno) print system error diagnostics corresponding to global errno code.'},
    'cprog-q26': {   'eq': '$$\\text{int main(int argc, char *argv[])}; \\quad argv[0] = \\text{Program Name}; \\quad '
                           '\\text{atoi(argv[i]) converts to int}$$',
                     'text': 'Command line arguments: argc counts arguments; argv is array of string pointers (argv[0] '
                             'is program name). String conversion functions (atoi, atof) parse numerical command-line '
                             'inputs.'},
    'cprog-q3': {   'eq': '$$x \\ll k = x \\times 2^k, \\quad x \\gg k = \\lfloor x / 2^k \\rfloor, \\quad '
                          '\\text{Precedence: Postfix} > \\text{Unary} > \\text{Arithmetic} > \\text{Shift} > '
                          '\\text{Relational} > \\text{Bitwise} > \\text{Logical} > \\text{Assign}$$',
                    'text': 'Bitwise operators (&, |, ^, ~, <<, >>) manipulate integer bits directly. Prefix ++x '
                            'changes then uses; postfix x++ uses then changes. Logical && and || feature short-circuit '
                            'evaluation.'},
    'cprog-q4': {   'eq': '$$\\%[\\text{flags}][\\text{width}][.\\text{precision}][\\text{length}]\\text{type}, \\quad '
                          '\\text{scanf Requires Memory Address } (\\&var)$$',
                    'text': 'printf formatting controls width and precision (%-10.2f left-justifies 2 decimals). scanf '
                            'requires memory address (&var for scalars; array name decays to base address without &). '
                            'Discard whitespace using " %c".'},
    'cprog-q5': {   'eq': '$$\\text{switch(expr): Integral types only}; \\quad \\text{break: Terminates loop/switch}; '
                          '\\quad \\text{continue: Skips to next iteration}$$',
                    'text': 'Control flow: if-else evaluates boolean truth; switch-case branches on integral constants '
                            '(fall-through without break). while is pre-tested (0+ times); do-while is post-tested (1+ '
                            'times guaranteed).'},
    'cprog-q6': {   'eq': '$$Loc(arr[i]) = \\text{Base} + (i \\times \\text{sizeof(Type)}), \\quad \\text{Binary '
                          'Search: } mid = low + \\frac{high - low}{2} \\ (O(\\log_2 N))$$',
                    'text': '1D arrays allocate contiguous memory with zero-based indexing (no bounds checking in C). '
                            'Binary Search on sorted arrays halves search space iteratively, achieving O(log N) '
                            'complexity.'},
    'cprog-q7': {   'eq': '$$Loc(arr[i][j]) = \\text{Base} + [(i \\times N) + j] \\times \\text{sizeof(Type)}, \\quad '
                          'C_{ij} = \\sum_{k=0}^{q-1} A_{ik} B_{kj} \\ (O(n^3))$$',
                    'text': 'Row-Major Order stores 2D matrix row by row. Matrix multiplication requires Columns of A '
                            '== Rows of B; computed using three nested loops with O(p*q*r) complexity.'},
    'cprog-q8': {   'eq': '$$\\text{String} = \\text{Character Array terminated by } \\backslash 0 \\ (\\text{ASCII '
                          '0}), \\quad \\text{Stack Array (Mutable) vs Literal Pointer (Read-Only)}$$',
                    'text': 'Strings in C are null-terminated (`\\0`). Character arrays on stack are mutable; string '
                            'literal pointers point to read-only text segments. Use fgets() to prevent buffer overflow '
                            'vulnerabilities.'},
    'cprog-q9': {   'eq': '$$\\text{strlen: Count until } \\backslash 0; \\quad \\text{strcpy: Copy including } '
                          '\\backslash 0; \\quad \\text{strcmp: } s1 - s2 \\text{ ASCII difference}$$',
                    'text': '<string.h> functions operate via pointer traversal until null byte: strlen computes '
                            'length, strcpy copies bytes, strcat appends to end, and strcmp compares ASCII '
                            'differences.'},
    'drive-q1': {   'eq': '$$\\text{Source} \\longrightarrow \\text{Power Modulator} \\longrightarrow \\text{Electric '
                          'Motor} \\longrightarrow \\text{Load} \\quad (\\text{Closed-Loop Control})$$',
                    'text': '<strong>Constituent Elements of an Electric Drive:</strong><br><strong>1. Power '
                            'Source:</strong> 1-phase/3-phase AC utility grid or DC source/battery.<br><strong>2. '
                            'Power Modulator:</strong> Regulates energy flow via converters/inverters (rectifiers, '
                            'choppers, VSIs, cycloconverters).<br><strong>3. Electric Motor:</strong> Converts '
                            'modulated electrical energy to controlled mechanical torque (DC, Induction, BLDC, '
                            'Synchronous).<br><strong>4. Control & Sensing Unit:</strong> Measures '
                            'current/speed/position and generates switching signals to enforce precision motion.'},
    'drive-q10': {   'eq': '$$V_a = \\delta V_s \\ge 0, \\quad I_a > 0 \\text{ (Motoring via } '
                           'CH_1\\text{-}D_2\\text{)}, \\quad I_a < 0 \\text{ (Regeneration via } '
                           'CH_2\\text{-}D_1\\text{)}$$',
                     'text': 'A two-quadrant Class-C chopper achieves seamless forward motoring (Q1) and forward '
                             'regenerative braking (Q2) by alternately switching two complementary chopper legs '
                             'without mechanical contactor reversal.'},
    'drive-q10b': {   'eq': '$$V_a = (2\\delta - 1)V_s, \\quad -V_s \\le V_a \\le +V_s, \\quad -I_{\\max} \\le I_a '
                            '\\le +I_{\\max}$$',
                      'text': 'A four-quadrant Class-E H-bridge chopper provides instantaneous bidirectional control '
                              'of both armature voltage and current, enabling smooth forward/reverse motoring and '
                              'regenerative braking.'},
    'drive-q11': {   'eq': '$$\\tau_{\\text{current}} \\approx 1\\text{--}2\\text{ ms} \\ll \\tau_{\\text{speed}} '
                           '\\approx 30\\text{--}100\\text{ ms} \\implies \\text{Cascaded Loops with Inner Current '
                           'Clamping}$$',
                     'text': 'Cascaded two-loop control uses an inner current loop to enforce instantaneous '
                             'semiconductor overcurrent protection, nested inside a slower outer PI speed loop that '
                             'ensures zero steady-state tracking error.'},
    'drive-q12': {   'eq': '$$T_e \\propto V_s^2 \\implies \\text{Torque drops quadratically with stator voltage; } '
                           'P_{cu2} = s P_g \\implies \\text{Severe Rotor Overheating}$$',
                     'text': 'Stator voltage speed control is restricted to high-slip induction motors driving '
                             'fan/pump loads over narrow speed ranges because motor torque collapses with $V_s^2$ and '
                             'causes excessive rotor copper dissipation.'},
    'drive-q12b': {   'eq': '$$\\text{VSI: DC voltage link with capacitor (PWM voltage output); } \\quad \\text{CSI: '
                            'DC current link with large inductor (inherent regeneration)}$$',
                      'text': 'VSI drives supply multiple parallel motors using fast IGBT switches with high power '
                              'factor, whereas CSI drives provide rugged short-circuit ride-through and direct '
                              'regenerative capability for high-power single motors.'},
    'drive-q13': {   'eq': '$$\\phi_m \\propto \\frac{V_s}{f_s} = \\text{constant} \\implies T_{\\max} = '
                           '\\frac{3}{2}\\frac{V_s^2}{\\omega_s (2\\omega_s L_l)} \\approx \\text{constant breakdown '
                           'torque}$$',
                     'text': 'Maintaining a constant $V/f$ ratio preserves constant air-gap magnetic flux and prevents '
                             'core saturation, guaranteeing maximum available breakdown torque across the entire base '
                             'speed range.'},
    'drive-q14': {   'eq': '$$R_{eff} = R_{ext} (1 - \\delta), \\quad s \\propto \\frac{R_2 + R_{eff}}{V_s^2} \\quad '
                           '(0 \\le \\delta \\le 1)$$',
                     'text': 'Rotor resistance chopper control smooths slip variation in wound-rotor induction motors '
                             'without mechanical resistor stepping, but dissipates slip power as heat in external '
                             'resistors.'},
    'drive-q14b': {   'eq': '$$P_{\\text{slip}} = s P_g; \\quad \\text{Kramer: Diode rectifier + line inverter '
                            '(sub-synchronous); Scherbius: Cycloconverter (sub/super-synchronous)}$$',
                      'text': 'Slip power recovery schemes recover rotor slip power $s P_g$ and inject it back into '
                              'the AC mains, achieving high operating efficiency in large-capacity pumps, fans, and '
                              'wind turbines.'},
    'drive-q15': {   'eq': '$$\\text{True Sync: Inverter frequency set independently } \\implies '
                           '\\text{Hunting/Stalling risk; Self-Controlled: Fired via Rotor Sensor } \\implies '
                           '\\text{No Hunting}$$',
                     'text': 'In self-controlled mode, inverter switching pulses are triggered directly by rotor '
                             'position sensors (encoder/Hall sensors), eliminating hunting oscillations and preventing '
                             'synchronous motor pull-out.'},
    'drive-q15b': {   'eq': '$$\\text{Leading Power Factor } (\\cos\\phi > 0 \\text{ leading}) \\implies \\text{Motor '
                            'Back-EMF naturally commutates thyristor inverter switches}$$',
                      'text': 'Load-Commutated Inverter (LCI) drives over-excite the synchronous motor to draw leading '
                              'current, allowing generated machine back-EMF to naturally turn off the inverter '
                              'thyristors without auxiliary commutation circuits.'},
    'drive-q16': {   'eq': '$$\\begin{bmatrix} x_\\alpha \\\\ x_\\beta \\end{bmatrix} = \\frac{2}{3}\\begin{bmatrix} 1 '
                           '& -\\frac{1}{2} & -\\frac{1}{2} \\\\ 0 & \\frac{\\sqrt{3}}{2} & -\\frac{\\sqrt{3}}{2} '
                           '\\end{bmatrix}\\begin{bmatrix} x_a \\\\ x_b \\\\ x_c \\end{bmatrix}, \\quad '
                           '\\begin{bmatrix} x_d \\\\ x_q \\end{bmatrix} = \\begin{bmatrix} \\cos\\theta_e & '
                           '\\sin\\theta_e \\\\ -\\sin\\theta_e & \\cos\\theta_e \\end{bmatrix}\\begin{bmatrix} '
                           'x_\\alpha \\\\ x_\\beta \\end{bmatrix}$$',
                     'text': 'Clarke transformation converts three-phase stationary $abc$ coordinates into two-phase '
                             'stationary $\\alpha\\beta$ coordinates, and Park transformation rotates them into a '
                             'synchronously rotating $dq$ reference frame.'},
    'drive-q17': {   'eq': '$$V_{ref} = \\frac{T_1}{T_s}V_1 + \\frac{T_2}{T_s}V_2 + \\frac{T_0}{T_s}V_0, \\quad '
                           'V_{out,\\max} = \\frac{V_{dc}}{\\sqrt{3}} \\approx 0.577 V_{dc} \\quad (15.5\\% \\text{ '
                           'higher than SPWM})$$',
                     'text': 'Space Vector PWM synthesizes rotating reference voltage vectors from adjacent stationary '
                             'active and zero vectors, achieving 15.5% higher DC bus voltage utilization and '
                             'significantly lower current THD than SPWM.'},
    'drive-q18': {   'eq': '$$\\psi_{rq} = 0 \\implies \\psi_r = \\psi_{rd} = L_m i_{sd}, \\qquad T_e = \\frac{3}{2} P '
                           '\\frac{L_m}{L_r} \\psi_{rd} i_{sq} \\propto i_{sd} \\cdot i_{sq}$$',
                     'text': 'Field-Oriented Control aligns the rotor flux vector strictly along the $d$-axis '
                             '($\\psi_{rq} = 0$), decoupling AC induction motor control into independent flux '
                             'regulation ($i_{sd}$) and torque regulation ($i_{sq}$).'},
    'drive-q2': {   'eq': '$$\\eta_{\\text{electric}} > 90\\%, \\quad \\text{Four-Quadrant Operation}, \\quad '
                          '\\text{Zero Direct Tailpipe Emissions}$$',
                    'text': 'Electric drives surpass mechanical/thermal drives with superior conversion efficiency, '
                            'instantaneous torque response, clean zero-emission operation, regenerative braking '
                            'capability, and digital automation integration.'},
    'drive-q3': {   'eq': '$$T_L = T_{L0} + C \\left(\\frac{\\omega}{\\omega_n}\\right)^k, \\quad k=0 \\text{ '
                          '(Hoist)}, \\; k=1 \\text{ (Calender)}, \\; k=2 \\text{ (Fan/Pump)}, \\; k=-1 \\text{ '
                          '(Lathe)}$$',
                    'text': '<strong>Classification of Industrial Load Torques:</strong><br><strong>1. Active Load '
                            'Torques:</strong> Torques that retain their sign/direction irrespective of rotation '
                            'direction (e.g., gravitational torque in hoists $k=0$, tension in coilers).<br><strong>2. '
                            'Passive Load Torques:</strong> Torques that always oppose motion (dry coulomb friction '
                            '$k=0$, viscous friction $k=1$, centrifugal fans/pumps $T_L \\propto \\omega^2$ with '
                            '$k=2$, constant power machine tools $T_L \\propto 1/\\omega$ with $k=-1$).'},
    'drive-q3b': {   'eq': '$$\\omega_{\\text{crit}} = \\sqrt{\\frac{K_{sh}(J_M + J_L)}{J_M \\cdot J_L}}, \\qquad '
                           '|\\omega_{\\text{operating}} - \\omega_{\\text{crit}}| \\ge 0.20 \\, '
                           '\\omega_{\\text{crit}}$$',
                     'text': 'Critical speed occurs when rotational shaft speed excites the natural torsional '
                             'frequency of the mechanical coupling, creating severe resonant torque oscillations and '
                             'catastrophic shaft fracture.'},
    'drive-q4': {   'eq': '$$T - T_L = J \\frac{d\\omega_m}{dt} + \\frac{1}{2} \\omega_m^2 \\frac{dJ}{dt} \\approx J '
                          '\\frac{d\\omega_m}{dt}$$',
                    'text': 'The fundamental dynamic torque equation governs acceleration: positive dynamic torque ($T '
                            '> T_L$) accelerates the motor, balanced torque ($T = T_L$) maintains steady speed, and '
                            'negative torque ($T < T_L$) causes deceleration.'},
    'drive-q5': {   'eq': '$$P_m = T \\cdot \\omega_m \\implies \\begin{cases} \\text{Q1: Forward Motoring } (+T, '
                          '+\\omega, P>0) & \\text{Q2: Forward Braking } (-T, +\\omega, P<0) \\\\ \\text{Q3: Reverse '
                          'Motoring } (-T, -\\omega, P>0) & \\text{Q4: Reverse Braking } (+T, -\\omega, P<0) '
                          '\\end{cases}$$',
                    'text': '<strong>Four-Quadrant Operation of Hoist Drive:</strong><br><strong>Quadrant 1 (Forward '
                            'Motoring):</strong> $+T, +\\omega_m$ &mdash; Hoisting a loaded cage upward against '
                            'gravity ($P_m > 0$).<br><strong>Quadrant 2 (Forward Braking):</strong> $-T, +\\omega_m$ '
                            '&mdash; Decelerating upward motion via regenerative braking ($P_m < '
                            '0$).<br><strong>Quadrant 3 (Reverse Motoring):</strong> $-T, -\\omega_m$ &mdash; Driving '
                            'an empty cage downward against friction ($P_m > 0$).<br><strong>Quadrant 4 (Reverse '
                            'Braking):</strong> $+T, -\\omega_m$ &mdash; Safely lowering a loaded cage under gravity '
                            'with braking counter-torque ($P_m < 0$).'},
    'drive-q6': {   'eq': '$$\\frac{dT_L}{d\\omega_m} - \\frac{dT}{d\\omega_m} > 0 \\iff \\frac{dT_L}{d\\omega_m} > '
                          '\\frac{dT}{d\\omega_m} \\quad (\\text{at equilibrium } T = T_L)$$',
                    'text': 'An electric drive operating point is steady-state stable if a small disturbance increase '
                            'in speed creates a retarding net torque ($T_L > T$), naturally restoring the drive to '
                            'equilibrium speed.'},
    'drive-q6b': {   'eq': '$$\\theta(t) = \\theta_{ss} (1 - e^{-t/\\tau_h}) + \\theta_0 e^{-t/\\tau_h}, \\quad '
                           '\\tau_h = \\frac{C_{th}}{A \\cdot h}, \\quad P_{\\text{rated}} \\ge P_{\\text{rms}} = '
                           '\\sqrt{\\frac{\\sum P_i^2 t_i}{\\sum t_i}}$$',
                     'text': 'Motor thermal selection ensures steady-state temperature rise $\\theta_{ss} = '
                             'P_{\\text{loss}}/(A \\cdot h)$ does not exceed the insulation class thermal rating ($B, '
                             'F, H$) under continuous and fluctuating duty cycles.'},
    'drive-q7': {   'eq': '$$\\omega_m = \\frac{V_a - I_a R_a}{K \\phi} \\implies \\begin{cases} \\text{Below Base '
                          'Speed: } V_a \\text{ variation at rated } \\phi \\implies \\text{Constant Torque Mode} \\\\ '
                          '\\text{Above Base Speed: } \\phi \\text{ reduction at rated } V_a \\implies \\text{Constant '
                          'Power Mode} \\end{cases}$$',
                    'text': '<strong>1. Armature Voltage Control (Below Base Speed):</strong> Variable $V_a$ with full '
                            'rated flux $\\phi$ provides <strong>Constant Torque</strong> ($T_{\\max} = K \\phi '
                            'I_{a,\\text{rated}}$), where power increases linearly with speed ($P \\propto '
                            '\\omega$).<br><strong>2. Field Weakening Control (Above Base Speed):</strong> Rated $V_a$ '
                            'with reduced field flux $\\phi$ provides <strong>Constant Power</strong> ($P = V_a I_a = '
                            '\\text{constant}$), where developed torque decreases inversely with speed ($T \\propto '
                            '1/\\omega$).'},
    'drive-q7b': {   'eq': '$$V_{dc} = \\frac{3\\sqrt{3}V_m}{2\\pi}(1 + \\cos\\alpha) \\ge 0 \\quad (\\forall \\alpha '
                           '\\in [0^\\circ, 180^\\circ])$$',
                     'text': 'Semi-converters use freewheeling diodes that clamp the output voltage to non-negative '
                             'values ($V_{dc} \\ge 0$), restricting drive operation to single-quadrant motoring and '
                             'preventing regenerative braking.'},
    'drive-q8': {   'eq': '$$V_a = \\frac{2V_m}{\\pi}\\cos\\alpha, \\quad \\omega_m = '
                          '\\frac{\\frac{2V_m}{\\pi}\\cos\\alpha - I_a R_a}{K_t \\phi} \\quad (\\text{Continuous '
                          'Conduction})$$',
                    'text': 'A single-phase full converter allows two-quadrant operation: rectification/motoring for '
                            'firing angle $\\alpha < 90^\\circ$ and inversion/regenerative braking into the AC mains '
                            'for $\\alpha > 90^\\circ$ with reversed armature connections.'},
    'drive-q8b': {   'eq': '$$V_a = \\frac{3\\sqrt{3}V_m}{\\pi}\\cos\\alpha, \\quad \\omega_m = '
                           '\\frac{\\frac{3\\sqrt{3}V_m}{\\pi}\\cos\\alpha - I_a R_a}{K_t \\phi}$$',
                     'text': 'Three-phase full converters provide six-pulse output with high ripple frequency '
                             '($300\\text{ Hz}$), maintaining continuous armature conduction across wide load ranges '
                             'with lower harmonic heating and higher motor efficiency.'},
    'drive-q9': {   'eq': '$$V_a = \\delta V_s = \\left(\\frac{t_{on}}{T}\\right) V_s, \\quad \\omega_m = '
                          '\\frac{\\delta V_s - I_a R_a}{K_t \\phi} \\quad (0 \\le \\delta \\le 1)$$',
                    'text': 'A Class-A step-down (buck) chopper controls motor speed smoothly in Quadrant 1 with high '
                            'energy efficiency, rapid dynamic response, and low armature current ripple.'},
    'drive-q9b': {   'eq': '$$V_s = \\frac{E_b}{1 - \\delta} \\implies I_a = \\frac{E_b - (1-\\delta)V_s}{R_a} \\quad '
                           '(\\text{Quadrant 2 Operation})$$',
                     'text': 'A Class-B step-up (boost) chopper uses the motor armature inductance to boost induced '
                             'back-EMF $E_b$ above DC source voltage $V_s$, pumping regenerative braking energy back '
                             'to the DC supply.'},
    'lac-q1': {   'eq': '$$\\operatorname{rank}(A) = \\operatorname{rank}([A|B]) = r \\implies \\begin{cases} r = n & '
                        '\\text{Unique solution} \\\\ r < n & \\text{Infinitely many solutions ($n-r$ free '
                        'parameters)} \\\\ \\operatorname{rank}(A) < \\operatorname{rank}([A|B]) & \\text{Inconsistent '
                        '(No solution)} \\end{cases}$$',
                  'text': '<strong>Rouché-Capelli Theorem:</strong> A linear system $AX = B$ is consistent iff '
                          '$\\operatorname{rank}(A) = \\operatorname{rank}([A|B]) = r$. If $r = n$, unique solution; '
                          'if $r < n$, infinitely many solutions with $n-r$ independent parameters; if '
                          '$\\operatorname{rank}(A) \\ne \\operatorname{rank}([A|B])$, no solution.'},
    'lac-q10': {   'eq': '$$Q = 8y_1^2 + 2y_2^2 + 2y_3^2, \\quad \\operatorname{rank} = 3, \\quad '
                         '\\operatorname{index} = 3, \\quad \\operatorname{signature} = 3, \\quad \\text{Strictly '
                         'Positive Definite}$$',
                   'text': '<strong>Orthogonal Diagonalisation & Quadratic Forms:</strong> Any real symmetric matrix '
                           '$A$ can be diagonalised by an orthogonal matrix $P$ ($P^T A P = D$). Canonical form is '
                           '$\\sum \\lambda_i y_i^2$. If all $\\lambda_i > 0$, the quadratic form is strictly positive '
                           'definite.'},
    'lac-q11': {   'eq': '$$\\lim_{x \\to 0} \\frac{x - \\sin x}{x^3} = \\lim_{x \\to 0} \\frac{1 - \\cos x}{3x^2} = '
                         '\\lim_{x \\to 0} \\frac{\\sin x}{6x} = \\lim_{x \\to 0} \\frac{\\cos x}{6} = \\frac{1}{6}$$',
                   'text': "<strong>L\\'Hopital\\'s Rule for Indeterminate Forms:</strong> When $\\lim "
                           '\\frac{f(x)}{g(x)}$ has form $\\frac{0}{0}$ or $\\frac{\\infty}{\\infty}$, differentiate '
                           'numerator and denominator independently until a determinate value emerges.'},
    'lac-q12': {   'eq': "$$f\\'\\'(x) = 12x(x-2) \\implies \\begin{cases} x \\in (-\\infty, 0) \\cup (2, \\infty) & "
                         "\\text{Concave Upward } (f\\'\\' > 0) \\\\ x \\in (0, 2) & \\text{Concave Downward } "
                         "(f\\'\\' < 0) \\end{cases}; \\quad \\text{Inflection Points: } (0, 10), (2, -6)$$",
                   'text': "<strong>Concavity & Inflection Criteria:</strong> Concave up where $f\\'\\'(x) > 0$; "
                           "concave down where $f\\'\\'(x) < 0$. Points of inflection occur strictly at real roots of "
                           "$f\\'\\'(x) = 0$ where $f\\'\\'(x)$ undergoes a sign change."},
    'lac-q13': {   'eq': '$$\\lim_{x \\to 0^+} (\\cot x)^{\\sin x} = e^{\\lim \\frac{\\ln(\\cot x)}{\\csc x}} = e^0 = '
                         '1, \\quad \\lim_{x \\to 0}\\left(\\frac{1}{x^2} - \\frac{\\cot x}{x}\\right) = \\lim_{x \\to '
                         '0}\\frac{\\sin x - x\\cos x}{x^3} = \\frac{1}{3}$$',
                   'text': '<strong>Exponential & Difference Indeterminate Forms:</strong> For power forms $0^0, '
                           '\\infty^0, 1^\\infty$, apply logarithms: $L = \\exp[\\lim g(x) \\ln f(x)]$. For $\\infty - '
                           '\\infty$, combine into a common denominator to reduce to $\\frac{0}{0}$.'},
    'lac-q14': {   'eq': '$$\\ln(\\cos x) = -\\frac{x^2}{2} - \\frac{x^4}{12} - \\frac{x^6}{45} - \\dots, \\quad '
                         '\\ln(\\cos 0.1) \\approx -0.00500833$$',
                   'text': '<strong>Taylor Expansion of Log-Cos:</strong> Because $\\ln(\\cos x)$ is an even function '
                           '($f(-x) = f(x)$), all odd-order derivatives vanish at $x=0$, leaving only even powers '
                           '$-x^2/2 - x^4/12$.'},
    'lac-q15': {   'eq': '$$e^x \\cos x = 1 + x - \\frac{x^3}{3} - \\frac{x^4}{6} + \\dots \\implies f^{(4)}(0) = -4, '
                         '\\quad e^{0.1}\\cos(0.1) \\approx 1.09965$$',
                   'text': '<strong>Series Cauchy Product & Derivatives:</strong> Multiplying Maclaurin series of '
                           'standard functions directly generates the composite expansion. The $n$-th derivative at '
                           'zero is extracted from the coefficient: $f^{(n)}(0) = n! \\cdot a_n$.'},
    'lac-q16': {   'eq': '$$f(x, y) = \\sin u, \\text{ degree } n=1 \\implies x \\frac{\\partial u}{\\partial x} + y '
                         "\\frac{\\partial u}{\\partial y} = n \\frac{f(u)}{f\\'(u)} = \\frac{\\sin u}{\\cos u} = "
                         '\\tan u$$',
                   'text': "<strong>Euler\\'s Theorem for Implicit Functions:</strong> If $f(u)$ is homogeneous of "
                           "degree $n$, then $x u_x + y u_y = n \\frac{f(u)}{f\\'(u)}$. For $f(u) = \\sin u$ of degree "
                           '1, this immediately yields $\\tan u$.'},
    'lac-q17': {   'eq': '$$\\left(\\frac{\\partial z}{\\partial r}\\right)^2 + \\frac{1}{r^2}\\left(\\frac{\\partial '
                         'z}{\\partial \\theta}\\right)^2 = \\left(\\frac{\\partial z}{\\partial x}\\right)^2 + '
                         '\\left(\\frac{\\partial z}{\\partial y}\\right)^2 = \\|\\nabla z\\|^2$$',
                   'text': '<strong>Invariance of Gradient Magnitude:</strong> The squared Euclidean norm of the '
                           'spatial gradient vector $\\|\\nabla z\\|^2$ is coordinate-invariant under rotation and '
                           'transformation from Cartesian $(x,y)$ to polar $(r,\\theta)$ frames.'},
    'lac-q18': {   'eq': "$$x^2 u_{xx} + 2xy u_{xy} + y^2 u_{yy} = g(u)[g\\'(u) - 1] = \\sin 2u (2\\cos 2u - 1) = 2 "
                         '\\cos 3u \\sin u$$',
                   'text': "<strong>Extended Euler\\'s Second Order Formula:</strong> If $x u_x + y u_y = g(u)$, then "
                           "$x^2 u_{xx} + 2xy u_{xy} + y^2 u_{yy} = g(u)[g\\'(u) - 1]$. For $g(u) = \\sin 2u$, this "
                           'simplifies to $2\\cos 3u \\sin u$.'},
    'lac-q19': {   'eq': '$$D = rt - s^2 \\implies \\begin{cases} (4, 0): D=36>0, r=-6<0 & \\text{Local Maximum } (f = '
                         '112) \\\\ (6, 0): D=36>0, r=6>0 & \\text{Local Minimum } (f = 108) \\\\ (5, \\pm 1): D=-36<0 '
                         '& \\text{Saddle Points } (f = 110) \\end{cases}$$',
                   'text': '<strong>Second Derivative Test for Functions of Two Variables:</strong> Calculate $D = '
                           'f_{xx}f_{yy} - (f_{xy})^2$. If $D > 0$ and $f_{xx} < 0$, local max; if $D > 0$ and $f_{xx} '
                           '> 0$, local min; if $D < 0$, saddle point.'},
    'lac-q2': {   'eq': '$$U = \\begin{bmatrix} 1 & 2 & -1 & 3 \\\\ 0 & 0 & 3 & -8 \\\\ 0 & 0 & 0 & 0 \\end{bmatrix} '
                        '\\implies \\operatorname{rank}(A) = \\text{number of non-zero rows} = 2$$',
                  'text': '<strong>Row Echelon Form & Rank:</strong> Elementary row operations preserve the rank of a '
                          'matrix. The rank equals the number of non-zero rows in the row echelon form.'},
    'lac-q20': {   'eq': '$$x = \\frac{a}{\\sqrt{3}}, \\; y = \\frac{b}{\\sqrt{3}}, \\; z = \\frac{c}{\\sqrt{3}} '
                         '\\implies V_{\\max} = 8xyz = \\frac{8abc}{3\\sqrt{3}}$$',
                   'text': '<strong>Lagrange Multipliers for Inscribed Volume:</strong> Equal partition of constraint '
                           'contributions $\\frac{x^2}{a^2} = \\frac{y^2}{b^2} = \\frac{z^2}{c^2} = \\frac{1}{3}$ '
                           'yields optimal vertex coordinates $(a/\\sqrt{3}, b/\\sqrt{3}, c/\\sqrt{3})$ and maximum '
                           'volume $8abc/(3\\sqrt{3})$.'},
    'lac-q21': {   'eq': '$$\\int_0^1 \\int_0^{\\sqrt{1-x^2}} (x^2 + y^2) \\, dy \\, dx = \\int_0^{\\pi/2} d\\theta '
                         '\\int_0^1 r^3 \\, dr = \\left(\\frac{\\pi}{2}\\right)\\left(\\frac{1}{4}\\right) = '
                         '\\frac{\\pi}{8}$$',
                   'text': '<strong>Cartesian to Polar Conversion:</strong> Substitute $x = r\\cos\\theta, y = '
                           'r\\sin\\theta, dx\\,dy = r\\,dr\\,d\\theta$. The first-quadrant unit circular arc '
                           'transforms to limits $r \\in [0, 1]$ and $\\theta \\in [0, \\pi/2]$.'},
    'lac-q22': {   'eq': '$$\\int_{x=0}^1 \\int_{y=x}^{\\sqrt{x}} f(x, y) \\, dy \\, dx = \\int_{y=0}^1 '
                         '\\int_{x=y^2}^y f(x, y) \\, dx \\, dy$$',
                   'text': '<strong>Change of Order of Integration:</strong> Sketch the region bounded by $y = x$ and '
                           '$y = \\sqrt{x}$. Switch from vertical strips ($x$-constant) to horizontal strips '
                           '($y$-constant), changing bounds from $y \\in [x, \\sqrt{x}]$ to $x \\in [y^2, y]$.'},
    'lac-q23': {   'eq': '$$\\int_0^\\infty \\int_0^\\infty e^{-(x^2+y^2)} \\, dx \\, dy = \\frac{\\pi}{4} \\implies '
                         '\\left(\\int_0^\\infty e^{-x^2} \\, dx\\right)^2 = \\frac{\\pi}{4} \\implies \\int_0^\\infty '
                         'e^{-x^2} \\, dx = \\frac{\\sqrt{\\pi}}{2}$$',
                   'text': '<strong>Gaussian Integral Evaluation via Double Integrals:</strong> Cartesian integration '
                           'of $e^{-x^2}$ lacks elementary antiderivative. Converting $J^2$ to polar coordinates '
                           'yields $r e^{-r^2}$, readily integrable to $\\pi/4$, proving $J = \\sqrt{\\pi}/2$.'},
    'lac-q24': {   'eq': '$$\\int_0^a \\int_y^a \\frac{x}{x^2 + y^2} \\, dx \\, dy = \\int_0^a \\left[\\int_0^x '
                         '\\frac{x}{x^2 + y^2} \\, dy \\right] dx = \\int_0^a \\frac{\\pi}{4} \\, dx = \\frac{\\pi '
                         'a}{4}$$',
                   'text': '<strong>Change of Order for Triangular Domain:</strong> Switching order from $dx\\,dy$ to '
                           '$dy\\,dx$ converts the complicated logarithmic $x$-integral into a standard inverse '
                           'tangent $\\tan^{-1}(y/x)$, collapsing the inner integral to constant $\\pi/4$.'},
    'lac-q25': {   'eq': '$$\\text{Area} = \\int_0^{4a} \\left(2\\sqrt{ax} - \\frac{x^2}{4a}\\right) dx = '
                         '\\left[\\frac{4\\sqrt{a}}{3}x^{3/2} - \\frac{x^3}{12a}\\right]_0^{4a} = \\frac{16a^2}{3}$$',
                   'text': '<strong>Area Enclosed by Conjugate Parabolas:</strong> The intersection between $y^2 = '
                           '4ax$ and $x^2 = 4ay$ spans $[0, 4a]$. Double integration yields the celebrated classical '
                           'area result $\\frac{16a^2}{3}$.'},
    'lac-q26': {   'eq': '$$V = \\int_0^{2\\pi} \\int_0^2 (4 - r\\sin\\theta) r \\, dr \\, d\\theta = \\int_0^{2\\pi} '
                         '\\left(8 - \\frac{8}{3}\\sin\\theta\\right) d\\theta = 16\\pi$$',
                   'text': '<strong>Volume of Truncated Cylinder via Cylindrical Coordinates:</strong> Cylindrical '
                           'coordinates simplify circular boundaries ($r \\le 2$). The odd periodic term '
                           '$\\sin\\theta$ integrates to zero over $[0, 2\\pi]$, leaving mean height $4$ times base '
                           'area $\\pi(2^2) = 16\\pi$.'},
    'lac-q3': {   'eq': '$$\\begin{bmatrix} 1 & 1 & 1 & | & 6 \\\\ 0 & 1 & 2 & | & 4 \\\\ 0 & 0 & \\lambda - 3 & | & '
                        '\\mu - 10 \\end{bmatrix} \\implies \\begin{cases} \\lambda = 3, \\mu \\ne 10 & \\text{No '
                        'solution} \\\\ \\lambda \\ne 3, \\forall \\mu & \\text{Unique solution} \\\\ \\lambda = 3, '
                        '\\mu = 10 & \\text{Infinite solutions} \\end{cases}$$',
                  'text': '<strong>Consistency Analysis with Parameters:</strong> At $\\lambda = 3$, row 3 of $A$ '
                          'vanishes. If $\\mu \\ne 10$, augmented matrix has rank 3 while $A$ has rank 2 '
                          '(inconsistent). If $\\mu = 10$, both ranks are 2 (infinitely many solutions). If $\\lambda '
                          '\\ne 3$, rank is 3 for any $\\mu$ (unique solution).'},
    'lac-q4': {   'eq': '$$\\operatorname{rank}(A) = \\operatorname{rank}([A|B]) = 2 < n=4 \\implies X = '
                        '\\begin{bmatrix} 7/5 \\\\ 1/5 \\\\ 0 \\\\ 0 \\end{bmatrix} + s \\begin{bmatrix} -17/5 \\\\ '
                        '-6/5 \\\\ 1 \\\\ 0 \\end{bmatrix} + t \\begin{bmatrix} 8/5 \\\\ -6/5 \\\\ 0 \\\\ 1 '
                        '\\end{bmatrix}$$',
                  'text': '<strong>Gauss Elimination Free Parameters:</strong> When $r < n$, the solution space is an '
                          'affine subspace with dimension $n - r$. The variables corresponding to non-pivot columns '
                          'become arbitrary parameters $s, t \\in \\mathbb{R}$.'},
    'lac-q5': {   'eq': '$$\\operatorname{rank}(A) = 3 = n \\implies \\operatorname{Nullity}(A) = n - r = 3 - 3 = 0 '
                        '\\implies X = \\begin{bmatrix} 0 \\\\ 0 \\\\ 0 \\end{bmatrix} \\text{ (Trivial solution '
                        'only)}$$',
                  'text': '<strong>Homogeneous System & Rank-Nullity:</strong> A homogeneous system $AX = 0$ possesses '
                          'non-trivial solutions if and only if $\\det(A) = 0$ ($\\operatorname{rank}(A) < n$). When '
                          '$\\operatorname{rank}(A) = n$, the null space is trivial and contains only the origin.'},
    'lac-q6': {   'eq': '$$A^2 - 5A - 2I = O \\implies A^{-1} = \\frac{1}{2}(A - 5I) = \\begin{bmatrix} -2 & 1 \\\\ '
                        '1.5 & -0.5 \\end{bmatrix}, \\quad A^3 = 27A + 10I = \\begin{bmatrix} 37 & 54 \\\\ 81 & 118 '
                        '\\end{bmatrix}$$',
                  'text': '<strong>Cayley-Hamilton Theorem:</strong> Every square matrix satisfies $\\det(A - \\lambda '
                          'I) = 0$. Premultiplying or postmultiplying the matrix polynomial by $A^{-1}$ enables direct '
                          'calculation of matrix inverse and high powers without determinants.'},
    'lac-q7': {   'eq': '$$\\lambda_1 = 4 \\implies X_1 = \\begin{bmatrix} 1 \\\\ 1 \\end{bmatrix}, \\quad \\lambda_2 '
                        '= 2 \\implies X_2 = \\begin{bmatrix} 1 \\\\ -1 \\end{bmatrix}, \\quad X_1^T X_2 = 1 - 1 = 0$$',
                  'text': '<strong>Orthogonality of Real Symmetric Matrix Eigenvectors:</strong> Eigenvectors of any '
                          'real symmetric matrix associated with distinct eigenvalues are strictly orthogonal: $X_i^T '
                          'X_j = 0$ for $\\lambda_i \\ne \\lambda_j$.'},
    'lac-q8': {   'eq': '$$\\lambda = 5, 1, 1 \\implies \\sum \\lambda_i = 7 = \\operatorname{tr}(A), \\quad \\prod '
                        '\\lambda_i = 5 = \\det(A); \\quad X_{\\lambda=5} = \\begin{bmatrix} 1 \\\\ 1 \\\\ 1 '
                        '\\end{bmatrix}, X_{\\lambda=1} = \\left\\{ \\begin{bmatrix} -2 \\\\ 1 \\\\ 0 \\end{bmatrix}, '
                        '\\begin{bmatrix} -1 \\\\ 0 \\\\ 1 \\end{bmatrix} \\right\\}$$',
                  'text': '<strong>Eigenvalue Properties & Multiplicity:</strong> Sum of eigenvalues equals the matrix '
                          'trace, and product equals the determinant. For repeated eigenvalues, geometric multiplicity '
                          'equals the nullity $n - \\operatorname{rank}(A - \\lambda I)$.'},
    'lac-q9': {   'eq': '$$A^3 - 3A^2 - A + 9I = O \\implies A^{-1} = \\frac{1}{9}\\begin{bmatrix} 0 & 3 & 3 \\\\ 3 & '
                        '2 & -7 \\\\ 3 & -1 & -1 \\end{bmatrix}, \\quad A^4 = 10A^2 - 6A - 27I$$',
                  'text': '<strong>Matrix Inverse via Characteristic Equation:</strong> For $A^3 - s_1 A^2 + s_2 A - '
                          '\\det(A)I = O$, multiplying by $A^{-1}$ yields $A^{-1} = \\frac{1}{\\det(A)}(A^2 - s_1 A + '
                          's_2 I)$, bypassing matrix cofactors.'},
    'lcs-q1': {   'eq': '$$S^T_G = \\frac{1}{1 + G(s)H(s)}, \\quad S^T_H = \\frac{-G(s)H(s)}{1 + G(s)H(s)}$$',
                  'text': 'Negative feedback reduces sensitivity to forward plant drifts by loop factor $(1+GH)$, but '
                          'sensitivity to feedback sensor drift remains high ($\\approx -1$), demanding precision '
                          'sensor components.'},
    'lcs-q10': {   'eq': '$$G_{PID}(s) = K_p + \\frac{K_i}{s} + K_d s = \\frac{K_d s^2 + K_p s + K_i}{s}$$',
                   'text': '<strong>P:</strong> Speeds response, reduces error.<br><strong>PI:</strong> Adds pole at '
                           '$s=0$, raises Type by 1, eliminates step error, reduces stability.<br><strong>PD:</strong> '
                           'Adds LHP zero, increases damping $\\zeta$, improves stability, sensitive to '
                           'noise.<br><strong>PID:</strong> Combines zero steady-state error with rapid damping.'},
    'lcs-q11': {   'eq': '$$\\int_0^\\infty |g(t)| \\, dt < \\infty \\iff \\text{All closed-loop poles lie strictly in '
                         'open LHP } (\\text{Re}(s_i) < 0)$$',
                   'text': 'BIBO stability requires absolute integrability of the impulse response. LHP poles decay '
                           'exponentially ($e^{-\\sigma t}$); RHP poles diverge ($e^{+\\sigma t}$); simple imaginary '
                           'axis poles yield sustained marginal oscillations.'},
    'lcs-q12': {   'eq': '$$\\text{Number of RHP roots} = \\text{Number of sign changes in 1st column of Routh array; '
                         'replace } 0 \\text{ with } \\epsilon > 0$$',
                   'text': 'In Special Case 1, a leading zero halts division. Replace it with $\\epsilon > 0$, compute '
                           'subsequent rows in terms of $\\epsilon$, and evaluate the signs as $\\epsilon \\to 0^+$. '
                           'Two sign changes confirm two RHP unstable roots.'},
    'lcs-q13': {   'eq': '$$A(s) = 15.75 s^2 + K_{mar} = 0 \\implies \\frac{dA(s)}{ds} = 31.5 s; \\quad K_{mar} = '
                         '19.6875, \\quad \\omega_{osc} = 1.118 \\text{ rad/s}$$',
                   'text': 'An entire row of zeros reveals roots symmetric about the origin. Differentiate the even '
                           'auxiliary polynomial $A(s)$, replace the zero row, and solve $A(s) = 0$ to find sustained '
                           'oscillation frequency $\\omega_{osc}$.'},
    'lcs-q14': {   'eq': '$$\\angle G(s)H(s) = \\pm (2q+1)180^\\circ, \\quad |G(s)H(s)| = 1, \\quad \\sigma_A = '
                         '\\frac{\\sum p_i - \\sum z_j}{n - m}, \\quad \\theta_a = \\frac{(2q+1)180^\\circ}{n - m}$$',
                   'text': 'Root locus plots closed-loop pole paths as gain $K$ varies $0 \\to \\infty$. Branches '
                           'depart from open poles, approach asymptotes at angle $\\theta_a$ intersecting at centroid '
                           '$\\sigma_A$, and break away where $dK/ds = 0$.'},
    'lcs-q15': {   'eq': '$$G(s) = \\frac{K}{s(s+2)(s+4)} \\implies \\sigma_A = -2, \\quad \\theta_a = 60^\\circ, '
                         '180^\\circ, 300^\\circ, \\quad s_{break} = -0.845, \\quad K_{mar} = 48, \\quad \\omega_{cr} '
                         '= \\pm j 2.83$$',
                   'text': 'Poles at $0, -2, -4$ collide at breakaway point $s = -0.845$ ($K=3.08$), cross '
                           '$j\\omega$-axis at $\\pm j 2.83$ at marginal gain $K_{mar} = 48$. Stable range is $0 < K < '
                           '48$.'},
    'lcs-q16': {   'eq': '$$M_r = \\frac{1}{2\\zeta\\sqrt{1-\\zeta^2}}, \\quad \\omega_r = '
                         '\\omega_n\\sqrt{1-2\\zeta^2}, \\quad \\omega_b = \\omega_n\\sqrt{(1-2\\zeta^2) + '
                         '\\sqrt{4\\zeta^4 - 4\\zeta^2 + 2}}$$',
                   'text': 'Resonant peak $M_r$ exists only for $\\zeta < 0.707$ and correlates directly with time '
                           'overshoot $M_p$. Bandwidth $\\omega_b$ is directly proportional to natural frequency '
                           '$\\omega_n$ and inversely to rise time $t_r$.'},
    'lcs-q17': {   'eq': '$$20\\log_{10}|G(j\\omega)| \\text{ (dB) vs } \\log\\omega, \\quad \\text{Corner frequency } '
                         '\\omega_c = \\frac{1}{T}, \\quad \\text{Slopes: } \\pm 20 \\text{ dB/decade}$$',
                   'text': 'Bode diagrams plot magnitude in dB and phase in degrees on semi-log scales. Standard '
                           'factors combine additively: simple poles break at $\\omega_c = 1/T$ with $-20 \\text{ '
                           'dB/dec}$ slope change and $-45^\\circ$ phase.'},
    'lcs-q18': {   'eq': '$$\\omega_{pc}: \\angle G(j\\omega_{pc}) = -180^\\circ, \\quad GM = '
                         '-20\\log_{10}|G(j\\omega_{pc})|; \\quad \\omega_{gc}: |G(j\\omega_{gc})| = 1, \\quad PM = '
                         '180^\\circ + \\angle G(j\\omega_{gc})$$',
                   'text': 'Stable systems require $\\omega_{gc} < \\omega_{pc}$, giving $GM > 0 \\text{ dB}$ and $PM '
                           '> 0^\\circ$. For $G(s) = 10/[s(1+0.1s)(1+0.05s)]$, $\\omega_{pc} = 14.14 \\text{ rad/s}, '
                           'GM = +9.54 \\text{ dB}, PM = +33.2^\\circ$.'},
    'lcs-q19': {   'eq': '$$\\text{Type 0: } (K, 0^\\circ) \\to 0\\angle -n(90^\\circ); \\quad \\text{Type 1: } '
                         '\\infty\\angle -90^\\circ \\to 0\\angle -n(90^\\circ); \\quad \\text{Type 2: } '
                         '\\infty\\angle -180^\\circ \\to 0\\angle -n(90^\\circ)$$',
                   'text': 'Polar plots map magnitude and phase vector locus as $\\omega: 0 \\to \\infty$. Adding a '
                           'pole introduces clockwise rotation ($-90^\\circ$ lag), shifting locus toward critical '
                           '$(-1, j0)$ and reducing stability.'},
    'lcs-q2': {   'eq': '$$F(t) = M \\ddot{x} + B \\dot{x} + K x \\longleftrightarrow e(t) = L \\ddot{q} + R \\dot{q} '
                        '+ \\frac{1}{C}q \\longleftrightarrow j(t) = C \\ddot{\\phi} + G \\dot{\\phi} + '
                        '\\frac{1}{L}\\phi$$',
                  'text': '<strong>F-V Analogy (Mesh):</strong> $F \\leftrightarrow v, M \\leftrightarrow L, B '
                          '\\leftrightarrow R, K \\leftrightarrow 1/C, v \\leftrightarrow i, x \\leftrightarrow '
                          'q$.<br><strong>F-I Analogy (Nodal):</strong> $F \\leftrightarrow i, M \\leftrightarrow C, B '
                          '\\leftrightarrow G=1/R, K \\leftrightarrow 1/L, v \\leftrightarrow v_n, x \\leftrightarrow '
                          '\\phi$.'},
    'lcs-q20': {   'eq': '$$N = P - Z \\implies Z = P - N \\implies Z = P - N_{ccw}; \\quad \\text{Closed-loop '
                         'stability requires } Z = 0 \\implies N_{ccw} = P$$',
                   'text': 'Nyquist stability theorem maps s-plane contour into $G(s)H(s)$ plane. The number of '
                           'counter-clockwise encirclements of $(-1, j0)$ must equal the number of open-loop RHP poles '
                           '$P$ for closed-loop stability.'},
    'lcs-q21': {   'eq': '$$G_{lead}(s) = \\frac{s + 1/T}{s + 1/(\\alpha T)}, \\quad \\sin\\phi_m = '
                         '\\frac{1-\\alpha}{1+\\alpha}, \\quad \\omega_m = \\frac{1}{T\\sqrt{\\alpha}}, \\quad 0 < '
                         '\\alpha < 1$$',
                   'text': 'Lead compensators place zero closer to origin than pole ($\\alpha < 1$), providing maximum '
                           'phase lead $\\phi_m = \\sin^{-1}(\\frac{1-\\alpha}{1+\\alpha})$ at geometric mean '
                           'frequency $\\omega_m = 1/(T\\sqrt{\\alpha})$ to boost bandwidth and damping.'},
    'lcs-q22': {   'eq': '$$\\phi_m = \\gamma_{spec} - \\gamma_{un} + \\epsilon, \\quad \\alpha = '
                         '\\frac{1-\\sin\\phi_m}{1+\\sin\\phi_m}, \\quad 20\\log_{10}|G_1(j\\omega_m)| = '
                         '-10\\log_{10}(1/\\alpha)$$',
                   'text': 'Lead compensator design on Bode plot selects required lead $\\phi_m$ with safety margin '
                           '$\\epsilon \\approx 5^\\circ$, calculates $\\alpha$, finds new crossover $\\omega_m = '
                           "\\omega'_{gc}$ at $-10\\log_{10}(1/\\alpha) \\text{ dB}$, and sets corner frequencies."},
    'lcs-q23': {   'eq': "$$\\phi_{plant}(\\omega'_{gc}) = -180^\\circ + \\gamma_{spec} + \\epsilon, \\quad \\beta = "
                         '10^{\\frac{|G_1|_{\\text{dB}}}{20}}, \\quad \\omega_z = \\frac{1}{T} = '
                         "\\frac{\\omega'_{gc}}{10}, \\quad \\omega_p = \\frac{\\omega_z}{\\beta}$$",
                   'text': "Lag compensator design identifies frequency $\\omega'_{gc}$ where plant phase provides "
                           'required margin $+ \\epsilon$, attenuates gain by $\\beta$, and places zero one decade '
                           "below $\\omega'_{gc}$ to minimize phase degradation."},
    'lcs-q24': {   'eq': '$$\\dot{\\mathbf{x}}(t) = A \\mathbf{x}(t) + B \\mathbf{u}(t), \\quad \\mathbf{y}(t) = C '
                         '\\mathbf{x}(t) + D \\mathbf{u}(t), \\quad \\mathbf{x}(t) \\in \\mathbb{R}^n$$',
                   'text': 'State-space represents $n$-th order dynamic systems via coupled first-order vector '
                           'differential equations, accommodating MIMO architectures, initial conditions, '
                           'non-linearities, and internal state observability.'},
    'lcs-q25': {   'eq': '$$G(s) = C (s I - A)^{-1} B + D = \\frac{C \\operatorname{adj}(s I - A) B}{\\det(s I - A)} + '
                         'D$$',
                   'text': 'Taking Laplace transforms with zero initial conditions relates state-space to transfer '
                           'functions, proving that transfer function poles are identically the eigenvalues of state '
                           'matrix $A$ ($\\det(sI-A)=0$).'},
    'lcs-q26': {   'eq': '$$\\Phi(t) = e^{At} = \\mathcal{L}^{-1}\\{(s I - A)^{-1}\\}, \\quad \\Phi(0) = I, \\quad '
                         '\\Phi^{-1}(t) = \\Phi(-t), \\quad \\Phi(t_1 + t_2) = \\Phi(t_1)\\Phi(t_2)$$',
                   'text': 'State transition matrix $\\Phi(t) = e^{At}$ maps initial state $x(0)$ to future autonomous '
                           'trajectory $x(t) = \\Phi(t)x(0)$. Evaluated via inverse Laplace transform of the resolvent '
                           'matrix $(sI - A)^{-1}$.'},
    'lcs-q3': {   'eq': '$$\\begin{bmatrix} M_1 s^2 + (B_1 + B_2)s + (K_1 + K_2) & -(B_2 s + K_2) \\\\ -(B_2 s + K_2) '
                        '& M_2 s^2 + (B_2 + B_3)s + K_2 \\end{bmatrix} \\begin{bmatrix} X_1(s) \\\\ X_2(s) '
                        '\\end{bmatrix} = \\begin{bmatrix} F(s) \\\\ 0 \\end{bmatrix}$$',
                  'text': 'Coupled mechanical systems produce an impedance matrix whose determinant $\\Delta(s) = 0$ '
                          'yields the characteristic equation, with transfer function $\\frac{X_2(s)}{F(s)} = '
                          '\\frac{B_2 s + K_2}{\\Delta(s)}$.'},
    'lcs-q4': {   'eq': '$$\\frac{C(s)}{R(s)} = \\frac{G(s)}{1 \\pm G(s)H(s)}, \\quad \\frac{C(s)}{R(s)} = \\frac{G_1 '
                        'G_2 G_3 G_4}{1 + G_3 H_1 + G_2 G_3 G_4 H_2 + G_1 G_2 G_3 G_4}$$',
                  'text': 'Block diagram reduction simplifies multi-loop topologies by combining series blocks ($G_1 '
                          'G_2$), parallel blocks ($G_1 \\pm G_2$), and closing negative feedback loops ($G / (1 + '
                          'GH)$).'},
    'lcs-q5': {   'eq': '$$T = \\frac{1}{\\Delta} \\sum_{k=1}^N P_k \\Delta_k, \\quad \\Delta = 1 - \\sum L_a + \\sum '
                        'L_b L_c - \\sum L_d L_e L_f + \\dots$$',
                  'text': "Mason's Gain Formula computes transfer functions by graph inspection without block algebra, "
                          'where $P_k$ is forward path gain, $\\Delta$ is graph determinant, and $\\Delta_k$ is the '
                          'non-touching cofactor of path $k$.'},
    'lcs-q6': {   'eq': '$$c(t) = 1 - e^{-t/T}, \\quad c(T) = 63.2\\%, \\quad c(2T) = 86.5\\%, \\quad c(3T) = 95.0\\%, '
                        '\\quad c(4T) = 98.2\\%$$',
                  'text': 'A first-order step response approaches unity exponentially, reaching 63.2% of its final '
                          'value in one time constant $T$ and entering the 2% tolerance band at $t = 4T$.'},
    'lcs-q7': {   'eq': '$$c(t) = 1 - \\frac{e^{-\\zeta \\omega_n t}}{\\sqrt{1 - \\zeta^2}} \\sin(\\omega_d t + '
                        '\\theta), \\quad \\omega_d = \\omega_n \\sqrt{1 - \\zeta^2}, \\quad \\theta = '
                        '\\cos^{-1}(\\zeta) = \\tan^{-1}\\left(\\frac{\\sqrt{1-\\zeta^2}}{\\zeta}\\right)$$',
                  'text': 'Underdamped second-order step response ($0 < \\zeta < 1$) consists of a constant target of '
                          '1 enveloped by an exponentially decaying sinusoidal oscillation with damping rate '
                          '$\\zeta\\omega_n$ and frequency $\\omega_d$.'},
    'lcs-q8': {   'eq': '$$t_r = \\frac{\\pi - \\theta}{\\omega_d}, \\quad t_p = \\frac{\\pi}{\\omega_d}, \\quad M_p = '
                        'e^{-\\frac{\\pi\\zeta}{\\sqrt{1-\\zeta^2}}} \\times 100\\%, \\quad t_s(2\\%) = '
                        '\\frac{4}{\\zeta\\omega_n}, \\quad t_s(5\\%) = \\frac{3}{\\zeta\\omega_n}$$',
                  'text': 'Peak overshoot $M_p$ depends strictly on damping ratio $\\zeta$ alone, peak time $t_p$ '
                          'depends on damped frequency $\\omega_d$, and settling time $t_s$ is inversely proportional '
                          'to attenuation factor $\\zeta\\omega_n$.'},
    'lcs-q9': {   'eq': '$$e_{ss} = \\lim_{s \\to 0} \\frac{s R(s)}{1 + G(s)H(s)}; \\quad K_p = \\lim_{s\\to 0} GH, '
                        '\\quad K_v = \\lim_{s\\to 0} s GH, \\quad K_a = \\lim_{s\\to 0} s^2 GH$$',
                  'text': '<strong>Type 0:</strong> $e_{ss}(\\text{step}) = 1/(1+K_p), e_{ss}(\\text{ramp}) = '
                          '\\infty$.<br><strong>Type 1:</strong> $e_{ss}(\\text{step}) = 0, e_{ss}(\\text{ramp}) = '
                          '1/K_v, e_{ss}(\\text{para}) = \\infty$.<br><strong>Type 2:</strong> $e_{ss}(\\text{step}) = '
                          '0, e_{ss}(\\text{ramp}) = 0, e_{ss}(\\text{para}) = 1/K_a$.'},
    'mech-q1': {   'eq': '$$R = \\sqrt{(\\Sigma F_x)^2 + (\\Sigma F_y)^2}, \\quad \\tan\\theta_R = '
                         '\\left|\\frac{\\Sigma F_y}{\\Sigma F_x}\\right|, \\quad \\Sigma F_x = 0, \\; \\Sigma F_y = '
                         '0$$',
                   'text': '<strong>Parallelogram Law:</strong> $R = \\sqrt{P^2 + Q^2 + 2PQ\\cos\\theta}$, '
                           '$\\tan\\alpha = \\frac{Q\\sin\\theta}{P + Q\\cos\\theta}$.<br><strong>Transmissibility '
                           'Principle:</strong> Point of application can slide along line of action on a rigid body '
                           'without altering external equilibrium.<br><strong>Cartesian Resolution:</strong> $R = '
                           '\\sqrt{(\\Sigma F_x)^2 + (\\Sigma F_y)^2}$.<br><strong>Equilibrium:</strong> Resultant '
                           'must vanish ($\\Sigma F_x = 0$, $\\Sigma F_y = 0$).'},
    'mech-q10': {   'eq': '$$m = 2j - 3 \\text{ (Perfect Truss)}, \\quad \\Sigma F_x = 0, \\; \\Sigma F_y = 0 \\text{ '
                          '(Joints)}, \\quad \\Sigma M_O = 0 \\text{ (Sections)}$$',
                    'text': '<strong>Truss Assumptions:</strong> Frictionless pin joints, concurrent axes, axial loads '
                            'only ($T$ tension or $C$ compression).<br><strong>Zero-Force Members:</strong> Two '
                            'non-collinear members meeting at unloaded joint carry zero force; two collinear plus one '
                            'third non-collinear $\\implies$ third is zero.<br><strong>Method of Joints:</strong> '
                            'Analyzes joint by joint ($\\Sigma F_x=0, \\Sigma F_y=0$).<br><strong>Method of '
                            'Sections:</strong> Cuts across up to 3 members; solves with $\\Sigma M_O = 0$.'},
    'mech-q11': {   'eq': '$$\\bar{x} = \\frac{\\sum A_i x_i}{\\sum A_i}, \\quad \\bar{y} = \\frac{\\sum A_i '
                          'y_i}{\\sum A_i}, \\quad Q_x = \\int y \\, dA = A \\bar{y}$$',
                    'text': '<strong>Centroid of Area:</strong> Geometric center based on first moment of area: $A '
                            '\\bar{y} = \\Sigma A_i y_i$.<br><strong>Axis of Symmetry:</strong> If a section possesses '
                            'an axis of symmetry, the centroid must lie on that axis.<br><strong>Composite '
                            'T-Section:</strong> Web ($20\\times 180$) and Flange ($150\\times 20$) give total area '
                            '$6600\\text{ mm}^2$ and $\\bar{y} = \\frac{894,000}{6600} = 135.45\\text{ mm}$ from '
                            'base.'},
    'mech-q12': {   'eq': '$$A = 2\\pi \\bar{y} L \\quad (\\text{Theorem 1}), \\quad V = 2\\pi \\bar{y} A \\quad '
                          '(\\text{Theorem 2})$$',
                    'text': '<strong>Pappus Theorem 1:</strong> Surface area of revolution equals curve length $L$ '
                            'times distance traveled by its centroid ($2\\pi \\bar{y} L$).<br><strong>Pappus Theorem '
                            '2:</strong> Volume of revolution equals plane area $A$ times distance traveled by its '
                            'centroid ($2\\pi \\bar{y} A$).<br><strong>Applications:</strong> Sphere ($A = 4\\pi R^2, '
                            'V = \\frac{4}{3}\\pi R^3$), Cone ($V = \\frac{1}{3}\\pi R^2 h$).'},
    'mech-q13': {   'eq': '$$I_{AB} = I_G + A d^2 \\quad (\\text{Parallel Axis}), \\quad I_{zz} = I_{xx} + I_{yy} '
                          '\\quad (\\text{Perpendicular Axis})$$',
                    'text': "<strong>Parallel Axis Theorem:</strong> $I_{AB} = I_G + A d^2$; first moment $\\int y' dA "
                            '= 0$ about centroid.<br><strong>Perpendicular Axis Theorem:</strong> $I_{zz} = I_{xx} + '
                            'I_{yy}$; valid strictly for planar 2D laminas.<br><strong>Radius of Gyration:</strong> $k '
                            '= \\sqrt{I/A} \\implies I = A k^2$.'},
    'mech-q14': {   'eq': '$$I_{xx} = \\sum \\left( \\frac{b_i h_i^3}{12} + A_i d_i^2 \\right) \\approx 54.82 \\times '
                          '10^6\\text{ mm}^4, \\quad I_{yy} = \\sum \\frac{h_i b_i^3}{12} \\approx 16.26 \\times '
                          '10^6\\text{ mm}^4$$',
                    'text': '<strong>I-Section Centroidal MOI:</strong> Calculate $\\bar{y}$ using first moments, then '
                            'apply parallel axis theorem to each rectangle: $I_{xx} = I_G + A '
                            'd^2$.<br><strong>Symmetry about Y-Axis:</strong> All $d_x = 0 \\implies I_{yy} = \\sum '
                            '\\frac{h b^3}{12}$.<br><strong>Radii of Gyration:</strong> $k_{xx} = \\sqrt{I_{xx}/A} '
                            '\\approx 78.93\\text{ mm}$, $k_{yy} = \\sqrt{I_{yy}/A} \\approx 42.98\\text{ mm}$.'},
    'mech-q15': {   'eq': '$$I_{\\text{rod}, G} = \\frac{1}{12} m L^2, \\quad I_{\\text{rod}, \\text{end}} = '
                          '\\frac{1}{3} m L^2, \\quad I_{\\text{disc}, z} = \\frac{1}{2} m R^2, \\quad '
                          'I_{\\text{disc}, d} = \\frac{1}{4} m R^2$$',
                    'text': '<strong>Mass Moment of Inertia:</strong> $I = \\int r^2 dm$, measures resistance to '
                            'angular acceleration ($T = I \\alpha$).<br><strong>Slender Rod:</strong> Centroidal '
                            'transverse axis $I_G = \\frac{1}{12} m L^2$; about one end $I = I_G + m(L/2)^2 = '
                            '\\frac{1}{3} m L^2$.<br><strong>Circular Disc:</strong> Polar axis $I_z = \\frac{1}{2} m '
                            'R^2$; diameter axis $I_d = \\frac{1}{4} m R^2$ (perpendicular axis theorem).'},
    'mech-q16': {   'eq': '$$a = \\frac{dv}{dt} = v \\frac{dv}{ds}, \\quad a = -k v \\implies v(t) = v_0 e^{-k t}, '
                          '\\quad s(t) = \\frac{v_0}{k}(1 - e^{-k t}), \\quad s_{max} = \\frac{v_0}{k}$$',
                    'text': '<strong>Variable Acceleration:</strong> Use $v = ds/dt$, $a = dv/dt$, or $v \\, dv = a '
                            '\\, ds$ based on independent variables.<br><strong>Linear Drag ($a = -kv$):</strong> '
                            'Velocity decays exponentially $v = v_0 e^{-kt}$.<br><strong>Stopping Distance:</strong> '
                            'Particle comes to rest asymptotically with total distance $s_{max} = v_0/k$.'},
    'mech-q17': {   'eq': '$$y = x \\tan\\theta - \\frac{g x^2}{2 u^2 \\cos^2\\theta}, \\quad T = \\frac{2 u '
                          '\\sin\\theta}{g}, \\quad H = \\frac{u^2 \\sin^2\\theta}{2g}, \\quad R = \\frac{u^2 '
                          '\\sin(2\\theta)}{g}$$',
                    'text': '<strong>Parabolic Trajectory:</strong> Eliminating time $t$ gives $y = x\\tan\\theta - '
                            '\\frac{gx^2}{2u^2\\cos^2\\theta}$.<br><strong>Time of Flight:</strong> $T = '
                            '\\frac{2u\\sin\\theta}{g}$ ($y=0$).<br><strong>Max Height:</strong> $H = '
                            '\\frac{u^2\\sin^2\\theta}{2g}$ ($v_y=0$).<br><strong>Horizontal Range:</strong> $R = '
                            '\\frac{u^2\\sin 2\\theta}{g}$; maximum range occurs at $\\theta = 45^\\circ$ ($R_{max} = '
                            'u^2/g$).'},
    'mech-q18': {   'eq': '$$\\mathbf{a} = a_t \\hat{\\mathbf{e}}_t + a_n \\hat{\\mathbf{e}}_n = \\frac{dv}{dt} '
                          '\\hat{\\mathbf{e}}_t + \\frac{v^2}{\\rho} \\hat{\\mathbf{e}}_n, \\quad a = \\sqrt{a_t^2 + '
                          'a_n^2}$$',
                    'text': '<strong>Tangential Acceleration ($a_t$):</strong> $a_t = \\frac{dv}{dt} = '
                            'v\\frac{dv}{ds}$, measures rate of change of speed along path tangent.<br><strong>Normal '
                            'Acceleration ($a_n$):</strong> $a_n = \\frac{v^2}{\\rho}$, measures rate of change of '
                            'direction, always directed inward toward center of '
                            'curvature.<br><strong>Curvature:</strong> $\\rho$ is radius of curvature; $a_n = 0$ only '
                            'for straight path ($\\rho \\to \\infty$).'},
    'mech-q19': {   'eq': '$$\\Sigma \\mathbf{F} + (-m \\mathbf{a}) = 0 \\implies \\Sigma \\mathbf{F} + \\mathbf{F}_i '
                          '= 0, \\quad a = \\left(\\frac{m_1 - m_2}{m_1 + m_2}\\right) g, \\quad T = \\left(\\frac{2 '
                          'm_1 m_2}{m_1 + m_2}\\right) g$$',
                    'text': "<strong>D'Alembert's Principle:</strong> Dynamic systems brought to static equilibrium by "
                            'adding reverse inertia force $\\mathbf{F}_i = -m\\mathbf{a}$.<br><strong>Accelerating '
                            'Elevator:</strong> Upward $\\implies N = m(g+a)$; Downward $\\implies N = m(g-a)$; Free '
                            'fall $\\implies N = 0$.<br><strong>Atwood Machine:</strong> Common acceleration $a = '
                            '\\frac{m_1 - m_2}{m_1 + m_2}g$, string tension $T = \\frac{2m_1 m_2}{m_1 + m_2}g$.'},
    'mech-q2': {   'eq': '$$\\frac{F_1}{\\sin\\alpha} = \\frac{F_2}{\\sin\\beta} = \\frac{F_3}{\\sin\\gamma}, \\quad T '
                         '= W \\frac{l + r}{\\sqrt{l^2 + 2lr}}, \\quad R_w = W \\frac{r}{\\sqrt{l^2 + 2lr}}$$',
                   'text': "<strong>Lami's Theorem:</strong> For 3 concurrent coplanar forces in equilibrium, each "
                           'force is proportional to the sine of the angle between the other two.<br><strong>Closed '
                           'Triangle:</strong> Proved using the Sine Rule on the closed force triangle ($\\Delta '
                           'ABC$).<br><strong>Suspended Sphere:</strong> Normal reaction $R_w = W\\tan\\theta$, '
                           'Tension $T = W/\\cos\\theta$ where $\\sin\\theta = \\frac{r}{l+r}$.'},
    'mech-q20': {   'eq': '$$a = \\frac{m_2 - m_1(\\sin\\alpha + \\mu \\cos\\alpha)}{m_1 + m_2} g, \\quad T = '
                          '\\frac{m_1 m_2 g}{m_1 + m_2}(1 + \\sin\\alpha + \\mu \\cos\\alpha)$$',
                    'text': '<strong>Connected Incline Dynamics:</strong> Normal reaction $N = m_1 g \\cos\\alpha$; '
                            'friction $F_k = \\mu m_1 g \\cos\\alpha$.<br><strong>Force Balance:</strong> $T - m_1 '
                            'g\\sin\\alpha - \\mu m_1 g\\cos\\alpha = m_1 a$, and $m_2 g - T = m_2 '
                            'a$.<br><strong>Motion Threshold:</strong> Mass accelerates up incline only if $m_2 > '
                            'm_1(\\sin\\alpha + \\mu\\cos\\alpha)$.'},
    'mech-q21': {   'eq': '$$U_{1-2} = \\int_1^2 \\mathbf{F} \\cdot d\\mathbf{r} = T_2 - T_1 = \\frac{1}{2} m v_2^2 - '
                          '\\frac{1}{2} m v_1^2 = \\Delta KE$$',
                    'text': '<strong>Work Done:</strong> $U = \\int \\mathbf{F}\\cdot d\\mathbf{r}$; Gravity $U_g = '
                            '-mg(y_2 - y_1)$; Spring $U_s = -\\frac{1}{2}k(x_2^2 - x_1^2)$.<br><strong>Work-Energy '
                            'Theorem:</strong> $F_t = m v \\frac{dv}{ds} \\implies \\int F_t ds = \\int mv dv '
                            '\\implies U_{1-2} = T_2 - T_1$.<br><strong>Key Advantage:</strong> Directly links force '
                            'and displacement without calculating elapsed time.'},
    'mech-q22': {   'eq': '$$\\oint \\mathbf{F}\\cdot d\\mathbf{r} = 0, \\quad \\mathbf{F} = -\\nabla V, \\quad T_1 + '
                          'V_1 = T_2 + V_2 = E_{\\text{total}} = \\text{constant}$$',
                    'text': '<strong>Conservative Force:</strong> Work done is path-independent ($\\nabla \\times '
                            '\\mathbf{F} = 0$); derived from potential $F = -\\nabla V$.<br><strong>Conservation of '
                            'Mechanical Energy:</strong> When non-conservative forces do no work, $T_1 + V_1 = T_2 + '
                            'V_2$.<br><strong>Simple Pendulum:</strong> Velocity at angle $\\theta$ is $v = '
                            '\\sqrt{2gl(\\cos\\theta - \\cos\\theta_0)}$; cord tension does zero work.'},
    'mech-q23': {   'eq': '$$\\mathbf{J}_{1-2} = \\int_{t_1}^{t_2} \\mathbf{F} \\, dt = m \\mathbf{v}_2 - m '
                          '\\mathbf{v}_1 = \\Delta \\mathbf{p}, \\quad R_{jet, x} = \\rho A v^2 (1 - \\cos\\beta)$$',
                    'text': '<strong>Linear Impulse:</strong> $\\mathbf{J} = \\int \\mathbf{F} dt = '
                            '\\Delta(m\\mathbf{v})$; equals area under $F-t$ curve.<br><strong>Impulsive '
                            'Forces:</strong> Large forces over tiny $\\Delta t$; gravity/friction neglected during '
                            'impact.<br><strong>Fluid Jet on Vane:</strong> Force on fluid is '
                            '$\\dot{m}(\\mathbf{v}_{out} - \\mathbf{v}_{in})$; jet force on semicircular cup ($\\beta '
                            '= 180^\\circ$) is $2\\rho A v^2$.'},
    'mech-q24': {   'eq': '$$\\Sigma \\mathbf{F}^{ext} = \\frac{d\\mathbf{P}}{dt} = 0 \\implies \\mathbf{P} = \\sum '
                          'm_i \\mathbf{v}_i = \\text{constant}, \\quad V_R = -\\left(\\frac{m}{M}\\right) v_b$$',
                    'text': '<strong>Linear Momentum Conservation:</strong> Internal forces cancel in pairs ($\\Sigma '
                            '\\mathbf{f}_{ij} = 0$). If $\\Sigma \\mathbf{F}^{ext} = 0$, total momentum is '
                            'conserved.<br><strong>Recoil Velocity:</strong> Firing projectile with muzzle speed $v_b$ '
                            'imparts cannon recoil $V_R = -(m/M)v_b$.<br><strong>Generality:</strong> Strictly '
                            'conserved regardless of whether mechanical energy is lost.'},
    'mech-q25': {   'eq': '$$e = \\frac{v_2 - v_1}{u_1 - u_2}, \\quad v_1 = \\frac{(m_1 - e m_2)u_1 + m_2(1+e)u_2}{m_1 '
                          '+ m_2}, \\quad v_2 = \\frac{m_1(1+e)u_1 + (m_2 - e m_1)u_2}{m_1 + m_2}$$',
                    'text': '<strong>Direct Central Impact:</strong> Centers of mass and velocities lie along the '
                            'normal line of impact.<br><strong>Restitution Coefficient ($e$):</strong> $e = '
                            '\\frac{\\text{Separation Velocity}}{\\text{Approach Velocity}} = \\frac{v_2 - v_1}{u_1 - '
                            'u_2}$.<br><strong>Special Cases:</strong> Elastic ($e = 1$) $\\implies$ equal masses '
                            'exchange velocities; Plastic ($e = 0$) $\\implies$ bodies coalesce with common velocity.'},
    'mech-q26': {   'eq': '$$\\Delta E = \\frac{m_1 m_2}{2(m_1 + m_2)} (1 - e^2) (u_1 - u_2)^2 = \\frac{1}{2} \\mu (1 '
                          '- e^2) (u_1 - u_2)^2$$',
                    'text': '<strong>Loss of Kinetic Energy:</strong> $\\Delta E = E_{initial} - E_{final} = '
                            '\\frac{m_1 m_2}{2(m_1 + m_2)}(1 - e^2)(u_1 - u_2)^2$.<br><strong>Reduced Mass:</strong> '
                            '$\\mu = \\frac{m_1 m_2}{m_1 + m_2}$.<br><strong>Regimes:</strong><br>- Perfectly Elastic '
                            '($e = 1$): $\\Delta E = 0$ (energy conserved).<br>- Inelastic ($0 < e < 1$): $\\Delta E > '
                            '0$ (dissipated as heat/sound).<br>- Perfectly Plastic ($e = 0$): Maximum energy loss.'},
    'mech-q3': {   'eq': '$$R_{AB} = \\frac{W_B}{\\sin\\theta} = 1250\\text{ N}, \\quad R_{wall} = 750\\text{ N}, '
                         '\\quad R_{floor} = W_A + W_B = 2000\\text{ N}$$',
                   'text': '<strong>Free Body Diagram (FBD):</strong> Isolate body and replace all supports with '
                           'physical reactions.<br><strong>Line of Centers:</strong> Distance between centers $d = '
                           '2R$; horizontal span $\\Delta x = L - 2R \\implies \\cos\\theta = \\Delta x / '
                           '2R$.<br><strong>Two Cylinders in Channel:</strong> Top cylinder equilibrium gives mutual '
                           'contact reaction $R_{AB} = W/\\sin\\theta$ and wall reaction $R_{wall} = '
                           'R_{AB}\\cos\\theta$.'},
    'mech-q4': {   'eq': '$$\\Sigma \\mathbf{M}_O = \\mathbf{r} \\times \\mathbf{R} \\implies \\sum_{i=1}^n F_i d_i = '
                         'R \\cdot d_R, \\quad \\mathbf{M}_{\\text{couple}} = \\mathbf{r}_{BA} \\times \\mathbf{F}$$',
                   'text': "<strong>Varignon's Theorem of Moments:</strong> The algebraic sum of moments of concurrent "
                           'forces about any point equals the moment of their resultant about that point ($\\Sigma M_O '
                           '= M_{R, O}$).<br><strong>Couple Characteristics:</strong> Net force is zero; moment $M = F '
                           '\\cdot d$ is a free vector, identical about all points.<br><strong>Force Shift:</strong> '
                           'Shifting force $F$ by perpendicular distance $d$ requires adding a couple $M = F \\cdot '
                           'd$.'},
    'mech-q5': {   'eq': '$$\\Sigma F_x = 0, \\quad \\Sigma F_y = 0, \\quad \\Sigma M_O = 0, \\quad R = \\sqrt{R_x^2 + '
                         'R_y^2}$$',
                   'text': '<strong>2D Rigid Body Equilibrium:</strong> Requires 3 independent equations ($\\Sigma F_x '
                           '= 0, \\Sigma F_y = 0, \\Sigma M = 0$).<br><strong>Support Reactions:</strong><br>- Roller: '
                           '1 normal reaction ($R_N$).<br>- Pin/Hinged: 2 orthogonal reactions ($R_x, R_y$).<br>- '
                           'Fixed: 3 reactions ($R_x, R_y, M_{\\text{fix}}$).<br><strong>UDL Conversion:</strong> '
                           'Replaced by equivalent point load $W = w \\cdot L$ at segment centroid.'},
    'mech-q6': {   'eq': '$$F_L = \\mu_s N, \\quad \\tan\\phi = \\mu_s \\implies \\phi = \\tan^{-1}\\mu_s, \\quad '
                         '\\theta_{\\text{repose}} = \\phi = \\tan^{-1}\\mu_s$$',
                   'text': "<strong>Coulomb's Friction Laws:</strong> Limiting friction $F_L = \\mu_s N$ is "
                           'independent of contact area; kinetic friction $\\mu_k < \\mu_s$.<br><strong>Angle of '
                           'Friction ($\\phi$):</strong> Angle between total reaction $R$ and normal $N$: $\\tan\\phi '
                           '= \\mu_s$.<br><strong>Angle of Repose ($\\theta$):</strong> Maximum incline angle before '
                           'sliding down under self-weight: $\\tan\\theta = \\mu_s \\implies \\theta = '
                           '\\phi$.<br><strong>Cone of Friction:</strong> Inverted cone of semi-vertex angle $\\phi$; '
                           'forces inside cone cannot cause slip.'},
    'mech-q7': {   'eq': '$$\\tan\\theta_{min} = \\frac{1 - \\mu_f \\mu_w}{2\\mu_f}, \\quad \\text{Smooth Wall: } '
                         '\\tan\\theta_{min} = \\frac{1}{2\\mu_f}, \\quad x_{max} = \\frac{N_w L(\\tan\\theta + '
                         '\\mu_w) - \\frac{W L}{2}}{W_1}$$',
                   'text': '<strong>Ladder Equilibrium:</strong> Floor friction $F_f = \\mu_f N_f \\rightarrow$, wall '
                           'reaction $N_w \\leftarrow$, wall friction $F_w = \\mu_w N_w \\uparrow$.<br><strong>Force '
                           'Balance:</strong> $N_w = \\mu_f N_f$, $N_f + \\mu_w N_w = W \\implies N_f = '
                           '\\frac{W}{1+\\mu_f\\mu_w}$.<br><strong>Minimum Angle:</strong> Taking $\\Sigma M_A = 0$ '
                           'yields $\\tan\\theta_{min} = \\frac{1 - \\mu_f\\mu_w}{2\\mu_f}$.'},
    'mech-q8': {   'eq': '$$P = W \\left[ \\frac{\\cos\\phi_1}{\\cos(\\alpha + \\phi_1 + \\phi_2)} \\right] \\left[ '
                         '\\frac{\\sin(\\alpha + \\phi_2 + \\phi_3)}{\\cos\\phi_3} \\right] \\xrightarrow{\\text{equal '
                         '}\\phi} P = W \\tan(\\alpha + 2\\phi)$$',
                   'text': '<strong>Wedge Mechanism:</strong> Translates small horizontal effort $P$ into large '
                           'vertical lifting force $W$.<br><strong>Block & Wedge Equilibrium:</strong> Reaction '
                           'between block and wedge tilts by $(\\alpha + \\phi_2)$ to the vertical.<br><strong>Minimum '
                           'Driving Force:</strong> $P = W\\tan(\\alpha + 2\\phi)$ for equal friction angle '
                           '$\\phi$.<br><strong>Self-Locking:</strong> Wedge will not slip back when $P=0$ if $\\alpha '
                           '< 2\\phi$.'},
    'mech-q9': {   'eq': '$$\\frac{T_1}{T_2} = e^{\\mu \\theta}, \\quad P = (T_1 - T_2)v = T_1(1 - e^{-\\mu\\theta})v, '
                         '\\quad T_c = m v^2$$',
                   'text': '<strong>Flat Belt Tension Ratio:</strong> $\\frac{T_1}{T_2} = e^{\\mu\\theta}$ where '
                           '$\\theta$ is wrap angle in radians.<br><strong>Power Transmitted:</strong> $P = (T_1 - '
                           'T_2)v$ where pitch speed $v = \\frac{\\pi D N}{60}\\text{ m/s}$.<br><strong>Centrifugal '
                           'Tension:</strong> $T_c = m v^2$; reduces grip $\\frac{T_1 - T_c}{T_2 - T_c} = '
                           'e^{\\mu\\theta}$; maximum power occurs when $T_c = T_{max}/3$.'},
    'mgt-q1': {   'eq': '$$\\text{Taylor: Science, not rule of thumb; Harmony, not discord; Cooperation; Development '
                        'of each man.}$$',
                  'text': 'F.W. Taylor pioneered Scientific Management: time and motion studies, functional '
                          'foremanship (8 specialized bosses), differential piece-rate incentive wages, and the Mental '
                          'Revolution aligning labor and capital.'},
    'mgt-q10': {   'eq': '$$NT = OT \\times \\left(\\frac{PR}{100}\\right), \\quad ST = NT_{total} \\times (1 + A) = '
                         'NT_{total} + \\text{Allowances}$$',
                   'text': '<strong>Time Study Derivation:</strong> Normal Time adjusts observed time by performance '
                           'rating ($PR$). Adding percentage allowances ($A\\%$: relaxation, personal, fatigue, '
                           'contingency) yields Standard Time ($ST$).'},
    'mgt-q11': {   'eq': '$$EOQ = Q^* = \\sqrt{\\frac{2 D S}{H}}, \\quad TIC^* = \\sqrt{2 D S H}, \\quad AOC = AHC \\ '
                         '(\\text{at } EOQ)$$',
                   'text': '<strong>Wilson EOQ Derivation:</strong> Minimizes total inventory cost by equating annual '
                           'ordering cost ($D S / Q$) to annual holding cost ($Q H / 2$). Second derivative is '
                           'strictly positive, verifying global minimum.'},
    'mgt-q12': {   'eq': '$$\\text{ABC: Pareto 80/20 Rule}; \\quad \\text{VED: Vital/Essential/Desirable}; \\quad '
                         '\\text{FSN: Fast/Slow/Non-moving}$$',
                   'text': '<strong>ABC Analysis:</strong> Category A ($10-20\\%$ items, $70-80\\%$ value, tightest '
                           'control); B ($20-30\\%$ items, $20\\%$ value); C ($50-70\\%$ items, $10\\%$ '
                           'value).<br><strong>VED:</strong> Spares criticality for maintenance.'},
    'mgt-q13': {   'eq': '$$k = \\frac{D \\cdot L (1 + \\alpha)}{C}, \\quad \\text{Seven Wastes: Muda of '
                         'Overproduction, Waiting, Transport...}$$',
                   'text': '<strong>JIT Philosophy:</strong> Pull system eliminating 7 wastes (Muda). Dual-card Kanban '
                           '(P-Kanban and C-Kanban) pulls standard containers only upon customer demand, preventing '
                           'overproduction.'},
    'mgt-q14': {   'eq': '$$\\text{Six Sigma: } 3.4 \\text{ DPMO } (6\\sigma); \\quad \\text{DMAIC: Define, Measure, '
                         'Analyze, Improve, Control}$$',
                   'text': '<strong>TQM:</strong> Deming 14 points, PDCA cycle, customer focus, Kaizen.<br><strong>Six '
                           'Sigma:</strong> Variation reduction yielding 3.4 defects per million opportunities via '
                           'DMAIC.<br><strong>ISO 9001:</strong> Certified Quality Management System.'},
    'mgt-q15': {   'eq': '$$UCL/LCL = \\bar{\\bar{X}} \\pm A_2 \\bar{R}, \\quad C_p = \\frac{USL - LSL}{6\\sigma}, '
                         '\\quad C_{pk} = \\min\\left[\\frac{USL - \\mu}{3\\sigma}, \\frac{\\mu - '
                         'LSL}{3\\sigma}\\right]$$',
                   'text': '<strong>SQC:</strong> Distinguishes common from assignable causes using $\\pm 3\\sigma$ '
                           'control limits.<br><strong>Capability:</strong> $C_p$ measures potential spread; $C_{pk} '
                           '\\ge 1.33$ accounts for process mean shifts.'},
    'mgt-q16': {   'eq': '$$\\text{Marketing Mix: 4 Ps (Product, Price, Place, Promotion)} + \\text{People, Process, '
                         'Physical Evidence (7 Ps)}$$',
                   'text': 'Marketing satisfies consumer needs profitably. STP framework segments heterogeneous '
                           'markets, targets profitable segments, and positions the brand distinctly on perceptual '
                           'maps.'},
    'mgt-q17': {   'eq': '$$\\text{PLC Stages: Introduction (Loss)} \\to \\text{Growth (Max Margin)} \\to '
                         '\\text{Maturity (Peak Sales)} \\to \\text{Decline}$$',
                   'text': 'Product Life Cycle traces sales and profit curves across 4 stages, guiding strategic '
                           'pricing (skimming vs penetration), advertising focus, product modifications, and '
                           'harvesting/divestment.'},
    'mgt-q18': {   'eq': '$$\\text{HRM: Planning} \\to \\text{Recruitment} \\to \\text{Selection} \\to '
                         '\\text{Induction} \\to \\text{Training (OJT / Off-JT)}$$',
                   'text': 'Recruitment attracts applicants (internal vs external); scientific selection uses tests '
                           'and panel interviews to screen candidates. Training encompasses on-the-job (JIT, rotation) '
                           'and off-the-job (vestibule, simulation).'},
    'mgt-q19': {   'eq': '$$\\text{Job Analysis} = \\text{Job Description (JD: Tasks)} + \\text{Job Specification (JS: '
                         'Human Specs)}$$',
                   'text': '<strong>Job Description:</strong> Duties, tools, working conditions.<br><strong>Job '
                           'Specification:</strong> Required qualifications and skills.<br><strong>Appraisal:</strong> '
                           '360-degree multi-rater feedback and Drucker Management by Objectives (MBO).'},
    'mgt-q2': {   'eq': '$$\\text{Unity of Command: 1 Employee} \\to 1 \\text{ Boss}; \\quad \\text{Gangplank: Direct '
                        'Cross-Communication}$$',
                  'text': 'Henri Fayol articulated 14 principles of administrative management, including Division of '
                          'Work, Authority and Responsibility, Unity of Command (one boss), Unity of Direction, Scalar '
                          'Chain, and the Gangplank communication bypass.'},
    'mgt-q20': {   'eq': '$$\\text{Maslow (Needs Hierarchy)} \\leftrightarrow \\text{Herzberg (Hygiene vs Motivators)} '
                         '\\leftrightarrow \\text{McGregor (Theory X vs Y)}$$',
                   'text': '<strong>Maslow:</strong> 5-tier pyramid of needs.<br><strong>Herzberg:</strong> Hygiene '
                           'factors prevent dissatisfaction; intrinsic motivators drive '
                           'satisfaction.<br><strong>McGregor:</strong> Theory X (authoritarian) vs Theory Y '
                           '(participative empowerment).'},
    'mgt-q21': {   'eq': '$$\\text{Assets} = \\text{Liabilities} + \\text{Equity}, \\quad W = \\sum_{t=1}^n '
                         '\\frac{CF_t}{(1 + k)^t} - I_0$$',
                   'text': '<strong>Wealth Maximization:</strong> Superior to profit maximization by discounting cash '
                           'flows.<br><strong>Capital Sources:</strong> Equity shares, debentures, retained earnings, '
                           'term loans.<br><strong>Financial Statements:</strong> Balance sheet and P&L income '
                           'statement.'},
    'mgt-q22': {   'eq': '$$Q_{BEP} = \\frac{FC}{P - v} = \\frac{FC}{C}, \\quad S_{BEP} = \\frac{FC}{P/V \\text{ '
                         'Ratio}}, \\quad MoS \\% = \\frac{S_{actual} - S_{BEP}}{S_{actual}} \\times 100\\%$$',
                   'text': '<strong>Break-Even Point:</strong> Zero-profit sales volume where total revenue equals '
                           'total costs ($FC + v \\cdot Q$). Contribution margin $C = P - v$. Margin of Safety ($MoS$) '
                           'measures cushion above BEP.'},
    'mgt-q23': {   'eq': '$$NPV = \\sum_{t=1}^n \\frac{CF_t}{(1 + k)^t} - I_0 > 0, \\quad \\sum_{t=1}^n '
                         '\\frac{CF_t}{(1 + IRR)^t} - I_0 = 0, \\quad PI = \\frac{PV}{I_0}$$',
                   'text': 'Capital budgeting evaluates long-term investments. Non-discounted Payback Period ignores '
                           'post-payback cash flows. Modern DCF criteria prioritize Net Present Value ($NPV$), '
                           'Internal Rate of Return ($IRR$), and Profitability Index ($PI$).'},
    'mgt-q24': {   'eq': '$$E_j = \\max[E_i + t_{ij}], \\quad L_i = \\min[L_j - t_{ij}], \\quad TF = (L_j - E_i) - '
                         't_{ij} = 0 \\ (\\text{Critical Path})$$',
                   'text': '<strong>CPM Network Analysis:</strong> Forward pass finds earliest times ($E_j$); backward '
                           'pass finds latest times ($L_i$). The Critical Path is the longest path through the '
                           'network, defined by activities with Zero Total Float ($TF = 0$).'},
    'mgt-q25': {   'eq': '$$t_e = \\frac{t_o + 4 t_m + t_p}{6}, \\quad \\sigma^2 = \\left(\\frac{t_p - '
                         't_o}{6}\\right)^2, \\quad Z = \\frac{T_s - T_e}{\\sigma_p}$$',
                   'text': '<strong>PERT Probabilistic Analysis:</strong> Three time estimates ($t_o, t_m, t_p$) '
                           'follow a Beta distribution. Total project variance is the sum of critical path variances. '
                           'Standard normal $Z$-score gives the probability of meeting target date $T_s$.'},
    'mgt-q26': {   'eq': '$$\\text{Cost Slope} = \\frac{CC - NC}{NT - CT}, \\quad \\text{Total Cost} = \\text{Direct '
                         'Cost} + \\text{Indirect Cost}$$',
                   'text': '<strong>Project Crashing:</strong> Expedites critical activities having the lowest cost '
                           'slope. Compressing project duration increases direct costs but decreases indirect overhead '
                           'costs, optimizing total project cost.'},
    'mgt-q3': {   'eq': '$$\\text{POSDCORB} = \\text{Planning, Organizing, Staffing, Directing, Coordinating, '
                        'Reporting, Budgeting}$$',
                  'text': 'Luther Gulick synthesized management functions into POSDCORB. Rational decision-making '
                          'evaluates alternatives under certainty ($100\\%$ known), risk (probabilistic $EMV = \\sum '
                          'p_i X_i$), and uncertainty.'},
    'mgt-q4': {   'eq': '$$\\text{Matrix Org: Dual Authority (Functional Manager } \\times \\text{ Project Manager)}$$',
                  'text': '<strong>Line Org:</strong> Rigid scalar chain, pure unity of command.<br><strong>Line & '
                          'Staff:</strong> Advisory specialists counsel executive line '
                          'managers.<br><strong>Matrix:</strong> High-flexibility dual-reporting structure for complex '
                          'technical projects.'},
    'mgt-q5': {   'eq': '$$\\text{Carroll Pyramid: Philanthropic (Apex)} \\to \\text{Ethical} \\to \\text{Legal} \\to '
                        '\\text{Economic (Base)}$$',
                  'text': 'CSR mandates corporate citizenship (India Companies Act: $2\\%$ net profit). Engineering '
                          'ethics mandates holding public safety paramount, avoiding conflicts of interest, and '
                          'protecting whistleblowers.'},
    'mgt-q6': {   'eq': '$$X^* = \\frac{\\sum x_i W_i}{\\sum W_i}, \\quad Y^* = \\frac{\\sum y_i W_i}{\\sum W_i}, '
                        '\\quad MI = \\frac{\\text{Weight of Raw Materials}}{\\text{Weight of Product}}$$',
                  'text': '<strong>Location Factors:</strong> Raw material proximity, market access, power, labor, '
                          'incentives.<br><strong>Models:</strong> Factor Rating weighted score, Center of Gravity '
                          'centroid $(X^*, Y^*)$, and Weber Material Index ($MI > 1$ raw material bound).'},
    'mgt-q7': {   'eq': '$$\\text{Product: Line Flow (High Vol)}; \\quad \\text{Process: Functional Groups}; \\quad '
                        '\\text{Cellular: Part Families}$$',
                  'text': '<strong>Product Layout:</strong> Machines arranged in sequential line for high-volume '
                          'standardized goods.<br><strong>Process Layout:</strong> Similar machines grouped in '
                          'departments for custom jobs.<br><strong>Cellular:</strong> U-shaped cells grouping part '
                          'families via Group Technology.'},
    'mgt-q8': {   'eq': '$$\\text{Work Study} = \\text{Method Study (How to do)} + \\text{Work Measurement (How '
                        'long)}$$',
                  'text': 'Work Study optimizes resource utilization without heavy capital cost. Method Study '
                          'procedure: Select $\\to$ Record $\\to$ Examine (questioning technique) $\\to$ Develop '
                          '$\\to$ Define $\\to$ Install $\\to$ Maintain.'},
    'mgt-q9': {   'eq': '$$\\bigcirc \\text{ (Operation)}, \\ \\Rightarrow \\text{ (Transport)}, \\ \\square \\text{ '
                        '(Inspection)}, \\ D \\text{ (Delay)}, \\ \\nabla \\text{ (Storage)}$$',
                  'text': 'Method recording uses 5 ASME symbols. Tools include Operation Process Chart, Flow Process '
                          'Chart (man/material/equipment), String Diagram, Multiple Activity Chart, and SIMO Chart '
                          'based on 17 Therbligs.'},
    'mobile-q1': {   'eq': '$$\\text{Mobile Client} \\xleftrightarrow{\\quad \\text{Wireless Link} \\quad} '
                           '\\text{Mobile Middleware / Gateway} \\xleftrightarrow{\\quad \\text{High-Speed Backbone} '
                           '\\quad} \\text{Enterprise Server}$$',
                     'text': 'Mobile middleware bridges resource-constrained mobile devices and enterprise backend '
                             'servers by abstracting protocol conversion, state caching, data transcoding, and offline '
                             'synchronization.'},
    'mobile-q10': {   'eq': '$$\\text{GEO: } 35,786\\text{ km (latency } \\sim 250\\text{ ms, 3 cover Earth); LEO: } '
                            '500\\text{--}1500\\text{ km (latency } \\sim 20\\text{ ms, dense constellation)}$$',
                      'text': 'Geostationary (GEO) satellites provide stationary global coverage with high propagation '
                              'delay, Medium Earth Orbit (MEO) serves GPS navigation, and Low Earth Orbit (LEO) '
                              'delivers low-latency mobile broadband.'},
    'mobile-q11': {   'eq': '$$\\text{IMEI (15-digit Handset ID)} \\quad | \\quad \\text{IMSI (15-digit SIM ID)} '
                            '\\quad | \\quad \\text{MSISDN (Public Number)} \\quad | \\quad \\text{TMSI (Temporary Air '
                            'ID)}$$',
                      'text': '<strong>Mobile Station Identifiers:</strong><br><strong>1. IMEI:</strong> 15-digit '
                              'hardware serial number uniquely identifying the physical mobile terminal hardware (TAC '
                              '+ FAC + SNR + Spare).<br><strong>2. IMSI:</strong> 15-digit subscriber identity stored '
                              'in SIM and HLR/AUC (MCC + MNC + MSIN).<br><strong>3. MSISDN:</strong> Dialable public '
                              'telephone number routed via PSTN (CC + NDC + SN).<br><strong>4. TMSI:</strong> '
                              'Temporary identity assigned by VLR to prevent eavesdropping and protect subscriber '
                              'anonymity over the air interface.'},
    'mobile-q12': {   'eq': '$$\\text{SS7 ISUP Signaling: Initial Address Message (IAM) } \\longrightarrow \\text{ '
                            'Address Complete Message (ACM / Ringback) } \\longrightarrow \\text{ Answer (ANM)}$$',
                      'text': 'Call progress indication uses out-of-band telecom signaling messages to update the '
                              'caller on setup phases (Dialing, Network Routing, Remote Ringing, Busy Tone, or Call '
                              'Queued).'},
    'mobile-q13': {   'eq': '$$\\text{Shannon: } C = B \\log_2(1 + \\text{SINR}); \\quad \\text{CDMA: Orthogonal Walsh '
                            'Codes } \\sum c_i(t)c_j(t) = 0 \\text{ sharing time \\& frequency}$$',
                      'text': 'Multiple access schemes allocate radio resources by splitting frequency channels '
                              '(FDMA), time slots (TDMA), unique mathematical spreading codes (CDMA), or directional '
                              'antenna beams (SDMA).'},
    'mobile-q14': {   'eq': '$$\\text{MS (Handset + SIM)} \\longleftrightarrow \\text{BSS (BTS + BSC)} '
                            '\\longleftrightarrow \\text{NSS (MSC + HLR + VLR + AUC + EIR)} \\longleftrightarrow '
                            '\\text{PSTN / ISDN}$$',
                      'text': 'GSM architecture is divided into the Mobile Station (MS), Base Station Subsystem (BSS) '
                              'for radio management, and Network and Switching Subsystem (NSS) for call routing, '
                              'subscriber mobility, and authentication.'},
    'mobile-q15': {   'eq': '$$\\text{MTC: GMSC queries HLR } \\longrightarrow \\text{ HLR requests MSRN from VLR } '
                            '\\longrightarrow \\text{ GMSC routes call to serving MSC} \\longrightarrow \\text{ MS '
                            'Paged}$$',
                      'text': 'Mobile Originated Calls (MOC) are routed directly by the local serving MSC, whereas '
                              'Mobile Terminated Calls (MTC) require querying the HLR to obtain a temporary Mobile '
                              'Station Roaming Number (MSRN).'},
    'mobile-q16': {   'eq': '$$\\text{Telecom Trunk (E1/T1/SIP) } \\longrightarrow \\text{ IVR Media Gateway (DTMF '
                            'Decoder / TTS / ASR) } \\longleftrightarrow \\text{ Database Server}$$',
                      'text': 'Interactive Voice Response (IVR) systems decode dual-tone multi-frequency (DTMF) keypad '
                              'signals and spoken voice inputs to guide callers through interactive audio menus and '
                              'query enterprise databases.'},
    'mobile-q17': {   'eq': '$$\\text{Authentication: } \\text{SRES} = A3(K_i, \\text{RAND}), \\quad \\text{Key Gen: } '
                            'K_c = A8(K_i, \\text{RAND}), \\quad \\text{Encryption: } \\text{Data} \\oplus A5(K_c)$$',
                      'text': '<strong>GSM Security Triad Algorithms:</strong><br><strong>1. A3 Algorithm '
                              '(Authentication):</strong> SIM computes 32-bit $\\text{SRES}$ from 128-bit challenge '
                              '$\\text{RAND}$ and secret key $K_i$; network authenticates if $\\text{SRES}$ matches '
                              'AUC.<br><strong>2. A8 Algorithm (Ciphering Key Generation):</strong> Computes 64-bit '
                              'session key $K_c$ on SIM from $\\text{RAND}$ and $K_i$ ($K_i$ never transmitted over '
                              'radio).<br><strong>3. A5 Algorithm (Air Encryption):</strong> Hardware stream cipher '
                              'that encrypts/decrypts TDMA radio bursts using $K_c$ and frame number.'},
    'mobile-q18': {   'eq': '$$\\text{SMS Transmission: Control Channels (SDCCH / SACCH) } \\implies \\text{Zero '
                            'impact on dedicated traffic channels (TCH)}$$',
                      'text': 'SMS operates as a store-and-forward signaling service, transferring short text messages '
                              'over cellular signaling control channels without interrupting or reserving voice '
                              'traffic channels.'},
    'mobile-q19': {   'eq': '$$\\text{Max Throughput: } 171.2\\text{ kbps (CS-4, 8 slots); Bottlenecks: Dynamic '
                            'channel coding, high latency, voice priority pre-emption}$$',
                      'text': 'GPRS packet data speeds are constrained by shared radio slot contention, '
                              'distance-dependent channel coding schemes (CS-1 to CS-4), and circuit-switched voice '
                              'calls preempting data channels.'},
    'mobile-q2': {   'eq': '$$\\text{Care-of-Address (CoA)} \\iff \\text{Home Agent (HA) Encapsulation/Tunneling} '
                           '\\iff \\text{Foreign Agent (FA) / Mobile Node}$$',
                     'text': 'The Internet serves as the universal transport backbone for mobile computing, using '
                             'Mobile IP tunneling to route packets seamlessly to mobile nodes regardless of their '
                             'changing physical point of attachment.'},
    'mobile-q20': {   'eq': '$$\\text{CDR Charging: S-CDR generated at SGSN (Radio/Mobility) } + \\text{ G-CDR '
                            'generated at GGSN (Data Volume \\& External IP)}$$',
                      'text': 'GPRS charges subscribers primarily for data volume transferred (megabytes) rather than '
                              'connection duration, combining SGSN mobility records and GGSN volume records into '
                              'unified billing files.'},
    'mobile-q21': {   'eq': '$$\\text{SMS-MT Delivery: SMSC } \\longrightarrow \\text{ SMS-GMSC } '
                            '\\xrightarrow{\\text{HLR Routing Info}} \\text{ Serving MSC/VLR } '
                            '\\xrightarrow{\\text{SDCCH Paging}} \\text{ MS}$$',
                      'text': 'SMS relies on the Short Message Service Center (SMSC) to store messages until the '
                              'destination phone is reachable, querying the HLR for current location before delivering '
                              'over signaling channels.'},
    'mobile-q22': {   'eq': '$$\\text{MS} \\xrightarrow{\\text{Um (MAC/RLC)}} \\text{BSS} \\xrightarrow{\\text{Gb '
                            '(Frame Relay)}} \\text{SGSN} \\xrightarrow{\\text{Gn (GTP/UDP/IP)}} \\text{GGSN} '
                            '\\xrightarrow{\\text{Gi}} \\text{Public Internet}$$',
                      'text': 'GPRS adds packet switching to GSM networks via the Serving GPRS Support Node (SGSN) for '
                              'mobility tracking and ciphering, and Gateway GPRS Support Node (GGSN) for external IP '
                              'routing.'},
    'mobile-q23': {   'eq': '$$\\text{QoS Profile} = \\langle \\text{Service Precedence (1-3)}, \\; \\text{Delay Class '
                            '(1-4)}, \\; \\text{Reliability Class (1-5)}, \\; \\text{Peak/Mean Throughput} \\rangle$$',
                      'text': 'GPRS negotiates QoS profiles between the mobile terminal and network to guarantee '
                              'bounded packet delay, acceptable packet loss rates, and prioritized transmission for '
                              'delay-critical traffic.'},
    'mobile-q24': {   'eq': '$$\\text{Infrastructure BSS: Mobile nodes communicate via Access Point (AP); IBSS: '
                            'Peer-to-peer ad-hoc communication without AP}$$',
                      'text': 'Infrastructure WLAN connects mobile devices to wired networks through access points '
                              'with centralized coordination, whereas IBSS forms spontaneous peer-to-peer networks '
                              'without fixed infrastructure.'},
    'mobile-q25': {   'eq': '$$\\text{Priority Hierarchy: } \\text{SIFS} < \\text{PIFS} < \\text{DIFS} < \\text{EIFS} '
                            '\\implies \\text{Shorter waiting interval guarantees higher channel access priority}$$',
                      'text': '<strong>IEEE 802.11 Interframe Spaces (IFS):</strong><br><strong>1. SIFS (Shortest, 10 '
                              '&mu;s):</strong> Highest priority for immediate response frames: ACK, CTS, and '
                              'fragmented frames.<br><strong>2. PIFS (PCF IFS):</strong> Medium priority used '
                              'exclusively by Access Point in Point Coordination Function for contention-free '
                              'polling.<br><strong>3. DIFS (DCF IFS):</strong> Standard interval contending stations '
                              'must wait after channel idle before initiating backoff counter in '
                              'CSMA/CA.<br><strong>4. EIFS (Extended IFS):</strong> Longest waiting period applied '
                              'whenever an invalid or corrupted packet frame is received.'},
    'mobile-q26': {   'eq': '$$\\text{Wi-Fi: Unlicensed 2.4/5 GHz band, high local bit-rate, low range; 3G: Licensed '
                            'spectrum, macrocells, QoS, seamless mobility}$$',
                      'text': 'Wi-Fi provides low-cost, high-speed local broadband over unlicensed spectrum with '
                              'contention-based access, while cellular networks provide high-mobility, licensed '
                              'spectrum with deterministic QoS and handoff.'},
    'mobile-q27': {   'eq': '$$\\text{Handshake: } \\text{Sender} \\xrightarrow{\\text{RTS}} \\text{Receiver} '
                            '\\xrightarrow{\\text{CTS}} \\text{Sender} \\implies \\text{Overcomes Hidden Terminal}; '
                            '\\quad \\text{NAV (Network Allocation Vector)}$$',
                      'text': 'RTS/CTS exchange reserves the wireless channel by broadcasting transmission duration in '
                              'the Network Allocation Vector (NAV), silencing hidden neighbors and preventing '
                              'carrier-sense collisions.'},
    'mobile-q28': {   'eq': '$$\\text{PSTN Exchange } \\longleftrightarrow \\text{ Radio Base Station (RBS) } '
                            '\\xleftarrow{\\text{Microwave / RF Link}} \\text{ Fixed Wireless Terminal (FWT) at '
                            'Subscriber Premise}$$',
                      'text': 'WLL replaces traditional copper wire local loops with fixed point-to-multipoint '
                              'microwave radio links, delivering rapid, cost-effective telephone and data deployment '
                              'in rural and suburban areas.'},
    'mobile-q29': {   'eq': '$$\\text{Evolution: WEP (Weak 24-bit IV, RC4) } \\longrightarrow \\text{ WPA (TKIP '
                            'per-packet key) } \\longrightarrow \\text{ WPA2 (AES-CCMP 128-bit block cipher)}$$',
                      'text': 'WEP was broken due to small 24-bit IV reuse; WPA introduced temporal key integrity '
                              '(TKIP), and WPA2 established robust enterprise security via AES-CCMP and 802.1X EAP '
                              'authentication.'},
    'mobile-q3': {   'eq': '$$\\text{Access Network (Radio BS/AP)} \\longrightarrow \\text{Edge Network (MEC, '
                           'Low-Latency Aggregation)} \\longrightarrow \\text{Core Network (HLR, GGSN/UPF)}$$',
                     'text': 'Mobile networks partition infrastructure into Access (over-the-air radio link), Edge '
                             '(localized edge computing and content caching), and Core (centralized mobility '
                             'management, authentication, and packet routing).'},
    'mobile-q30': {   'eq': '$$\\text{HIPERLAN/1: Non-preemptive Priority Multiple Access (EY-NPMA); HIPERLAN/2: '
                            'TDMA/TDD centralized dynamic scheduling in 5 GHz band}$$',
                      'text': 'HIPERLAN/1 utilizes Elimination-Yield contention access for peer-to-peer high-speed '
                              'traffic, while HIPERLAN/2 employs connection-oriented TDMA/TDD frames with guaranteed '
                              'ATM/Ethernet QoS.'},
    'mobile-q31': {   'eq': '$$\\text{Security Pillars: Confidentiality (AES/RSA), Integrity (SHA-256/HMAC), '
                            'Availability (DDoS Defense), Auth \\& Non-Repudiation (DSA)}$$',
                      'text': '<strong>Foundational Information Security Pillars:</strong><br><strong>1. '
                              'Confidentiality:</strong> Ensures sensitive transmitted data is unreadable to '
                              'eavesdroppers via encryption.<br><strong>2. Integrity:</strong> Guarantees that data '
                              'packets are not tampered with, altered, or injected in transit using cryptographic hash '
                              'functions (SHA/HMAC).<br><strong>3. Availability:</strong> Assures that network '
                              'services and spectrum remain accessible to legitimate users under peak load or '
                              'attacks.<br><strong>4. Authenticity & Non-Repudiation:</strong> Verifies genuine '
                              'claimant identity and prevents sender from denying authorship via digital signatures.'},
    'mobile-q32': {   'eq': '$$\\text{Passive Attacks (Eavesdropping, Traffic Analysis) vs Active Attacks (Masquerade, '
                            'Replay, Message Modification, Denial of Service)}$$',
                      'text': 'Passive attacks threaten confidentiality by silently intercepting wireless '
                              'transmissions without altering data, whereas active attacks compromise integrity and '
                              'availability by injecting forged or altered packets.'},
    'mobile-q33': {   'eq': '$$\\text{TLS Architecture: Handshake Protocol (mutual auth \\& key exchange) + Record '
                            'Protocol (symmetric encryption \\& HMAC data integrity)}$$',
                      'text': 'TLS operates above the transport layer providing authenticated end-to-end encryption, '
                              'while WTLS adapts TLS for low-bandwidth mobile handsets using compact headers and '
                              'elliptic curves.'},
    'mobile-q34': {   'eq': '$$n = p \\cdot q, \\quad \\phi(n) = (p-1)(q-1), \\quad e \\cdot d \\equiv 1 '
                            '\\pmod{\\phi(n)}, \\quad C = M^e \\pmod n, \\quad M = C^d \\pmod n$$',
                      'text': 'RSA security relies on the computational difficulty of factoring the product of two '
                              'large prime numbers $n = pq$, using public encryption key $(e, n)$ and private '
                              'decryption key $(d, n)$.'},
    'mobile-q35': {   'eq': '$$Y_A = \\alpha^{X_A} \\pmod q, \\quad Y_B = \\alpha^{X_B} \\pmod q, \\quad K = '
                            '(Y_B)^{X_A} \\pmod q = (Y_A)^{X_B} \\pmod q = \\alpha^{X_A X_B} \\pmod q$$',
                      'text': 'Diffie-Hellman enables two parties to establish a shared secret key $K$ over an '
                              'insecure channel based on the discrete logarithm problem, vulnerable to '
                              'Man-in-the-Middle if unauthenticated.'},
    'mobile-q36': {   'eq': '$$\\Delta f = \\frac{1}{T_{\\text{sym}}}, \\quad \\int_0^{T_{\\text{sym}}} \\cos(2\\pi '
                            'f_i t)\\cos(2\\pi f_j t) dt = 0 \\; (i \\ne j), \\quad T_{\\text{total}} = '
                            'T_{\\text{sym}} + T_{CP}$$',
                      'text': 'OFDM divides broadband channels into densely spaced orthogonal narrowband subcarriers, '
                              'adding a Cyclic Prefix (CP) to eliminate Intersymbol Interference (ISI) and multipath '
                              'fading.'},
    'mobile-q37': {   'eq': '$$\\text{MBMS: Point-to-Multipoint transmission sharing single radio bearer; MPLS: Label '
                            'Switched Path (LSP) fast packet forwarding via 32-bit labels}$$',
                      'text': 'MBMS conserves cellular bandwidth by broadcasting multimedia data simultaneously to '
                              'unlimited subscribers on a shared carrier, accelerated by MPLS label switching in the '
                              'core.'},
    'mobile-q38': {   'eq': '$$\\text{Evolution: 2G (Voice/TDMA, 64 kbps) } \\to \\text{ 3G (CDMA, 2 Mbps) } \\to '
                            '\\text{ 4G (All-IP/OFDMA, 100 Mbps) } \\to \\text{ 5G (eMBB/URLLC/mMTC, 10-20 Gbps)}$$',
                      'text': 'Mobile networks evolved from circuit-switched analog/digital voice (1G/2G) to wideband '
                              'data (3G), flat All-IP OFDMA (4G LTE), and service-based network slicing supporting '
                              'sub-millisecond URLLC and massive IoT (5G).'},
    'mobile-q4': {   'eq': '$$\\text{Primary Constraints: Limited Battery Life, Scarce Bandwidth, Multipath Fading, '
                           'Intermittent Connectivity, Security Risks}$$',
                     'text': 'Mobile computing environments are constrained by finite battery energy, highly variable '
                             'wireless bandwidth, physical signal attenuation, frequent disconnections, and heightened '
                             'physical and wireless security risks.'},
    'mobile-q5': {   'eq': '$$\\text{Tier 1: Presentation (Thin/Smart Client)} \\longleftrightarrow \\text{Tier 2: '
                           'Application / Middleware Logic} \\longleftrightarrow \\text{Tier 3: Enterprise Database}$$',
                     'text': 'Three-tier architecture separates presentation on the mobile device from application '
                             'processing on intermediate servers and persistent data storage on enterprise databases, '
                             'optimizing network utilization.'},
    'mobile-q6': {   'eq': '$$\\text{Key Axioms: Energy-Aware Scheduling, Adaptive Bandwidth Throttling, Offline '
                           'Replication, End-to-End Security}$$',
                     'text': 'Mobile software engineering requires cross-layer optimization prioritizing aggressive '
                             'battery conservation, bandwidth adaptation, asynchronous offline transaction queuing, '
                             'and lightweight cryptography.'},
    'mobile-q7': {   'eq': '$$\\text{Context Tuple } \\mathcal{C} = \\langle \\text{Location}, \\text{Network '
                           'Bandwidth}, \\text{Battery Energy}, \\text{Device Profile}, \\text{User Activity} '
                           '\\rangle$$',
                     'text': 'Context-aware systems dynamically modify application behavior, media fidelity, and '
                             'security rules based on real-time awareness of user location, device battery state, and '
                             'available network bandwidth.'},
    'mobile-q8': {   'eq': '$$\\text{Transcoding: Modality Conversion (Text } \\leftrightarrow \\text{ Speech), '
                           'Resolution Scaling, Format Compression (PNG } \\to \\text{ WebP)}$$',
                     'text': 'Content adaptation dynamically transforms, compresses, or transcodes media at '
                             'intermediary proxies to match the specific screen resolution, memory limits, and network '
                             'throughput of the client handset.'},
    'mobile-q9': {   'eq': '$$\\text{Seamless Mobility: Continuous Session State, Zero Packet Loss '
                           '(Buffering/Bicasting), and Handover Latency } \\le 50\\text{ ms}$$',
                     'text': 'Seamless communication preserves active TCP sessions, multimedia streams, and security '
                             'contexts during cellular handoffs without packet drops or noticeable interruption to the '
                             'user.'},
    'pe-q1': {   'eq': '$$I_A = \\frac{\\alpha_2 I_g + I_{CBO1} + I_{CBO2}}{1 - (\\alpha_1 + \\alpha_2)}, \\quad I_L '
                       '\\approx (2 \\text{ to } 3) I_H$$',
                 'text': 'SCR 4-layer $p_1-n_1-p_2-n_2$ structure modeled as coupled PNP ($Q_1$) and NPN ($Q_2$) '
                         'transistors. Forward latching occurs via regenerative positive feedback when loop gain '
                         '$\\alpha_1 + \\alpha_2 \\to 1$. Latching current $I_L$ is minimum turn-on holding value; '
                         '$I_H$ is drop-out threshold.'},
    'pe-q10': {   'eq': '$$\\cos(\\alpha + \\mu) = \\cos\\alpha - \\frac{2 \\omega L_s I_{dc}}{V_m}, \\quad \\Delta '
                        'V_d = \\frac{2 \\omega L_s}{\\pi} I_{dc} \\ (\\text{1-ph}), \\quad \\Delta V_d = \\frac{3 '
                        '\\omega L_s}{\\pi} I_{dc} \\ (\\text{3-ph})$$',
                  'text': 'Source inductance $L_s$ prevents instantaneous current transfer, causing commutation '
                          'overlap angle $\\mu$. Output voltage drops by $\\Delta V_d$. In inverter mode, if $\\alpha '
                          '+ \\mu > 180^\\circ - \\omega t_q$, commutation failure occurs.'},
    'pe-q11': {   'eq': '$$V_o = D V_s, \\quad \\Delta I_L = \\frac{V_s D(1 - D)}{f_s L}, \\quad \\Delta V_c = '
                        '\\frac{V_s D(1 - D)}{8 f_s^2 L C}, \\quad L_c = \\frac{(1 - D) R}{2 f_s}$$',
                  'text': 'Step-down (Buck) converter in CCM. Inductor volt-second balance yields linear gain $M = D$. '
                          'Second-order LC filter delivers low output voltage ripple. Critical inductance $L_c$ '
                          'guarantees continuous conduction at specified load resistance.'},
    'pe-q12': {   'eq': '$$V_o = \\frac{V_s}{1 - D}, \\quad \\Delta I_L = \\frac{V_s D}{f_s L}, \\quad \\Delta V_c = '
                        '\\frac{V_o D}{R f_s C}, \\quad L_c = \\frac{D(1 - D)^2 R}{2 f_s}$$',
                  'text': 'Step-up (Boost) converter in CCM. Energy stored during switch ON adds in series with DC '
                          'source during switch OFF. Output capacitor supplies load while switch is ON. Inductor '
                          'parasitic resistance limits maximum practical voltage gain.'},
    'pe-q13': {   'eq': '$$V_o = -\\frac{D}{1 - D} V_s, \\quad \\Delta I_L = \\frac{V_s D}{f_s L}, \\quad \\Delta V_c '
                        '= \\frac{V_o D}{R f_s C}, \\quad L_c = \\frac{(1 - D)^2 R}{2 f_s}$$',
                  'text': 'Inverting Buck-Boost converter provides step-down ($D < 0.5$) and step-up ($D > 0.5$) '
                          'voltage translation with reversed output polarity. Inductor acts as intermediate energy '
                          'reservoir between input and output ports.'},
    'pe-q14': {   'eq': '$$V_o = -\\frac{D}{1 - D} V_s, \\quad V_{C1} = \\frac{V_s}{1 - D}, \\quad \\Delta I_{L1} = '
                        '\\frac{V_s D}{f_s L_1}, \\quad \\Delta I_{L2} = \\frac{V_s D}{f_s L_2}$$',
                  'text': 'Ćuk converter transfers energy capacitively via intermediate capacitor $C_1$. Dual input '
                          'and output inductors eliminate pulsating currents at both terminal ports, yielding low EMI '
                          'signatures and smooth continuous waveforms.'},
    'pe-q15': {   'eq': '$$\\text{Class A: } (+V_o, +I_o), \\ \\text{Class B: } (+V_o, -I_o), \\ \\text{Class C: } '
                        '(+V_o, \\pm I_o), \\ \\text{Class D: } (\\pm V_o, +I_o), \\ \\text{Class E: } (\\pm V_o, \\pm '
                        'I_o)$$',
                  'text': 'Chopper classification across $(V_o, I_o)$ plane: Class A (Motoring), Class B (Regenerative '
                          'braking), Class C (Reversible drive), Class D (Coil de-energization), and Class E (Complete '
                          '4-quadrant H-bridge servo drive).'},
    'pe-q16': {   'eq': '$$\\text{Half: } V_{o,rms} = \\frac{V_{dc}}{2}, \\ V_{o1} = \\frac{2 V_{dc}}{\\pi}; \\quad '
                        '\\text{Full: } V_{o,rms} = V_{dc}, \\ V_{o1} = \\frac{4 V_{dc}}{\\pi}; \\quad '
                        'V_{o1,\\text{quasi}} = \\frac{4 V_{dc}}{\\pi}\\sin d$$',
                  'text': '1-Phase VSI topologies: Full-bridge delivers twice the voltage and 4x the power of '
                          'half-bridge. Feedback diodes circulate reactive load current and return energy to DC source '
                          '($v_o \\cdot i_o < 0$). Quasi-square wave modulation controls fundamental and eliminates '
                          'harmonics.'},
    'pe-q17': {   'eq': '$$V_{L,rms} = \\sqrt{\\frac{2}{3}} V_{dc} \\approx 0.8165 V_{dc}, \\quad V_{ph,rms} = '
                        '\\frac{\\sqrt{2}}{3} V_{dc} \\approx 0.4714 V_{dc}, \\quad V_{L1,rms} = '
                        '\\frac{\\sqrt{6}}{\\pi} V_{dc} \\approx 0.7797 V_{dc}$$',
                  'text': '3-Phase VSI 180° conduction: Each switch conducts for 180°, with 3 switches ON '
                          'simultaneously. Six-step phase voltage waveform. Triplen harmonics are inherently '
                          'eliminated from line-to-line voltages.'},
    'pe-q18': {   'eq': '$$V_{L,rms} = \\frac{V_{dc}}{\\sqrt{2}} \\approx 0.7071 V_{dc}, \\quad V_{ph,rms} = '
                        '\\frac{V_{dc}}{\\sqrt{6}} \\approx 0.4082 V_{dc}, \\quad \\text{Inherent } 60^\\circ \\text{ '
                        'Deadband}$$',
                  'text': '3-Phase VSI 120° conduction: Each switch conducts for 120°, with 2 switches ON '
                          'simultaneously. Inherent 60° deadband prevents shoot-through faults without blanking '
                          'circuits. Delivers 86.6% of the line voltage of 180° mode.'},
    'pe-q19': {   'eq': '$$m_a = \\frac{A_r}{A_c}, \\quad m_f = \\frac{f_c}{f_m}, \\quad V_{o1\\max} = m_a V_{dc} \\ '
                        '(m_a \\le 1), \\quad f_h = (j \\cdot m_f \\pm k) f_m$$',
                  'text': 'Sinusoidal PWM (SPWM) compares sine reference with triangular carrier. Linear modulation up '
                          'to $m_a = 1$. High carrier ratio $m_f$ pushes harmonic sidebands far above line frequency, '
                          'simplifying passive filter design.'},
    'pe-q2': {   'eq': '$$P_{gm} = V_g I_g = \\text{const}, \\quad E_s = V_g + R_g I_g, \\quad i_c = '
                       'C_{j2}\\frac{dv}{dt}$$',
                 'text': 'Turn-on via gate pulse, light (LASCR), thermal, or $dv/dt$. Gate operating point must lie '
                         'inside preferred triggering window bounded by $V_{g\\min}, V_{g\\max}, I_{g\\min}, '
                         'I_{g\\max}$ and peak gate power hyperbola $P_{gm}$. Pulse transformer / optocoupler provides '
                         'galvanic isolation.'},
    'pe-q20': {   'eq': '$$\\text{VSI: Stiff } C_{dc}, \\text{ antiparallel diodes, shoot-through risk}; \\quad '
                        '\\text{CSI: Stiff } L_{dc}, \\text{ series diodes, open-circuit risk}$$',
                  'text': 'VSI regulates voltage (load determines current), dominates EVs and industrial inverters. '
                          'CSI regulates current via large series choke $L_{dc}$ with ASCI commutation, offering '
                          'inherent short-circuit immunity and four-quadrant regeneration for MW drives.'},
    'pe-q21': {   'eq': '$$\\text{Integral: } V_{o,rms} = V_s \\sqrt{\\frac{n}{n + m}}, \\ \\text{PF} = '
                        '\\sqrt{\\frac{n}{n + m}}; \\quad \\text{Phase: } V_{o,rms} = V_s '
                        '\\sqrt{\\frac{1}{\\pi}\\left[(\\pi - \\alpha) + \\frac{1}{2}\\sin 2\\alpha\\right]}$$',
                  'text': '1-Phase AC Voltage Controller with R load: Integral cycle control switches at zero '
                          'crossings (no RFI, heating loads); Phase angle control varies firing angle $\\alpha$ from 0 '
                          'to 180° to continuously regulate output RMS voltage.'},
    'pe-q22': {   'eq': '$$i_o(\\omega t) = \\frac{V_m}{Z}\\left[\\sin(\\omega t - \\phi) - \\sin(\\alpha - \\phi) '
                        'e^{-\\frac{R}{\\omega L}(\\omega t - \\alpha)}\\right], \\quad \\alpha \\ge \\phi \\ '
                        '(\\text{Operating Rule})$$',
                  'text': '1-Phase AC Controller with RL load: Controlled discontinuous mode for $\\alpha > \\phi$. '
                          'When $\\alpha = \\phi$, current is continuous sinusoid ($V_{o,rms} = V_s$). Firing at '
                          '$\\alpha < \\phi$ causes loss of control and DC core saturation; wide gate pulses '
                          'required.'},
    'pe-q23': {   'eq': '$$f_o = \\frac{f_s}{k} \\ (k = 2, 3\\dots), \\quad \\alpha_P + \\alpha_N = 180^\\circ \\ '
                        '(\\text{Circulating Mode with IGR})$$',
                  'text': 'Cycloconverters directly convert AC frequency without intermediate DC link. Step-down '
                          'operation uses line commutation. Non-circulating mode requires zero-crossing deadtime; '
                          'circulating mode uses Intergroup Reactor (IGR) to eliminate crossover distortion.'},
    'pe-q24': {   'eq': '$$P_{sw} = \\frac{1}{2} V_s I_o (t_r + t_f) f_s, \\quad \\text{ZCS: } i_{sw} = 0 \\ '
                        '(\\text{IGBT tail loss elimination}), \\quad \\text{ZVS: } v_{sw} = 0 \\ (\\text{MOSFET } '
                        'C_{oss})$$',
                  'text': 'Soft switching eliminates hard-switching overlap power dissipation. ZCS turns switch on/off '
                          'at zero current (ideal for IGBTs). ZVS turns switch on/off at zero voltage (ideal for '
                          'high-frequency Power MOSFETs, eliminating $\\frac{1}{2}CV^2$ losses).'},
    'pe-q25': {   'eq': '$$\\text{Flyback: } V_o = \\frac{N_s}{N_p}\\left(\\frac{D}{1-D}\\right)V_s, \\quad '
                        '\\text{Forward: } V_o = \\frac{N_s}{N_p} D V_s \\ (D < 0.5), \\quad \\text{Push-Pull/Full: } '
                        'V_o = 2\\frac{N_s}{N_p} D V_s$$',
                  'text': 'Isolated SMPS topologies: Flyback uses coupled inductor (energy stored in gap during switch '
                          'ON, $<150\\text{ W}$); Forward transfers energy during switch ON (needs tertiary reset '
                          'winding); Push-Pull, Half-Bridge, and Full-Bridge provide 2-quadrant core utilization for '
                          'high power.'},
    'pe-q26': {   'eq': '$$\\text{Offline: } 4-10\\text{ ms transfer}; \\quad \\text{Line-Interactive: } 2-4\\text{ '
                        'ms}; \\quad \\text{Online Double-Conversion: } 0\\text{ ms (Zero)}$$',
                  'text': 'UPS configurations: Offline provides raw mains with battery backup; Line-Interactive adds '
                          'AVR voltage conditioning; Online Double-Conversion continuously converts $AC \\to DC \\to '
                          'AC$, delivering 0 ms transfer time, perfect sine wave, and static bypass protection.'},
    'pe-q3': {   'eq': '$$t_{on} = t_d + t_r + t_p, \\quad t_q = t_{rr} + t_{gr}, \\quad t_c > t_q \\ '
                       '(\\text{commutation})$$',
                 'text': 'Turn-on transient comprises delay ($t_d$), rise ($t_r$), and spread ($t_p$) times. Turn-off '
                         'transient requires sweeping out reverse carriers ($t_{rr}$) and thermal recombination of '
                         'trapped junction charges ($t_{gr}$). Circuit turn-off time must satisfy $t_c > t_q$ to avoid '
                         'commutation failure.'},
    'pe-q4': {   'eq': '$$L_s \\ge \\frac{V_s}{(di/dt)_{\\max}}, \\quad C_s = \\frac{V_s^2}{L_s (dv/dt)_{\\max}^2}, '
                       '\\quad R_s \\ge \\frac{V_s}{I_{T\\max}}, \\quad \\zeta = '
                       '\\frac{R_s}{2}\\sqrt{\\frac{C_s}{L_s}}$$',
                 'text': 'Series inductor $L_s$ suppresses localized gate hot-spot burning from high $di/dt$. Parallel '
                         'RC snubber dampens transient $dv/dt$ displacement currents across junction $J_2$. Snubber '
                         'resistor $R_s$ limits discharge current when SCR fires.'},
    'pe-q5': {   'eq': '$$\\beta_{off} = \\frac{I_A}{I_{GR}} \\approx 3-5 \\ (\\text{GTO}), \\quad R_{DS(on)} \\propto '
                       'V_{BR}^{2.5} \\ (\\text{MOSFET}), \\quad V_{CE(sat)} \\approx 1.8-2.5\\text{ V} \\ '
                       '(\\text{IGBT})$$',
                 'text': '<strong>TRIAC:</strong> Bidirectional AC line switch (4 quadrants).<br><strong>GTO:</strong> '
                         'Turn-off via large reverse gate current.<br><strong>MOSFET:</strong> Unipolar '
                         'majority-carrier switch for MHz frequencies ($<600\\text{ V}$).<br><strong>IGBT:</strong> '
                         'Hybrid MOS-input BJT-output with conductivity modulation for medium/high power.'},
    'pe-q6': {   'eq': '$$V_{dc} = \\frac{V_m}{2\\pi}(1 + \\cos\\alpha), \\quad V_{rms} = '
                       '\\frac{V_m}{2\\sqrt{\\pi}}\\sqrt{(\\pi - \\alpha) + \\frac{1}{2}\\sin 2\\alpha}, \\quad '
                       'i_o(\\beta) = 0$$',
                 'text': '1-Phase Half-Wave Controlled Rectifier. Inductive RL load extends conduction into negative '
                         'half-cycle to extinction angle $\\beta$. Freewheeling diode clamps $v_o \\ge 0$, discharges '
                         'inductive energy, boosts average DC voltage, and improves power factor.'},
    'pe-q7': {   'eq': '$$V_{dc} = \\frac{2 V_m}{\\pi}\\cos\\alpha, \\quad V_{rms} = \\frac{V_m}{\\sqrt{2}} = V_s, '
                       '\\quad I_{dc} = \\frac{V_{dc} - E}{R}$$',
                 'text': '1-Phase Full Converter with RLE load operates in Quadrant I ($0 \\le \\alpha < 90^\\circ$, '
                         'Rectification) and Quadrant IV ($90^\\circ < \\alpha < 180^\\circ$, Inversion). Line '
                         'commutation transfers current between SCR pairs. Discontinuous conduction occurs at light '
                         'loads.'},
    'pe-q8': {   'eq': '$$\\text{DF} = \\cos\\alpha, \\quad \\text{THD} = '
                       '\\sqrt{\\left(\\frac{\\pi}{2\\sqrt{2}}\\right)^2 - 1} \\approx 48.34\\%, \\quad \\text{PF} = '
                       '\\frac{2\\sqrt{2}}{\\pi}\\cos\\alpha$$',
                 'text': 'Displacement Factor $\\text{DF} = \\cos\\phi_1$. Total Harmonic Distortion measures ripple '
                         'current relative to fundamental. Semi-converter exhibits higher PF ($\\text{DF} = '
                         '\\cos(\\alpha/2)$) and lower reactive power than full converter due to freewheeling action.'},
    'pe-q9': {   'eq': '$$V_{dc} = \\frac{3 V_{ml}}{\\pi}\\cos\\alpha = \\frac{3\\sqrt{3}V_{mp}}{\\pi}\\cos\\alpha '
                       '\\approx 1.35 V_L \\cos\\alpha, \\quad V_{rms} = V_{ml}\\sqrt{\\frac{1}{2} + '
                       '\\frac{3\\sqrt{3}}{4\\pi}\\cos 2\\alpha}$$',
                 'text': '3-Phase 6-Pulse Full Bridge Converter: 6 SCRs triggered at $60^\\circ$ intervals, each '
                         'conducting for $120^\\circ$. Output line voltage switches between 6 line pairs. Operates as '
                         'rectifier for $\\alpha \\le 90^\\circ$ and line-commutated inverter for $\\alpha > '
                         '90^\\circ$.'},
    'phy-q1': {   'eq': '$$\\frac{d^2 x}{dt^2} + 2\\gamma \\frac{dx}{dt} + \\omega_0^2 x = 0 \\implies x(t) = A '
                        'e^{-\\gamma t}\\cos(\\omega t - \\phi), \\quad \\omega = \\sqrt{\\omega_0^2 - \\gamma^2}$$',
                  'text': '<strong>Damped Motion Equation:</strong> $\\ddot{x} + 2\\gamma\\dot{x} + \\omega_0^2 x = '
                          '0$, where $\\gamma = b/2m$ and $\\omega_0 = \\sqrt{k/m}$.<br><strong>Three '
                          'Regimes:</strong><br>1. <strong>Overdamped ($\\gamma > \\omega_0$):</strong> Deadbeat '
                          'exponential return without oscillation.<br>2. <strong>Critically Damped ($\\gamma = '
                          '\\omega_0$):</strong> Fastest return to equilibrium without overshoot ($x = (C_1 + C_2 '
                          't)e^{-\\gamma t}$).<br>3. <strong>Underdamped ($\\gamma < \\omega_0$):</strong> Oscillatory '
                          'motion with decaying amplitude $A(t) = A_0 e^{-\\gamma t}$ and frequency $\\omega = '
                          '\\sqrt{\\omega_0^2 - \\gamma^2}$.<br><strong>Relaxation Time:</strong> $\\tau = 1/\\gamma = '
                          '2m/b$.'},
    'phy-q10': {   'eq': '$$(a + b)\\sin\\theta = n\\lambda, \\quad \\frac{d\\theta}{d\\lambda} = '
                         '\\frac{n}{(a+b)\\cos\\theta}, \\quad R = \\frac{\\lambda}{d\\lambda} = n N$$',
                   'text': '<strong>Grating Equation:</strong> $(a + b)\\sin\\theta = n\\lambda$, where $d = a + b$ is '
                           'the grating element.<br><strong>Max Order:</strong> $n_{max} = \\lfloor (a+b)/\\lambda '
                           '\\rfloor$.<br><strong>Dispersive Power:</strong> $\\frac{d\\theta}{d\\lambda} = '
                           '\\frac{n}{(a+b)\\cos\\theta}$ (linear normal spectrum).<br><strong>Resolving '
                           "Power:</strong> $R = \\lambda / d\\lambda = n N$ (Rayleigh's criterion, product of order "
                           '$n$ and total rulings $N$).'},
    'phy-q11': {   'eq': '$$\\lambda = \\frac{h}{\\sqrt{2mE}} = \\frac{h}{\\sqrt{2mqV}} = '
                         '\\frac{1.227}{\\sqrt{V}}\\text{ nm}, \\quad \\Delta x \\cdot \\Delta p_x \\ge '
                         '\\frac{\\hbar}{2}$$',
                   'text': '<strong>Matter Waves:</strong> De Broglie relation $\\lambda = h/p$. Accelerated electron: '
                           '$\\lambda = 1.227/\\sqrt{V}\\text{ nm}$.<br><strong>Uncertainty Principle:</strong> '
                           '$\\Delta x \\cdot \\Delta p_x \\ge \\hbar / 2$.<br><strong>Non-Existence of Electron in '
                           'Nucleus:</strong> For nuclear confinement ($\\Delta x \\approx 2\\times 10^{-14}\\text{ '
                           'm}$), $E_k \\ge 5\\text{ to } 20\\text{ MeV}$, far exceeding observed beta decay energies '
                           '($<4\\text{ MeV}$).'},
    'phy-q12': {   'eq': '$$P(x,t) = |\\psi(x,t)|^2 = \\psi^* \\psi, \\quad \\int_{-\\infty}^{+\\infty} |\\psi(x,t)|^2 '
                         'dx = 1$$',
                   'text': '<strong>Physical Meaning:</strong> Wavefunction $\\psi$ is complex and unobservable; '
                           '$|\\psi|^2$ represents position probability density.<br><strong>Acceptable Wavefunction '
                           'Criteria:</strong> Must be finite, single-valued, and continuous everywhere with a '
                           'continuous first spatial derivative.<br><strong>Normalization:</strong> Total probability '
                           'across all space must equal 1.'},
    'phy-q13': {   'eq': '$$i\\hbar \\frac{\\partial \\Psi}{\\partial t} = -\\frac{\\hbar^2}{2m}\\frac{\\partial^2 '
                         '\\Psi}{\\partial x^2} + V(x)\\Psi, \\quad \\frac{d^2 \\psi}{dx^2} + \\frac{2m}{\\hbar^2}(E - '
                         'V)\\psi = 0$$',
                   'text': '<strong>Quantum Operators:</strong> Momentum operator $\\hat{p} = -i\\hbar '
                           '\\frac{\\partial}{\\partial x}$, Energy operator $\\hat{E} = i\\hbar '
                           '\\frac{\\partial}{\\partial t}$.<br><strong>Time-Dependent:</strong> Governs '
                           'non-stationary states: $\\hat{H}\\Psi = i\\hbar \\frac{\\partial \\Psi}{\\partial '
                           't}$.<br><strong>Time-Independent:</strong> Eigenvalue equation $\\hat{H}\\psi = E\\psi$ '
                           'for conservative stationary states ($V = V(x)$).'},
    'phy-q14': {   'eq': '$$E_n = \\frac{n^2 h^2}{8m L^2}, \\quad \\psi_n(x) = '
                         '\\sqrt{\\frac{2}{L}}\\sin\\left(\\frac{n\\pi x}{L}\\right), \\quad n = 1, 2, 3, \\dots$$',
                   'text': '<strong>Boundary Conditions:</strong> $\\psi(0) = 0$ and $\\psi(L) = 0$, giving quantized '
                           'wave vector $k_n = n\\pi / L$.<br><strong>Energy Quantization:</strong> $E_n \\propto '
                           'n^2$.<br><strong>Zero-Point Energy:</strong> $E_1 = \\frac{h^2}{8mL^2} \\neq 0$ (quantum '
                           'mechanical requirement of uncertainty principle).<br><strong>Eigenfunctions:</strong> '
                           'Normalization constant is $\\sqrt{2/L}$.'},
    'phy-q15': {   'eq': '$$E_g(d) = E_{g,bulk} + \\frac{h^2}{8\\mu d^2} - \\frac{1.8 e^2}{4\\pi\\epsilon d}, \\quad '
                         '\\text{DOS: } 0D \\to \\delta(E), \\; 1D \\to E^{-1/2}, \\; 2D \\to \\text{Step}$$',
                   'text': '<strong>Quantum Confinement:</strong> Spatial dimensions $\\le 100\\text{ nm}$ comparable '
                           'to exciton Bohr radius widen effective bandgap ($E_g \\propto '
                           '1/d^2$).<br><strong>Dimensionality:</strong> 0D (Quantum Dots, 3 confined axes), 1D '
                           '(Nanowires, 2 confined axes), 2D (Quantum Wells, 1 confined '
                           'axis).<br><strong>Synthesis:</strong> Sol-Gel (hydrolysis $\\to$ condensation $\\to$ sol '
                           '$\\to$ gel $\\to$ sintering) and CVD (gaseous precursors cracking on heated catalytic '
                           'substrate).'},
    'phy-q16': {   'eq': '$$f = \\frac{p}{2 t} \\sqrt{\\frac{Y}{\\rho}}, \\quad f_1 = \\frac{1}{2 '
                         't}\\sqrt{\\frac{Y}{\\rho}}$$',
                   'text': '<strong>Converse Piezoelectric Effect:</strong> Applying alternating high-frequency '
                           'voltage across electrical faces induces mechanical vibrations along mechanical '
                           'faces.<br><strong>Crystal Cut:</strong> $X$-cut quartz vibrates in thickness '
                           'mode.<br><strong>Resonance Condition:</strong> $LC$ oscillator tuned to quartz natural '
                           'frequency.<br><strong>Frequency:</strong> $f \\propto 1/t$ ($1\\text{ mm}$ quartz '
                           '$\\implies \\approx 2.73\\text{ MHz}$).'},
    'phy-q17': {   'eq': '$$f = \\frac{1}{2 l} \\sqrt{\\frac{Y}{\\rho}}, \\quad \\text{Operating Range: } 20\\text{ '
                         'kHz to } 100\\text{ kHz}$$',
                   'text': '<strong>Magnetostrictive Joule Effect:</strong> Ferromagnetic rod changes length in '
                           'longitudinal magnetic field regardless of field sign.<br><strong>DC Polarizing '
                           'Field:</strong> Required to eliminate frequency doubling ($2f \\to '
                           'f$).<br><strong>Resonance:</strong> Midpoint clamping produces central node and terminal '
                           'antinodes.<br><strong>Limitation:</strong> Upper frequency limited to $<300\\text{ kHz}$ '
                           'by eddy current and hysteresis losses.'},
    'phy-q18': {   'eq': '$$d = \\frac{v \\cdot t_f}{2}, \\quad T = \\frac{v \\cdot t_b}{2}, \\quad R = '
                         '\\left(\\frac{Z_2 - Z_1}{Z_2 + Z_1}\\right)^2$$',
                   'text': '<strong>Acoustic Impedance Mismatch:</strong> $Z = \\rho v$; air crack interface in metal '
                           'reflects almost $100\\%$ ($R \\approx 1.0$).<br><strong>A-Scan Display:</strong> Displays '
                           'Initial Pulse ($P_0$), Flaw Echo ($P_f$), and Back-Wall Echo ($P_b$).<br><strong>Flaw '
                           'Depth:</strong> $d = \\frac{v t_f}{2} = (\\frac{t_f}{t_b})T$.'},
    'phy-q19': {   'eq': '$$T = \\frac{0.161 V}{A} = \\frac{0.161 V}{\\sum a_i S_i}$$',
                   'text': '<strong>Reverberation Time ($T$):</strong> Time for acoustic energy density to drop by '
                           '$60\\text{ dB}$ ($10^{-6}$ of steady-state value).<br><strong>Absorption Unit:</strong> '
                           'Sabin / Open Window Unit (OWU).<br><strong>Energy Balance:</strong> $V \\frac{d\\rho}{dt} '
                           '= P - \\frac{c A \\rho}{4}$, leading to decay $\\rho(t) = \\rho_0 e^{-\\frac{c A t}{4V}}$. '
                           'Setting $\\rho / \\rho_0 = 10^{-6}$ yields $T \\approx \\frac{0.161 V}{A}$.'},
    'phy-q2': {   'eq': '$$A = \\frac{f_0}{\\sqrt{(\\omega_0^2 - \\omega^2)^2 + 4\\gamma^2 \\omega^2}}, \\quad '
                        '\\tan\\phi = \\frac{2\\gamma \\omega}{\\omega_0^2 - \\omega^2}$$',
                  'text': '<strong>Steady-State Solution:</strong> $x(t) = A \\sin(\\omega t - '
                          '\\phi)$.<br><strong>Phase Angle Across Frequencies:</strong><br>1. $\\omega \\ll \\omega_0 '
                          '\\implies \\phi \\to 0$ (displacement in phase with driving force, '
                          'stiffness-controlled).<br>2. $\\omega = \\omega_0 \\implies \\phi = \\pi/2$ (displacement '
                          'lags force by $90^\\circ$, force in phase with velocity, velocity resonance).<br>3. '
                          '$\\omega \\gg \\omega_0 \\implies \\phi \\to \\pi$ (displacement lags force by '
                          '$180^\\circ$, inertia-controlled).'},
    'phy-q20': {   'eq': '$$T_{\\text{opt}} \\approx 0.8\\text{ to } 1.2\\text{ s (Speech)}, \\quad 1.5\\text{ to } '
                         '2.2\\text{ s (Music)}, \\quad \\text{Echo Threshold: } \\Delta t > 0.05\\text{ s}$$',
                   'text': '<strong>Acoustic Defects & Remedies:</strong><br>1. <strong>Excess Reverberation:</strong> '
                           'Deploy acoustic absorbent panels/curtains.<br>2. <strong>Echoes:</strong> Tilt/splay rear '
                           'walls, add absorbent cladding.<br>3. <strong>Flutter Echoes:</strong> Splay parallel walls '
                           'by $5-8^\\circ$ or install convex acoustic diffusers.<br>4. <strong>Sound '
                           'Focusing:</strong> Eliminate concave domes; install convex reflective baffles.<br>5. '
                           '<strong>Resonance Modes:</strong> Avoid integer room ratios; use Golden proportions.'},
    'phy-q21': {   'eq': '$$B_{12} = B_{21}, \\quad \\frac{A_{21}}{B_{21}} = \\frac{8\\pi h \\nu^3}{c^3}, \\quad '
                         '\\frac{R_{sp}}{R_{stim}} = e^{h\\nu / k_B T} - 1$$',
                   'text': "<strong>Einstein's Relations:</strong> Equating transition balance to Planck's radiation "
                           'law proves $B_{12} = B_{21}$ and $A_{21}/B_{21} = 8\\pi h\\nu^3 / '
                           'c^3$.<br><strong>Frequency Dependence:</strong> Spontaneous emission scales with $\\nu^3$, '
                           'dominating in the optical spectrum under thermal equilibrium.<br><strong>Laser '
                           'Condition:</strong> Population inversion ($N_2 > N_1$) is mandatory for stimulated '
                           'emission to outpace absorption.'},
    'phy-q22': {   'eq': '$$\\lambda = 694.3\\text{ nm (Pulsed Red)}, \\quad \\text{Active Medium: } Al_2O_3 : Cr^{3+} '
                         '(0.05\\%)$$',
                   'text': '<strong>3-Level Laser System:</strong> Ground state $^4A_2$ ($E_1$), pump bands $^4F_1, '
                           '^4F_2$ ($E_3$), metastable state $^2E$ ($E_2$, lifetime $\\approx 3\\text{ '
                           'ms}$).<br><strong>Pumping:</strong> Xenon helical flash lamp ($550\\text{ nm}$ green '
                           'band).<br><strong>Fast Decay:</strong> $E_3 \\to E_2$ non-radiative phonon '
                           'decay.<br><strong>Drawback:</strong> High threshold pumping power since $>50\\%$ of all '
                           'ground atoms must be excited for inversion.'},
    'phy-q23': {   'eq': '$$\\lambda = 632.8\\text{ nm (Continuous Wave Red)}, \\quad \\text{He : Ne Ratio} = 10 : 1$$',
                   'text': '<strong>4-Level Gas Laser:</strong> Continuous wave (CW) '
                           'operation.<br><strong>Pumping:</strong> Electric discharge excites He atoms to metastable '
                           '$2^1S_0$ ($20.61\\text{ eV}$) and $2^3S_1$ ($19.82\\text{ eV}$).<br><strong>Resonant '
                           'Collisions:</strong> Transfer energy to Ne $3s$ ($20.66\\text{ eV}$) and $2s$ '
                           '($19.78\\text{ eV}$) levels.<br><strong>Laser Transition:</strong> Ne $3s \\to 2p$ '
                           '($632.8\\text{ nm}$). Narrow bore ($2-4\\text{ mm}$) ensures wall-collision '
                           'de-excitation.'},
    'phy-q24': {   'eq': '$$\\lambda \\approx \\frac{1.24}{E_g\\text{ (in eV)}}\\ \\mu\\text{m}, \\quad (E_{Fn} - '
                         'E_{Fp}) > h\\nu > E_g, \\quad \\text{GaAs: } \\lambda \\approx 873\\text{ nm}$$',
                   'text': '<strong>Direct Bandgap Requirement:</strong> Direct electron-hole recombination conserves '
                           'crystal momentum ($k = 0$).<br><strong>Degenerate Doping:</strong> Heavy $p^{++}$ and '
                           '$n^{++}$ doping shifts Fermi levels into valence/conduction bands.<br><strong>Population '
                           'Inversion:</strong> Forward bias injects high-density minority carriers into active '
                           'depletion layer.<br><strong>Cavity:</strong> Cleaved natural $(110)$ crystal facets '
                           'provide $\\approx 32\\%$ Fresnel reflection.'},
    'phy-q25': {   'eq': '$$\\theta_a = \\sin^{-1}\\left(\\sqrt{n_1^2 - n_2^2}\\right), \\quad NA = \\sin\\theta_a = '
                         '\\sqrt{n_1^2 - n_2^2} \\approx n_1 \\sqrt{2\\Delta}$$',
                   'text': '<strong>Total Internal Reflection (TIR):</strong> Requires $n_1 > n_2$ and incidence angle '
                           '$\\phi \\ge \\phi_c = \\sin^{-1}(n_2/n_1)$.<br><strong>Acceptance Angle '
                           '($\\theta_a$):</strong> Maximum semi-cone launch angle for TIR: $\\sin\\theta_a = '
                           '\\sqrt{n_1^2 - n_2^2}$.<br><strong>Numerical Aperture ($NA$):</strong> Light-collecting '
                           'capacity: $NA = n_1 \\sqrt{2\\Delta}$, where $\\Delta = (n_1 - n_2)/n_1$.'},
    'phy-q26': {   'eq': '$$V = \\frac{2\\pi a}{\\lambda}\\sqrt{n_1^2 - n_2^2} \\le 2.405\\text{ (Single Mode)}, '
                         '\\quad \\alpha = \\frac{10}{L}\\log_{10}\\left(\\frac{P_{in}}{P_{out}}\\right), \\quad '
                         '\\alpha_{\\text{Rayleigh}} \\propto \\frac{1}{\\lambda^4}$$',
                   'text': '<strong>Index Profiles:</strong> Step-Index (abrupt step) vs Graded-Index (parabolic '
                           'profile, minimizes intermodal dispersion).<br><strong>Modes:</strong> Single-Mode ($V \\le '
                           '2.405$, $8-10\\ \\mu\\text{m}$ core, zero intermodal dispersion) vs Multimode ($V > '
                           '2.405$, $50-62.5\\ \\mu\\text{m}$ core).<br><strong>Losses:</strong> Absorption (UV '
                           'electronic, IR lattice, $OH^-$ peaks at $1.38\\ \\mu\\text{m}$), Rayleigh scattering '
                           '($\\propto 1/\\lambda^4$), and bending losses (macrobending & microbending).'},
    'phy-q3': {   'eq': '$$\\omega_r = \\sqrt{\\omega_0^2 - 2\\gamma^2}, \\quad Q = \\frac{\\omega_0}{2\\gamma} = '
                        '\\frac{\\omega_0}{\\Delta \\omega}, \\quad \\delta = \\gamma T = \\frac{\\pi}{Q}$$',
                  'text': '<strong>Resonant Frequency:</strong> Amplitude resonance occurs at $\\omega_r = '
                          '\\sqrt{\\omega_0^2 - 2\\gamma^2} < \\omega_0$.<br><strong>Quality Factor ($Q$):</strong> $Q '
                          '= 2\\pi \\frac{\\text{Energy Stored}}{\\text{Energy Lost / Cycle}} = '
                          '\\frac{\\omega_0}{\\text{Bandwidth }\\Delta\\omega}$. Higher $Q$ means sharper resonance '
                          'and lower damping.<br><strong>Logarithmic Decrement ($\\delta$):</strong> $\\delta = '
                          '\\ln(A_n / A_{n+1}) = \\gamma T = \\pi / Q$.'},
    'phy-q4': {   'eq': '$$\\frac{\\partial^2 y}{\\partial t^2} = v^2 \\frac{\\partial^2 y}{\\partial x^2}, \\quad '
                        '\\text{where } v = \\sqrt{\\frac{T}{\\mu}}$$',
                  'text': '<strong>1D Wave Equation:</strong> Relates local acceleration to spatial curvature in a '
                          'continuous elastic medium.<br><strong>Wave Velocity on Stretched String:</strong> $v = '
                          '\\sqrt{T/\\mu}$, where $T$ is tension and $\\mu$ is linear mass '
                          "density.<br><strong>D'Alembert Solution:</strong> $y(x,t) = f(x - vt) + g(x + vt)$."},
    'phy-q5': {   'eq': '$$f_n = \\frac{n v}{2L} = \\frac{n}{2L}\\sqrt{\\frac{T}{\\mu}}, \\quad \\lambda_n = '
                        '\\frac{2L}{n}, \\quad n = 1, 2, 3, \\dots$$',
                  'text': '<strong>Standing Wave Modes:</strong> Fixed ends require nodes at $x = 0$ and $x = L$, '
                          'giving quantized wave vectors $k_n = n\\pi / L$.<br><strong>Harmonics:</strong> Supports '
                          "all harmonics $f_n = n f_1$ ($f_1 = \\frac{1}{2L}\\sqrt{T/\\mu}$).<br><strong>Mersenne's "
                          'Laws:</strong> $f \\propto 1/L$, $f \\propto \\sqrt{T}$, $f \\propto 1/\\sqrt{\\mu}$.'},
    'phy-q6': {   'eq': '$$\\Delta = 2\\mu t \\cos r - \\frac{\\lambda}{2} \\implies \\text{Bright: } 2\\mu t \\cos r '
                        '= (2n + 1)\\frac{\\lambda}{2}, \\quad \\text{Dark: } 2\\mu t \\cos r = n\\lambda$$',
                  'text': '<strong>Geometric Path Difference:</strong> $\\Delta_{geom} = 2\\mu t \\cos '
                          "r$.<br><strong>Stokes' Phase Shift:</strong> Reflection at an optically denser medium "
                          'introduces an equivalent path difference of $\\lambda/2$.<br><strong>Zero Thickness ($t '
                          '\\to 0$):</strong> Effective path difference $\\Delta = -\\lambda/2$, causing destructive '
                          'interference across all visible wavelengths (very thin film appears pitch black).'},
    'phy-q7': {   'eq': '$$\\beta = \\frac{\\lambda L}{2d} \\implies d = \\frac{\\lambda L}{2\\beta}$$',
                  'text': '<strong>Air Wedge Fringe Width:</strong> $\\beta = \\frac{\\lambda}{2\\theta} = '
                          '\\frac{\\lambda L}{2d}$, producing equidistant, straight, parallel fringes.<br><strong>Apex '
                          'Line of Contact:</strong> Always a dark fringe ($2t = 0 \\cdot \\lambda$).<br><strong>Wire '
                          'Diameter ($d$):</strong> Measured using travelling microscope: $d = \\frac{\\lambda '
                          'L}{2\\beta}$.'},
    'phy-q8': {   'eq': '$$D_n^2 = 4n R \\lambda \\text{ (Dark)}, \\quad \\lambda = \\frac{D_{n+p}^2 - D_n^2}{4 p R}, '
                        '\\quad \\mu = \\frac{(D_{n+p}^2 - D_n^2)_{air}}{(D_{n+p}^2 - D_n^2)_{liquid}}$$',
                  'text': '<strong>Air Film Thickness:</strong> $t = r^2 / 2R$.<br><strong>Dark Ring '
                          'Diameters:</strong> $D_n \\propto \\sqrt{n}$ ($D_n = 2\\sqrt{n R \\lambda}$); center is '
                          'dark ($D_0 = 0$).<br><strong>Bright Ring Diameters:</strong> $D_n \\propto \\sqrt{2n - '
                          '1}$.<br><strong>Liquid Film:</strong> Fringes contract when liquid of index $\\mu > 1$ is '
                          'introduced ($D_n \\propto 1/\\sqrt{\\mu}$).'},
    'phy-q9': {   'eq': '$$I(\\theta) = I_0 \\left(\\frac{\\sin\\alpha}{\\alpha}\\right)^2, \\quad \\alpha = '
                        '\\frac{\\pi a \\sin\\theta}{\\lambda}, \\quad \\text{Minima: } a \\sin\\theta = m\\lambda$$',
                  'text': '<strong>Fraunhofer Single Slit:</strong> Sinc-squared intensity pattern.<br><strong>Central '
                          'Maximum:</strong> Width $2\\theta_1 = 2\\lambda/a$, contains $>90\\%$ of total optical '
                          'energy.<br><strong>Diffraction Minima:</strong> $a \\sin\\theta = \\pm m\\lambda$ ($m = 1, '
                          '2, 3, \\dots$).<br><strong>Secondary Maxima:</strong> Occur at $\\tan\\alpha = \\alpha$ '
                          'with rapidly falling intensities ($I_1 \\approx 4.7\\% I_0, I_2 \\approx 1.65\\% I_0$).'},
    'ps2-q1': {   'eq': '$$i(t) = \\frac{V_m}{|Z|} \\sin(\\omega t + \\alpha - \\theta) - \\frac{V_m}{|Z|} '
                        '\\sin(\\alpha - \\theta) e^{-t/\\tau}, \\quad i_{peak} \\approx 2 \\frac{V_m}{|Z|}$$',
                  'text': 'Short circuit on an RL line produces a symmetrical AC wave plus a decaying DC offset. If '
                          'fault occurs at voltage zero ($\\alpha - \\theta = -\\pi/2$), maximum DC offset causes the '
                          'Doubling Effect ($i_{peak} \\approx 2 I_m$).'},
    'ps2-q10': {   'eq': '$$V_{a1} = V_{a2} = V_{a0} - 3 I_{a0} Z_f, \\quad I_{a1} = \\frac{E_a}{Z_1 + \\frac{Z_2 (Z_0 '
                         '+ 3 Z_f)}{Z_2 + Z_0 + 3 Z_f}}, \\quad I_f = 3 I_{a0}$$',
                   'text': 'Double Line-to-Ground fault enforces equal sequence voltages, requiring a Parallel '
                           'interconnection of positive, negative, and zero sequence networks; total ground fault '
                           'current is $3I_{a0}$.'},
    'ps2-q11': {   'eq': '$$Y_{ii} = \\sum_{k\\ne i} y_{ik} + y_{i0}, \\quad Y_{ik} = -y_{ik}; \\quad \\text{Slack: } '
                         '|V|, \\delta; \\quad \\text{PV: } P, |V|; \\quad \\text{PQ: } P, Q$$',
                   'text': 'Slack bus fixes $|V|, \\delta=0$ to balance losses; PV bus regulates voltage with reactive '
                           'limits ($Q_{min} \\le Q \\le Q_{max}$); PQ bus demands real and reactive power. $Y_{bus}$ '
                           'is symmetric and sparse.'},
    'ps2-q12': {   'eq': '$$P_i = \\sum_{k=1}^n |V_i| |V_k| |Y_{ik}| \\cos(\\theta_{ik} + \\delta_k - \\delta_i), '
                         '\\quad Q_i = -\\sum_{k=1}^n |V_i| |V_k| |Y_{ik}| \\sin(\\theta_{ik} + \\delta_k - '
                         '\\delta_i)$$',
                   'text': 'Static power flow equations derived from $S_i^* = P_i - jQ_i = V_i^* \\sum Y_{ik} V_k$. '
                           'Real power depends primarily on angle differences ($\\delta_k - \\delta_i$); reactive '
                           'power depends on voltage magnitudes.'},
    'ps2-q13': {   'eq': '$$V_i^{(m+1)} = \\frac{1}{Y_{ii}} \\left[ \\frac{P_i - j Q_i}{(V_i^{(m)})^*} - '
                         '\\sum_{k=1}^{i-1} Y_{ik} V_k^{(m+1)} - \\sum_{k=i+1}^n Y_{ik} V_k^{(m)} \\right], \\quad '
                         'V_i^{acc} = V_i^{(m)} + \\alpha(V_i^{(m+1)} - V_i^{(m)})$$',
                   'text': 'Gauss-Seidel substitutes updated voltages immediately, accelerated by factor $\\alpha '
                           '\\approx 1.4 \\text{ to } 1.6$. PV buses estimate $Q_i$; if $Q_i$ violates limits, bus '
                           'converts to PQ type.'},
    'ps2-q14': {   'eq': '$$\\begin{bmatrix} \\Delta P \\\\ \\Delta Q \\end{bmatrix} = \\begin{bmatrix} H & N \\\\ M & '
                         'L \\end{bmatrix} \\begin{bmatrix} \\Delta\\delta \\\\ \\Delta|V|/|V| \\end{bmatrix}, \\quad '
                         'H_{ii} = -Q_i - |V_i|^2 B_{ii}, \\quad L_{ii} = Q_i - |V_i|^2 B_{ii}$$',
                   'text': 'Newton-Raphson linearizes power flow using Jacobian matrix with quadratic convergence (3-5 '
                           'iterations). Off-diagonals satisfy $M_{ik} = -N_{ik}$ and $L_{ik} = H_{ik}$.'},
    'ps2-q15': {   'eq': "$$\\left[\\frac{\\Delta P}{|V|}\\right] = [B'][\\Delta\\delta], \\quad \\left[\\frac{\\Delta "
                         "Q}{|V|}\\right] = [B''][\\Delta|V|], \\quad R \\ll X, \\quad \\cos(\\delta_i - \\delta_k) "
                         '\\approx 1$$',
                   'text': "Fast Decoupled Load Flow exploits $P-\\delta$ and $Q-V$ physical decoupling. Matrices $B'$ "
                           "and $B''$ are constant, real, symmetric, and inverted only once, accelerating computations "
                           '5-fold.'},
    'ps2-q16': {   'eq': '$$\\frac{2H}{\\omega_s} \\frac{d^2\\delta}{dt^2} = P_m - P_e \\quad \\text{or} \\quad '
                         '\\frac{H}{\\pi f} \\frac{d^2\\delta}{dt^2} = P_m - P_e, \\quad M = \\frac{G H}{\\pi f}$$',
                   'text': 'Swing equation governs rotor acceleration driven by power imbalance $P_m - P_e$. Inertia '
                           'constant $H$ defines kinetic energy in MJ per MVA rating, normalized across machines.'},
    'ps2-q17': {   'eq': '$$P_e = \\frac{|E||V|}{X} \\sin\\delta = P_{max} \\sin\\delta, \\quad P_{syn} = '
                         '\\frac{dP_e}{d\\delta} = P_{max} \\cos\\delta > 0 \\implies 0 \\le \\delta < 90^\\circ$$',
                   'text': 'Cylindrical rotor electrical power follows sinusoidal curve peaking at $\\delta = '
                           '90^\\circ$. Steady-state stability requires positive synchronizing power ($P_{syn} > 0$), '
                           'limiting stable operation to $\\delta < 90^\\circ$.'},
    'ps2-q18': {   'eq': '$$\\int_{\\delta_0}^{\\delta_{max}} (P_m - P_e) \\, d\\delta = 0 \\implies A_1 = A_2 \\quad '
                         '(\\text{Accelerating Area } = \\text{ Decelerating Area})$$',
                   'text': 'Equal Area Criterion determines transient stability without solving differential '
                           'equations. Stored kinetic energy gained during acceleration ($A_1$) must be completely '
                           'absorbed during deceleration ($A_2$).'},
    'ps2-q19': {   'eq': '$$\\cos\\delta_{cr} = \\frac{P_m(\\delta_{max} - \\delta_0) - P_{max2}\\cos\\delta_0 + '
                         'P_{max3}\\cos\\delta_{max}}{P_{max3} - P_{max2}}, \\quad t_{cr} = '
                         '\\sqrt{\\frac{2H(\\delta_{cr} - \\delta_0)}{\\pi f P_m}}$$',
                   'text': 'Critical Clearing Angle $\\delta_{cr}$ defines the maximum allowable rotor advance before '
                           'fault isolation. Breakers must trip before critical clearing time $t_{cr}$ to preserve '
                           'transient stability.'},
    'ps2-q2': {   'eq': "$$I'' = \\frac{E_g}{X_d''}, \\quad I' = \\frac{E_g}{X_d'}, \\quad I = \\frac{E_g}{X_d}, "
                        "\\quad E'' = V_t + j I_L X_d''$$",
                  'text': "Damper currents choke stator flux in subtransient period ($X_d''$), field currents resist "
                          "in transient period ($X_d'$), settling to steady state ($X_d$). Subtransient internal "
                          "voltage $E'' = V_t + j I_L X_d''$."},
    'ps2-q20': {   'eq': '$$E_{acc} \\propto t^2, \\quad X_{eff} = X_{line} - X_C, \\quad P_{max} = '
                         '\\frac{|E||V|}{X_{eff}}$$',
                   'text': 'Stability is enhanced by 2-cycle fast fault clearing, high-speed auto-reclosing, dynamic '
                           'braking resistors, fast static excitation with PSS, series capacitors, and FACTS '
                           'controllers (STATCOM/SVC/TCSC).'},
    'ps2-q21': {   'eq': '$$\\Delta f_{ss} = \\frac{-\\Delta P_L}{D + \\frac{1}{R}} = \\frac{-\\Delta P_L}{\\beta}, '
                         '\\quad K_p = \\frac{1}{D}, \\quad \\tau_p = \\frac{2H}{f_0 D}$$',
                   'text': 'Primary governor droop leaves a steady-state frequency drop $\\Delta f_{ss} = -\\Delta P_L '
                           '/ \\beta$, where $\\beta = D + 1/R$ is system stiffness. Secondary integral control is '
                           'required to restore frequency to $50 \\text{ Hz}$.'},
    'ps2-q22': {   'eq': '$$ACE_1 = \\Delta P_{tie1} + B_1 \\Delta f_1, \\quad \\Delta P_{tie12} = \\frac{2\\pi '
                         'T_{12}}{s} (\\Delta f_1 - \\Delta f_2), \\quad B_i = \\beta_i = D_i + \\frac{1}{R_i}$$',
                   'text': 'In interconnected two-area systems, each area regulates its own Area Control Error ($ACE = '
                           '\\Delta P_{tie} + B \\Delta f$) via integral control, driving steady-state frequency and '
                           'tie-line deviations to zero.'},
    'ps2-q23': {   'eq': '$$G_{open}(s) = \\frac{K_A K_E K_F K_R}{(1 + s\\tau_A)(1 + s\\tau_E)(1 + s\\tau_F)(1 + '
                         's\\tau_R)}$$',
                   'text': 'Automatic Voltage Regulator controls exciter voltage to maintain terminal voltage $|V_t|$. '
                           'Rate feedback transformer stabilizers introduce phase lead to prevent oscillatory '
                           'instability from exciter-generator lag poles.'},
    'ps2-q24': {   'eq': '$$\\frac{dC_1}{dP_1} = \\frac{dC_2}{dP_2} = \\dots = \\frac{dC_N}{dP_N} = \\lambda, \\quad '
                         '\\sum_{i=1}^N P_i = P_D, \\quad P_{i, min} \\le P_i \\le P_{i, max}$$',
                   'text': 'Economic load dispatch neglecting losses mandates that all generating units operate at the '
                           'Equal Incremental Fuel Cost $\\lambda$. Constrained units are pegged at their limit, and '
                           'remaining load is re-dispatched.'},
    'ps2-q25': {   'eq': '$$\\frac{dC_i}{dP_i} \\cdot L_i = \\lambda, \\quad L_i = \\frac{1}{1 - \\frac{\\partial '
                         'P_L}{\\partial P_i}}, \\quad P_L = \\sum\\sum P_m B_{mn} P_n$$',
                   'text': 'Economic dispatch including losses coordinates incremental fuel cost with transmission '
                           'Penalty Factor $L_i$. Remote units with high incremental losses ($L_i > 1$) are backed '
                           'down to optimize overall delivered cost.'},
    'ps2-q26': {   'eq': '$$\\lambda = 27.55 \\text{ Rs/MWh}, \\quad P_1 = 75.45 \\text{ MW}, \\quad P_2 = 104.55 '
                         '\\text{ MW}, \\quad \\text{Net Savings} = 23.27 \\text{ Rs/h}$$',
                   'text': 'Equal incremental cost dispatch allocates $P_1 = 75.45 \\text{ MW}, P_2 = 104.55 \\text{ '
                           'MW}$ at $\\lambda = 27.55 \\text{ Rs/MWh}$, reducing generation costs by $23.27 \\text{ '
                           'Rs/h}$ ($203,845 \\text{ Rs/year}$) over equal sharing.'},
    'ps2-q3': {   'eq': '$$SCMVA = \\frac{MVA_{base}}{X_{th, pu}}, \\quad I_{making, peak} = 1.6 \\times \\sqrt{2} '
                        '\\times I_{sc, sym} \\approx 2.55 \\times I_{sc, sym}$$',
                  'text': 'Short Circuit MVA measures fault severity. Breaker rated making current ($2.55 I_{sc}$) '
                          'withstands peak first-cycle electromechanical forces; interrupting current is evaluated at '
                          'contact separation (2 to 5 cycles).'},
    'ps2-q4': {   'eq': '$$Z_{ij}^{new} = Z_{ij}^{old} - \\frac{Z_{iq} Z_{qj}}{Z_{qq}}, \\quad I_{f, k} = '
                        '\\frac{V_k(0)}{Z_{kk}}, \\quad V_i^{fault} = V_i(0) - \\frac{Z_{ik}}{Z_{kk}} V_k(0)$$',
                  'text': 'Z_bus algorithm builds impedance matrix by adding branches in 4 topological types. '
                          'Loop-closing branches (Types 3 and 4) are eliminated by Kron reduction. Driving-point '
                          'impedance $Z_{kk}$ directly yields fault current.'},
    'ps2-q5': {   'eq': '$$X_{th} = 0.25 \\parallel 0.7035 = 0.1844 \\text{ pu}, \\quad I_f = 2.371 \\text{ kA}, '
                        '\\quad SCMVA = 542.3 \\text{ MVA}$$',
                  'text': 'Per-unit reactance diagram combines parallel generator-transformer branches to fault bus: '
                          '$X_{th} = 0.1844 \\text{ pu}$, giving fault current $I_f = 2.371 \\text{ kA}$ and $SCMVA = '
                          '542.3 \\text{ MVA}$ on $100 \\text{ MVA}$ base.'},
    'ps2-q6': {   'eq': '$$V_{abc} = A V_{012}, \\quad A = \\begin{bmatrix} 1 & 1 & 1 \\\\ 1 & a^2 & a \\\\ 1 & a & '
                        'a^2 \\end{bmatrix}, \\quad a = 1\\angle 120^\\circ, \\quad 1 + a + a^2 = 0$$',
                  'text': "Fortescue's theorem resolves unbalanced 3-phase phasors into positive ($1, a^2, a$), "
                          'negative ($1, a, a^2$), and zero ($1, 1, 1$) sequence sets. Complex power is strictly '
                          'invariant: $S_{3\\phi} = 3(V_0 I_0^* + V_1 I_1^* + V_2 I_2^*)$.'},
    'ps2-q7': {   'eq': '$$Z_0 = Z_{g0} + 3 Z_n, \\quad Z_1 = Z_2 = Z_{leakage} \\text{ (Transformer)}, \\quad Z_0 '
                        '\\approx 2.5 \\text{ to } 3.5 \\times Z_1 \\text{ (Line)}$$',
                  'text': 'Generator neutral grounding impedance appears as $3Z_n$ in zero-sequence network. '
                          'Transformers block zero sequence unless grounded star ($Y_g$); delta ($\\Delta$) circulates '
                          'zero sequence internally.'},
    'ps2-q8': {   'eq': '$$I_{a0} = I_{a1} = I_{a2} = \\frac{E_a}{Z_1 + Z_2 + Z_0 + 3 Z_f}, \\quad I_f = 3 I_{a1} = '
                        '\\frac{3 E_a}{Z_1 + Z_2 + Z_0 + 3 Z_f}$$',
                  'text': 'Single Line-to-Ground fault enforces identical sequence currents ($I_{a0} = I_{a1} = '
                          'I_{a2}$), requiring a Series interconnection of positive, negative, and zero sequence '
                          'networks with $3Z_f$ inserted.'},
    'ps2-q9': {   'eq': '$$I_{a0} = 0, \\quad I_{a1} = -I_{a2} = \\frac{E_a}{Z_1 + Z_2 + Z_f}, \\quad I_f = '
                        '-j\\sqrt{3} I_{a1} = \\frac{\\sqrt{3} E_a}{Z_1 + Z_2 + Z_f} \\angle -90^\\circ$$',
                  'text': 'Line-to-Line fault has zero sequence current ($I_{a0} = 0$). Positive and negative sequence '
                          'networks connect in Parallel opposition; fault current is $\\sqrt{3} I_{a1} \\approx '
                          '86.6\\%$ of 3-phase fault.'},
    'res-q1': {   'eq': '$$I_{sc} = 1367 \\text{ W/m}^2, \\quad AM = \\frac{1}{\\cos\\theta_z} = \\sec\\theta_z, '
                        '\\quad I_{on} = I_{sc}\\left[1 + 0.033\\cos\\left(\\frac{360n}{365}\\right)\\right]$$',
                  'text': '<strong>Solar Constant:</strong> $I_{sc} = 1367\\text{ W/m}^2$ is the extraterrestrial '
                          'solar irradiance normal to the beam at mean earth-sun distance.<br><strong>Air '
                          'Mass:</strong> $AM = 1/\\cos\\theta_z$ defines optical atmospheric path length ($AM0$ in '
                          'space, $AM1.5$ with $1000\\text{ W/m}^2$ for terrestrial testing).'},
    'res-q10': {   'eq': '$$P_{import} = P_{load} - P_{pv}, \\quad t_{islanding} \\le 2.0\\text{ s}$$',
                   'text': '<strong>Stand-Alone PV:</strong> Battery storage bank, MPPT charge controller, and '
                           'off-grid inverter operate autonomously.<br><strong>Grid-Tied PV:</strong> Grid-interactive '
                           'inverter synchronizes via PLL; mandatory IEEE 1547 anti-islanding shuts down within 2 '
                           'seconds of grid loss.'},
    'res-q11': {   'eq': '$$P_w = \\frac{1}{2}\\rho A v^3, \\quad C_p = 4a(1-a)^2, \\quad C_{p,\\max} = \\frac{16}{27} '
                         '\\approx 0.5926 \\quad (\\text{at } a = 1/3)$$',
                   'text': '<strong>Wind Power:</strong> Proportional to cube of wind speed ($v^3$).<br><strong>Betz '
                           'Limit:</strong> By 1D actuator disc theory, optimal axial induction factor is $a = 1/3$, '
                           'establishing maximum aerodynamic power coefficient $C_{p,\\max} = 16/27 \\approx '
                           '59.3\\%$.'},
    'res-q12': {   'eq': '$$\\lambda = \\frac{\\omega R}{v}, \\quad HAWT: \\lambda \\approx 7-10 \\ (C_p \\approx '
                         '0.48), \\quad VAWT: \\lambda \\approx 1-4$$',
                   'text': '<strong>HAWT:</strong> Lift-based airfoil blades with high tip-speed ratio ($\\lambda$) '
                           'and high efficiency ($C_p \\approx 0.48$); requires active yaw '
                           'tracking.<br><strong>VAWT:</strong> Savonius (drag) and Darrieus (lift) operate '
                           'omnidirectionally with ground-level drive train, but lower efficiency and high cyclic '
                           'fatigue.'},
    'res-q13': {   'eq': '$$n_{generator} = G_{ratio} \\times n_{rotor} \\implies 1500\\text{ rpm} = 100 \\times '
                         '15\\text{ rpm}$$',
                   'text': 'Nacelle houses low-speed shaft ($15\\text{ rpm}$), planetary/helical gearbox ($1:100$ '
                           'speed increase), high-speed shaft with mechanical disc brake, generator, independent blade '
                           'pitch actuators, yaw ring drive, and anemometer sensors.'},
    'res-q14': {   'eq': '$$P_{rotor} = s \\cdot P_{stator}, \\quad s = \\frac{N_s - N_r}{N_s} \\in [-0.3, +0.3], '
                         '\\quad P_{net} = P_{stator} + |P_{rotor}|$$',
                   'text': '<strong>DFIG:</strong> Stator connects directly to grid; rotor connects via slip rings and '
                           'partial-scale converter ($25-30\\%$ rating) handling slip power.<br><strong>PMSG:</strong> '
                           'Direct-drive multi-pole synchronous machine with permanent magnets; connected via $100\\%$ '
                           'full-scale converter, eliminating gearbox.'},
    'res-q15': {   'eq': '$$T_e = k_{opt}\\omega^2 \\ (\\text{Region 2 MPPT}), \\quad P = P_{rated} = \\text{const} \\ '
                         '(\\text{Region 3 Pitch Regulation})$$',
                   'text': '<strong>Region 1:</strong> Below cut-in ($<3\\text{ m/s}$).<br><strong>Region 2:</strong> '
                           'MPPT ($3-12\\text{ m/s}$) tracking optimal tip-speed ratio '
                           '($\\lambda_{opt}$).<br><strong>Region 3:</strong> Rated power ($12-25\\text{ m/s}$) where '
                           'pitch actuators feather blades.<br><strong>Region 4:</strong> Cut-out ($>25\\text{ m/s}$) '
                           'shutdown.'},
    'res-q16': {   'eq': '$$C + CO_2 \\rightleftharpoons 2 CO, \\quad C + H_2 O \\rightleftharpoons CO + H_2, \\quad '
                         '\\text{LHV} \\approx 4.5-6.0\\text{ MJ/Nm}^3$$',
                   'text': '<strong>Direct Combustion:</strong> Full oxidation with excess air '
                           '($800-1100^\\circ\\text{C}$).<br><strong>Gasification:</strong> Partial oxidation '
                           '($\\lambda = 0.3$) producing syngas/producer gas ($CO + '
                           'H_2$).<br><strong>Pyrolysis:</strong> Oxygen-free thermal cracking at '
                           '$500^\\circ\\text{C}$ yielding liquid bio-oil.'},
    'res-q17': {   'eq': '$$\\text{Hydrolysis} \\to \\text{Acidogenesis (VFAs)} \\to \\text{Acetogenesis (Acetic '
                         'Acid)} \\to \\text{Methanogenesis (CH}_4\\text{)}$$',
                   'text': 'Anaerobic digestion degrades organic matter in four steps. Methanogens convert acetic acid '
                           'and $H_2 + CO_2$ to methane ($55-70\\% \\text{ CH}_4$). Optimum parameters: $C/N = '
                           '25-30:1$, mesophilic temp $35-38^\\circ\\text{C}$, neutral pH $6.8-7.5$.'},
    'res-q18': {   'eq': '$$P_{KVIC} = \\text{Constant } (8-12\\text{ cm } H_2O), \\quad P_{Deenabandhu} = '
                         '\\text{Variable } (0-100\\text{ cm } H_2O)$$',
                   'text': '<strong>Floating Drum (KVIC):</strong> Inverted mild steel drum maintains constant gas '
                           'pressure; higher cost and corrosion.<br><strong>Fixed Dome (Deenabandhu):</strong> '
                           'Underground brick masonry dome with slurry displacement chamber; lower cost, zero moving '
                           'parts, long lifespan.'},
    'res-q19': {   'eq': '$$\\eta_{Carnot} = \\frac{T_H - T_C}{T_H} \\approx \\frac{300.15 - 278.15}{300.15} \\approx '
                         '7.33\\%, \\quad \\eta_{net} \\approx 2.5-4.0\\%$$',
                   'text': 'OTEC exploits thermal gradient ($\\Delta T \\approx 20^\\circ\\text{C}$) between surface '
                           'warm water ($26^\\circ\\text{C}$) and deep water ($5^\\circ\\text{C}$). Closed Rankine '
                           'cycle uses ammonia; Open Claude cycle flash-evaporates seawater into low-pressure steam, '
                           'co-producing desalinated water.'},
    'res-q2': {   'eq': '$$\\delta = 23.45^\\circ \\sin\\left[\\frac{360}{365}(284 + n)\\right], \\quad \\sin\\alpha = '
                        '\\cos\\theta_z = \\sin\\phi\\sin\\delta + \\cos\\phi\\cos\\delta\\cos\\omega$$',
                  'text': '<strong>Declination ($\\delta$):</strong> Angle between sun-earth line and equatorial plane '
                          '($-23.45^\\circ \\le \\delta \\le +23.45^\\circ$).<br><strong>Hour Angle '
                          '($\\omega$):</strong> Earth rotation displacement ($15^\\circ/\\text{hr}$, '
                          '$\\omega=0^\\circ$ at solar noon).<br><strong>Zenith ($\\theta_z$) & Altitude '
                          '($\\alpha$):</strong> $\\alpha + \\theta_z = 90^\\circ$.'},
    'res-q20': {   'eq': '$$E = \\frac{1}{2} \\rho g A R^2, \\quad P_{avg} = \\frac{\\rho g A R^2}{2 T_{tide}}, \\quad '
                         '\\text{Wells Turbine Lift: } F_{tan} > 0 \\ (\\forall \\text{ flow})$$',
                   'text': '<strong>Tidal Barrage:</strong> Potential energy is proportional to basin area $A$ and '
                           'square of tidal range ($R^2$).<br><strong>Oscillating Water Column (OWC):</strong> Waves '
                           'compress/expand air column driving a Wells turbine whose symmetrical blades rotate '
                           'unidirectionally.'},
    'res-q21': {   'eq': '$$E_0 = -\\frac{\\Delta G}{n F} \\approx 1.229\\text{ V}, \\quad \\eta_{th} = \\frac{\\Delta '
                         'G}{\\Delta H} \\approx 83.0\\%, \\quad V_{cell} = E_0 - \\Delta V_{act} - \\Delta V_{ohm} - '
                         '\\Delta V_{conc}$$',
                   'text': 'Hydrogen fuel cell converts chemical energy directly into DC electricity and water. '
                           'Thermodynamic efficiency is $\\Delta G / \\Delta H \\approx 83\\%$. Polarization '
                           'overpotentials comprise activation (charge transfer), ohmic (electrolyte resistance), and '
                           'concentration (mass transport).'},
    'res-q22': {   'eq': '$$\\text{PEMFC: } H^+ \\text{ ion, } 60-80^\\circ\\text{C}, \\ Pt \\text{ catalyst}; \\quad '
                         '\\text{SOFC: } O^{2-} \\text{ ion, } 700-1000^\\circ\\text{C}, \\ \\text{YSZ ceramic}$$',
                   'text': '<strong>PEMFC:</strong> Solid polymer membrane conducts protons at $80^\\circ\\text{C}$ '
                           'with Pt catalyst; fast startup for FCEVs, requires pure $H_2$.<br><strong>SOFC:</strong> '
                           'Yttria-stabilized zirconia ceramic conducts $O^{2-}$ at $800-1000^\\circ\\text{C}$; '
                           'fuel-flexible (internal reforming of $CH_4$), excellent for CHP baseload.'},
    'res-q23': {   'eq': '$$SoC(t) = SoC(t_0) - \\frac{1}{Q_n}\\int I(t)\\,dt, \\quad DoD = 1 - SoC, \\quad '
                         '\\text{VRFB: } V^{2+}/V^{3+} \\leftrightarrow V^{4+}/V^{5+}$$',
                   'text': '<strong>BESS:</strong> Lithium-ion ($90-95\\%$ efficiency, $150-250\\text{ Wh/kg}$) '
                           'dominates EVs and grid support.<br><strong>Redox Flow (VRFB):</strong> Liquid vanadium '
                           'electrolytes decouple power (stack area) from energy (tank '
                           'volume).<br><strong>Degradation:</strong> SEI growth, lithium plating, and high DoD '
                           'cycling.'},
    'res-q24': {   'eq': '$$P_{ren}(t) = P_{pv}(t) + P_{wind}(t), \\quad P_{net}(t) = P_{load}(t) - P_{ren}(t) = '
                         'P_{batt}(t) + P_{diesel}(t)$$',
                   'text': 'Hybrid renewable systems exploit seasonal and diurnal complementarity between solar and '
                           'wind.<br><strong>DC-Coupled:</strong> High battery charging efficiency via common DC '
                           'bus.<br><strong>AC-Coupled:</strong> High modularity with standard grid '
                           'inverters.<br><strong>EMS Dispatch:</strong> Prioritizes renewables $\\to$ battery $\\to$ '
                           'diesel generator.'},
    'res-q25': {   'eq': '$$f = f_0 - m_p(P - P_0), \\quad V = V_0 - n_q(Q - Q_0), \\quad m_p = \\frac{\\Delta '
                         'f_{\\max}}{P_{\\max}}$$',
                   'text': '<strong>Microgrid Modes:</strong> Grid-connected (inverters follow P-Q grid) vs Islanded '
                           '(grid-forming inverters regulate $V$ and $f$).<br><strong>Droop Control:</strong> Emulates '
                           'synchronous generator governor via $P-f$ active droop and $Q-V$ reactive droop, enabling '
                           'decentralized power sharing without communications.'},
    'res-q26': {   'eq': '$$\\frac{df}{dt} = \\frac{f_0 (P_m - P_e)}{2 H S_n}, \\quad I_q \\ge 2\\% \\text{ per } 1\\% '
                         '\\ \\Delta V \\ (\\text{LVRT})$$',
                   'text': '<strong>Duck Curve:</strong> Midday net-load plunge followed by steep evening ramp '
                           'requirement.<br><strong>Low Inertia:</strong> Non-synchronous inverters lower system '
                           'inertia $H$, amplifying $RoCoF$.<br><strong>LVRT:</strong> Mandatory grid code requiring '
                           'inverters to stay connected and inject reactive current $I_q$ during grid faults down to '
                           '$0.15\\text{ pu}$.'},
    'res-q3': {   'eq': '$$V_{out} = C_{cal} \\cdot I_g, \\quad I_{bN} = \\frac{V_{pyr}}{C_{pyr}}$$',
                  'text': '<strong>Pyranometer:</strong> Measures total hemispherical global radiation ($I_g = '
                          'I_b\\cos\\theta_z + I_d$) across $0.3-3.0\\,\\mu\\text{m}$ using a black thermopile with '
                          'dual glass domes.<br><strong>Pyrheliometer:</strong> Measures beam direct normal irradiance '
                          '(DNI) using a narrow collimating tube ($5.7^\\circ$ field of view) mounted on a 2-axis '
                          'solar tracker.'},
    'res-q4': {   'eq': '$$I = I_{ph} - I_0 \\left[ \\exp\\left( \\frac{q (V + I R_s)}{n k T} \\right) - 1 \\right] - '
                        '\\frac{V + I R_s}{R_{sh}}$$',
                  'text': 'Single-diode PV equivalent circuit couples light-generated current $I_{ph}$, dark diode '
                          'recombination current $I_D$, series contact resistance $R_s$, and parallel shunt leakage '
                          'resistance $R_{sh}$. Open-circuit voltage scales logarithmically: $V_{oc} \\approx V_t '
                          '\\cdot n \\ln(I_{sc}/I_0)$.'},
    'res-q5': {   'eq': '$$FF = \\frac{P_{mp}}{V_{oc} I_{sc}} = \\frac{V_{mp} I_{mp}}{V_{oc} I_{sc}}, \\quad \\eta = '
                        '\\frac{P_{mp}}{G \\cdot A} \\times 100\\% = \\frac{V_{oc} I_{sc} FF}{G \\cdot A} \\times '
                        '100\\%$$',
                  'text': '<strong>Fill Factor ($FF$):</strong> Measures the squareness of the I-V curve (typically '
                          '$0.75 - 0.85$).<br><strong>Conversion Efficiency ($\\eta$):</strong> Ratio of maximum '
                          'electrical power $P_{mp}$ to total incident solar optical power $P_{in} = G \\cdot A$.'},
    'res-q6': {   'eq': '$$q_u = F_R A_c [I_t (\\tau\\alpha) - U_L (T_i - T_a)], \\quad \\eta = F_R (\\tau\\alpha) - '
                        'F_R U_L \\left(\\frac{T_i - T_a}{I_t}\\right)$$',
                  'text': '<strong>Hottel-Whillier-Bliss Equation:</strong> Quantifies useful thermal gain $q_u$ of a '
                          'flat-plate collector using heat removal factor $F_R$, optical transmittance-absorptance '
                          'product $(\\tau\\alpha)$, and overall heat loss coefficient $U_L$.'},
    'res-q7': {   'eq': '$$C_R = \\frac{A_a}{A_r}, \\quad PTC: C_R \\approx 15-80, \\quad CR (\\text{Tower}): C_R '
                        '\\approx 500-1500$$',
                  'text': 'Concentrating Solar Power (CSP) reduces heat loss area $A_r$ relative to aperture $A_a$ to '
                          'achieve high operating temperatures.<br><strong>Line Focus:</strong> Parabolic Trough '
                          '($400^\\circ\\text{C}$) & Linear Fresnel ($350^\\circ\\text{C}$).<br><strong>Point '
                          'Focus:</strong> Solar Power Tower ($550-800^\\circ\\text{C}$) with molten salt storage.'},
    'res-q8': {   'eq': '$$P_{dissipated} = |V_{reverse}| \\times I_{string}, \\quad V_{bypass} \\approx -0.7\\text{ '
                        'V}$$',
                  'text': '<strong>Hot-Spot Phenomenon:</strong> Shaded cell in series carries illuminated string '
                          'current, forced into reverse bias and dissipating power as concentrated '
                          'heat.<br><strong>Bypass Diodes:</strong> Placed anti-parallel across cell groups to conduct '
                          'string current when reverse-biased, protecting cells from burn-out.'},
    'res-q9': {   'eq': '$$\\frac{dP}{dV} = 0 \\implies \\frac{dI}{dV} = -\\frac{I}{V} \\quad (\\text{at MPP}), \\quad '
                        '\\frac{dI}{dV} > -\\frac{I}{V} \\ (\\text{Left}), \\quad \\frac{dI}{dV} < -\\frac{I}{V} \\ '
                        '(\\text{Right})$$',
                  'text': '<strong>P&O MPPT:</strong> Perturbs voltage and observes power change; hunts in 3-point '
                          'cycle.<br><strong>Incremental Conductance:</strong> Tracks derivative $\\frac{dI}{dV} + '
                          '\\frac{I}{V} = 0$, halting perturbations at exact peak and eliminating steady-state '
                          'oscillation.'},
    'vcdet-q1': {   'eq': '$$v = y^{-1} \\implies \\frac{dv}{dx} - v = \\sin x - \\cos x \\implies \\frac{1}{y} = C '
                          'e^x - \\sin x$$',
                    'text': '<strong>Bernoulli Equation Transformation:</strong> Dividing by $y^n$ and substituting $v '
                            '= y^{1-n}$ transforms the non-linear Bernoulli ODE into a standard first-order linear ODE '
                            'solvable via integrating factor $e^{\\int P dx}$.'},
    'vcdet-q10': {   'eq': '$$\\nabla(r^n) = n r^{n-2}\\vec{r}, \\quad \\nabla \\cdot (r^n \\vec{r}) = (n+3)r^n, '
                           '\\quad \\nabla^2(r^n) = n(n+1)r^{n-2} \\implies \\nabla^2(r^{-1}) = 0$$',
                     'text': '<strong>Radial Field Vector Identities:</strong> Central fields have radial gradients. '
                             'The Laplacian $\\nabla^2(r^n) = n(n+1)r^{n-2}$ vanishes identically for $n = -1$, '
                             "proving that the Coulomb/Newtonian potential $1/r$ satisfies Laplace\\'s equation."},
    'vcdet-q11': {   'eq': '$$\\oint_C [(x-y)dx + (x+y)dy] = \\iint_R (1 - (-1)) dx\\,dy = 2 \\int_0^1 (\\sqrt{x} - '
                           'x^2)dx = 2\\left(\\frac{1}{3}\\right) = \\frac{2}{3}$$',
                     'text': "<strong>Green\\'s Theorem in a Plane:</strong> Converts a closed line integral $\\oint "
                             '(Mdx + Ndy)$ into a double integral of $(\\partial N/\\partial x - \\partial M/\\partial '
                             'y)$. When the integrand is constant 2, the integral simply equals $2 \\times '
                             '\\text{enclosed area}$.'},
    'vcdet-q12': {   'eq': '$$\\iint_S \\vec{F} \\cdot \\hat{n} \\, dS = \\iiint_V (\\nabla \\cdot \\vec{F}) \\, dV '
                           '\\iff \\Phi_{\\text{net}} = \\iiint (\\text{source density}) \\, dV$$',
                     'text': '<strong>Gauss Divergence Theorem:</strong> Relates outward flux through a closed '
                             'boundary surface to the volumetric accumulation of divergence within the bounded domain; '
                             "underpins Gauss\\'s Law in electromagnetics."},
    'vcdet-q13': {   'eq': '$$\\oint_C = \\int_{C_1} + \\int_{C_2} = \\frac{19}{20} - 1 = -\\frac{1}{20} = \\iint_R (x '
                           '- 2y) dy\\,dx$$',
                     'text': "<strong>Verification of Green\\'s Theorem:</strong> Compute line integral along "
                             'piecewise boundary curves ($C_1: y=x^2, C_2: y=x$) and compare against surface double '
                             'integral of $(N_x - M_y) = x - 2y$; both equal $-1/20$.'},
    'vcdet-q14': {   'eq': '$$\\iiint_V (\\nabla \\cdot \\vec{F}) dV = \\int_0^1 \\int_0^1 (4z - y) dydz = '
                           '\\frac{3}{2} = \\sum_{i=1}^6 \\iint_{S_i} \\vec{F} \\cdot \\hat{n} \\, dS$$',
                     'text': '<strong>Gauss Theorem Verification on Cube:</strong> Evaluate outward normal flux across '
                             'all 6 faces ($\\Phi = 2 + 0 - 1 + 0 + 1/2 + 0 = 3/2$) and confirm identity with volume '
                             'integral of divergence $4z - y = 3/2$.'},
    'vcdet-q15': {   'eq': '$$\\nabla \\times \\vec{F} = \\hat{k} \\implies \\iint_S (\\nabla \\times \\vec{F}) \\cdot '
                           '\\hat{n} \\, dS = \\iint_{x^2+y^2 \\le 1} dx\\,dy = \\pi = \\oint_C \\vec{F} \\cdot '
                           'd\\vec{r}$$',
                     'text': "<strong>Stokes\\' Theorem Verification:</strong> The line integral of $\\vec{F}$ around "
                             'the equator boundary circle equals $\\pi$. The curl simplifies to unit vertical vector '
                             '$\\hat{k}$, whose surface flux projects directly to the equatorial disc area $\\pi$.'},
    'vcdet-q16': {   'eq': '$$S(x_0) = \\begin{cases} f(x_0) & \\text{at points of continuity} \\\\ \\frac{f(x_0^+) + '
                           'f(x_0^-)}{2} & \\text{at points of jump discontinuity} \\end{cases}$$',
                     'text': "<strong>Dirichlet\\'s Conditions & Discontinuity Convergence:</strong> Requires "
                             'boundedness, finite extrema, and finite jump discontinuities. At any step discontinuity, '
                             'the Fourier series converges strictly to the midpoint of the jump.'},
    'vcdet-q17': {   'eq': '$$f(x) = \\frac{4k}{\\pi} \\sum_{n=1,3,5,\\dots}^\\infty \\frac{\\sin nx}{n} = '
                           '\\frac{4k}{\\pi}\\left(\\sin x + \\frac{\\sin 3x}{3} + \\frac{\\sin 5x}{5} + '
                           '\\dots\\right)$$',
                     'text': '<strong>Half-Range Sine Series:</strong> All even harmonic coefficients vanish because '
                             '$1 - (-1)^n = 0$. Odd harmonics decay as $1/n$, generating the classic synthesis of a '
                             'constant step via sinusoidal basis modes.'},
    'vcdet-q18': {   'eq': '$$x^2 = \\frac{\\pi^2}{3} + 4\\sum_{n=1}^\\infty \\frac{(-1)^n}{n^2}\\cos nx \\implies '
                           '\\sum_{n=1}^\\infty \\frac{1}{n^2} = \\frac{\\pi^2}{6}, \\quad \\sum_{n=1}^\\infty '
                           '\\frac{(-1)^{n-1}}{n^2} = \\frac{\\pi^2}{12}$$',
                     'text': '<strong>Fourier Expansion of Parabola:</strong> For even function $x^2$, $b_n = 0, a_n = '
                             '4(-1)^n/n^2$. Evaluating at $x=0$ and $x=\\pi$ resolves the famous Basel problem $\\sum '
                             '1/n^2 = \\pi^2/6$.'},
    'vcdet-q19': {   'eq': '$$f(x) = \\frac{4k}{\\pi} \\sum_{n=1,3,5,\\dots}^\\infty \\frac{\\sin nx}{n} \\implies '
                           '\\text{at } x = \\frac{\\pi}{2}: \\quad 1 - \\frac{1}{3} + \\frac{1}{5} - \\frac{1}{7} + '
                           '\\dots = \\frac{\\pi}{4}$$',
                     'text': '<strong>Square Wave Harmonic Spectrum:</strong> Contains purely odd harmonics with '
                             'harmonic amplitudes decaying inversely as $1/n$. Evaluation at the peak $x = \\pi/2$ '
                             "directly establishes Leibniz\\'s formula for $\\pi$."},
    'vcdet-q2': {   'eq': '$$y = (C_1 + C_2 x) e^{2x} + 4x^2 e^{2x} + \\frac{1}{8}\\cos 2x$$',
                    'text': '<strong>Repeated Roots & Resonant PI:</strong> When auxiliary root $m=a$ is repeated $k$ '
                            'times, complementary function includes $(C_1 + C_2 x)e^{ax}$, and particular integral for '
                            '$e^{ax}$ introduces resonant factor $\\frac{x^k}{k!} e^{ax}$.'},
    'vcdet-q20': {   'eq': '$$\\mathcal{F}_c\\{e^{-ax}\\} = \\frac{a}{a^2 + \\omega^2}, \\quad '
                           '\\mathcal{F}_s\\{e^{-ax}\\} = \\frac{\\omega}{a^2 + \\omega^2} \\implies \\int_0^\\infty '
                           '\\frac{\\cos(\\omega x)}{a^2 + \\omega^2} d\\omega = \\frac{\\pi}{2a}e^{-ax}$$',
                     'text': '<strong>Exponential Fourier Transforms:</strong> Cosine transform yields the Lorentzian '
                             "spectrum $\\frac{a}{a^2 + \\omega^2}$. Applying inverse transform evaluates Laplace\\'s "
                             'famous contour integral $\\frac{\\pi}{2a}e^{-ax}$.'},
    'vcdet-q21': {   'eq': '$$\\mathcal{L}\\{t^2 e^{-3t} \\sin 2t\\} = \\frac{d^2}{ds^2}\\left[\\frac{2}{(s+3)^2 + '
                           '4}\\right] = \\frac{12s^2 + 72s + 92}{(s^2 + 6s + 13)^3}$$',
                     'text': '<strong>Multiplication by $t^n$ & First Shifting:</strong> Applying the first shift '
                             'property replaces $s \\to s + 3$. Differentiating twice with respect to $s$ implements '
                             'multiplication by $t^2$ in the time domain.'},
    'vcdet-q22': {   'eq': '$$\\mathcal{L}^{-1}\\{F(s)G(s)\\} = \\int_0^t f(u)g(t-u)du \\implies '
                           '\\mathcal{L}^{-1}\\left\\{\\frac{1}{s(s^2+1)}\\right\\} = \\int_0^t \\sin(t-u)du = 1 - '
                           '\\cos t$$',
                     'text': '<strong>Convolution Theorem:</strong> Transforms multiplication in the complex '
                             '$s$-frequency domain into a convolution integral in the temporal domain, enabling direct '
                             'calculation without partial fractions.'},
    'vcdet-q23': {   'eq': '$$\\mathcal{L}\\left\\{\\frac{\\cos at - \\cos bt}{t}\\right\\} = '
                           '\\frac{1}{2}\\ln\\left(\\frac{s^2 + b^2}{s^2 + a^2}\\right) \\implies \\int_0^\\infty '
                           '\\frac{\\cos t - \\cos 2t}{t} \\, dt = \\ln 2$$',
                     'text': '<strong>Division by $t$ & Frullani-Type Integrals:</strong> Dividing by $t$ in time '
                             'corresponds to integrating $F(u)$ from $s$ to $\\infty$. Letting $s \\to 0$ computes '
                             'classic improper integrals like $\\int_0^\\infty \\frac{\\cos t - \\cos 2t}{t} dt = \\ln '
                             '2$.'},
    'vcdet-q24': {   'eq': '$$\\mathcal{L}^{-1}\\left\\{\\frac{1}{(s^2+a^2)^2}\\right\\} = \\frac{1}{a^2}\\int_0^t '
                           '\\sin(au)\\sin(a(t-u))du = \\frac{\\sin at - at\\cos at}{2a^3}$$',
                     'text': '<strong>Convolution of Resonant Poles:</strong> Convolving $\\frac{1}{a}\\sin at$ with '
                             'itself generates the secular term $t\\cos at$. The result describes resonance growth in '
                             'undamped harmonic oscillators.'},
    'vcdet-q25': {   'eq': '$$Y(s) = -\\frac{2}{s+2} + \\frac{4}{(s+2)^2} + \\frac{6}{(s+2)^3} \\implies y(t) = (3t^2 '
                           '+ 4t - 2)e^{-2t}$$',
                     'text': '<strong>Initial Value Problem via Laplace Transforms:</strong> Incorporates initial '
                             'conditions automatically into algebraic equations in $s$. The repeated pole $(s+2)^3$ '
                             'yields critical damping response terms $e^{-2t}, te^{-2t}$, and resonant forcing $t^2 '
                             'e^{-2t}$.'},
    'vcdet-q26': {   'eq': '$$X(s) = \\frac{s}{s^2 - 1} \\implies x(t) = \\cosh t; \\quad Y(s) = \\frac{1}{s^2 + 1} - '
                           '\\frac{1}{s^2 - 1} \\implies y(t) = \\sin t - \\sinh t$$',
                     'text': '<strong>Simultaneous Differential Systems:</strong> Coupled time-domain differential '
                             'equations transform into a system of linear algebraic equations in $X(s)$ and $Y(s)$. '
                             'Elimination reveals hyperbolic decoupling modes $\\cosh t$ and $\\sin t - \\sinh t$.'},
    'vcdet-q3': {   'eq': '$$W = 1, \\; u(x) = x - \\tan x, \\; v(x) = \\ln|\\sec x| \\implies y = C_1 \\cos x + C_2 '
                          '\\sin x + x \\cos x + \\sin x \\ln|\\sec x|$$',
                    'text': "<strong>Variation of Parameters:</strong> For $y\\'\\' + y = R(x)$, basis solutions are "
                            '$y_1 = \\cos x, y_2 = \\sin x$ with Wronskian $W = 1$. The formulas $u = -\\int y_2 R / W '
                            '\\, dx$ and $v = \\int y_1 R / W \\, dx$ yield particular integrals for any '
                            'non-elementary excitation.'},
    'vcdet-q4': {   'eq': '$$[D_z(D_z-1) - 3D_z + 4]y = 2e^{2z} \\implies y(x) = x^2 [C_1 + C_2 \\ln x + (\\ln x)^2]$$',
                    'text': '<strong>Cauchy-Euler Reduction:</strong> Setting $x = e^z$ converts variable-coefficient '
                            'Cauchy-Euler equations into constant-coefficient ODEs in $z$, where $x^k \\frac{d^k '
                            'y}{dx^k} = D_z(D_z - 1)\\dots(D_z - k + 1)y$.'},
    'vcdet-q5': {   'eq': '$$y_p = e^x \\frac{1}{D^2}[x \\sin x] = -e^x(x\\sin x + 2\\cos x) \\implies y = (C_1 + C_2 '
                          'x)e^x - e^x(x\\sin x + 2\\cos x)$$',
                    'text': '<strong>Exponential Shift Theorem:</strong> Shifting $e^{ax}$ outside the differential '
                            'operator via $f(D)[e^{ax} V] = e^{ax} f(D+a)V$ eliminates the exponential factor and '
                            'reduces operator power.'},
    'vcdet-q6': {   'eq': '$$\\nabla \\phi = 8\\hat{i} - \\hat{j} - 10\\hat{k}, \\quad \\hat{u} = \\frac{2\\hat{i} - '
                          '\\hat{j} - 2\\hat{k}}{3} \\implies D_{\\hat{u}}\\phi = \\nabla\\phi \\cdot \\hat{u} = '
                          '\\frac{37}{3}$$',
                    'text': '<strong>Directional Derivative:</strong> Represents the rate of change of a scalar field '
                            '$\\phi$ along a unit direction $\\hat{u}$. Maximum rate of increase occurs along '
                            '$\\nabla\\phi$ with magnitude $\\|\\nabla\\phi\\|$.'},
    'vcdet-q7': {   'eq': '$$\\hat{n} = \\frac{\\nabla f}{|\\nabla f|} = \\frac{\\hat{i} + \\hat{j} + '
                          '2\\hat{k}}{\\sqrt{6}}, \\quad \\text{Tangent Plane: } x + y + 2z = 4$$',
                    'text': '<strong>Unit Normal & Tangent Plane:</strong> Gradient $\\nabla f$ at any point on the '
                            'level surface $f(x,y,z) = c$ defines the orthogonal surface normal. The tangent plane '
                            'equation is $\\nabla f \\cdot (\\vec{r} - \\vec{r}_0) = 0$.'},
    'vcdet-q8': {   'eq': '$$\\nabla \\times \\vec{F} = \\vec{0} \\implies \\phi = x^2 y + x z^3, \\quad W = \\phi(3, '
                          '1, 4) - \\phi(1, -2, 1) = 201 - (-1) = 202$$',
                    'text': '<strong>Conservative Field & Potential:</strong> An irrotational field ($\\nabla \\times '
                            '\\vec{F} = 0$) possesses a scalar potential $\\vec{F} = \\nabla\\phi$. Line integrals are '
                            'path-independent, reducing work done simply to $\\phi(\\text{end}) - '
                            '\\phi(\\text{start})$.'},
    'vcdet-q9': {   'eq': '$$\\nabla \\times \\vec{F} = \\vec{0} \\implies a = 4, \\; b = 2, \\; c = -1; \\quad '
                          '\\nabla \\cdot \\vec{F} = 1 - 3 + 2 = 0 \\text{ (Solenoidal for all } a,b,c \\text{)}$$',
                    'text': '<strong>Irrotational and Solenoidal Fields:</strong> $\\vec{F}$ is irrotational if '
                            '$\\nabla \\times \\vec{F} = \\vec{0}$ (symmetric Jacobian). $\\vec{F}$ is solenoidal if '
                            '$\\nabla \\cdot \\vec{F} = 0$ (divergence-free, zero net flux expansion).'}}

def get_byheart_card_html(qid, marks=3):
    # Check if a lecturer answer with refined remember_this exists
    try:
        from lecturer_answers import REPRESENTATIVE_ANSWERS
        rep = REPRESENTATIVE_ANSWERS.get(qid)
        if rep and rep.get("remember_this"):
            rem = rep["remember_this"]
            title = rem.get("title", "Key Equation" if rem.get("eq") else "Remember This")
            icon = "⚡" if "Equation" in title else "📌"
            eq_html = f'<div class="byheart-eq">{rem["eq"]}</div>' if rem.get("eq") else ""
            time_badge = '<span class="byheart-time-badge">⏱️ 5 Mins Writing Time</span>' if marks == 3 else '<span class="byheart-time-badge">⏱️ 12 Mins Writing Time</span>'
            text_html = f'<p class="byheart-text">{rem["text"]}</p>' if rem.get("text") else ""
            return f"""
            <div class="byheart-card">
                <div class="byheart-header">
                    <div class="byheart-title-group">
                        <span class="byheart-icon">{icon}</span>
                        <span class="byheart-title">{title}</span>
                    </div>
                    <div class="byheart-badges-group">
                        {time_badge}
                        <span class="byheart-badge">⭐ High Mark Weightage</span>
                    </div>
                </div>
                <div class="byheart-body">
                    {eq_html}
                    {text_html}
                </div>
            </div>"""
    except Exception:
        pass

    item = BYHEART_DATA.get(qid)
    if not item:
        return ""
    has_eq = bool(item.get("eq"))
    title = "Key Equation" if has_eq else "Remember This"
    icon = "⚡" if has_eq else "📌"
    eq_html = f'<div class="byheart-eq">{item["eq"]}</div>' if has_eq else ""
    time_badge = '<span class="byheart-time-badge">⏱️ 5 Mins Writing Time</span>' if marks == 3 else '<span class="byheart-time-badge">⏱️ 12 Mins Writing Time</span>'
    return f"""
            <div class="byheart-card">
                <div class="byheart-header">
                    <div class="byheart-title-group">
                        <span class="byheart-icon">{icon}</span>
                        <span class="byheart-title">{title}</span>
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
