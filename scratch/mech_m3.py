# -*- coding: utf-8 -*-
"""
Module 3: Centroid, Center of Gravity and Moment of Inertia (mech-q11 to mech-q15)
KTU 2019 Scheme Engineering Mechanics (EST100)
"""

MODULE_3 = {
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
}
