# -*- coding: utf-8 -*-
"""
Module 3 for Power System II (EET304)
Power Flow Analysis
"""

M3_QUESTIONS = [
    {
        "qid": "ps2-q11",
        "marks": 3,
        "type": "Short Answer",
        "title": "Power Flow Bus Classification and Formulation of Bus Admittance Matrix (Y_bus)",
        "yt_query": "bus classification load flow slack PV PQ bus Y bus formulation inspection method",
        "img_path": "images/ps2/bus_classification_types.png",
        "img_caption": "Figure 3.1: Power Flow Bus Types and Network Representation for Y_bus Construction",
        "answer": r"""
In power system engineering, power flow (load flow) analysis computes the steady-state operating state of a transmission network under specified generation and loading schedules. At each bus $i$ in an $n$-bus system, four fundamental electrical variables are defined:
1. Real power injection: $P_i = P_{Gi} - P_{Di}$
2. Reactive power injection: $Q_i = Q_{Gi} - Q_{Di}$
3. Voltage magnitude: $|V_i|$
4. Voltage phase angle: $\delta_i$

Because only two independent algebraic equations (real and reactive power balance) can be formulated at each node, exactly two of these four variables must be specified a priori, leaving the remaining two to be calculated. Based on this specification, buses are categorized into three distinct classes:

1. Slack / Swing / Reference Bus (Usually Bus 1):
- Specified (Known) Variables: Voltage magnitude $|V_1|$ (typically set to $1.0 \text{ pu}$) and voltage phase angle $\delta_1 = 0^\circ$ (acting as the system angular reference).
- Unknown (Calculated) Variables: Active power $P_1$ and reactive power $Q_1$.
- Physical Role: Because total transmission grid losses ($P_{loss}$) cannot be known until all bus voltages and line currents are computed, the slack bus generator supplies or absorbs the residual active and reactive power necessary to maintain overall power balance ($\sum P_G = \sum P_D + P_{loss}$).

2. Generator / Voltage-Controlled / PV Bus:
- Specified (Known) Variables: Real power generation $P_i$ and terminal voltage magnitude $|V_i|$ (held constant by the automatic voltage regulator excitation system).
- Unknown (Calculated) Variables: Reactive power generation $Q_i$ and voltage phase angle $\delta_i$.
- Reactive Limits: The excitation system has physical thermal boundaries: $Q_{i,min} \le Q_i \le Q_{i,max}$. If the calculated $Q_i$ violates these limits during iteration, the generator can no longer regulate voltage; $|V_i|$ is released, and the bus is converted into a PQ bus.

3. Load / PQ Bus:
- Specified (Known) Variables: Net real power $P_i$ and reactive power $Q_i$ demanded by the consumer load.
- Unknown (Calculated) Variables: Voltage magnitude $|V_i|$ and phase angle $\delta_i$.

Formulation of the Bus Admittance Matrix ($Y_{bus}$):
The relationship between injected nodal currents and bus voltages is governed by:
$$I_{bus} = Y_{bus} V_{bus}$$
In an $n$-bus network, $Y_{bus}$ is an $n \times n$ complex symmetric matrix synthesized by the direct Inspection Method:
1. Diagonal Elements (Self Admittances $Y_{ii}$):
The diagonal element $Y_{ii}$ is equal to the algebraic sum of all admittances connected directly to bus $i$, including line charging susceptances and shunt capacitor/reactor elements connected from bus $i$ to ground:
$$Y_{ii} = \sum_{k=1, k\ne i}^n y_{ik} + y_{i0}$$
where $y_{ik} = \frac{1}{R_{ik} + j X_{ik}}$ is the series admittance of the branch between buses $i$ and $k$, and $y_{i0} = j \frac{B_{ik}'}{2} + y_{shunt, i}$ is the total shunt admittance at bus $i$.
2. Off-Diagonal Elements (Mutual Admittances $Y_{ik}$):
The off-diagonal element $Y_{ik}$ equals the negative of the total series branch admittance connected directly between bus $i$ and bus $k$:
$$Y_{ik} = Y_{ki} = -y_{ik} = -\frac{1}{Z_{ik}}$$
If no direct transmission line connects bus $i$ and bus $k$, $Y_{ik} = 0$.

Because typical power grids are sparsely connected (a substation connects to only 2 to 4 adjacent stations), $Y_{bus}$ is extremely sparse with over 90% zero entries, enabling highly efficient sparse-matrix storage and computation.
"""
    },
    {
        "qid": "ps2-q12",
        "marks": 7,
        "type": "Long Derivation",
        "title": "Derivation of Static Power Flow Equations in Polar Coordinates",
        "yt_query": "static power flow equations derivation polar coordinates real reactive power injection",
        "img_path": "images/ps2/static_power_flow_derivation.png",
        "img_caption": "Figure 3.2: Nodal Power Injection Diagram for Power Flow Derivation",
        "answer": r"""
To establish the fundamental mathematical framework for numerical load flow algorithms, we derive the non-linear algebraic static power flow equations governing active and reactive power balance at each bus.

Consider an $n$-bus electrical power transmission system. Let:
- $V_i = |V_i| \angle \delta_i = |V_i| e^{j \delta_i}$ represent the complex phasor voltage at bus $i$.
- $I_i$ represent the net complex current injected into the network at bus $i$.
- $Y_{ik} = |Y_{ik}| \angle \theta_{ik} = |Y_{ik}| e^{j \theta_{ik}} = G_{ik} + j B_{ik}$ represent the $(i, k)$-th entry of the bus admittance matrix $Y_{bus}$, where $G_{ik}$ is conductance and $B_{ik}$ is susceptance.

Applying Kirchhoff's Current Law (KCL) at bus $i$, the total injected current equals the sum of currents leaving bus $i$ to all other connected buses $k = 1, 2, \dots, n$:
$$I_i = \sum_{k=1}^n Y_{ik} V_k$$

The net complex power $S_i$ injected into bus $i$ is defined by the phasor relation:
$$S_i = P_i + j Q_i = V_i I_i^*$$
where $P_i$ is net real power ($P_{Gi} - P_{Di}$), $Q_i$ is net reactive power ($Q_{Gi} - Q_{Di}$), and $I_i^*$ is the complex conjugate of the injected current phasor.
Taking the complex conjugate on both sides of the power equation:
$$S_i^* = P_i - j Q_i = V_i^* I_i$$
Substituting the KCL current summation into this expression:
$$P_i - j Q_i = V_i^* \sum_{k=1}^n Y_{ik} V_k = \sum_{k=1}^n V_i^* Y_{ik} V_k$$

Substituting the polar forms $V_i^* = |V_i| e^{-j \delta_i}$, $Y_{ik} = |Y_{ik}| e^{j \theta_{ik}}$, and $V_k = |V_k| e^{j \delta_k}$:
$$P_i - j Q_i = \sum_{k=1}^n \left( |V_i| e^{-j \delta_i} \right) \left( |Y_{ik}| e^{j \theta_{ik}} \right) \left( |V_k| e^{j \delta_k} \right)$$
Combining the exponential terms:
$$P_i - j Q_i = \sum_{k=1}^n |V_i| |V_k| |Y_{ik}| e^{j (\theta_{ik} + \delta_k - \delta_i)}$$

Applying Euler's identity $e^{j\phi} = \cos\phi + j\sin\phi$:
$$P_i - j Q_i = \sum_{k=1}^n |V_i| |V_k| |Y_{ik}| \left[ \cos(\theta_{ik} + \delta_k - \delta_i) + j \sin(\theta_{ik} + \delta_k - \delta_i) \right]$$

Equating real parts on both sides yields the Static Real Power Flow Equation:
$$P_i = \sum_{k=1}^n |V_i| |V_k| |Y_{ik}| \cos(\theta_{ik} + \delta_k - \delta_i)$$

Equating imaginary parts on both sides (noting the negative sign in $-j Q_i$):
$$-Q_i = \sum_{k=1}^n |V_i| |V_k| |Y_{ik}| \sin(\theta_{ik} + \delta_k - \delta_i)$$
Multiplying by $-1$ yields the Static Reactive Power Flow Equation:
$$Q_i = -\sum_{k=1}^n |V_i| |V_k| |Y_{ik}| \sin(\theta_{ik} + \delta_k - \delta_i)$$

Alternative Rectangular Formulation using Conductance ($G_{ik}$) and Susceptance ($B_{ik}$):
Using the trigonometric angle addition formula on $\theta_{ik} - (\delta_i - \delta_k)$:
$$\cos(\theta_{ik} - \delta_i + \delta_k) = \cos\theta_{ik} \cos(\delta_i - \delta_k) + \sin\theta_{ik} \sin(\delta_i - \delta_k)$$
Since $G_{ik} = |Y_{ik}|\cos\theta_{ik}$ and $B_{ik} = |Y_{ik}|\sin\theta_{ik}$:
$$P_i = |V_i| \sum_{k=1}^n |V_k| \left[ G_{ik} \cos(\delta_i - \delta_k) + B_{ik} \sin(\delta_i - \delta_k) \right]$$
$$Q_i = |V_i| \sum_{k=1}^n |V_k| \left[ G_{ik} \sin(\delta_i - \delta_k) - B_{ik} \cos(\delta_i - \delta_k) \right]$$

Power Mismatches:
During iterative numerical solution, the calculated injections $P_i^{calc}$ and $Q_i^{calc}$ evaluated at iteration $(m)$ are compared against specified scheduled values to form power mismatches:
$$\Delta P_i^{(m)} = P_i^{sch} - P_i^{calc,(m)}$$
$$\Delta Q_i^{(m)} = Q_i^{sch} - Q_i^{calc,(m)}$$
Convergence is achieved when all mismatches satisfy $|\Delta P_i| \le \epsilon$ and $|\Delta Q_i| \le \epsilon$ across all non-slack buses.
"""
    },
    {
        "qid": "ps2-q13",
        "marks": 7,
        "type": "Long Derivation",
        "title": "Gauss-Seidel Power Flow Algorithm: Formulation, Acceleration, and PV Bus Handling",
        "yt_query": "gauss seidel load flow algorithm acceleration factor PV bus handling reactive limits",
        "img_path": "images/ps2/gauss_seidel_flowchart.png",
        "img_caption": "Figure 3.3: Algorithmic Flowchart of Gauss-Seidel Method with Q-Limit Checking on PV Buses",
        "answer": r"""
The Gauss-Seidel method is an iterative numerical technique for solving large sets of non-linear algebraic equations. In power flow studies, its primary advantages are computational simplicity, low computer memory requirements, and straightforward programming.

Derivation of the Iterative Voltage Equation:
From the complex power injection equation at bus $i$:
$$S_i^* = P_i - j Q_i = V_i^* I_i \implies I_i = \frac{P_i - j Q_i}{V_i^*}$$
Expressing injected current using the bus admittance matrix:
$$I_i = \sum_{k=1}^n Y_{ik} V_k = Y_{ii} V_i + \sum_{k=1, k\ne i}^n Y_{ik} V_k$$
Equating both expressions for $I_i$:
$$Y_{ii} V_i + \sum_{k=1, k\ne i}^n Y_{ik} V_k = \frac{P_i - j Q_i}{V_i^*}$$
Isolating the bus voltage $V_i$:
$$Y_{ii} V_i = \frac{P_i - j Q_i}{V_i^*} - \sum_{k=1, k\ne i}^n Y_{ik} V_k$$
$$V_i = \frac{1}{Y_{ii}} \left[ \frac{P_i - j Q_i}{V_i^*} - \sum_{k=1, k\ne i}^n Y_{ik} V_k \right]$$

In the Gauss-Seidel scheme, newly computed voltage values are immediately substituted as soon as they become available within the same iteration cycle. When updating bus $i$ during the $(m+1)$-th iteration, the voltages for buses $k = 1$ to $(i - 1)$ have already been updated to iteration $(m+1)$, whereas voltages for buses $k = (i + 1)$ to $n$ remain at iteration $(m)$:
$$V_i^{(m+1)} = \frac{1}{Y_{ii}} \left[ \frac{P_i^{sch} - j Q_i^{sch}}{\left(V_i^{(m)}\right)^*} - \sum_{k=1}^{i-1} Y_{ik} V_k^{(m+1)} - \sum_{k=i+1}^n Y_{ik} V_k^{(m)} \right]$$

Acceleration Factor ($\alpha$):
Because the Gauss-Seidel algorithm exhibits slow, linear convergence, an acceleration factor $\alpha$ ($1.4 \le \alpha \le 1.6$) is universally applied to speed up convergence by magnifying the incremental correction:
$$V_i^{(m+1), acc} = V_i^{(m)} + \alpha \left[ V_i^{(m+1)} - V_i^{(m)} \right]$$
Applying acceleration to both real and imaginary components reduces the total number of iterations by up to 50%.

Handling of Generator (PV) Buses:
At a PV bus $i$, active power $P_i^{sch}$ and voltage magnitude $|V_i|^{spec}$ are specified, while reactive power $Q_i$ and phase angle $\delta_i$ are unknown. Because $Q_i$ is not specified, it must be estimated at every iteration:
1. Estimate Reactive Power $Q_i^{(m+1)}$:
Using the current estimates of bus voltages:
$$Q_i^{(m+1)} = -\text{Im} \left\{ \left(V_i^{(m)}\right)^* \left[ \sum_{k=1}^{i-1} Y_{ik} V_k^{(m+1)} + \sum_{k=i}^n Y_{ik} V_k^{(m)} \right] \right\}$$
2. Check Reactive Power Capability Limits:
Compare the calculated $Q_i^{(m+1)}$ against the generator physical excitation limits:
$$Q_{i,min} \le Q_i^{(m+1)} \le Q_{i,max}$$
- If $Q_i^{(m+1)}$ falls strictly within limits, the bus remains a PV bus. Compute temporary voltage $V_{i,temp}^{(m+1)}$ using the standard Gauss-Seidel formula with $Q_i = Q_i^{(m+1)}$.
Because the magnitude $|V_i|^{spec}$ must remain fixed, preserve the newly computed phase angle $\delta_i^{(m+1)}$ while resetting the magnitude:
$$V_i^{(m+1)} = |V_i|^{spec} \angle \delta_{i,temp}^{(m+1)} = |V_i|^{spec} \frac{V_{i,temp}^{(m+1)}}{|V_{i,temp}^{(m+1)}|}$$
- If $Q_i^{(m+1)} > Q_{i,max}$: Clamp $Q_i = Q_{i,max}$. The generator has reached its overexcitation thermal limit. Release voltage magnitude $|V_i|^{spec}$ and treat the bus as a PQ bus for all subsequent iterations.
- If $Q_i^{(m+1)} < Q_{i,min}$: Clamp $Q_i = Q_{i,min}$. The generator has reached its stability underexcitation limit. Treat the bus as a PQ bus.

Algorithm Termination:
Iterations terminate when the maximum voltage change between successive iterations falls below a specified convergence tolerance $\epsilon$:
$$\max_{i} \left| V_i^{(m+1)} - V_i^{(m)} \right| \le \epsilon \approx 10^{-4} \text{ pu}$$
"""
    },
    {
        "qid": "ps2-q14",
        "marks": 7,
        "type": "Long Derivation",
        "title": "Newton-Raphson Power Flow Method in Polar Coordinates: Jacobian Formulation",
        "yt_query": "newton raphson load flow method polar coordinates jacobian matrix derivation",
        "img_path": "images/ps2/newton_raphson_jacobian_structure.png",
        "img_caption": "Figure 3.4: Partitioned Structure of the Newton-Raphson Power Flow Jacobian Matrix",
        "answer": r"""
The Newton-Raphson (N-R) method is the industrial standard algorithm for power flow analysis in modern transmission grids. Based on multi-variable Taylor series expansion, it possesses quadratic convergence characteristics, typically achieving convergence to machine precision in only 3 to 5 iterations regardless of network size.

Mathematical Formulation:
Let an $n$-bus system contain 1 Slack bus (Bus 1), $m$ PV buses, and $(n - 1 - m)$ PQ buses.
The unknown state variables are:
- Voltage phase angles $\delta_i$ for all $n - 1$ non-slack buses ($i = 2, 3, \dots, n$).
- Voltage magnitudes $|V_i|$ for all $(n - 1 - m)$ PQ buses.

Expanding the non-linear real and reactive power equations in Taylor series around operating point $(\delta^{(0)}, |V|^{(0)})$ and truncating higher-order terms:
$$\begin{bmatrix} \Delta P \\ \Delta Q \end{bmatrix} = \begin{bmatrix} J_1 & J_2 \\ J_3 & J_4 \end{bmatrix} \begin{bmatrix} \Delta \delta \\ \Delta |V| \end{bmatrix} = \begin{bmatrix} H & N \\ M & L \end{bmatrix} \begin{bmatrix} \Delta \delta \\ \Delta |V| / |V| \end{bmatrix}$$
where $\Delta P_i = P_i^{sch} - P_i^{calc}$ and $\Delta Q_i = Q_i^{sch} - Q_i^{calc}$ are the mismatch vectors, and $J$ is the Jacobian Matrix.

To achieve mathematical elegance and computational symmetry, the voltage correction terms are normalized by dividing by $|V|$, scaling the Jacobian sub-matrices:
$$H_{ik} = \frac{\partial P_i}{\partial \delta_k}, \quad N_{ik} = |V_k| \frac{\partial P_i}{\partial |V_k|}, \quad M_{ik} = \frac{\partial Q_i}{\partial \delta_k}, \quad L_{ik} = |V_k| \frac{\partial Q_i}{\partial |V_k|}$$

Derivations of Jacobian Sub-Matrix Elements:
From the static power equations:
$$P_i = |V_i|^2 G_{ii} + \sum_{k=1, k\ne i}^n |V_i| |V_k| \left[ G_{ik} \cos(\delta_i - \delta_k) + B_{ik} \sin(\delta_i - \delta_k) \right]$$
$$Q_i = -|V_i|^2 B_{ii} + \sum_{k=1, k\ne i}^n |V_i| |V_k| \left[ G_{ik} \sin(\delta_i - \delta_k) - B_{ik} \cos(\delta_i - \delta_k) \right]$$

1. Sub-matrix $H$ ($\frac{\partial P}{\partial \delta}$):
- Off-Diagonal Elements ($k \ne i$):
  $$H_{ik} = \frac{\partial P_i}{\partial \delta_k} = |V_i| |V_k| \left[ G_{ik} \sin(\delta_i - \delta_k) - B_{ik} \cos(\delta_i - \delta_k) \right]$$
- Diagonal Elements ($k = i$):
  $$H_{ii} = \frac{\partial P_i}{\partial \delta_i} = -\sum_{k=1, k\ne i}^n |V_i| |V_k| \left[ G_{ik} \sin(\delta_i - \delta_k) - B_{ik} \cos(\delta_i - \delta_k) \right] = -Q_i - |V_i|^2 B_{ii}$$

2. Sub-matrix $N$ ($|V| \frac{\partial P}{\partial |V|}$):
- Off-Diagonal Elements ($k \ne i$):
  $$N_{ik} = |V_k| \frac{\partial P_i}{\partial |V_k|} = |V_i| |V_k| \left[ G_{ik} \cos(\delta_i - \delta_k) + B_{ik} \sin(\delta_i - \delta_k) \right]$$
- Diagonal Elements ($k = i$):
  $$N_{ii} = |V_i| \frac{\partial P_i}{\partial |V_i|} = P_i + |V_i|^2 G_{ii}$$

3. Sub-matrix $M$ ($\frac{\partial Q}{\partial \delta}$):
- Off-Diagonal Elements ($k \ne i$):
  $$M_{ik} = \frac{\partial Q_i}{\partial \delta_k} = -|V_i| |V_k| \left[ G_{ik} \cos(\delta_i - \delta_k) + B_{ik} \sin(\delta_i - \delta_k) \right] = -N_{ik}$$
- Diagonal Elements ($k = i$):
  $$M_{ii} = \frac{\partial Q_i}{\partial \delta_i} = \sum_{k=1, k\ne i}^n |V_i| |V_k| \left[ G_{ik} \cos(\delta_i - \delta_k) + B_{ik} \sin(\delta_i - \delta_k) \right] = P_i - |V_i|^2 G_{ii}$$

4. Sub-matrix $L$ ($|V| \frac{\partial Q}{\partial |V|}$):
- Off-Diagonal Elements ($k \ne i$):
  $$L_{ik} = |V_k| \frac{\partial Q_i}{\partial |V_k|} = |V_i| |V_k| \left[ G_{ik} \sin(\delta_i - \delta_k) - B_{ik} \cos(\delta_i - \delta_k) \right] = H_{ik}$$
- Diagonal Elements ($k = i$):
  $$L_{ii} = |V_i| \frac{\partial Q_i}{\partial |V_i|} = Q_i - |V_i|^2 B_{ii}$$

Computational Algorithm:
1. Initialize flat start: $\delta_i^{(0)} = 0^\circ$ and $|V_i|^{(0)} = 1.0 \text{ pu}$ for PQ buses.
2. Evaluate $P_i^{calc}$ and $Q_i^{calc}$ using current states.
3. Compute mismatches $\Delta P_i$ and $\Delta Q_i$. If all mismatches are less than tolerance ($10^{-4}$), stop.
4. Formulate the Jacobian matrix $J$ using derived analytical derivatives.
5. Solve the linear algebraic system $J \begin{bmatrix} \Delta\delta \\ \Delta|V|/|V| \end{bmatrix} = \begin{bmatrix} \Delta P \\ \Delta Q \end{bmatrix}$ via LU decomposition.
6. Update states: $\delta_i^{(m+1)} = \delta_i^{(m)} + \Delta\delta_i$ and $|V_i|^{(m+1)} = |V_i|^{(m)} + \Delta|V_i|$. Repeat until convergence.

Comparison: N-R requires significantly fewer iterations (3-5) compared to Gauss-Seidel (50-200), converges reliably on ill-conditioned systems, but requires evaluating and factorizing the Jacobian matrix at every iteration.
"""
    },
    {
        "qid": "ps2-q15",
        "marks": 3,
        "type": "Short Answer",
        "title": "Fast Decoupled Load Flow (FDLF): Physical Assumptions, B' and B'' Derivation",
        "yt_query": "fast decoupled load flow FDLF assumptions B prime B double prime derivation",
        "img_path": "images/ps2/fdlf_decoupling_concept.png",
        "img_caption": "Figure 3.5: Physical Decoupling of P-delta and Q-V Control Loops in Fast Decoupled Load Flow",
        "answer": r"""
The Fast Decoupled Load Flow (FDLF) method, developed by Brian Stott and Ongun Alsac in 1974, represents one of the most brilliant practical simplifications of the Newton-Raphson algorithm. It exploits the inherent physical properties of high-voltage electrical transmission systems to decouple active and reactive power computations into two independent, fast matrix equations.

Physical Decoupling Assumptions:
In high-voltage transmission networks:
1. $P - \delta$ and $Q - |V|$ Decoupling: Active power flow $P$ is predominantly driven by voltage phase angle differences $\delta$, showing very weak sensitivity to voltage magnitude variations ($\frac{\partial P}{\partial |V|} \approx 0 \implies N \approx 0$). Conversely, reactive power flow $Q$ is primarily controlled by voltage magnitude differences $|V|$, being virtually insensitive to phase angles ($\frac{\partial Q}{\partial \delta} \approx 0 \implies M \approx 0$). This sets the off-diagonal sub-matrices of the Jacobian to zero:
$$\begin{bmatrix} \Delta P \\ \Delta Q \end{bmatrix} = \begin{bmatrix} H & 0 \\ 0 & L \end{bmatrix} \begin{bmatrix} \Delta \delta \\ \Delta |V| \end{bmatrix}$$
2. Small Angle Differences: Under normal operating conditions, phase angle differences between adjacent buses are small (typically less than $5^\circ$):
$$\cos(\delta_i - \delta_k) \approx 1, \quad \sin(\delta_i - \delta_k) \approx 0$$
3. High $X/R$ Ratio: Overhead lines have line reactances far exceeding line resistances ($X \gg R \implies R/X \ll 1$):
$$G_{ik} = \frac{R}{R^2 + X^2} \ll B_{ik} = \frac{-X}{R^2 + X^2} \implies G_{ik} \approx 0$$
4. Reactive Injection Dominance: Bus reactive power injection is negligible compared to bus short-circuit susceptance ($Q_i \ll |V_i|^2 B_{ii}$).

Derivation of Decoupled Matrices $B'$ and $B''$:
Under these physical simplifications, the diagonal and off-diagonal elements of $H$ and $L$ reduce to:
$$H_{ik} = L_{ik} = -|V_i| |V_k| B_{ik}$$
$$H_{ii} = L_{ii} = -|V_i|^2 B_{ii}$$
Dividing both sides by $|V_i|$ and assuming $|V_k| \approx 1.0 \text{ pu}$:
$$\frac{\Delta P_i}{|V_i|} = \sum_{k=1, k\ne i}^n -B_{ik} (\Delta\delta_k) - B_{ii} (\Delta\delta_i)$$
$$\frac{\Delta Q_i}{|V_i|} = \sum_{k=1, k\ne i}^n -B_{ik} (\Delta|V_k|) - B_{ii} (\Delta|V_i|)$$

In compact matrix notation:
$$\left[ \frac{\Delta P}{|V|} \right] = \left[ B' \right] [\Delta \delta]$$
$$\left[ \frac{\Delta Q}{|V|} \right] = \left[ B'' \right] [\Delta |V|]$$
where:
- Matrix $B'$ has dimension $(n - 1) \times (n - 1)$, formed by omitting the slack bus row and column from the imaginary part of $Y_{bus}$. Furthermore, elements that primarily influence MVAR flow (such as shunt reactances and transformer off-nominal taps) are omitted from $B'$.
- Matrix $B''$ has dimension $(n - 1 - m) \times (n - 1 - m)$, formed by omitting the slack bus and all PV bus rows and columns. Phase-shifting transformer angle effects are omitted from $B''$.

Key Engineering Advantages:
1. Invariable Matrices: Both $B'$ and $B''$ are real, symmetric, sparse, and strictly constant. They are factorized into triangular $LU$ forms once at the start of the program and never re-evaluated during iterations.
2. Computational Speed: Each iteration requires only simple forward-backward substitutions. An FDLF iteration is roughly 5 times faster than a standard Newton-Raphson iteration.
3. Reliability: While it may require 1 to 2 more iterations than full N-R, overall solution speed is 3 to 4 times faster with virtually identical numerical accuracy.
"""
    }
]
