# -*- coding: utf-8 -*-
"""
Module 1 for Subject 2: Vector Calculus, Differential Equations and Transforms (MAT102 / MATHS - VCDET)
Ordinary Differential Equations, Bernoulli & Cauchy-Euler Equations
"""

M1_QUESTIONS = [
    {
        "qid": "vcdet-q1",
        "marks": 3,
        "type": "Short Answer",
        "title": "Solution of Bernoulli's Non-Linear First Order Differential Equation",
        "yt_query": "bernoulli differential equation first order non linear substitution integrating factor",
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
        "title": "Second Order Linear ODE with Repeated Roots and Dual Forcing Functions",
        "yt_query": "second order linear ode repeated roots complementary function particular integral",
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
        "title": "Method of Variation of Parameters for Non-Elementary Forcing Functions",
        "yt_query": "variation of parameters method second order differential equations wronskian sec tan",
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
        "title": "Cauchy-Euler Equidimensional Differential Equation Transformation and Solution",
        "yt_query": "cauchy euler differential equation substitution x=e^z engineering mathematics",
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
        "title": "Exponential Shift Operator Method for Composite Product Forcing Functions",
        "yt_query": "exponential shift theorem particular integral D operator x e^x sin x",
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
    }
]

M1_BYHEART = {
    "vcdet-q1": {
        "eq": r'$$v = y^{-1} \implies \frac{dv}{dx} - v = \sin x - \cos x \implies \frac{1}{y} = C e^x - \sin x$$',
        "text": r'<strong>Bernoulli Equation Transformation:</strong> Dividing by $y^n$ and substituting $v = y^{1-n}$ transforms the non-linear Bernoulli ODE into a standard first-order linear ODE solvable via integrating factor $e^{\int P dx}$.'
    },
    "vcdet-q2": {
        "eq": r'$$y = (C_1 + C_2 x) e^{2x} + 4x^2 e^{2x} + \frac{1}{8}\cos 2x$$',
        "text": r'<strong>Repeated Roots & Resonant PI:</strong> When auxiliary root $m=a$ is repeated $k$ times, complementary function includes $(C_1 + C_2 x)e^{ax}$, and particular integral for $e^{ax}$ introduces resonant factor $\frac{x^k}{k!} e^{ax}$.'
    },
    "vcdet-q3": {
        "eq": r'$$W = 1, \; u(x) = x - \tan x, \; v(x) = \ln|\sec x| \implies y = C_1 \cos x + C_2 \sin x + x \cos x + \sin x \ln|\sec x|$$',
        "text": r'<strong>Variation of Parameters:</strong> For $y\'\' + y = R(x)$, basis solutions are $y_1 = \cos x, y_2 = \sin x$ with Wronskian $W = 1$. The formulas $u = -\int y_2 R / W \, dx$ and $v = \int y_1 R / W \, dx$ yield particular integrals for any non-elementary excitation.'
    },
    "vcdet-q4": {
        "eq": r'$$[D_z(D_z-1) - 3D_z + 4]y = 2e^{2z} \implies y(x) = x^2 [C_1 + C_2 \ln x + (\ln x)^2]$$',
        "text": r'<strong>Cauchy-Euler Reduction:</strong> Setting $x = e^z$ converts variable-coefficient Cauchy-Euler equations into constant-coefficient ODEs in $z$, where $x^k \frac{d^k y}{dx^k} = D_z(D_z - 1)\dots(D_z - k + 1)y$.'
    },
    "vcdet-q5": {
        "eq": r'$$y_p = e^x \frac{1}{D^2}[x \sin x] = -e^x(x\sin x + 2\cos x) \implies y = (C_1 + C_2 x)e^x - e^x(x\sin x + 2\cos x)$$',
        "text": r'<strong>Exponential Shift Theorem:</strong> Shifting $e^{ax}$ outside the differential operator via $f(D)[e^{ax} V] = e^{ax} f(D+a)V$ eliminates the exponential factor and reduces operator power.'
    }
}
