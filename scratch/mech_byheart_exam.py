# -*- coding: utf-8 -*-
"""
Byheart Data and Exam Questions for Engineering Mechanics (EST100)
Covers mech-q1 to mech-q26
"""

MECHANICS_BYHEART = {
    "mech-q1": {
        "eq": r"$$R = \sqrt{(\Sigma F_x)^2 + (\Sigma F_y)^2}, \quad \tan\theta_R = \left|\frac{\Sigma F_y}{\Sigma F_x}\right|, \quad \Sigma F_x = 0, \; \Sigma F_y = 0$$",
        "text": r"<strong>Parallelogram Law:</strong> $R = \sqrt{P^2 + Q^2 + 2PQ\cos\theta}$, $\tan\alpha = \frac{Q\sin\theta}{P + Q\cos\theta}$.<br><strong>Transmissibility Principle:</strong> Point of application can slide along line of action on a rigid body without altering external equilibrium.<br><strong>Cartesian Resolution:</strong> $R = \sqrt{(\Sigma F_x)^2 + (\Sigma F_y)^2}$.<br><strong>Equilibrium:</strong> Resultant must vanish ($\Sigma F_x = 0$, $\Sigma F_y = 0$)."
    },
    "mech-q2": {
        "eq": r"$$\frac{F_1}{\sin\alpha} = \frac{F_2}{\sin\beta} = \frac{F_3}{\sin\gamma}, \quad T = W \frac{l + r}{\sqrt{l^2 + 2lr}}, \quad R_w = W \frac{r}{\sqrt{l^2 + 2lr}}$$",
        "text": r"<strong>Lami's Theorem:</strong> For 3 concurrent coplanar forces in equilibrium, each force is proportional to the sine of the angle between the other two.<br><strong>Closed Triangle:</strong> Proved using the Sine Rule on the closed force triangle ($\Delta ABC$).<br><strong>Suspended Sphere:</strong> Normal reaction $R_w = W\tan\theta$, Tension $T = W/\cos\theta$ where $\sin\theta = \frac{r}{l+r}$."
    },
    "mech-q3": {
        "eq": r"$$R_{AB} = \frac{W_B}{\sin\theta} = 1250\text{ N}, \quad R_{wall} = 750\text{ N}, \quad R_{floor} = W_A + W_B = 2000\text{ N}$$",
        "text": r"<strong>Free Body Diagram (FBD):</strong> Isolate body and replace all supports with physical reactions.<br><strong>Line of Centers:</strong> Distance between centers $d = 2R$; horizontal span $\Delta x = L - 2R \implies \cos\theta = \Delta x / 2R$.<br><strong>Two Cylinders in Channel:</strong> Top cylinder equilibrium gives mutual contact reaction $R_{AB} = W/\sin\theta$ and wall reaction $R_{wall} = R_{AB}\cos\theta$."
    },
    "mech-q4": {
        "eq": r"$$\Sigma \mathbf{M}_O = \mathbf{r} \times \mathbf{R} \implies \sum_{i=1}^n F_i d_i = R \cdot d_R, \quad \mathbf{M}_{\text{couple}} = \mathbf{r}_{BA} \times \mathbf{F}$$",
        "text": r"<strong>Varignon's Theorem of Moments:</strong> The algebraic sum of moments of concurrent forces about any point equals the moment of their resultant about that point ($\Sigma M_O = M_{R, O}$).<br><strong>Couple Characteristics:</strong> Net force is zero; moment $M = F \cdot d$ is a free vector, identical about all points.<br><strong>Force Shift:</strong> Shifting force $F$ by perpendicular distance $d$ requires adding a couple $M = F \cdot d$."
    },
    "mech-q5": {
        "eq": r"$$\Sigma F_x = 0, \quad \Sigma F_y = 0, \quad \Sigma M_O = 0, \quad R = \sqrt{R_x^2 + R_y^2}$$",
        "text": r"<strong>2D Rigid Body Equilibrium:</strong> Requires 3 independent equations ($\Sigma F_x = 0, \Sigma F_y = 0, \Sigma M = 0$).<br><strong>Support Reactions:</strong><br>- Roller: 1 normal reaction ($R_N$).<br>- Pin/Hinged: 2 orthogonal reactions ($R_x, R_y$).<br>- Fixed: 3 reactions ($R_x, R_y, M_{\text{fix}}$).<br><strong>UDL Conversion:</strong> Replaced by equivalent point load $W = w \cdot L$ at segment centroid."
    },
    "mech-q6": {
        "eq": r"$$F_L = \mu_s N, \quad \tan\phi = \mu_s \implies \phi = \tan^{-1}\mu_s, \quad \theta_{\text{repose}} = \phi = \tan^{-1}\mu_s$$",
        "text": r"<strong>Coulomb's Friction Laws:</strong> Limiting friction $F_L = \mu_s N$ is independent of contact area; kinetic friction $\mu_k < \mu_s$.<br><strong>Angle of Friction ($\phi$):</strong> Angle between total reaction $R$ and normal $N$: $\tan\phi = \mu_s$.<br><strong>Angle of Repose ($\theta$):</strong> Maximum incline angle before sliding down under self-weight: $\tan\theta = \mu_s \implies \theta = \phi$.<br><strong>Cone of Friction:</strong> Inverted cone of semi-vertex angle $\phi$; forces inside cone cannot cause slip."
    },
    "mech-q7": {
        "eq": r"$$\tan\theta_{min} = \frac{1 - \mu_f \mu_w}{2\mu_f}, \quad \text{Smooth Wall: } \tan\theta_{min} = \frac{1}{2\mu_f}, \quad x_{max} = \frac{N_w L(\tan\theta + \mu_w) - \frac{W L}{2}}{W_1}$$",
        "text": r"<strong>Ladder Equilibrium:</strong> Floor friction $F_f = \mu_f N_f \rightarrow$, wall reaction $N_w \leftarrow$, wall friction $F_w = \mu_w N_w \uparrow$.<br><strong>Force Balance:</strong> $N_w = \mu_f N_f$, $N_f + \mu_w N_w = W \implies N_f = \frac{W}{1+\mu_f\mu_w}$.<br><strong>Minimum Angle:</strong> Taking $\Sigma M_A = 0$ yields $\tan\theta_{min} = \frac{1 - \mu_f\mu_w}{2\mu_f}$."
    },
    "mech-q8": {
        "eq": r"$$P = W \left[ \frac{\cos\phi_1}{\cos(\alpha + \phi_1 + \phi_2)} \right] \left[ \frac{\sin(\alpha + \phi_2 + \phi_3)}{\cos\phi_3} \right] \xrightarrow{\text{equal }\phi} P = W \tan(\alpha + 2\phi)$$",
        "text": r"<strong>Wedge Mechanism:</strong> Translates small horizontal effort $P$ into large vertical lifting force $W$.<br><strong>Block & Wedge Equilibrium:</strong> Reaction between block and wedge tilts by $(\alpha + \phi_2)$ to the vertical.<br><strong>Minimum Driving Force:</strong> $P = W\tan(\alpha + 2\phi)$ for equal friction angle $\phi$.<br><strong>Self-Locking:</strong> Wedge will not slip back when $P=0$ if $\alpha < 2\phi$."
    },
    "mech-q9": {
        "eq": r"$$\frac{T_1}{T_2} = e^{\mu \theta}, \quad P = (T_1 - T_2)v = T_1(1 - e^{-\mu\theta})v, \quad T_c = m v^2$$",
        "text": r"<strong>Flat Belt Tension Ratio:</strong> $\frac{T_1}{T_2} = e^{\mu\theta}$ where $\theta$ is wrap angle in radians.<br><strong>Power Transmitted:</strong> $P = (T_1 - T_2)v$ where pitch speed $v = \frac{\pi D N}{60}\text{ m/s}$.<br><strong>Centrifugal Tension:</strong> $T_c = m v^2$; reduces grip $\frac{T_1 - T_c}{T_2 - T_c} = e^{\mu\theta}$; maximum power occurs when $T_c = T_{max}/3$."
    },
    "mech-q10": {
        "eq": r"$$m = 2j - 3 \text{ (Perfect Truss)}, \quad \Sigma F_x = 0, \; \Sigma F_y = 0 \text{ (Joints)}, \quad \Sigma M_O = 0 \text{ (Sections)}$$",
        "text": r"<strong>Truss Assumptions:</strong> Frictionless pin joints, concurrent axes, axial loads only ($T$ tension or $C$ compression).<br><strong>Zero-Force Members:</strong> Two non-collinear members meeting at unloaded joint carry zero force; two collinear plus one third non-collinear $\implies$ third is zero.<br><strong>Method of Joints:</strong> Analyzes joint by joint ($\Sigma F_x=0, \Sigma F_y=0$).<br><strong>Method of Sections:</strong> Cuts across up to 3 members; solves with $\Sigma M_O = 0$."
    },
    "mech-q11": {
        "eq": r"$$\bar{x} = \frac{\sum A_i x_i}{\sum A_i}, \quad \bar{y} = \frac{\sum A_i y_i}{\sum A_i}, \quad Q_x = \int y \, dA = A \bar{y}$$",
        "text": r"<strong>Centroid of Area:</strong> Geometric center based on first moment of area: $A \bar{y} = \Sigma A_i y_i$.<br><strong>Axis of Symmetry:</strong> If a section possesses an axis of symmetry, the centroid must lie on that axis.<br><strong>Composite T-Section:</strong> Web ($20\times 180$) and Flange ($150\times 20$) give total area $6600\text{ mm}^2$ and $\bar{y} = \frac{894,000}{6600} = 135.45\text{ mm}$ from base."
    },
    "mech-q12": {
        "eq": r"$$A = 2\pi \bar{y} L \quad (\text{Theorem 1}), \quad V = 2\pi \bar{y} A \quad (\text{Theorem 2})$$",
        "text": r"<strong>Pappus Theorem 1:</strong> Surface area of revolution equals curve length $L$ times distance traveled by its centroid ($2\pi \bar{y} L$).<br><strong>Pappus Theorem 2:</strong> Volume of revolution equals plane area $A$ times distance traveled by its centroid ($2\pi \bar{y} A$).<br><strong>Applications:</strong> Sphere ($A = 4\pi R^2, V = \frac{4}{3}\pi R^3$), Cone ($V = \frac{1}{3}\pi R^2 h$)."
    },
    "mech-q13": {
        "eq": r"$$I_{AB} = I_G + A d^2 \quad (\text{Parallel Axis}), \quad I_{zz} = I_{xx} + I_{yy} \quad (\text{Perpendicular Axis})$$",
        "text": r"<strong>Parallel Axis Theorem:</strong> $I_{AB} = I_G + A d^2$; first moment $\int y' dA = 0$ about centroid.<br><strong>Perpendicular Axis Theorem:</strong> $I_{zz} = I_{xx} + I_{yy}$; valid strictly for planar 2D laminas.<br><strong>Radius of Gyration:</strong> $k = \sqrt{I/A} \implies I = A k^2$."
    },
    "mech-q14": {
        "eq": r"$$I_{xx} = \sum \left( \frac{b_i h_i^3}{12} + A_i d_i^2 \right) \approx 54.82 \times 10^6\text{ mm}^4, \quad I_{yy} = \sum \frac{h_i b_i^3}{12} \approx 16.26 \times 10^6\text{ mm}^4$$",
        "text": r"<strong>I-Section Centroidal MOI:</strong> Calculate $\bar{y}$ using first moments, then apply parallel axis theorem to each rectangle: $I_{xx} = I_G + A d^2$.<br><strong>Symmetry about Y-Axis:</strong> All $d_x = 0 \implies I_{yy} = \sum \frac{h b^3}{12}$.<br><strong>Radii of Gyration:</strong> $k_{xx} = \sqrt{I_{xx}/A} \approx 78.93\text{ mm}$, $k_{yy} = \sqrt{I_{yy}/A} \approx 42.98\text{ mm}$."
    },
    "mech-q15": {
        "eq": r"$$I_{\text{rod}, G} = \frac{1}{12} m L^2, \quad I_{\text{rod}, \text{end}} = \frac{1}{3} m L^2, \quad I_{\text{disc}, z} = \frac{1}{2} m R^2, \quad I_{\text{disc}, d} = \frac{1}{4} m R^2$$",
        "text": r"<strong>Mass Moment of Inertia:</strong> $I = \int r^2 dm$, measures resistance to angular acceleration ($T = I \alpha$).<br><strong>Slender Rod:</strong> Centroidal transverse axis $I_G = \frac{1}{12} m L^2$; about one end $I = I_G + m(L/2)^2 = \frac{1}{3} m L^2$.<br><strong>Circular Disc:</strong> Polar axis $I_z = \frac{1}{2} m R^2$; diameter axis $I_d = \frac{1}{4} m R^2$ (perpendicular axis theorem)."
    },
    "mech-q16": {
        "eq": r"$$a = \frac{dv}{dt} = v \frac{dv}{ds}, \quad a = -k v \implies v(t) = v_0 e^{-k t}, \quad s(t) = \frac{v_0}{k}(1 - e^{-k t}), \quad s_{max} = \frac{v_0}{k}$$",
        "text": r"<strong>Variable Acceleration:</strong> Use $v = ds/dt$, $a = dv/dt$, or $v \, dv = a \, ds$ based on independent variables.<br><strong>Linear Drag ($a = -kv$):</strong> Velocity decays exponentially $v = v_0 e^{-kt}$.<br><strong>Stopping Distance:</strong> Particle comes to rest asymptotically with total distance $s_{max} = v_0/k$."
    },
    "mech-q17": {
        "eq": r"$$y = x \tan\theta - \frac{g x^2}{2 u^2 \cos^2\theta}, \quad T = \frac{2 u \sin\theta}{g}, \quad H = \frac{u^2 \sin^2\theta}{2g}, \quad R = \frac{u^2 \sin(2\theta)}{g}$$",
        "text": r"<strong>Parabolic Trajectory:</strong> Eliminating time $t$ gives $y = x\tan\theta - \frac{gx^2}{2u^2\cos^2\theta}$.<br><strong>Time of Flight:</strong> $T = \frac{2u\sin\theta}{g}$ ($y=0$).<br><strong>Max Height:</strong> $H = \frac{u^2\sin^2\theta}{2g}$ ($v_y=0$).<br><strong>Horizontal Range:</strong> $R = \frac{u^2\sin 2\theta}{g}$; maximum range occurs at $\theta = 45^\circ$ ($R_{max} = u^2/g$)."
    },
    "mech-q18": {
        "eq": r"$$\mathbf{a} = a_t \hat{\mathbf{e}}_t + a_n \hat{\mathbf{e}}_n = \frac{dv}{dt} \hat{\mathbf{e}}_t + \frac{v^2}{\rho} \hat{\mathbf{e}}_n, \quad a = \sqrt{a_t^2 + a_n^2}$$",
        "text": r"<strong>Tangential Acceleration ($a_t$):</strong> $a_t = \frac{dv}{dt} = v\frac{dv}{ds}$, measures rate of change of speed along path tangent.<br><strong>Normal Acceleration ($a_n$):</strong> $a_n = \frac{v^2}{\rho}$, measures rate of change of direction, always directed inward toward center of curvature.<br><strong>Curvature:</strong> $\rho$ is radius of curvature; $a_n = 0$ only for straight path ($\rho \to \infty$)."
    },
    "mech-q19": {
        "eq": r"$$\Sigma \mathbf{F} + (-m \mathbf{a}) = 0 \implies \Sigma \mathbf{F} + \mathbf{F}_i = 0, \quad a = \left(\frac{m_1 - m_2}{m_1 + m_2}\right) g, \quad T = \left(\frac{2 m_1 m_2}{m_1 + m_2}\right) g$$",
        "text": r"<strong>D'Alembert's Principle:</strong> Dynamic systems brought to static equilibrium by adding reverse inertia force $\mathbf{F}_i = -m\mathbf{a}$.<br><strong>Accelerating Elevator:</strong> Upward $\implies N = m(g+a)$; Downward $\implies N = m(g-a)$; Free fall $\implies N = 0$.<br><strong>Atwood Machine:</strong> Common acceleration $a = \frac{m_1 - m_2}{m_1 + m_2}g$, string tension $T = \frac{2m_1 m_2}{m_1 + m_2}g$."
    },
    "mech-q20": {
        "eq": r"$$a = \frac{m_2 - m_1(\sin\alpha + \mu \cos\alpha)}{m_1 + m_2} g, \quad T = \frac{m_1 m_2 g}{m_1 + m_2}(1 + \sin\alpha + \mu \cos\alpha)$$",
        "text": r"<strong>Connected Incline Dynamics:</strong> Normal reaction $N = m_1 g \cos\alpha$; friction $F_k = \mu m_1 g \cos\alpha$.<br><strong>Force Balance:</strong> $T - m_1 g\sin\alpha - \mu m_1 g\cos\alpha = m_1 a$, and $m_2 g - T = m_2 a$.<br><strong>Motion Threshold:</strong> Mass accelerates up incline only if $m_2 > m_1(\sin\alpha + \mu\cos\alpha)$."
    },
    "mech-q21": {
        "eq": r"$$U_{1-2} = \int_1^2 \mathbf{F} \cdot d\mathbf{r} = T_2 - T_1 = \frac{1}{2} m v_2^2 - \frac{1}{2} m v_1^2 = \Delta KE$$",
        "text": r"<strong>Work Done:</strong> $U = \int \mathbf{F}\cdot d\mathbf{r}$; Gravity $U_g = -mg(y_2 - y_1)$; Spring $U_s = -\frac{1}{2}k(x_2^2 - x_1^2)$.<br><strong>Work-Energy Theorem:</strong> $F_t = m v \frac{dv}{ds} \implies \int F_t ds = \int mv dv \implies U_{1-2} = T_2 - T_1$.<br><strong>Key Advantage:</strong> Directly links force and displacement without calculating elapsed time."
    },
    "mech-q22": {
        "eq": r"$$\oint \mathbf{F}\cdot d\mathbf{r} = 0, \quad \mathbf{F} = -\nabla V, \quad T_1 + V_1 = T_2 + V_2 = E_{\text{total}} = \text{constant}$$",
        "text": r"<strong>Conservative Force:</strong> Work done is path-independent ($\nabla \times \mathbf{F} = 0$); derived from potential $F = -\nabla V$.<br><strong>Conservation of Mechanical Energy:</strong> When non-conservative forces do no work, $T_1 + V_1 = T_2 + V_2$.<br><strong>Simple Pendulum:</strong> Velocity at angle $\theta$ is $v = \sqrt{2gl(\cos\theta - \cos\theta_0)}$; cord tension does zero work."
    },
    "mech-q23": {
        "eq": r"$$\mathbf{J}_{1-2} = \int_{t_1}^{t_2} \mathbf{F} \, dt = m \mathbf{v}_2 - m \mathbf{v}_1 = \Delta \mathbf{p}, \quad R_{jet, x} = \rho A v^2 (1 - \cos\beta)$$",
        "text": r"<strong>Linear Impulse:</strong> $\mathbf{J} = \int \mathbf{F} dt = \Delta(m\mathbf{v})$; equals area under $F-t$ curve.<br><strong>Impulsive Forces:</strong> Large forces over tiny $\Delta t$; gravity/friction neglected during impact.<br><strong>Fluid Jet on Vane:</strong> Force on fluid is $\dot{m}(\mathbf{v}_{out} - \mathbf{v}_{in})$; jet force on semicircular cup ($\beta = 180^\circ$) is $2\rho A v^2$."
    },
    "mech-q24": {
        "eq": r"$$\Sigma \mathbf{F}^{ext} = \frac{d\mathbf{P}}{dt} = 0 \implies \mathbf{P} = \sum m_i \mathbf{v}_i = \text{constant}, \quad V_R = -\left(\frac{m}{M}\right) v_b$$",
        "text": r"<strong>Linear Momentum Conservation:</strong> Internal forces cancel in pairs ($\Sigma \mathbf{f}_{ij} = 0$). If $\Sigma \mathbf{F}^{ext} = 0$, total momentum is conserved.<br><strong>Recoil Velocity:</strong> Firing projectile with muzzle speed $v_b$ imparts cannon recoil $V_R = -(m/M)v_b$.<br><strong>Generality:</strong> Strictly conserved regardless of whether mechanical energy is lost."
    },
    "mech-q25": {
        "eq": r"$$e = \frac{v_2 - v_1}{u_1 - u_2}, \quad v_1 = \frac{(m_1 - e m_2)u_1 + m_2(1+e)u_2}{m_1 + m_2}, \quad v_2 = \frac{m_1(1+e)u_1 + (m_2 - e m_1)u_2}{m_1 + m_2}$$",
        "text": r"<strong>Direct Central Impact:</strong> Centers of mass and velocities lie along the normal line of impact.<br><strong>Restitution Coefficient ($e$):</strong> $e = \frac{\text{Separation Velocity}}{\text{Approach Velocity}} = \frac{v_2 - v_1}{u_1 - u_2}$.<br><strong>Special Cases:</strong> Elastic ($e = 1$) $\implies$ equal masses exchange velocities; Plastic ($e = 0$) $\implies$ bodies coalesce with common velocity."
    },
    "mech-q26": {
        "eq": r"$$\Delta E = \frac{m_1 m_2}{2(m_1 + m_2)} (1 - e^2) (u_1 - u_2)^2 = \frac{1}{2} \mu (1 - e^2) (u_1 - u_2)^2$$",
        "text": r"<strong>Loss of Kinetic Energy:</strong> $\Delta E = E_{initial} - E_{final} = \frac{m_1 m_2}{2(m_1 + m_2)}(1 - e^2)(u_1 - u_2)^2$.<br><strong>Reduced Mass:</strong> $\mu = \frac{m_1 m_2}{m_1 + m_2}$.<br><strong>Regimes:</strong><br>- Perfectly Elastic ($e = 1$): $\Delta E = 0$ (energy conserved).<br>- Inelastic ($0 < e < 1$): $\Delta E > 0$ (dissipated as heat/sound).<br>- Perfectly Plastic ($e = 0$): Maximum energy loss."
    }
}

MECHANICS_EXAM_QUESTIONS = {
    "mech-q1": "State the Parallelogram Law of Forces and the Principle of Transmissibility of Forces. Explain the analytical method of resolving a system of coplanar concurrent forces to find the resultant and state the conditions of static equilibrium.",
    "mech-q2": "State and prove Lami's Theorem using the sine rule on a force triangle. Apply Lami's theorem to find the cord tension and wall reaction for a smooth sphere of weight W suspended against a vertical wall.",
    "mech-q3": "What is a Free Body Diagram (FBD)? Explain the steps to construct an FBD. Two smooth identical cylinders of weight W and radius R rest in a rectangular channel of width L. Determine all contact reactions.",
    "mech-q4": "State and prove Varignon's Theorem of Moments for a system of coplanar concurrent forces. Define a couple, list its characteristics, and explain how a force can be replaced by an equivalent force-couple system.",
    "mech-q5": "State the equations of static equilibrium of a rigid body in two dimensions. Classify common structural supports and determine the support reactions for a simply supported beam carrying a UDL, inclined point load, and concentrated couple.",
    "mech-q6": "State Coulomb's laws of dry friction. Define the terms: static friction, limiting friction, kinetic friction, angle of friction, angle of repose, and cone of friction. Prove that the angle of repose is equal to the angle of friction.",
    "mech-q7": "A uniform ladder of length L and weight W rests against a rough vertical wall and a rough horizontal floor. Formulate the equilibrium equations, derive the expression for the minimum inclination angle to prevent slipping, and determine the maximum distance a person can climb.",
    "mech-q8": "Explain the working principle of a wedge for raising heavy loads. Draw the free body diagrams of the block and wedge system and derive the formula for the minimum horizontal driving force P required to raise the load.",
    "mech-q9": "Derive the formula for the ratio of belt tensions T1/T2 = e^(mu*theta) for a flat belt passing over a fixed cylindrical pulley. Obtain the expression for the power transmitted by the belt and discuss the effect of centrifugal tension.",
    "mech-q10": "State the assumptions in the analysis of pin-jointed trusses. State the conditions for a truss to be perfect, deficient, or redundant. State the rules for identifying zero-force members by inspection and explain the Method of Joints and Method of Sections.",
    "mech-q11": "Define the first moment of area and centroid of a composite plane area. Derive the centroid formulas and determine the centroid coordinates of an unsymmetrical T-section.",
    "mech-q12": "State and prove Pappus-Guldinus Theorem 1 (Surface Area of Revolution) and Theorem 2 (Volume of Revolution). Use these theorems to calculate the surface area and volume of a sphere and a right circular cone.",
    "mech-q13": "Define area moment of inertia, polar moment of inertia, and radius of gyration. State and prove the Parallel Axis Theorem (Steiner's Theorem) and the Perpendicular Axis Theorem for area moment of inertia.",
    "mech-q14": "Determine the centroidal moments of inertia Ixx and Iyy and the radii of gyration kxx and kyy for an unsymmetrical I-section with given flange and web dimensions.",
    "mech-q15": "Define mass moment of inertia and radius of gyration. Derive the mass moment of inertia of a uniform slender rod of mass m and length L about its centroidal transverse axis and one end, and of a thin circular disc about its polar and diameter axes.",
    "mech-q16": "Formulate the kinematic equations for rectilinear motion with variable acceleration. Solve the equation of motion for a particle subjected to a resisting drag force proportional to velocity (a = -kv) and determine the velocity, displacement, and total distance traveled.",
    "mech-q17": "Derive the parabolic trajectory equation for an unresisted projectile launched with initial velocity u at angle theta. Derive expressions for the time of flight, maximum vertical height, and horizontal range, and obtain the condition for maximum range.",
    "mech-q18": "Derive the expressions for the normal and tangential components of acceleration for a particle executing curvilinear planar motion. Explain the physical significance of each component.",
    "mech-q19": "State Newton's Second Law of Motion and D'Alembert's Principle of dynamic equilibrium. Apply D'Alembert's principle to analyze the apparent weight in an accelerating elevator and determine the acceleration and cord tension in an Atwood machine.",
    "mech-q20": "Formulate the equations of dynamic motion for two connected bodies where one body moves along a rough inclined plane and is connected by a cord over a pulley to a hanging body. Derive expressions for the common acceleration and cord tension.",
    "mech-q21": "Define work done by a force and derive expressions for work done by gravity and spring forces. Derive the Work-Energy Theorem for a particle moving under a variable force.",
    "mech-q22": "Define a conservative force and state its criteria. Define potential energy and prove the Law of Conservation of Mechanical Energy. Apply it to find the velocity of an oscillating simple pendulum.",
    "mech-q23": "State and derive the Linear Impulse-Momentum Principle from Newton's second law. Explain impulsive forces and derive the dynamic force exerted by a high-velocity fluid jet striking a curved vane.",
    "mech-q24": "State and prove the Principle of Conservation of Linear Momentum for a system of interacting particles. Apply the principle to determine the recoil velocity of an artillery gun firing a shell.",
    "mech-q25": "Define direct central impact and coefficient of restitution. Derive expressions for the post-collision velocities v1 and v2 of two colliding bodies in terms of their masses, initial velocities, and coefficient of restitution.",
    "mech-q26": "Derive the complete mathematical expression for the loss of kinetic energy during direct central inelastic impact of two bodies: Delta E = (m1*m2)/(2*(m1+m2)) * (1 - e^2) * (u1 - u2)^2. Discuss perfectly elastic, inelastic, and plastic collisions."
}
