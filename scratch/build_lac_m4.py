# -*- coding: utf-8 -*-
"""
Module 4 for Subject 1: Linear Algebra and Calculus (MAT101 / MATHS - LAC)
Multivariable Differential Calculus, Partial Derivatives & Optimization
"""

M4_QUESTIONS = [
    {
        "qid": "lac-q16",
        "marks": 3,
        "type": "Short Answer",
        "title": "Euler's Theorem on Homogeneous Functions Applied to Implicit Functions",
        "yt_query": "eulers theorem homogeneous functions multivariable calculus engineering mathematics",
        "img_path": "",
        "img_caption": "",
        "answer": r"""
**Statement of Euler's Theorem on Homogeneous Functions:**
A function $f(x, y)$ is said to be homogeneous of degree $n$ in variables $x$ and $y$ if for any non-zero real scalar $t$:
$$f(tx, ty) = t^n f(x, y)$$
Euler's Theorem states that if $f(x, y)$ is a homogeneous function of degree $n$ possessing continuous first-order partial derivatives, then:
$$x \frac{\partial f}{\partial x} + y \frac{\partial f}{\partial y} = n f(x, y)$$

**Problem Application:**
We are given:
$$u = \sin^{-1}\left( \frac{x^2 + y^2}{x + y} \right)$$
We must prove that:
$$x \frac{\partial u}{\partial x} + y \frac{\partial u}{\partial y} = \tan u$$

**Step 1: Define the Auxiliary Homogeneous Function**
Notice that $u$ itself is not homogeneous because the inverse sine operation breaks algebraic scaling. Take the sine of both sides:
$$\sin u = \frac{x^2 + y^2}{x + y}$$
Define the function $f(x, y) = \sin u = \frac{x^2 + y^2}{x + y}$.

**Step 2: Determine the Degree of Homogeneity of $f(x, y)$**
Replace $x$ with $tx$ and $y$ with $ty$:
$$f(tx, ty) = \frac{(tx)^2 + (ty)^2}{tx + ty} = \frac{t^2(x^2 + y^2)}{t(x + y)} = t^1 \left( \frac{x^2 + y^2}{x + y} \right) = t^1 f(x, y)$$
Thus, $f(x, y)$ is a homogeneous function of degree $n = 1$.

**Step 3: Apply Euler's Theorem to $f(x, y)$**
By Euler's theorem:
$$x \frac{\partial f}{\partial x} + y \frac{\partial f}{\partial y} = 1 \cdot f(x, y) = \sin u$$

**Step 4: Express Partial Derivatives in Terms of $u$**
Since $f = \sin u$, applying the single-variable chain rule gives:
$$\frac{\partial f}{\partial x} = \frac{d(\sin u)}{du} \frac{\partial u}{\partial x} = \cos u \frac{\partial u}{\partial x}$$
$$\frac{\partial f}{\partial y} = \frac{d(\sin u)}{du} \frac{\partial u}{\partial y} = \cos u \frac{\partial u}{\partial y}$$

Substitute these partial derivatives into Euler's equation:
$$x \left( \cos u \frac{\partial u}{\partial x} \right) + y \left( \cos u \frac{\partial u}{\partial y} \right) = \sin u$$
$$\cos u \left( x \frac{\partial u}{\partial x} + y \frac{\partial u}{\partial y} \right) = \sin u$$
Divide both sides by $\cos u$ (for $u \neq (2k+1)\frac{\pi}{2}$):
$$x \frac{\partial u}{\partial x} + y \frac{\partial u}{\partial y} = \frac{\sin u}{\cos u} = \tan u$$
This completes the formal proof.
"""
    },
    {
        "qid": "lac-q17",
        "marks": 3,
        "type": "Short Answer",
        "title": "Coordinate Invariance of Gradient Magnitude in Polar Form",
        "yt_query": "multivariable chain rule partial derivatives cartesian to polar gradient invariance",
        "img_path": "",
        "img_caption": "",
        "answer": r"""
Let $z = f(x, y)$ be a smooth scalar field where the Cartesian coordinates $(x, y)$ are related to plane polar coordinates $(r, \theta)$ by:
$$x = r \cos \theta, \quad y = r \sin \theta$$
We must show that the sum of squared partial derivatives satisfies:
$$\left( \frac{\partial z}{\partial x} \right)^2 + \left( \frac{\partial z}{\partial y} \right)^2 = \left( \frac{\partial z}{\partial r} \right)^2 + \frac{1}{r^2} \left( \frac{\partial z}{\partial \theta} \right)^2$$

**Step 1: Express Polar Derivatives via the Multivariable Chain Rule**
Treating $z$ as a composite function of $r$ and $\theta$ through intermediate variables $x$ and $y$:
$$\frac{\partial z}{\partial r} = \frac{\partial z}{\partial x} \frac{\partial x}{\partial r} + \frac{\partial z}{\partial y} \frac{\partial y}{\partial r}$$
$$\frac{\partial z}{\partial \theta} = \frac{\partial z}{\partial x} \frac{\partial x}{\partial \theta} + \frac{\partial z}{\partial y} \frac{\partial y}{\partial \theta}$$

**Step 2: Evaluate the Coordinate Partial Derivatives**
From $x = r \cos \theta$ and $y = r \sin \theta$:
$$\frac{\partial x}{\partial r} = \cos \theta, \quad \frac{\partial y}{\partial r} = \sin \theta$$
$$\frac{\partial x}{\partial \theta} = -r \sin \theta, \quad \frac{\partial y}{\partial \theta} = r \cos \theta$$

**Step 3: Substitute into the Polar Chain Rule Expressions**
$$\frac{\partial z}{\partial r} = \frac{\partial z}{\partial x} \cos \theta + \frac{\partial z}{\partial y} \sin \theta \quad \text{--- (Equation 1)}$$
$$\frac{\partial z}{\partial \theta} = -r \frac{\partial z}{\partial x} \sin \theta + r \frac{\partial z}{\partial y} \cos \theta$$
Divide the second equation by $r$ ($r \neq 0$):
$$\frac{1}{r} \frac{\partial z}{\partial \theta} = -\frac{\partial z}{\partial x} \sin \theta + \frac{\partial z}{\partial y} \cos \theta \quad \text{--- (Equation 2)}$$

**Step 4: Square and Add Equations (1) and (2)**
$$\left( \frac{\partial z}{\partial r} \right)^2 + \frac{1}{r^2} \left( \frac{\partial z}{\partial \theta} \right)^2 = \left( \frac{\partial z}{\partial x} \cos \theta + \frac{\partial z}{\partial y} \sin \theta \right)^2 + \left( -\frac{\partial z}{\partial x} \sin \theta + \frac{\partial z}{\partial y} \cos \theta \right)^2$$

Expand each squared term:
$$\left( \frac{\partial z}{\partial x} \right)^2 \cos^2 \theta + \left( \frac{\partial z}{\partial y} \right)^2 \sin^2 \theta + 2 \frac{\partial z}{\partial x} \frac{\partial z}{\partial y} \cos \theta \sin \theta$$
$$+ \left( \frac{\partial z}{\partial x} \right)^2 \sin^2 \theta + \left( \frac{\partial z}{\partial y} \right)^2 \cos^2 \theta - 2 \frac{\partial z}{\partial x} \frac{\partial z}{\partial y} \sin \theta \cos \theta$$

The cross-product terms cancel out completely ($+2 \cos\theta\sin\theta - 2\sin\theta\cos\theta = 0$). Grouping the remaining terms:
$$= \left( \frac{\partial z}{\partial x} \right)^2 (\cos^2 \theta + \sin^2 \theta) + \left( \frac{\partial z}{\partial y} \right)^2 (\sin^2 \theta + \cos^2 \theta)$$
Using the fundamental trigonometric identity $\cos^2 \theta + \sin^2 \theta = 1$:
$$= \left( \frac{\partial z}{\partial x} \right)^2 (1) + \left( \frac{\partial z}{\partial y} \right)^2 (1) = \left( \frac{\partial z}{\partial x} \right)^2 + \left( \frac{\partial z}{\partial y} \right)^2$$
Hence proved. Geometrically, this confirms that the squared Euclidean norm of the gradient vector $\|\nabla z\|^2$ is strictly invariant under orthogonal coordinate rotation from Cartesian to polar systems.
"""
    },
    {
        "qid": "lac-q18",
        "marks": 7,
        "type": "Analytical Problem",
        "title": "Extended Euler's Theorem for First and Second Order Partial Differential Relations",
        "yt_query": "eulers theorem second order partial derivatives tan inverse homogeneous engineering mathematics",
        "img_path": "",
        "img_caption": "",
        "answer": r"""
We consider the multivariable relation:
$$u = \tan^{-1}\left( \frac{x^3 + y^3}{x - y} \right)$$
We are required to establish two important identities:
(i) $x \frac{\partial u}{\partial x} + y \frac{\partial u}{\partial y} = \sin 2u$
(ii) $x^2 \frac{\partial^2 u}{\partial x^2} + 2xy \frac{\partial^2 u}{\partial x \partial y} + y^2 \frac{\partial^2 u}{\partial y^2} = 2 \cos 3u \sin u$

---
### Part (i): Proof of First Order Relation

**Step 1: Define Homogeneous Function $f(u)$**
Take the tangent of both sides:
$$\tan u = \frac{x^3 + y^3}{x - y}$$
Let $f(x, y) = \tan u = \frac{x^3 + y^3}{x - y}$.

**Step 2: Test for Homogeneity**
Substitute $tx$ and $ty$:
$$f(tx, ty) = \frac{(tx)^3 + (ty)^3}{tx - ty} = \frac{t^3(x^3 + y^3)}{t(x - y)} = t^2 \left( \frac{x^3 + y^3}{x - y} \right) = t^2 f(x, y)$$
Therefore, $f(x, y)$ is a homogeneous function of degree $n = 2$.

**Step 3: Apply Euler's Theorem**
$$x \frac{\partial f}{\partial x} + y \frac{\partial f}{\partial y} = n f(x, y) = 2 \tan u$$
Since $f = \tan u$, we have $\frac{\partial f}{\partial x} = \sec^2 u \frac{\partial u}{\partial x}$ and $\frac{\partial f}{\partial y} = \sec^2 u \frac{\partial u}{\partial y}$.
Substitute these derivatives:
$$\sec^2 u \left( x \frac{\partial u}{\partial x} + y \frac{\partial u}{\partial y} \right) = 2 \tan u$$
$$x \frac{\partial u}{\partial x} + y \frac{\partial u}{\partial y} = \frac{2 \tan u}{\sec^2 u} = \frac{2 (\sin u / \cos u)}{1 / \cos^2 u} = 2 \sin u \cos u = \sin 2u$$
This proves part (i).

---
### Part (ii): Proof of Second Order Extended Relation

**Step 1: Recall Extended Euler's Formula for Homogeneous Functions**
For any function $u(x, y)$ where $x \frac{\partial u}{\partial x} + y \frac{\partial u}{\partial y} = g(u)$, the second-order differential operator satisfies:
$$x^2 \frac{\partial^2 u}{\partial x^2} + 2xy \frac{\partial^2 u}{\partial x \partial y} + y^2 \frac{\partial^2 u}{\partial y^2} = g(u) [g'(u) - 1]$$

*Analytical Proof of this Operator Identity:*
Let $u_x = \frac{\partial u}{\partial x}$ and $u_y = \frac{\partial u}{\partial y}$. We have:
$$x u_x + y u_y = g(u)$$
Differentiate both sides with respect to $x$ using product and chain rules:
$$(1 \cdot u_x + x u_{xx}) + y u_{yx} = g'(u) u_x \implies x u_{xx} + y u_{xy} = [g'(u) - 1] u_x \quad \text{--- (A)}$$
Differentiate both sides with respect to $y$:
$$x u_{xy} + (1 \cdot u_y + y u_{yy}) = g'(u) u_y \implies x u_{xy} + y u_{yy} = [g'(u) - 1] u_y \quad \text{--- (B)}$$
Now multiply Equation (A) by $x$ and Equation (B) by $y$, and add them together:
$$x(x u_{xx} + y u_{xy}) + y(x u_{xy} + y u_{yy}) = [g'(u) - 1] (x u_x + y u_y)$$
$$x^2 u_{xx} + 2xy u_{xy} + y^2 u_{yy} = [g'(u) - 1] g(u) = g(u)[g'(u) - 1]$$

**Step 2: Evaluate with $g(u) = \sin 2u$**
Here $g(u) = \sin 2u$. Differentiating with respect to $u$:
$$g'(u) = \frac{d}{du}(\sin 2u) = 2 \cos 2u$$
Substitute $g(u)$ and $g'(u)$ into the formula:
$$g(u)[g'(u) - 1] = \sin 2u [2 \cos 2u - 1] = 2 \sin 2u \cos 2u - \sin 2u$$
Using the double angle identity $2 \sin A \cos A = \sin 2A$:
$$2 \sin 2u \cos 2u = \sin 4u$$
Thus:
$$g(u)[g'(u) - 1] = \sin 4u - \sin 2u$$

**Step 3: Apply the Product-to-Sum Trigonometric Identity**
Recall $\sin A - \sin B = 2 \cos\left(\frac{A + B}{2}\right) \sin\left(\frac{A - B}{2}\right)$:
With $A = 4u$ and $B = 2u$:
$$\sin 4u - \sin 2u = 2 \cos\left(\frac{4u + 2u}{2}\right) \sin\left(\frac{4u - 2u}{2}\right) = 2 \cos(3u) \sin(u)$$
Therefore:
$$x^2 \frac{\partial^2 u}{\partial x^2} + 2xy \frac{\partial^2 u}{\partial x \partial y} + y^2 \frac{\partial^2 u}{\partial y^2} = 2 \cos 3u \sin u$$
This completes the rigorous proof.
"""
    },
    {
        "qid": "lac-q19",
        "marks": 7,
        "type": "Analytical Problem",
        "title": "Local Extrema and Saddle Points of Two-Variable Functions",
        "yt_query": "maxima minima saddle points two variables hessian second derivative test",
        "img_path": "",
        "img_caption": "",
        "answer": r"""
We are required to determine all local maxima, local minima, and saddle points of the two-variable function:
$$f(x, y) = x^3 + 3xy^2 - 15x^2 - 15y^2 + 72x$$

**Step 1: Compute First-Order Partial Derivatives**
$$f_x = \frac{\partial f}{\partial x} = 3x^2 + 3y^2 - 30x + 72$$
$$f_y = \frac{\partial f}{\partial y} = 6xy - 30y = 6y(x - 5)$$

**Step 2: Find Stationary (Critical) Points**
Critical points occur where $f_x = 0$ and $f_y = 0$ simultaneously.
From $f_y = 0$:
$$6y(x - 5) = 0 \implies y = 0 \quad \text{or} \quad x = 5$$

- **Case A: $y = 0$**
  Substitute $y = 0$ into $f_x = 0$:
  $$3x^2 + 3(0)^2 - 30x + 72 = 0 \implies 3x^2 - 30x + 72 = 0$$
  Divide by 3:
  $$x^2 - 10x + 24 = 0 \implies (x - 4)(x - 6) = 0 \implies x = 4 \quad \text{or} \quad x = 6$$
  This yields two critical points:
  $$P_1 = (4, 0), \quad P_2 = (6, 0)$$

- **Case B: $x = 5$**
  Substitute $x = 5$ into $f_x = 0$:
  $$3(5^2) + 3y^2 - 30(5) + 72 = 0$$
  $$3(25) + 3y^2 - 150 + 72 = 0 \implies 75 + 3y^2 - 150 + 72 = 0$$
  $$3y^2 - 3 = 0 \implies 3y^2 = 3 \implies y^2 = 1 \implies y = \pm 1$$
  This yields two more critical points:
  $$P_3 = (5, 1), \quad P_4 = (5, -1)$$

Thus, there are four stationary points: $(4, 0), (6, 0), (5, 1), (5, -1)$.

**Step 3: Compute Second-Order Partial Derivatives and Discriminant $D$**
$$r = f_{xx} = \frac{\partial}{\partial x}(3x^2 + 3y^2 - 30x + 72) = 6x - 30 = 6(x - 5)$$
$$s = f_{xy} = \frac{\partial}{\partial y}(3x^2 + 3y^2 - 30x + 72) = 6y$$
$$t = f_{yy} = \frac{\partial}{\partial y}(6xy - 30y) = 6x - 30 = 6(x - 5)$$

The discriminant (Hessian determinant) is:
$$D = rt - s^2 = [6(x - 5)][6(x - 5)] - (6y)^2 = 36(x - 5)^2 - 36y^2 = 36[(x - 5)^2 - y^2]$$

**Step 4: Classification of Each Critical Point**

1. **At point $P_1(4, 0)$:**
   $$r = 6(4 - 5) = -6$$
   $$s = 6(0) = 0$$
   $$t = 6(4 - 5) = -6$$
   $$D = (-6)(-6) - 0^2 = 36 > 0$$
   Since $D > 0$ and $r < 0$, the function attains a **Local Maximum** at $(4, 0)$.
   Local maximum value:
   $$f(4, 0) = 4^3 + 0 - 15(4^2) - 0 + 72(4) = 64 - 240 + 288 = 112$$

2. **At point $P_2(6, 0)$:**
   $$r = 6(6 - 5) = +6$$
   $$s = 6(0) = 0$$
   $$t = 6(6 - 5) = +6$$
   $$D = (6)(6) - 0^2 = 36 > 0$$
   Since $D > 0$ and $r > 0$, the function attains a **Local Minimum** at $(6, 0)$.
   Local minimum value:
   $$f(6, 0) = 6^3 + 0 - 15(6^2) - 0 + 72(6) = 216 - 540 + 432 = 108$$

3. **At point $P_3(5, 1)$:**
   $$r = 6(5 - 5) = 0$$
   $$s = 6(1) = 6$$
   $$t = 6(5 - 5) = 0$$
   $$D = (0)(0) - (6)^2 = -36 < 0$$
   Since $D < 0$, $(5, 1)$ is a **Saddle Point**.
   Value at saddle point: $f(5, 1) = 125 + 15 - 375 - 15 + 360 = 110$.

4. **At point $P_4(5, -1)$:**
   $$r = 6(5 - 5) = 0$$
   $$s = 6(-1) = -6$$
   $$t = 6(5 - 5) = 0$$
   $$D = (0)(0) - (-6)^2 = -36 < 0$$
   Since $D < 0$, $(5, -1)$ is a **Saddle Point**.
   Value at saddle point: $f(5, -1) = 125 + 15 - 375 - 15 + 360 = 110$.
"""
    },
    {
        "qid": "lac-q20",
        "marks": 7,
        "type": "Analytical Problem",
        "title": "Lagrange Multiplier Optimization for Maximal Inscribed Parallelepiped",
        "yt_query": "maximum volume rectangular box inscribed in ellipsoid lagrange multipliers",
        "img_path": "",
        "img_caption": "",
        "answer": r"""
We are required to determine the dimensions and maximum volume of a rectangular parallelepiped (box) with faces parallel to the coordinate planes that can be inscribed inside the ellipsoid:
$$\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$$
using Lagrange's method of undetermined multipliers.

**Step 1: Formulate the Objective Function and Constraint**
Let $(x, y, z)$ be the vertex of the box in the first octant, so that $x > 0, y > 0, z > 0$.
By the three-dimensional symmetry of the ellipsoid across the coordinate planes, the full lengths of the three edges of the box are $2x, 2y$, and $2z$.
The volume of the rectangular box is:
$$V(x, y, z) = (2x)(2y)(2z) = 8xyz$$

The vertex $(x, y, z)$ is constrained to lie strictly on the surface of the ellipsoid:
$$\phi(x, y, z) = \frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} - 1 = 0$$

**Step 2: Construct the Lagrangian Function**
Define the Lagrangian auxiliary function:
$$L(x, y, z, \lambda) = 8xyz - \lambda \left( \frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} - 1 \right)$$
where $\lambda$ is the Lagrange undetermined multiplier.

**Step 3: Establish Stationarity Conditions ($\nabla L = 0$)**
Taking partial derivatives with respect to $x, y, z$ and setting them to zero:
1. $\frac{\partial L}{\partial x} = 8yz - \frac{2\lambda x}{a^2} = 0 \implies 8yz = \frac{2\lambda x}{a^2} \quad \text{--- (1)}$
2. $\frac{\partial L}{\partial y} = 8xz - \frac{2\lambda y}{b^2} = 0 \implies 8xz = \frac{2\lambda y}{b^2} \quad \text{--- (2)}$
3. $\frac{\partial L}{\partial z} = 8xy - \frac{2\lambda z}{c^2} = 0 \implies 8xy = \frac{2\lambda z}{c^2} \quad \text{--- (3)}$

Multiply Equation (1) by $x$, Equation (2) by $y$, and Equation (3) by $z$:
$$8xyz = \frac{2\lambda x^2}{a^2} \quad \text{--- (4)}$$
$$8xyz = \frac{2\lambda y^2}{b^2} \quad \text{--- (5)}$$
$$8xyz = \frac{2\lambda z^2}{c^2} \quad \text{--- (6)}$$

**Step 4: Equate and Solve for the Optimum Coordinates**
From Equations (4), (5), and (6):
$$\frac{2\lambda x^2}{a^2} = \frac{2\lambda y^2}{b^2} = \frac{2\lambda z^2}{c^2} = 8xyz$$
Since maximum volume requires non-zero dimensions ($x, y, z > 0$), we must have $V > 0$ and therefore $\lambda \neq 0$. Dividing by $2\lambda$:
$$\frac{x^2}{a^2} = \frac{y^2}{b^2} = \frac{z^2}{c^2}$$

Substitute this condition into the ellipsoid constraint $\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$:
$$\frac{x^2}{a^2} + \frac{x^2}{a^2} + \frac{x^2}{a^2} = 1 \implies 3 \frac{x^2}{a^2} = 1 \implies x^2 = \frac{a^2}{3} \implies x = \frac{a}{\sqrt{3}}$$
By symmetry:
$$y = \frac{b}{\sqrt{3}}, \quad z = \frac{c}{\sqrt{3}}$$

**Step 5: Determine Dimensions and Maximum Volume**
The optimal dimensions of the inscribed rectangular box are:
$$\text{Length} = 2x = \frac{2a}{\sqrt{3}}, \quad \text{Width} = 2y = \frac{2b}{\sqrt{3}}, \quad \text{Height} = 2z = \frac{2c}{\sqrt{3}}$$

The maximum inscribed volume is:
$$V_{\max} = 8xyz = 8 \left(\frac{a}{\sqrt{3}}\right) \left(\frac{b}{\sqrt{3}}\right) \left(\frac{c}{\sqrt{3}}\right) = \frac{8abc}{3\sqrt{3}}$$
"""
    }
]

M4_BYHEART = {
    "lac-q16": {
        "eq": r'$$f(x, y) = \sin u, \text{ degree } n=1 \implies x \frac{\partial u}{\partial x} + y \frac{\partial u}{\partial y} = n \frac{f(u)}{f\'(u)} = \frac{\sin u}{\cos u} = \tan u$$',
        "text": r'<strong>Euler\'s Theorem for Implicit Functions:</strong> If $f(u)$ is homogeneous of degree $n$, then $x u_x + y u_y = n \frac{f(u)}{f\'(u)}$. For $f(u) = \sin u$ of degree 1, this immediately yields $\tan u$.'
    },
    "lac-q17": {
        "eq": r'$$\left(\frac{\partial z}{\partial r}\right)^2 + \frac{1}{r^2}\left(\frac{\partial z}{\partial \theta}\right)^2 = \left(\frac{\partial z}{\partial x}\right)^2 + \left(\frac{\partial z}{\partial y}\right)^2 = \|\nabla z\|^2$$',
        "text": r'<strong>Invariance of Gradient Magnitude:</strong> The squared Euclidean norm of the spatial gradient vector $\|\nabla z\|^2$ is coordinate-invariant under rotation and transformation from Cartesian $(x,y)$ to polar $(r,\theta)$ frames.'
    },
    "lac-q18": {
        "eq": r'$$x^2 u_{xx} + 2xy u_{xy} + y^2 u_{yy} = g(u)[g\'(u) - 1] = \sin 2u (2\cos 2u - 1) = 2 \cos 3u \sin u$$',
        "text": r'<strong>Extended Euler\'s Second Order Formula:</strong> If $x u_x + y u_y = g(u)$, then $x^2 u_{xx} + 2xy u_{xy} + y^2 u_{yy} = g(u)[g\'(u) - 1]$. For $g(u) = \sin 2u$, this simplifies to $2\cos 3u \sin u$.'
    },
    "lac-q19": {
        "eq": r'$$D = rt - s^2 \implies \begin{cases} (4, 0): D=36>0, r=-6<0 & \text{Local Maximum } (f = 112) \\ (6, 0): D=36>0, r=6>0 & \text{Local Minimum } (f = 108) \\ (5, \pm 1): D=-36<0 & \text{Saddle Points } (f = 110) \end{cases}$$',
        "text": r'<strong>Second Derivative Test for Functions of Two Variables:</strong> Calculate $D = f_{xx}f_{yy} - (f_{xy})^2$. If $D > 0$ and $f_{xx} < 0$, local max; if $D > 0$ and $f_{xx} > 0$, local min; if $D < 0$, saddle point.'
    },
    "lac-q20": {
        "eq": r'$$x = \frac{a}{\sqrt{3}}, \; y = \frac{b}{\sqrt{3}}, \; z = \frac{c}{\sqrt{3}} \implies V_{\max} = 8xyz = \frac{8abc}{3\sqrt{3}}$$',
        "text": r'<strong>Lagrange Multipliers for Inscribed Volume:</strong> Equal partition of constraint contributions $\frac{x^2}{a^2} = \frac{y^2}{b^2} = \frac{z^2}{c^2} = \frac{1}{3}$ yields optimal vertex coordinates $(a/\sqrt{3}, b/\sqrt{3}, c/\sqrt{3})$ and maximum volume $8abc/(3\sqrt{3})$.'
    }
}
