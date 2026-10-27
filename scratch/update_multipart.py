# scratch/update_multipart.py
import sys
sys.path.append('scratch')
import byheart_data

updates = {
    'acs-q1': {
        'eq': r"""$$\dot{\mathbf{x}}(t) = A \mathbf{x}(t) + B \mathbf{u}(t), \quad \mathbf{y}(t) = C \mathbf{x}(t) + D \mathbf{u}(t), \quad \mathbf{x}(t) \in \mathbb{R}^n$$""",
        'text': (
            r'<strong>(i) State:</strong> The minimal set of variables $x_1(t), \dots, x_n(t)$ whose values at $t_0$, together with input $u(t)$ for $t \ge t_0$, uniquely determine the system state and output for all future time $t > t_0$.<br>'
            r'<strong>(ii) State Variables:</strong> The smallest set of linearly independent variables $\{x_i(t)\}$ representing dynamic energy storage states (inductor currents, capacitor voltages, position, velocity).<br>'
            r'<strong>(iii) State Vector:</strong> Column vector $\mathbf{x}(t) = [x_1(t), x_2(t), \dots, x_n(t)]^T \in \mathbb{R}^n$ grouping all $n$ state variables.<br>'
            r'<strong>(iv) State Space:</strong> The $n$-dimensional Euclidean vector space $\mathbb{R}^n$ whose orthogonal coordinate axes are formed by the state variables $x_1, x_2, \dots, x_n$.'
        )
    },
    'acs-q2': {
        'eq': r"""$$x_1 = y, \; x_2 = \dot{y}, \; \dots, \; x_n = y^{(n-1)} \implies \dot{x}_n = -\sum_{i=0}^{n-1} a_i x_{i+1} + b_0 u$$""",
        'text': (
            r'<strong>Phase Variables Definition:</strong> State variables defined as the output variable and its successive $(n-1)$ time derivatives ($x_1=y, x_2=\dot{y}, \dots, x_n=y^{(n-1)}$).<br>'
            r'<strong>Companion Form:</strong> Produces companion matrix $A$ having 1s along the first super-diagonal and negated differential equation coefficients $[-a_0, -a_1, \dots, -a_{n-1}]$ along the bottom row.'
        )
    },
    'acs-q3': {
        'eq': r"""$$\dot{x}(t) = A x(t) + B u(t), \quad y(t) = C x(t) + D u(t)$$""",
        'text': (
            r'<strong>Integrators:</strong> State variables $x_i(t)$ are strictly the physical outputs of integrators ($1/s$), driven by derivative inputs $\dot{x}_i(t)$.<br>'
            r'<strong>Matrix Functions:</strong> Matrix $A$ ($n\times n$) provides internal state feedback, $B$ ($n\times m$) distributes external inputs, $C$ ($p\times n$) observes states to outputs, and $D$ ($p\times m$) provides direct feedthrough.'
        )
    },
    'acs-q4': {
        'eq': r"""$$\bar{A} = P^{-1} A P, \quad \bar{B} = P^{-1} B, \quad \bar{C} = C P, \quad \bar{D} = D \implies \det(sI - \bar{A}) = \det(sI - A)$$""",
        'text': (
            r'<strong>Non-Uniqueness:</strong> Any non-singular similarity transformation $x = P z$ creates an equivalent valid state space representation.<br>'
            r'<strong>System Invariants:</strong> System eigenvalues (roots of $\det(sI-A)=0$) and the transfer function $G(s) = C(sI-A)^{-1}B + D$ remain strictly invariant under coordinate transformations.'
        )
    },
    'acs-q9': {
        'eq': r"""$$\Phi(t) = e^{At} = \mathcal{L}^{-1}\{(sI - A)^{-1}\} = \sum_{k=0}^{\infty} \frac{A^k t^k}{k!}$$""",
        'text': (
            r'<strong>Key Properties of State Transition Matrix:</strong><br>'
            r'<strong>1. Identity:</strong> $\Phi(0) = e^0 = I$<br>'
            r'<strong>2. Inverse / Time Reversal:</strong> $\Phi^{-1}(t) = \Phi(-t)$<br>'
            r'<strong>3. Group Property:</strong> $\Phi(t_1 + t_2) = \Phi(t_1)\Phi(t_2)$<br>'
            r'<strong>4. Power Property:</strong> $[\Phi(t)]^k = \Phi(kt)$<br>'
            r'<strong>5. Derivative:</strong> $\dot{\Phi}(t) = A \Phi(t) = \Phi(t) A$'
        )
    },
    'acs-q16': {
        'eq': r"""$$f(x_1 + x_2) \ne f(x_1) + f(x_2), \quad f(\alpha x) \ne \alpha f(x) \implies \text{Superposition Principle Fails}$$""",
        'text': (
            r'<strong>Distinct Non-Linear Physical Phenomena:</strong><br>'
            r'<strong>1. Limit Cycles:</strong> Isolated, self-sustained closed periodic orbits in state space (stable or unstable).<br>'
            r'<strong>2. Jump Resonance:</strong> Discontinuous jump in amplitude and phase during continuous sinusoidal frequency sweeps.<br>'
            r'<strong>3. Subharmonics:</strong> Generation of steady output responses at integer fractions ($f/2, f/3$) of input frequency.<br>'
            r'<strong>4. Amplitude-Dependent Stability:</strong> System stability depends on initial state or excitation amplitude, unlike linear systems.'
        )
    },
    'acs-q16b': {
        'eq': r"""$$N(X)_{\text{ideal}} = \frac{4M}{\pi X}, \qquad N(X)_{\text{deadzone}} = \frac{4M}{\pi X} \sqrt{1 - \left(\frac{D}{X}\right)^2} \quad (X > D)$$""",
        'text': (
            r'<strong>1. Ideal Relay:</strong> Output switches between $+M$ and $-M$; describing function $N(X) = \frac{4M}{\pi X}$ is pure real with zero phase shift ($\angle N(X) = 0^\circ$).<br>'
            r'<strong>2. Relay with Dead-Zone ($D$):</strong> Output is zero for input amplitude $X \le D$; for $X > D$, effective gain drops as amplitude increases with zero phase shift.'
        )
    },
    'acs-q19': {
        'eq': r"""$$\frac{dx_2}{dx_1} = \frac{f_2(x_1, x_2)}{f_1(x_1, x_2)} = \frac{0}{0} \quad \text{at equilibrium point } (x_1^*, x_2^*)$$""",
        'text': (
            r'<strong>Classification of Singular Points by Linearized Eigenvalues:</strong><br>'
            r'<strong>1. Stable / Unstable Node:</strong> Real eigenvalues of same sign ($\lambda_1, \lambda_2 \in \mathbb{R}, \lambda_1\lambda_2 > 0$).<br>'
            r'<strong>2. Saddle Point:</strong> Real eigenvalues of opposite sign ($\lambda_1 > 0, \lambda_2 < 0$) &mdash; <em>always unstable</em>!<br>'
            r'<strong>3. Stable / Unstable Focus:</strong> Complex conjugate eigenvalues with real part ($\sigma \pm j\omega, \sigma \ne 0$).<br>'
            r'<strong>4. Center (Vortex):</strong> Purely imaginary conjugate eigenvalues ($\pm j\omega, \sigma = 0$) &mdash; closed concentric periodic orbits.'
        )
    },
    'acs-q20': {
        'eq': r"""$$V(x) = x^T P x > 0 \quad (\forall x \ne 0) \iff \Delta_1 > 0, \; \Delta_2 > 0, \; \dots, \; \Delta_n > 0$$""",
        'text': (
            r'<strong>Sylvester Criterion for Positive Definiteness:</strong> A real symmetric matrix $P = P^T$ is positive definite if and only if all $n$ leading principal minors $\Delta_k = \det(P_{k\times k})$ are strictly positive ($\Delta_1 > 0, \Delta_2 > 0, \dots, \Delta_n > 0$).<br>'
            r'<strong>Negative Definite:</strong> If and only if leading principal minors alternate signs starting negative ($\Delta_1 < 0, \Delta_2 > 0, \Delta_3 < 0, \dots$).'
        )
    },
    'drive-q1': {
        'eq': r"""$$\text{Source} \longrightarrow \text{Power Modulator} \longrightarrow \text{Electric Motor} \longrightarrow \text{Load} \quad (\text{Closed-Loop Control})$$""",
        'text': (
            r'<strong>Constituent Elements of an Electric Drive:</strong><br>'
            r'<strong>1. Power Source:</strong> 1-phase/3-phase AC utility grid or DC source/battery.<br>'
            r'<strong>2. Power Modulator:</strong> Regulates energy flow via converters/inverters (rectifiers, choppers, VSIs, cycloconverters).<br>'
            r'<strong>3. Electric Motor:</strong> Converts modulated electrical energy to controlled mechanical torque (DC, Induction, BLDC, Synchronous).<br>'
            r'<strong>4. Control & Sensing Unit:</strong> Measures current/speed/position and generates switching signals to enforce precision motion.'
        )
    },
    'drive-q3': {
        'eq': r"""$$T_L = T_{L0} + C \left(\frac{\omega}{\omega_n}\right)^k, \quad k=0 \text{ (Hoist)}, \; k=1 \text{ (Calender)}, \; k=2 \text{ (Fan/Pump)}, \; k=-1 \text{ (Lathe)}$$""",
        'text': (
            r'<strong>Classification of Industrial Load Torques:</strong><br>'
            r'<strong>1. Active Load Torques:</strong> Torques that retain their sign/direction irrespective of rotation direction (e.g., gravitational torque in hoists $k=0$, tension in coilers).<br>'
            r'<strong>2. Passive Load Torques:</strong> Torques that always oppose motion (dry coulomb friction $k=0$, viscous friction $k=1$, centrifugal fans/pumps $T_L \propto \omega^2$ with $k=2$, constant power machine tools $T_L \propto 1/\omega$ with $k=-1$).'
        )
    },
    'drive-q5': {
        'eq': r"""$$P_m = T \cdot \omega_m \implies \begin{cases} \text{Q1: Forward Motoring } (+T, +\omega, P>0) & \text{Q2: Forward Braking } (-T, +\omega, P<0) \\ \text{Q3: Reverse Motoring } (-T, -\omega, P>0) & \text{Q4: Reverse Braking } (+T, -\omega, P<0) \end{cases}$$""",
        'text': (
            r'<strong>Four-Quadrant Operation of Hoist Drive:</strong><br>'
            r'<strong>Quadrant 1 (Forward Motoring):</strong> $+T, +\omega_m$ &mdash; Hoisting a loaded cage upward against gravity ($P_m > 0$).<br>'
            r'<strong>Quadrant 2 (Forward Braking):</strong> $-T, +\omega_m$ &mdash; Decelerating upward motion via regenerative braking ($P_m < 0$).<br>'
            r'<strong>Quadrant 3 (Reverse Motoring):</strong> $-T, -\omega_m$ &mdash; Driving an empty cage downward against friction ($P_m > 0$).<br>'
            r'<strong>Quadrant 4 (Reverse Braking):</strong> $+T, -\omega_m$ &mdash; Safely lowering a loaded cage under gravity with braking counter-torque ($P_m < 0$).'
        )
    },
    'drive-q7': {
        'eq': r"""$$\omega_m = \frac{V_a - I_a R_a}{K \phi} \implies \begin{cases} \text{Below Base Speed: } V_a \text{ variation at rated } \phi \implies \text{Constant Torque Mode} \\ \text{Above Base Speed: } \phi \text{ reduction at rated } V_a \implies \text{Constant Power Mode} \end{cases}$$""",
        'text': (
            r'<strong>1. Armature Voltage Control (Below Base Speed):</strong> Variable $V_a$ with full rated flux $\phi$ provides <strong>Constant Torque</strong> ($T_{\max} = K \phi I_{a,\text{rated}}$), where power increases linearly with speed ($P \propto \omega$).<br>'
            r'<strong>2. Field Weakening Control (Above Base Speed):</strong> Rated $V_a$ with reduced field flux $\phi$ provides <strong>Constant Power</strong> ($P = V_a I_a = \text{constant}$), where developed torque decreases inversely with speed ($T \propto 1/\omega$).'
        )
    },
    'mobile-q11': {
        'eq': r"""$$\text{IMEI (15-digit Handset ID)} \quad | \quad \text{IMSI (15-digit SIM ID)} \quad | \quad \text{MSISDN (Public Number)} \quad | \quad \text{TMSI (Temporary Air ID)}$$""",
        'text': (
            r'<strong>Mobile Station Identifiers:</strong><br>'
            r'<strong>1. IMEI:</strong> 15-digit hardware serial number uniquely identifying the physical mobile terminal hardware (TAC + FAC + SNR + Spare).<br>'
            r'<strong>2. IMSI:</strong> 15-digit subscriber identity stored in SIM and HLR/AUC (MCC + MNC + MSIN).<br>'
            r'<strong>3. MSISDN:</strong> Dialable public telephone number routed via PSTN (CC + NDC + SN).<br>'
            r'<strong>4. TMSI:</strong> Temporary identity assigned by VLR to prevent eavesdropping and protect subscriber anonymity over the air interface.'
        )
    },
    'mobile-q17': {
        'eq': r"""$$\text{Authentication: } \text{SRES} = A3(K_i, \text{RAND}), \quad \text{Key Gen: } K_c = A8(K_i, \text{RAND}), \quad \text{Encryption: } \text{Data} \oplus A5(K_c)$$""",
        'text': (
            r'<strong>GSM Security Triad Algorithms:</strong><br>'
            r'<strong>1. A3 Algorithm (Authentication):</strong> SIM computes 32-bit $\text{SRES}$ from 128-bit challenge $\text{RAND}$ and secret key $K_i$; network authenticates if $\text{SRES}$ matches AUC.<br>'
            r'<strong>2. A8 Algorithm (Ciphering Key Generation):</strong> Computes 64-bit session key $K_c$ on SIM from $\text{RAND}$ and $K_i$ ($K_i$ never transmitted over radio).<br>'
            r'<strong>3. A5 Algorithm (Air Encryption):</strong> Hardware stream cipher that encrypts/decrypts TDMA radio bursts using $K_c$ and frame number.'
        )
    },
    'mobile-q25': {
        'eq': r"""$$\text{Priority Hierarchy: } \text{SIFS} < \text{PIFS} < \text{DIFS} < \text{EIFS} \implies \text{Shorter waiting interval guarantees higher channel access priority}$$""",
        'text': (
            r'<strong>IEEE 802.11 Interframe Spaces (IFS):</strong><br>'
            r'<strong>1. SIFS (Shortest, 10 &mu;s):</strong> Highest priority for immediate response frames: ACK, CTS, and fragmented frames.<br>'
            r'<strong>2. PIFS (PCF IFS):</strong> Medium priority used exclusively by Access Point in Point Coordination Function for contention-free polling.<br>'
            r'<strong>3. DIFS (DCF IFS):</strong> Standard interval contending stations must wait after channel idle before initiating backoff counter in CSMA/CA.<br>'
            r'<strong>4. EIFS (Extended IFS):</strong> Longest waiting period applied whenever an invalid or corrupted packet frame is received.'
        )
    },
    'mobile-q31': {
        'eq': r"""$$\text{Security Pillars: Confidentiality (AES/RSA), Integrity (SHA-256/HMAC), Availability (DDoS Defense), Auth \& Non-Repudiation (DSA)}$$""",
        'text': (
            r'<strong>Foundational Information Security Pillars:</strong><br>'
            r'<strong>1. Confidentiality:</strong> Ensures sensitive transmitted data is unreadable to eavesdroppers via encryption.<br>'
            r'<strong>2. Integrity:</strong> Guarantees that data packets are not tampered with, altered, or injected in transit using cryptographic hash functions (SHA/HMAC).<br>'
            r'<strong>3. Availability:</strong> Assures that network services and spectrum remain accessible to legitimate users under peak load or attacks.<br>'
            r'<strong>4. Authenticity & Non-Repudiation:</strong> Verifies genuine claimant identity and prevents sender from denying authorship via digital signatures.'
        )
    }
}

for qid, data in updates.items():
    if qid in byheart_data.BYHEART_DATA:
        byheart_data.BYHEART_DATA[qid]['eq'] = data['eq']
        byheart_data.BYHEART_DATA[qid]['text'] = data['text']

with open('scratch/byheart_data.py', 'w', encoding='utf-8') as f:
    f.write('# scratch/byheart_data.py\n# High mark-weightage equations and core memorization sentences for all 94 exam questions.\n# Heading: Sentence / (Equation) to Byhart\n\nBYHEART_DATA = {\n')
    keys = list(byheart_data.BYHEART_DATA.keys())
    for i, k in enumerate(keys):
        item = byheart_data.BYHEART_DATA[k]
        comma = ',' if i < len(keys) - 1 else ''
        f.write(f'    {repr(k)}: {{\n        "eq": r{repr(item["eq"])},\n        "text": r{repr(item["text"])}\n    }}{comma}\n')
    f.write('''}\n\ndef get_byheart_card_html(qid, marks=3):\n    item = BYHEART_DATA.get(qid)\n    if not item:\n        return ""\n    eq_html = f'<div class="byheart-eq">{item["eq"]}</div>' if item.get("eq") else ""\n    time_badge = '<span class="byheart-time-badge">⏱️ 5 Mins Writing Time</span>' if marks == 3 else '<span class="byheart-time-badge">⏱️ 12 Mins Writing Time</span>'\n    return f"""\n            <div class="byheart-card">\n                <div class="byheart-header">\n                    <div class="byheart-title-group">\n                        <span class="byheart-icon">⚡</span>\n                        <span class="byheart-title">Sentence / (Equation) to Byhart</span>\n                    </div>\n                    <div class="byheart-badges-group">\n                        {time_badge}\n                        <span class="byheart-badge">⭐ High Mark Weightage</span>\n                    </div>\n                </div>\n                <div class="byheart-body">\n                    {eq_html}\n                    <p class="byheart-text">{item['text']}</p>\n                </div>\n            </div>"""\n''')

print('Successfully updated scratch/byheart_data.py with comprehensive multi-part exam answers!')
