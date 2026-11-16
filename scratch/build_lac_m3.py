# -*- coding: utf-8 -*-
"""
Module 3 for Subject 1: Linear Algebra and Calculus (MAT101 / MATHS - LAC)
Calculus of Single Variable, Taylor Series & Indeterminate Forms
"""

M3_QUESTIONS = [
    {
        "qid": "lac-q11",
        "marks": 3,
        "type": "Short Answer",
        "title": "Evaluation of Indeterminate Form 0/0 via L'Hopital's Rule and Series Expansion",
        "yt_query": "limit x minus sin x over x cubed lhopital rule taylor series engineering mathematics",
        "img_path": "",
        "img_caption": "",
        "answer": r"""
We are required to evaluate the limit:
$$L = \lim_{x \to 0} \frac{x - \sin x}{x^3}$$
using L'Hopital's rule, and subsequently verify the result using Maclaurin series expansion.

**Method 1: Step-by-Step Evaluation via L'Hopital's Rule**
At $x = 0$, the numerator evaluates to $0 - \sin 0 = 0$, and the denominator evaluates to $0^3 = 0$. This represents the fundamental indeterminate form $\frac{0}{0}$.

Applying L'Hopital's rule by differentiating numerator and denominator with respect to $x$:
$$L = \lim_{x \to 0} \frac{\frac{d}{dx}(x - \sin x)}{\frac{d}{dx}(x^3)} = \lim_{x \to 0} \frac{1 - \cos x}{3x^2}$$
Evaluating at $x = 0$ gives $\frac{1 - \cos 0}{3(0)^2} = \frac{1 - 1}{0} = \frac{0}{0}$, which is still indeterminate.

Applying L'Hopital's rule a second time:
$$L = \lim_{x \to 0} \frac{\frac{d}{dx}(1 - \cos x)}{\frac{d}{dx}(3x^2)} = \lim_{x \to 0} \frac{-(-\sin x)}{6x} = \lim_{x \to 0} \frac{\sin x}{6x}$$
Evaluating at $x = 0$ gives $\frac{\sin 0}{6(0)} = \frac{0}{0}$, which remains indeterminate.

Applying L'Hopital's rule a third time:
$$L = \lim_{x \to 0} \frac{\frac{d}{dx}(\sin x)}{\frac{d}{dx}(6x)} = \lim_{x \to 0} \frac{\cos x}{6}$$
Evaluating at $x = 0$:
$$L = \frac{\cos 0}{6} = \frac{1}{6}$$

**Method 2: Verification using Maclaurin Series Expansion**
The Maclaurin series expansion for $\sin x$ about $x = 0$ is:
$$\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \dots = x - \frac{x^3}{6} + \frac{x^5}{120} - \dots$$
Substitute this series into the numerator:
$$x - \sin x = x - \left( x - \frac{x^3}{6} + \frac{x^5}{120} - \dots \right) = \frac{x^3}{6} - \frac{x^5}{120} + \dots$$
Now substitute into the limit quotient:
$$\frac{x - \sin x}{x^3} = \frac{\frac{x^3}{6} - \frac{x^5}{120} + \dots}{x^3} = \frac{1}{6} - \frac{x^2}{120} + \dots$$
Taking the limit as $x \to 0$:
$$\lim_{x \to 0} \left( \frac{1}{6} - \frac{x^2}{120} + \mathcal{O}(x^4) \right) = \frac{1}{6} - 0 + 0 = \frac{1}{6}$$
Both analytical methods yield the identical result $\frac{1}{6}$.
"""
    },
    {
        "qid": "lac-q12",
        "marks": 3,
        "type": "Short Answer",
        "title": "Concavity, Convexity, and Points of Inflection Analysis",
        "yt_query": "intervals of concavity points of inflection second derivative test engineering mathematics",
        "img_path": "",
        "img_caption": "",
        "answer": r"""
A twice-differentiable function $y = f(x)$ is defined to be:
1. **Concave Upward (Convex):** on an open interval where $f''(x) > 0$. Geometrically, the curve lies above its tangent lines and bends upwards like a cup.
2. **Concave Downward (Concave):** on an open interval where $f''(x) < 0$. Geometrically, the curve lies below its tangent lines and bends downwards like an inverted cup.
3. **Point of Inflection:** A point $(x_0, f(x_0))$ on the continuous curve where the concavity changes from upward to downward or downward to upward. At such a point, $f''(x_0) = 0$ (or $f''(x_0)$ does not exist) and $f''(x)$ strictly changes sign across $x_0$.

Let us analyze the given polynomial function:
$$f(x) = x^4 - 4x^3 + 10$$

**Step 1: Compute First and Second Derivatives**
$$f'(x) = \frac{d}{dx}(x^4 - 4x^3 + 10) = 4x^3 - 12x^2$$
$$f''(x) = \frac{d}{dx}(4x^3 - 12x^2) = 12x^2 - 24x = 12x(x - 2)$$

**Step 2: Find Candidate Inflection Points**
Set $f''(x) = 0$:
$$12x(x - 2) = 0 \implies x = 0 \quad \text{or} \quad x = 2$$
These two critical values partition the real number line $(-\infty, \infty)$ into three disjoint test intervals: $(-\infty, 0)$, $(0, 2)$, and $(2, \infty)$.

**Step 3: Interval Sign Analysis for $f''(x)$**
- **Interval 1: $(-\infty, 0)$**
  Select test point $x = -1$:
  $$f''(-1) = 12(-1)(-1 - 2) = (-12)(-3) = +36 > 0$$
  Since $f''(x) > 0$, the function is **Concave Upward** on $(-\infty, 0)$.

- **Interval 2: $(0, 2)$**
  Select test point $x = 1$:
  $$f''(1) = 12(1)(1 - 2) = (12)(-1) = -12 < 0$$
  Since $f''(x) < 0$, the function is **Concave Downward** on $(0, 2)$.

- **Interval 3: $(2, \infty)$**
  Select test point $x = 3$:
  $$f''(3) = 12(3)(3 - 2) = (36)(1) = +36 > 0$$
  Since $f''(x) > 0$, the function is **Concave Upward** on $(2, \infty)$.

**Step 4: Coordinates of Points of Inflection**
Because $f''(x)$ undergoes a strict sign change across both $x = 0$ (from positive to negative) and $x = 2$ (from negative to positive):
- At $x = 0$: $f(0) = 0^4 - 4(0^3) + 10 = 10 \implies$ Inflection point at $(0, 10)$.
- At $x = 2$: $f(2) = 2^4 - 4(2^3) + 10 = 16 - 32 + 10 = -6 \implies$ Inflection point at $(2, -6)$.
"""
    },
    {
        "qid": "lac-q13",
        "marks": 7,
        "type": "Analytical Problem",
        "title": "Evaluation of Exponential (infinity^0) and Difference (infinity - infinity) Indeterminate Forms",
        "yt_query": "indeterminate forms infinity to power 0 infinity minus infinity lhopital rule",
        "img_path": "",
        "img_caption": "",
        "answer": r"""
We evaluate two classic non-standard indeterminate forms step-by-step.

---
### Part (i): Evaluate $L_1 = \lim_{x \to 0^+} (\cot x)^{\sin x}$

**Step 1: Identify the Indeterminate Form**
As $x \to 0^+$, $\cot x \to +\infty$ and $\sin x \to 0$.
The limit exhibits the exponential indeterminate form $\infty^0$.

**Step 2: Logarithmic Transformation**
Let $y = (\cot x)^{\sin x}$. Taking the natural logarithm on both sides:
$$\ln y = \ln\left((\cot x)^{\sin x}\right) = \sin x \ln(\cot x)$$
As $x \to 0^+$, this has the form $0 \cdot \infty$. Rewrite it in fractional form to create an indeterminate quotient:
$$\ln y = \frac{\ln(\cot x)}{\frac{1}{\sin x}} = \frac{\ln(\cot x)}{\csc x}$$
Now, as $x \to 0^+$, $\ln(\cot x) \to \infty$ and $\csc x \to \infty$. This is the standard form $\frac{\infty}{\infty}$.

**Step 3: Apply L'Hopital's Rule**
Differentiate the numerator and denominator with respect to $x$:
$$\lim_{x \to 0^+} \ln y = \lim_{x \to 0^+} \frac{\frac{d}{dx}[\ln(\cot x)]}{\frac{d}{dx}[\csc x]} = \lim_{x \to 0^+} \frac{\frac{1}{\cot x}(-\csc^2 x)}{-\csc x \cot x}$$
Cancel the negative signs and one factor of $\csc x$:
$$\lim_{x \to 0^+} \ln y = \lim_{x \to 0^+} \frac{\csc x}{\cot^2 x}$$
Express in terms of elementary sine and cosine functions:
$$\frac{\csc x}{\cot^2 x} = \frac{\frac{1}{\sin x}}{\frac{\cos^2 x}{\sin^2 x}} = \frac{1}{\sin x} \cdot \frac{\sin^2 x}{\cos^2 x} = \frac{\sin x}{\cos^2 x}$$
Evaluate the limit as $x \to 0^+$:
$$\lim_{x \to 0^+} \ln y = \frac{\sin 0}{\cos^2 0} = \frac{0}{1^2} = 0$$

**Step 4: Exponentiate to Obtain Final Limit**
Since $\lim_{x \to 0^+} \ln y = 0$, by the continuity of the exponential function:
$$L_1 = \lim_{x \to 0^+} y = e^{\lim_{x \to 0^+} \ln y} = e^0 = 1$$

---
### Part (ii): Evaluate $L_2 = \lim_{x \to 0} \left( \frac{1}{x^2} - \frac{\cot x}{x} \right)$

**Step 1: Identify the Indeterminate Form**
As $x \to 0$, $\frac{1}{x^2} \to \infty$ and $\frac{\cot x}{x} = \frac{\cos x}{x \sin x} \to \infty$.
This exhibits the difference indeterminate form $\infty - \infty$.

**Step 2: Combine into a Single Rational Fraction**
Express $\cot x = \frac{\cos x}{\sin x}$:
$$\frac{1}{x^2} - \frac{\cot x}{x} = \frac{1}{x^2} - \frac{\cos x}{x \sin x} = \frac{\sin x - x \cos x}{x^2 \sin x}$$
At $x = 0$, this yields $\frac{0 - 0}{0} = \frac{0}{0}$.

Notice that as $x \to 0$, $\sin x \sim x$, so $x^2 \sin x \sim x^3$. Formally:
$$L_2 = \lim_{x \to 0} \frac{\sin x - x \cos x}{x^3} \cdot \lim_{x \to 0} \frac{x}{\sin x} = \lim_{x \to 0} \frac{\sin x - x \cos x}{x^3} \cdot 1$$

**Step 3: Apply L'Hopital's Rule to the Simplified Quotient**
$$L_2 = \lim_{x \to 0} \frac{\frac{d}{dx}(\sin x - x \cos x)}{\frac{d}{dx}(x^3)} = \lim_{x \to 0} \frac{\cos x - (\cos x - x \sin x)}{3x^2} = \lim_{x \to 0} \frac{x \sin x}{3x^2} = \lim_{x \to 0} \frac{\sin x}{3x}$$
Since $\lim_{x \to 0} \frac{\sin x}{x} = 1$:
$$L_2 = \frac{1}{3} \lim_{x \to 0} \frac{\sin x}{x} = \frac{1}{3}(1) = \frac{1}{3}$$
"""
    },
    {
        "qid": "lac-q14",
        "marks": 7,
        "type": "Analytical Problem",
        "title": "Taylor Series Expansion of Logarithmic Cosine and Numerical Approximation",
        "yt_query": "taylor series ln cos x about 0 maclaurin expansion approximation",
        "img_path": "",
        "img_caption": "",
        "answer": r"""
We are required to find the Taylor series expansion (Maclaurin series) of the function $f(x) = \ln(\cos x)$ about $x = 0$ up to the fourth-degree term in $x$, and deduce an approximate value for $\ln(\cos 0.1)$.

**Step 1: Formula for Maclaurin Series**
The Maclaurin series of a function $f(x)$ is given by:
$$f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \frac{f^{(4)}(0)}{4!}x^4 + \dots$$

**Step 2: Systematic Computation of Successive Derivatives at $x = 0$**
1. **Function value at 0:**
   $$f(0) = \ln(\cos 0) = \ln(1) = 0$$

2. **First Derivative:**
   $$f'(x) = \frac{1}{\cos x}(-\sin x) = -\tan x$$
   $$f'(0) = -\tan(0) = 0$$

3. **Second Derivative:**
   $$f''(x) = \frac{d}{dx}(-\tan x) = -\sec^2 x$$
   $$f''(0) = -\sec^2(0) = -(1)^2 = -1$$

4. **Third Derivative:**
   $$f'''(x) = \frac{d}{dx}(-\sec^2 x) = -2\sec x (\sec x \tan x) = -2\sec^2 x \tan x$$
   $$f'''(0) = -2(1)^2(0) = 0$$

5. **Fourth Derivative:**
   Apply the product rule to $f'''(x) = -2\sec^2 x \tan x$:
   $$f^{(4)}(x) = -2 \left[ \frac{d}{dx}(\sec^2 x) \tan x + \sec^2 x \frac{d}{dx}(\tan x) \right]$$
   $$f^{(4)}(x) = -2 \left[ (2\sec^2 x \tan x)\tan x + \sec^2 x(\sec^2 x) \right] = -2 [2\sec^2 x \tan^2 x + \sec^4 x]$$
   Evaluate at $x = 0$:
   $$f^{(4)}(0) = -2 [2(1)^2(0)^2 + (1)^4] = -2 [0 + 1] = -2$$

*(Notice that since $\ln(\cos(-x)) = \ln(\cos x)$ is an even function, all odd-order derivatives vanish identically at $x = 0$.)*

**Step 3: Construct the Maclaurin Series**
Substitute the derived values into the Maclaurin formula:
$$f(x) = 0 + 0 \cdot x + \frac{-1}{2!} x^2 + 0 \cdot x^3 + \frac{-2}{4!} x^4 + \dots$$
$$f(x) = -\frac{1}{2} x^2 - \frac{2}{24} x^4 - \dots$$
$$\ln(\cos x) = -\frac{x^2}{2} - \frac{x^4}{12} - \dots$$

**Step 4: Approximate $\ln(\cos 0.1)$**
Substitute $x = 0.1$ (radians) into the truncated polynomial:
$$\ln(\cos 0.1) \approx -\frac{(0.1)^2}{2} - \frac{(0.1)^4}{12}$$
Calculate the numerical values of each term:
$$-\frac{(0.1)^2}{2} = -\frac{0.01}{2} = -0.005$$
$$-\frac{(0.1)^4}{12} = -\frac{0.0001}{12} \approx -0.000008333$$
Summing both contributions:
$$\ln(\cos 0.1) \approx -0.005 - 0.000008333 = -0.005008333$$
"""
    },
    {
        "qid": "lac-q15",
        "marks": 7,
        "type": "Analytical Problem",
        "title": "Maclaurin Series Expansion of Composite Product Function and Derivative Deduction",
        "yt_query": "maclaurin series e^x cos x product of series fourth derivative deduction",
        "img_path": "",
        "img_caption": "",
        "answer": r"""
We are required to determine the Maclaurin series expansion of $f(x) = e^x \cos x$ up to the term containing $x^4$. Using this expansion, we deduce the value of the fourth derivative at the origin $f^{(4)}(0)$ and calculate an approximate numerical value for $e^{0.1}\cos(0.1)$.

**Step 1: Standard Known Series Expansions**
The Maclaurin series for $e^x$ is:
$$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \dots = 1 + x + \frac{x^2}{2} + \frac{x^3}{6} + \frac{x^4}{24} + \dots$$

The Maclaurin series for $\cos x$ is:
$$\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \dots = 1 - \frac{x^2}{2} + \frac{x^4}{24} - \dots$$

**Step 2: Cauchy Product of the Two Power Series**
Multiply the two series together, systematically grouping by powers of $x$ up to degree 4:
$$e^x \cos x = \left( 1 + x + \frac{x^2}{2} + \frac{x^3}{6} + \frac{x^4}{24} + \dots \right) \left( 1 - \frac{x^2}{2} + \frac{x^4}{24} - \dots \right)$$

Collecting terms:
- **Constant term ($x^0$):**
  $$1 \cdot 1 = 1$$
- **Degree 1 ($x^1$):**
  $$x \cdot 1 = x$$
- **Degree 2 ($x^2$):**
  $$1 \cdot \left(-\frac{x^2}{2}\right) + \frac{x^2}{2} \cdot 1 = \left(-\frac{1}{2} + \frac{1}{2}\right)x^2 = 0x^2$$
- **Degree 3 ($x^3$):**
  $$x \cdot \left(-\frac{x^2}{2}\right) + \frac{x^3}{6} \cdot 1 = \left(-\frac{1}{2} + \frac{1}{6}\right)x^3 = \left(-\frac{3}{6} + \frac{1}{6}\right)x^3 = -\frac{2}{6}x^3 = -\frac{1}{3}x^3$$
- **Degree 4 ($x^4$):**
  $$1 \cdot \left(\frac{x^4}{24}\right) + \frac{x^2}{2} \cdot \left(-\frac{x^2}{2}\right) + \frac{x^4}{24} \cdot 1 = \left(\frac{1}{24} - \frac{1}{4} + \frac{1}{24}\right)x^4$$
  $$= \left(\frac{2}{24} - \frac{6}{24}\right)x^4 = -\frac{4}{24}x^4 = -\frac{1}{6}x^4$$

Therefore, the combined Maclaurin series expansion up to degree 4 is:
$$e^x \cos x = 1 + x - \frac{x^3}{3} - \frac{x^4}{6} + \dots$$

**Step 3: Deduce the Fourth Derivative $f^{(4)}(0)$**
By Taylor's theorem, any function's Maclaurin series has the general form:
$$f(x) = \sum_{n=0}^\infty \frac{f^{(n)}(0)}{n!} x^n$$
Equating the coefficient of $x^4$ from our series to the general formula:
$$\frac{f^{(4)}(0)}{4!} = -\frac{1}{6}$$
Since $4! = 24$:
$$\frac{f^{(4)}(0)}{24} = -\frac{1}{6} \implies f^{(4)}(0) = 24 \left(-\frac{1}{6}\right) = -4$$

**Step 4: Numerical Approximation of $e^{0.1}\cos(0.1)$**
Substitute $x = 0.1$ into the truncated series:
$$e^{0.1}\cos(0.1) \approx 1 + 0.1 - \frac{(0.1)^3}{3} - \frac{(0.1)^4}{6}$$
$$= 1 + 0.1 - \frac{0.001}{3} - \frac{0.0001}{6}$$
$$= 1.1 - 0.00033333 - 0.00001667$$
$$= 1.1 - 0.00035000 = 1.09965$$
"""
    }
]

M3_BYHEART = {
    "lac-q11": {
        "eq": r'$$\lim_{x \to 0} \frac{x - \sin x}{x^3} = \lim_{x \to 0} \frac{1 - \cos x}{3x^2} = \lim_{x \to 0} \frac{\sin x}{6x} = \lim_{x \to 0} \frac{\cos x}{6} = \frac{1}{6}$$',
        "text": r'<strong>L\'Hopital\'s Rule for Indeterminate Forms:</strong> When $\lim \frac{f(x)}{g(x)}$ has form $\frac{0}{0}$ or $\frac{\infty}{\infty}$, differentiate numerator and denominator independently until a determinate value emerges.'
    },
    "lac-q12": {
        "eq": r'$$f\'\'(x) = 12x(x-2) \implies \begin{cases} x \in (-\infty, 0) \cup (2, \infty) & \text{Concave Upward } (f\'\' > 0) \\ x \in (0, 2) & \text{Concave Downward } (f\'\' < 0) \end{cases}; \quad \text{Inflection Points: } (0, 10), (2, -6)$$',
        "text": r'<strong>Concavity & Inflection Criteria:</strong> Concave up where $f\'\'(x) > 0$; concave down where $f\'\'(x) < 0$. Points of inflection occur strictly at real roots of $f\'\'(x) = 0$ where $f\'\'(x)$ undergoes a sign change.'
    },
    "lac-q13": {
        "eq": r'$$\lim_{x \to 0^+} (\cot x)^{\sin x} = e^{\lim \frac{\ln(\cot x)}{\csc x}} = e^0 = 1, \quad \lim_{x \to 0}\left(\frac{1}{x^2} - \frac{\cot x}{x}\right) = \lim_{x \to 0}\frac{\sin x - x\cos x}{x^3} = \frac{1}{3}$$',
        "text": r'<strong>Exponential & Difference Indeterminate Forms:</strong> For power forms $0^0, \infty^0, 1^\infty$, apply logarithms: $L = \exp[\lim g(x) \ln f(x)]$. For $\infty - \infty$, combine into a common denominator to reduce to $\frac{0}{0}$.'
    },
    "lac-q14": {
        "eq": r'$$\ln(\cos x) = -\frac{x^2}{2} - \frac{x^4}{12} - \frac{x^6}{45} - \dots, \quad \ln(\cos 0.1) \approx -0.00500833$$',
        "text": r'<strong>Taylor Expansion of Log-Cos:</strong> Because $\ln(\cos x)$ is an even function ($f(-x) = f(x)$), all odd-order derivatives vanish at $x=0$, leaving only even powers $-x^2/2 - x^4/12$.'
    },
    "lac-q15": {
        "eq": r'$$e^x \cos x = 1 + x - \frac{x^3}{3} - \frac{x^4}{6} + \dots \implies f^{(4)}(0) = -4, \quad e^{0.1}\cos(0.1) \approx 1.09965$$',
        "text": r'<strong>Series Cauchy Product & Derivatives:</strong> Multiplying Maclaurin series of standard functions directly generates the composite expansion. The $n$-th derivative at zero is extracted from the coefficient: $f^{(n)}(0) = n! \cdot a_n$.'
    }
}
