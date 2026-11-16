# -*- coding: utf-8 -*-
"""
Module 1: Statics of Particles and Rigid Bodies (mech-q1 to mech-q5)
KTU 2019 Scheme Engineering Mechanics (EST100)
"""

MODULE_1 = {
    "module_id": "mech-m1",
    "module_num": "Module 1",
    "module_title": "Statics of Particles, Coplanar Forces and Rigid Body Equilibrium",
    "questions": [
        {
            "qid": "mech-q1",
            "marks": 7,
            "type": "Derivation & Theory",
            "title": "Fundamental Principles of Mechanics and Resultant of Coplanar Concurrent Forces",
            "yt_query": "parallelogram law of forces resolution concurrent forces resultant engineering mechanics",
            "img_path": "images/mechanics/concurrent_forces_resultant.png",
            "img_caption": "Figure 1.1: Parallelogram Law and Cartesian Resolution of Concurrent Coplanar Forces",
            "answer": r"""
Engineering mechanics is grounded in Newtonian principles governing the action of forces upon material bodies at rest or in motion. When multiple forces act simultaneously on a particle or rigid body, the combined physical effect of these forces can be represented by a single equivalent force called the resultant.

Fundamental Principles of Mechanics:
1. Parallelogram Law of Forces: Discovered experimentally by Stevinus in 1586, this axiom states that if two forces acting concurrently on a particle at a point are represented in magnitude and direction by the two adjacent sides of a parallelogram drawn from that point, their resultant is represented in magnitude and direction by the diagonal of the parallelogram passing through that same point.
Let two concurrent forces $\mathbf{P}$ and $\mathbf{Q}$ act at an angle $\theta$. By completing the parallelogram $OACB$ where $\vec{OA} = \mathbf{P}$ and $\vec{OB} = \mathbf{Q}$, the diagonal $\vec{OC} = \mathbf{R}$.
Dropping a perpendicular $CD$ from vertex $C$ to the extension of line $OA$:
In the right-angled triangle $\Delta ODC$:
$$OC^2 = OD^2 + CD^2 = (OA + AD)^2 + CD^2$$
From $\Delta ADC$, $AD = Q \cos\theta$ and $CD = Q \sin\theta$. Substituting these:
$$R^2 = (P + Q \cos\theta)^2 + (Q \sin\theta)^2 = P^2 + 2PQ \cos\theta + Q^2 \cos^2\theta + Q^2 \sin^2\theta$$
Since $\cos^2\theta + \sin^2\theta = 1$:
$$R = \sqrt{P^2 + Q^2 + 2PQ \cos\theta}$$
The direction angle $\alpha$ of resultant $\mathbf{R}$ with respect to force $\mathbf{P}$ is:
$$\tan\alpha = \frac{CD}{OD} = \frac{Q \sin\theta}{P + Q \cos\theta} \implies \alpha = \tan^{-1}\left(\frac{Q \sin\theta}{P + Q \cos\theta}\right)$$

2. Principle of Transmissibility of Forces: Stated by French mathematician Pierre Varignon, this principle asserts that the internal conditions of motion or external equilibrium of a rigid body remain unchanged if a force acting at a given point on the body is transmitted to act at any other point along its line of action, provided its magnitude, direction, and sense remain unaltered. This principle allows forces acting on rigid bodies to be treated as sliding vectors along their lines of action.

Analytical Resolution of a System of Coplanar Concurrent Forces:
When a system comprises $n$ concurrent forces $\mathbf{F}_1, \mathbf{F}_2, \dots, \mathbf{F}_n$ acting at a common point $O$, inclined at angles $\theta_1, \theta_2, \dots, \theta_n$ relative to the positive horizontal $x$-axis, the analytical method of resolution provides a general, systematic approach for determining the resultant:
1. Resolution into Orthogonal Components:
Each individual force $\mathbf{F}_i$ is resolved into its horizontal and vertical Cartesian components:
$$F_{ix} = F_i \cos\theta_i$$
$$F_{iy} = F_i \sin\theta_i$$
2. Algebraic Summation along Coordinate Axes:
The algebraic sum of the horizontal components of all forces is:
$$\Sigma F_x = F_1 \cos\theta_1 + F_2 \cos\theta_2 + \dots + F_n \cos\theta_n = \sum_{i=1}^n F_i \cos\theta_i$$
The algebraic sum of the vertical components of all forces is:
$$\Sigma F_y = F_1 \sin\theta_1 + F_2 \sin\theta_2 + \dots + F_n \sin\theta_n = \sum_{i=1}^n F_i \sin\theta_i$$
3. Resultant Vector Formulation:
The resultant force vector $\mathbf{R}$ is the vector sum of these orthogonal components:
$$\mathbf{R} = (\Sigma F_x)\hat{\mathbf{i}} + (\Sigma F_y)\hat{\mathbf{j}}$$
4. Magnitude and Direction of Resultant:
The scalar magnitude of the resultant force is:
$$R = \sqrt{(\Sigma F_x)^2 + (\Sigma F_y)^2}$$
The inclination angle $\theta_R$ of the resultant with respect to the horizontal $x$-axis is given by:
$$\tan\theta_R = \left| \frac{\Sigma F_y}{\Sigma F_x} \right| \implies \theta_R = \tan^{-1}\left( \frac{|\Sigma F_y|}{|\Sigma F_x|} \right)$$
The true physical quadrant of resultant $\mathbf{R}$ is determined by the individual algebraic signs of $\Sigma F_x$ and $\Sigma F_y$.

Analytical Conditions of Static Equilibrium:
A particle subjected to a system of coplanar concurrent forces is in static equilibrium if and only if the resultant force acting on it is identically zero ($\mathbf{R} = 0$). This vector condition translates into two independent scalar algebraic equations:
$$\Sigma F_x = 0 \quad \text{and} \quad \Sigma F_y = 0$$
"""
        },
        {
            "qid": "mech-q2",
            "marks": 7,
            "type": "Derivation & Application",
            "title": "Lami's Theorem: Statement, Proof, and Application to Suspended Sphere Equilibrium",
            "yt_query": "lamis theorem proof suspended sphere vertical wall engineering mechanics",
            "img_path": "images/mechanics/lamis_theorem_sphere.png",
            "img_caption": "Figure 1.2: Lami's Force Triangle and Equilibrium of a Smooth Sphere Suspended by a Cord",
            "answer": r"""
Lami's Theorem is a classical kinematic equation derived by French mathematician Bernard Lamy in 1687. It provides a simple, direct trigonometric method for analyzing the static equilibrium of a particle acted upon by exactly three concurrent, coplanar forces.

Statement of Lami's Theorem:
If three coplanar, concurrent forces acting at a point are in static equilibrium, each force is directly proportional to the sine of the angle included between the other two forces.
Mathematically, let three forces $\mathbf{F}_1, \mathbf{F}_2, \mathbf{F}_3$ act concurrently at point $O$ in equilibrium. Let $\alpha$ be the angle between $\mathbf{F}_2$ and $\mathbf{F}_3$, $\beta$ be the angle between $\mathbf{F}_1$ and $\mathbf{F}_3$, and $\gamma$ be the angle between $\mathbf{F}_1$ and $\mathbf{F}_2$. Lami's theorem states:
$$\frac{F_1}{\sin\alpha} = \frac{F_2}{\sin\beta} = \frac{F_3}{\sin\gamma}$$

Mathematical Proof of Lami's Theorem:
Consider three concurrent coplanar forces $\mathbf{F}_1, \mathbf{F}_2, \mathbf{F}_3$ in equilibrium:
$$\mathbf{F}_1 + \mathbf{F}_2 + \mathbf{F}_3 = 0$$
According to the polygon law of forces, if three concurrent forces are in equilibrium, they can be represented in magnitude and direction by the three sides of a closed triangle taken in order.
Let triangle $\Delta ABC$ represent this force equilibrium, where side $\vec{AB} = \mathbf{F}_1$, side $\vec{BC} = \mathbf{F}_2$, and side $\vec{CA} = \mathbf{F}_3$.
Now consider the external angles between the vector directions at point $O$:
- The external angle between $\mathbf{F}_1$ and $\mathbf{F}_2$ is $\gamma$. In $\Delta ABC$, the interior angle at vertex $B$ between the sides representing $\mathbf{F}_1$ and $\mathbf{F}_2$ is $\angle B = 180^\circ - \gamma$.
- The external angle between $\mathbf{F}_2$ and $\mathbf{F}_3$ is $\alpha$. The interior angle at vertex $C$ is $\angle C = 180^\circ - \alpha$.
- The external angle between $\mathbf{F}_3$ and $\mathbf{F}_1$ is $\beta$. The interior angle at vertex $A$ is $\angle A = 180^\circ - \beta$.
Applying the standard Law of Sines (Sine Rule) to triangle $\Delta ABC$:
$$\frac{AB}{\sin(\angle C)} = \frac{BC}{\sin(\angle A)} = \frac{CA}{\sin(\angle B)}$$
Substituting the force magnitudes and interior angles:
$$\frac{F_1}{\sin(180^\circ - \alpha)} = \frac{F_2}{\sin(180^\circ - \beta)} = \frac{F_3}{\sin(180^\circ - \gamma)}$$
Using the trigonometric identity $\sin(180^\circ - \theta) = \sin\theta$:
$$\frac{F_1}{\sin\alpha} = \frac{F_2}{\sin\beta} = \frac{F_3}{\sin\gamma}$$
This completes the mathematical proof.

Classic Engineering Application: Equilibrium of a Suspended Sphere:
Problem Statement: A uniform smooth sphere of weight $W$ and radius $r$ is suspended from a peg on a smooth vertical wall by a flexible, inextensible cord of length $l$ attached to a point on its surface. Determine the tension $T$ in the cord and the normal reaction $R_w$ exerted by the vertical wall on the sphere.

Analytical Solution:
1. Identifying Forces and Drawing the Free Body Diagram (FBD):
The center of the sphere is designated as $C$. The three forces acting concurrently at center $C$ are:
- The downward gravitational weight $W$ acting vertically through $C$.
- The normal reaction $R_w$ from the smooth wall, which acts horizontally through the point of contact $A$ and passes directly through center $C$ (since the wall is frictionless, reaction is purely normal).
- The tension force $T$ exerted by the cord along line $BC$, where $B$ is the suspension peg on the wall. The line of action of the cord must pass through the center of mass $C$ for rotational equilibrium.
2. Geometry of the Cord:
In the right-angled triangle formed by peg $B$, wall contact $A$, and sphere center $C$:
- The hypotenuse is $BC = l + r$ (cord length plus radius).
- The horizontal side is $AC = r$ (sphere radius).
Let $\theta$ be the inclination angle of the cord with the vertical wall:
$$\sin\theta = \frac{AC}{BC} = \frac{r}{l + r} \implies \theta = \sin^{-1}\left(\frac{r}{l + r}\right)$$
$$\cos\theta = \frac{AB}{BC} = \frac{\sqrt{(l + r)^2 - r^2}}{l + r} = \frac{\sqrt{l^2 + 2lr}}{l + r}$$
3. Determining Angles Between Forces at Center $C$:
- The angle between normal reaction $R_w$ (horizontal) and weight $W$ (downward vertical) is $90^\circ$.
- The angle between tension $T$ and weight $W$ is $180^\circ - \theta$.
- The angle between tension $T$ and wall reaction $R_w$ is $90^\circ + \theta$.
4. Applying Lami's Theorem:
$$\frac{T}{\sin(90^\circ)} = \frac{R_w}{\sin(180^\circ - \theta)} = \frac{W}{\sin(90^\circ + \theta)}$$
Since $\sin(90^\circ) = 1$, $\sin(180^\circ - \theta) = \sin\theta$, and $\sin(90^\circ + \theta) = \cos\theta$:
$$\frac{T}{1} = \frac{R_w}{\sin\theta} = \frac{W}{\cos\theta}$$
Solving for the cord tension $T$:
$$T = \frac{W}{\cos\theta} = W \frac{l + r}{\sqrt{l^2 + 2lr}}$$
Solving for the wall reaction $R_w$:
$$R_w = W \tan\theta = W \frac{\sin\theta}{\cos\theta} = W \frac{r}{\sqrt{l^2 + 2lr}}$$
These simple closed-form expressions highlight the power of Lami's theorem in statics.
"""
        },
        {
            "qid": "mech-q3",
            "marks": 7,
            "type": "Theory & Application",
            "title": "Free Body Diagrams (FBD) and Equilibrium of Nested Cylinders in a Channel",
            "yt_query": "free body diagram nested cylinders channel equilibrium engineering mechanics",
            "img_path": "images/mechanics/nested_cylinders_fbd.png",
            "img_caption": "Figure 1.3: Free Body Diagrams and Contact Normal Reactions for Two Nested Rollers in a Channel",
            "answer": r"""
A Free Body Diagram (FBD) is a graphical representation used in engineering mechanics to isolate a body or system of interconnected bodies from its surroundings. In an FBD, all external physical contacts, supports, walls, and constraints are replaced by their corresponding reactive forces and moments, along with externally applied loads and body forces (weight). Constructing an accurate FBD is the essential prerequisite for setting up the equations of static and dynamic equilibrium.

Steps for Constructing an FBD:
1. Isolate the Body: Draw a clear schematic outline of the isolated body, detached from all surrounding structures.
2. Apply External and Body Forces: Draw the weight vector $W = mg$ acting vertically downward through the center of gravity, along with any given applied forces.
3. Replace Supports with Reactive Forces:
   - Smooth frictionless surface: Replace with a normal reaction force $N$ directed perpendicular to the contact tangent into the body.
   - Flexible cable / cord: Replace with a tensile force $T$ directed away from the body along the cord axis.
   - Rough surface: Include both normal reaction $N$ and a tangential frictional force $F_f$ opposing relative motion.
   - Contact between curved surfaces: Normal reaction acts along the common normal passing through the centers of curvature.

Equilibrium of Nested Cylinders in a Rectangular Channel:
Problem: Two smooth, identical solid cylinders $A$ and $B$, each having weight $W = 1000\text{ N}$ and radius $R = 250\text{ mm}$, rest inside a horizontal rectangular channel of internal width $L = 800\text{ mm}$. Cylinder $A$ rests on the horizontal bottom floor and touches the left vertical wall. Cylinder $B$ rests on cylinder $A$ and touches the right vertical wall. Determine all contact reactions at the walls, floor, and between the cylinders.

Step-by-Step Analytical Equilibrium Solution:
1. Geometric Configuration and Line of Centers:
Let $C_A$ and $C_B$ denote the center points of cylinders $A$ and $B$.
The horizontal distance between the left wall and center $C_A$ is $R$.
The horizontal distance between the right wall and center $C_B$ is $R$.
Therefore, the horizontal distance $\Delta x$ between the centers $C_A$ and $C_B$ is:
$$\Delta x = L - R - R = L - 2R = 800 - 2(250) = 800 - 500 = 300\text{ mm}$$
When the two smooth cylinders touch, the distance between their centers is:
$$d = C_A C_B = R + R = 2R = 2(250) = 500\text{ mm}$$
Let $\theta$ be the angle that the line of centers $C_A C_B$ makes with the horizontal:
$$\cos\theta = \frac{\Delta x}{d} = \frac{300}{500} = 0.6 \implies \theta = \cos^{-1}(0.6) \approx 53.13^\circ$$
$$\sin\theta = \sqrt{1 - \cos^2\theta} = \sqrt{1 - 0.6^2} = 0.8$$

2. Equilibrium of the Upper Cylinder $B$:
Upper cylinder $B$ is acted upon by three concurrent forces at center $C_B$:
- Downward gravitational weight: $W_B = 1000\text{ N}$ ($\downarrow$).
- Horizontal normal reaction from the right vertical wall: $R_{B,wall}$ acting to the left ($\leftarrow$).
- Mutual contact normal reaction $R_{AB}$ exerted by cylinder $A$ on $B$, directed upward along the line of centers at angle $\theta = 53.13^\circ$ above the horizontal ($\nearrow$).
Applying equations of equilibrium for cylinder $B$:
Vertical force balance ($\Sigma F_y = 0$):
$$R_{AB} \sin\theta - W_B = 0 \implies R_{AB} (0.8) = 1000$$
$$R_{AB} = \frac{1000}{0.8} = 1250\text{ N}$$
Horizontal force balance ($\Sigma F_x = 0$):
$$-R_{B,wall} + R_{AB} \cos\theta = 0 \implies R_{B,wall} = R_{AB} \cos\theta = 1250 \times 0.6 = 750\text{ N}$$
Thus, the right wall exerts a horizontal reaction of $750\text{ N}$ on cylinder $B$.

3. Equilibrium of the Lower Cylinder $A$:
Lower cylinder $A$ is acted upon by four forces:
- Downward gravitational weight: $W_A = 1000\text{ N}$ ($\downarrow$).
- Downward contact normal reaction from cylinder $B$: By Newton's third law, $R_{BA} = R_{AB} = 1250\text{ N}$, inclined at angle $\theta = 53.13^\circ$ below the horizontal ($\swarrow$).
- Horizontal normal reaction from the left vertical wall: $R_{A,wall}$ acting to the right ($\rightarrow$).
- Vertical normal reaction from the horizontal floor: $R_{A,floor}$ acting vertically upward ($\uparrow$).
Applying equations of equilibrium for cylinder $A$:
Horizontal force balance ($\Sigma F_x = 0$):
$$R_{A,wall} - R_{BA} \cos\theta = 0 \implies R_{A,wall} = 1250 \times 0.6 = 750\text{ N}$$
Vertical force balance ($\Sigma F_y = 0$):
$$R_{A,floor} - W_A - R_{BA} \sin\theta = 0$$
$$R_{A,floor} = 1000 + 1250 \times (0.8) = 1000 + 1000 = 2000\text{ N}$$

Summary of Contact Reactions:
- Normal reaction between the two cylinders: $R_{AB} = 1250\text{ N}$
- Left vertical wall reaction: $R_{A,wall} = 750\text{ N}$ (acting rightward)
- Right vertical wall reaction: $R_{B,wall} = 750\text{ N}$ (acting leftward)
- Horizontal bottom floor reaction: $R_{A,floor} = 2000\text{ N}$ (acting upward, exactly balancing total weight $W_A + W_B$)
"""
        },
        {
            "qid": "mech-q4",
            "marks": 7,
            "type": "Derivation & Theory",
            "title": "Varignon's Theorem of Moments, Couples, and Force-Couple Systems",
            "yt_query": "varignons theorem moments proof couple force couple system engineering mechanics",
            "img_path": "images/mechanics/varignon_theorem.png",
            "img_caption": "Figure 1.4: Geometric and Vector Proof of Varignon's Theorem of Moments About an Arbitrary Point O",
            "answer": r"""
The rotational tendency of a force about a specified pivot point or axis is quantified by the Moment of a Force. In vector mechanics, the moment of a force vector $\mathbf{F}$ acting at a point defined by position vector $\mathbf{r}$ relative to a reference origin $O$ is defined as the cross product:
$$\mathbf{M}_O = \mathbf{r} \times \mathbf{F}$$
The magnitude of the moment is given by $M_O = r F \sin\theta = F \cdot d$, where $d = r \sin\theta$ represents the perpendicular distance (moment arm) from the moment center $O$ to the line of action of force $\mathbf{F}$.

Varignon's Theorem of Moments (Principle of Moments):
Stated by French mathematician Pierre Varignon in 1687, this theorem is one of the most widely used principles in engineering statics.
Statement:
The algebraic sum of the moments of any number of coplanar concurrent forces about any arbitrary point in their plane is equal to the moment of their resultant force about the same point.
Mathematically, if forces $\mathbf{F}_1, \mathbf{F}_2, \dots, \mathbf{F}_n$ act concurrently at point $A$ defined by position vector $\mathbf{r}$ relative to origin $O$, and their resultant is $\mathbf{R} = \sum \mathbf{F}_i$, then:
$$\Sigma \mathbf{M}_O = \mathbf{M}_R \implies \sum_{i=1}^n (\mathbf{r} \times \mathbf{F}_i) = \mathbf{r} \times \mathbf{R}$$

Vector Proof of Varignon's Theorem:
Let concurrent forces $\mathbf{F}_1, \mathbf{F}_2, \dots, \mathbf{F}_n$ act at point $A$.
The position vector of point $A$ with respect to moment pivot $O$ is $\mathbf{r}$.
By definition of resultant force:
$$\mathbf{R} = \mathbf{F}_1 + \mathbf{F}_2 + \dots + \mathbf{F}_n = \sum_{i=1}^n \mathbf{F}_i$$
The total moment of all individual forces about point $O$ is:
$$\Sigma \mathbf{M}_O = \mathbf{M}_1 + \mathbf{M}_2 + \dots + \mathbf{M}_n = (\mathbf{r} \times \mathbf{F}_1) + (\mathbf{r} \times \mathbf{F}_2) + \dots + (\mathbf{r} \times \mathbf{F}_n)$$
Using the distributive property of the vector cross product over vector addition:
$$\Sigma \mathbf{M}_O = \mathbf{r} \times (\mathbf{F}_1 + \mathbf{F}_2 + \dots + \mathbf{F}_n) = \mathbf{r} \times \mathbf{R} = \mathbf{M}_{R, O}$$
This completes the vector proof. In scalar terms for coplanar forces:
$$\sum_{i=1}^n F_i d_i = R \cdot d_R$$
where $d_R$ is the perpendicular distance from $O$ to the resultant's line of action.

Theory of Couples in Mechanics:
A couple is defined as a system formed by two parallel forces having equal magnitudes, opposite directions, and distinct non-collinear parallel lines of action separated by a perpendicular distance $d$.
1. Characteristics of a Couple:
- Zero Net Force: The resultant translational force of a couple is identically zero ($\mathbf{R} = \mathbf{F} + (-\mathbf{F}) = 0$). A couple produces pure rotation without linear translation.
- Invariance of Moment (Free Vector): Unlike the moment of a single force (which depends on the choice of pivot point $O$), the moment of a couple is identical about every point in space.
Proof: Let forces $-\mathbf{F}$ and $+\mathbf{F}$ act at points $A$ and $B$, having position vectors $\mathbf{r}_A$ and $\mathbf{r}_B$ relative to an arbitrary origin $O$. The total moment about $O$ is:
$$\mathbf{M} = (\mathbf{r}_A \times -\mathbf{F}) + (\mathbf{r}_B \times \mathbf{F}) = (\mathbf{r}_B - \mathbf{r}_A) \times \mathbf{F} = \mathbf{r}_{BA} \times \mathbf{F}$$
where $\mathbf{r}_{BA} = \mathbf{r}_B - \mathbf{r}_A$ is the relative displacement vector pointing from $A$ to $B$. The scalar magnitude is:
$$M = F \cdot r_{BA} \sin\theta = F \cdot d$$
Since $\mathbf{M}$ is independent of position vectors $\mathbf{r}_A$ and $\mathbf{r}_B$, a couple is a free vector and can be translated anywhere within its plane without altering its external rotational effect on a rigid body.

Resolution of a Force into a Force and a Couple at Another Point:
In structural analysis, it is frequently necessary to shift the line of action of a force $\mathbf{F}$ from point $A$ to another point $B$ separated by perpendicular distance $d$.
1. At point $B$, introduce two equal, opposite, and collinear forces $+\mathbf{F}$ and $-\mathbf{F}$ parallel to the original force. Because their net sum is zero, the mechanical state of the rigid body is unaffected.
2. The original force $+\mathbf{F}$ at $A$ and the opposing force $-\mathbf{F}$ at $B$ form a couple of moment $M = F \cdot d$.
3. The remaining force $+\mathbf{F}$ at $B$ provides the original linear translational action.
Therefore, any force $\mathbf{F}$ acting on a rigid body can be replaced at an arbitrary point $B$ by an identical parallel force $\mathbf{F}$ combined with a couple of moment $M = F \cdot d$.
"""
        },
        {
            "qid": "mech-q5",
            "marks": 7,
            "type": "Theory & Application",
            "title": "Equilibrium of Rigid Bodies in 2D and Step-by-Step Support Reaction Analysis",
            "yt_query": "equilibrium of rigid bodies support reactions simply supported beam UDL point load couple",
            "img_path": "images/mechanics/beam_support_reactions.png",
            "img_caption": "Figure 1.5: Free Body Diagram of Beam with Hinged and Roller Supports under Combined Loading",
            "answer": r"""
A rigid body is defined as an idealization of a solid body in which the deformations between constituent particles are negligibly small compared to the overall dimensions. Unlike a particle (which can be treated as a point mass without rotational degrees of freedom), a rigid body can undergo both linear translation and rotation. Consequently, for a rigid body to remain in static equilibrium in a two-dimensional plane, both the resultant force and the resultant moment about any point must vanish simultaneously.

General Equations of Equilibrium in Two Dimensions:
For any coplanar force system acting on a rigid body, the vector equilibrium equations $\mathbf{R} = 0$ and $\mathbf{M}_O = 0$ yield three independent scalar equilibrium equations:
$$\Sigma F_x = 0$$
$$\Sigma F_y = 0$$
$$\Sigma M_O = 0 \quad (\text{about any arbitrary reference pivot } O)$$

Classification of Structural Supports and Reactive Forces in 2D:
1. Roller Support: Allows free translation along the supporting plane and free rotation about the pin axis. It resists motion strictly perpendicular to the supporting surface, providing exactly one unknown reactive force $R_N$ oriented normal to the plane.
2. Hinged / Pin Support: Restrains both horizontal and vertical translation, but permits free rotation about the pin axis. It exerts an unknown reaction at an unknown angle, which is resolved into two orthogonal unknown reaction components: horizontal force $R_x$ and vertical force $R_y$.
3. Fixed / Built-in Support: Completely restrains translation in all directions as well as rotation. It develops three unknown reactions: horizontal force $R_x$, vertical force $R_y$, and a reactive resisting couple (fixing moment) $M$.

Worked Problem: Determination of Support Reactions for a Beam:
Problem Statement: A horizontal beam $AB$ of span $L = 8\text{ m}$ is simply supported with a pin support at left end $A$ and a roller support at right end $B$. The beam carries the following loads:
- A uniformly distributed load (UDL) of $w = 4\text{ kN/m}$ over the left half of the beam from $x = 0$ to $x = 4\text{ m}$.
- A concentrated point load of $P = 20\text{ kN}$ applied at distance $x = 6\text{ m}$ from $A$, inclined at $60^\circ$ to the horizontal towards the left.
- A concentrated clockwise couple $M_0 = 16\text{ kN}\cdot\text{m}$ applied at the center of the beam ($x = 4\text{ m}$).
Determine the support reactions at ends $A$ and $B$.

Step-by-Step Analytical Solution:
1. Converting Distributed and Inclined Loads to Equivalent Components:
- The UDL extends over length $L_{udl} = 4\text{ m}$. Its equivalent total concentrated load is:
$$W_{udl} = w \times L_{udl} = 4\text{ kN/m} \times 4\text{ m} = 16\text{ kN}$$
This equivalent load acts at the centroid of the distributed rectangle, which is at distance $\bar{x} = \frac{4}{2} = 2\text{ m}$ from support $A$.
- The inclined load $P = 20\text{ kN}$ at $x = 6\text{ m}$ is resolved into Cartesian components:
Horizontal component (directed leftward):
$$P_x = P \cos(60^\circ) = 20 \times 0.5 = 10\text{ kN} \quad (\leftarrow)$$
Vertical component (directed downward):
$$P_y = P \sin(60^\circ) = 20 \times \frac{\sqrt{3}}{2} \approx 17.32\text{ kN} \quad (\downarrow)$$

2. Setting Up Support Reactions on the Free Body Diagram:
- At pin support $A$: Two unknown reactive forces: horizontal reaction $R_{Ax}$ (assumed rightward $\rightarrow$) and vertical reaction $R_{Ay}$ (assumed upward $\uparrow$).
- At roller support $B$: One unknown vertical reactive force $R_B$ (assumed upward $\uparrow$).

3. Applying the Equations of Static Equilibrium:
First, Horizontal Force Equilibrium ($\Sigma F_x = 0$):
Taking rightward forces as positive:
$$R_{Ax} - P_x = 0 \implies R_{Ax} - 10 = 0 \implies R_{Ax} = 10\text{ kN} \quad (\rightarrow)$$

Second, Rotational Moment Equilibrium about Support $A$ ($\Sigma M_A = 0$):
Taking counter-clockwise moments as positive ($+ \circlearrowleft$):
- Moment of $W_{udl}$ at $x = 2\text{ m}$: Clockwise $\implies -(16\text{ kN} \times 2\text{ m}) = -32\text{ kN}\cdot\text{m}$
- Applied concentrated couple at $x = 4\text{ m}$: Clockwise $\implies -16\text{ kN}\cdot\text{m}$
- Moment of vertical component $P_y$ at $x = 6\text{ m}$: Clockwise $\implies -(17.32\text{ kN} \times 6\text{ m}) = -103.92\text{ kN}\cdot\text{m}$
- Moment of roller reaction $R_B$ at $x = 8\text{ m}$: Counter-clockwise $\implies +(R_B \times 8\text{ m})$
Summing all moments about pivot $A$:
$$\Sigma M_A = -32 - 16 - 103.92 + 8 R_B = 0$$
$$-151.92 + 8 R_B = 0 \implies 8 R_B = 151.92 \implies R_B = \frac{151.92}{8} \approx 18.99\text{ kN} \quad (\uparrow)$$

Third, Vertical Force Equilibrium ($\Sigma F_y = 0$):
Taking upward forces as positive:
$$R_{Ay} + R_B - W_{udl} - P_y = 0$$
$$R_{Ay} + 18.99 - 16 - 17.32 = 0 \implies R_{Ay} + 18.99 - 33.32 = 0$$
$$R_{Ay} = 33.32 - 18.99 = 14.33\text{ kN} \quad (\uparrow)$$

Total Resultant Reaction at Pin Support $A$:
$$R_A = \sqrt{R_{Ax}^2 + R_{Ay}^2} = \sqrt{10^2 + 14.33^2} = \sqrt{100 + 205.35} = \sqrt{305.35} \approx 17.47\text{ kN}$$
Inclination angle with the horizontal:
$$\theta_A = \tan^{-1}\left(\frac{R_{Ay}}{R_{Ax}}\right) = \tan^{-1}\left(\frac{14.33}{10}\right) \approx 55.09^\circ$$
Final Support Reactions:
- Pin Support $A$: $R_{Ax} = 10.0\text{ kN} \rightarrow$, $R_{Ay} = 14.33\text{ kN} \uparrow$ (Resultant $R_A = 17.47\text{ kN}$ at $55.09^\circ$).
- Roller Support $B$: $R_B = 18.99\text{ kN} \uparrow$.
"""
        }
    ]
}
