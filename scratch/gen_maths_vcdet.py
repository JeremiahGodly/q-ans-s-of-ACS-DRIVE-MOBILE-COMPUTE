# -*- coding: utf-8 -*-
"""
Content generator for Subject 2: Vector Calculus, Differential Equations and Transforms (MAT102 / MATHS - VCDET)
KTU 2019 Scheme Electrical & Electronics Engineering (EEE) Question Bank.
All answers written from the perspective of an experienced engineering mathematics professor.
Contains complete step-by-step mathematical working, intermediate equations, and highlighted results.
All strings use raw multiline strings to prevent any LaTeX escape corruptions.
Equations use standard KaTeX syntax: $$...$$ for display equations, $...$ for inline math.
"""

MATHS_VCDET_EXAM_QUESTIONS = {
    "vcdet-q1": "Solve Bernoulli's differential equation dy/dx + y = y^2 (cos x - sin x).",
    "vcdet-q2": 'Solve the second order differential equation (D^2 - 4D + 4)y = 8e^(2x) + sin 2x.',
    "vcdet-q3": 'Solve the differential equation d^2y/dx^2 + y = sec x tan x using the method of variation of parameters.',
    "vcdet-q4": 'Solve the Cauchy-Euler differential equation: x^2 d^2y/dx^2 - 3x dy/dx + 4y = 2x^2 using the transformation x = e^z.',
    "vcdet-q5": 'Solve the non-homogeneous higher order linear differential equation: (D^2 - 2D + 1)y = x e^x sin x using the exponential shift operator.',
    "vcdet-q6": 'Find the directional derivative of phi(x, y, z) = x^2 y z + 4 x z^2 at the point (1, -2, -1) in the direction of the vector a = 2i - j - 2k.',
    "vcdet-q7": 'Find the unit normal vector to the surface x^2 + y^2 + 2z^2 = 4 at the point (1, 1, 1), and find the equation of the tangent plane.',
    "vcdet-q8": 'Show that the vector field F = (2xy + z^3)i + x^2 j + 3xz^2 k is conservative and irrotational. Find its scalar potential phi(x, y, z) such that F = grad phi. Hence evaluate the work done in moving a particle from (1, -2, 1) to (3, 1, 4).',
    "vcdet-q9": 'Find constants a, b, c such that the vector field F = (x + 2y + az)i + (bx - 3y - z)j + (4x + cy + 2z)k is irrotational. Also show that F is solenoidal for all values of a, b, c.',
    "vcdet-q10": 'If r = x i + y j + z k and r = |r|, prove that: (i) grad(r^n) = n r^(n-2) r, (ii) div(r^n r) = (n+3)r^n, and (iii) Laplacian(r^n) = n(n+1)r^(n-2). Hence show that 1/r is harmonic for r != 0.',
    "vcdet-q11": "Using Green's theorem, evaluate the line integral oint_C [(x - y) dx + (x + y) dy] where C is the closed curve bounded by y = x^2 and y^2 = x traversed counter-clockwise.",
    "vcdet-q12": 'State Gauss divergence theorem and explain its physical significance in electrostatics and fluid mechanics.',
    "vcdet-q13": "Verify Green's theorem in the plane for oint_C [(xy + y^2) dx + x^2 dy] where C is the closed curve bounded by y = x and y = x^2.",
    "vcdet-q14": 'Verify Gauss divergence theorem for F = 4xz i - y^2 j + yz k over the cube bounded by x = 0, x = 1, y = 0, y = 1, z = 0, z = 1.',
    "vcdet-q15": "Verify Stokes' theorem for F = (2x - y)i - yz^2 j - y^2 z k over the upper hemisphere S: x^2 + y^2 + z^2 = 1, z >= 0 bounded by the circle C: x^2 + y^2 = 1 in the xy-plane.",
    "vcdet-q16": "State Dirichlet's conditions for the existence of Fourier series of a function f(x) in an interval (c, c + 2L). What does the Fourier series converge to at a point of finite discontinuity?",
    "vcdet-q17": 'Find the half-range Fourier sine series expansion for f(x) = k (constant) in the interval 0 < x < pi.',
    "vcdet-q18": 'Find the Fourier series of f(x) = x^2 in the interval -pi <= x <= pi. Hence deduce that: (i) sum_{n=1}^infinity (-1)^(n-1)/n^2 = pi^2/12, and (ii) sum_{n=1}^infinity 1/n^2 = pi^2/6.',
    "vcdet-q19": 'Find the Fourier series of the periodic square wave: f(x) = -k for -pi < x < 0 and k for 0 < x < pi with period 2pi. Hence deduce the Gregory-Leibniz series for pi: 1 - 1/3 + 1/5 - 1/7 + ... = pi/4.',
    "vcdet-q20": 'Find the Fourier cosine and sine transforms of f(x) = e^(-ax) (a > 0). Hence evaluate the integral int_0^infinity cos(omega*x) / (a^2 + omega^2) d(omega).',
    "vcdet-q21": 'Find the Laplace transform of f(t) = t^2 e^(-3t) sin 2t.',
    "vcdet-q22": 'State the Convolution Theorem for Laplace transforms. Use it to find L^(-1){1 / (s(s^2 + 1))}.',
    "vcdet-q23": 'Evaluate L{(cos at - cos bt) / t} and hence compute the improper integral int_0^infinity (cos t - cos 2t) / t dt.',
    "vcdet-q24": 'Using the Convolution Theorem, find the inverse Laplace transform of F(s) = 1 / (s^2 + a^2)^2.',
    "vcdet-q25": "Solve the initial value problem using Laplace transform: d^2y/dt^2 + 4 dy/dt + 4y = 6 e^(-2t) subject to y(0) = -2 and y'(0) = 8.",
    "vcdet-q26": 'Solve the system of simultaneous ordinary differential equations using Laplace transform: dx/dt + y = sin t, dy/dt + x = cos t subject to x(0) = 1 and y(0) = 0.',
}

MATHS_VCDET_BYHEART = {
    "vcdet-q1": {
        "eq": r"""$$v = y^{-1} \implies \frac{dv}{dx} - v = \sin x - \cos x \implies \frac{1}{y} = C e^x - \sin x$$""",
        "text": r"""<strong>Bernoulli Equation Transformation:</strong> Dividing by $y^n$ and substituting $v = y^{1-n}$ transforms the non-linear Bernoulli ODE into a standard first-order linear ODE solvable via integrating factor $e^{\int P dx}$."""
    },
    "vcdet-q2": {
        "eq": r"""$$y = (C_1 + C_2 x) e^{2x} + 4x^2 e^{2x} + \frac{1}{8}\cos 2x$$""",
        "text": r"""<strong>Repeated Roots & Resonant PI:</strong> When auxiliary root $m=a$ is repeated $k$ times, complementary function includes $(C_1 + C_2 x)e^{ax}$, and particular integral for $e^{ax}$ introduces resonant factor $\frac{x^k}{k!} e^{ax}$."""
    },
    "vcdet-q3": {
        "eq": r"""$$W = 1, \; u(x) = x - \tan x, \; v(x) = \ln|\sec x| \implies y = C_1 \cos x + C_2 \sin x + x \cos x + \sin x \ln|\sec x|$$""",
        "text": r"""<strong>Variation of Parameters:</strong> For $y\'\' + y = R(x)$, basis solutions are $y_1 = \cos x, y_2 = \sin x$ with Wronskian $W = 1$. The formulas $u = -\int y_2 R / W \, dx$ and $v = \int y_1 R / W \, dx$ yield particular integrals for any non-elementary excitation."""
    },
    "vcdet-q4": {
        "eq": r"""$$[D_z(D_z-1) - 3D_z + 4]y = 2e^{2z} \implies y(x) = x^2 [C_1 + C_2 \ln x + (\ln x)^2]$$""",
        "text": r"""<strong>Cauchy-Euler Reduction:</strong> Setting $x = e^z$ converts variable-coefficient Cauchy-Euler equations into constant-coefficient ODEs in $z$, where $x^k \frac{d^k y}{dx^k} = D_z(D_z - 1)\dots(D_z - k + 1)y$."""
    },
    "vcdet-q5": {
        "eq": r"""$$y_p = e^x \frac{1}{D^2}[x \sin x] = -e^x(x\sin x + 2\cos x) \implies y = (C_1 + C_2 x)e^x - e^x(x\sin x + 2\cos x)$$""",
        "text": r"""<strong>Exponential Shift Theorem:</strong> Shifting $e^{ax}$ outside the differential operator via $f(D)[e^{ax} V] = e^{ax} f(D+a)V$ eliminates the exponential factor and reduces operator power."""
    },
    "vcdet-q6": {
        "eq": r"""$$\nabla \phi = 8\hat{i} - \hat{j} - 10\hat{k}, \quad \hat{u} = \frac{2\hat{i} - \hat{j} - 2\hat{k}}{3} \implies D_{\hat{u}}\phi = \nabla\phi \cdot \hat{u} = \frac{37}{3}$$""",
        "text": r"""<strong>Directional Derivative:</strong> Represents the rate of change of a scalar field $\phi$ along a unit direction $\hat{u}$. Maximum rate of increase occurs along $\nabla\phi$ with magnitude $\|\nabla\phi\|$."""
    },
    "vcdet-q7": {
        "eq": r"""$$\hat{n} = \frac{\nabla f}{|\nabla f|} = \frac{\hat{i} + \hat{j} + 2\hat{k}}{\sqrt{6}}, \quad \text{Tangent Plane: } x + y + 2z = 4$$""",
        "text": r"""<strong>Unit Normal & Tangent Plane:</strong> Gradient $\nabla f$ at any point on the level surface $f(x,y,z) = c$ defines the orthogonal surface normal. The tangent plane equation is $\nabla f \cdot (\vec{r} - \vec{r}_0) = 0$."""
    },
    "vcdet-q8": {
        "eq": r"""$$\nabla \times \vec{F} = \vec{0} \implies \phi = x^2 y + x z^3, \quad W = \phi(3, 1, 4) - \phi(1, -2, 1) = 201 - (-1) = 202$$""",
        "text": r"""<strong>Conservative Field & Potential:</strong> An irrotational field ($\nabla \times \vec{F} = 0$) possesses a scalar potential $\vec{F} = \nabla\phi$. Line integrals are path-independent, reducing work done simply to $\phi(\text{end}) - \phi(\text{start})$."""
    },
    "vcdet-q9": {
        "eq": r"""$$\nabla \times \vec{F} = \vec{0} \implies a = 4, \; b = 2, \; c = -1; \quad \nabla \cdot \vec{F} = 1 - 3 + 2 = 0 \text{ (Solenoidal for all } a,b,c \text{)}$$""",
        "text": r"""<strong>Irrotational and Solenoidal Fields:</strong> $\vec{F}$ is irrotational if $\nabla \times \vec{F} = \vec{0}$ (symmetric Jacobian). $\vec{F}$ is solenoidal if $\nabla \cdot \vec{F} = 0$ (divergence-free, zero net flux expansion)."""
    },
    "vcdet-q10": {
        "eq": r"""$$\nabla(r^n) = n r^{n-2}\vec{r}, \quad \nabla \cdot (r^n \vec{r}) = (n+3)r^n, \quad \nabla^2(r^n) = n(n+1)r^{n-2} \implies \nabla^2(r^{-1}) = 0$$""",
        "text": r"""<strong>Radial Field Vector Identities:</strong> Central fields have radial gradients. The Laplacian $\nabla^2(r^n) = n(n+1)r^{n-2}$ vanishes identically for $n = -1$, proving that the Coulomb/Newtonian potential $1/r$ satisfies Laplace\'s equation."""
    },
    "vcdet-q11": {
        "eq": r"""$$\oint_C [(x-y)dx + (x+y)dy] = \iint_R (1 - (-1)) dx\,dy = 2 \int_0^1 (\sqrt{x} - x^2)dx = 2\left(\frac{1}{3}\right) = \frac{2}{3}$$""",
        "text": r"""<strong>Green\'s Theorem in a Plane:</strong> Converts a closed line integral $\oint (Mdx + Ndy)$ into a double integral of $(\partial N/\partial x - \partial M/\partial y)$. When the integrand is constant 2, the integral simply equals $2 \times \text{enclosed area}$."""
    },
    "vcdet-q12": {
        "eq": r"""$$\iint_S \vec{F} \cdot \hat{n} \, dS = \iiint_V (\nabla \cdot \vec{F}) \, dV \iff \Phi_{\text{net}} = \iiint (\text{source density}) \, dV$$""",
        "text": r"""<strong>Gauss Divergence Theorem:</strong> Relates outward flux through a closed boundary surface to the volumetric accumulation of divergence within the bounded domain; underpins Gauss\'s Law in electromagnetics."""
    },
    "vcdet-q13": {
        "eq": r"""$$\oint_C = \int_{C_1} + \int_{C_2} = \frac{19}{20} - 1 = -\frac{1}{20} = \iint_R (x - 2y) dy\,dx$$""",
        "text": r"""<strong>Verification of Green\'s Theorem:</strong> Compute line integral along piecewise boundary curves ($C_1: y=x^2, C_2: y=x$) and compare against surface double integral of $(N_x - M_y) = x - 2y$; both equal $-1/20$."""
    },
    "vcdet-q14": {
        "eq": r"""$$\iiint_V (\nabla \cdot \vec{F}) dV = \int_0^1 \int_0^1 (4z - y) dydz = \frac{3}{2} = \sum_{i=1}^6 \iint_{S_i} \vec{F} \cdot \hat{n} \, dS$$""",
        "text": r"""<strong>Gauss Theorem Verification on Cube:</strong> Evaluate outward normal flux across all 6 faces ($\Phi = 2 + 0 - 1 + 0 + 1/2 + 0 = 3/2$) and confirm identity with volume integral of divergence $4z - y = 3/2$."""
    },
    "vcdet-q15": {
        "eq": r"""$$\nabla \times \vec{F} = \hat{k} \implies \iint_S (\nabla \times \vec{F}) \cdot \hat{n} \, dS = \iint_{x^2+y^2 \le 1} dx\,dy = \pi = \oint_C \vec{F} \cdot d\vec{r}$$""",
        "text": r"""<strong>Stokes\' Theorem Verification:</strong> The line integral of $\vec{F}$ around the equator boundary circle equals $\pi$. The curl simplifies to unit vertical vector $\hat{k}$, whose surface flux projects directly to the equatorial disc area $\pi$."""
    },
    "vcdet-q16": {
        "eq": r"""$$S(x_0) = \begin{cases} f(x_0) & \text{at points of continuity} \\ \frac{f(x_0^+) + f(x_0^-)}{2} & \text{at points of jump discontinuity} \end{cases}$$""",
        "text": r"""<strong>Dirichlet\'s Conditions & Discontinuity Convergence:</strong> Requires boundedness, finite extrema, and finite jump discontinuities. At any step discontinuity, the Fourier series converges strictly to the midpoint of the jump."""
    },
    "vcdet-q17": {
        "eq": r"""$$f(x) = \frac{4k}{\pi} \sum_{n=1,3,5,\dots}^\infty \frac{\sin nx}{n} = \frac{4k}{\pi}\left(\sin x + \frac{\sin 3x}{3} + \frac{\sin 5x}{5} + \dots\right)$$""",
        "text": r"""<strong>Half-Range Sine Series:</strong> All even harmonic coefficients vanish because $1 - (-1)^n = 0$. Odd harmonics decay as $1/n$, generating the classic synthesis of a constant step via sinusoidal basis modes."""
    },
    "vcdet-q18": {
        "eq": r"""$$x^2 = \frac{\pi^2}{3} + 4\sum_{n=1}^\infty \frac{(-1)^n}{n^2}\cos nx \implies \sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}, \quad \sum_{n=1}^\infty \frac{(-1)^{n-1}}{n^2} = \frac{\pi^2}{12}$$""",
        "text": r"""<strong>Fourier Expansion of Parabola:</strong> For even function $x^2$, $b_n = 0, a_n = 4(-1)^n/n^2$. Evaluating at $x=0$ and $x=\pi$ resolves the famous Basel problem $\sum 1/n^2 = \pi^2/6$."""
    },
    "vcdet-q19": {
        "eq": r"""$$f(x) = \frac{4k}{\pi} \sum_{n=1,3,5,\dots}^\infty \frac{\sin nx}{n} \implies \text{at } x = \frac{\pi}{2}: \quad 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \dots = \frac{\pi}{4}$$""",
        "text": r"""<strong>Square Wave Harmonic Spectrum:</strong> Contains purely odd harmonics with harmonic amplitudes decaying inversely as $1/n$. Evaluation at the peak $x = \pi/2$ directly establishes Leibniz\'s formula for $\pi$."""
    },
    "vcdet-q20": {
        "eq": r"""$$\mathcal{F}_c\{e^{-ax}\} = \frac{a}{a^2 + \omega^2}, \quad \mathcal{F}_s\{e^{-ax}\} = \frac{\omega}{a^2 + \omega^2} \implies \int_0^\infty \frac{\cos(\omega x)}{a^2 + \omega^2} d\omega = \frac{\pi}{2a}e^{-ax}$$""",
        "text": r"""<strong>Exponential Fourier Transforms:</strong> Cosine transform yields the Lorentzian spectrum $\frac{a}{a^2 + \omega^2}$. Applying inverse transform evaluates Laplace\'s famous contour integral $\frac{\pi}{2a}e^{-ax}$."""
    },
    "vcdet-q21": {
        "eq": r"""$$\mathcal{L}\{t^2 e^{-3t} \sin 2t\} = \frac{d^2}{ds^2}\left[\frac{2}{(s+3)^2 + 4}\right] = \frac{12s^2 + 72s + 92}{(s^2 + 6s + 13)^3}$$""",
        "text": r"""<strong>Multiplication by $t^n$ & First Shifting:</strong> Applying the first shift property replaces $s \to s + 3$. Differentiating twice with respect to $s$ implements multiplication by $t^2$ in the time domain."""
    },
    "vcdet-q22": {
        "eq": r"""$$\mathcal{L}^{-1}\{F(s)G(s)\} = \int_0^t f(u)g(t-u)du \implies \mathcal{L}^{-1}\left\{\frac{1}{s(s^2+1)}\right\} = \int_0^t \sin(t-u)du = 1 - \cos t$$""",
        "text": r"""<strong>Convolution Theorem:</strong> Transforms multiplication in the complex $s$-frequency domain into a convolution integral in the temporal domain, enabling direct calculation without partial fractions."""
    },
    "vcdet-q23": {
        "eq": r"""$$\mathcal{L}\left\{\frac{\cos at - \cos bt}{t}\right\} = \frac{1}{2}\ln\left(\frac{s^2 + b^2}{s^2 + a^2}\right) \implies \int_0^\infty \frac{\cos t - \cos 2t}{t} \, dt = \ln 2$$""",
        "text": r"""<strong>Division by $t$ & Frullani-Type Integrals:</strong> Dividing by $t$ in time corresponds to integrating $F(u)$ from $s$ to $\infty$. Letting $s \to 0$ computes classic improper integrals like $\int_0^\infty \frac{\cos t - \cos 2t}{t} dt = \ln 2$."""
    },
    "vcdet-q24": {
        "eq": r"""$$\mathcal{L}^{-1}\left\{\frac{1}{(s^2+a^2)^2}\right\} = \frac{1}{a^2}\int_0^t \sin(au)\sin(a(t-u))du = \frac{\sin at - at\cos at}{2a^3}$$""",
        "text": r"""<strong>Convolution of Resonant Poles:</strong> Convolving $\frac{1}{a}\sin at$ with itself generates the secular term $t\cos at$. The result describes resonance growth in undamped harmonic oscillators."""
    },
    "vcdet-q25": {
        "eq": r"""$$Y(s) = -\frac{2}{s+2} + \frac{4}{(s+2)^2} + \frac{6}{(s+2)^3} \implies y(t) = (3t^2 + 4t - 2)e^{-2t}$$""",
        "text": r"""<strong>Initial Value Problem via Laplace Transforms:</strong> Incorporates initial conditions automatically into algebraic equations in $s$. The repeated pole $(s+2)^3$ yields critical damping response terms $e^{-2t}, te^{-2t}$, and resonant forcing $t^2 e^{-2t}$."""
    },
    "vcdet-q26": {
        "eq": r"""$$X(s) = \frac{s}{s^2 - 1} \implies x(t) = \cosh t; \quad Y(s) = \frac{1}{s^2 + 1} - \frac{1}{s^2 - 1} \implies y(t) = \sin t - \sinh t$$""",
        "text": r"""<strong>Simultaneous Differential Systems:</strong> Coupled time-domain differential equations transform into a system of linear algebraic equations in $X(s)$ and $Y(s)$. Elimination reveals hyperbolic decoupling modes $\cosh t$ and $\sin t - \sinh t$."""
    },
}

MATHS_VCDET_MODULES = [
    {
        "module_id": "vcdet-m1",
        "module_num": "Module 1",
        "module_title": "Ordinary Differential Equations, Bernoulli & Cauchy-Euler Equations",
        "questions": [
            {
                "qid": "vcdet-q1",
                "marks": 3,
                "type": "Short Answer",
                "title": "Solution of Bernoulli's Non-Linear First Order Differential Equation",
                "yt_query": 'bernoulli differential equation first order non linear substitution integrating factor',
                "img_path": "",
                "img_caption": "",
                "answer": r"""
A first-order non-linear differential equation of the form:
$$\frac{dy}{dx} + P(x)y = Q(x)y^n$$
is known as **Bernoulli's equation**, where $P(x)$ and $Q(x)$ are continuous functions of $x$ (or constants) and $n \in \mathbb{R} \setminus \{0, 1\}$.

We are required to solve:
$$\frac{dy}{dx} + y = y^2 (\cos x - \sin x)$$
Here, $P(x) = 1, Q(x) = \cos x - \sin x$, and the non-linear power is $n = 2$.

**Step 1: Divide by $y^2$ to Normalize the Non-Linear Term**
Dividing the entire equation by $y^2$:
$$y^{-2} \frac{dy}{dx} + y^{-1} = \cos x - \sin x \quad \text{--- (Equation 1)}$$

**Step 2: Linearizing Substitution**
Let:
$$v = y^{1 - n} = y^{1 - 2} = y^{-1} = \frac{1}{y}$$
Differentiate $v$ with respect to $x$ using the chain rule:
$$\frac{dv}{dx} = -y^{-2} \frac{dy}{dx} \implies y^{-2} \frac{dy}{dx} = -\frac{dv}{dx}$$

**Step 3: Substitute into Equation (1)**
$$-\frac{dv}{dx} + v = \cos x - \sin x$$
Multiply through by $-1$ to establish the standard linear form:
$$\frac{dv}{dx} - v = \sin x - \cos x$$
This is a standard first-order linear ordinary differential equation in $v$ of the form:
$$\frac{dv}{dx} + P_1(x)v = Q_1(x)$$
with $P_1(x) = -1$ and $Q_1(x) = \sin x - \cos x$.

**Step 4: Determine Integrating Factor (IF)**
$$IF = e^{\int P_1(x) \, dx} = e^{\int -1 \, dx} = e^{-x}$$

**Step 5: Solve for $v(x)$**
The general solution for the linear equation is:
$$v \cdot IF = \int Q_1(x) \cdot IF \, dx + C$$
$$v e^{-x} = \int e^{-x} (\sin x - \cos x) \, dx + C$$
Notice that by the product rule of differentiation:
$$\frac{d}{dx} \left[ e^{-x} \sin x \right] = -e^{-x} \sin x + e^{-x} \cos x = -e^{-x} (\sin x - \cos x)$$
Therefore:
$$\int e^{-x} (\sin x - \cos x) \, dx = -e^{-x} \sin x$$
Substituting this back into the solution:
$$v e^{-x} = -e^{-x} \sin x + C$$
Multiply through by $e^x$:
$$v = -\sin x + C e^x = C e^x - \sin x$$

**Step 6: Resubstitute $v = 1/y$**
$$\frac{1}{y} = C e^x - \sin x \implies y(x) = \frac{1}{C e^x - \sin x}$$
where $C$ is an arbitrary constant of integration.
"""
            },
            {
                "qid": "vcdet-q2",
                "marks": 3,
                "type": "Short Answer",
                "title": 'Second Order Linear ODE with Repeated Roots and Dual Forcing Functions',
                "yt_query": 'second order linear ode repeated roots complementary function particular integral',
                "img_path": "",
                "img_caption": "",
                "answer": r"""
We are required to find the complete general solution of the second-order non-homogeneous ordinary differential equation with constant coefficients:
$$(D^2 - 4D + 4)y = 8e^{2x} + \sin 2x$$
where $D = \frac{d}{dx}$ is the differential operator.

**Step 1: Determine the Complementary Function ($y_c$)**
The corresponding homogeneous equation is $(D^2 - 4D + 4)y = 0$.
The auxiliary equation is:
$$m^2 - 4m + 4 = 0 \implies (m - 2)^2 = 0 \implies m = 2, \quad 2 \quad (\text{real repeated root})$$
For a repeated root $m = 2$ of multiplicity 2, the complementary function is:
$$y_c = (C_1 + C_2 x) e^{2x}$$
where $C_1$ and $C_2$ are arbitrary constants.

**Step 2: Determine the Particular Integral ($y_p$)**
By the superposition principle for linear systems, the particular integral is:
$$y_p = \frac{1}{(D - 2)^2} [8e^{2x} + \sin 2x] = y_{p1} + y_{p2}$$

1. **Evaluation of $y_{p1} = \frac{1}{(D - 2)^2} [8e^{2x}]$:**
   Since $D = 2$ causes the denominator polynomial to vanish ($f(2) = 0$), we have a case of resonance. Because the root $m = 2$ has multiplicity $k = 2$:
   $$y_{p1} = 8 \cdot \frac{x^2}{2!} e^{2x} = 8 \cdot \frac{x^2}{2} e^{2x} = 4x^2 e^{2x}$$

2. **Evaluation of $y_{p2} = \frac{1}{D^2 - 4D + 4} [\sin 2x]$:**
   For a sinusoidal forcing function $\sin(ax)$ with $a = 2$, replace $D^2$ with $-a^2 = -(2^2) = -4$:
   $$y_{p2} = \frac{1}{-4 - 4D + 4} \sin 2x = \frac{1}{-4D} \sin 2x$$
   Since $\frac{1}{D}$ denotes integration with respect to $x$:
   $$y_{p2} = -\frac{1}{4} \int \sin 2x \, dx = -\frac{1}{4} \left( -\frac{\cos 2x}{2} \right) = \frac{1}{8} \cos 2x$$

**Step 3: Form the Complete General Solution**
$$y(x) = y_c + y_{p1} + y_{p2} = (C_1 + C_2 x) e^{2x} + 4x^2 e^{2x} + \frac{1}{8} \cos 2x$$
"""
            },
            {
                "qid": "vcdet-q3",
                "marks": 7,
                "type": "Analytical Problem",
                "title": 'Method of Variation of Parameters for Non-Elementary Forcing Functions',
                "yt_query": 'variation of parameters method second order differential equations wronskian sec tan',
                "img_path": "",
                "img_caption": "",
                "answer": r"""
We are required to solve the second-order non-homogeneous linear differential equation:
$$\frac{d^2y}{dx^2} + y = \sec x \tan x$$
using the **method of variation of parameters**. The standard undetermined coefficients method fails here because $\sec x \tan x$ possesses infinitely many linearly independent derivatives.

**Step 1: Find the Complementary Function ($y_c$)**
The homogeneous equation is:
$$\frac{d^2y}{dx^2} + y = 0$$
Auxiliary equation:
$$m^2 + 1 = 0 \implies m = \pm i$$
The complementary function is:
$$y_c = C_1 \cos x + C_2 \sin x$$
Identify the two linearly independent basis solutions:
$$y_1(x) = \cos x, \quad y_2(x) = \sin x$$

**Step 2: Compute the Wronskian $W(y_1, y_2)$**
The Wronskian determinant is:
$$W(x) = \begin{vmatrix} y_1 & y_2 \\ y_1' & y_2' \end{vmatrix} = \begin{vmatrix} \cos x & \sin x \\ -\sin x & \cos x \end{vmatrix} = (\cos x)(\cos x) - (\sin x)(-\sin x) = \cos^2 x + \sin^2 x = 1$$
Since $W(x) = 1 \neq 0$, the solutions are linearly independent for all $x \in \mathbb{R}$.

**Step 3: Variation of Parameters Formula for Particular Integral**
The particular integral is assumed to have the form:
$$y_p(x) = u(x) y_1(x) + v(x) y_2(x)$$
where:
$$u(x) = -\int \frac{y_2(x) R(x)}{W(x)} \, dx, \quad v(x) = \int \frac{y_1(x) R(x)}{W(x)} \, dx$$
with the forcing term $R(x) = \sec x \tan x$.

**Step 4: Compute $u(x)$**
$$u(x) = -\int \frac{(\sin x)(\sec x \tan x)}{1} \, dx = -\int \sin x \cdot \frac{1}{\cos x} \cdot \frac{\sin x}{\cos x} \, dx = -\int \frac{\sin^2 x}{\cos^2 x} \, dx = -\int \tan^2 x \, dx$$
Using the trigonometric identity $\tan^2 x = \sec^2 x - 1$:
$$u(x) = -\int (\sec^2 x - 1) \, dx = -(\tan x - x) = x - \tan x$$

**Step 5: Compute $v(x)$**
$$v(x) = \int \frac{(\cos x)(\sec x \tan x)}{1} \, dx = \int \cos x \cdot \frac{1}{\cos x} \cdot \tan x \, dx = \int \tan x \, dx = \ln|\sec x|$$

**Step 6: Assemble the Particular Integral $y_p(x)$**
$$y_p(x) = u(x) y_1(x) + v(x) y_2(x) = (x - \tan x)\cos x + (\ln|\sec x|)\sin x$$
$$y_p(x) = x \cos x - \tan x \cos x + \sin x \ln|\sec x| = x \cos x - \sin x + \sin x \ln|\sec x|$$
Notice that the term $-\sin x$ is a scalar multiple of the basis solution $y_2(x)$ and can be absorbed into the arbitrary constant $C_2$ in the complementary function.

**Step 7: Complete General Solution**
$$y(x) = y_c + y_p = C_1 \cos x + C_2 \sin x + x \cos x + \sin x \ln|\sec x|$$
where $C_1$ and $C_2$ are arbitrary constants.
"""
            },
            {
                "qid": "vcdet-q4",
                "marks": 7,
                "type": "Analytical Problem",
                "title": 'Cauchy-Euler Equidimensional Differential Equation Transformation and Solution',
                "yt_query": 'cauchy euler differential equation substitution x=e^z engineering mathematics',
                "img_path": "",
                "img_caption": "",
                "answer": r"""
We are required to solve the second-order Cauchy-Euler (equidimensional) differential equation:
$$x^2 \frac{d^2y}{dx^2} - 3x \frac{dy}{dx} + 4y = 2x^2 \quad (x > 0)$$
using the logarithmic transformation $x = e^z$.

**Step 1: Coordinate Transformation to Constant Coefficients**
Let:
$$x = e^z \iff z = \ln x$$
Let $D_z = \frac{d}{dz}$ denote the derivative operator with respect to the new independent variable $z$.
By the chain rule:
$$\frac{dy}{dx} = \frac{dy}{dz} \frac{dz}{dx} = \frac{1}{x} \frac{dy}{dz} \implies x \frac{dy}{dx} = D_z y$$
For the second derivative:
$$\frac{d^2y}{dx^2} = \frac{d}{dx}\left( \frac{1}{x} \frac{dy}{dz} \right) = -\frac{1}{x^2} \frac{dy}{dz} + \frac{1}{x} \frac{d}{dz}\left(\frac{dy}{dz}\right)\frac{dz}{dx} = \frac{1}{x^2}\left( \frac{d^2y}{dz^2} - \frac{dy}{dz} \right)$$
$$x^2 \frac{d^2y}{dx^2} = D_z(D_z - 1)y$$

Also express the right-hand side excitation in terms of $z$:
$$2x^2 = 2(e^z)^2 = 2e^{2z}$$

**Step 2: Formulate the Transformed ODE in $z$**
Substitute these operator representations into the differential equation:
$$[D_z(D_z - 1) - 3D_z + 4]y = 2e^{2z}$$
$$(D_z^2 - D_z - 3D_z + 4)y = 2e^{2z} \implies (D_z^2 - 4D_z + 4)y = 2e^{2z}$$
This is now a linear ODE with constant coefficients.

**Step 3: Complementary Function $y_c(z)$**
Auxiliary equation:
$$m^2 - 4m + 4 = 0 \implies (m - 2)^2 = 0 \implies m = 2, \quad 2$$
The complementary function is:
$$y_c(z) = (C_1 + C_2 z) e^{2z}$$

**Step 4: Particular Integral $y_p(z)$**
$$y_p(z) = \frac{1}{(D_z - 2)^2} [2e^{2z}]$$
Since $D_z = 2$ is a root of multiplicity $k = 2$ of the denominator operator:
$$y_p(z) = 2 \cdot \frac{z^2}{2!} e^{2z} = 2 \cdot \frac{z^2}{2} e^{2z} = z^2 e^{2z}$$

**Step 5: General Solution in $z$**
$$y(z) = y_c(z) + y_p(z) = (C_1 + C_2 z) e^{2z} + z^2 e^{2z} = (C_1 + C_2 z + z^2) e^{2z}$$

**Step 6: Transform back to the original variable $x$**
Substitute $z = \ln x$ and $e^{2z} = (e^z)^2 = x^2$:
$$y(x) = [C_1 + C_2 \ln x + (\ln x)^2] x^2$$
where $C_1$ and $C_2$ are arbitrary constants.
"""
            },
            {
                "qid": "vcdet-q5",
                "marks": 7,
                "type": "Analytical Problem",
                "title": 'Exponential Shift Operator Method for Composite Product Forcing Functions',
                "yt_query": 'exponential shift theorem particular integral D operator x e^x sin x',
                "img_path": "",
                "img_caption": "",
                "answer": r"""
We are required to solve the non-homogeneous higher order linear differential equation:
$$(D^2 - 2D + 1)y = x e^x \sin x$$
where $D = \frac{d}{dx}$.

**Step 1: Determine the Complementary Function ($y_c$)**
Auxiliary equation:
$$m^2 - 2m + 1 = 0 \implies (m - 1)^2 = 0 \implies m = 1, \quad 1 \quad (\text{repeated root})$$
The complementary function is:
$$y_c = (C_1 + C_2 x) e^x$$
where $C_1$ and $C_2$ are arbitrary constants.

**Step 2: Determine the Particular Integral ($y_p$)**
$$y_p = \frac{1}{(D - 1)^2} [x e^x \sin x]$$

**Step 3: Apply the Exponential Shift Theorem**
The fundamental operator shift identity states:
$$\frac{1}{f(D)} [e^{ax} V(x)] = e^{ax} \frac{1}{f(D + a)} [V(x)]$$
Here $a = 1$ and $V(x) = x \sin x$. Replacing $D$ by $D + 1$:
$$y_p = e^x \frac{1}{((D + 1) - 1)^2} [x \sin x] = e^x \frac{1}{D^2} [x \sin x]$$
The differential operator $\frac{1}{D^2}$ denotes two successive indefinite integrations with respect to $x$.

**Step 4: Perform Successive Integrations**
- **First Integration ($\frac{1}{D}[x \sin x]$):**
  Integrate by parts: $\int u v' \, dx = u v - \int u' v \, dx$.
  Let $u = x \implies u' = 1$. Let $v' = \sin x \implies v = -\cos x$.
  $$\frac{1}{D}[x \sin x] = \int x \sin x \, dx = x(-\cos x) - \int 1 \cdot (-\cos x) \, dx = -x \cos x + \int \cos x \, dx$$
  $$\frac{1}{D}[x \sin x] = -x \cos x + \sin x$$

- **Second Integration ($\frac{1}{D^2}[x \sin x] = \frac{1}{D}[-x \cos x + \sin x]$):**
  $$\frac{1}{D^2}[x \sin x] = \int (-x \cos x + \sin x) \, dx = -\int x \cos x \, dx + \int \sin x \, dx$$
  Integrate $\int x \cos x \, dx$ by parts:
  $$\int x \cos x \, dx = x \sin x - \int 1 \cdot \sin x \, dx = x \sin x - (-\cos x) = x \sin x + \cos x$$
  Therefore:
  $$\frac{1}{D^2}[x \sin x] = -(x \sin x + \cos x) + (-\cos x) = -x \sin x - \cos x - \cos x = -x \sin x - 2\cos x$$

**Step 5: Assemble the Particular Integral and Complete General Solution**
$$y_p = e^x (-x \sin x - 2\cos x) = -e^x (x \sin x + 2\cos x)$$
Combining the complementary function and particular integral:
$$y(x) = y_c + y_p = (C_1 + C_2 x)e^x - e^x (x \sin x + 2\cos x)$$
"""
            },
        ]
    },
    {
        "module_id": "vcdet-m2",
        "module_num": "Module 2",
        "module_title": "Vector Differentiation, Gradient, Divergence, Curl & Potentials",
        "questions": [
            {
                "qid": "vcdet-q6",
                "marks": 3,
                "type": "Short Answer",
                "title": 'Directional Derivative of Scalar Potential Field along Specified Vector',
                "yt_query": 'directional derivative of scalar function gradient vector engineering mathematics',
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
                "title": 'Unit Normal Vector and Tangent Plane to Implicit Level Surface',
                "yt_query": 'unit normal vector to surface tangent plane gradient engineering mathematics',
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
                "title": 'Irrotational Vector Field, Conservative Potential, and Work Done Line Integral',
                "yt_query": 'conservative vector field curl scalar potential work done path independent',
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
                "title": 'Determination of Constants for Irrotational Field and Solenoidal Field Verification',
                "yt_query": 'find constants a b c irrotational vector field solenoidal divergence curl zero',
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
                "title": 'Fundamental Radial Vector Identities and Harmonicity of the Inverse Distance Potential',
                "yt_query": 'gradient of r^n divergence r^n r laplacian r^n harmonic 1/r engineering mathematics',
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
            },
        ]
    },
    {
        "module_id": "vcdet-m3",
        "module_num": "Module 3",
        "module_title": "Vector Integration, Green's, Gauss Divergence & Stokes' Theorems",
        "questions": [
            {
                "qid": "vcdet-q11",
                "marks": 3,
                "type": "Short Answer",
                "title": "Green's Theorem Evaluation of Closed Line Integral over Parabolic Boundaries",
                "yt_query": 'greens theorem evaluate line integral parabolas y=x^2 y^2=x engineering mathematics',
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
                "title": 'Gauss Divergence Theorem Statement and Physical Interpretation in Engineering',
                "yt_query": 'gauss divergence theorem statement physical significance electrodynamics fluid flow',
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
                "yt_query": 'verify greens theorem line integral surface integral y=x y=x^2 engineering mathematics',
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
                "title": 'Rigorous Verification of Gauss Divergence Theorem over a Closed Unit Cube',
                "yt_query": 'verify gauss divergence theorem unit cube six faces flux engineering mathematics',
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
                "yt_query": 'verify stokes theorem hemisphere line integral curl engineering mathematics',
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
            },
        ]
    },
    {
        "module_id": "vcdet-m4",
        "module_num": "Module 4",
        "module_title": "Fourier Series, Harmonic Analysis & Fourier Integral Transforms",
        "questions": [
            {
                "qid": "vcdet-q16",
                "marks": 3,
                "type": "Short Answer",
                "title": "Dirichlet's Conditions for Fourier Series and Value at Jump Discontinuities",
                "yt_query": 'dirichlets conditions fourier series convergence point of discontinuity',
                "img_path": "",
                "img_caption": "",
                "answer": r"""
**Dirichlet's Conditions for the Existence of a Fourier Series:**
A periodic function $f(x)$ of period $2L$ defined in an interval $(c, c + 2L)$ can be represented by a convergent Fourier series if it satisfies the following three classical conditions:
1. **Single-Valued and Bounded:** $f(x)$ is single-valued and bounded everywhere in the interval (there exists a real positive constant $M$ such that $|f(x)| \le M$).
2. **Piecewise Continuous:** $f(x)$ has at most a finite number of finite jump discontinuities in any single period.
3. **Finite Extrema:** $f(x)$ has at most a finite number of local maxima and local minima in any single period.

Functions satisfying these criteria are called piecewise smooth (Dirichlet) functions, which encompass virtually all physically realizable waveforms encountered in electrical and electronic engineering.

**Convergence of Fourier Series at Discontinuities:**
Let $S(x)$ denote the sum of the Fourier series of $f(x)$ at any point $x$:
1. At any point of **continuity** $x_0$, the Fourier series converges exactly to the actual function value:
   $$S(x_0) = f(x_0)$$
2. At a point of **finite jump discontinuity** $x = a$, the Fourier series converges strictly to the arithmetic mean (midpoint) of the right-hand and left-hand limits of $f(x)$ as $x$ approaches $a$:
   $$S(a) = \frac{f(a^+) + f(a^-)}{2} = \frac{1}{2} \left[ \lim_{h \to 0^+} f(a + h) + \lim_{h \to 0^+} f(a - h) \right]$$
3. At the **endpoints** of the fundamental interval $[c, c + 2L]$, by periodicity, the Fourier series converges to:
   $$S(c) = S(c + 2L) = \frac{f(c^+) + f((c + 2L)^-)}{2}$$
"""
            },
            {
                "qid": "vcdet-q17",
                "marks": 3,
                "type": "Short Answer",
                "title": 'Half-Range Fourier Sine Series for Constant Function',
                "yt_query": 'half range fourier sine series constant function engineering mathematics',
                "img_path": "",
                "img_caption": "",
                "answer": r"""
We are required to determine the half-range Fourier sine series expansion for the constant function $f(x) = k$ over the interval $0 < x < \pi$.

**Step 1: Formula for Half-Range Sine Series**
The half-range sine series of $f(x)$ in $(0, \pi)$ is generated by extending $f(x)$ as an odd periodic function of period $2\pi$ into $(-\pi, \pi)$. Because the extension is odd, all cosine coefficients $a_0 = 0$ and $a_n = 0$.
The series is given by:
$$f(x) = \sum_{n=1}^\infty b_n \sin nx$$
where the Fourier sine coefficients $b_n$ are given by:
$$b_n = \frac{2}{\pi} \int_0^\pi f(x) \sin nx \, dx$$

**Step 2: Compute the Coefficient $b_n$**
Substitute $f(x) = k$:
$$b_n = \frac{2}{\pi} \int_0^\pi k \sin nx \, dx = \frac{2k}{\pi} \int_0^\pi \sin nx \, dx$$
Evaluate the integral:
$$b_n = \frac{2k}{\pi} \left[ \frac{-\cos nx}{n} \right]_0^\pi = \frac{2k}{n\pi} [-\cos n\pi - (-\cos 0)] = \frac{2k}{n\pi} [1 - \cos n\pi]$$
Recall that $\cos n\pi = (-1)^n$ for integer $n$:
$$b_n = \frac{2k}{n\pi} [1 - (-1)^n]$$

**Step 3: Analyze Even and Odd Harmonics**
- For **even** values of $n$ ($n = 2, 4, 6, \dots$):
  $$(-1)^n = 1 \implies 1 - (-1)^n = 1 - 1 = 0 \implies b_n = 0$$
- For **odd** values of $n$ ($n = 1, 3, 5, \dots$):
  $$(-1)^n = -1 \implies 1 - (-1)^n = 1 - (-1) = 2 \implies b_n = \frac{2k}{n\pi}(2) = \frac{4k}{n\pi}$$

Let $n = 2m - 1$ where $m = 1, 2, 3, \dots$:
$$b_{2m-1} = \frac{4k}{(2m - 1)\pi}$$

**Step 4: Formulate the Complete Series**
$$f(x) = \frac{4k}{\pi} \sum_{m=1}^\infty \frac{\sin(2m - 1)x}{2m - 1} = \frac{4k}{\pi} \left( \sin x + \frac{\sin 3x}{3} + \frac{\sin 5x}{5} + \frac{\sin 7x}{7} + \dots \right)$$
"""
            },
            {
                "qid": "vcdet-q18",
                "marks": 7,
                "type": "Analytical Problem",
                "title": 'Fourier Series Expansion of Parabola and Resolution of Basel Inverse-Square Series',
                "yt_query": 'fourier series x^2 even function deduce sum 1/n^2 pi^2/6 basel problem',
                "img_path": "",
                "img_caption": "",
                "answer": r"""
We are required to determine the Fourier series expansion of the quadratic function $f(x) = x^2$ in the symmetric interval $-\pi \le x \le \pi$, and deduce the following mathematical series:
(i) $\sum_{n=1}^\infty \frac{(-1)^{n-1}}{n^2} = 1 - \frac{1}{4} + \frac{1}{9} - \frac{1}{16} + \dots = \frac{\pi^2}{12}$
(ii) $\sum_{n=1}^\infty \frac{1}{n^2} = 1 + \frac{1}{4} + \frac{1}{9} + \frac{1}{16} + \dots = \frac{\pi^2}{6}$

**Step 1: Symmetry Analysis**
Check if the function is even or odd:
$$f(-x) = (-x)^2 = x^2 = f(x)$$
Because $f(x)$ is an **even function** over the symmetric interval $[-\pi, \pi]$:
- All sine coefficients vanish identically: $b_n = 0$ for all $n \ge 1$.
- The Fourier series consists strictly of cosine terms:
$$f(x) = \frac{a_0}{2} + \sum_{n=1}^\infty a_n \cos nx$$

**Step 2: Determine $a_0$**
$$a_0 = \frac{2}{\pi} \int_0^\pi f(x) \, dx = \frac{2}{\pi} \int_0^\pi x^2 \, dx = \frac{2}{\pi} \left[ \frac{x^3}{3} \right]_0^\pi = \frac{2}{\pi} \left( \frac{\pi^3}{3} \right) = \frac{2\pi^2}{3}$$
The constant term in the Fourier expansion is:
$$\frac{a_0}{2} = \frac{\pi^2}{3}$$

**Step 3: Determine $a_n$**
$$a_n = \frac{2}{\pi} \int_0^\pi x^2 \cos nx \, dx$$
Integrate by parts using Bernoulli's generalized formula:
$$\int u v \, dx = u v_1 - u' v_2 + u'' v_3 - \dots$$
Let $u = x^2 \implies u' = 2x, u'' = 2, u''' = 0$.
Let $v = \cos nx \implies v_1 = \frac{\sin nx}{n}, v_2 = -\frac{\cos nx}{n^2}, v_3 = -\frac{\sin nx}{n^3}$.

$$a_n = \frac{2}{\pi} \left[ x^2 \left(\frac{\sin nx}{n}\right) - 2x\left(-\frac{\cos nx}{n^2}\right) + 2\left(-\frac{\sin nx}{n^3}\right) \right]_0^\pi$$
$$a_n = \frac{2}{\pi} \left[ \frac{x^2 \sin nx}{n} + \frac{2x \cos nx}{n^2} - \frac{2\sin nx}{n^3} \right]_0^\pi$$

Evaluate at the limits $x = \pi$ and $x = 0$:
Since $\sin n\pi = 0$ and $\sin 0 = 0$:
$$a_n = \frac{2}{\pi} \left[ 0 + \frac{2\pi \cos n\pi}{n^2} - 0 - (0 + 0 - 0) \right] = \frac{2}{\pi} \left( \frac{2\pi (-1)^n}{n^2} \right) = \frac{4(-1)^n}{n^2}$$

**Step 4: Assemble the Fourier Series Expansion**
$$x^2 = \frac{\pi^2}{3} + \sum_{n=1}^\infty \frac{4(-1)^n}{n^2} \cos nx = \frac{\pi^2}{3} - 4 \sum_{n=1}^\infty \frac{(-1)^{n-1}}{n^2} \cos nx$$
$$x^2 = \frac{\pi^2}{3} - 4 \left( \frac{\cos x}{1^2} - \frac{\cos 2x}{2^2} + \frac{\cos 3x}{3^2} - \frac{\cos 4x}{4^2} + \dots \right)$$

---
### Step 5: Deduce Series (i) and (ii)

**Deduction of (i): Substitute $x = 0$:**
At $x = 0$, $f(x)$ is continuous and $\cos(0) = 1$:
$$0^2 = \frac{\pi^2}{3} - 4 \left( \frac{1}{1^2} - \frac{1}{2^2} + \frac{1}{3^2} - \frac{1}{4^2} + \dots \right)$$
$$4 \left( 1 - \frac{1}{4} + \frac{1}{9} - \frac{1}{16} + \dots \right) = \frac{\pi^2}{3}$$
Divide both sides by 4:
$$1 - \frac{1}{4} + \frac{1}{9} - \frac{1}{16} + \dots = \sum_{n=1}^\infty \frac{(-1)^{n-1}}{n^2} = \frac{\pi^2}{12}$$

**Deduction of (ii): Substitute $x = \pi$:**
At $x = \pi$, $\cos n\pi = (-1)^n$:
$$\pi^2 = \frac{\pi^2}{3} + 4 \sum_{n=1}^\infty \frac{(-1)^n (-1)^n}{n^2} = \frac{\pi^2}{3} + 4 \sum_{n=1}^\infty \frac{(-1)^{2n}}{n^2}$$
Since $(-1)^{2n} = ((-1)^2)^n = 1^n = 1$:
$$\pi^2 = \frac{\pi^2}{3} + 4 \sum_{n=1}^\infty \frac{1}{n^2}$$
Subtract $\frac{\pi^2}{3}$ from both sides:
$$\pi^2 - \frac{\pi^2}{3} = 4 \sum_{n=1}^\infty \frac{1}{n^2} \implies \frac{2\pi^2}{3} = 4 \sum_{n=1}^\infty \frac{1}{n^2}$$
Divide both sides by 4:
$$\sum_{n=1}^\infty \frac{1}{n^2} = 1 + \frac{1}{4} + \frac{1}{9} + \frac{1}{16} + \dots = \frac{2\pi^2}{12} = \frac{\pi^2}{6}$$
"""
            },
            {
                "qid": "vcdet-q19",
                "marks": 7,
                "type": "Analytical Problem",
                "title": 'Fourier Harmonic Spectrum of Square Wave and Deduction of Gregory-Leibniz Formula',
                "yt_query": 'fourier series square wave odd function deduce pi/4 leibniz series',
                "img_path": "",
                "img_caption": "",
                "answer": r"""
We are required to find the Fourier series of the periodic square wave:
$$f(x) = \begin{cases} -k, & -\pi < x < 0 \\ k, & 0 < x < \pi \end{cases}$$
with period $2\pi$ ($f(x + 2\pi) = f(x)$), and hence deduce the Gregory-Leibniz series for $\pi$:
$$1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \dots = \frac{\pi}{4}$$

**Step 1: Test for Symmetry**
Observe that:
$$f(-x) = \begin{cases} -k, & 0 < -x < \pi \iff -\pi < x < 0 \\ k, & -\pi < -x < 0 \iff 0 < x < \pi \end{cases} = -f(x)$$
Because $f(-x) = -f(x)$ for all $x \in (-\pi, \pi) \setminus \{0\}$, $f(x)$ is a strictly **odd function**.

By the properties of odd functions over symmetric intervals:
$$a_0 = 0$$
$$a_n = \frac{1}{\pi} \int_{-\pi}^\pi f(x) \cos nx \, dx = 0 \quad (\text{since } f(x)\cos nx \text{ is odd})$$
The Fourier series contains only sine terms:
$$f(x) = \sum_{n=1}^\infty b_n \sin nx$$

**Step 2: Compute Fourier Sine Coefficient $b_n$**
Using the property of odd functions ($f(x)\sin nx$ is even):
$$b_n = \frac{2}{\pi} \int_0^\pi f(x) \sin nx \, dx = \frac{2}{\pi} \int_0^\pi k \sin nx \, dx = \frac{2k}{\pi} \left[ \frac{-\cos nx}{n} \right]_0^\pi$$
$$b_n = \frac{2k}{n\pi} [1 - \cos n\pi] = \frac{2k}{n\pi} [1 - (-1)^n]$$

- For **even** $n$ ($n = 2, 4, 6, \dots$):
  $$b_n = \frac{2k}{n\pi}[1 - 1] = 0$$
- For **odd** $n$ ($n = 1, 3, 5, \dots$):
  $$b_n = \frac{2k}{n\pi}[1 - (-1)] = \frac{4k}{n\pi}$$

**Step 3: Construct the Fourier Series Expansion**
$$f(x) = \frac{4k}{\pi} \sum_{m=1}^\infty \frac{\sin(2m - 1)x}{2m - 1} = \frac{4k}{\pi} \left( \sin x + \frac{\sin 3x}{3} + \frac{\sin 5x}{5} + \frac{\sin 7x}{7} + \dots \right)$$

**Step 4: Deduction of the Leibniz Series at $x = \frac{\pi}{2}$**
Notice that at $x = \frac{\pi}{2}$, $f(x)$ is continuous, and $f(\pi/2) = k$.
Evaluate the harmonic sine terms at $x = \frac{\pi}{2}$:
$$\sin\left(\frac{\pi}{2}\right) = 1$$
$$\sin\left(\frac{3\pi}{2}\right) = -1$$
$$\sin\left(\frac{5\pi}{2}\right) = 1$$
$$\sin\left(\frac{7\pi}{2}\right) = -1$$
In general, $\sin\left(\frac{(2m - 1)\pi}{2}\right) = (-1)^{m-1}$.

Substitute $x = \frac{\pi}{2}$ into the Fourier series:
$$k = \frac{4k}{\pi} \left( 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \dots \right)$$
Divide both sides by $k$ (since $k \neq 0$):
$$1 = \frac{4}{\pi} \left( 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \dots \right)$$
Multiply through by $\frac{\pi}{4}$:
$$1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \dots = \frac{\pi}{4}$$
This proves the celebrated Gregory-Leibniz formula.
"""
            },
            {
                "qid": "vcdet-q20",
                "marks": 7,
                "type": "Analytical Problem",
                "title": 'Fourier Cosine and Sine Integral Transforms and Evaluation of Improper Integrals',
                "yt_query": 'fourier cosine sine transform e^-ax evaluate improper integral inverse transform',
                "img_path": "",
                "img_caption": "",
                "answer": r"""
We are required to determine the Fourier cosine and Fourier sine transforms of the decaying exponential function $f(x) = e^{-ax}$ ($a > 0$), and hence evaluate the improper integral:
$$\int_0^\infty \frac{\cos(\omega x)}{a^2 + \omega^2} \, d\omega$$

---
### Part 1: Fourier Cosine Transform $\mathcal{F}_c\{e^{-ax}\}$

By definition:
$$\mathcal{F}_c\{f(x)\} = F_c(\omega) = \int_0^\infty f(x) \cos(\omega x) \, dx = \int_0^\infty e^{-ax} \cos(\omega x) \, dx$$
Recall the standard exponential-trigonometric integration formula:
$$\int e^{Ax} \cos Bx \, dx = \frac{e^{Ax}}{A^2 + B^2} (A \cos Bx + B \sin Bx)$$
Here $A = -a$ and $B = \omega$:
$$F_c(\omega) = \left[ \frac{e^{-ax}}{a^2 + \omega^2} (-a \cos \omega x + \omega \sin \omega x) \right]_0^\infty$$

As $x \to \infty$, since $a > 0$, $e^{-ax} \to 0$ while the trigonometric terms remain bounded. Hence the upper limit vanishes ($0$).
At $x = 0$, $e^0 = 1, \cos 0 = 1, \sin 0 = 0$:
$$F_c(\omega) = 0 - \frac{1}{a^2 + \omega^2} (-a(1) + 0) = \frac{a}{a^2 + \omega^2}$$

---
### Part 2: Fourier Sine Transform $\mathcal{F}_s\{e^{-ax}\}$

By definition:
$$\mathcal{F}_s\{f(x)\} = F_s(\omega) = \int_0^\infty f(x) \sin(\omega x) \, dx = \int_0^\infty e^{-ax} \sin(\omega x) \, dx$$
Recall the formula:
$$\int e^{Ax} \sin Bx \, dx = \frac{e^{Ax}}{A^2 + B^2} (A \sin Bx - B \cos Bx)$$
With $A = -a$ and $B = \omega$:
$$F_s(\omega) = \left[ \frac{e^{-ax}}{a^2 + \omega^2} (-a \sin \omega x - \omega \cos \omega x) \right]_0^\infty$$
At $x \to \infty$, $e^{-ax} \to 0$.
At $x = 0$, $e^0 = 1, \sin 0 = 0, \cos 0 = 1$:
$$F_s(\omega) = 0 - \frac{1}{a^2 + \omega^2} (0 - \omega(1)) = \frac{\omega}{a^2 + \omega^2}$$

---
### Part 3: Evaluation of the Improper Integral via Inverse Fourier Cosine Transform

By the Fourier Inverse Cosine Transform formula:
$$f(x) = \frac{2}{\pi} \int_0^\infty F_c(\omega) \cos(\omega x) \, d\omega$$
Substitute $f(x) = e^{-ax}$ and $F_c(\omega) = \frac{a}{a^2 + \omega^2}$:
$$e^{-ax} = \frac{2}{\pi} \int_0^\infty \frac{a}{a^2 + \omega^2} \cos(\omega x) \, d\omega = \frac{2a}{\pi} \int_0^\infty \frac{\cos(\omega x)}{a^2 + \omega^2} \, d\omega$$

Multiply both sides by $\frac{\pi}{2a}$ (for $a > 0$):
$$\int_0^\infty \frac{\cos(\omega x)}{a^2 + \omega^2} \, d\omega = \frac{\pi}{2a} e^{-ax} \quad (x > 0, a > 0)$$
This formally evaluates Laplace's famous contour integral using Fourier transforms.
"""
            },
        ]
    },
    {
        "module_id": "vcdet-m5",
        "module_num": "Module 5",
        "module_title": "Laplace Transforms, Convolution Theorem & Differential Systems",
        "questions": [
            {
                "qid": "vcdet-q21",
                "marks": 3,
                "type": "Short Answer",
                "title": 'Laplace Transform of Modulated Sinusoid with Multiplied Polynomial Power',
                "yt_query": 'laplace transform t squared e^-3t sin 2t first shifting multiplication by t',
                "img_path": "",
                "img_caption": "",
                "answer": r"""
We are required to evaluate the Laplace transform of the composite time function:
$$f(t) = t^2 e^{-3t} \sin 2t$$

**Step 1: Elementary Transform**
The Laplace transform of $\sin 2t$ is:
$$\mathcal{L}\{\sin 2t\} = \frac{2}{s^2 + 2^2} = \frac{2}{s^2 + 4}$$

**Step 2: Apply the First Shifting (Frequency Translation) Property**
The First Shifting Property states:
$$\mathcal{L}\{e^{at} g(t)\} = G(s - a), \quad \text{where } G(s) = \mathcal{L}\{g(t)\}$$
Here $a = -3$, so we replace $s$ by $s - (-3) = s + 3$:
$$\mathcal{L}\{e^{-3t} \sin 2t\} = \frac{2}{(s + 3)^2 + 4} = \frac{2}{s^2 + 6s + 9 + 4} = \frac{2}{s^2 + 6s + 13}$$
Let $H(s) = \frac{2}{s^2 + 6s + 13} = 2(s^2 + 6s + 13)^{-1}$.

**Step 3: Apply the Multiplication by $t^n$ Property**
The multiplication by power of $t$ property states:
$$\mathcal{L}\{t^n g(t)\} = (-1)^n \frac{d^n}{ds^n} G(s)$$
For $n = 2$:
$$\mathcal{L}\{t^2 [e^{-3t} \sin 2t]\} = (-1)^2 \frac{d^2}{ds^2}[H(s)] = \frac{d^2}{ds^2}\left[ 2(s^2 + 6s + 13)^{-1} \right]$$

Compute the first derivative:
$$\frac{d}{ds} H(s) = 2 \cdot (-1)(s^2 + 6s + 13)^{-2} (2s + 6) = -\frac{2(2s + 6)}{(s^2 + 6s + 13)^2} = -\frac{4(s + 3)}{(s^2 + 6s + 13)^2}$$

Compute the second derivative using the quotient rule:
$$\frac{d^2}{ds^2} H(s) = -4 \frac{d}{ds}\left[ \frac{s + 3}{(s^2 + 6s + 13)^2} \right]$$
$$= -4 \left[ \frac{1 \cdot (s^2 + 6s + 13)^2 - (s + 3) \cdot 2(s^2 + 6s + 13)(2s + 6)}{(s^2 + 6s + 13)^4} \right]$$
Cancel the common factor $(s^2 + 6s + 13)$ from numerator and denominator:
$$= -4 \left[ \frac{(s^2 + 6s + 13) - 2(s + 3)(2s + 6)}{(s^2 + 6s + 13)^3} \right]$$
Notice that $2s + 6 = 2(s + 3)$, so $2(s + 3)(2s + 6) = 4(s + 3)^2 = 4(s^2 + 6s + 9)$:
$$= -4 \left[ \frac{s^2 + 6s + 13 - (4s^2 + 24s + 36)}{(s^2 + 6s + 13)^3} \right]$$
$$= -4 \left[ \frac{-3s^2 - 18s - 23}{(s^2 + 6s + 13)^3} \right] = \frac{4(3s^2 + 18s + 23)}{(s^2 + 6s + 13)^3} = \frac{12s^2 + 72s + 92}{(s^2 + 6s + 13)^3}$$

Therefore:
$$\mathcal{L}\{t^2 e^{-3t} \sin 2t\} = \frac{12s^2 + 72s + 92}{(s^2 + 6s + 13)^3}$$
"""
            },
            {
                "qid": "vcdet-q22",
                "marks": 3,
                "type": "Short Answer",
                "title": 'Convolution Theorem for Inverse Laplace Transforms and Standard Evaluation',
                "yt_query": 'convolution theorem inverse laplace transform 1/s(s^2+1) engineering mathematics',
                "img_path": "",
                "img_caption": "",
                "answer": r"""
**Statement of the Convolution Theorem:**
Let $F(s)$ and $G(s)$ be the Laplace transforms of functions $f(t)$ and $g(t)$ respectively, so that $\mathcal{L}^{-1}\{F(s)\} = f(t)$ and $\mathcal{L}^{-1}\{G(s)\} = g(t)$. Then the inverse Laplace transform of their algebraic product is given by the convolution integral:
$$\mathcal{L}^{-1}\{F(s)G(s)\} = (f * g)(t) = \int_0^t f(u) g(t - u) \, du$$

**Problem Application:**
We are required to evaluate:
$$\mathcal{L}^{-1}\left\{ \frac{1}{s(s^2 + 1)} \right\}$$
using the convolution theorem.

**Step 1: Decompose into Product of Standard Transforms**
Let:
$$F(s) = \frac{1}{s} \implies f(t) = \mathcal{L}^{-1}\left\{\frac{1}{s}\right\} = 1$$
$$G(s) = \frac{1}{s^2 + 1} \implies g(t) = \mathcal{L}^{-1}\left\{\frac{1}{s^2 + 1}\right\} = \sin t$$

**Step 2: Apply the Convolution Integral**
$$(f * g)(t) = \int_0^t f(u) g(t - u) \, du = \int_0^t (1) \sin(t - u) \, du$$

**Step 3: Evaluate the Integral**
Perform integration with respect to the dummy variable $u$:
$$\int_0^t \sin(t - u) \, du = \left[ \frac{-\cos(t - u)}{-1} \right]_{u=0}^{u=t} = \left[ \cos(t - u) \right]_{u=0}^{u=t}$$
Evaluate at the limits:
$$= \cos(t - t) - \cos(t - 0) = \cos(0) - \cos(t) = 1 - \cos t$$
Therefore:
$$\mathcal{L}^{-1}\left\{ \frac{1}{s(s^2 + 1)} \right\} = 1 - \cos t$$
"""
            },
            {
                "qid": "vcdet-q23",
                "marks": 7,
                "type": "Analytical Problem",
                "title": 'Laplace Transform of Quotient Functions and Deduction of Frullani Improper Integrals',
                "yt_query": 'laplace transform division by t cos at minus cos bt improper integral',
                "img_path": "",
                "img_caption": "",
                "answer": r"""
We are required to evaluate the Laplace transform:
$$\mathcal{L}\left\{ \frac{\cos at - \cos bt}{t} \right\}$$
and hence deduce the value of the improper integral:
$$\int_0^\infty \frac{\cos t - \cos 2t}{t} \, dt$$

---
### Part 1: Laplace Transform via Division by $t$ Property

**Division by $t$ Theorem:**
If $\mathcal{L}\{f(t)\} = F(s)$ and $\lim_{t \to 0} \frac{f(t)}{t}$ exists finitely, then:
$$\mathcal{L}\left\{ \frac{f(t)}{t} \right\} = \int_s^\infty F(u) \, du$$

**Check Existence of Limit at $t \to 0$:**
$$\lim_{t \to 0} \frac{\cos at - \cos bt}{t} = \frac{1 - 1}{0} \quad \left(\frac{0}{0} \text{ form}\right)$$
Apply L'Hopital's rule:
$$\lim_{t \to 0} \frac{-a \sin at + b \sin bt}{1} = 0$$
The limit exists finitely.

**Step 1: Transform of the Numerator**
Let $f(t) = \cos at - \cos bt$.
$$F(s) = \mathcal{L}\{\cos at - \cos bt\} = \frac{s}{s^2 + a^2} - \frac{s}{s^2 + b^2}$$

**Step 2: Integrate $F(u)$ from $s$ to $\infty$**
$$\mathcal{L}\left\{ \frac{\cos at - \cos bt}{t} \right\} = \int_s^\infty \left( \frac{u}{u^2 + a^2} - \frac{u}{u^2 + b^2} \right) du$$
Recall $\int \frac{u}{u^2 + k^2} \, du = \frac{1}{2} \ln(u^2 + k^2)$:
$$= \frac{1}{2} \left[ \ln(u^2 + a^2) - \ln(u^2 + b^2) \right]_s^\infty = \frac{1}{2} \left[ \ln\left( \frac{u^2 + a^2}{u^2 + b^2} \right) \right]_s^\infty$$

Evaluate at the limits:
As $u \to \infty$:
$$\lim_{u \to \infty} \frac{u^2 + a^2}{u^2 + b^2} = \lim_{u \to \infty} \frac{1 + a^2/u^2}{1 + b^2/u^2} = 1 \implies \ln(1) = 0$$
At the lower limit $u = s$:
$$= 0 - \frac{1}{2} \ln\left( \frac{s^2 + a^2}{s^2 + b^2} \right) = \frac{1}{2} \ln\left( \frac{s^2 + b^2}{s^2 + a^2} \right)$$
Therefore:
$$\mathcal{L}\left\{ \frac{\cos at - \cos bt}{t} \right\} = \frac{1}{2} \ln\left( \frac{s^2 + b^2}{s^2 + a^2} \right)$$

---
### Part 2: Deduction of the Improper Integral

By the formal definition of the unilateral Laplace transform:
$$\mathcal{L}\{g(t)\} = \int_0^\infty e^{-st} g(t) \, dt$$
Applying this to $g(t) = \frac{\cos at - \cos bt}{t}$:
$$\int_0^\infty e^{-st} \left( \frac{\cos at - \cos bt}{t} \right) dt = \frac{1}{2} \ln\left( \frac{s^2 + b^2}{s^2 + a^2} \right)$$

Taking the limit as $s \to 0^+$:
$$\int_0^\infty \frac{\cos at - \cos bt}{t} \, dt = \lim_{s \to 0^+} \frac{1}{2} \ln\left( \frac{s^2 + b^2}{s^2 + a^2} \right) = \frac{1}{2} \ln\left( \frac{b^2}{a^2} \right) = \frac{1}{2} \ln\left[\left(\frac{b}{a}\right)^2\right] = \ln\left(\frac{b}{a}\right)$$

For the specific given integral, set $a = 1$ and $b = 2$:
$$\int_0^\infty \frac{\cos t - \cos 2t}{t} \, dt = \ln\left(\frac{2}{1}\right) = \ln 2$$
"""
            },
            {
                "qid": "vcdet-q24",
                "marks": 7,
                "type": "Analytical Problem",
                "title": 'Inverse Laplace Transform of Resonant Quadratic Pole via Convolution',
                "yt_query": 'inverse laplace transform 1/(s^2+a^2)^2 convolution theorem resonance',
                "img_path": "",
                "img_caption": "",
                "answer": r"""
We are required to determine the inverse Laplace transform of:
$$F(s) = \frac{1}{(s^2 + a^2)^2}$$
using the **convolution theorem**.

**Step 1: Factor $F(s)$ into Two Recognizable Transforms**
Write:
$$F(s) = \frac{1}{s^2 + a^2} \cdot \frac{1}{s^2 + a^2} = F_1(s) \cdot F_2(s)$$
where:
$$F_1(s) = F_2(s) = \frac{1}{s^2 + a^2}$$

**Step 2: Find Individual Time-Domain Functions**
Recall the elementary inverse transform:
$$\mathcal{L}^{-1}\left\{ \frac{a}{s^2 + a^2} \right\} = \sin at \implies \mathcal{L}^{-1}\left\{ \frac{1}{s^2 + a^2} \right\} = \frac{1}{a} \sin at$$
Thus:
$$f_1(t) = f_2(t) = \frac{1}{a} \sin at$$

**Step 3: Set up the Convolution Integral**
By the convolution theorem:
$$\mathcal{L}^{-1}\{F_1(s)F_2(s)\} = (f_1 * f_2)(t) = \int_0^t f_1(u) f_2(t - u) \, du$$
$$= \int_0^t \left( \frac{1}{a} \sin au \right) \left( \frac{1}{a} \sin a(t - u) \right) du = \frac{1}{a^2} \int_0^t \sin(au) \sin(at - au) \, du$$

**Step 4: Use Trigonometric Product-to-Sum Identity**
Recall:
$$\sin A \sin B = \frac{1}{2} [\cos(A - B) - \cos(A + B)]$$
Let $A = au$ and $B = at - au$:
$$A - B = au - (at - au) = 2au - at$$
$$A + B = au + (at - au) = at$$
Therefore:
$$\sin(au) \sin(at - au) = \frac{1}{2} [\cos(2au - at) - \cos(at)]$$

**Step 5: Perform Integration**
$$f(t) = \frac{1}{a^2} \int_0^t \frac{1}{2} [\cos(2au - at) - \cos(at)] \, du = \frac{1}{2a^2} \int_0^t [\cos(2au - at) - \cos(at)] \, du$$
Integrate with respect to $u$ (notice that $\cos(at)$ is independent of $u$):
$$f(t) = \frac{1}{2a^2} \left[ \frac{\sin(2au - at)}{2a} - u \cos(at) \right]_{u=0}^{u=t}$$

Evaluate at upper limit $u = t$:
$$\frac{\sin(2at - at)}{2a} - t \cos(at) = \frac{\sin(at)}{2a} - t \cos(at)$$

Evaluate at lower limit $u = 0$:
$$\frac{\sin(0 - at)}{2a} - 0 \cdot \cos(at) = \frac{\sin(-at)}{2a} = -\frac{\sin(at)}{2a}$$

Subtract the lower limit evaluation:
$$\left[ \frac{\sin(at)}{2a} - t \cos(at) \right] - \left[ -\frac{\sin(at)}{2a} \right] = \frac{\sin(at)}{2a} - t \cos(at) + \frac{\sin(at)}{2a} = \frac{2\sin(at)}{2a} - t \cos(at) = \frac{\sin(at)}{a} - t \cos(at)$$

**Step 6: Final Algebraic Simplification**
$$f(t) = \frac{1}{2a^2} \left( \frac{\sin at}{a} - t \cos at \right) = \frac{\sin at - at \cos at}{2a^3}$$
Therefore:
$$\mathcal{L}^{-1}\left\{ \frac{1}{(s^2 + a^2)^2} \right\} = \frac{\sin at - at \cos at}{2a^3}$$
"""
            },
            {
                "qid": "vcdet-q25",
                "marks": 7,
                "type": "Analytical Problem",
                "title": 'Initial Value Problem Solution of Critically Damped Second-Order System via Laplace Transforms',
                "yt_query": 'solve differential equation laplace transform initial value problem second order critical damping',
                "img_path": "",
                "img_caption": "",
                "answer": r"""
We are required to solve the initial value ordinary differential equation problem:
$$\frac{d^2y}{dt^2} + 4\frac{dy}{dt} + 4y = 6 e^{-2t}$$
subject to the initial conditions:
$$y(0) = -2, \quad y'(0) = 8$$
using the Laplace transform method.

**Step 1: Take Laplace Transform on Both Sides**
$$\mathcal{L}\{y''(t)\} + 4\mathcal{L}\{y'(t)\} + 4\mathcal{L}\{y(t)\} = 6\mathcal{L}\{e^{-2t}\}$$
Let $\mathcal{L}\{y(t)\} = Y(s)$.
Recall the derivative transform properties:
$$\mathcal{L}\{y'(t)\} = s Y(s) - y(0) = s Y(s) - (-2) = s Y(s) + 2$$
$$\mathcal{L}\{y''(t)\} = s^2 Y(s) - s y(0) - y'(0) = s^2 Y(s) - s(-2) - 8 = s^2 Y(s) + 2s - 8$$
Right-hand side:
$$6\mathcal{L}\{e^{-2t}\} = \frac{6}{s + 2}$$

**Step 2: Form the Algebraic Equation in $Y(s)$**
$$(s^2 Y(s) + 2s - 8) + 4(s Y(s) + 2) + 4 Y(s) = \frac{6}{s + 2}$$
$$(s^2 + 4s + 4)Y(s) + 2s - 8 + 8 = \frac{6}{s + 2}$$
$$(s + 2)^2 Y(s) + 2s = \frac{6}{s + 2}$$

**Step 3: Solve for $Y(s)$**
$$(s + 2)^2 Y(s) = \frac{6}{s + 2} - 2s$$
Divide through by $(s + 2)^2$:
$$Y(s) = \frac{6}{(s + 2)^3} - \frac{2s}{(s + 2)^2}$$

Express the second term with numerator centered at $(s + 2)$:
$$-2s = -2(s + 2 - 2) = -2(s + 2) + 4$$
Substitute this into the second fraction:
$$-\frac{2s}{(s + 2)^2} = \frac{-2(s + 2) + 4}{(s + 2)^2} = -\frac{2}{s + 2} + \frac{4}{(s + 2)^2}$$

Combining all terms:
$$Y(s) = -\frac{2}{s + 2} + \frac{4}{(s + 2)^2} + \frac{6}{(s + 2)^3}$$

**Step 4: Inverse Laplace Transform using First Shifting Theorem**
Recall that:
$$\mathcal{L}^{-1}\left\{ \frac{1}{(s + 2)^n} \right\} = e^{-2t} \mathcal{L}^{-1}\left\{ \frac{1}{s^n} \right\} = e^{-2t} \frac{t^{n-1}}{(n - 1)!}$$

1. First term:
   $$\mathcal{L}^{-1}\left\{ -\frac{2}{s + 2} \right\} = -2 e^{-2t}$$
2. Second term:
   $$\mathcal{L}^{-1}\left\{ \frac{4}{(s + 2)^2} \right\} = 4 e^{-2t} \frac{t^{2-1}}{1!} = 4t e^{-2t}$$
3. Third term:
   $$\mathcal{L}^{-1}\left\{ \frac{6}{(s + 2)^3} \right\} = 6 e^{-2t} \frac{t^{3-1}}{2!} = 6 e^{-2t} \frac{t^2}{2} = 3t^2 e^{-2t}$$

Summing all components:
$$y(t) = -2e^{-2t} + 4t e^{-2t} + 3t^2 e^{-2t} = (3t^2 + 4t - 2)e^{-2t}$$

**Step 5: Verification of Initial Conditions**
- Check $y(0)$:
  $$y(0) = (0 + 0 - 2)e^0 = -2 \quad (\text{Satisfied})$$
- Check $y'(0)$:
  $$y'(t) = (6t + 4)e^{-2t} - 2(3t^2 + 4t - 2)e^{-2t}$$
  $$y'(0) = (0 + 4)(1) - 2(-2)(1) = 4 + 4 = 8 \quad (\text{Satisfied})$$
"""
            },
            {
                "qid": "vcdet-q26",
                "marks": 7,
                "type": "Analytical Problem",
                "title": 'Solution of Coupled Simultaneous Ordinary Differential Equations via Laplace Transforms',
                "yt_query": 'simultaneous differential equations laplace transform dx/dt + y = sin t',
                "img_path": "",
                "img_caption": "",
                "answer": r"""
We are required to solve the system of simultaneous first-order ordinary differential equations:
$$\frac{dx}{dt} + y = \sin t \quad \text{--- (1)}$$
$$\frac{dy}{dt} + x = \cos t \quad \text{--- (2)}$$
subject to the initial conditions:
$$x(0) = 1, \quad y(0) = 0$$
using Laplace transforms.

**Step 1: Take Laplace Transforms of Both Equations**
Let $\mathcal{L}\{x(t)\} = X(s)$ and $\mathcal{L}\{y(t)\} = Y(s)$.
$$\mathcal{L}\left\{\frac{dx}{dt}\right\} = s X(s) - x(0) = s X(s) - 1$$
$$\mathcal{L}\left\{\frac{dy}{dt}\right\} = s Y(s) - y(0) = s Y(s) - 0 = s Y(s)$$

Right-hand sides:
$$\mathcal{L}\{\sin t\} = \frac{1}{s^2 + 1}, \quad \mathcal{L}\{\cos t\} = \frac{s}{s^2 + 1}$$

Transformed system of algebraic equations:
$$s X(s) - 1 + Y(s) = \frac{1}{s^2 + 1} \implies s X(s) + Y(s) = 1 + \frac{1}{s^2 + 1} = \frac{s^2 + 2}{s^2 + 1} \quad \text{--- (A)}$$
$$X(s) + s Y(s) = \frac{s}{s^2 + 1} \quad \text{--- (B)}$$

**Step 2: Eliminate $Y(s)$ to Solve for $X(s)$**
Multiply Equation (A) by $s$:
$$s^2 X(s) + s Y(s) = \frac{s(s^2 + 2)}{s^2 + 1} \quad \text{--- (C)}$$
Subtract Equation (B) from Equation (C):
$$(s^2 - 1)X(s) = \frac{s(s^2 + 2)}{s^2 + 1} - \frac{s}{s^2 + 1} = \frac{s^3 + 2s - s}{s^2 + 1} = \frac{s^3 + s}{s^2 + 1} = \frac{s(s^2 + 1)}{s^2 + 1}$$
Cancel $(s^2 + 1)$ from numerator and denominator:
$$(s^2 - 1)X(s) = s \implies X(s) = \frac{s}{s^2 - 1}$$

**Step 3: Solve for $Y(s)$**
From Equation (B):
$$s Y(s) = \frac{s}{s^2 + 1} - X(s) = \frac{s}{s^2 + 1} - \frac{s}{s^2 - 1} = s \left[ \frac{1}{s^2 + 1} - \frac{1}{s^2 - 1} \right]$$
Divide both sides by $s$:
$$Y(s) = \frac{1}{s^2 + 1} - \frac{1}{s^2 - 1} = -\frac{1}{s^2 - 1} + \frac{1}{s^2 + 1}$$

**Step 4: Inverse Laplace Transforms**
Recall the standard hyperbolic and trigonometric inverse transforms:
$$\mathcal{L}^{-1}\left\{ \frac{s}{s^2 - 1} \right\} = \cosh t$$
$$\mathcal{L}^{-1}\left\{ \frac{1}{s^2 - 1} \right\} = \sinh t$$
$$\mathcal{L}^{-1}\left\{ \frac{1}{s^2 + 1} \right\} = \sin t$$

Inverting $X(s)$:
$$x(t) = \mathcal{L}^{-1}\{X(s)\} = \cosh t$$

Inverting $Y(s)$:
$$y(t) = \mathcal{L}^{-1}\{Y(s)\} = -\sinh t + \sin t = \sin t - \sinh t$$

**Step 5: Verification of Solutions**
- Initial conditions:
  $$x(0) = \cosh(0) = 1 \quad (\text{Satisfied})$$
  $$y(0) = \sin(0) - \sinh(0) = 0 - 0 = 0 \quad (\text{Satisfied})$$
- First differential equation check:
  $$\frac{dx}{dt} = \sinh t \implies \frac{dx}{dt} + y = \sinh t + (\sin t - \sinh t) = \sin t \quad (\text{Matches Eq 1})$$
- Second differential equation check:
  $$\frac{dy}{dt} = \cos t - \cosh t \implies \frac{dy}{dt} + x = (\cos t - \cosh t) + \cosh t = \cos t \quad (\text{Matches Eq 2})$$
"""
            },
        ]
    },
]
