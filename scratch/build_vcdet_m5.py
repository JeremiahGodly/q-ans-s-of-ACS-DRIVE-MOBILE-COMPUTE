# -*- coding: utf-8 -*-
"""
Module 5 for Subject 2: Vector Calculus, Differential Equations and Transforms (MAT102 / MATHS - VCDET)
Laplace Transforms, Convolution Theorem & Differential Systems
"""

M5_QUESTIONS = [
    {
        "qid": "vcdet-q21",
        "marks": 3,
        "type": "Short Answer",
        "title": "Laplace Transform of Modulated Sinusoid with Multiplied Polynomial Power",
        "yt_query": "laplace transform t squared e^-3t sin 2t first shifting multiplication by t",
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
        "title": "Convolution Theorem for Inverse Laplace Transforms and Standard Evaluation",
        "yt_query": "convolution theorem inverse laplace transform 1/s(s^2+1) engineering mathematics",
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
        "title": "Laplace Transform of Quotient Functions and Deduction of Frullani Improper Integrals",
        "yt_query": "laplace transform division by t cos at minus cos bt improper integral",
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
        "title": "Inverse Laplace Transform of Resonant Quadratic Pole via Convolution",
        "yt_query": "inverse laplace transform 1/(s^2+a^2)^2 convolution theorem resonance",
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
        "title": "Initial Value Problem Solution of Critically Damped Second-Order System via Laplace Transforms",
        "yt_query": "solve differential equation laplace transform initial value problem second order critical damping",
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
        "title": "Solution of Coupled Simultaneous Ordinary Differential Equations via Laplace Transforms",
        "yt_query": "simultaneous differential equations laplace transform dx/dt + y = sin t",
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
    }
]

M5_BYHEART = {
    "vcdet-q21": {
        "eq": r'$$\mathcal{L}\{t^2 e^{-3t} \sin 2t\} = \frac{d^2}{ds^2}\left[\frac{2}{(s+3)^2 + 4}\right] = \frac{12s^2 + 72s + 92}{(s^2 + 6s + 13)^3}$$',
        "text": r'<strong>Multiplication by $t^n$ & First Shifting:</strong> Applying the first shift property replaces $s \to s + 3$. Differentiating twice with respect to $s$ implements multiplication by $t^2$ in the time domain.'
    },
    "vcdet-q22": {
        "eq": r'$$\mathcal{L}^{-1}\{F(s)G(s)\} = \int_0^t f(u)g(t-u)du \implies \mathcal{L}^{-1}\left\{\frac{1}{s(s^2+1)}\right\} = \int_0^t \sin(t-u)du = 1 - \cos t$$',
        "text": r'<strong>Convolution Theorem:</strong> Transforms multiplication in the complex $s$-frequency domain into a convolution integral in the temporal domain, enabling direct calculation without partial fractions.'
    },
    "vcdet-q23": {
        "eq": r'$$\mathcal{L}\left\{\frac{\cos at - \cos bt}{t}\right\} = \frac{1}{2}\ln\left(\frac{s^2 + b^2}{s^2 + a^2}\right) \implies \int_0^\infty \frac{\cos t - \cos 2t}{t} \, dt = \ln 2$$',
        "text": r'<strong>Division by $t$ & Frullani-Type Integrals:</strong> Dividing by $t$ in time corresponds to integrating $F(u)$ from $s$ to $\infty$. Letting $s \to 0$ computes classic improper integrals like $\int_0^\infty \frac{\cos t - \cos 2t}{t} dt = \ln 2$.'
    },
    "vcdet-q24": {
        "eq": r'$$\mathcal{L}^{-1}\left\{\frac{1}{(s^2+a^2)^2}\right\} = \frac{1}{a^2}\int_0^t \sin(au)\sin(a(t-u))du = \frac{\sin at - at\cos at}{2a^3}$$',
        "text": r'<strong>Convolution of Resonant Poles:</strong> Convolving $\frac{1}{a}\sin at$ with itself generates the secular term $t\cos at$. The result describes resonance growth in undamped harmonic oscillators.'
    },
    "vcdet-q25": {
        "eq": r'$$Y(s) = -\frac{2}{s+2} + \frac{4}{(s+2)^2} + \frac{6}{(s+2)^3} \implies y(t) = (3t^2 + 4t - 2)e^{-2t}$$',
        "text": r'<strong>Initial Value Problem via Laplace Transforms:</strong> Incorporates initial conditions automatically into algebraic equations in $s$. The repeated pole $(s+2)^3$ yields critical damping response terms $e^{-2t}, te^{-2t}$, and resonant forcing $t^2 e^{-2t}$.'
    },
    "vcdet-q26": {
        "eq": r'$$X(s) = \frac{s}{s^2 - 1} \implies x(t) = \cosh t; \quad Y(s) = \frac{1}{s^2 + 1} - \frac{1}{s^2 - 1} \implies y(t) = \sin t - \sinh t$$',
        "text": r'<strong>Simultaneous Differential Systems:</strong> Coupled time-domain differential equations transform into a system of linear algebraic equations in $X(s)$ and $Y(s)$. Elimination reveals hyperbolic decoupling modes $\cosh t$ and $\sin t - \sinh t$.'
    }
}
