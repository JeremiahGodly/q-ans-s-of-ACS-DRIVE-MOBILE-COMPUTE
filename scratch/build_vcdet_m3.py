# -*- coding: utf-8 -*-
"""
Module 3 for Subject 2: Vector Calculus, Differential Equations and Transforms (MAT102 / MATHS - VCDET)
Vector Integration, Green's, Gauss Divergence & Stokes' Theorems
"""

M3_QUESTIONS = [
    {
        "qid": "vcdet-q11",
        "marks": 3,
        "type": "Short Answer",
        "title": "Green's Theorem Evaluation of Closed Line Integral over Parabolic Boundaries",
        "yt_query": "greens theorem evaluate line integral parabolas y=x^2 y^2=x engineering mathematics",
        "img_path": "",
        "img_caption": "",
        "answer": r"""
**Statement of Green's Theorem in a Plane:**
Let $C$ be a positively oriented (counter-clockwise), piecewise smooth, simple closed curve in the $xy$-plane bounding a simply connected region $R$. If $M(x, y)$ and $N(x, y)$ are continuous functions having continuous first-order partial derivatives throughout $R$, then:
$$\oint_C (M \, dx + N \, dy) = \iint_R \left( \frac{\partial N}{\partial x} - \frac{\partial M}{\partial y} \right) dx \, dy$$

We are required to evaluate:
$$I = \oint_C [(x - y)\, dx + (x + y)\, dy]$$
around the closed boundary $C$ of the region bounded by $y = x^2$ and $y^2 = x$.

**Step 1: Identify Functions $M$ and $N$ and Their Partial Derivatives**
$$M(x, y) = x - y \implies \frac{\partial M}{\partial y} = -1$$
$$N(x, y) = x + y \implies \frac{\partial N}{\partial x} = 1$$
Compute the integrand of the double integral:
$$\frac{\partial N}{\partial x} - \frac{\partial M}{\partial y} = 1 - (-1) = 1 + 1 = 2$$

**Step 2: Determine the Region of Integration $R$**
The boundary curves are:
- Lower boundary: $y = x^2$
- Upper boundary: $y = \sqrt{x}$ (from $y^2 = x$)
Intersection points:
$$x^2 = \sqrt{x} \implies x^4 = x \implies x(x^3 - 1) = 0 \implies x = 0 \quad \text{and} \quad x = 1$$
The curves intersect at $(0, 0)$ and $(1, 1)$.

**Step 3: Evaluate the Double Integral**
Applying Green's theorem:
$$I = \iint_R 2 \, dx \, dy = 2 \iint_R dx \, dy = 2 \times (\text{Area of region } R)$$
Set up the iterated integral:
$$\text{Area}(R) = \int_{x=0}^1 \left[ \int_{y=x^2}^{\sqrt{x}} dy \right] dx = \int_0^1 (\sqrt{x} - x^2) \, dx$$
Evaluate the single integral:
$$\int_0^1 (x^{1/2} - x^2) \, dx = \left[ \frac{x^{3/2}}{3/2} - \frac{x^3}{3} \right]_0^1 = \left[ \frac{2}{3}x^{3/2} - \frac{1}{3}x^3 \right]_0^1 = \frac{2}{3} - \frac{1}{3} = \frac{1}{3}$$
Multiplying by the integrand value 2:
$$I = 2 \left( \frac{1}{3} \right) = \frac{2}{3}$$
"""
    },
    {
        "qid": "vcdet-q12",
        "marks": 3,
        "type": "Short Answer",
        "title": "Gauss Divergence Theorem Statement and Physical Interpretation in Engineering",
        "yt_query": "gauss divergence theorem statement physical significance electrodynamics fluid flow",
        "img_path": "",
        "img_caption": "",
        "answer": r"""
**Statement of Gauss Divergence Theorem:**
Let $V$ be a bounded volume in three-dimensional space enclosed by a piecewise smooth, closed, orientable surface $S$. Let $\vec{F}(x, y, z)$ be a continuously differentiable vector field defined on $V$ and its boundary $S$. Then the net outward flux of $\vec{F}$ across the closed surface $S$ is identically equal to the volume integral of the divergence of $\vec{F}$ throughout the interior volume $V$:
$$\iint_S \vec{F} \cdot \hat{n} \, dS = \iiint_V (\nabla \cdot \vec{F}) \, dV$$
where $\hat{n}$ is the outward-pointing unit normal vector to the surface element $dS$.

**Physical Significance in Engineering and Physics:**

1. **Fluid Dynamics (Continuity and Mass Conservation):**
   If $\vec{v}$ represents the velocity vector field of a fluid with density $\rho$, the vector $\vec{F} = \rho \vec{v}$ represents mass flux density. The surface integral $\iint_S (\rho \vec{v}) \cdot \hat{n} \, dS$ quantifies the net physical rate at which fluid mass is escaping outwards through the enclosing boundary $S$.
   The divergence $\nabla \cdot (\rho \vec{v})$ represents the volumetric source density (local rate of fluid creation or expansion per unit volume). If $\nabla \cdot \vec{F} > 0$, the point acts as a source; if $\nabla \cdot \vec{F} < 0$, it acts as a sink. The theorem proves that the total outward mass discharge across the boundary equals the sum total of all internal fluid sources minus sinks inside the volume.

2. **Electromagnetics (Gauss's Law):**
   In electrostatics, Maxwell's first equation states $\nabla \cdot \vec{D} = \rho_v$, where $\vec{D}$ is the electric flux density and $\rho_v$ is volume charge density. Applying the Gauss divergence theorem:
   $$\iint_S \vec{D} \cdot \hat{n} \, dS = \iiint_V (\nabla \cdot \vec{D}) \, dV = \iiint_V \rho_v \, dV = Q_{\text{enclosed}}$$
   This establishes that the total outward electric flux passing through any closed Gaussian surface equals the total enclosed electric charge $Q_{\text{enclosed}}$.
"""
    },
    {
        "qid": "vcdet-q13",
        "marks": 7,
        "type": "Analytical Problem",
        "title": "Comprehensive Verification of Green's Theorem on Closed Bounded Planar Region",
        "yt_query": "verify greens theorem line integral surface integral y=x y=x^2 engineering mathematics",
        "img_path": "",
        "img_caption": "",
        "answer": r"""
We are required to verify Green's theorem in the plane for:
$$\oint_C [(xy + y^2)\, dx + x^2\, dy]$$
where $C$ is the closed curve bounded by the line $y = x$ and the parabola $y = x^2$, traversed in the positive (counter-clockwise) direction.

Green's theorem states:
$$\oint_C (M \, dx + N \, dy) = \iint_R \left( \frac{\partial N}{\partial x} - \frac{\partial M}{\partial y} \right) dx \, dy$$

---
### Part 1: Evaluation of the Double Integral (Right-Hand Side)

Here:
$$M(x, y) = xy + y^2 \implies \frac{\partial M}{\partial y} = x + 2y$$
$$N(x, y) = x^2 \implies \frac{\partial N}{\partial x} = 2x$$
Compute the integrand:
$$\frac{\partial N}{\partial x} - \frac{\partial M}{\partial y} = 2x - (x + 2y) = x - 2y$$

The region $R$ is bounded below by the parabola $y = x^2$ and above by the line $y = x$, from $x = 0$ to $x = 1$.
$$\iint_R (x - 2y) \, dy \, dx = \int_{x=0}^1 \left[ \int_{y=x^2}^x (x - 2y) \, dy \right] dx$$

Evaluate the inner integral with respect to $y$:
$$\int_{x^2}^x (x - 2y) \, dy = \left[ xy - y^2 \right]_{y=x^2}^{y=x}$$
$$= [x(x) - x^2] - [x(x^2) - (x^2)^2] = [x^2 - x^2] - [x^3 - x^4] = -(x^3 - x^4) = x^4 - x^3$$

Now evaluate the outer integral with respect to $x$:
$$\int_0^1 (x^4 - x^3) \, dx = \left[ \frac{x^5}{5} - \frac{x^4}{4} \right]_0^1 = \frac{1}{5} - \frac{1}{4} = \frac{4 - 5}{20} = -\frac{1}{20}$$
Thus:
$$\text{RHS} = -\frac{1}{20}$$

---
### Part 2: Evaluation of the Line Integral (Left-Hand Side)

The closed boundary curve $C$ consists of two distinct oriented segments: $C = C_1 + C_2$.
1. Curve $C_1$: Along the parabola $y = x^2$ from the origin $(0, 0)$ to $(1, 1)$.
2. Curve $C_2$: Along the straight line $y = x$ from $(1, 1)$ back to the origin $(0, 0)$.

**Integral along $C_1$ ($y = x^2 \implies dy = 2x \, dx$, with $x$ running from $0$ to $1$):**
$$\int_{C_1} [(xy + y^2)\, dx + x^2\, dy] = \int_0^1 \left[ \left( x(x^2) + (x^2)^2 \right) dx + x^2 (2x \, dx) \right]$$
$$= \int_0^1 \left( x^3 + x^4 + 2x^3 \right) dx = \int_0^1 (3x^3 + x^4) \, dx$$
$$= \left[ \frac{3x^4}{4} + \frac{x^5}{5} \right]_0^1 = \frac{3}{4} + \frac{1}{5} = \frac{15 + 4}{20} = \frac{19}{20}$$

**Integral along $C_2$ ($y = x \implies dy = dx$, with $x$ running from $1$ to $0$):**
$$\int_{C_2} [(xy + y^2)\, dx + x^2\, dy] = \int_1^0 \left[ (x(x) + x^2)\, dx + x^2\, dx \right]$$
$$= \int_1^0 (x^2 + x^2 + x^2) \, dx = \int_1^0 3x^2 \, dx = \left[ x^3 \right]_1^0 = 0^3 - 1^3 = -1$$

**Total Line Integral:**
$$\oint_C (M \, dx + N \, dy) = \int_{C_1} + \int_{C_2} = \frac{19}{20} + (-1) = \frac{19 - 20}{20} = -\frac{1}{20}$$
Thus:
$$\text{LHS} = -\frac{1}{20}$$

Since $\text{LHS} = \text{RHS} = -\frac{1}{20}$, Green's theorem is completely verified.
"""
    },
    {
        "qid": "vcdet-q14",
        "marks": 7,
        "type": "Analytical Problem",
        "title": "Rigorous Verification of Gauss Divergence Theorem over a Closed Unit Cube",
        "yt_query": "verify gauss divergence theorem unit cube six faces flux engineering mathematics",
        "img_path": "",
        "img_caption": "",
        "answer": r"""
We are required to verify the Gauss divergence theorem for the vector field:
$$\vec{F} = 4xz\hat{i} - y^2\hat{j} + yz\hat{k}$$
over the unit cube bounded by the coordinate planes:
$$x = 0, \quad x = 1, \quad y = 0, \quad y = 1, \quad z = 0, \quad z = 1$$

Gauss Divergence Theorem states:
$$\iint_S \vec{F} \cdot \hat{n} \, dS = \iiint_V (\nabla \cdot \vec{F}) \, dV$$

---
### Part 1: Evaluation of the Volume Integral (RHS)

Compute the divergence of $\vec{F}$:
$$\nabla \cdot \vec{F} = \frac{\partial}{\partial x}(4xz) + \frac{\partial}{\partial y}(-y^2) + \frac{\partial}{\partial z}(yz) = 4z - 2y + y = 4z - y$$

Evaluate the triple integral over the unit cube:
$$\iiint_V (\nabla \cdot \vec{F}) \, dV = \int_{z=0}^1 \int_{y=0}^1 \int_{x=0}^1 (4z - y) \, dx \, dy \, dz$$
Since the integrand is independent of $x$, the $x$-integral is simply $\int_0^1 dx = 1$:
$$= \int_{z=0}^1 \int_{y=0}^1 (4z - y) \, dy \, dz$$

Integrate with respect to $y$:
$$\int_0^1 (4z - y) \, dy = \left[ 4zy - \frac{y^2}{2} \right]_0^1 = 4z(1) - \frac{1}{2} = 4z - \frac{1}{2}$$

Integrate with respect to $z$:
$$\int_0^1 \left( 4z - \frac{1}{2} \right) dz = \left[ 2z^2 - \frac{z}{2} \right]_0^1 = 2(1)^2 - \frac{1}{2} = 2 - \frac{1}{2} = \frac{3}{2}$$
Therefore:
$$\text{RHS} = \frac{3}{2}$$

---
### Part 2: Evaluation of the Surface Integral over all Six Faces (LHS)

The closed boundary surface $S$ consists of the 6 square faces of the unit cube:

1. **Face $S_1$ (Right Face: $x = 1$, outward normal $\hat{n} = \hat{i}$, $dS = dy \, dz$):**
   $$\vec{F} \cdot \hat{n} = \vec{F} \cdot \hat{i} = 4xz = 4(1)z = 4z$$
   $$I_1 = \int_0^1 \int_0^1 4z \, dy \, dz = \left( \int_0^1 dy \right) \left[ 2z^2 \right]_0^1 = (1)(2) = 2$$

2. **Face $S_2$ (Left Face: $x = 0$, outward normal $\hat{n} = -\hat{i}$, $dS = dy \, dz$):**
   $$\vec{F} \cdot \hat{n} = -(4xz) = -4(0)z = 0 \implies I_2 = 0$$

3. **Face $S_3$ (Front Face: $y = 1$, outward normal $\hat{n} = \hat{j}$, $dS = dx \, dz$):**
   $$\vec{F} \cdot \hat{n} = \vec{F} \cdot \hat{j} = -y^2 = -(1)^2 = -1$$
   $$I_3 = \int_0^1 \int_0^1 (-1) \, dx \, dz = -1(1)(1) = -1$$

4. **Face $S_4$ (Back Face: $y = 0$, outward normal $\hat{n} = -\hat{j}$, $dS = dx \, dz$):**
   $$\vec{F} \cdot \hat{n} = -(-y^2) = y^2 = 0^2 = 0 \implies I_4 = 0$$

5. **Face $S_5$ (Top Face: $z = 1$, outward normal $\hat{n} = \hat{k}$, $dS = dx \, dy$):**
   $$\vec{F} \cdot \hat{n} = \vec{F} \cdot \hat{k} = yz = y(1) = y$$
   $$I_5 = \int_0^1 \int_0^1 y \, dx \, dy = \left( \int_0^1 dx \right) \left[ \frac{y^2}{2} \right]_0^1 = (1)\left(\frac{1}{2}\right) = \frac{1}{2}$$

6. **Face $S_6$ (Bottom Face: $z = 0$, outward normal $\hat{n} = -\hat{k}$, $dS = dx \, dy$):**
   $$\vec{F} \cdot \hat{n} = -(yz) = -y(0) = 0 \implies I_6 = 0$$

**Total Surface Flux:**
$$\iint_S \vec{F} \cdot \hat{n} \, dS = \sum_{i=1}^6 I_i = 2 + 0 + (-1) + 0 + \frac{1}{2} + 0 = 1 + \frac{1}{2} = \frac{3}{2}$$
Thus:
$$\text{LHS} = \frac{3}{2}$$

Since $\text{LHS} = \text{RHS} = \frac{3}{2}$, the Gauss divergence theorem is verified.
"""
    },
    {
        "qid": "vcdet-q15",
        "marks": 7,
        "type": "Analytical Problem",
        "title": "Stokes' Theorem Verification on Hemispherical Surface with Circular Boundary",
        "yt_query": "verify stokes theorem hemisphere line integral curl engineering mathematics",
        "img_path": "",
        "img_caption": "",
        "answer": r"""
We are required to verify Stokes' theorem for the vector field:
$$\vec{F} = (2x - y)\hat{i} - yz^2\hat{j} - y^2 z\hat{k}$$
over the upper hemispherical surface $S: x^2 + y^2 + z^2 = 1, z \ge 0$, bounded by the circle $C: x^2 + y^2 = 1$ lying in the $xy$-plane ($z = 0$).

Stokes' Theorem states:
$$\oint_C \vec{F} \cdot d\vec{r} = \iint_S (\nabla \times \vec{F}) \cdot \hat{n} \, dS$$

---
### Part 1: Evaluation of the Line Integral around Boundary $C$ (LHS)

The boundary curve $C$ is the circle $x^2 + y^2 = 1, z = 0$ in the $xy$-plane, oriented counter-clockwise when viewed from above.
Parametric equations of $C$:
$$x = \cos t, \quad y = \sin t, \quad z = 0, \quad \text{where } 0 \le t \le 2\pi$$
The differentials are:
$$dx = -\sin t \, dt, \quad dy = \cos t \, dt, \quad dz = 0$$

On $z = 0$, the vector field $\vec{F}$ simplifies to:
$$\vec{F} = (2x - y)\hat{i} - y(0)^2\hat{j} - y^2(0)\hat{k} = (2x - y)\hat{i}$$
The differential displacement vector is $d\vec{r} = dx\hat{i} + dy\hat{j} + dz\hat{k}$.
$$\vec{F} \cdot d\vec{r} = (2x - y) \, dx$$
Substitute the parametric relations:
$$\vec{F} \cdot d\vec{r} = (2\cos t - \sin t)(-\sin t \, dt) = (-2\sin t \cos t + \sin^2 t) \, dt = (-\sin 2t + \sin^2 t) \, dt$$

Now integrate from $t = 0$ to $t = 2\pi$:
$$\oint_C \vec{F} \cdot d\vec{r} = \int_0^{2\pi} (-\sin 2t + \sin^2 t) \, dt$$
1. $\int_0^{2\pi} -\sin 2t \, dt = \left[ \frac{\cos 2t}{2} \right]_0^{2\pi} = \frac{1 - 1}{2} = 0$.
2. $\int_0^{2\pi} \sin^2 t \, dt = \int_0^{2\pi} \frac{1 - \cos 2t}{2} \, dt = \left[ \frac{t}{2} - \frac{\sin 2t}{4} \right]_0^{2\pi} = \frac{2\pi}{2} - 0 = \pi$.

Therefore:
$$\text{LHS} = \oint_C \vec{F} \cdot d\vec{r} = 0 + \pi = \pi$$

---
### Part 2: Evaluation of the Surface Integral of Curl (RHS)

Compute the curl of $\vec{F}$:
$$\nabla \times \vec{F} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ 2x - y & -yz^2 & -y^2 z \end{vmatrix}$$

Evaluate components:
- **$\hat{i}$-component:**
  $$\frac{\partial}{\partial y}(-y^2 z) - \frac{\partial}{\partial z}(-yz^2) = -2yz - (-2yz) = -2yz + 2yz = 0$$
- **$\hat{j}$-component:**
  $$-\left( \frac{\partial}{\partial x}(-y^2 z) - \frac{\partial}{\partial z}(2x - y) \right) = -(0 - 0) = 0$$
- **$\hat{k}$-component:**
  $$\frac{\partial}{\partial x}(-yz^2) - \frac{\partial}{\partial y}(2x - y) = 0 - (-1) = 1$$

Thus:
$$\nabla \times \vec{F} = 0\hat{i} + 0\hat{j} + 1\hat{k} = \hat{k}$$

Now evaluate the surface integral:
$$\iint_S (\nabla \times \vec{F}) \cdot \hat{n} \, dS = \iint_S \hat{k} \cdot \hat{n} \, dS$$
Recall from vector surface theory that $\hat{k} \cdot \hat{n} \, dS = dx \, dy$, which is the orthogonal projection of the infinitesimal surface patch $dS$ onto the $xy$-plane.
As $S$ is the upper hemisphere $x^2 + y^2 + z^2 = 1, z \ge 0$, its projection onto the $xy$-plane is precisely the circular disk $R: x^2 + y^2 \le 1$.
Therefore:
$$\iint_S \hat{k} \cdot \hat{n} \, dS = \iint_R dx \, dy = \text{Area of the circular disk } (x^2 + y^2 \le 1) = \pi(1)^2 = \pi$$
Thus:
$$\text{RHS} = \pi$$

Since $\text{LHS} = \text{RHS} = \pi$, Stokes' theorem is completely verified.
"""
    }
]

M3_BYHEART = {
    "vcdet-q11": {
        "eq": r'$$\oint_C [(x-y)dx + (x+y)dy] = \iint_R (1 - (-1)) dx\,dy = 2 \int_0^1 (\sqrt{x} - x^2)dx = 2\left(\frac{1}{3}\right) = \frac{2}{3}$$',
        "text": r'<strong>Green\'s Theorem in a Plane:</strong> Converts a closed line integral $\oint (Mdx + Ndy)$ into a double integral of $(\partial N/\partial x - \partial M/\partial y)$. When the integrand is constant 2, the integral simply equals $2 \times \text{enclosed area}$.'
    },
    "vcdet-q12": {
        "eq": r'$$\iint_S \vec{F} \cdot \hat{n} \, dS = \iiint_V (\nabla \cdot \vec{F}) \, dV \iff \Phi_{\text{net}} = \iiint (\text{source density}) \, dV$$',
        "text": r'<strong>Gauss Divergence Theorem:</strong> Relates outward flux through a closed boundary surface to the volumetric accumulation of divergence within the bounded domain; underpins Gauss\'s Law in electromagnetics.'
    },
    "vcdet-q13": {
        "eq": r'$$\oint_C = \int_{C_1} + \int_{C_2} = \frac{19}{20} - 1 = -\frac{1}{20} = \iint_R (x - 2y) dy\,dx$$',
        "text": r'<strong>Verification of Green\'s Theorem:</strong> Compute line integral along piecewise boundary curves ($C_1: y=x^2, C_2: y=x$) and compare against surface double integral of $(N_x - M_y) = x - 2y$; both equal $-1/20$.'
    },
    "vcdet-q14": {
        "eq": r'$$\iiint_V (\nabla \cdot \vec{F}) dV = \int_0^1 \int_0^1 (4z - y) dydz = \frac{3}{2} = \sum_{i=1}^6 \iint_{S_i} \vec{F} \cdot \hat{n} \, dS$$',
        "text": r'<strong>Gauss Theorem Verification on Cube:</strong> Evaluate outward normal flux across all 6 faces ($\Phi = 2 + 0 - 1 + 0 + 1/2 + 0 = 3/2$) and confirm identity with volume integral of divergence $4z - y = 3/2$.'
    },
    "vcdet-q15": {
        "eq": r'$$\nabla \times \vec{F} = \hat{k} \implies \iint_S (\nabla \times \vec{F}) \cdot \hat{n} \, dS = \iint_{x^2+y^2 \le 1} dx\,dy = \pi = \oint_C \vec{F} \cdot d\vec{r}$$',
        "text": r'<strong>Stokes\' Theorem Verification:</strong> The line integral of $\vec{F}$ around the equator boundary circle equals $\pi$. The curl simplifies to unit vertical vector $\hat{k}$, whose surface flux projects directly to the equatorial disc area $\pi$.'
    }
}
