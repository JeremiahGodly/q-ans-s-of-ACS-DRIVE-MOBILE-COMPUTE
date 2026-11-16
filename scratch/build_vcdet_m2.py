# -*- coding: utf-8 -*-
"""
Module 2 for Subject 2: Vector Calculus, Differential Equations and Transforms (MAT102 / MATHS - VCDET)
Vector Differentiation, Gradient, Divergence, Curl & Potentials
"""

M2_QUESTIONS = [
    {
        "qid": "vcdet-q6",
        "marks": 3,
        "type": "Short Answer",
        "title": "Directional Derivative of Scalar Potential Field along Specified Vector",
        "yt_query": "directional derivative of scalar function gradient vector engineering mathematics",
        "img_path": "",
        "img_caption": "",
        "answer": r"""
The **directional derivative** of a differentiable scalar field $\phi(x, y, z)$ at a point $P$ in the direction of a non-zero vector $\vec{a}$ quantifies the instantaneous spatial rate of change of $\phi$ along that direction. It is formally calculated by taking the scalar dot product of the gradient vector $\nabla \phi$ evaluated at $P$ with the unit direction vector $\hat{u}$:
$$D_{\hat{u}}\phi = \nabla \phi \cdot \hat{u} = \nabla \phi \cdot \frac{\vec{a}}{|\vec{a}|}$$

We are given the scalar field:
$$\phi(x, y, z) = x^2 y z + 4 x z^2$$
at the point $P(1, -2, -1)$ in the direction of the vector $\vec{a} = 2\hat{i} - \hat{j} - 2\hat{k}$.

**Step 1: Compute the Gradient Vector $\nabla \phi$**
$$\nabla \phi = \frac{\partial \phi}{\partial x}\hat{i} + \frac{\partial \phi}{\partial y}\hat{j} + \frac{\partial \phi}{\partial z}\hat{k}$$
Compute the first-order partial derivatives:
$$\frac{\partial \phi}{\partial x} = \frac{\partial}{\partial x}(x^2 y z + 4 x z^2) = 2xyz + 4z^2$$
$$\frac{\partial \phi}{\partial y} = \frac{\partial}{\partial y}(x^2 y z + 4 x z^2) = x^2 z$$
$$\frac{\partial \phi}{\partial z} = \frac{\partial}{\partial z}(x^2 y z + 4 x z^2) = x^2 y + 8xz$$

**Step 2: Evaluate $\nabla \phi$ at the Point $P(1, -2, -1)$**
$$\left.\frac{\partial \phi}{\partial x}\right|_{(1, -2, -1)} = 2(1)(-2)(-1) + 4(-1)^2 = 4 + 4 = 8$$
$$\left.\frac{\partial \phi}{\partial y}\right|_{(1, -2, -1)} = (1)^2(-1) = -1$$
$$\left.\frac{\partial \phi}{\partial z}\right|_{(1, -2, -1)} = (1)^2(-2) + 8(1)(-1) = -2 - 8 = -10$$
Therefore:
$$\nabla \phi_{(1, -2, -1)} = 8\hat{i} - \hat{j} - 10\hat{k}$$

**Step 3: Determine the Unit Direction Vector $\hat{u}$**
The magnitude of $\vec{a} = 2\hat{i} - \hat{j} - 2\hat{k}$ is:
$$|\vec{a}| = \sqrt{2^2 + (-1)^2 + (-2)^2} = \sqrt{4 + 1 + 4} = \sqrt{9} = 3$$
The unit vector is:
$$\hat{u} = \frac{\vec{a}}{|\vec{a}|} = \frac{2\hat{i} - \hat{j} - 2\hat{k}}{3}$$

**Step 4: Compute the Directional Derivative**
$$D_{\hat{u}}\phi = \nabla \phi \cdot \hat{u} = (8\hat{i} - \hat{j} - 10\hat{k}) \cdot \left( \frac{2\hat{i} - \hat{j} - 2\hat{k}}{3} \right)$$
$$= \frac{(8)(2) + (-1)(-1) + (-10)(-2)}{3} = \frac{16 + 1 + 20}{3} = \frac{37}{3}$$
The rate of increase of $\phi$ in the given direction is $\frac{37}{3}$ units per unit distance.
"""
    },
    {
        "qid": "vcdet-q7",
        "marks": 3,
        "type": "Short Answer",
        "title": "Unit Normal Vector and Tangent Plane to Implicit Level Surface",
        "yt_query": "unit normal vector to surface tangent plane gradient engineering mathematics",
        "img_path": "",
        "img_caption": "",
        "answer": r"""
A geometric surface defined implicitly by $f(x, y, z) = c$ represents a level surface of the scalar field $f$. The spatial gradient vector $\nabla f$ evaluated at any point $P(x_0, y_0, z_0)$ on the surface is strictly orthogonal (perpendicular) to the tangent plane of the surface at that point.

The **unit normal vector** to the surface at $P$ is defined by:
$$\hat{n} = \frac{\nabla f}{|\nabla f|}$$
The corresponding equation of the **tangent plane** at $P(x_0, y_0, z_0)$ is:
$$\nabla f \cdot [(x - x_0)\hat{i} + (y - y_0)\hat{j} + (z - z_0)\hat{k}] = 0$$

We are given the ellipsoidal surface:
$$x^2 + y^2 + 2z^2 = 4$$
at the point $P(1, 1, 1)$.

**Step 1: Define the Scalar Level Function**
$$f(x, y, z) = x^2 + y^2 + 2z^2 - 4 = 0$$

**Step 2: Compute the Gradient Vector $\nabla f$**
$$\nabla f = \frac{\partial f}{\partial x}\hat{i} + \frac{\partial f}{\partial y}\hat{j} + \frac{\partial f}{\partial z}\hat{k} = 2x\hat{i} + 2y\hat{j} + 4z\hat{k}$$

**Step 3: Evaluate $\nabla f$ at Point $P(1, 1, 1)$**
$$\vec{n} = \nabla f_{(1, 1, 1)} = 2(1)\hat{i} + 2(1)\hat{j} + 4(1)\hat{k} = 2\hat{i} + 2\hat{j} + 4\hat{k}$$

**Step 4: Compute the Unit Normal Vector $\hat{n}$**
Calculate the magnitude of $\vec{n}$:
$$|\vec{n}| = \sqrt{2^2 + 2^2 + 4^2} = \sqrt{4 + 4 + 16} = \sqrt{24} = \sqrt{4 \times 6} = 2\sqrt{6}$$
The unit outward normal vector is:
$$\hat{n} = \frac{2\hat{i} + 2\hat{j} + 4\hat{k}}{2\sqrt{6}} = \frac{\hat{i} + \hat{j} + 2\hat{k}}{\sqrt{6}}$$

**Step 5: Determine the Tangent Plane Equation**
The tangent plane equation at $(1, 1, 1)$ is:
$$2(x - 1) + 2(y - 1) + 4(z - 1) = 0$$
$$2x - 2 + 2y - 2 + 4z - 4 = 0 \implies 2x + 2y + 4z = 8$$
Divide through by 2:
$$x + y + 2z = 4$$
"""
    },
    {
        "qid": "vcdet-q8",
        "marks": 7,
        "type": "Analytical Problem",
        "title": "Irrotational Vector Field, Conservative Potential, and Work Done Line Integral",
        "yt_query": "conservative vector field curl scalar potential work done path independent",
        "img_path": "",
        "img_caption": "",
        "answer": r"""
We consider the three-dimensional vector field:
$$\vec{F} = (2xy + z^3)\hat{i} + x^2\hat{j} + 3xz^2\hat{k}$$

We are required to:
1. Prove that $\vec{F}$ is conservative and irrotational.
2. Find the scalar potential function $\phi(x, y, z)$ such that $\vec{F} = \nabla \phi$.
3. Evaluate the work done in moving a particle under this force from point $A(1, -2, 1)$ to point $B(3, 1, 4)$.

---
### Part 1: Prove that $\vec{F}$ is Irrotational and Conservative

A vector field is **irrotational** (and therefore conservative in simply connected domains) if its curl vanishes identically: $\nabla \times \vec{F} = \vec{0}$.
Let $F_1 = 2xy + z^3$, $F_2 = x^2$, and $F_3 = 3xz^2$.
$$\nabla \times \vec{F} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ 2xy + z^3 & x^2 & 3xz^2 \end{vmatrix}$$

Evaluate each component:
- **$\hat{i}$-component:**
  $$\frac{\partial F_3}{\partial y} - \frac{\partial F_2}{\partial z} = \frac{\partial}{\partial y}(3xz^2) - \frac{\partial}{\partial z}(x^2) = 0 - 0 = 0$$
- **$\hat{j}$-component:**
  $$-\left( \frac{\partial F_3}{\partial x} - \frac{\partial F_1}{\partial z} \right) = -\left( \frac{\partial}{\partial x}(3xz^2) - \frac{\partial}{\partial z}(2xy + z^3) \right) = -(3z^2 - 3z^2) = 0$$
- **$\hat{k}$-component:**
  $$\frac{\partial F_2}{\partial x} - \frac{\partial F_1}{\partial y} = \frac{\partial}{\partial x}(x^2) - \frac{\partial}{\partial y}(2xy + z^3) = 2x - 2x = 0$$

Thus:
$$\nabla \times \vec{F} = 0\hat{i} + 0\hat{j} + 0\hat{k} = \vec{0}$$
Since $\nabla \times \vec{F} = \vec{0}$ everywhere in $\mathbb{R}^3$, $\vec{F}$ is strictly **irrotational** and **conservative**.

---
### Part 2: Find the Scalar Potential $\phi(x, y, z)$

Since $\vec{F}$ is conservative, there exists a scalar potential $\phi$ such that:
$$\nabla \phi = \vec{F} \implies \frac{\partial \phi}{\partial x}\hat{i} + \frac{\partial \phi}{\partial y}\hat{j} + \frac{\partial \phi}{\partial z}\hat{k} = (2xy + z^3)\hat{i} + x^2\hat{j} + 3xz^2\hat{k}$$

This yields three partial differential equations:
1. $\frac{\partial \phi}{\partial x} = 2xy + z^3 \quad \text{--- (1)}$
2. $\frac{\partial \phi}{\partial y} = x^2 \quad \text{--- (2)}$
3. $\frac{\partial \phi}{\partial z} = 3xz^2 \quad \text{--- (3)}$

Integrate Equation (1) with respect to $x$ (treating $y$ and $z$ as constants):
$$\phi(x, y, z) = \int (2xy + z^3) \, dx = x^2 y + x z^3 + g(y, z) \quad \text{--- (4)}$$
where $g(y, z)$ is an arbitrary function of $y$ and $z$.

Differentiate Equation (4) with respect to $y$ and equate to Equation (2):
$$\frac{\partial \phi}{\partial y} = x^2 + \frac{\partial g}{\partial y} = x^2 \implies \frac{\partial g}{\partial y} = 0$$
This implies $g(y, z)$ is independent of $y$, so $g(y, z) = h(z)$.
Thus $\phi(x, y, z) = x^2 y + x z^3 + h(z)$.

Now differentiate with respect to $z$ and equate to Equation (3):
$$\frac{\partial \phi}{\partial z} = 3xz^2 + h'(z) = 3xz^2 \implies h'(z) = 0 \implies h(z) = C \quad (\text{constant})$$

Taking $C = 0$ for the standard potential:
$$\phi(x, y, z) = x^2 y + x z^3$$

---
### Part 3: Evaluate Work Done

For any conservative force field, the work done along any curve $C$ connecting point $A$ to point $B$ is independent of the path and depends strictly on the potential difference at the boundaries:
$$W = \int_A^B \vec{F} \cdot d\vec{r} = \int_A^B \nabla \phi \cdot d\vec{r} = \phi(B) - \phi(A)$$

Evaluate $\phi$ at the initial point $A(1, -2, 1)$:
$$\phi(A) = \phi(1, -2, 1) = (1^2)(-2) + (1)(1^3) = -2 + 1 = -1$$

Evaluate $\phi$ at the final point $B(3, 1, 4)$:
$$\phi(B) = \phi(3, 1, 4) = (3^2)(1) + (3)(4^3) = 9 + 3(64) = 9 + 192 = 201$$

Calculate the total work done:
$$W = \phi(B) - \phi(A) = 201 - (-1) = 201 + 1 = 202 \text{ units}$$
"""
    },
    {
        "qid": "vcdet-q9",
        "marks": 7,
        "type": "Analytical Problem",
        "title": "Determination of Constants for Irrotational Field and Solenoidal Field Verification",
        "yt_query": "find constants a b c irrotational vector field solenoidal divergence curl zero",
        "img_path": "",
        "img_caption": "",
        "answer": r"""
We consider the vector field:
$$\vec{F} = (x + 2y + az)\hat{i} + (bx - 3y - z)\hat{j} + (4x + cy + 2z)\hat{k}$$

We are required to:
1. Determine the scalar constants $a, b, c$ such that $\vec{F}$ is irrotational.
2. Prove that $\vec{F}$ is solenoidal for all real values of $a, b, c$.

---
### Part 1: Determine Constants $a, b, c$ for Irrotationality

A vector field $\vec{F} = F_1\hat{i} + F_2\hat{j} + F_3\hat{k}$ is **irrotational** if and only if $\nabla \times \vec{F} = \vec{0}$:
$$\nabla \times \vec{F} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ x + 2y + az & bx - 3y - z & 4x + cy + 2z \end{vmatrix} = \vec{0}$$

Expand the curl determinant:
$$\hat{i} \left[ \frac{\partial}{\partial y}(4x + cy + 2z) - \frac{\partial}{\partial z}(bx - 3y - z) \right]$$
$$- \hat{j} \left[ \frac{\partial}{\partial x}(4x + cy + 2z) - \frac{\partial}{\partial z}(x + 2y + az) \right]$$
$$+ \hat{k} \left[ \frac{\partial}{\partial x}(bx - 3y - z) - \frac{\partial}{\partial y}(x + 2y + az) \right] = 0\hat{i} + 0\hat{j} + 0\hat{k}$$

Evaluate each bracketed partial derivative:
1. **$\hat{i}$-component:**
   $$\frac{\partial}{\partial y}(4x + cy + 2z) - \frac{\partial}{\partial z}(bx - 3y - z) = c - (-1) = c + 1$$
   Setting this equal to zero:
   $$c + 1 = 0 \implies c = -1$$

2. **$\hat{j}$-component:**
   $$-\left[ \frac{\partial}{\partial x}(4x + cy + 2z) - \frac{\partial}{\partial z}(x + 2y + az) \right] = -(4 - a) = a - 4$$
   Setting this equal to zero:
   $$a - 4 = 0 \implies a = 4$$

3. **$\hat{k}$-component:**
   $$\frac{\partial}{\partial x}(bx - 3y - z) - \frac{\partial}{\partial y}(x + 2y + az) = b - 2$$
   Setting this equal to zero:
   $$b - 2 = 0 \implies b = 2$$

Thus, the vector field is irrotational when:
$$a = 4, \quad b = 2, \quad c = -1$$

---
### Part 2: Show that $\vec{F}$ is Solenoidal for all $a, b, c$

A vector field is **solenoidal** if its divergence is identically zero everywhere: $\nabla \cdot \vec{F} = 0$.
Compute the divergence of $\vec{F}$:
$$\nabla \cdot \vec{F} = \frac{\partial F_1}{\partial x} + \frac{\partial F_2}{\partial y} + \frac{\partial F_3}{\partial z}$$
$$\frac{\partial F_1}{\partial x} = \frac{\partial}{\partial x}(x + 2y + az) = 1$$
$$\frac{\partial F_2}{\partial y} = \frac{\partial}{\partial y}(bx - 3y - z) = -3$$
$$\frac{\partial F_3}{\partial z} = \frac{\partial}{\partial z}(4x + cy + 2z) = 2$$

Summing these partial derivatives:
$$\nabla \cdot \vec{F} = 1 + (-3) + 2 = 1 - 3 + 2 = 0$$

Notice that the divergence calculation is completely independent of the parameters $a, b$, and $c$. The algebraic sum of the direct coordinate partial derivatives evaluates identically to zero. Therefore, $\vec{F}$ is strictly **solenoidal** for all arbitrary real values of $a, b$, and $c$.
"""
    },
    {
        "qid": "vcdet-q10",
        "marks": 7,
        "type": "Analytical Problem",
        "title": "Fundamental Radial Vector Identities and Harmonicity of the Inverse Distance Potential",
        "yt_query": "gradient of r^n divergence r^n r laplacian r^n harmonic 1/r engineering mathematics",
        "img_path": "",
        "img_caption": "",
        "answer": r"""
Let $\vec{r} = x\hat{i} + y\hat{j} + z\hat{k}$ be the position vector in three-dimensional Euclidean space $\mathbb{R}^3$, and let $r = |\vec{r}| = \sqrt{x^2 + y^2 + z^2}$ be its Euclidean magnitude (distance from the origin).

**Preliminary Partial Derivatives of $r$:**
Since $r^2 = x^2 + y^2 + z^2$, differentiating implicitly with respect to $x$:
$$2r \frac{\partial r}{\partial x} = 2x \implies \frac{\partial r}{\partial x} = \frac{x}{r}$$
By symmetry:
$$\frac{\partial r}{\partial y} = \frac{y}{r}, \quad \frac{\partial r}{\partial z} = \frac{z}{r}$$
The gradient of the scalar distance $r$ is:
$$\nabla r = \frac{\partial r}{\partial x}\hat{i} + \frac{\partial r}{\partial y}\hat{j} + \frac{\partial r}{\partial z}\hat{k} = \frac{x}{r}\hat{i} + \frac{y}{r}\hat{j} + \frac{z}{r}\hat{k} = \frac{\vec{r}}{r}$$

---
### Part (i): Prove that $\nabla(r^n) = n r^{n-2} \vec{r}$

By the chain rule of multivariable calculus:
$$\nabla(r^n) = \frac{d(r^n)}{dr} \nabla r$$
Since $\frac{d(r^n)}{dr} = n r^{n-1}$ and $\nabla r = \frac{\vec{r}}{r}$:
$$\nabla(r^n) = (n r^{n-1}) \left( \frac{\vec{r}}{r} \right) = n r^{n-2} \vec{r}$$
Hence proved.

---
### Part (ii): Prove that $\nabla \cdot (r^n \vec{r}) = (n + 3)r^n$

Using the standard vector identity for the divergence of a product of a scalar field $\phi$ and a vector field $\vec{A}$:
$$\nabla \cdot (\phi \vec{A}) = \phi (\nabla \cdot \vec{A}) + (\nabla \phi) \cdot \vec{A}$$
Let $\phi = r^n$ and $\vec{A} = \vec{r}$:
$$\nabla \cdot (r^n \vec{r}) = r^n (\nabla \cdot \vec{r}) + \nabla(r^n) \cdot \vec{r}$$

Now evaluate $\nabla \cdot \vec{r}$:
$$\nabla \cdot \vec{r} = \frac{\partial x}{\partial x} + \frac{\partial y}{\partial y} + \frac{\partial z}{\partial z} = 1 + 1 + 1 = 3$$
From Part (i), substitute $\nabla(r^n) = n r^{n-2}\vec{r}$:
$$\nabla(r^n) \cdot \vec{r} = (n r^{n-2} \vec{r}) \cdot \vec{r} = n r^{n-2} (\vec{r} \cdot \vec{r})$$
Since $\vec{r} \cdot \vec{r} = |\vec{r}|^2 = r^2$:
$$\nabla(r^n) \cdot \vec{r} = n r^{n-2} (r^2) = n r^n$$
Substitute both terms:
$$\nabla \cdot (r^n \vec{r}) = r^n (3) + n r^n = (n + 3)r^n$$
Hence proved.

---
### Part (iii): Prove that $\nabla^2(r^n) = n(n + 1)r^{n-2}$ and Harmonicity of $1/r$

The Laplacian operator $\nabla^2$ is defined as the divergence of the gradient:
$$\nabla^2(r^n) = \nabla \cdot [\nabla(r^n)]$$
From Part (i), $\nabla(r^n) = n r^{n-2} \vec{r}$. Therefore:
$$\nabla^2(r^n) = \nabla \cdot (n r^{n-2} \vec{r}) = n [\nabla \cdot (r^{n-2} \vec{r})]$$
Apply the result of Part (ii) with the replacement of exponent $n$ by $m = n - 2$:
$$\nabla \cdot (r^{n-2} \vec{r}) = ((n - 2) + 3) r^{n-2} = (n + 1)r^{n-2}$$
Multiply by the constant pre-factor $n$:
$$\nabla^2(r^n) = n(n + 1)r^{n-2}$$
Hence proved.

**Deduction: Proof that $1/r$ is Harmonic ($r \neq 0$):**
A scalar function $\psi$ is defined to be **harmonic** in a spatial region if it satisfies Laplace's equation:
$$\nabla^2 \psi = 0$$
Let $\psi = \frac{1}{r} = r^{-1}$. Here $n = -1$.
Substitute $n = -1$ into the general Laplacian formula:
$$\nabla^2(r^{-1}) = (-1)(-1 + 1)r^{-1 - 2} = (-1)(0)r^{-3} = 0 \quad (\text{for } r \neq 0)$$
Since $\nabla^2(1/r) = 0$, the inverse distance field $1/r$ is strictly harmonic everywhere in $\mathbb{R}^3 \setminus \{(0,0,0)\}$. This confirms why the electrostatic potential of a point charge and the gravitational potential of a point mass satisfy Laplace's equation in source-free space.
"""
    }
]

M2_BYHEART = {
    "vcdet-q6": {
        "eq": r'$$\nabla \phi = 8\hat{i} - \hat{j} - 10\hat{k}, \quad \hat{u} = \frac{2\hat{i} - \hat{j} - 2\hat{k}}{3} \implies D_{\hat{u}}\phi = \nabla\phi \cdot \hat{u} = \frac{37}{3}$$',
        "text": r'<strong>Directional Derivative:</strong> Represents the rate of change of a scalar field $\phi$ along a unit direction $\hat{u}$. Maximum rate of increase occurs along $\nabla\phi$ with magnitude $\|\nabla\phi\|$.'
    },
    "vcdet-q7": {
        "eq": r'$$\hat{n} = \frac{\nabla f}{|\nabla f|} = \frac{\hat{i} + \hat{j} + 2\hat{k}}{\sqrt{6}}, \quad \text{Tangent Plane: } x + y + 2z = 4$$',
        "text": r'<strong>Unit Normal & Tangent Plane:</strong> Gradient $\nabla f$ at any point on the level surface $f(x,y,z) = c$ defines the orthogonal surface normal. The tangent plane equation is $\nabla f \cdot (\vec{r} - \vec{r}_0) = 0$.'
    },
    "vcdet-q8": {
        "eq": r'$$\nabla \times \vec{F} = \vec{0} \implies \phi = x^2 y + x z^3, \quad W = \phi(3, 1, 4) - \phi(1, -2, 1) = 201 - (-1) = 202$$',
        "text": r'<strong>Conservative Field & Potential:</strong> An irrotational field ($\nabla \times \vec{F} = 0$) possesses a scalar potential $\vec{F} = \nabla\phi$. Line integrals are path-independent, reducing work done simply to $\phi(\text{end}) - \phi(\text{start})$.'
    },
    "vcdet-q9": {
        "eq": r'$$\nabla \times \vec{F} = \vec{0} \implies a = 4, \; b = 2, \; c = -1; \quad \nabla \cdot \vec{F} = 1 - 3 + 2 = 0 \text{ (Solenoidal for all } a,b,c \text{)}$$',
        "text": r'<strong>Irrotational and Solenoidal Fields:</strong> $\vec{F}$ is irrotational if $\nabla \times \vec{F} = \vec{0}$ (symmetric Jacobian). $\vec{F}$ is solenoidal if $\nabla \cdot \vec{F} = 0$ (divergence-free, zero net flux expansion).'
    },
    "vcdet-q10": {
        "eq": r'$$\nabla(r^n) = n r^{n-2}\vec{r}, \quad \nabla \cdot (r^n \vec{r}) = (n+3)r^n, \quad \nabla^2(r^n) = n(n+1)r^{n-2} \implies \nabla^2(r^{-1}) = 0$$',
        "text": r'<strong>Radial Field Vector Identities:</strong> Central fields have radial gradients. The Laplacian $\nabla^2(r^n) = n(n+1)r^{n-2}$ vanishes identically for $n = -1$, proving that the Coulomb/Newtonian potential $1/r$ satisfies Laplace\'s equation.'
    }
}
