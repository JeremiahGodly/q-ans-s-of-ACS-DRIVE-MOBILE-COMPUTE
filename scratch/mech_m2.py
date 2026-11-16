# -*- coding: utf-8 -*-
"""
Module 2: Friction and Trusses (mech-q6 to mech-q10)
KTU 2019 Scheme Engineering Mechanics (EST100)
"""

MODULE_2 = {
    "module_id": "mech-m2",
    "module_num": "Module 2",
    "module_title": "Friction, Belt Friction, Wedges and Pin-Jointed Trusses",
    "questions": [
        {
            "qid": "mech-q6",
            "marks": 7,
            "type": "Theory & Derivation",
            "title": "Coulomb's Laws of Dry Friction: Angle of Friction, Angle of Repose, and Cone of Friction",
            "yt_query": "laws of dry friction angle of friction angle of repose cone of friction engineering mechanics",
            "img_path": "images/mechanics/friction_laws_cone.png",
            "img_caption": "Figure 2.1: Limiting Static Friction, Total Reaction Angle, and Cone of Friction Geometry",
            "answer": r"""
Friction is the tangential contact resisting force that develops between two solid contacting surfaces when one surface slides or tends to slide across the other. Formulated empirically by Guillaume Amontons and Charles-Augustin de Coulomb, dry friction (Coulomb friction) arises from microscopic surface asperities interlocking and adhesion bonds forming across real contact areas.

Classification of Dry Friction:
1. Static Friction ($F_s$): The resisting tangential force that exists between two contacting bodies when there is an impending tendency to slide, but actual relative motion has not yet initiated. Static friction is a self-adjusting force: as the tangential disturbing force $P$ increases, the static friction force $F_s$ increases proportionally in magnitude and opposes $P$ to maintain static equilibrium ($F_s = P$).
2. Limiting Friction ($F_{max}$ or $F_L$): The maximum possible value that static friction can attain just before relative sliding motion begins. It represents the boundary threshold between rest and motion.
3. Kinetic (Dynamic) Friction ($F_k$): The resisting frictional force operating between surfaces in active relative sliding motion. Once motion initiates, the interlocking asperities are sheared off or ride over one another, causing kinetic friction to drop to a value lower than the limiting static friction ($F_k < F_{max}$).

Coulomb's Laws of Dry Friction:
1. First Law: The limiting friction force $F_L$ is directly proportional to the normal reaction force $N$ pressing the contacting surfaces together:
$$F_L = \mu_s N$$
where $\mu_s$ is the dimensionless Coefficient of Static Friction.
2. Second Law: For surfaces in relative motion, the kinetic friction force $F_k$ is directly proportional to the normal reaction force:
$$F_k = \mu_k N$$
where $\mu_k$ is the Coefficient of Kinetic Friction, with $\mu_k < \mu_s$.
3. Third Law: The frictional force is independent of the apparent geometric area of contact, depending only on the actual microscopic contact area (which is governed by normal load $N$).
4. Fourth Law: Kinetic friction is largely independent of relative sliding velocity at low to moderate speeds.

Angle of Friction ($\phi$):
At limiting equilibrium, the contacting surface exerts two simultaneous forces on a body: the normal reaction $N$ perpendicular to the contact interface, and the limiting friction force $F_L = \mu_s N$ tangential to the interface.
The resultant of these two forces is the Total Reaction $\mathbf{R}$:
$$R = \sqrt{N^2 + F_L^2} = \sqrt{N^2 + (\mu_s N)^2} = N \sqrt{1 + \mu_s^2}$$
The Angle of Friction $\phi$ is defined as the angle that the total resultant reaction $\mathbf{R}$ makes with the normal reaction $N$ at the instant of limiting equilibrium:
$$\tan\phi = \frac{F_L}{N} = \frac{\mu_s N}{N} = \mu_s \implies \phi = \tan^{-1}(\mu_s)$$

Angle of Repose ($\theta$):
The Angle of Repose $\theta$ is defined as the maximum angle of inclination of a rough plane with the horizontal at which a body placed upon it will remain at rest in limiting equilibrium under the action of its own weight alone, without sliding downward.
Proof that Angle of Repose equals Angle of Friction ($\theta = \phi$):
Consider a body of weight $W$ resting on a rough plane inclined at angle $\theta$ to the horizontal.
Resolving the weight $W$ along and perpendicular to the inclined plane:
- Component perpendicular to the incline: $W \cos\theta$
- Component parallel to the incline acting downward: $W \sin\theta$
Setting up equations of limiting equilibrium:
Perpendicular to incline ($\Sigma F_y = 0$):
$$N = W \cos\theta$$
Along the incline ($\Sigma F_x = 0$):
$$F_L - W \sin\theta = 0 \implies F_L = W \sin\theta$$
Since the body is at limiting equilibrium, $F_L = \mu_s N$:
$$W \sin\theta = \mu_s (W \cos\theta)$$
Dividing both sides by $W \cos\theta$:
$$\tan\theta = \mu_s$$
Since we established earlier that $\mu_s = \tan\phi$ (where $\phi$ is the angle of friction):
$$\tan\theta = \tan\phi \implies \theta = \phi$$
This proves that the angle of repose is identically equal to the angle of friction.

Cone of Friction:
When an external disturbing force tends to move a body in various directions across a horizontal plane, the limiting friction force $F_L$ always acts in the opposite direction. Consequently, the total reaction vector $\mathbf{R}$ tilts by angle $\phi$ away from the normal reaction $N$ in whichever direction motion is impending.
If the direction of impending motion rotates through a full circle of $360^\circ$ around the contact point, the total reaction vector $\mathbf{R}$ sweeps out a right circular inverted cone called the Cone of Friction.
- The vertex of the cone is located at the point of contact.
- The axis of the cone aligns with the normal reaction $N$.
- The semi-vertex angle of the cone is the angle of friction $\phi = \tan^{-1}\mu_s$.
Significance: If the resultant applied force falls inside the cone of friction, motion is physically impossible regardless of the magnitude of the force (self-locking condition).
"""
        },
        {
            "qid": "mech-q7",
            "marks": 7,
            "type": "Derivation & Application",
            "title": "Ladder Friction: Equilibrium Equations, Minimum Angle, and Maximum Climbing Distance",
            "yt_query": "ladder friction equilibrium derivation minimum angle maximum distance climbed engineering mechanics",
            "img_path": "images/mechanics/ladder_friction.png",
            "img_caption": "Figure 2.2: Free Body Diagram of Ladder Resting Against Rough Wall and Rough Floor",
            "answer": r"""
A ladder resting against a vertical wall and a horizontal floor is a classic problem in engineering mechanics involving two frictional contacts simultaneously. When the ladder tends to slip, the bottom foot slides horizontally outward away from the wall, while the top end slides vertically downward along the wall.

Formulation of Free Body Diagram and Governing Equations:
Consider a uniform ladder $AB$ of length $L$ and weight $W$ resting with its lower end $A$ on a rough horizontal floor (coefficient of friction $\mu_f$) and its upper end $B$ against a rough vertical wall (coefficient of friction $\mu_w$). The ladder is inclined at an angle $\theta$ to the horizontal floor. Let the uniform weight $W$ act downward through the ladder's midpoint $G$ at distance $L/2$ from $A$.

At bottom end $A$ (impending slip is to the left):
- Normal floor reaction $N_f$ acting vertically upward ($\uparrow$).
- Frictional floor force $F_f = \mu_f N_f$ acting horizontally toward the wall ($\rightarrow$).
At top end $B$ (impending slip is downward):
- Normal wall reaction $N_w$ acting horizontally outward from the wall ($\leftarrow$).
- Frictional wall force $F_w = \mu_w N_w$ acting vertically upward along the wall ($\uparrow$).

Applying Equations of Static Equilibrium:
1. Horizontal Force Equilibrium ($\Sigma F_x = 0$):
Taking rightward forces as positive:
$$F_f - N_w = 0 \implies N_w = F_f = \mu_f N_f \quad \text{--- (Equation 1)}$$
2. Vertical Force Equilibrium ($\Sigma F_y = 0$):
Taking upward forces as positive:
$$N_f + F_w - W = 0 \implies N_f + \mu_w N_w = W \quad \text{--- (Equation 2)}$$
Substituting Equation 1 ($N_w = \mu_f N_f$) into Equation 2:
$$N_f + \mu_w (\mu_f N_f) = W \implies N_f (1 + \mu_f \mu_w) = W$$
Solving for the normal floor reaction:
$$N_f = \frac{W}{1 + \mu_f \mu_w}$$
Substituting $N_f$ back into Equation 1 yields the normal wall reaction:
$$N_w = \frac{\mu_f W}{1 + \mu_f \mu_w}$$
The wall friction is:
$$F_w = \mu_w N_w = \frac{\mu_f \mu_w W}{1 + \mu_f \mu_w}$$

Derivation of Minimum Inclination Angle ($\theta_{min}$):
To establish the threshold angle of inclination $\theta$ below which the ladder will slip, we take moments of all forces about the base pivot $A$ ($\Sigma M_A = 0$):
Taking counter-clockwise moments as positive ($+ \circlearrowleft$):
- Moment of ladder weight $W$: Clockwise about $A$ with moment arm $\frac{L}{2}\cos\theta$:
$$M_W = -W \left(\frac{L}{2}\cos\theta\right)$$
- Moment of normal wall reaction $N_w$: Counter-clockwise about $A$ with vertical moment arm $L\sin\theta$:
$$M_{Nw} = +N_w (L\sin\theta)$$
- Moment of wall friction $F_w$: Counter-clockwise about $A$ with horizontal moment arm $L\cos\theta$:
$$M_{Fw} = +F_w (L\cos\theta)$$
Summing moments about base $A$:
$$\Sigma M_A = N_w L\sin\theta + F_w L\cos\theta - W \frac{L}{2}\cos\theta = 0$$
Dividing throughout by $L$:
$$N_w \sin\theta + F_w \cos\theta = \frac{W}{2}\cos\theta$$
Dividing throughout by $\cos\theta$ (since $\cos\theta \neq 0$):
$$N_w \tan\theta + F_w = \frac{W}{2} \implies N_w \tan\theta = \frac{W}{2} - F_w$$
Substituting the derived expressions for $N_w$ and $F_w$:
$$\left(\frac{\mu_f W}{1 + \mu_f \mu_w}\right)\tan\theta = \frac{W}{2} - \frac{\mu_f \mu_w W}{1 + \mu_f \mu_w} = W \left[ \frac{1 + \mu_f \mu_w - 2\mu_f \mu_w}{2(1 + \mu_f \mu_w)} \right] = W \left[ \frac{1 - \mu_f \mu_w}{2(1 + \mu_f \mu_w)} \right]$$
Canceling the common term $\frac{W}{1 + \mu_f \mu_w}$ from both sides:
$$\mu_f \tan\theta = \frac{1 - \mu_f \mu_w}{2}$$
Solving for $\tan\theta$:
$$\tan\theta_{min} = \frac{1 - \mu_f \mu_w}{2\mu_f} \implies \theta_{min} = \tan^{-1}\left(\frac{1 - \mu_f \mu_w}{2\mu_f}\right)$$
Special Case (Smooth Vertical Wall, $\mu_w = 0$):
$$\tan\theta_{min} = \frac{1 - (0)}{2\mu_f} = \frac{1}{2\mu_f}$$

Maximum Distance a Person Can Climb Before Slipping:
Consider a person of weight $W_1$ climbing up the ladder at inclination $\theta$. Let $x$ be the distance climbed along the ladder from base $A$.
The new vertical equilibrium equation is:
$$N_f + \mu_w N_w = W + W_1 \implies N_f = \frac{W + W_1}{1 + \mu_f \mu_w}$$
$$N_w = \mu_f N_f = \frac{\mu_f (W + W_1)}{1 + \mu_f \mu_w}$$
Taking moments about base $A$ with the person at distance $x$:
$$N_w L\sin\theta + \mu_w N_w L\cos\theta - W \left(\frac{L}{2}\cos\theta\right) - W_1 (x\cos\theta) = 0$$
Dividing by $\cos\theta$:
$$N_w L\tan\theta + \mu_w N_w L - W \frac{L}{2} - W_1 x = 0$$
Solving for the maximum safe climbing distance $x_{max}$:
$$x_{max} = \frac{N_w L (\tan\theta + \mu_w) - \frac{W L}{2}}{W_1}$$
If $x_{max} \ge L$, the person can climb to the top of the ladder safely without slipping.
"""
        },
        {
            "qid": "mech-q8",
            "marks": 7,
            "type": "Theory & Application",
            "title": "Wedge Friction: Mechanical Advantage, Equilibrium Analysis, and Force Formulation",
            "yt_query": "wedge friction equilibrium derivation minimum horizontal force engineering mechanics",
            "img_path": "images/mechanics/wedge_friction.png",
            "img_caption": "Figure 2.3: Free Body Diagrams for Raising a Heavy Load W Using a Slender Wedge of Angle Alpha",
            "answer": r"""
A wedge is an inclined plane machine used in engineering practice to lift heavy machinery loads, make small vertical adjustments, or split materials through the application of a comparatively small transverse effort. Because of high frictional resistance along sliding faces, wedges possess the desirable property of being self-locking, meaning the lifted load does not slide back down when the driving effort is removed.

Problem Description and System Geometry:
Consider a heavy block of weight $W$ constrained to move strictly in the vertical direction by smooth or rough vertical guides. The block is lifted by driving a slender wedge of self-weight $w$ (often negligible, $w \approx 0$) and wedge angle $\alpha$ horizontally underneath it by applying an external horizontal driving force $P$.
Let the friction coefficients be:
- $\mu_1 = \tan\phi_1$ along the vertical guide wall.
- $\mu_2 = \tan\phi_2$ along the inclined contact interface between block and wedge.
- $\mu_3 = \tan\phi_3$ along the horizontal ground surface supporting the wedge.
To analyze this system, we separate the assembly into two distinct free body diagrams: one for the vertical block and one for the horizontal wedge.

1. Equilibrium of the Vertical Block (Lifting Mode):
The block moves vertically upward ($\uparrow$).
Forces acting on the block:
- Downward weight $W$ ($\downarrow$).
- Normal reaction $N_1$ from the vertical wall acting horizontally to the right ($\rightarrow$).
- Frictional force $F_1 = \mu_1 N_1$ along the vertical wall acting vertically downward ($\downarrow$) opposing upward motion.
- Contact normal reaction $N_2$ perpendicular to the inclined face of the wedge, acting at angle $\alpha$ to the vertical.
- Frictional force $F_2 = \mu_2 N_2$ along the inclined interface, directed downward and to the right along the slope ($\searrow$) opposing the relative motion of the block sliding up the wedge.

The normal reaction $N_2$ and friction $F_2$ combine into a single Total Reaction $R_2$ inclined at angle $(\alpha + \phi_2)$ to the vertical, where $\phi_2 = \tan^{-1}\mu_2$.
Similarly, $N_1$ and $F_1$ combine into total reaction $R_1$ inclined at angle $\phi_1$ below the horizontal.
Applying equations of equilibrium for the block:
$$\Sigma F_x = 0 \implies N_1 - N_2 \sin\alpha - \mu_2 N_2 \cos\alpha = 0$$
$$\Sigma F_y = 0 \implies N_2 \cos\alpha - \mu_2 N_2 \sin\alpha - \mu_1 N_1 - W = 0$$
Expressing these in terms of total reactions:
Resolving horizontally and vertically:
$$R_1 \cos\phi_1 = R_2 \sin(\alpha + \phi_2) \implies R_1 = R_2 \frac{\sin(\alpha + \phi_2)}{\cos\phi_1}$$
Vertical balance:
$$R_2 \cos(\alpha + \phi_2) - R_1 \sin\phi_1 - W = 0$$
Substituting $R_1$:
$$R_2 \cos(\alpha + \phi_2) - R_2 \frac{\sin(\alpha + \phi_2)\sin\phi_1}{\cos\phi_1} = W$$
$$R_2 \left[ \frac{\cos(\alpha + \phi_2)\cos\phi_1 - \sin(\alpha + \phi_2)\sin\phi_1}{\cos\phi_1} \right] = W$$
Using the trigonometric identity $\cos(A + B) = \cos A \cos B - \sin A \sin B$:
$$R_2 \frac{\cos(\alpha + \phi_1 + \phi_2)}{\cos\phi_1} = W \implies R_2 = W \frac{\cos\phi_1}{\cos(\alpha + \phi_1 + \phi_2)}$$

2. Equilibrium of the Horizontal Wedge:
The wedge moves horizontally to the left ($\leftarrow$) under applied horizontal force $P$.
Forces acting on the wedge:
- Applied horizontal driving force $P$ acting to the left ($\leftarrow$).
- Mutual contact reaction from the block: by Newton's third law, this is $R_2$, directed downward and to the left at angle $(\alpha + \phi_2)$ to the vertical.
- Ground normal reaction $N_3$ acting vertically upward ($\uparrow$).
- Ground friction force $F_3 = \mu_3 N_3$ acting to the right ($\rightarrow$) opposing motion.
$N_3$ and $F_3$ combine into the total ground reaction $R_3$ inclined at friction angle $\phi_3$ to the vertical.

Setting up force balance for the wedge:
Resolving all forces along the horizontal and vertical axes:
$$\Sigma F_y = 0 \implies R_3 \cos\phi_3 - R_2 \cos(\alpha + \phi_2) = 0 \implies R_3 = R_2 \frac{\cos(\alpha + \phi_2)}{\cos\phi_3}$$
$$\Sigma F_x = 0 \implies P - R_2 \sin(\alpha + \phi_2) - R_3 \sin\phi_3 = 0$$
$$P = R_2 \sin(\alpha + \phi_2) + R_3 \sin\phi_3$$
Substituting $R_3$:
$$P = R_2 \sin(\alpha + \phi_2) + R_2 \frac{\cos(\alpha + \phi_2)\sin\phi_3}{\cos\phi_3} = R_2 \left[ \frac{\sin(\alpha + \phi_2)\cos\phi_3 + \cos(\alpha + \phi_2)\sin\phi_3}{\cos\phi_3} \right]$$
Using $\sin(A + B) = \sin A \cos B + \cos A \sin B$:
$$P = R_2 \frac{\sin(\alpha + \phi_2 + \phi_3)}{\cos\phi_3}$$
Now substituting the derived expression for $R_2$ from block equilibrium:
$$P = W \left[ \frac{\cos\phi_1}{\cos(\alpha + \phi_1 + \phi_2)} \right] \left[ \frac{\sin(\alpha + \phi_2 + \phi_3)}{\cos\phi_3} \right]$$

Special Case (Uniform Friction Coefficient $\phi_1 = \phi_2 = \phi_3 = \phi$):
$$P = W \frac{\cos\phi \sin(\alpha + 2\phi)}{\cos\phi \cos(\alpha + 2\phi)} = W \tan(\alpha + 2\phi)$$
This simple formula gives the minimum horizontal force required to drive the wedge and lift the load $W$.

Condition for Self-Locking of the Wedge:
When the driving force $P$ is completely removed ($P = 0$), the wedge will remain locked in position without being pushed backward by load $W$ provided the friction forces are sufficient. The condition for self-locking is:
$$\alpha < \phi_2 + \phi_3 \quad \text{or for equal friction: } \alpha < 2\phi$$
If the wedge angle $\alpha$ is smaller than the sum of friction angles, the wedge is self-locking.
"""
        },
        {
            "qid": "mech-q9",
            "marks": 7,
            "type": "Derivation",
            "title": "Belt Friction: Ratio of Belt Tensions and Power Transmission Derivation",
            "yt_query": "belt friction derivation ratio of tensions power transmitted flat belt drive",
            "img_path": "images/mechanics/belt_friction.png",
            "img_caption": "Figure 2.4: Infinitesimal Element of Belt on Pulley Showing Differential Tensions and Normal Reaction",
            "answer": r"""
Flexible power transmission elements—such as flat belts, V-belts, ropes, and band brakes—transmit torque between rotating shafts through frictional grip developed over the curved circumferential contact surface of a cylindrical drum or pulley. As torque is transmitted, the belt stretches slightly, establishing an unequal tension distribution: a higher tension $T_1$ on the driving (tight) side and a lower tension $T_2$ on the trailing (slack) side.

Derivation of the Ratio of Belt Tensions ($\frac{T_1}{T_2} = e^{\mu \theta}$):
Consider a flat flexible belt running over a fixed or rotating circular pulley of radius $R$.
Let:
- $\theta$ = total angle of lap / wrap (contact angle) in radians.
- $\mu$ = coefficient of friction between belt and pulley surface.
- $T_1$ = tension on the tight side.
- $T_2$ = tension on the slack side ($T_1 > T_2$).

To evaluate the tension profile, we isolate an infinitesimal differential segment of the belt subtending an angle $d\theta$ at the center of the pulley:
- At one end of the segment, the belt tension is $T$.
- At the other end, the tension increases to $T + dT$.
- The pulley surface exerts an outward radial normal reaction $dN$ on the element.
- The frictional resistance force $dF = \mu dN$ acts tangentially to the pulley, opposing the relative motion/slip of the belt.

Force Equilibrium of the Belt Element:
The normal reaction $dN$ acts along the radial centerline bisecting angle $d\theta$. The tensions $T$ and $T + dT$ act along tangents at angles of $\frac{d\theta}{2}$ to the perpendicular axis.
1. Radial Force Balance:
Summing forces along the radial direction toward the pulley center:
$$\Sigma F_r = dN - T \sin\left(\frac{d\theta}{2}\right) - (T + dT)\sin\left(\frac{d\theta}{2}\right) = 0$$
$$dN = [2T + dT]\sin\left(\frac{d\theta}{2}\right)$$
Because $d\theta$ is an infinitesimal angle, we apply the small-angle approximation $\sin\left(\frac{d\theta}{2}\right) \approx \frac{d\theta}{2}$. Neglecting the higher-order product $dT \cdot \frac{d\theta}{2}$:
$$dN = 2T \left(\frac{d\theta}{2}\right) = T d\theta \quad \text{--- (Equation 1)}$$

2. Tangential Force Balance:
Summing forces along the tangential direction:
$$\Sigma F_t = (T + dT)\cos\left(\frac{d\theta}{2}\right) - T \cos\left(\frac{d\theta}{2}\right) - dF = 0$$
Using the approximation $\cos\left(\frac{d\theta}{2}\right) \approx 1$:
$$(T + dT)(1) - T(1) - dF = 0 \implies dT = dF$$
At limiting friction equilibrium, $dF = \mu dN$. Therefore:
$$dT = \mu dN \quad \text{--- (Equation 2)}$$

3. Integration Across the Wrap Angle:
Substituting Equation 1 ($dN = T d\theta$) into Equation 2:
$$dT = \mu (T d\theta) \implies \frac{dT}{T} = \mu d\theta$$
Integrating this separable differential equation across the entire contact wrap angle from $\theta = 0$ (where $T = T_2$, slack side) to $\theta = \theta$ (where $T = T_1$, tight side):
$$\int_{T_2}^{T_1} \frac{dT}{T} = \mu \int_0^\theta d\theta$$
$$\left[ \ln T \right]_{T_2}^{T_1} = \mu [\theta]_0^\theta \implies \ln T_1 - \ln T_2 = \mu \theta$$
$$\ln\left(\frac{T_1}{T_2}\right) = \mu \theta$$
Taking the exponential on both sides yields the classical Belt Friction Equation:
$$\frac{T_1}{T_2} = e^{\mu \theta}$$
Important Notes on the Tension Ratio:
1. The angle of wrap $\theta$ must be expressed strictly in radians ($\theta_{\text{rad}} = \theta_{\text{deg}} \times \frac{\pi}{180}$).
2. For V-belts or ropes running in grooved pulleys with groove angle $2\beta$, the normal reaction is increased by wedging action:
$$\frac{T_1}{T_2} = e^{\frac{\mu \theta}{\sin\beta}}$$

Power Transmitted by a Belt Drive:
Let a belt drive transmit torque to a pulley of diameter $D$ rotating at speed $N$ revolutions per minute ($\text{rpm}$).
The linear pitch line velocity of the belt is:
$$v = \frac{\pi D N}{60}\text{ m/s}$$
The effective tangential driving force transmitted by the belt to the pulley circumference is the difference between tight-side and slack-side tensions:
$$F_{eff} = T_1 - T_2$$
The mechanical power $P$ transmitted is the product of effective driving force and belt speed:
$$P = (T_1 - T_2) v = (T_1 - T_2) \frac{\pi D N}{60} \quad \text{(in Watts)}$$
Expressing power in terms of maximum tension $T_1$:
$$P = T_1 \left(1 - \frac{T_2}{T_1}\right) v = T_1 \left(1 - e^{-\mu\theta}\right) v$$

Centrifugal Tension Correction ($T_c$):
When the belt runs at high speeds, continuous centripetal acceleration gives rise to centrifugal tension:
$$T_c = m v^2$$
where $m$ is the mass per unit length of the belt ($\text{kg/m}$) and $v$ is belt velocity. Incorporating $T_c$, the effective tensions governing friction become:
$$\frac{T_1 - T_c}{T_2 - T_c} = e^{\mu \theta}$$
The maximum power transmission occurs at an optimum velocity $v = \sqrt{\frac{T_{max}}{3m}}$, where centrifugal tension equals one-third of the maximum allowable belt tension ($T_c = \frac{T_{max}}{3}$).
"""
        },
        {
            "qid": "mech-q10",
            "marks": 7,
            "type": "Theory & Application",
            "title": "Analysis of Pin-Jointed Simple Trusses: Method of Joints, Method of Sections, and Zero-Force Members",
            "yt_query": "truss analysis method of joints method of sections zero force members engineering mechanics",
            "img_path": "images/mechanics/truss_analysis.png",
            "img_caption": "Figure 2.5: Planar Pratt Truss Geometry with Free Body Diagram of Cut Section and Joint Equilibrium",
            "answer": r"""
A truss is an engineering structure composed of slender structural members connected together at their endpoints to form a rigid structural framework. Widely used in bridge spans, roof trusses, crane booms, and transmission towers, trusses carry loads over long spans while minimizing material usage.

Assumptions in Ideal Planar Truss Analysis:
1. All truss members are connected together at their ends by frictionless, smooth cylindrical pins.
2. All external loads and support reactions are applied strictly at the pin joints (no transverse loads are applied directly along member lengths).
3. The centroidal longitudinal axes of all members meeting at any joint are concurrent.
4. The self-weight of the members is negligible compared to the applied working loads.
Under these standard assumptions, every member acts as a pure two-force member, carrying only axial forces (either axial tension $T$ pulling away from joints or axial compression $C$ pushing into joints), with zero internal bending moments or shear forces.

Structural Determinacy and Classification:
Let $m$ be the number of members and $j$ be the number of pin joints in a planar truss:
1. Perfect (Statically Determinate) Truss: $m = 2j - 3$. The truss has just enough members to maintain geometric stability, and internal forces can be determined using equations of statics alone.
2. Deficient (Imperfect / Mechanism) Truss: $m < 2j - 3$. The truss lacks sufficient members and will collapse under certain loads.
3. Redundant (Statically Indeterminate) Truss: $m > 2j - 3$. The truss possesses extra members, requiring deformation analysis to solve.

Rules for Identifying Zero-Force Members by Inspection:
Inspecting a truss for zero-force members before performing detailed calculations simplifies the analysis:
1. Rule 1 (Two-Member Joint): If only two non-collinear members meet at an unloaded joint (no external load or support reaction), both members carry zero force.
2. Rule 2 (Three-Member Joint with Two Collinear): If three members meet at an unloaded joint where two of the members are collinear, the third non-collinear member carries zero force. The two collinear members carry equal and opposite forces.
3. Rule 3 (Two Collinear with Applied Load): If two collinear members meet at a joint with an external load applied parallel to them, a third perpendicular member carries zero force.

Method of Joints:
The Method of Joints isolates individual pin joints as free body diagrams. Because all member forces meeting at a joint are concurrent, the moment equilibrium equation is trivially satisfied ($\Sigma M = 0$). Only two independent scalar equilibrium equations apply at each joint:
$$\Sigma F_x = 0 \quad \text{and} \quad \Sigma F_y = 0$$
Systematic Analysis Procedure:
1. Determine external support reactions by treating the entire truss as a single rigid body and applying $\Sigma F_x = 0, \Sigma F_y = 0, \Sigma M = 0$.
2. Identify and eliminate all zero-force members using the inspection rules.
3. Locate a joint that connects no more than two unknown member forces.
4. Draw the isolated joint FBD, assuming unknown member forces are tensile (pulling away from the joint). If the computed force is positive, the member is in tension ($T$); if negative, it is in compression ($C$).
5. Apply $\Sigma F_x = 0$ and $\Sigma F_y = 0$ to solve for the two unknown forces.
6. Advance sequentially to adjacent joints, carrying forward solved forces with opposite senses (Newton's third law), until all member forces are determined.

Method of Sections (Ritter's Method):
When member forces are required in only a few specific internal members (e.g., near the center of a large bridge span), the Method of Joints is tedious. The Method of Sections determines internal forces directly by cutting the entire truss into two separate parts.
Procedure:
1. Determine external support reactions using whole-truss equilibrium.
2. Pass an imaginary cut section line $a-a$ through the truss, cutting through the members whose forces are required.
   - Constraint: The cut line must not cut more than three non-concurrent, non-parallel members.
3. Isolate either the left or right part of the truss as a free body diagram.
4. Replace the cut members with unknown axial forces acting along their lines of action.
5. Because the isolated part is a rigid body in 2D, apply the three full equations of equilibrium:
$$\Sigma F_x = 0, \quad \Sigma F_y = 0, \quad \Sigma M_O = 0$$
Choosing the moment center $O$ at the intersection of two unknown forces eliminates both from the moment equation, enabling direct solution of the third unknown member force in a single algebraic step.
"""
        }
    ]
}
