# -*- coding: utf-8 -*-
"""
Module 5 for Subject 1: Linear Algebra and Calculus (MAT101 / MATHS - LAC)
Multiple Integrals, Polar Transformations & Volume Computation
"""

M5_QUESTIONS = [
    {
        "qid": "lac-q21",
        "marks": 3,
        "type": "Short Answer",
        "title": "Double Integral Evaluation via Transformation to Polar Coordinates",
        "yt_query": "evaluate double integral polar coordinates unit circle first quadrant",
        "img_path": "",
        "img_caption": "",
        "answer": r"""
We are required to evaluate the Cartesian double integral:
$$I = \int_{x=0}^1 \int_{y=0}^{\sqrt{1 - x^2}} (x^2 + y^2) \, dy \, dx$$
by transforming into plane polar coordinates.

**Step 1: Identify the Region of Integration $R$ in the $xy$-Plane**
Examining the Cartesian limits:
- The inner integral runs from the lower boundary $y = 0$ ($x$-axis) to the upper boundary $y = \sqrt{1 - x^2}$.
  Squaring both sides of $y = \sqrt{1 - x^2}$ yields $x^2 + y^2 = 1$ with $y \ge 0$, which represents the upper semicircle of the unit circle centered at the origin with radius $R = 1$.
- The outer integral runs from $x = 0$ to $x = 1$.
Therefore, the region of integration $R$ is precisely the **first quadrant** of the circular disk $x^2 + y^2 \le 1$.

**Step 2: Transform to Polar Coordinates**
Substitute the standard polar coordinate relations:
$$x = r \cos \theta, \quad y = r \sin \theta$$
The integrand simplifies to:
$$x^2 + y^2 = r^2 \cos^2 \theta + r^2 \sin^2 \theta = r^2$$
The infinitesimal differential area element transforms via the Jacobian determinant:
$$dx \, dy = |J| \, dr \, d\theta = r \, dr \, d\theta$$

**Step 3: Determine Polar Limits of Integration**
- The radial distance $r$ extends from the origin $r = 0$ to the circular boundary $r = 1$.
- The polar angle $\theta$ spans the first quadrant from the positive $x$-axis ($\theta = 0$) to the positive $y$-axis ($\theta = \frac{\pi}{2}$).

**Step 4: Evaluate the Transformed Integral**
$$I = \int_{\theta=0}^{\pi/2} \int_{r=0}^1 (r^2) \cdot (r \, dr \, d\theta) = \int_{\theta=0}^{\pi/2} \int_{r=0}^1 r^3 \, dr \, d\theta$$
Because the limits of integration are decoupled constants and the integrand factors into single-variable functions:
$$I = \left( \int_{\theta=0}^{\pi/2} d\theta \right) \left( \int_{r=0}^1 r^3 \, dr \right)$$
Evaluate each single integral:
$$\int_0^{\pi/2} d\theta = [\theta]_0^{\pi/2} = \frac{\pi}{2}$$
$$\int_0^1 r^3 \, dr = \left[ \frac{r^4}{4} \right]_0^1 = \frac{1^4}{4} - 0 = \frac{1}{4}$$
Multiply the results:
$$I = \left(\frac{\pi}{2}\right) \left(\frac{1}{4}\right) = \frac{\pi}{8}$$
"""
    },
    {
        "qid": "lac-q22",
        "marks": 3,
        "type": "Short Answer",
        "title": "Reversal of Order of Integration for Parabolic-Linear Enclosed Domain",
        "yt_query": "change order of integration double integral parabola line engineering mathematics",
        "img_path": "",
        "img_caption": "",
        "answer": r"""
We are required to change the order of integration in the double integral:
$$I = \int_{x=0}^1 \int_{y=x}^{\sqrt{x}} f(x, y) \, dy \, dx$$

**Step 1: Identify the Original Limits and Geometry of the Region $R$**
In the given order $dy \, dx$:
- Vertical strips are utilized.
- Inner limits: $y$ varies from the lower straight line $y = x$ to the upper parabolic arc $y = \sqrt{x}$ (which is the parabola $y^2 = x$ in the upper half plane).
- Outer limits: $x$ varies from $x = 0$ to $x = 1$.

**Step 2: Find the Intersection Points of the Boundary Curves**
Equate the two boundary equations:
$$y = x \quad \text{and} \quad y^2 = x$$
$$x^2 = x \implies x^2 - x = 0 \implies x(x - 1) = 0$$
Thus, the boundary curves intersect at:
$$(0, 0) \quad \text{and} \quad (1, 1)$$
Throughout the interval $0 \le x \le 1$, $\sqrt{x} \ge x$, confirming that the parabolic arc $y = \sqrt{x}$ lies strictly above the straight line $y = x$.

**Step 3: Construct Horizontal Strips for the Reversed Order $dx \, dy$**
To reverse the order of integration, we slice the region $R$ into horizontal strips parallel to the $x$-axis:
- Each horizontal strip enters the region from the left along the parabolic boundary $y = \sqrt{x} \implies x = y^2$.
- The horizontal strip exits the region on the right along the straight line $y = x \implies x = y$.
Hence, for a fixed value of $y$, $x$ varies from $x = y^2$ to $x = y$.
- The vertical extent of the region spans from the bottom-most point $y = 0$ to the top-most intersection point $y = 1$.
Hence, $y$ varies from $y = 0$ to $y = 1$.

**Step 4: Formulate the Transformed Integral**
With the order of integration reversed:
$$I = \int_{y=0}^1 \int_{x=y^2}^y f(x, y) \, dx \, dy$$
"""
    },
    {
        "qid": "lac-q23",
        "marks": 7,
        "type": "Analytical Problem",
        "title": "Improper Double Integral in Polar Form and Proof of the Gaussian Integral",
        "yt_query": "gaussian integral evaluation using polar coordinates double integral e^-x^2",
        "img_path": "",
        "img_caption": "",
        "answer": r"""
We are required to evaluate the improper double integral:
$$I = \int_{x=0}^\infty \int_{y=0}^\infty e^{-(x^2 + y^2)} \, dy \, dx$$
by transforming into polar coordinates, and hence rigorously deduce the value of the famous Gaussian integral:
$$J = \int_0^\infty e^{-x^2} \, dx = \frac{\sqrt{\pi}}{2}$$

**Step 1: Region of Integration in the Cartesian Plane**
The Cartesian limits of integration are $0 \le x < \infty$ and $0 \le y < \infty$.
This domain represents the entire **first quadrant** of the two-dimensional infinite plane $\mathbb{R}^2$.

**Step 2: Transformation to Polar Coordinates**
Let:
$$x = r \cos \theta, \quad y = r \sin \theta \implies x^2 + y^2 = r^2$$
The differential area element is:
$$dx \, dy = r \, dr \, d\theta$$
The first quadrant is characterized in polar coordinates by:
- Radial distance: $r$ ranges from $0$ to $\infty$.
- Polar angle: $\theta$ ranges from $0$ to $\frac{\pi}{2}$.

**Step 3: Evaluate the Transformed Polar Double Integral**
Substitute these polar quantities into the integral:
$$I = \int_{\theta=0}^{\pi/2} \int_{r=0}^\infty e^{-r^2} (r \, dr \, d\theta) = \left( \int_0^{\pi/2} d\theta \right) \left( \int_0^\infty r e^{-r^2} \, dr \right)$$

1. Angular integral:
   $$\int_0^{\pi/2} d\theta = [\theta]_0^{\pi/2} = \frac{\pi}{2}$$

2. Radial integral:
   Evaluate $K = \int_0^\infty r e^{-r^2} \, dr$ by substitution. Let:
   $$u = r^2 \implies du = 2r \, dr \implies r \, dr = \frac{du}{2}$$
   When $r = 0$, $u = 0$; when $r \to \infty$, $u \to \infty$.
   $$K = \int_0^\infty e^{-u} \frac{du}{2} = \frac{1}{2} \left[ -e^{-u} \right]_0^\infty = \frac{1}{2} \left( 0 - (-1) \right) = \frac{1}{2}$$

Multiplying the two independent single integrals:
$$I = \left(\frac{\pi}{2}\right) \left(\frac{1}{2}\right) = \frac{\pi}{4}$$

**Step 4: Deduction of the Gaussian Integral $J$**
Notice that the original integrand $e^{-(x^2 + y^2)} = e^{-x^2} e^{-y^2}$ factors into two completely independent functions of $x$ and $y$. Because the region of integration is the Cartesian product $[0, \infty) \times [0, \infty)$, Fubini's theorem allows factoring:
$$I = \int_0^\infty \int_0^\infty e^{-x^2} e^{-y^2} \, dx \, dy = \left( \int_0^\infty e^{-x^2} \, dx \right) \left( \int_0^\infty e^{-y^2} \, dy \right)$$
Since $x$ and $y$ are dummy integration variables, both single integrals are identical:
$$\int_0^\infty e^{-x^2} \, dx = \int_0^\infty e^{-y^2} \, dy = J$$
Therefore:
$$I = J \cdot J = J^2$$
From Step 3, we proved that $I = \frac{\pi}{4}$. Thus:
$$J^2 = \frac{\pi}{4}$$
Taking the positive square root (since $e^{-x^2} > 0$ everywhere):
$$J = \int_0^\infty e^{-x^2} \, dx = \frac{\sqrt{\pi}}{2}$$

*(Note: For the two-sided Gaussian integral over the entire real line $(-\infty, \infty)$, since $e^{-x^2}$ is strictly even, $\int_{-\infty}^\infty e^{-x^2} dx = 2J = \sqrt{\pi}$.)*
"""
    },
    {
        "qid": "lac-q24",
        "marks": 7,
        "type": "Analytical Problem",
        "title": "Order of Integration Reversal and Evaluation of Rational Double Integral",
        "yt_query": "change order of integration x over x^2 plus y^2 double integral",
        "img_path": "",
        "img_caption": "",
        "answer": r"""
We are required to change the order of integration and evaluate the double integral:
$$I = \int_{y=0}^a \int_{x=y}^a \frac{x}{x^2 + y^2} \, dx \, dy$$

**Step 1: Analyze the Original Limits and Geometry of Region $R$**
In the given order $dx \, dy$:
- Horizontal strips are utilized.
- Inner limits: $x$ varies from the lower straight line $x = y$ to the vertical line $x = a$.
- Outer limits: $y$ varies from the horizontal axis $y = 0$ to $y = a$.
Geometrically, this represents a right-angled triangular domain bounded by:
1. The line $y = 0$ ($x$-axis)
2. The line $x = a$ (vertical line)
3. The line $y = x$ (diagonal line of slope 1)
The vertices of this triangle are located at $(0, 0), (a, 0),$ and $(a, a)$.

**Step 2: Reverse the Order of Integration ($dy \, dx$)**
To reverse the order of integration, we slice the triangular region using vertical strips parallel to the $y$-axis:
- Each vertical strip enters the region from the bottom along the line $y = 0$.
- The vertical strip exits the region at the top along the line $y = x$.
Hence, for a fixed value of $x$, $y$ varies from $y = 0$ to $y = x$.
- The horizontal span of the triangle runs from $x = 0$ to $x = a$.
Hence, $x$ varies from $x = 0$ to $x = a$.

The integral with changed order becomes:
$$I = \int_{x=0}^a \left[ \int_{y=0}^x \frac{x}{x^2 + y^2} \, dy \right] dx$$

**Step 3: Evaluate the Inner Integral with respect to $y$**
In the inner integral, $x$ is held constant. Recall the standard standard inverse-tangent integral formula:
$$\int \frac{1}{y^2 + x^2} \, dy = \frac{1}{x} \tan^{-1}\left( \frac{y}{x} \right)$$
Multiplying by the constant numerator $x$:
$$\int_{y=0}^x \frac{x}{x^2 + y^2} \, dy = x \left[ \frac{1}{x} \tan^{-1}\left( \frac{y}{x} \right) \right]_{y=0}^{y=x} = \left[ \tan^{-1}\left( \frac{y}{x} \right) \right]_{y=0}^{y=x}$$
Evaluate at the limits:
$$= \tan^{-1}\left( \frac{x}{x} \right) - \tan^{-1}(0) = \tan^{-1}(1) - 0 = \frac{\pi}{4}$$
The inner integral evaluates to the constant $\frac{\pi}{4}$, completely independent of $x$.

**Step 4: Evaluate the Outer Integral with respect to $x$**
Substitute the result of the inner integral:
$$I = \int_{x=0}^a \frac{\pi}{4} \, dx = \frac{\pi}{4} [x]_0^a = \frac{\pi}{4} (a - 0) = \frac{\pi a}{4}$$
"""
    },
    {
        "qid": "lac-q25",
        "marks": 7,
        "type": "Analytical Problem",
        "title": "Double Integral Area Computation Enclosed by Conjugate Parabolas",
        "yt_query": "area bounded by parabolas y^2=4ax and x^2=4ay double integration",
        "img_path": "",
        "img_caption": "",
        "answer": r"""
We are required to compute the area bounded between the two intersecting parabolas:
$$y^2 = 4ax \quad \text{and} \quad x^2 = 4ay \quad (a > 0)$$
using double integration.

**Step 1: Find Points of Intersection**
Express $y$ from the second parabola:
$$y = \frac{x^2}{4a}$$
Substitute this into the equation of the first parabola:
$$\left( \frac{x^2}{4a} \right)^2 = 4ax \implies \frac{x^4}{16a^2} = 4ax$$
$$x^4 = 64a^3 x \implies x^4 - 64a^3 x = 0 \implies x(x^3 - 64a^3) = 0$$
The real roots are:
$$x = 0 \quad \text{and} \quad x = (64a^3)^{1/3} = 4a$$

Find corresponding $y$-values:
- At $x = 0$: $y = \frac{0^2}{4a} = 0 \implies (0, 0)$ (the origin).
- At $x = 4a$: $y = \frac{(4a)^2}{4a} = \frac{16a^2}{4a} = 4a \implies (4a, 4a)$.
The two parabolas enclose a single bounded region spanning from $x = 0$ to $x = 4a$.

**Step 2: Determine Upper and Lower Boundary Functions**
For any $x \in (0, 4a)$:
- Lower boundary curve: $y_1(x) = \frac{x^2}{4a}$ (from $x^2 = 4ay$)
- Upper boundary curve: $y_2(x) = \sqrt{4ax} = 2\sqrt{a} \sqrt{x}$ (from $y^2 = 4ax$)

**Step 3: Set up the Double Integral for Area**
$$\text{Area } A = \iint_R dy \, dx = \int_{x=0}^{4a} \left[ \int_{y=x^2/(4a)}^{2\sqrt{a}\sqrt{x}} dy \right] dx$$

**Step 4: Evaluate the Inner and Outer Integrals**
Evaluate the inner integral:
$$\int_{x^2/(4a)}^{2\sqrt{a}\sqrt{x}} dy = [y]_{x^2/(4a)}^{2\sqrt{a}\sqrt{x}} = 2\sqrt{a} x^{1/2} - \frac{x^2}{4a}$$

Now evaluate the outer integral with respect to $x$:
$$A = \int_0^{4a} \left( 2\sqrt{a} x^{1/2} - \frac{1}{4a} x^2 \right) dx$$
$$= 2\sqrt{a} \left[ \frac{x^{3/2}}{3/2} \right]_0^{4a} - \frac{1}{4a} \left[ \frac{x^3}{3} \right]_0^{4a}$$
$$= \frac{4\sqrt{a}}{3} (4a)^{3/2} - \frac{1}{12a} (4a)^3$$

Compute each term:
$$(4a)^{3/2} = (\sqrt{4a})^3 = (2\sqrt{a})^3 = 8 a\sqrt{a} = 8a^{3/2}$$
$$(4a)^3 = 64a^3$$
Substitute these values:
$$A = \frac{4\sqrt{a}}{3} (8 a\sqrt{a}) - \frac{1}{12a} (64a^3)$$
$$A = \frac{32a^2}{3} - \frac{64a^2}{12} = \frac{32a^2}{3} - \frac{16a^2}{3} = \frac{16a^2}{3}$$
Thus, the enclosed area is $\frac{16a^2}{3}$ square units.
"""
    },
    {
        "qid": "lac-q26",
        "marks": 7,
        "type": "Analytical Problem",
        "title": "Triple Integral Volume Determination of Truncated Right Circular Cylinder",
        "yt_query": "volume bounded by cylinder x^2+y^2=4 planes y+z=4 z=0 triple integration",
        "img_path": "",
        "img_caption": "",
        "answer": r"""
We are required to determine the volume of the solid region bounded by:
- The right circular cylinder: $x^2 + y^2 = 4$
- The upper inclined plane: $y + z = 4 \implies z = 4 - y$
- The lower horizontal plane: $z = 0$
using triple integration.

**Step 1: Set up the Volume Integral in Cylindrical Coordinates**
Because the lateral boundary is a circular cylinder centered on the $z$-axis, cylindrical coordinates $(r, \theta, z)$ are the most natural and efficient coordinate system:
$$x = r \cos \theta, \quad y = r \sin \theta, \quad z = z$$
The differential volume element in cylindrical coordinates is:
$$dV = dz \, r \, dr \, d\theta$$

**Step 2: Determine Limits of Integration**
- **$z$-limits:** The solid is bounded below by the plane $z = 0$ and above by the inclined plane $z = 4 - y = 4 - r \sin \theta$.
  Since $r \le 2$, $4 - r \sin \theta \ge 4 - 2 = 2 > 0$, guaranteeing that the upper plane always lies strictly above $z = 0$.
  Hence $z$ ranges from $0$ to $4 - r \sin \theta$.
- **$r$-limits:** The projection of the cylinder onto the $xy$-plane is the circular disk $x^2 + y^2 \le 4$, so $r$ ranges from $0$ to $2$.
- **$\theta$-limits:** The full cross-section requires tracing the complete circle, so $\theta$ ranges from $0$ to $2\pi$.

**Step 3: Evaluate the Triple Integral**
$$V = \iiint_D dV = \int_{\theta=0}^{2\pi} \int_{r=0}^2 \int_{z=0}^{4 - r \sin \theta} dz \, r \, dr \, d\theta$$

Evaluate the innermost integral with respect to $z$:
$$\int_{z=0}^{4 - r \sin \theta} dz = [z]_0^{4 - r \sin \theta} = 4 - r \sin \theta$$
Substitute into the double integral:
$$V = \int_{\theta=0}^{2\pi} \int_{r=0}^2 (4 - r \sin \theta) r \, dr \, d\theta = \int_{\theta=0}^{2\pi} \int_{r=0}^2 (4r - r^2 \sin \theta) \, dr \, d\theta$$

Evaluate the inner integral with respect to $r$:
$$\int_{r=0}^2 (4r - r^2 \sin \theta) \, dr = \left[ 2r^2 - \frac{r^3}{3} \sin \theta \right]_{r=0}^2 = 2(2^2) - \frac{2^3}{3} \sin \theta = 8 - \frac{8}{3} \sin \theta$$

Evaluate the outer integral with respect to $\theta$:
$$V = \int_0^{2\pi} \left( 8 - \frac{8}{3} \sin \theta \right) d\theta = \int_0^{2\pi} 8 \, d\theta - \frac{8}{3} \int_0^{2\pi} \sin \theta \, d\theta$$
$$\int_0^{2\pi} 8 \, d\theta = [8\theta]_0^{2\pi} = 8(2\pi) = 16\pi$$
$$\int_0^{2\pi} \sin \theta \, d\theta = [-\cos \theta]_0^{2\pi} = -\cos(2\pi) - (-\cos 0) = -1 - (-1) = 0$$
Therefore:
$$V = 16\pi - \frac{8}{3}(0) = 16\pi$$
The volume of the truncated cylinder is $16\pi$ cubic units.
"""
    }
]

M5_BYHEART = {
    "lac-q21": {
        "eq": r'$$\int_0^1 \int_0^{\sqrt{1-x^2}} (x^2 + y^2) \, dy \, dx = \int_0^{\pi/2} d\theta \int_0^1 r^3 \, dr = \left(\frac{\pi}{2}\right)\left(\frac{1}{4}\right) = \frac{\pi}{8}$$',
        "text": r'<strong>Cartesian to Polar Conversion:</strong> Substitute $x = r\cos\theta, y = r\sin\theta, dx\,dy = r\,dr\,d\theta$. The first-quadrant unit circular arc transforms to limits $r \in [0, 1]$ and $\theta \in [0, \pi/2]$.'
    },
    "lac-q22": {
        "eq": r'$$\int_{x=0}^1 \int_{y=x}^{\sqrt{x}} f(x, y) \, dy \, dx = \int_{y=0}^1 \int_{x=y^2}^y f(x, y) \, dx \, dy$$',
        "text": r'<strong>Change of Order of Integration:</strong> Sketch the region bounded by $y = x$ and $y = \sqrt{x}$. Switch from vertical strips ($x$-constant) to horizontal strips ($y$-constant), changing bounds from $y \in [x, \sqrt{x}]$ to $x \in [y^2, y]$.'
    },
    "lac-q23": {
        "eq": r'$$\int_0^\infty \int_0^\infty e^{-(x^2+y^2)} \, dx \, dy = \frac{\pi}{4} \implies \left(\int_0^\infty e^{-x^2} \, dx\right)^2 = \frac{\pi}{4} \implies \int_0^\infty e^{-x^2} \, dx = \frac{\sqrt{\pi}}{2}$$',
        "text": r'<strong>Gaussian Integral Evaluation via Double Integrals:</strong> Cartesian integration of $e^{-x^2}$ lacks elementary antiderivative. Converting $J^2$ to polar coordinates yields $r e^{-r^2}$, readily integrable to $\pi/4$, proving $J = \sqrt{\pi}/2$.'
    },
    "lac-q24": {
        "eq": r'$$\int_0^a \int_y^a \frac{x}{x^2 + y^2} \, dx \, dy = \int_0^a \left[\int_0^x \frac{x}{x^2 + y^2} \, dy \right] dx = \int_0^a \frac{\pi}{4} \, dx = \frac{\pi a}{4}$$',
        "text": r'<strong>Change of Order for Triangular Domain:</strong> Switching order from $dx\,dy$ to $dy\,dx$ converts the complicated logarithmic $x$-integral into a standard inverse tangent $\tan^{-1}(y/x)$, collapsing the inner integral to constant $\pi/4$.'
    },
    "lac-q25": {
        "eq": r'$$\text{Area} = \int_0^{4a} \left(2\sqrt{ax} - \frac{x^2}{4a}\right) dx = \left[\frac{4\sqrt{a}}{3}x^{3/2} - \frac{x^3}{12a}\right]_0^{4a} = \frac{16a^2}{3}$$',
        "text": r'<strong>Area Enclosed by Conjugate Parabolas:</strong> The intersection between $y^2 = 4ax$ and $x^2 = 4ay$ spans $[0, 4a]$. Double integration yields the celebrated classical area result $\frac{16a^2}{3}$.'
    },
    "lac-q26": {
        "eq": r'$$V = \int_0^{2\pi} \int_0^2 (4 - r\sin\theta) r \, dr \, d\theta = \int_0^{2\pi} \left(8 - \frac{8}{3}\sin\theta\right) d\theta = 16\pi$$',
        "text": r'<strong>Volume of Truncated Cylinder via Cylindrical Coordinates:</strong> Cylindrical coordinates simplify circular boundaries ($r \le 2$). The odd periodic term $\sin\theta$ integrates to zero over $[0, 2\pi]$, leaving mean height $4$ times base area $\pi(2^2) = 16\pi$.'
    }
}
