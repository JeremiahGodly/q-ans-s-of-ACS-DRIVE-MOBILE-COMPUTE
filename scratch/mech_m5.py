# -*- coding: utf-8 -*-
"""
Module 5: Work, Energy, Impulse, Momentum and Impact (mech-q21 to mech-q26)
KTU 2019 Scheme Engineering Mechanics (EST100)
"""

MODULE_5 = {
    "module_id": "mech-m5",
    "module_num": "Module 5",
    "module_title": "Work-Energy Theorem, Impulse-Momentum and Direct Central Impact",
    "questions": [
        {
            "qid": "mech-q21",
            "marks": 7,
            "type": "Derivation",
            "title": "Work-Energy Theorem for a Particle: Derivation and Work Done by Forces",
            "yt_query": "work energy theorem particle derivation work done gravity spring force mechanics",
            "img_path": "images/mechanics/work_energy_particle.png",
            "img_caption": "Figure 5.1: Particle Displacement along Curve under Variable Force and Work Calculation",
            "answer": r"""
The Work-Energy Theorem provides an integral formulation of Newton's second law that relates the forces acting on a body directly to changes in its velocity over a specified displacement, completely eliminating time as an intermediate variable.

Definition of Work Done by a Force:
In classical mechanics, the work done $U$ by a force vector $\mathbf{F}$ acting on a particle as it undergoes an infinitesimal vector displacement $d\mathbf{r}$ is defined as the dot product:
$$dU = \mathbf{F} \cdot d\mathbf{r} = F \cos\theta \, ds$$
where $\theta$ is the angle between the force vector and the displacement vector, and $ds = |d\mathbf{r}|$ is the scalar path displacement.
The total work done by force $\mathbf{F}$ as the particle traverses a continuous path from position 1 to position 2 is the line integral:
$$U_{1-2} = \int_1^2 \mathbf{F} \cdot d\mathbf{r} = \int_{s_1}^{s_2} F_t \, ds$$
where $F_t = F \cos\theta$ is the tangential component of force along the path of motion.

Work Done by Common Engineering Forces:
1. Work Done by a Constant Force in Rectilinear Motion:
If a constant force $F$ acts at a constant angle $\theta$ over linear displacement $s$:
$$U = (F \cos\theta) s$$
2. Work Done by Gravity (Weight of Particle):
Let a body of mass $m$ move from vertical elevation $y_1$ to elevation $y_2$. The gravitational force is $\mathbf{F}_g = -mg \hat{\mathbf{j}}$ (acting downward).
The differential displacement is $d\mathbf{r} = dx \hat{\mathbf{i}} + dy \hat{\mathbf{j}} + dz \hat{\mathbf{k}}$.
$$U_g = \int_{y_1}^{y_2} (-mg \hat{\mathbf{j}}) \cdot (dy \hat{\mathbf{j}}) = -mg \int_{y_1}^{y_2} dy = -mg (y_2 - y_1)$$
- If the body moves downward ($y_2 < y_1$), work done by gravity is positive ($+mg h$).
- If the body moves upward ($y_2 > y_1$), work done by gravity is negative ($-mg h$).
3. Work Done by a Linear Elastic Spring:
According to Hooke's law, the restoring force exerted by a spring deformed by displacement $x$ from its unstretched equilibrium position is $F_s = -k x$, where $k$ is the spring stiffness ($\text{N/m}$).
The work done by the spring as its deformation changes from initial stretch $x_1$ to final stretch $x_2$ is:
$$U_s = \int_{x_1}^{x_2} (-k x) dx = -k \left[ \frac{x^2}{2} \right]_{x_1}^{x_2} = -\frac{1}{2} k (x_2^2 - x_1^2) = \frac{1}{2} k x_1^2 - \frac{1}{2} k x_2^2$$

Mathematical Derivation of the Work-Energy Theorem:
Consider a particle of mass $m$ moving along a curved path under the action of a resultant force $\mathbf{F}$.
Resolving Newton's second law along the tangential direction of motion:
$$F_t = m a_t$$
Substituting the kinematic relation for tangential acceleration $a_t = v \frac{dv}{ds}$:
$$F_t = m \left( v \frac{dv}{ds} \right)$$
Multiplying both sides by the differential path displacement $ds$:
$$F_t \, ds = m v \, dv$$
Integrating both sides between state 1 (position $s_1$, velocity $v_1$) and state 2 (position $s_2$, velocity $v_2$):
$$\int_{s_1}^{s_2} F_t \, ds = \int_{v_1}^{v_2} m v \, dv$$
The left-hand side is the total work done by all forces acting on the particle, denoted as $U_{1-2}$ (or $\Sigma W_{1-2}$).
Evaluating the integral on the right-hand side:
$$\int_{v_1}^{v_2} m v \, dv = m \left[ \frac{v^2}{2} \right]_{v_1}^{v_2} = \frac{1}{2} m v_2^2 - \frac{1}{2} m v_1^2$$
Defining the Kinetic Energy of the particle as $T = \frac{1}{2} m v^2$:
$$U_{1-2} = T_2 - T_1 = \Delta T = \Delta KE$$
Statement of the Work-Energy Theorem:
The total work done by all external forces (conservative and non-conservative) acting on a particle during a displacement is equal to the change in the kinetic energy of the particle over that displacement.
"""
        },
        {
            "qid": "mech-q22",
            "marks": 7,
            "type": "Theory & Derivation",
            "title": "Conservative Force Fields and the Law of Conservation of Mechanical Energy",
            "yt_query": "conservative forces potential energy conservation mechanical energy pendulum derivation",
            "img_path": "images/mechanics/conservation_mechanical_energy.png",
            "img_caption": "Figure 5.2: Potential and Kinetic Energy Exchange in Simple Pendulum Oscillation",
            "answer": r"""
In engineering mechanics, forces acting on dynamic systems are broadly classified as either conservative or non-conservative (dissipative) forces.

Conservative Forces and Criteria:
A force $\mathbf{F}$ is defined as Conservative if the work done by the force in moving a particle between two points depends solely on the initial and final positions of the particle and is completely independent of the physical path taken between them.
Mathematical Criteria for a Conservative Force:
1. Path Independence: For any two distinct paths $A$ and $B$ joining positions 1 and 2:
$$\int_{1, \text{Path } A}^2 \mathbf{F} \cdot d\mathbf{r} = \int_{1, \text{Path } B}^2 \mathbf{F} \cdot d\mathbf{r}$$
2. Zero Closed Loop Work: The net work done by a conservative force around any closed loop is identically zero:
$$\oint \mathbf{F} \cdot d\mathbf{r} = 0$$
3. Curl-Free Force Field: The curl of the force vector is identically zero:
$$\nabla \times \mathbf{F} = \text{curl}(\mathbf{F}) = 0$$
Examples of conservative forces include gravitational forces, electrostatic forces, and ideal linear elastic spring forces. In contrast, frictional forces and fluid drag are non-conservative because their work depends on path length and is dissipated irreversibly as heat.

Potential Energy Function ($V$):
Because the work done by a conservative force is path-independent, it can be expressed as the negative change of a scalar potential function $V(\mathbf{r})$, called the Potential Energy:
$$dU = \mathbf{F} \cdot d\mathbf{r} = -dV \implies \mathbf{F} = -\nabla V = -\left( \frac{\partial V}{\partial x}\hat{\mathbf{i}} + \frac{\partial V}{\partial y}\hat{\mathbf{j}} + \frac{\partial V}{\partial z}\hat{\mathbf{k}} \right)$$
Integrating from position 1 to position 2:
$$U_{1-2} = \int_1^2 \mathbf{F} \cdot d\mathbf{r} = -\int_1^2 dV = -(V_2 - V_1) = V_1 - V_2$$
Standard Potential Energy Expressions:
- Gravitational Potential Energy: Taking datum at $y = 0$:
$$V_g = m g y$$
- Elastic Spring Potential Energy: Taking datum at unstretched length $x = 0$:
$$V_e = \frac{1}{2} k x^2$$

Mathematical Proof of the Law of Conservation of Mechanical Energy:
Consider a mechanical system acted upon solely by conservative forces.
According to the Work-Energy Theorem:
$$U_{1-2} = T_2 - T_1$$
Since all operating forces are conservative:
$$U_{1-2} = V_1 - V_2$$
Equating these two expressions:
$$V_1 - V_2 = T_2 - T_1$$
Rearranging terms so that state 1 terms appear on the left and state 2 terms on the right:
$$T_1 + V_1 = T_2 + V_2$$
Defining the Total Mechanical Energy $E$ as the sum of kinetic and potential energy ($E = T + V$):
$$E_1 = E_2 = \text{constant}$$
Statement of the Law:
In an isolated mechanical system where all active forces are conservative, the total mechanical energy (kinetic plus potential) remains strictly constant throughout the motion.

Physical Application: Velocity of an Oscillating Simple Pendulum:
Consider a simple pendulum consisting of a bob of mass $m$ suspended by a light inextensible cord of length $l$. The bob is pulled aside to an initial angle $\theta_0$ with the vertical and released from rest ($v_1 = 0$).
Determine the velocity $v$ of the bob when it swings through an intermediate angle $\theta$.
1. Select Datum: Set the gravitational potential energy datum ($y = 0$) at the lowest equilibrium position of the bob ($\theta = 0$).
2. Initial State 1 (Release at angle $\theta_0$):
- Height above datum: $h_1 = l - l \cos\theta_0 = l(1 - \cos\theta_0)$
- Kinetic energy: $T_1 = \frac{1}{2} m v_1^2 = 0$ (released from rest)
- Potential energy: $V_1 = m g h_1 = m g l (1 - \cos\theta_0)$
- Total initial energy: $E_1 = T_1 + V_1 = m g l (1 - \cos\theta_0)$
3. Intermediate State 2 (At angle $\theta$):
- Height above datum: $h_2 = l(1 - \cos\theta)$
- Kinetic energy: $T_2 = \frac{1}{2} m v^2$
- Potential energy: $V_2 = m g h_2 = m g l (1 - \cos\theta)$
- Total energy: $E_2 = \frac{1}{2} m v^2 + m g l (1 - \cos\theta)$
4. Applying Conservation of Mechanical Energy ($E_1 = E_2$):
$$m g l (1 - \cos\theta_0) = \frac{1}{2} m v^2 + m g l (1 - \cos\theta)$$
$$\frac{1}{2} m v^2 = m g l (1 - \cos\theta_0) - m g l (1 - \cos\theta) = m g l (\cos\theta - \cos\theta_0)$$
Dividing by $m$ and multiplying by 2:
$$v^2 = 2 g l (\cos\theta - \cos\theta_0) \implies v = \sqrt{2 g l (\cos\theta - \cos\theta_0)}$$
At the lowest point ($\theta = 0$, $\cos 0 = 1$), the velocity reaches its maximum:
$$v_{max} = \sqrt{2 g l (1 - \cos\theta_0)}$$
Notice that cord tension does zero work because it is always perpendicular to velocity ($T \perp d\mathbf{r}$), making energy conservation exact.
"""
        },
        {
            "qid": "mech-q23",
            "marks": 7,
            "type": "Derivation & Application",
            "title": "Linear Impulse-Momentum Principle: Derivation and Force of Water Jet on Vane",
            "yt_query": "impulse momentum principle derivation water jet impact vane engineering mechanics",
            "img_path": "images/mechanics/impulse_momentum_jet.png",
            "img_caption": "Figure 5.3: Impulse of Force Vector and Dynamic Deflection of a Continuous Fluid Jet Striking a Vane",
            "answer": r"""
The Impulse-Momentum Principle provides a direct formulation of Newton's second law integrated with respect to time rather than displacement. It relates applied forces and time intervals directly to changes in linear momentum.

Linear Momentum and Impulse Definitions:
1. Linear Momentum ($\mathbf{p}$): The linear momentum of a particle of mass $m$ moving with velocity vector $\mathbf{v}$ is defined as:
$$\mathbf{p} = m \mathbf{v}$$
Linear momentum is a vector quantity having the same direction as the instantaneous velocity, with SI units of $\text{kg}\cdot\text{m/s}$ (or $\text{N}\cdot\text{s}$).
2. Linear Impulse ($\mathbf{J}$): The linear impulse of a force $\mathbf{F}$ acting over a time interval from $t_1$ to $t_2$ is defined as the time integral of the force vector:
$$\mathbf{J} = \int_{t_1}^{t_2} \mathbf{F} \, dt$$
Impulse is a vector quantity having the direction of the force. Graphically, the magnitude of impulse equals the area under the force-time curve ($F-t$ curve) between $t_1$ and $t_2$.
If the force $\mathbf{F}$ is constant in magnitude and direction:
$$\mathbf{J} = \mathbf{F} (t_2 - t_1) = \mathbf{F} \Delta t$$
3. Impulsive Forces: An impulsive force is a very large force that acts over an extremely short duration $\Delta t$ (such as an impact blow, hammer strike, explosion, or projectile collision). Because the time interval is vanishingly small, non-impulsive forces (such as gravity or light spring forces) produce negligible impulse during the impact interval and are neglected in momentum analysis.

Mathematical Derivation of the Impulse-Momentum Principle:
Consider a particle of constant mass $m$ acted upon by a resultant force $\mathbf{F}$.
Newton's second law states:
$$\mathbf{F} = m \mathbf{a} = m \frac{d\mathbf{v}}{dt} = \frac{d(m\mathbf{v})}{dt} = \frac{d\mathbf{p}}{dt}$$
Multiplying both sides by differential time $dt$:
$$\mathbf{F} \, dt = d(m\mathbf{v})$$
Integrating both sides over the time interval from $t_1$ (when velocity is $\mathbf{v}_1$) to $t_2$ (when velocity is $\mathbf{v}_2$):
$$\int_{t_1}^{t_2} \mathbf{F} \, dt = \int_{\mathbf{v}_1}^{\mathbf{v}_2} d(m\mathbf{v}) = m \mathbf{v}_2 - m \mathbf{v}_1$$
Substituting the definition of impulse $\mathbf{J}$:
$$\mathbf{J}_{1-2} = m \mathbf{v}_2 - m \mathbf{v}_1 = \mathbf{p}_2 - \mathbf{p}_1 = \Delta \mathbf{p}$$
Statement of the Impulse-Momentum Principle:
The total linear impulse exerted on a particle by the resultant force over a given time interval is equal to the change in the linear momentum of the particle over that same time interval.
In scalar Cartesian components:
$$\int_{t_1}^{t_2} F_x \, dt = m v_{2x} - m v_{1x}$$
$$\int_{t_1}^{t_2} F_y \, dt = m v_{2y} - m v_{1y}$$

Engineering Application: Hydrodynamic Force Exerted by a Fluid Jet on a Fixed Vane:
Consider a continuous high-speed liquid jet (e.g., water in a Pelton turbine) of fluid density $\rho$, cross-sectional area $A$, and velocity $v$ discharging horizontally. The jet strikes a stationary solid curved vane that deflects the jet through an angle $\beta$ without altering its speed ($v_{exit} = v$, assuming smooth frictionless flow).
1. Mass Flow Rate:
The mass of water striking the vane per second is:
$$\dot{m} = \rho A v = \rho Q$$
where $Q = A v$ is the volumetric discharge rate ($\text{m}^3\text{/s}$).
2. Applying Impulse-Momentum Equation to Steady Fluid Flow:
For a continuous flow stream, the impulse-momentum principle translates into the momentum rate equation:
$$\Sigma \mathbf{F} = \dot{m} (\mathbf{v}_{out} - \mathbf{v}_{in})$$
where $\Sigma \mathbf{F}$ is the net force exerted by the vane on the fluid stream.
3. Resolving Velocity Components:
- Initial velocity vector entering horizontally along $x$:
  $$\mathbf{v}_{in} = v \hat{\mathbf{i}} + 0 \hat{\mathbf{j}}$$
- Final velocity vector exiting the curved vane at angle $\beta$ to the horizontal:
  $$\mathbf{v}_{out} = (v \cos\beta)\hat{\mathbf{i}} + (v \sin\beta)\hat{\mathbf{j}}$$
4. Force Exerted on the Fluid Stream:
- Horizontal force on fluid:
  $$F_x = \dot{m}(v_{out, x} - v_{in, x}) = \dot{m}(v \cos\beta - v) = -\dot{m} v (1 - \cos\beta)$$
- Vertical force on fluid:
  $$F_y = \dot{m}(v_{out, y} - v_{in, y}) = \dot{m}(v \sin\beta - 0) = \dot{m} v \sin\beta$$
5. Dynamic Force Exerted by the Fluid Jet on the Vane:
By Newton's third law of action and reaction, the force $\mathbf{R}_{jet}$ exerted by the jet on the vane is equal and opposite to the force exerted by the vane on the fluid:
$$R_{jet, x} = -F_x = \dot{m} v (1 - \cos\beta) = \rho A v^2 (1 - \cos\beta)$$
$$R_{jet, y} = -F_y = -\dot{m} v \sin\beta = -\rho A v^2 \sin\beta$$
Special Case 1: Flat Plate Perpendicular to Jet ($\beta = 90^\circ, \cos 90^\circ = 0$):
$$R_x = \rho A v^2$$
Special Case 2: Semicircular Curved Vane Deflecting Jet by $180^\circ$ ($\beta = 180^\circ, \cos 180^\circ = -1$):
$$R_x = \rho A v^2 [1 - (-1)] = 2 \rho A v^2$$
The horizontal force on a $180^\circ$ reversing cup vane is twice that on a flat plate, which is why Pelton turbine buckets are split into double-hemispherical cups.
"""
        },
        {
            "qid": "mech-q24",
            "marks": 7,
            "type": "Derivation & Application",
            "title": "Conservation of Linear Momentum: System of Particles and Recoil Mechanics",
            "yt_query": "conservation of linear momentum derivation system particles recoil velocity mechanics",
            "img_path": "images/mechanics/conservation_linear_momentum.png",
            "img_caption": "Figure 5.4: Internal Action-Reaction Forces Canceling in Pairs During Recoil of Artillery Cannon",
            "answer": r"""
The Principle of Conservation of Linear Momentum is one of the most fundamental conservation laws in physics and engineering. It applies universally to all mechanical interactions, collisions, and propulsion systems, regardless of whether mechanical kinetic energy is conserved or whether the internal forces are linear or non-linear.

Derivation for a System of Interacting Particles:
Consider an arbitrary system composed of $n$ interacting particles of masses $m_1, m_2, \dots, m_n$ moving with velocities $\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n$.
The total linear momentum $\mathbf{P}$ of the system is the vector sum of the linear momentums of all constituent particles:
$$\mathbf{P} = \sum_{i=1}^n m_i \mathbf{v}_i = m_1 \mathbf{v}_1 + m_2 \mathbf{v}_2 + \dots + m_n \mathbf{v}_n$$
The forces acting on any $i$-th particle are divided into two categories:
1. Internal Forces ($\mathbf{f}_{ij}$): Forces exerted on particle $i$ by particle $j$ inside the system (e.g., intermolecular forces, structural tension, mutual contact forces).
2. External Forces ($\mathbf{F}_i^{ext}$): Forces exerted on particle $i$ by bodies outside the system boundary (e.g., gravity, external applied loads).

Applying Newton's second law to the $i$-th particle:
$$\mathbf{F}_i^{ext} + \sum_{j \neq i} \mathbf{f}_{ij} = \frac{d}{dt}(m_i \mathbf{v}_i)$$
Summing this equation over all $n$ particles in the system:
$$\sum_{i=1}^n \mathbf{F}_i^{ext} + \sum_{i=1}^n \sum_{j \neq i} \mathbf{f}_{ij} = \frac{d}{dt}\left( \sum_{i=1}^n m_i \mathbf{v}_i \right) = \frac{d\mathbf{P}}{dt}$$
According to Newton's third law of motion, for every action force $\mathbf{f}_{ij}$ exerted by particle $j$ on particle $i$, particle $i$ exerts an equal and opposite reaction force $\mathbf{f}_{ji}$ on particle $j$:
$$\mathbf{f}_{ij} = -\mathbf{f}_{ji} \implies \mathbf{f}_{ij} + \mathbf{f}_{ji} = 0$$
Consequently, when summed over the entire closed system, all internal action-reaction force pairs cancel identically:
$$\sum_{i=1}^n \sum_{j \neq i} \mathbf{f}_{ij} = 0$$
The equation simplifies to:
$$\Sigma \mathbf{F}^{ext} = \frac{d\mathbf{P}}{dt}$$
This proves that the time rate of change of the total linear momentum of a system of particles depends solely on the resultant external force acting on the system.

Statement of the Principle of Conservation of Linear Momentum:
If the resultant external force acting on a system of particles is identically zero ($\Sigma \mathbf{F}^{ext} = 0$):
$$\frac{d\mathbf{P}}{dt} = 0 \implies \mathbf{P} = \sum_{i=1}^n m_i \mathbf{v}_i = \text{constant}$$
The total linear momentum of an isolated system remains constant in both magnitude and direction over time.
For two interacting bodies of masses $m_1$ and $m_2$ colliding or separating:
$$m_1 \mathbf{u}_1 + m_2 \mathbf{u}_2 = m_1 \mathbf{v}_1 + m_2 \mathbf{v}_2$$
where $\mathbf{u}_1, \mathbf{u}_2$ are velocities before interaction and $\mathbf{v}_1, \mathbf{v}_2$ are velocities after interaction.

Application: Recoil Velocity of an Artillery Gun:
Problem Statement: A cannon of mass $M$ mounted on a frictionless horizontal track fires a shell of mass $m$ with a horizontal muzzle velocity $v_b$ relative to the barrel. Determine the recoil velocity $V_R$ of the cannon.

Step-by-Step Analytical Solution:
1. Identify the System:
Define the system as the cannon plus the shell: total mass $= M + m$.
2. Analyze External Forces:
In the horizontal direction, there are no external applied forces (the horizontal track is frictionless, $\Sigma F_x^{ext} = 0$). The explosion of gunpowder generates explosive expanding gas pressures that are purely internal to the cannon-shell system.
Therefore, total linear momentum in the horizontal direction is strictly conserved:
$$P_{initial, x} = P_{final, x}$$
3. Initial State (Before Firing):
Both the cannon and the shell are at rest:
$$P_{initial, x} = 0$$
4. Final State (After Firing):
Let the shell be fired with velocity $v_b$ in the positive $x$-direction ($+\hat{\mathbf{i}}$).
Let $V_R$ be the recoil velocity of the cannon in the negative $x$-direction ($-\hat{\mathbf{i}}$).
The total final momentum is:
$$P_{final, x} = m v_b + M V_R$$
5. Applying Conservation of Momentum:
$$0 = m v_b + M V_R \implies M V_R = -m v_b$$
Solving for the recoil velocity:
$$V_R = -\left(\frac{m}{M}\right) v_b$$
The negative sign confirms that the cannon recoils in the opposite direction to the trajectory of the fired projectile.
Because the mass of the cannon is much larger than the mass of the shell ($M \gg m$), the ratio $\frac{m}{M}$ is small, ensuring that the recoil velocity $V_R$ remains manageable and can be absorbed by hydraulic recoil brake buffers.
"""
        },
        {
            "qid": "mech-q25",
            "marks": 7,
            "type": "Derivation",
            "title": "Direct Central Impact of Colliding Bodies: Coefficient of Restitution and Velocity Formulations",
            "yt_query": "direct central impact collision coefficient of restitution velocities derivation mechanics",
            "img_path": "images/mechanics/direct_central_impact.png",
            "img_caption": "Figure 5.5: Contact Phases During Direct Central Collision: Approach, Maximum Deformation, and Restitution",
            "answer": r"""
Impact is defined as a collision between two bodies occurring over a very short duration of time, during which comparatively large impulsive contact forces are generated. In engineering dynamics, an impact is classified as:
1. Direct Impact: The velocities of both colliding bodies are directed along the common normal to the contacting surfaces (the line of impact).
2. Central Impact: The centers of mass ($CG$) of both colliding bodies lie on the line of impact.
A Direct Central Impact occurs when both bodies move collinear along the line connecting their centers of mass before and after impact.

Physical Phases of Collision and Coefficient of Restitution ($e$):
When two elastic bodies of masses $m_1$ and $m_2$ collide with initial approach velocities $u_1$ and $u_2$ (with $u_1 > u_2$ along the common line of impact):
1. Period of Deformation: Contact begins; the bodies deform elastically and plastically. The impulsive deformation force compresses both bodies until they reach a common intermediate velocity $v_c$ at the instant of maximum deformation.
Let $\int P \, dt$ be the deformation impulse.
2. Period of Restitution: The internal elastic strain energy stored during deformation attempts to restore the original shapes, pushing the bodies apart until they separate with final velocities $v_1$ and $v_2$.
Let $\int R \, dt$ be the restitution impulse.

Newton's Experimental Law of Collision and Definition of $e$:
Formulated empirically by Sir Isaac Newton, the Coefficient of Restitution $e$ is defined as the ratio of the magnitude of the restitution impulse to the deformation impulse:
$$e = \frac{\int R \, dt}{\int P \, dt}$$
Newton demonstrated that this impulse ratio is identically equal to the ratio of the relative velocity of separation to the relative velocity of approach along the line of impact:
$$e = \frac{\text{Relative Velocity of Separation}}{\text{Relative Velocity of Approach}} = \frac{v_2 - v_1}{u_1 - u_2}$$
where $0 \le e \le 1$.
- Perfectly Elastic Collision ($e = 1$): Complete restitution, kinetic energy is conserved.
- Inelastic Collision ($0 < e < 1$): Partial restitution, some kinetic energy is dissipated as heat and sound.
- Perfectly Plastic / Inelastic Collision ($e = 0$): Zero restitution; colliding bodies stick together and move with a single common velocity ($v_1 = v_2$).

Mathematical Derivation of Post-Collision Velocities ($v_1$ and $v_2$):
Consider two bodies of masses $m_1$ and $m_2$ moving along a straight horizontal line with initial velocities $u_1$ and $u_2$ ($u_1 > u_2$).
Let their post-collision velocities be $v_1$ and $v_2$.
Because the impulsive contact forces during impact are internal to the two-body system, total linear momentum along the line of impact is strictly conserved:
$$m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2 \quad \text{--- (Equation 1)}$$
From the definition of the coefficient of restitution:
$$v_2 - v_1 = e (u_1 - u_2) \implies v_2 = v_1 + e (u_1 - u_2) \quad \text{--- (Equation 2)}$$

1. Derivation of Velocity of Body 1 ($v_1$):
Substituting Equation 2 ($v_2 = v_1 + e(u_1 - u_2)$) directly into Equation 1:
$$m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 \left[ v_1 + e (u_1 - u_2) \right]$$
Expanding terms:
$$m_1 u_1 + m_2 u_2 = (m_1 + m_2) v_1 + m_2 e u_1 - m_2 e u_2$$
Rearranging to isolate $(m_1 + m_2) v_1$:
$$(m_1 + m_2) v_1 = m_1 u_1 - m_2 e u_1 + m_2 u_2 + m_2 e u_2$$
Factoring $u_1$ and $u_2$:
$$(m_1 + m_2) v_1 = (m_1 - e m_2) u_1 + m_2 (1 + e) u_2$$
Dividing by $(m_1 + m_2)$ yields:
$$v_1 = \frac{(m_1 - e m_2) u_1 + m_2 (1 + e) u_2}{m_1 + m_2}$$

2. Derivation of Velocity of Body 2 ($v_2$):
From Equation 2, $v_1 = v_2 - e (u_1 - u_2)$. Substituting this into Equation 1:
$$m_1 u_1 + m_2 u_2 = m_1 \left[ v_2 - e (u_1 - u_2) \right] + m_2 v_2 = (m_1 + m_2) v_2 - m_1 e u_1 + m_1 e u_2$$
Rearranging to isolate $(m_1 + m_2) v_2$:
$$(m_1 + m_2) v_2 = m_1 u_1 + m_1 e u_1 + m_2 u_2 - m_1 e u_2$$
Factoring $u_1$ and $u_2$:
$$(m_1 + m_2) v_2 = m_1 (1 + e) u_1 + (m_2 - e m_1) u_2$$
Dividing by $(m_1 + m_2)$ yields:
$$v_2 = \frac{m_1 (1 + e) u_1 + (m_2 - e m_1) u_2}{m_1 + m_2}$$

Special Physical Cases:
1. Identical Masses in Perfectly Elastic Collision ($m_1 = m_2 = m$, $e = 1$):
$$v_1 = \frac{(m - m)u_1 + m(2)u_2}{2m} = \frac{2m u_2}{2m} = u_2$$
$$v_2 = \frac{m(2)u_1 + (m - m)u_2}{2m} = \frac{2m u_1}{2m} = u_1$$
The two bodies exchange their velocities completely upon impact (as observed in Newton's Cradle).
2. Perfectly Plastic Collision ($e = 0$):
$$v_1 = v_2 = \frac{m_1 u_1 + m_2 u_2}{m_1 + m_2}$$
Both bodies coalesce and travel together at the common system center-of-mass velocity.
"""
        },
        {
            "qid": "mech-q26",
            "marks": 7,
            "type": "Derivation",
            "title": "Loss of Kinetic Energy During Inelastic Impact: Complete Mathematical Derivation",
            "yt_query": "loss of kinetic energy during impact derivation inelastic collision mechanics",
            "img_path": "images/mechanics/kinetic_energy_loss.png",
            "img_caption": "Figure 5.6: Initial vs Final Kinetic Energies and Energy Dissipation Curve as Function of e",
            "answer": r"""
During a real, inelastic direct central collision between two bodies, while the total linear momentum is strictly conserved ($\Sigma \mathbf{P} = \text{constant}$), the total mechanical kinetic energy is not conserved. A portion of the initial kinetic energy is converted irreversibly into acoustic wave energy (sound), thermal energy (heat), and internal plastic strain energy during permanent deformation.

System Setup and Initial Energy Formulation:
Consider two smooth bodies of masses $m_1$ and $m_2$ moving along a common straight line with initial velocities $u_1$ and $u_2$ before impact.
Let $e$ be the coefficient of restitution, and let $v_1$ and $v_2$ be their post-collision velocities.
The total initial kinetic energy of the system before impact is:
$$E_1 = \frac{1}{2} m_1 u_1^2 + \frac{1}{2} m_2 u_2^2$$
The total final kinetic energy of the system after impact is:
$$E_2 = \frac{1}{2} m_1 v_1^2 + \frac{1}{2} m_2 v_2^2$$
The net loss of kinetic energy during the collision is defined as:
$$\Delta E = E_1 - E_2 = \left(\frac{1}{2} m_1 u_1^2 + \frac{1}{2} m_2 u_2^2\right) - \left(\frac{1}{2} m_1 v_1^2 + \frac{1}{2} m_2 v_2^2\right) \quad \text{--- (Equation 1)}$$

Step-by-Step Algebraic Derivation:
From the fundamental governing equations of direct central impact:
Conservation of linear momentum:
$$m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2 \implies m_1 (u_1 - v_1) = m_2 (v_2 - u_2) \quad \text{--- (Equation 2)}$$
Newton's law of restitution:
$$v_2 - v_1 = e (u_1 - u_2) \quad \text{--- (Equation 3)}$$

Multiplying Equation 1 by 2:
$$2 \Delta E = m_1 (u_1^2 - v_1^2) + m_2 (u_2^2 - v_2^2) = m_1 (u_1^2 - v_1^2) - m_2 (v_2^2 - u_2^2)$$
Factoring the differences of squares:
$$2 \Delta E = m_1 (u_1 - v_1)(u_1 + v_1) - m_2 (v_2 - u_2)(v_2 + u_2)$$
Using Equation 2, let $K = m_1 (u_1 - v_1) = m_2 (v_2 - u_2)$. Substituting $K$:
$$2 \Delta E = K (u_1 + v_1) - K (v_2 + u_2) = K \left[ (u_1 - u_2) - (v_2 - v_1) \right]$$
Substituting Equation 3 ($v_2 - v_1 = e(u_1 - u_2)$) into the bracket:
$$2 \Delta E = K \left[ (u_1 - u_2) - e(u_1 - u_2) \right] = K (1 - e)(u_1 - u_2) \quad \text{--- (Equation 4)}$$

Now we must evaluate the factor $K = m_1 (u_1 - v_1)$ in terms of initial velocities and mass parameters.
From the derived formula for post-collision velocity $v_1$:
$$v_1 = \frac{(m_1 - e m_2) u_1 + m_2 (1 + e) u_2}{m_1 + m_2}$$
Subtracting $v_1$ from $u_1$:
$$u_1 - v_1 = u_1 - \frac{(m_1 - e m_2) u_1 + m_2 (1 + e) u_2}{m_1 + m_2} = \frac{(m_1 + m_2) u_1 - (m_1 - e m_2) u_1 - m_2 (1 + e) u_2}{m_1 + m_2}$$
$$u_1 - v_1 = \frac{m_1 u_1 + m_2 u_1 - m_1 u_1 + e m_2 u_1 - m_2 u_2 - e m_2 u_2}{m_1 + m_2} = \frac{m_2 (1 + e) u_1 - m_2 (1 + e) u_2}{m_1 + m_2}$$
$$u_1 - v_1 = \frac{m_2 (1 + e)(u_1 - u_2)}{m_1 + m_2}$$
Multiplying by mass $m_1$ to obtain $K$:
$$K = m_1 (u_1 - v_1) = \frac{m_1 m_2 (1 + e)(u_1 - u_2)}{m_1 + m_2} \quad \text{--- (Equation 5)}$$

Substituting Equation 5 into Equation 4:
$$2 \Delta E = \left[ \frac{m_1 m_2 (1 + e)(u_1 - u_2)}{m_1 + m_2} \right] (1 - e)(u_1 - u_2)$$
$$2 \Delta E = \frac{m_1 m_2}{m_1 + m_2} (1 + e)(1 - e) (u_1 - u_2)^2$$
Since $(1 + e)(1 - e) = 1 - e^2$:
$$2 \Delta E = \frac{m_1 m_2}{m_1 + m_2} (1 - e^2) (u_1 - u_2)^2$$
Dividing by 2 gives the celebrated expression for the Loss of Kinetic Energy:
$$\Delta E = \frac{m_1 m_2}{2(m_1 + m_2)} (1 - e^2) (u_1 - u_2)^2$$
Defining the Reduced Mass of the two-body system as $\mu = \frac{m_1 m_2}{m_1 + m_2}$:
$$\Delta E = \frac{1}{2} \mu (1 - e^2) (u_1 - u_2)^2$$

Analysis of Physical Regimes:
1. Perfectly Elastic Impact ($e = 1$):
$$\Delta E = \frac{m_1 m_2}{2(m_1 + m_2)} (1 - 1^2)(u_1 - u_2)^2 = 0$$
The loss of kinetic energy is zero ($\Delta E = 0$). Kinetic energy is strictly conserved.
2. Inelastic Impact ($0 < e < 1$):
Since $0 < e < 1$, $(1 - e^2) > 0$. Therefore $\Delta E > 0$, confirming that kinetic energy is always lost during real physical collisions.
3. Perfectly Plastic / Inelastic Impact ($e = 0$):
$$\Delta E_{max} = \frac{m_1 m_2}{2(m_1 + m_2)} (u_1 - u_2)^2$$
The loss of kinetic energy is maximized when $e = 0$.
"""
        }
    ]
}
