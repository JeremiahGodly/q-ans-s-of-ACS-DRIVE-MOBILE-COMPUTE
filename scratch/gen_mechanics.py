# -*- coding: utf-8 -*-
"""
Content generator for Subject 6: Engineering Mechanics (EST100)
KTU 2019 Scheme Syllabus Comprehensive Question Bank.
All answers are elaborated in paragraph format with step-by-step mathematical derivations.
All strings are raw multiline strings to prevent any LaTeX escape corruptions.
Exports: MECHANICS_MODULES, MECHANICS_BYHEART, MECHANICS_EXAM_QUESTIONS
"""

MECHANICS_MODULES = [
    {
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
    },
    {
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
    },
    {
        "module_id": "mech-m3",
        "module_num": "Module 3",
        "module_title": "Centroid, Center of Gravity, Pappus Theorems and Moment of Inertia",
        "questions": [
            {
                "qid": "mech-q11",
                "marks": 7,
                "type": "Theory & Application",
                "title": "Centroid of Composite Plane Areas: First Moment of Area and Worked T-Section Calculation",
                "yt_query": "centroid of composite areas first moment of area T section worked problem mechanics",
                "img_path": "images/mechanics/centroid_composite_areas.png",
                "img_caption": "Figure 3.1: Geometric Partitioning of Composite T-Section and Coordinate System for Centroid Calculation",
                "answer": r"""
The Centroid of a plane area represents the geometric center of the figure, defined as the point where the entire area may be considered concentrated. While the term Center of Gravity ($CG$) applies to physical bodies possessing mass and weight, Centroid refers strictly to geometric entities such as curves, plane areas, and volumes where density is uniform or irrelevant.

First Moment of Area and Mathematical Definition:
The first moment of a plane area $A$ with respect to a reference coordinate axis is defined as the integral of the product of each differential area element $dA$ and its perpendicular coordinate distance to that axis:
$$Q_y = \int_A x \, dA \quad \text{(First Moment of Area with respect to the } y\text{-axis)}$$
$$Q_x = \int_A y \, dA \quad \text{(First Moment of Area with respect to the } x\text{-axis)}$$
If the entire area $A = \int dA$ were concentrated at a single centroidal point $C(\bar{x}, \bar{y})$, its moments about the $y$ and $x$ axes would be $A \bar{x}$ and $A \bar{y}$ respectively. Equating these gives:
$$\bar{x} = \frac{\int x \, dA}{\int dA} = \frac{Q_y}{A}$$
$$\bar{y} = \frac{\int y \, dA}{\int dA} = \frac{Q_x}{A}$$

For a composite figure composed of $n$ simple geometric sub-shapes (rectangles, triangles, circles) of known individual areas $A_i$ and centroidal coordinates $(x_i, y_i)$, the integral converts into discrete summations:
$$\bar{x} = \frac{\sum_{i=1}^n A_i x_i}{\sum_{i=1}^n A_i} = \frac{A_1 x_1 + A_2 x_2 + \dots + A_n x_n}{A_1 + A_2 + \dots + A_n}$$
$$\bar{y} = \frac{\sum_{i=1}^n A_i y_i}{\sum_{i=1}^n A_i} = \frac{A_1 y_1 + A_2 y_2 + \dots + A_n y_n}{A_1 + A_2 + \dots + A_n}$$
If the composite shape contains cutouts or hollow holes of area $A_{hole}$, their area is treated as negative (subtracted from the sum).

Worked Problem: Centroid Calculation of an Unsymmetrical T-Section:
Problem Statement: Determine the coordinates of the centroid of a structural T-section composed of a top horizontal flange of dimensions $150\text{ mm} \times 20\text{ mm}$ and a vertical web of dimensions $20\text{ mm} \times 180\text{ mm}$.

Step-by-Step Analytical Solution:
1. Setting Up the Reference Coordinate Axes:
- Place the horizontal $x$-axis along the bottom edge of the vertical web ($y = 0$).
- Place the vertical $y$-axis along the vertical line of symmetry passing through the center of the web.
Because the T-section is symmetric about the vertical centerline:
$$\bar{x} = 0$$
The centroid lies on the vertical axis of symmetry. We only need to compute $\bar{y}$.

2. Subdividing into Standard Simple Rectangles:
- Shape 1 (Vertical Web):
  - Width $b_1 = 20\text{ mm}$, Height $h_1 = 180\text{ mm}$
  - Area $A_1 = b_1 \times h_1 = 20 \times 180 = 3600\text{ mm}^2$
  - Height of centroid $y_1$ from the base ($y = 0$):
  $$y_1 = \frac{h_1}{2} = \frac{180}{2} = 90\text{ mm}$$
  - First moment $A_1 y_1 = 3600 \times 90 = 324,000\text{ mm}^3$

- Shape 2 (Top Horizontal Flange):
  - Width $b_2 = 150\text{ mm}$, Thickness $h_2 = 20\text{ mm}$
  - Area $A_2 = b_2 \times h_2 = 150 \times 20 = 3000\text{ mm}^2$
  - The flange rests on top of the web (web height $= 180\text{ mm}$).
  - Height of centroid $y_2$ from base ($y = 0$):
  $$y_2 = h_1 + \frac{h_2}{2} = 180 + \frac{20}{2} = 180 + 10 = 190\text{ mm}$$
  - First moment $A_2 y_2 = 3000 \times 190 = 570,000\text{ mm}^3$

3. Tabular Calculation of Composite Centroid:
- Total Area:
$$A_{total} = A_1 + A_2 = 3600 + 3000 = 6600\text{ mm}^2$$
- Total First Moment of Area about Base:
$$\Sigma A_i y_i = A_1 y_1 + A_2 y_2 = 324,000 + 570,000 = 894,000\text{ mm}^3$$
4. Calculating $\bar{y}$:
$$\bar{y} = \frac{\Sigma A_i y_i}{A_{total}} = \frac{894,000\text{ mm}^3}{6600\text{ mm}^2} \approx 135.45\text{ mm}$$
The centroid of the T-section is located on the vertical line of symmetry at a distance of $135.45\text{ mm}$ above the bottom edge of the web.
"""
            },
            {
                "qid": "mech-q12",
                "marks": 7,
                "type": "Derivation & Application",
                "title": "Theorems of Pappus and Guldinus: Statements, Proofs, and Geometric Applications",
                "yt_query": "pappus guldinus theorem proof surface area volume of revolution cone sphere",
                "img_path": "images/mechanics/pappus_guldinus.png",
                "img_caption": "Figure 3.2: Generation of Surface Area and Volume of Revolution via Centroid Rotation",
                "answer": r"""
The theorems of Pappus of Alexandria (circa 300 AD), rediscovered by Swiss mathematician Paul Guldin in 1640, provide elegant integral formulations relating the surface area and volume of bodies of revolution to the centroidal paths of their generating plane curves and plane areas.

Theorem 1: Surface Area of Revolution:
Statement:
The surface area generated by rotating a plane curve of finite length $L$ about a non-intersecting coplanar axis is equal to the product of the length of the generating curve and the distance traveled by its centroid during the revolution.
If the curve is rotated through a full angle of $2\pi$ radians ($360^\circ$):
$$A = 2\pi \bar{y} L$$
where $L$ is the arc length of the generating curve and $\bar{y}$ is the perpendicular distance of the centroid of the curve from the axis of rotation.

Mathematical Proof of Theorem 1:
Let a plane curve of total length $L$ lie in the $xy$-plane, and let the $x$-axis be the axis of revolution. Let $dL$ be an infinitesimal element of the curve located at vertical distance $y$ from the $x$-axis.
When the curve rotates through a full revolution ($2\pi$ radians) about the $x$-axis, the differential element $dL$ sweeps out a circular ribbon of radius $y$ and width $dL$.
The differential surface area generated is:
$$dA = 2\pi y \, dL$$
Integrating over the entire length of the curve:
$$A = \int_L 2\pi y \, dL = 2\pi \int_L y \, dL$$
By definition of the centroid of a line/curve:
$$\bar{y} = \frac{\int_L y \, dL}{L} \implies \int_L y \, dL = \bar{y} L$$
Substituting this into the surface area integral:
$$A = 2\pi \bar{y} L$$
If rotated through an arbitrary angle $\theta$ (in radians), $A = \theta \bar{y} L$. This completes the proof.

Theorem 2: Volume of Revolution:
Statement:
The volume of a solid generated by rotating a plane area $A$ about a non-intersecting coplanar axis is equal to the product of the generating area and the distance traveled by the centroid of that area during the revolution.
For a complete revolution of $2\pi$ radians:
$$V = 2\pi \bar{y} A$$
where $A$ is the generating plane area and $\bar{y}$ is the distance of the centroid of the area from the revolution axis.

Mathematical Proof of Theorem 2:
Let a plane lamina of area $A$ lie in the $xy$-plane, and let the $x$-axis be the axis of revolution. Consider a differential area element $dA$ situated at vertical coordinate $y$.
When the area rotates through $2\pi$ radians about the $x$-axis, the element $dA$ sweeps out a circular ring of radius $y$, cross-sectional area $dA$, and circumference $2\pi y$.
The differential volume generated is:
$$dV = 2\pi y \, dA$$
Integrating over the entire area $A$:
$$V = \int_A 2\pi y \, dA = 2\pi \int_A y \, dA$$
By definition of the centroid of a plane area:
$$\bar{y} = \frac{\int_A y \, dA}{A} \implies \int_A y \, dA = \bar{y} A$$
Substituting this yields:
$$V = 2\pi \bar{y} A$$
This completes the proof.

Applications to Classic Geometric Solids:
1. Surface Area and Volume of a Sphere:
- Generating Curve: A semi-circular arc of radius $R$ rotating about its diameter diameter axis.
  - Length of semi-circular arc: $L = \pi R$
  - Centroid distance from diameter axis: $\bar{y} = \frac{2R}{\pi}$
  - Surface Area by Theorem 1:
  $$A = 2\pi \bar{y} L = 2\pi \left(\frac{2R}{\pi}\right)(\pi R) = 4\pi R^2$$
- Generating Area: A semi-circular area of radius $R$ rotating about its diameter axis.
  - Area of semi-circle: $A_{semi} = \frac{\pi R^2}{2}$
  - Centroid distance from diameter axis: $\bar{y} = \frac{4R}{3\pi}$
  - Volume by Theorem 2:
  $$V = 2\pi \bar{y} A_{semi} = 2\pi \left(\frac{4R}{3\pi}\right)\left(\frac{\pi R^2}{2}\right) = \frac{4}{3}\pi R^3$$

2. Volume of a Right Circular Cone:
- Generating Area: A right-angled triangle with base radius $R$ and height $h$ rotating about the vertical axis $h$.
  - Area of triangle: $A = \frac{1}{2} R h$
  - Centroid distance from the axis of rotation: $\bar{x} = \frac{R}{3}$
  - Volume by Theorem 2:
  $$V = 2\pi \bar{x} A = 2\pi \left(\frac{R}{3}\right)\left(\frac{1}{2} R h\right) = \frac{1}{3}\pi R^2 h$$
"""
            },
            {
                "qid": "mech-q13",
                "marks": 7,
                "type": "Derivation",
                "title": "Parallel and Perpendicular Axis Theorems of Area Moment of Inertia: Complete Proofs",
                "yt_query": "parallel axis theorem perpendicular axis theorem area moment of inertia proof",
                "img_path": "images/mechanics/parallel_perpendicular_axis.png",
                "img_caption": "Figure 3.3: Coordinate Shift for Parallel Axis Theorem and Orthogonal Axes for Perpendicular Axis Theorem",
                "answer": r"""
The Second Moment of Area, commonly termed the Area Moment of Inertia, is a fundamental geometric property of structural cross-sections that measures their resistance to bending deflection and torsional shearing stresses.
For a planar cross-section of area $A$ in the $xy$-plane, the moments of inertia about the Cartesian axes are defined as:
$$I_{xx} = \int_A y^2 \, dA \quad \text{and} \quad I_{yy} = \int_A x^2 \, dA$$
The Polar Moment of Inertia $J_z$ about the perpendicular $z$-axis passing through origin $O$ is:
$$J_z = I_{zz} = \int_A r^2 \, dA = \int_A (x^2 + y^2)\, dA$$
The Radius of Gyration $k$ represents the distance from the axis at which the entire area could be concentrated without altering its moment of inertia:
$$k_x = \sqrt{\frac{I_{xx}}{A}} \quad \text{and} \quad k_y = \sqrt{\frac{I_{yy}}{A}}$$

1. Parallel Axis Theorem (Steiner's Theorem):
Statement:
The moment of inertia of any plane area about an arbitrary axis $AB$ parallel to its centroidal axis is equal to the moment of inertia about the parallel centroidal axis plus the product of the area and the square of the perpendicular distance between the two axes.
Mathematically:
$$I_{AB} = I_G + A d^2$$
where $I_G$ is the moment of inertia about the centroidal axis passing through centroid $G$, $A$ is the total area, and $d$ is the perpendicular distance between the two parallel axes.

Mathematical Proof of Parallel Axis Theorem:
Consider a plane area $A$. Let $G$ be the centroid of the area.
Set up a centroidal coordinate system with its origin at $G$, having axes $x'$ and $y'$.
Let an arbitrary parallel axis $AB$ lie at a perpendicular distance $d$ from the centroidal $x'$-axis.
Consider an infinitesimal differential area element $dA$ located at coordinate $y'$ from the centroidal axis. Its distance from the parallel axis $AB$ is:
$$y = y' + d$$
By definition, the moment of inertia of area $A$ about axis $AB$ is:
$$I_{AB} = \int_A y^2 \, dA = \int_A (y' + d)^2 \, dA$$
Expanding the binomial term inside the integral:
$$I_{AB} = \int_A \left[(y')^2 + 2d y' + d^2\right] dA = \int_A (y')^2 \, dA + 2d \int_A y' \, dA + d^2 \int_A dA$$
Analyzing the three individual integral terms:
1. First Term: $\int_A (y')^2 \, dA = I_G$ (the moment of inertia about the centroidal axis).
2. Second Term: The integral $\int_A y' \, dA$ represents the first moment of area about the centroidal axis $x'$. By definition of the centroid, the first moment of area about an axis passing through the centroid is identically zero:
$$\int_A y' \, dA = A \bar{y}' = A(0) = 0$$
Therefore, the middle term $2d \int_A y' \, dA = 0$.
3. Third Term: $d^2 \int_A dA = A d^2$ (since $\int_A dA = A$).
Substituting these evaluations:
$$I_{AB} = I_G + 0 + A d^2 = I_G + A d^2$$
This proves the Parallel Axis Theorem. (Note: The theorem can only be applied directly between an axis and a centroidal axis; to transfer between two non-centroidal axes, one must first transfer back to the centroid).

2. Perpendicular Axis Theorem:
Statement:
For any plane lamina lying in the $xy$-plane, the moment of inertia about the perpendicular $z$-axis (polar axis normal to the plane) is equal to the sum of the moments of inertia about the two mutually perpendicular coplanar axes $x$ and $y$ intersecting at the same point.
Mathematically:
$$I_{zz} = I_{xx} + I_{yy} \quad \text{or} \quad J_O = I_x + I_y$$

Mathematical Proof of Perpendicular Axis Theorem:
Let a thin plane lamina of area $A$ lie in the $xy$-plane.
Let $O$ be the origin, with mutually perpendicular coplanar coordinate axes $x$ and $y$. Let the $z$-axis pass through $O$ perpendicular to the plane of the lamina.
Consider a differential area element $dA$ with coordinates $(x, y)$.
Its distance from the $x$-axis is $y$, so its moment of inertia about the $x$-axis is $dI_x = y^2 dA$.
Its distance from the $y$-axis is $x$, so its moment of inertia about the $y$-axis is $dI_y = x^2 dA$.
Its radial distance from the origin $O$ (and from the $z$-axis) is $r$.
By the Pythagorean theorem:
$$r^2 = x^2 + y^2$$
The moment of inertia of the element about the $z$-axis is:
$$dI_{zz} = r^2 \, dA$$
Integrating across the entire area $A$:
$$I_{zz} = \int_A r^2 \, dA = \int_A (x^2 + y^2) \, dA = \int_A x^2 \, dA + \int_A y^2 \, dA$$
Substituting the definitions $I_{yy} = \int x^2 dA$ and $I_{xx} = \int y^2 dA$:
$$I_{zz} = I_{yy} + I_{xx} = I_{xx} + I_{yy}$$
This proves the Perpendicular Axis Theorem. (Crucial limitation: The theorem applies strictly to planar 2D figures; it cannot be applied to three-dimensional solids).
"""
            },
            {
                "qid": "mech-q14",
                "marks": 7,
                "type": "Theory & Application",
                "title": "Centroidal Moment of Inertia of a Composite I-Section: Step-by-Step Calculation",
                "yt_query": "moment of inertia composite I section parallel axis theorem radii of gyration",
                "img_path": "images/mechanics/i_section_moment_inertia.png",
                "img_caption": "Figure 3.4: Cross-Sectional Geometry and Centroidal Axes of an Unsymmetric I-Beam",
                "answer": r"""
Determining the second moment of area (moment of inertia) of structural beams is essential in structural engineering for evaluating bending stresses ($\sigma = \frac{M y}{I}$) and deflection profiles.

Problem Statement:
Determine the centroidal moments of inertia $I_{xx}$ and $I_{yy}$ and the radii of gyration $k_{xx}$ and $k_{yy}$ for an unsymmetrical I-section with the following dimensions:
- Top Flange: Width $b_1 = 120\text{ mm}$, Thickness $t_1 = 20\text{ mm}$
- Web: Thickness $t_2 = 15\text{ mm}$, Height $h_2 = 160\text{ mm}$
- Bottom Flange: Width $b_3 = 200\text{ mm}$, Thickness $t_3 = 20\text{ mm}$

Step 1: Locating the Centroid of the Composite Section:
Set the origin at the bottom-left corner of the bottom flange.
Because the cross-section is symmetric about the vertical centerline:
$$\bar{x} = \frac{b_3}{2} = \frac{200}{2} = 100\text{ mm}$$
The vertical centroidal axis $y-y$ coincides with this line of symmetry.

Now calculate the vertical centroid coordinate $\bar{y}$ from the bottom edge:
- Rectangle 1 (Bottom Flange):
  - Area: $A_1 = 200 \times 20 = 4000\text{ mm}^2$
  - Centroid height: $y_1 = \frac{20}{2} = 10\text{ mm}$
  - First moment: $A_1 y_1 = 4000 \times 10 = 40,000\text{ mm}^3$
- Rectangle 2 (Web):
  - Area: $A_2 = 15 \times 160 = 2400\text{ mm}^2$
  - Centroid height: $y_2 = 20 + \frac{160}{2} = 20 + 80 = 100\text{ mm}$
  - First moment: $A_2 y_2 = 2400 \times 100 = 240,000\text{ mm}^3$
- Rectangle 3 (Top Flange):
  - Area: $A_3 = 120 \times 20 = 2400\text{ mm}^2$
  - Centroid height: $y_3 = 20 + 160 + \frac{20}{2} = 180 + 10 = 190\text{ mm}$
  - First moment: $A_3 y_3 = 2400 \times 190 = 456,000\text{ mm}^3$

Total Area:
$$A_{total} = A_1 + A_2 + A_3 = 4000 + 2400 + 2400 = 8800\text{ mm}^2$$
Total First Moment:
$$\Sigma A_i y_i = 40,000 + 240,000 + 456,000 = 736,000\text{ mm}^3$$
Centroid height from base:
$$\bar{y} = \frac{\Sigma A_i y_i}{A_{total}} = \frac{736,000}{8800} \approx 83.64\text{ mm}$$

Step 2: Calculating Centroidal Moment of Inertia $I_{xx}$:
Applying the Parallel Axis Theorem $I_{xx, i} = I_{Gi} + A_i d_i^2$, where $I_{Gi} = \frac{b_i h_i^3}{12}$ and $d_i = |y_i - \bar{y}|$:
- For Bottom Flange (Shape 1):
  $$I_{G1} = \frac{200 \times 20^3}{12} = \frac{200 \times 8000}{12} \approx 133,333.33\text{ mm}^4$$
  $$d_1 = |10 - 83.64| = 73.64\text{ mm}$$
  $$A_1 d_1^2 = 4000 \times (73.64)^2 = 4000 \times 5422.85 \approx 21,691,400\text{ mm}^4$$
  $$I_{xx, 1} = 133,333 + 21,691,400 = 21,824,733\text{ mm}^4$$

- For Web (Shape 2):
  $$I_{G2} = \frac{15 \times 160^3}{12} = \frac{15 \times 4,096,000}{12} = 5,120,000\text{ mm}^4$$
  $$d_2 = |100 - 83.64| = 16.36\text{ mm}$$
  $$A_2 d_2^2 = 2400 \times (16.36)^2 = 2400 \times 267.65 \approx 642,360\text{ mm}^4$$
  $$I_{xx, 2} = 5,120,000 + 642,360 = 5,762,360\text{ mm}^4$$

- For Top Flange (Shape 3):
  $$I_{G3} = \frac{120 \times 20^3}{12} = \frac{120 \times 8000}{12} = 80,000\text{ mm}^4$$
  $$d_3 = |190 - 83.64| = 106.36\text{ mm}$$
  $$A_3 d_3^2 = 2400 \times (106.36)^2 = 2400 \times 11312.45 \approx 27,149,880\text{ mm}^4$$
  $$I_{xx, 3} = 80,000 + 27,149,880 = 27,229,880\text{ mm}^4$$

Total Moment of Inertia about horizontal centroidal axis $x-x$:
$$I_{xx} = I_{xx, 1} + I_{xx, 2} + I_{xx, 3} = 21,824,733 + 5,762,360 + 27,229,880 \approx 54.82 \times 10^6\text{ mm}^4$$

Step 3: Calculating Centroidal Moment of Inertia $I_{yy}$:
Because the vertical centerline is the common axis of symmetry for all three rectangles, all centroidal shifts in the $x$-direction are zero ($d_{xi} = 0$). Hence, no parallel axis term is needed:
$$I_{yy} = \sum \frac{h_i b_i^3}{12}$$
- Bottom Flange: $I_{yy, 1} = \frac{20 \times 200^3}{12} = \frac{20 \times 8,000,000}{12} \approx 13,333,333\text{ mm}^4$
- Web: $I_{yy, 2} = \frac{160 \times 15^3}{12} = \frac{160 \times 3375}{12} = 45,000\text{ mm}^4$
- Top Flange: $I_{yy, 3} = \frac{20 \times 120^3}{12} = \frac{20 \times 1,728,000}{12} = 2,880,000\text{ mm}^4$
$$I_{yy} = 13,333,333 + 45,000 + 2,880,000 \approx 16.26 \times 10^6\text{ mm}^4$$

Step 4: Calculating Radii of Gyration:
$$k_{xx} = \sqrt{\frac{I_{xx}}{A}} = \sqrt{\frac{54.82 \times 10^6}{8800}} = \sqrt{6229.5} \approx 78.93\text{ mm}$$
$$k_{yy} = \sqrt{\frac{I_{yy}}{A}} = \sqrt{\frac{16.26 \times 10^6}{8800}} = \sqrt{1847.7} \approx 42.98\text{ mm}$$
"""
            },
            {
                "qid": "mech-q15",
                "marks": 7,
                "type": "Derivation",
                "title": "Mass Moment of Inertia: Derivations for Uniform Slender Rod and Thin Circular Disc",
                "yt_query": "mass moment of inertia uniform slender rod circular disc derivation mechanics",
                "img_path": "images/mechanics/mass_moment_inertia.png",
                "img_caption": "Figure 3.5: Mass Elements and Rotational Axes for Slender Rod and Circular Disc",
                "answer": r"""
The Mass Moment of Inertia of a rigid body is the rotational analogue of inertial mass in linear motion. While mass $m$ quantifies a body's resistance to linear acceleration ($F = ma$), mass moment of inertia $I$ measures its resistance to rotational angular acceleration about a specified rotational axis ($T = I \alpha$).
Mathematically, for a rigid body of continuous mass distribution, the mass moment of inertia about an axis is defined as:
$$I = \int r^2 \, dm$$
where $dm$ is a differential mass element and $r$ is the perpendicular distance of the element from the axis of rotation. The Mass Radius of Gyration $k$ is given by:
$$k = \sqrt{\frac{I}{m}} \implies I = m k^2$$
The Parallel Axis Theorem for mass states that the mass moment of inertia about any axis parallel to a centroidal axis is:
$$I = I_G + m d^2$$
where $I_G$ is the moment of inertia about the parallel centroidal axis, $m$ is total mass, and $d$ is the perpendicular distance between axes.

Derivation 1: Mass Moment of Inertia of a Uniform Slender Rod:
Consider a straight uniform slender rod of total mass $m$, total length $L$, and uniform linear mass density $\lambda = \frac{m}{L}$. We assume the cross-sectional dimensions of the rod are negligibly small compared to its length.

1. Moment of Inertia About Centroidal Transverse Axis ($y$-axis passing through center $G$):
Place the origin $O$ at the center of mass $G$ of the rod, so the rod extends from $x = -L/2$ to $x = +L/2$.
Consider a differential element of length $dx$ situated at distance $x$ from the center.
The mass of this differential element is:
$$dm = \lambda \, dx = \left(\frac{m}{L}\right) dx$$
Its perpendicular distance from the transverse centroidal $y$-axis is $x$.
The differential mass moment of inertia is:
$$dI_G = x^2 \, dm = x^2 \left(\frac{m}{L}\right) dx$$
Integrating over the entire length of the rod from $-L/2$ to $+L/2$:
$$I_G = \frac{m}{L} \int_{-L/2}^{L/2} x^2 \, dx = \frac{m}{L} \left[ \frac{x^3}{3} \right]_{-L/2}^{L/2} = \frac{m}{3L} \left[ \left(\frac{L}{2}\right)^3 - \left(-\frac{L}{2}\right)^3 \right] = \frac{m}{3L} \left[ \frac{L^3}{8} - \left(-\frac{L^3}{8}\right) \right]$$
$$I_G = \frac{m}{3L} \left(\frac{2L^3}{8}\right) = \frac{m}{3L} \left(\frac{L^3}{4}\right) = \frac{m L^2}{12}$$
Therefore, the centroidal mass moment of inertia of a uniform slender rod is:
$$I_G = \frac{1}{12} m L^2$$

2. Moment of Inertia About an Axis Passing Through One End:
To find the moment of inertia $I_{end}$ about an axis passing through one end of the rod perpendicular to its length, we apply the Parallel Axis Theorem.
The distance between the centroid $G$ and the end of the rod is $d = L/2$:
$$I_{end} = I_G + m d^2 = \frac{1}{12} m L^2 + m \left(\frac{L}{2}\right)^2 = \frac{1}{12} m L^2 + \frac{1}{4} m L^2 = \left(\frac{1}{12} + \frac{3}{12}\right) m L^2 = \frac{4}{12} m L^2$$
$$I_{end} = \frac{1}{3} m L^2$$
The moment of inertia about one end is four times larger than about the center.

Derivation 2: Mass Moment of Inertia of a Thin Circular Disc:
Consider a thin, uniform circular disc of mass $m$, radius $R$, and uniform surface mass density $\sigma = \frac{m}{\pi R^2}$.

1. Moment of Inertia About Central Perpendicular Axis ($z$-axis):
Divide the disc into concentric circular rings. Consider an elemental ring of radius $r$ and radial width $dr$.
The surface area of the ring is $dA = 2\pi r \, dr$.
The mass of the elemental ring is:
$$dm = \sigma \, dA = \left(\frac{m}{\pi R^2}\right) (2\pi r \, dr) = \frac{2m}{R^2} r \, dr$$
Because all points on this ring are at the identical radial distance $r$ from the central perpendicular $z$-axis, its moment of inertia is:
$$dI_z = r^2 \, dm = r^2 \left( \frac{2m}{R^2} r \, dr \right) = \frac{2m}{R^2} r^3 \, dr$$
Integrating over the entire disc from $r = 0$ to $r = R$:
$$I_z = \frac{2m}{R^2} \int_0^R r^3 \, dr = \frac{2m}{R^2} \left[ \frac{r^4}{4} \right]_0^R = \frac{2m}{R^2} \left(\frac{R^4}{4}\right) = \frac{1}{2} m R^2$$
Thus, for a thin uniform circular disc about its polar axis:
$$I_z = \frac{1}{2} m R^2$$

2. Moment of Inertia About a Diametral Axis ($x$ or $y$ axis):
Because the disc is planar and thin, we apply the Perpendicular Axis Theorem:
$$I_z = I_x + I_y$$
By rotational symmetry, the moments of inertia about all diameter axes are identical: $I_x = I_y = I_d$.
$$I_z = I_d + I_d = 2 I_d \implies I_d = \frac{I_z}{2}$$
Substituting $I_z = \frac{1}{2} m R^2$:
$$I_d = \frac{1}{4} m R^2$$
This gives the mass moment of inertia of a circular disc about any diameter in its plane.
"""
            }
        ]
    },
    {
        "module_id": "mech-m4",
        "module_num": "Module 4",
        "module_title": "Kinematics and Kinetics of Particles, D'Alembert's Principle",
        "questions": [
            {
                "qid": "mech-q16",
                "marks": 7,
                "type": "Derivation & Analytical",
                "title": "Rectilinear Motion with Variable Acceleration: Calculus Formulation and Resisted Motion",
                "yt_query": "rectilinear motion variable acceleration integration resisted motion engineering mechanics",
                "img_path": "images/mechanics/variable_acceleration.png",
                "img_caption": "Figure 4.1: Kinematic Position, Velocity, and Acceleration Profiles for Resisted Rectilinear Motion",
                "answer": r"""
Rectilinear motion describes the one-dimensional translation of a particle along a straight line path. When acceleration is constant, motion is governed by standard algebraic kinematic equations ($v = u + at, s = ut + \frac{1}{2}at^2, v^2 = u^2 + 2as$). However, in most engineering situations—such as aerodynamic drag, vehicle braking, fluid viscosity resistance, or spring-mass dynamics—acceleration varies continuously as a function of time $t$, velocity $v$, or displacement $s$.

Fundamental Differential Kinematic Equations:
The position coordinate of a particle along a straight line is $s(t)$.
The instantaneous velocity $v$ is the first time derivative of displacement:
$$v = \frac{ds}{dt} \implies ds = v \, dt$$
The instantaneous acceleration $a$ is the time derivative of velocity:
$$a = \frac{dv}{dt} = \frac{d^2 s}{dt^2} \implies dv = a \, dt$$
By applying the chain rule of differentiation, time $t$ can be eliminated to link acceleration directly to displacement:
$$a = \frac{dv}{dt} = \frac{dv}{ds} \cdot \frac{ds}{dt} = v \frac{dv}{ds} \implies v \, dv = a \, ds$$

Analytical Solutions for Specific Functional Forms of Acceleration:
1. Case 1: Acceleration as a Function of Time, $a = f(t)$:
Separating variables in $dv = a \, dt$:
$$\int_{v_0}^v dv = \int_0^t f(t) \, dt \implies v(t) = v_0 + \int_0^t f(t) \, dt$$
Once $v(t)$ is obtained, displacement is integrated:
$$\int_{s_0}^s ds = \int_0^t v(t) \, dt \implies s(t) = s_0 + \int_0^t v(t) \, dt$$

2. Case 2: Acceleration as a Function of Displacement, $a = f(s)$:
Separating variables in $v \, dv = a \, ds$:
$$\int_{v_0}^v v \, dv = \int_{s_0}^s f(s) \, ds \implies \frac{v^2 - v_0^2}{2} = \int_{s_0}^s f(s) \, ds \implies v(s) = \sqrt{v_0^2 + 2\int_{s_0}^s f(s) \, ds}$$
Time is then obtained by integrating $dt = \frac{ds}{v(s)}$:
$$t = \int_{s_0}^s \frac{ds}{v(s)}$$

3. Case 3: Acceleration as a Function of Velocity (Resisted Fluid Motion), $a = -k v$:
Consider a particle launched into a viscous fluid with initial velocity $v_0$ at $t = 0, s = 0$. The fluid exerts a resisting drag force proportional to velocity, resulting in deceleration:
$$a = \frac{dv}{dt} = -k v$$
where $k$ is a positive constant of drag per unit mass ($s^{-1}$).
- Velocity as a Function of Time:
Separating variables:
$$\frac{dv}{v} = -k \, dt$$
Integrating from initial velocity $v_0$ at $t = 0$ to velocity $v$ at time $t$:
$$\int_{v_0}^v \frac{dv}{v} = -k \int_0^t dt \implies \left[ \ln v \right]_{v_0}^v = -k t \implies \ln\left(\frac{v}{v_0}\right) = -k t$$
Exponentiating both sides:
$$v(t) = v_0 e^{-k t}$$
The velocity decays exponentially with time, approaching zero asymptotically as $t \to \infty$.

- Displacement as a Function of Time:
Substituting $v = \frac{ds}{dt}$:
$$\frac{ds}{dt} = v_0 e^{-k t} \implies ds = v_0 e^{-k t} \, dt$$
Integrating with initial condition $s(0) = 0$:
$$\int_0^s ds = v_0 \int_0^t e^{-k t} \, dt \implies s(t) = v_0 \left[ \frac{e^{-k t}}{-k} \right]_0^t = \frac{v_0}{k} \left(1 - e^{-k t}\right)$$
- Maximum Distance Traveled Before Coming to Rest:
As time approaches infinity ($t \to \infty$), $e^{-k t} \to 0$. The total stopping distance $s_{max}$ is finite:
$$s_{max} = \lim_{t \to \infty} \frac{v_0}{k}\left(1 - e^{-k t}\right) = \frac{v_0}{k}$$
Alternatively, using $a = v \frac{dv}{ds} = -kv \implies dv = -k \, ds$. Integrating from $v_0$ to $0$ gives $0 - v_0 = -k s_{max} \implies s_{max} = \frac{v_0}{k}$. This demonstrates the consistency of the differential approach.
"""
            },
            {
                "qid": "mech-q17",
                "marks": 7,
                "type": "Derivation",
                "title": "Projectile Motion: Trajectory Equation, Time of Flight, Maximum Height, and Range",
                "yt_query": "projectile motion derivation trajectory equation time of flight maximum height horizontal range",
                "img_path": "images/mechanics/projectile_motion.png",
                "img_caption": "Figure 4.2: Parabolic Trajectory of a Projectile Showing Velocity Vectors and Range",
                "answer": r"""
A projectile is any object projected into the atmosphere with an initial velocity that continues in motion under the sole influence of gravity (assuming air resistance is negligible). Because gravity acts purely in the vertical downward direction, the horizontal and vertical motions are independent.

Kinematic Formulation and Coordinate Setup:
Let a particle be projected from origin $O(0,0)$ with an initial velocity $u$ at an angle of projection $\theta$ with the horizontal $x$-axis.
Resolving initial velocity $u$ into Cartesian components:
- Initial horizontal velocity: $u_x = u \cos\theta$
- Initial vertical velocity: $u_y = u \sin\theta$

Governing Equations of Motion:
1. Horizontal Motion: Zero horizontal acceleration ($a_x = 0$):
The horizontal velocity remains constant throughout the flight:
$$v_x(t) = u_x = u \cos\theta$$
The horizontal displacement at any time $t$ is:
$$x(t) = (u \cos\theta) t \implies t = \frac{x}{u \cos\theta} \quad \text{--- (Equation 1)}$$
2. Vertical Motion: Downward gravitational acceleration ($a_y = -g$):
The vertical velocity at any time $t$ is:
$$v_y(t) = u \sin\theta - g t$$
The vertical displacement at time $t$ is:
$$y(t) = (u \sin\theta) t - \frac{1}{2} g t^2 \quad \text{--- (Equation 2)}$$

1. Derivation of the Equation of the Path (Trajectory):
To determine the geometric path, we eliminate time parameter $t$ by substituting Equation 1 into Equation 2:
$$y = (u \sin\theta) \left( \frac{x}{u \cos\theta} \right) - \frac{1}{2} g \left( \frac{x}{u \cos\theta} \right)^2$$
$$y = x \left(\frac{\sin\theta}{\cos\theta}\right) - \frac{g x^2}{2 u^2 \cos^2\theta} \implies y = x \tan\theta - \frac{g x^2}{2 u^2 \cos^2\theta}$$
This equation is of the standard quadratic form $y = A x - B x^2$ (where $A = \tan\theta$ and $B = \frac{g}{2u^2 \cos^2\theta}$ are constants). This proves that the trajectory of an unresisted projectile is a parabola with its vertex pointing upward.

2. Derivation of Time of Flight ($T$):
The total time of flight $T$ is the total elapsed time from projection until the projectile strikes the horizontal ground plane again ($y = 0$).
Setting $y = 0$ in the vertical displacement equation:
$$0 = (u \sin\theta) T - \frac{1}{2} g T^2 \implies T \left( u \sin\theta - \frac{1}{2} g T \right) = 0$$
Since $T \neq 0$ (which corresponds to launch):
$$u \sin\theta - \frac{1}{2} g T = 0 \implies \frac{1}{2} g T = u \sin\theta$$
$$T = \frac{2 u \sin\theta}{g}$$
The time to reach the maximum height $t_h$ (where vertical velocity vanishes, $v_y = 0 \implies u \sin\theta - g t_h = 0$) is exactly half the total time of flight:
$$t_h = \frac{u \sin\theta}{g} = \frac{T}{2}$$

3. Derivation of Maximum Vertical Height ($H$):
At the peak apex of the trajectory ($t = t_h = \frac{u \sin\theta}{g}$), the vertical displacement reaches its maximum value $H$.
Using the kinematic relation $v_y^2 = u_y^2 - 2g H$ with $v_y = 0$:
$$0 = (u \sin\theta)^2 - 2g H \implies 2g H = u^2 \sin^2\theta$$
$$H = \frac{u^2 \sin^2\theta}{2g}$$

4. Derivation of Horizontal Range ($R$) and Condition for Maximum Range:
The horizontal range $R$ is the horizontal distance covered during the entire time of flight $T$:
$$R = x(T) = (u \cos\theta) \cdot T = (u \cos\theta) \left( \frac{2 u \sin\theta}{g} \right) = \frac{u^2 (2 \sin\theta \cos\theta)}{g}$$
Using the trigonometric identity $2 \sin\theta \cos\theta = \sin(2\theta)$:
$$R = \frac{u^2 \sin(2\theta)}{g}$$

Condition for Maximum Horizontal Range ($R_{max}$):
For a given launch velocity $u$, the range $R$ depends solely on the launch angle $\theta$. To find the angle that maximizes $R$:
$$\frac{dR}{d\theta} = \frac{u^2}{g} \frac{d}{d\theta}[\sin(2\theta)] = \frac{u^2}{g} [2 \cos(2\theta)] = 0$$
$$\cos(2\theta) = 0 \implies 2\theta = 90^\circ \implies \theta = 45^\circ$$
The maximum horizontal range is achieved at a projection angle of $45^\circ$:
$$R_{max} = \frac{u^2 \sin(90^\circ)}{g} = \frac{u^2}{g}$$
For any range $R < R_{max}$, two complementary launch angles ($\theta$ and $90^\circ - \theta$) produce the exact same horizontal range, since $\sin[2(90^\circ - \theta)] = \sin(180^\circ - 2\theta) = \sin(2\theta)$.
"""
            },
            {
                "qid": "mech-q18",
                "marks": 7,
                "type": "Derivation",
                "title": "Normal and Tangential Acceleration in Curvilinear Motion",
                "yt_query": "normal and tangential acceleration derivation curvilinear motion engineering mechanics",
                "img_path": "images/mechanics/normal_tangential_acceleration.png",
                "img_caption": "Figure 4.3: Intrinsic Coordinate System Showing Tangential and Normal Acceleration Vectors",
                "answer": r"""
When a particle moves along a general curved path in a two-dimensional plane, its velocity vector changes continuously in both magnitude (speed) and spatial direction. While Cartesian coordinates $(x,y)$ are often convenient, describing motion using the intrinsic coordinate system defined by Tangential ($\hat{\mathbf{e}}_t$) and Normal ($\hat{\mathbf{e}}_n$) unit vectors provides direct physical insight into the dynamics of curved motion.

Intrinsic Coordinate System Formulation:
Let a particle move along a planar curve described by path arc length $s(t)$. At any point $P$ along the trajectory:
- Tangential Unit Vector $\hat{\mathbf{e}}_t$: Directed tangent to the path curve pointing in the direction of increasing arc length $s$ (direction of motion).
- Principal Normal Unit Vector $\hat{\mathbf{e}}_n$: Directed perpendicular to the tangent, pointing inwards toward the instantaneous center of curvature $C$ of the path.
By fundamental definition, the velocity vector $\mathbf{v}$ is always directed along the instantaneous tangent:
$$\mathbf{v} = v \, \hat{\mathbf{e}}_t = \left(\frac{ds}{dt}\right) \hat{\mathbf{e}}_t$$
where $v = \frac{ds}{dt}$ is the scalar speed of the particle.

Derivation of the Acceleration Vector:
The acceleration vector $\mathbf{a}$ is the total time derivative of the velocity vector:
$$\mathbf{a} = \frac{d\mathbf{v}}{dt} = \frac{d}{dt}\left( v \, \hat{\mathbf{e}}_t \right)$$
Applying the product rule of differentiation:
$$\mathbf{a} = \frac{dv}{dt} \hat{\mathbf{e}}_t + v \frac{d\hat{\mathbf{e}}_t}{dt} \quad \text{--- (Equation 1)}$$

To evaluate the time derivative of the unit tangent vector $\frac{d\hat{\mathbf{e}}_t}{dt}$:
Let the particle move a differential distance $ds$ from point $P$ to a neighboring point $P'$ along the curve in time $dt$.
At point $P$, the tangent is inclined at angle $\theta$ to a fixed reference direction.
At point $P'$, the tangent is inclined at angle $\theta + d\theta$.
The change in the unit tangent vector is $d\hat{\mathbf{e}}_t = \hat{\mathbf{e}}_t(P') - \hat{\mathbf{e}}_t(P)$.
Because $\hat{\mathbf{e}}_t$ has constant unit magnitude ($|\hat{\mathbf{e}}_t| = 1$), the vector triangle formed by $\hat{\mathbf{e}}_t$, $\hat{\mathbf{e}}_t + d\hat{\mathbf{e}}_t$, and $d\hat{\mathbf{e}}_t$ is an isosceles triangle with vertex angle $d\theta$.
For an infinitesimal angle $d\theta$:
$$|d\hat{\mathbf{e}}_t| \approx 1 \cdot d\theta = d\theta$$
As $dt \to 0$, the vector $d\hat{\mathbf{e}}_t$ becomes perpendicular to $\hat{\mathbf{e}}_t$ and points toward the inside of the curve (in the direction of the normal unit vector $\hat{\mathbf{e}}_n$).
Therefore, in vector form:
$$d\hat{\mathbf{e}}_t = d\theta \, \hat{\mathbf{e}}_n$$
Dividing by differential time $dt$:
$$\frac{d\hat{\mathbf{e}}_t}{dt} = \frac{d\theta}{dt} \hat{\mathbf{e}}_n = \left(\frac{d\theta}{ds} \cdot \frac{ds}{dt}\right) \hat{\mathbf{e}}_n$$
From differential geometry, the curvature of a plane curve is $\kappa = \frac{d\theta}{ds} = \frac{1}{\rho}$, where $\rho$ is the instantaneous Radius of Curvature.
Since $\frac{ds}{dt} = v$:
$$\frac{d\hat{\mathbf{e}}_t}{dt} = \left(\frac{1}{\rho} \cdot v\right) \hat{\mathbf{e}}_n = \frac{v}{\rho} \hat{\mathbf{e}}_n \quad \text{--- (Equation 2)}$$

Substituting Equation 2 back into Equation 1 yields the complete acceleration vector:
$$\mathbf{a} = \frac{dv}{dt} \hat{\mathbf{e}}_t + \frac{v^2}{\rho} \hat{\mathbf{e}}_n = a_t \hat{\mathbf{e}}_t + a_n \hat{\mathbf{e}}_n$$

Physical Interpretation of Acceleration Components:
1. Tangential Acceleration Component ($a_t$):
$$a_t = \frac{dv}{dt} = \dot{v} = v \frac{dv}{ds} = \frac{d^2 s}{dt^2}$$
$a_t$ measures the time rate of change of the magnitude of velocity (speed).
- If the particle speeds up, $a_t > 0$ (points in the direction of motion, $+\hat{\mathbf{e}}_t$).
- If the particle slows down (brakes), $a_t < 0$ (opposes motion, $-\hat{\mathbf{e}}_t$).
- In uniform circular motion (constant speed), $a_t = 0$.
2. Normal (Centripetal) Acceleration Component ($a_n$):
$$a_n = \frac{v^2}{\rho}$$
$a_n$ measures the time rate of change of the direction of the velocity vector.
- It is always directed perpendicular to the path inward toward the center of curvature ($+\hat{\mathbf{e}}_n$).
- $a_n$ can never be negative, and is zero only if the path is a straight line ($\rho \to \infty$).

Resultant Acceleration Magnitude and Direction:
Because the tangential and normal unit vectors are mutually orthogonal ($\hat{\mathbf{e}}_t \cdot \hat{\mathbf{e}}_n = 0$), the total acceleration magnitude is:
$$a = \sqrt{a_t^2 + a_n^2} = \sqrt{\left(\frac{dv}{dt}\right)^2 + \left(\frac{v^2}{\rho}\right)^2}$$
The angle $\phi$ between total acceleration $\mathbf{a}$ and the tangential direction of motion is:
$$\tan\phi = \frac{a_n}{a_t} = \frac{v^2 / \rho}{dv / dt} \implies \phi = \tan^{-1}\left(\frac{a_n}{a_t}\right)$$
"""
            },
            {
                "qid": "mech-q19",
                "marks": 7,
                "type": "Theory & Application",
                "title": "Newton's Second Law and D'Alembert's Principle: Dynamic Equilibrium of Connected Bodies",
                "yt_query": "dalemberts principle dynamic equilibrium connected bodies atwood machine mechanics",
                "img_path": "images/mechanics/dalembert_principle.png",
                "img_caption": "Figure 4.4: Dynamic Equilibrium of Accelerating Elevator and Connected Pulley System Using Inertia Forces",
                "answer": r"""
Sir Isaac Newton's Second Law of Motion forms the foundation of classical particle kinetics: the net external force $\Sigma \mathbf{F}$ acting on a particle of constant mass $m$ produces an acceleration $\mathbf{a}$ directly proportional to the force and in the same direction:
$$\Sigma \mathbf{F} = m \mathbf{a}$$
While Newton's formulation describes a dynamic non-equilibrium state, in 1743 French mathematician Jean le Rond d'Alembert proposed a principle that transforms dynamic problems into equivalent static equilibrium problems.

D'Alembert's Principle of Dynamic Equilibrium:
D'Alembert's principle states that a system of particles or a rigid body undergoing accelerated motion can be brought into a state of dynamic equilibrium by adding an imaginary force called the Inertia Force (or reverse-effective force) to the system of actual external forces.
The Inertia Force $\mathbf{F}_i$ is defined mathematically as the negative product of mass and acceleration:
$$\mathbf{F}_i = -m \mathbf{a}$$
Adding the inertia force to Newton's second law:
$$\Sigma \mathbf{F} + (-m \mathbf{a}) = 0 \implies \Sigma \mathbf{F} + \mathbf{F}_i = 0$$
Statement of the Principle:
The vector sum of all external physical forces acting on a body and the fictitious inertia force is identically equal to zero.
This formulation allows engineers to analyze complex dynamic mechanisms using the familiar methods of statics:
$$\Sigma F_x = 0, \quad \Sigma F_y = 0, \quad \Sigma M_O = 0$$

Application 1: Apparent Weight in an Accelerating Elevator:
Consider a passenger of mass $m$ standing on a weighing scale inside an elevator cab undergoing vertical acceleration $a$.
Forces acting on the passenger:
- Real external forces: Downward weight $W = mg$ ($\downarrow$), Upward normal reaction $N$ from scale ($\uparrow$).
- Fictitious inertia force: $\mathbf{F}_i = -m\mathbf{a}$.
1. Elevator Accelerating Upward ($+a \uparrow$):
The inertia force acts downward: $F_i = ma$ ($\downarrow$).
Applying dynamic equilibrium ($\Sigma F_y = 0$):
$$N - mg - ma = 0 \implies N = m(g + a)$$
The weighing scale reads an increased apparent weight ($N > mg$).
2. Elevator Accelerating Downward ($-a \downarrow$):
The inertia force acts upward: $F_i = ma$ ($\uparrow$).
Applying dynamic equilibrium:
$$N + ma - mg = 0 \implies N = m(g - a)$$
The apparent weight decreases ($N < mg$).
3. Free Fall ($a = g \downarrow$):
$$N = m(g - g) = 0$$
The passenger experiences apparent weightlessness.

Application 2: Atwood's Machine (Connected Bodies Over a Smooth Pulley):
Problem Statement: Two bodies of unequal masses $m_1$ and $m_2$ ($m_1 > m_2$) are suspended from the ends of a light, flexible, inextensible cord passing over a frictionless, massless pulley. Determine the common acceleration $a$ of the system and the tension $T$ in the cord using D'Alembert's principle.

Analytical Solution Using Dynamic Equilibrium:
Because the cord is inextensible, mass $m_1$ accelerates downward with acceleration $a$ ($\downarrow$), while mass $m_2$ accelerates upward with the identical acceleration $a$ ($\uparrow$).
1. Dynamic Equilibrium of Mass $m_1$:
Real forces: Downward weight $m_1 g$ ($\downarrow$), Upward cable tension $T$ ($\uparrow$).
Since acceleration is downward, the inertia force acts upward: $F_{i1} = m_1 a$ ($\uparrow$).
Applying static equilibrium condition ($\Sigma F_y = 0$):
$$T + m_1 a - m_1 g = 0 \implies T = m_1(g - a) \quad \text{--- (Equation 1)}$$

2. Dynamic Equilibrium of Mass $m_2$:
Real forces: Downward weight $m_2 g$ ($\downarrow$), Upward cable tension $T$ ($\uparrow$).
Since acceleration is upward, the inertia force acts downward: $F_{i2} = m_2 a$ ($\downarrow$).
Applying static equilibrium condition ($\Sigma F_y = 0$):
$$T - m_2 g - m_2 a = 0 \implies T = m_2(g + a) \quad \text{--- (Equation 2)}$$

3. Solving for Common Acceleration $a$:
Equating Equations 1 and 2:
$$m_1(g - a) = m_2(g + a)$$
$$m_1 g - m_1 a = m_2 g + m_2 a$$
Rearranging terms:
$$(m_1 + m_2) a = (m_1 - m_2) g$$
$$a = \left(\frac{m_1 - m_2}{m_1 + m_2}\right) g$$

4. Solving for Cord Tension $T$:
Substituting $a$ into Equation 2:
$$T = m_2 \left[ g + \left(\frac{m_1 - m_2}{m_1 + m_2}\right) g \right] = m_2 g \left[ 1 + \frac{m_1 - m_2}{m_1 + m_2} \right] = m_2 g \left[ \frac{m_1 + m_2 + m_1 - m_2}{m_1 + m_2} \right]$$
$$T = \left(\frac{2 m_1 m_2}{m_1 + m_2}\right) g$$
This demonstrates how D'Alembert's principle transforms dynamic systems into straightforward static force balance equations.
"""
            },
            {
                "qid": "mech-q20",
                "marks": 7,
                "type": "Theory & Application",
                "title": "Connected Bodies on Rough Inclined Planes: Complete Equations of Motion and Tension",
                "yt_query": "connected bodies rough inclined plane friction pulley acceleration tension mechanics",
                "img_path": "images/mechanics/inclined_plane_connected.png",
                "img_caption": "Figure 4.5: Free Body Diagrams for Block on Rough Incline Connected to Hanging Weight via Pulley",
                "answer": r"""
A fundamental problem in engineering mechanics involves the dynamic motion of interconnected bodies where one mass slides along a rough inclined plane while connected by a flexible cord over a pulley to a second hanging mass. This configuration models hoist haulage systems, inclined conveyor lines, and mine shaft cars.

System Description and Free Body Formulation:
Consider a body $A$ of mass $m_1$ resting on a rough plane inclined at angle $\alpha$ to the horizontal. The coefficient of kinetic friction between body $A$ and the plane is $\mu$. A light, flexible, inextensible cord attached to body $A$ passes over a smooth, frictionless, massless pulley fixed at the apex of the incline, supporting a hanging body $B$ of mass $m_2$ at its opposite end.
Assume mass $m_2$ is sufficiently heavy to pull mass $m_1$ up the inclined plane with an acceleration $a$.
- Mass $m_1$ moves up the incline with acceleration $a$ directed parallel to the slope ($\nearrow$).
- Mass $m_2$ moves vertically downward with acceleration $a$ ($\downarrow$).
Both bodies share the same acceleration magnitude $a$ due to cord inextensibility, and the tension $T$ is uniform throughout the cord.

1. Analysis of Body $A$ on the Rough Incline (Moving Upward):
Set up a tilted Cartesian coordinate system with the $x$-axis parallel to the incline pointing upward ($\nearrow$) and the $y$-axis perpendicular to the incline pointing outward ($\nwarrow$).
Forces acting on mass $m_1$:
- Weight $W_1 = m_1 g$ acting vertically downward ($\downarrow$).
  Resolving into components:
  - Perpendicular to incline: $m_1 g \cos\alpha$ ($-\hat{\mathbf{j}}$)
  - Parallel to incline acting down the slope: $m_1 g \sin\alpha$ ($-\hat{\mathbf{i}}$)
- Normal reaction $N$ exerted by the incline on $m_1$ ($+\hat{\mathbf{j}}$).
- Cable tension $T$ pulling up the incline ($+\hat{\mathbf{i}}$).
- Kinetic friction force $F_k = \mu N$. Because the block moves up the slope, friction acts down the slope ($-\hat{\mathbf{i}}$) opposing motion.

Applying equilibrium perpendicular to the incline ($\Sigma F_y = 0$):
$$N - m_1 g \cos\alpha = 0 \implies N = m_1 g \cos\alpha$$
The kinetic friction force is therefore:
$$F_k = \mu N = \mu m_1 g \cos\alpha$$
Applying Newton's second law / D'Alembert's dynamic equilibrium along the incline ($\Sigma F_x = m_1 a$):
$$T - m_1 g \sin\alpha - F_k = m_1 a$$
Substituting $F_k$:
$$T - m_1 g \sin\alpha - \mu m_1 g \cos\alpha = m_1 a \quad \text{--- (Equation 1)}$$
Solving for tension $T$:
$$T = m_1 a + m_1 g (\sin\alpha + \mu \cos\alpha)$$

2. Analysis of Hanging Body $B$ (Moving Downward):
Forces acting on hanging mass $m_2$:
- Downward gravitational weight: $m_2 g$ ($\downarrow$).
- Upward cable tension: $T$ ($\uparrow$).
Applying Newton's second law in the downward direction ($\Sigma F_y = m_2 a$):
$$m_2 g - T = m_2 a \quad \text{--- (Equation 2)}$$
Solving for tension $T$:
$$T = m_2 (g - a)$$

3. Derivation of Common System Acceleration ($a$):
Adding Equation 1 and Equation 2 eliminates the internal cord tension $T$:
$$(T - m_1 g \sin\alpha - \mu m_1 g \cos\alpha) + (m_2 g - T) = m_1 a + m_2 a$$
$$m_2 g - m_1 g (\sin\alpha + \mu \cos\alpha) = (m_1 + m_2) a$$
Factoring out $g$:
$$g \left[ m_2 - m_1(\sin\alpha + \mu \cos\alpha) \right] = (m_1 + m_2) a$$
Dividing by total system mass $(m_1 + m_2)$ gives the acceleration:
$$a = \frac{m_2 - m_1(\sin\alpha + \mu \cos\alpha)}{m_1 + m_2} g$$

Condition for Motion to Occur:
For mass $m_1$ to accelerate up the incline ($a > 0$), the numerator must be strictly positive:
$$m_2 > m_1(\sin\alpha + \mu \cos\alpha)$$
If $m_2 < m_1(\sin\alpha - \mu \cos\alpha)$, the block will accelerate down the incline (reversing the sign of friction).
If $m_2$ falls between these two limits, the system remains in static equilibrium at rest ($a = 0$).

4. Derivation of Cable Tension ($T$):
Substituting the acceleration expression $a$ back into Equation 2:
$$T = m_2 (g - a) = m_2 \left[ g - \frac{m_2 - m_1(\sin\alpha + \mu \cos\alpha)}{m_1 + m_2} g \right]$$
$$T = \frac{m_2 g}{m_1 + m_2} \left[ (m_1 + m_2) - m_2 + m_1(\sin\alpha + \mu \cos\alpha) \right]$$
$$T = \frac{m_1 m_2 g}{m_1 + m_2} \left[ 1 + \sin\alpha + \mu \cos\alpha \right]$$
This closed-form solution yields both the motion acceleration and internal cable tension for the connected system.
"""
            }
        ]
    },
    {
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
    },
]

MECHANICS_BYHEART = {
    "mech-q1": {
        "eq": r"""$$R = \sqrt{(\Sigma F_x)^2 + (\Sigma F_y)^2}, \quad \tan\theta_R = \left|\frac{\Sigma F_y}{\Sigma F_x}\right|, \quad \Sigma F_x = 0, \; \Sigma F_y = 0$$""",
        "text": r"""<strong>Parallelogram Law:</strong> $R = \sqrt{P^2 + Q^2 + 2PQ\cos\theta}$, $\tan\alpha = \frac{Q\sin\theta}{P + Q\cos\theta}$.<br><strong>Transmissibility Principle:</strong> Point of application can slide along line of action on a rigid body without altering external equilibrium.<br><strong>Cartesian Resolution:</strong> $R = \sqrt{(\Sigma F_x)^2 + (\Sigma F_y)^2}$.<br><strong>Equilibrium:</strong> Resultant must vanish ($\Sigma F_x = 0$, $\Sigma F_y = 0$)."""
    },
    "mech-q2": {
        "eq": r"""$$\frac{F_1}{\sin\alpha} = \frac{F_2}{\sin\beta} = \frac{F_3}{\sin\gamma}, \quad T = W \frac{l + r}{\sqrt{l^2 + 2lr}}, \quad R_w = W \frac{r}{\sqrt{l^2 + 2lr}}$$""",
        "text": r"""<strong>Lami's Theorem:</strong> For 3 concurrent coplanar forces in equilibrium, each force is proportional to the sine of the angle between the other two.<br><strong>Closed Triangle:</strong> Proved using the Sine Rule on the closed force triangle ($\Delta ABC$).<br><strong>Suspended Sphere:</strong> Normal reaction $R_w = W\tan\theta$, Tension $T = W/\cos\theta$ where $\sin\theta = \frac{r}{l+r}$."""
    },
    "mech-q3": {
        "eq": r"""$$R_{AB} = \frac{W_B}{\sin\theta} = 1250\text{ N}, \quad R_{wall} = 750\text{ N}, \quad R_{floor} = W_A + W_B = 2000\text{ N}$$""",
        "text": r"""<strong>Free Body Diagram (FBD):</strong> Isolate body and replace all supports with physical reactions.<br><strong>Line of Centers:</strong> Distance between centers $d = 2R$; horizontal span $\Delta x = L - 2R \implies \cos\theta = \Delta x / 2R$.<br><strong>Two Cylinders in Channel:</strong> Top cylinder equilibrium gives mutual contact reaction $R_{AB} = W/\sin\theta$ and wall reaction $R_{wall} = R_{AB}\cos\theta$."""
    },
    "mech-q4": {
        "eq": r"""$$\Sigma \mathbf{M}_O = \mathbf{r} \times \mathbf{R} \implies \sum_{i=1}^n F_i d_i = R \cdot d_R, \quad \mathbf{M}_{\text{couple}} = \mathbf{r}_{BA} \times \mathbf{F}$$""",
        "text": r"""<strong>Varignon's Theorem of Moments:</strong> The algebraic sum of moments of concurrent forces about any point equals the moment of their resultant about that point ($\Sigma M_O = M_{R, O}$).<br><strong>Couple Characteristics:</strong> Net force is zero; moment $M = F \cdot d$ is a free vector, identical about all points.<br><strong>Force Shift:</strong> Shifting force $F$ by perpendicular distance $d$ requires adding a couple $M = F \cdot d$."""
    },
    "mech-q5": {
        "eq": r"""$$\Sigma F_x = 0, \quad \Sigma F_y = 0, \quad \Sigma M_O = 0, \quad R = \sqrt{R_x^2 + R_y^2}$$""",
        "text": r"""<strong>2D Rigid Body Equilibrium:</strong> Requires 3 independent equations ($\Sigma F_x = 0, \Sigma F_y = 0, \Sigma M = 0$).<br><strong>Support Reactions:</strong><br>- Roller: 1 normal reaction ($R_N$).<br>- Pin/Hinged: 2 orthogonal reactions ($R_x, R_y$).<br>- Fixed: 3 reactions ($R_x, R_y, M_{\text{fix}}$).<br><strong>UDL Conversion:</strong> Replaced by equivalent point load $W = w \cdot L$ at segment centroid."""
    },
    "mech-q6": {
        "eq": r"""$$F_L = \mu_s N, \quad \tan\phi = \mu_s \implies \phi = \tan^{-1}\mu_s, \quad \theta_{\text{repose}} = \phi = \tan^{-1}\mu_s$$""",
        "text": r"""<strong>Coulomb's Friction Laws:</strong> Limiting friction $F_L = \mu_s N$ is independent of contact area; kinetic friction $\mu_k < \mu_s$.<br><strong>Angle of Friction ($\phi$):</strong> Angle between total reaction $R$ and normal $N$: $\tan\phi = \mu_s$.<br><strong>Angle of Repose ($\theta$):</strong> Maximum incline angle before sliding down under self-weight: $\tan\theta = \mu_s \implies \theta = \phi$.<br><strong>Cone of Friction:</strong> Inverted cone of semi-vertex angle $\phi$; forces inside cone cannot cause slip."""
    },
    "mech-q7": {
        "eq": r"""$$\tan\theta_{min} = \frac{1 - \mu_f \mu_w}{2\mu_f}, \quad \text{Smooth Wall: } \tan\theta_{min} = \frac{1}{2\mu_f}, \quad x_{max} = \frac{N_w L(\tan\theta + \mu_w) - \frac{W L}{2}}{W_1}$$""",
        "text": r"""<strong>Ladder Equilibrium:</strong> Floor friction $F_f = \mu_f N_f \rightarrow$, wall reaction $N_w \leftarrow$, wall friction $F_w = \mu_w N_w \uparrow$.<br><strong>Force Balance:</strong> $N_w = \mu_f N_f$, $N_f + \mu_w N_w = W \implies N_f = \frac{W}{1+\mu_f\mu_w}$.<br><strong>Minimum Angle:</strong> Taking $\Sigma M_A = 0$ yields $\tan\theta_{min} = \frac{1 - \mu_f\mu_w}{2\mu_f}$."""
    },
    "mech-q8": {
        "eq": r"""$$P = W \left[ \frac{\cos\phi_1}{\cos(\alpha + \phi_1 + \phi_2)} \right] \left[ \frac{\sin(\alpha + \phi_2 + \phi_3)}{\cos\phi_3} \right] \xrightarrow{\text{equal }\phi} P = W \tan(\alpha + 2\phi)$$""",
        "text": r"""<strong>Wedge Mechanism:</strong> Translates small horizontal effort $P$ into large vertical lifting force $W$.<br><strong>Block & Wedge Equilibrium:</strong> Reaction between block and wedge tilts by $(\alpha + \phi_2)$ to the vertical.<br><strong>Minimum Driving Force:</strong> $P = W\tan(\alpha + 2\phi)$ for equal friction angle $\phi$.<br><strong>Self-Locking:</strong> Wedge will not slip back when $P=0$ if $\alpha < 2\phi$."""
    },
    "mech-q9": {
        "eq": r"""$$\frac{T_1}{T_2} = e^{\mu \theta}, \quad P = (T_1 - T_2)v = T_1(1 - e^{-\mu\theta})v, \quad T_c = m v^2$$""",
        "text": r"""<strong>Flat Belt Tension Ratio:</strong> $\frac{T_1}{T_2} = e^{\mu\theta}$ where $\theta$ is wrap angle in radians.<br><strong>Power Transmitted:</strong> $P = (T_1 - T_2)v$ where pitch speed $v = \frac{\pi D N}{60}\text{ m/s}$.<br><strong>Centrifugal Tension:</strong> $T_c = m v^2$; reduces grip $\frac{T_1 - T_c}{T_2 - T_c} = e^{\mu\theta}$; maximum power occurs when $T_c = T_{max}/3$."""
    },
    "mech-q10": {
        "eq": r"""$$m = 2j - 3 \text{ (Perfect Truss)}, \quad \Sigma F_x = 0, \; \Sigma F_y = 0 \text{ (Joints)}, \quad \Sigma M_O = 0 \text{ (Sections)}$$""",
        "text": r"""<strong>Truss Assumptions:</strong> Frictionless pin joints, concurrent axes, axial loads only ($T$ tension or $C$ compression).<br><strong>Zero-Force Members:</strong> Two non-collinear members meeting at unloaded joint carry zero force; two collinear plus one third non-collinear $\implies$ third is zero.<br><strong>Method of Joints:</strong> Analyzes joint by joint ($\Sigma F_x=0, \Sigma F_y=0$).<br><strong>Method of Sections:</strong> Cuts across up to 3 members; solves with $\Sigma M_O = 0$."""
    },
    "mech-q11": {
        "eq": r"""$$\bar{x} = \frac{\sum A_i x_i}{\sum A_i}, \quad \bar{y} = \frac{\sum A_i y_i}{\sum A_i}, \quad Q_x = \int y \, dA = A \bar{y}$$""",
        "text": r"""<strong>Centroid of Area:</strong> Geometric center based on first moment of area: $A \bar{y} = \Sigma A_i y_i$.<br><strong>Axis of Symmetry:</strong> If a section possesses an axis of symmetry, the centroid must lie on that axis.<br><strong>Composite T-Section:</strong> Web ($20\times 180$) and Flange ($150\times 20$) give total area $6600\text{ mm}^2$ and $\bar{y} = \frac{894,000}{6600} = 135.45\text{ mm}$ from base."""
    },
    "mech-q12": {
        "eq": r"""$$A = 2\pi \bar{y} L \quad (\text{Theorem 1}), \quad V = 2\pi \bar{y} A \quad (\text{Theorem 2})$$""",
        "text": r"""<strong>Pappus Theorem 1:</strong> Surface area of revolution equals curve length $L$ times distance traveled by its centroid ($2\pi \bar{y} L$).<br><strong>Pappus Theorem 2:</strong> Volume of revolution equals plane area $A$ times distance traveled by its centroid ($2\pi \bar{y} A$).<br><strong>Applications:</strong> Sphere ($A = 4\pi R^2, V = \frac{4}{3}\pi R^3$), Cone ($V = \frac{1}{3}\pi R^2 h$)."""
    },
    "mech-q13": {
        "eq": r"""$$I_{AB} = I_G + A d^2 \quad (\text{Parallel Axis}), \quad I_{zz} = I_{xx} + I_{yy} \quad (\text{Perpendicular Axis})$$""",
        "text": r"""<strong>Parallel Axis Theorem:</strong> $I_{AB} = I_G + A d^2$; first moment $\int y' dA = 0$ about centroid.<br><strong>Perpendicular Axis Theorem:</strong> $I_{zz} = I_{xx} + I_{yy}$; valid strictly for planar 2D laminas.<br><strong>Radius of Gyration:</strong> $k = \sqrt{I/A} \implies I = A k^2$."""
    },
    "mech-q14": {
        "eq": r"""$$I_{xx} = \sum \left( \frac{b_i h_i^3}{12} + A_i d_i^2 \right) \approx 54.82 \times 10^6\text{ mm}^4, \quad I_{yy} = \sum \frac{h_i b_i^3}{12} \approx 16.26 \times 10^6\text{ mm}^4$$""",
        "text": r"""<strong>I-Section Centroidal MOI:</strong> Calculate $\bar{y}$ using first moments, then apply parallel axis theorem to each rectangle: $I_{xx} = I_G + A d^2$.<br><strong>Symmetry about Y-Axis:</strong> All $d_x = 0 \implies I_{yy} = \sum \frac{h b^3}{12}$.<br><strong>Radii of Gyration:</strong> $k_{xx} = \sqrt{I_{xx}/A} \approx 78.93\text{ mm}$, $k_{yy} = \sqrt{I_{yy}/A} \approx 42.98\text{ mm}$."""
    },
    "mech-q15": {
        "eq": r"""$$I_{\text{rod}, G} = \frac{1}{12} m L^2, \quad I_{\text{rod}, \text{end}} = \frac{1}{3} m L^2, \quad I_{\text{disc}, z} = \frac{1}{2} m R^2, \quad I_{\text{disc}, d} = \frac{1}{4} m R^2$$""",
        "text": r"""<strong>Mass Moment of Inertia:</strong> $I = \int r^2 dm$, measures resistance to angular acceleration ($T = I \alpha$).<br><strong>Slender Rod:</strong> Centroidal transverse axis $I_G = \frac{1}{12} m L^2$; about one end $I = I_G + m(L/2)^2 = \frac{1}{3} m L^2$.<br><strong>Circular Disc:</strong> Polar axis $I_z = \frac{1}{2} m R^2$; diameter axis $I_d = \frac{1}{4} m R^2$ (perpendicular axis theorem)."""
    },
    "mech-q16": {
        "eq": r"""$$a = \frac{dv}{dt} = v \frac{dv}{ds}, \quad a = -k v \implies v(t) = v_0 e^{-k t}, \quad s(t) = \frac{v_0}{k}(1 - e^{-k t}), \quad s_{max} = \frac{v_0}{k}$$""",
        "text": r"""<strong>Variable Acceleration:</strong> Use $v = ds/dt$, $a = dv/dt$, or $v \, dv = a \, ds$ based on independent variables.<br><strong>Linear Drag ($a = -kv$):</strong> Velocity decays exponentially $v = v_0 e^{-kt}$.<br><strong>Stopping Distance:</strong> Particle comes to rest asymptotically with total distance $s_{max} = v_0/k$."""
    },
    "mech-q17": {
        "eq": r"""$$y = x \tan\theta - \frac{g x^2}{2 u^2 \cos^2\theta}, \quad T = \frac{2 u \sin\theta}{g}, \quad H = \frac{u^2 \sin^2\theta}{2g}, \quad R = \frac{u^2 \sin(2\theta)}{g}$$""",
        "text": r"""<strong>Parabolic Trajectory:</strong> Eliminating time $t$ gives $y = x\tan\theta - \frac{gx^2}{2u^2\cos^2\theta}$.<br><strong>Time of Flight:</strong> $T = \frac{2u\sin\theta}{g}$ ($y=0$).<br><strong>Max Height:</strong> $H = \frac{u^2\sin^2\theta}{2g}$ ($v_y=0$).<br><strong>Horizontal Range:</strong> $R = \frac{u^2\sin 2\theta}{g}$; maximum range occurs at $\theta = 45^\circ$ ($R_{max} = u^2/g$)."""
    },
    "mech-q18": {
        "eq": r"""$$\mathbf{a} = a_t \hat{\mathbf{e}}_t + a_n \hat{\mathbf{e}}_n = \frac{dv}{dt} \hat{\mathbf{e}}_t + \frac{v^2}{\rho} \hat{\mathbf{e}}_n, \quad a = \sqrt{a_t^2 + a_n^2}$$""",
        "text": r"""<strong>Tangential Acceleration ($a_t$):</strong> $a_t = \frac{dv}{dt} = v\frac{dv}{ds}$, measures rate of change of speed along path tangent.<br><strong>Normal Acceleration ($a_n$):</strong> $a_n = \frac{v^2}{\rho}$, measures rate of change of direction, always directed inward toward center of curvature.<br><strong>Curvature:</strong> $\rho$ is radius of curvature; $a_n = 0$ only for straight path ($\rho \to \infty$)."""
    },
    "mech-q19": {
        "eq": r"""$$\Sigma \mathbf{F} + (-m \mathbf{a}) = 0 \implies \Sigma \mathbf{F} + \mathbf{F}_i = 0, \quad a = \left(\frac{m_1 - m_2}{m_1 + m_2}\right) g, \quad T = \left(\frac{2 m_1 m_2}{m_1 + m_2}\right) g$$""",
        "text": r"""<strong>D'Alembert's Principle:</strong> Dynamic systems brought to static equilibrium by adding reverse inertia force $\mathbf{F}_i = -m\mathbf{a}$.<br><strong>Accelerating Elevator:</strong> Upward $\implies N = m(g+a)$; Downward $\implies N = m(g-a)$; Free fall $\implies N = 0$.<br><strong>Atwood Machine:</strong> Common acceleration $a = \frac{m_1 - m_2}{m_1 + m_2}g$, string tension $T = \frac{2m_1 m_2}{m_1 + m_2}g$."""
    },
    "mech-q20": {
        "eq": r"""$$a = \frac{m_2 - m_1(\sin\alpha + \mu \cos\alpha)}{m_1 + m_2} g, \quad T = \frac{m_1 m_2 g}{m_1 + m_2}(1 + \sin\alpha + \mu \cos\alpha)$$""",
        "text": r"""<strong>Connected Incline Dynamics:</strong> Normal reaction $N = m_1 g \cos\alpha$; friction $F_k = \mu m_1 g \cos\alpha$.<br><strong>Force Balance:</strong> $T - m_1 g\sin\alpha - \mu m_1 g\cos\alpha = m_1 a$, and $m_2 g - T = m_2 a$.<br><strong>Motion Threshold:</strong> Mass accelerates up incline only if $m_2 > m_1(\sin\alpha + \mu\cos\alpha)$."""
    },
    "mech-q21": {
        "eq": r"""$$U_{1-2} = \int_1^2 \mathbf{F} \cdot d\mathbf{r} = T_2 - T_1 = \frac{1}{2} m v_2^2 - \frac{1}{2} m v_1^2 = \Delta KE$$""",
        "text": r"""<strong>Work Done:</strong> $U = \int \mathbf{F}\cdot d\mathbf{r}$; Gravity $U_g = -mg(y_2 - y_1)$; Spring $U_s = -\frac{1}{2}k(x_2^2 - x_1^2)$.<br><strong>Work-Energy Theorem:</strong> $F_t = m v \frac{dv}{ds} \implies \int F_t ds = \int mv dv \implies U_{1-2} = T_2 - T_1$.<br><strong>Key Advantage:</strong> Directly links force and displacement without calculating elapsed time."""
    },
    "mech-q22": {
        "eq": r"""$$\oint \mathbf{F}\cdot d\mathbf{r} = 0, \quad \mathbf{F} = -\nabla V, \quad T_1 + V_1 = T_2 + V_2 = E_{\text{total}} = \text{constant}$$""",
        "text": r"""<strong>Conservative Force:</strong> Work done is path-independent ($\nabla \times \mathbf{F} = 0$); derived from potential $F = -\nabla V$.<br><strong>Conservation of Mechanical Energy:</strong> When non-conservative forces do no work, $T_1 + V_1 = T_2 + V_2$.<br><strong>Simple Pendulum:</strong> Velocity at angle $\theta$ is $v = \sqrt{2gl(\cos\theta - \cos\theta_0)}$; cord tension does zero work."""
    },
    "mech-q23": {
        "eq": r"""$$\mathbf{J}_{1-2} = \int_{t_1}^{t_2} \mathbf{F} \, dt = m \mathbf{v}_2 - m \mathbf{v}_1 = \Delta \mathbf{p}, \quad R_{jet, x} = \rho A v^2 (1 - \cos\beta)$$""",
        "text": r"""<strong>Linear Impulse:</strong> $\mathbf{J} = \int \mathbf{F} dt = \Delta(m\mathbf{v})$; equals area under $F-t$ curve.<br><strong>Impulsive Forces:</strong> Large forces over tiny $\Delta t$; gravity/friction neglected during impact.<br><strong>Fluid Jet on Vane:</strong> Force on fluid is $\dot{m}(\mathbf{v}_{out} - \mathbf{v}_{in})$; jet force on semicircular cup ($\beta = 180^\circ$) is $2\rho A v^2$."""
    },
    "mech-q24": {
        "eq": r"""$$\Sigma \mathbf{F}^{ext} = \frac{d\mathbf{P}}{dt} = 0 \implies \mathbf{P} = \sum m_i \mathbf{v}_i = \text{constant}, \quad V_R = -\left(\frac{m}{M}\right) v_b$$""",
        "text": r"""<strong>Linear Momentum Conservation:</strong> Internal forces cancel in pairs ($\Sigma \mathbf{f}_{ij} = 0$). If $\Sigma \mathbf{F}^{ext} = 0$, total momentum is conserved.<br><strong>Recoil Velocity:</strong> Firing projectile with muzzle speed $v_b$ imparts cannon recoil $V_R = -(m/M)v_b$.<br><strong>Generality:</strong> Strictly conserved regardless of whether mechanical energy is lost."""
    },
    "mech-q25": {
        "eq": r"""$$e = \frac{v_2 - v_1}{u_1 - u_2}, \quad v_1 = \frac{(m_1 - e m_2)u_1 + m_2(1+e)u_2}{m_1 + m_2}, \quad v_2 = \frac{m_1(1+e)u_1 + (m_2 - e m_1)u_2}{m_1 + m_2}$$""",
        "text": r"""<strong>Direct Central Impact:</strong> Centers of mass and velocities lie along the normal line of impact.<br><strong>Restitution Coefficient ($e$):</strong> $e = \frac{\text{Separation Velocity}}{\text{Approach Velocity}} = \frac{v_2 - v_1}{u_1 - u_2}$.<br><strong>Special Cases:</strong> Elastic ($e = 1$) $\implies$ equal masses exchange velocities; Plastic ($e = 0$) $\implies$ bodies coalesce with common velocity."""
    },
    "mech-q26": {
        "eq": r"""$$\Delta E = \frac{m_1 m_2}{2(m_1 + m_2)} (1 - e^2) (u_1 - u_2)^2 = \frac{1}{2} \mu (1 - e^2) (u_1 - u_2)^2$$""",
        "text": r"""<strong>Loss of Kinetic Energy:</strong> $\Delta E = E_{initial} - E_{final} = \frac{m_1 m_2}{2(m_1 + m_2)}(1 - e^2)(u_1 - u_2)^2$.<br><strong>Reduced Mass:</strong> $\mu = \frac{m_1 m_2}{m_1 + m_2}$.<br><strong>Regimes:</strong><br>- Perfectly Elastic ($e = 1$): $\Delta E = 0$ (energy conserved).<br>- Inelastic ($0 < e < 1$): $\Delta E > 0$ (dissipated as heat/sound).<br>- Perfectly Plastic ($e = 0$): Maximum energy loss."""
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
