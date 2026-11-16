# -*- coding: utf-8 -*-
"""
Content generator for Subject 1: Linear Algebra and Calculus (MAT101 / MATHS - LAC)
KTU 2019 Scheme Electrical & Electronics Engineering (EEE) Question Bank.
All answers written from the perspective of an experienced engineering mathematics professor.
Contains complete step-by-step mathematical working, intermediate equations, and highlighted results.
All strings use raw multiline strings to prevent any LaTeX escape corruptions.
Equations use standard KaTeX syntax: $$...$$ for display equations, $...$ for inline math.
"""

MATHS_LAC_EXAM_QUESTIONS = {
    "lac-q1": 'State the conditions for consistency of a non-homogeneous system of linear equations AX = B in terms of ranks of the coefficient matrix and the augmented matrix using the Rouché-Capelli theorem. Explain when the system has a unique solution, infinitely many solutions, and no solution.',
    "lac-q2": 'Define row echelon form of a matrix. Reduce the matrix A = [[1, 2, -1, 3], [2, 4, 1, -2], [3, 6, 3, -7]] to row echelon form and determine its rank.',
    "lac-q3": 'Investigate for what values of lambda and mu the system of equations x + y + z = 6, x + 2y + 3z = 10, x + 2y + lambda*z = mu has: (i) no solution, (ii) a unique solution, and (iii) infinitely many solutions. Also find the solutions when lambda = 4, mu = 13 and when lambda = 3, mu = 10.',
    "lac-q4": 'Test for consistency and solve the system of linear equations using Gauss elimination: x1 - 2x2 + x3 - 4x4 = 1, x1 + 3x2 + 7x3 + 2x4 = 2, x1 - 12x2 - 11x3 - 16x4 = -1.',
    "lac-q5": 'Find the non-trivial solutions of the homogeneous system of equations: x + 2y + 3z = 0, 3x + 4y + 4z = 0, 7x + 10y + 12z = 0. Determine the basis and dimension (nullity) of the solution space.',
    "lac-q6": 'State Cayley-Hamilton theorem. Use it to find A^(-1) and A^3 for the matrix A = [[1, 2], [3, 4]].',
    "lac-q7": 'Find the eigenvalues and eigenvectors of the matrix A = [[3, 1], [1, 3]] and verify that the eigenvectors corresponding to distinct eigenvalues are mutually orthogonal.',
    "lac-q8": 'Find the eigenvalues and eigenvectors of the 3x3 matrix A = [[2, 2, 1], [1, 3, 1], [1, 2, 2]]. Verify that the sum of the eigenvalues equals the trace of A and the product of the eigenvalues equals the determinant of A.',
    "lac-q9": 'Verify Cayley-Hamilton theorem for the matrix A = [[1, 0, 3], [2, 1, -1], [1, -1, 1]] and hence compute A^(-1) and A^4.',
    "lac-q10": 'Orthogonally diagonalise the symmetric matrix A = [[6, -2, 2], [-2, 3, -1], [2, -1, 3]]. Hence reduce the quadratic form Q = 6x^2 + 3y^2 + 3z^2 - 4xy + 4xz - 2yz into canonical form and determine its rank, index, signature, and nature.',
    "lac-q11": "Evaluate the limit lim_{x->0} (x - sin x) / x^3 using L'Hopital's rule, and verify the result using Maclaurin series expansion.",
    "lac-q12": 'Determine the intervals of concavity, convexity, and points of inflection for the function f(x) = x^4 - 4x^3 + 10.',
    "lac-q13": 'Evaluate the indeterminate forms: (i) lim_{x->0+} (cot x)^(sin x) (form infinity^0), and (ii) lim_{x->0} (1/x^2 - cot x / x) (form infinity - infinity).',
    "lac-q14": 'Find the Taylor series expansion of f(x) = ln(cos x) about x = 0 up to the term containing x^4 and deduce an approximation for ln(cos 0.1).',
    "lac-q15": 'Find the Maclaurin series expansion of f(x) = e^x cos x up to the term in x^4. Hence determine f^(4)(0) and calculate an approximate value for e^(0.1) cos(0.1).',
    "lac-q16": "State Euler's theorem on homogeneous functions. If u = sin^(-1)((x^2 + y^2)/(x + y)), prove that x du/dx + y du/dy = tan u.",
    "lac-q17": 'If z = f(x, y) where x = r cos theta and y = r sin theta, show that (dz/dx)^2 + (dz/dy)^2 = (dz/dr)^2 + (1/r^2)(dz/d theta)^2.',
    "lac-q18": 'If u = tan^(-1)((x^3 + y^3)/(x - y)), prove that: (i) x du/dx + y du/dy = sin 2u, and (ii) x^2 d^2u/dx^2 + 2xy d^2u/dxdy + y^2 d^2u/dy^2 = 2 cos 3u sin u.',
    "lac-q19": 'Find all local maxima, local minima, and saddle points of the multivariable function f(x, y) = x^3 + 3xy^2 - 15x^2 - 15y^2 + 72x.',
    "lac-q20": "Find the maximum volume of a rectangular parallelepiped inscribed in the ellipsoid x^2/a^2 + y^2/b^2 + z^2/c^2 = 1 using Lagrange's method of undetermined multipliers.",
    "lac-q21": 'Evaluate the double integral int_0^1 int_0^(sqrt(1-x^2)) (x^2 + y^2) dy dx by transforming into polar coordinates.',
    "lac-q22": 'Change the order of integration in int_0^1 int_x^(sqrt(x)) f(x, y) dy dx.',
    "lac-q23": 'Evaluate the improper double integral int_0^infinity int_0^infinity e^(-(x^2 + y^2)) dx dy by transforming into polar coordinates, and hence deduce the value of the Gaussian integral int_0^infinity e^(-x^2) dx = sqrt(pi)/2.',
    "lac-q24": 'Change the order of integration and evaluate: int_0^a int_y^a x / (x^2 + y^2) dx dy.',
    "lac-q25": 'Find the area bounded by the parabolas y^2 = 4ax and x^2 = 4ay using double integration.',
    "lac-q26": 'Find the volume of the solid bounded by the cylinder x^2 + y^2 = 4 and the planes y + z = 4 and z = 0 using triple integration.',
}

MATHS_LAC_BYHEART = {
    "lac-q1": {
        "eq": r"""$$\operatorname{rank}(A) = \operatorname{rank}([A|B]) = r \implies \begin{cases} r = n & \text{Unique solution} \\ r < n & \text{Infinitely many solutions ($n-r$ free parameters)} \\ \operatorname{rank}(A) < \operatorname{rank}([A|B]) & \text{Inconsistent (No solution)} \end{cases}$$""",
        "text": r"""<strong>Rouché-Capelli Theorem:</strong> A linear system $AX = B$ is consistent iff $\operatorname{rank}(A) = \operatorname{rank}([A|B]) = r$. If $r = n$, unique solution; if $r < n$, infinitely many solutions with $n-r$ independent parameters; if $\operatorname{rank}(A) \ne \operatorname{rank}([A|B])$, no solution."""
    },
    "lac-q2": {
        "eq": r"""$$U = \begin{bmatrix} 1 & 2 & -1 & 3 \\ 0 & 0 & 3 & -8 \\ 0 & 0 & 0 & 0 \end{bmatrix} \implies \operatorname{rank}(A) = \text{number of non-zero rows} = 2$$""",
        "text": r"""<strong>Row Echelon Form & Rank:</strong> Elementary row operations preserve the rank of a matrix. The rank equals the number of non-zero rows in the row echelon form."""
    },
    "lac-q3": {
        "eq": r"""$$\begin{bmatrix} 1 & 1 & 1 & | & 6 \\ 0 & 1 & 2 & | & 4 \\ 0 & 0 & \lambda - 3 & | & \mu - 10 \end{bmatrix} \implies \begin{cases} \lambda = 3, \mu \ne 10 & \text{No solution} \\ \lambda \ne 3, \forall \mu & \text{Unique solution} \\ \lambda = 3, \mu = 10 & \text{Infinite solutions} \end{cases}$$""",
        "text": r"""<strong>Consistency Analysis with Parameters:</strong> At $\lambda = 3$, row 3 of $A$ vanishes. If $\mu \ne 10$, augmented matrix has rank 3 while $A$ has rank 2 (inconsistent). If $\mu = 10$, both ranks are 2 (infinitely many solutions). If $\lambda \ne 3$, rank is 3 for any $\mu$ (unique solution)."""
    },
    "lac-q4": {
        "eq": r"""$$\operatorname{rank}(A) = \operatorname{rank}([A|B]) = 2 < n=4 \implies X = \begin{bmatrix} 7/5 \\ 1/5 \\ 0 \\ 0 \end{bmatrix} + s \begin{bmatrix} -17/5 \\ -6/5 \\ 1 \\ 0 \end{bmatrix} + t \begin{bmatrix} 8/5 \\ -6/5 \\ 0 \\ 1 \end{bmatrix}$$""",
        "text": r"""<strong>Gauss Elimination Free Parameters:</strong> When $r < n$, the solution space is an affine subspace with dimension $n - r$. The variables corresponding to non-pivot columns become arbitrary parameters $s, t \in \mathbb{R}$."""
    },
    "lac-q5": {
        "eq": r"""$$\operatorname{rank}(A) = 3 = n \implies \operatorname{Nullity}(A) = n - r = 3 - 3 = 0 \implies X = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix} \text{ (Trivial solution only)}$$""",
        "text": r"""<strong>Homogeneous System & Rank-Nullity:</strong> A homogeneous system $AX = 0$ possesses non-trivial solutions if and only if $\det(A) = 0$ ($\operatorname{rank}(A) < n$). When $\operatorname{rank}(A) = n$, the null space is trivial and contains only the origin."""
    },
    "lac-q6": {
        "eq": r"""$$A^2 - 5A - 2I = O \implies A^{-1} = \frac{1}{2}(A - 5I) = \begin{bmatrix} -2 & 1 \\ 1.5 & -0.5 \end{bmatrix}, \quad A^3 = 27A + 10I = \begin{bmatrix} 37 & 54 \\ 81 & 118 \end{bmatrix}$$""",
        "text": r"""<strong>Cayley-Hamilton Theorem:</strong> Every square matrix satisfies $\det(A - \lambda I) = 0$. Premultiplying or postmultiplying the matrix polynomial by $A^{-1}$ enables direct calculation of matrix inverse and high powers without determinants."""
    },
    "lac-q7": {
        "eq": r"""$$\lambda_1 = 4 \implies X_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}, \quad \lambda_2 = 2 \implies X_2 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}, \quad X_1^T X_2 = 1 - 1 = 0$$""",
        "text": r"""<strong>Orthogonality of Real Symmetric Matrix Eigenvectors:</strong> Eigenvectors of any real symmetric matrix associated with distinct eigenvalues are strictly orthogonal: $X_i^T X_j = 0$ for $\lambda_i \ne \lambda_j$."""
    },
    "lac-q8": {
        "eq": r"""$$\lambda = 5, 1, 1 \implies \sum \lambda_i = 7 = \operatorname{tr}(A), \quad \prod \lambda_i = 5 = \det(A); \quad X_{\lambda=5} = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}, X_{\lambda=1} = \left\{ \begin{bmatrix} -2 \\ 1 \\ 0 \end{bmatrix}, \begin{bmatrix} -1 \\ 0 \\ 1 \end{bmatrix} \right\}$$""",
        "text": r"""<strong>Eigenvalue Properties & Multiplicity:</strong> Sum of eigenvalues equals the matrix trace, and product equals the determinant. For repeated eigenvalues, geometric multiplicity equals the nullity $n - \operatorname{rank}(A - \lambda I)$."""
    },
    "lac-q9": {
        "eq": r"""$$A^3 - 3A^2 - A + 9I = O \implies A^{-1} = \frac{1}{9}\begin{bmatrix} 0 & 3 & 3 \\ 3 & 2 & -7 \\ 3 & -1 & -1 \end{bmatrix}, \quad A^4 = 10A^2 - 6A - 27I$$""",
        "text": r"""<strong>Matrix Inverse via Characteristic Equation:</strong> For $A^3 - s_1 A^2 + s_2 A - \det(A)I = O$, multiplying by $A^{-1}$ yields $A^{-1} = \frac{1}{\det(A)}(A^2 - s_1 A + s_2 I)$, bypassing matrix cofactors."""
    },
    "lac-q10": {
        "eq": r"""$$Q = 8y_1^2 + 2y_2^2 + 2y_3^2, \quad \operatorname{rank} = 3, \quad \operatorname{index} = 3, \quad \operatorname{signature} = 3, \quad \text{Strictly Positive Definite}$$""",
        "text": r"""<strong>Orthogonal Diagonalisation & Quadratic Forms:</strong> Any real symmetric matrix $A$ can be diagonalised by an orthogonal matrix $P$ ($P^T A P = D$). Canonical form is $\sum \lambda_i y_i^2$. If all $\lambda_i > 0$, the quadratic form is strictly positive definite."""
    },
    "lac-q11": {
        "eq": r"""$$\lim_{x \to 0} \frac{x - \sin x}{x^3} = \lim_{x \to 0} \frac{1 - \cos x}{3x^2} = \lim_{x \to 0} \frac{\sin x}{6x} = \lim_{x \to 0} \frac{\cos x}{6} = \frac{1}{6}$$""",
        "text": r"""<strong>L\'Hopital\'s Rule for Indeterminate Forms:</strong> When $\lim \frac{f(x)}{g(x)}$ has form $\frac{0}{0}$ or $\frac{\infty}{\infty}$, differentiate numerator and denominator independently until a determinate value emerges."""
    },
    "lac-q12": {
        "eq": r"""$$f\'\'(x) = 12x(x-2) \implies \begin{cases} x \in (-\infty, 0) \cup (2, \infty) & \text{Concave Upward } (f\'\' > 0) \\ x \in (0, 2) & \text{Concave Downward } (f\'\' < 0) \end{cases}; \quad \text{Inflection Points: } (0, 10), (2, -6)$$""",
        "text": r"""<strong>Concavity & Inflection Criteria:</strong> Concave up where $f\'\'(x) > 0$; concave down where $f\'\'(x) < 0$. Points of inflection occur strictly at real roots of $f\'\'(x) = 0$ where $f\'\'(x)$ undergoes a sign change."""
    },
    "lac-q13": {
        "eq": r"""$$\lim_{x \to 0^+} (\cot x)^{\sin x} = e^{\lim \frac{\ln(\cot x)}{\csc x}} = e^0 = 1, \quad \lim_{x \to 0}\left(\frac{1}{x^2} - \frac{\cot x}{x}\right) = \lim_{x \to 0}\frac{\sin x - x\cos x}{x^3} = \frac{1}{3}$$""",
        "text": r"""<strong>Exponential & Difference Indeterminate Forms:</strong> For power forms $0^0, \infty^0, 1^\infty$, apply logarithms: $L = \exp[\lim g(x) \ln f(x)]$. For $\infty - \infty$, combine into a common denominator to reduce to $\frac{0}{0}$."""
    },
    "lac-q14": {
        "eq": r"""$$\ln(\cos x) = -\frac{x^2}{2} - \frac{x^4}{12} - \frac{x^6}{45} - \dots, \quad \ln(\cos 0.1) \approx -0.00500833$$""",
        "text": r"""<strong>Taylor Expansion of Log-Cos:</strong> Because $\ln(\cos x)$ is an even function ($f(-x) = f(x)$), all odd-order derivatives vanish at $x=0$, leaving only even powers $-x^2/2 - x^4/12$."""
    },
    "lac-q15": {
        "eq": r"""$$e^x \cos x = 1 + x - \frac{x^3}{3} - \frac{x^4}{6} + \dots \implies f^{(4)}(0) = -4, \quad e^{0.1}\cos(0.1) \approx 1.09965$$""",
        "text": r"""<strong>Series Cauchy Product & Derivatives:</strong> Multiplying Maclaurin series of standard functions directly generates the composite expansion. The $n$-th derivative at zero is extracted from the coefficient: $f^{(n)}(0) = n! \cdot a_n$."""
    },
    "lac-q16": {
        "eq": r"""$$f(x, y) = \sin u, \text{ degree } n=1 \implies x \frac{\partial u}{\partial x} + y \frac{\partial u}{\partial y} = n \frac{f(u)}{f\'(u)} = \frac{\sin u}{\cos u} = \tan u$$""",
        "text": r"""<strong>Euler\'s Theorem for Implicit Functions:</strong> If $f(u)$ is homogeneous of degree $n$, then $x u_x + y u_y = n \frac{f(u)}{f\'(u)}$. For $f(u) = \sin u$ of degree 1, this immediately yields $\tan u$."""
    },
    "lac-q17": {
        "eq": r"""$$\left(\frac{\partial z}{\partial r}\right)^2 + \frac{1}{r^2}\left(\frac{\partial z}{\partial \theta}\right)^2 = \left(\frac{\partial z}{\partial x}\right)^2 + \left(\frac{\partial z}{\partial y}\right)^2 = \|\nabla z\|^2$$""",
        "text": r"""<strong>Invariance of Gradient Magnitude:</strong> The squared Euclidean norm of the spatial gradient vector $\|\nabla z\|^2$ is coordinate-invariant under rotation and transformation from Cartesian $(x,y)$ to polar $(r,\theta)$ frames."""
    },
    "lac-q18": {
        "eq": r"""$$x^2 u_{xx} + 2xy u_{xy} + y^2 u_{yy} = g(u)[g\'(u) - 1] = \sin 2u (2\cos 2u - 1) = 2 \cos 3u \sin u$$""",
        "text": r"""<strong>Extended Euler\'s Second Order Formula:</strong> If $x u_x + y u_y = g(u)$, then $x^2 u_{xx} + 2xy u_{xy} + y^2 u_{yy} = g(u)[g\'(u) - 1]$. For $g(u) = \sin 2u$, this simplifies to $2\cos 3u \sin u$."""
    },
    "lac-q19": {
        "eq": r"""$$D = rt - s^2 \implies \begin{cases} (4, 0): D=36>0, r=-6<0 & \text{Local Maximum } (f = 112) \\ (6, 0): D=36>0, r=6>0 & \text{Local Minimum } (f = 108) \\ (5, \pm 1): D=-36<0 & \text{Saddle Points } (f = 110) \end{cases}$$""",
        "text": r"""<strong>Second Derivative Test for Functions of Two Variables:</strong> Calculate $D = f_{xx}f_{yy} - (f_{xy})^2$. If $D > 0$ and $f_{xx} < 0$, local max; if $D > 0$ and $f_{xx} > 0$, local min; if $D < 0$, saddle point."""
    },
    "lac-q20": {
        "eq": r"""$$x = \frac{a}{\sqrt{3}}, \; y = \frac{b}{\sqrt{3}}, \; z = \frac{c}{\sqrt{3}} \implies V_{\max} = 8xyz = \frac{8abc}{3\sqrt{3}}$$""",
        "text": r"""<strong>Lagrange Multipliers for Inscribed Volume:</strong> Equal partition of constraint contributions $\frac{x^2}{a^2} = \frac{y^2}{b^2} = \frac{z^2}{c^2} = \frac{1}{3}$ yields optimal vertex coordinates $(a/\sqrt{3}, b/\sqrt{3}, c/\sqrt{3})$ and maximum volume $8abc/(3\sqrt{3})$."""
    },
    "lac-q21": {
        "eq": r"""$$\int_0^1 \int_0^{\sqrt{1-x^2}} (x^2 + y^2) \, dy \, dx = \int_0^{\pi/2} d\theta \int_0^1 r^3 \, dr = \left(\frac{\pi}{2}\right)\left(\frac{1}{4}\right) = \frac{\pi}{8}$$""",
        "text": r"""<strong>Cartesian to Polar Conversion:</strong> Substitute $x = r\cos\theta, y = r\sin\theta, dx\,dy = r\,dr\,d\theta$. The first-quadrant unit circular arc transforms to limits $r \in [0, 1]$ and $\theta \in [0, \pi/2]$."""
    },
    "lac-q22": {
        "eq": r"""$$\int_{x=0}^1 \int_{y=x}^{\sqrt{x}} f(x, y) \, dy \, dx = \int_{y=0}^1 \int_{x=y^2}^y f(x, y) \, dx \, dy$$""",
        "text": r"""<strong>Change of Order of Integration:</strong> Sketch the region bounded by $y = x$ and $y = \sqrt{x}$. Switch from vertical strips ($x$-constant) to horizontal strips ($y$-constant), changing bounds from $y \in [x, \sqrt{x}]$ to $x \in [y^2, y]$."""
    },
    "lac-q23": {
        "eq": r"""$$\int_0^\infty \int_0^\infty e^{-(x^2+y^2)} \, dx \, dy = \frac{\pi}{4} \implies \left(\int_0^\infty e^{-x^2} \, dx\right)^2 = \frac{\pi}{4} \implies \int_0^\infty e^{-x^2} \, dx = \frac{\sqrt{\pi}}{2}$$""",
        "text": r"""<strong>Gaussian Integral Evaluation via Double Integrals:</strong> Cartesian integration of $e^{-x^2}$ lacks elementary antiderivative. Converting $J^2$ to polar coordinates yields $r e^{-r^2}$, readily integrable to $\pi/4$, proving $J = \sqrt{\pi}/2$."""
    },
    "lac-q24": {
        "eq": r"""$$\int_0^a \int_y^a \frac{x}{x^2 + y^2} \, dx \, dy = \int_0^a \left[\int_0^x \frac{x}{x^2 + y^2} \, dy \right] dx = \int_0^a \frac{\pi}{4} \, dx = \frac{\pi a}{4}$$""",
        "text": r"""<strong>Change of Order for Triangular Domain:</strong> Switching order from $dx\,dy$ to $dy\,dx$ converts the complicated logarithmic $x$-integral into a standard inverse tangent $\tan^{-1}(y/x)$, collapsing the inner integral to constant $\pi/4$."""
    },
    "lac-q25": {
        "eq": r"""$$\text{Area} = \int_0^{4a} \left(2\sqrt{ax} - \frac{x^2}{4a}\right) dx = \left[\frac{4\sqrt{a}}{3}x^{3/2} - \frac{x^3}{12a}\right]_0^{4a} = \frac{16a^2}{3}$$""",
        "text": r"""<strong>Area Enclosed by Conjugate Parabolas:</strong> The intersection between $y^2 = 4ax$ and $x^2 = 4ay$ spans $[0, 4a]$. Double integration yields the celebrated classical area result $\frac{16a^2}{3}$."""
    },
    "lac-q26": {
        "eq": r"""$$V = \int_0^{2\pi} \int_0^2 (4 - r\sin\theta) r \, dr \, d\theta = \int_0^{2\pi} \left(8 - \frac{8}{3}\sin\theta\right) d\theta = 16\pi$$""",
        "text": r"""<strong>Volume of Truncated Cylinder via Cylindrical Coordinates:</strong> Cylindrical coordinates simplify circular boundaries ($r \le 2$). The odd periodic term $\sin\theta$ integrates to zero over $[0, 2\pi]$, leaving mean height $4$ times base area $\pi(2^2) = 16\pi$."""
    },
}

MATHS_LAC_MODULES = [
    {
        "module_id": "lac-m1",
        "module_num": "Module 1",
        "module_title": "Linear Systems of Equations, Gauss Elimination & Rank",
        "questions": [
            {
                "qid": "lac-q1",
                "marks": 3,
                "type": "Short Answer",
                "title": 'Consistency Criteria of Linear Systems: Rouché-Capelli Theorem',
                "yt_query": 'consistency of system of linear equations rouche capelli theorem rank matrix',
                "img_path": "",
                "img_caption": "",
                "answer": r"""
In linear algebra, a system of $m$ linear equations in $n$ unknowns is written in matrix notation as $AX = B$, where $A$ is the $m \times n$ coefficient matrix, $X$ is the $n \times 1$ column vector of unknowns, and $B$ is the $m \times 1$ non-homogeneous column vector. The augmented matrix of the system is formed by adjoining $B$ to $A$ as an additional column, denoted as $[A | B]$ with dimensions $m \times (n+1)$. The fundamental theorem governing the solvability of this system is the Rouché-Capelli theorem.

The Rouché-Capelli theorem states that the linear system $AX = B$ is consistent (possesses at least one solution) if and only if the rank of the coefficient matrix equals the rank of the augmented matrix:
$$\operatorname{rank}(A) = \operatorname{rank}([A | B]) = r$$

When this rank equality holds, the nature of the solution space depends strictly on the value of $r$ relative to the number of unknowns $n$:

1. **Unique Solution ($r = n$):** If $\operatorname{rank}(A) = \operatorname{rank}([A | B]) = n$, the system has exactly one unique solution. The row echelon form contains a leading pivot in every variable column, meaning there are no free variables. All variables are uniquely determined by back-substitution.

2. **Infinitely Many Solutions ($r < n$):** If $\operatorname{rank}(A) = \operatorname{rank}([A | B]) = r < n$, the system is consistent but possesses infinitely many solutions. Exactly $(n - r)$ variables can be assigned arbitrary real parameters. These $(n - r)$ variables are called free variables or parameters, and the solution forms an affine subspace of dimension $(n - r)$.

3. **Inconsistent / No Solution ($\operatorname{rank}(A) < \operatorname{rank}([A | B])$):** If the rank of the coefficient matrix is strictly less than the rank of the augmented matrix, the system is inconsistent and has no solution. In row echelon form, this condition manifests as a row of the form $\begin{bmatrix} 0 & 0 & \dots & 0 & | & c \end{bmatrix}$ where $c \neq 0$, which represents the impossible contradiction $0 = c$.

For a homogeneous linear system $AX = 0$, the vector $B = 0$ always adds a column of zeros. Hence $\operatorname{rank}(A) = \operatorname{rank}([A | 0])$ is always satisfied, guaranteeing that homogeneous systems are unconditionally consistent. If $r = n$, only the trivial solution $X = 0$ exists. If $r < n$, the system possesses non-trivial solutions with $(n - r)$ linearly independent solution vectors forming a basis of the null space $\operatorname{Null}(A)$.
"""
            },
            {
                "qid": "lac-q2",
                "marks": 3,
                "type": "Short Answer",
                "title": 'Row Echelon Form and Rank Determination by Row Reduction',
                "yt_query": 'row echelon form of matrix rank reduction engineering mathematics',
                "img_path": "",
                "img_caption": "",
                "answer": r"""
A matrix is said to be in **row echelon form** if it satisfies three strict structural conditions:
1. All non-zero rows precede any all-zero rows (all-zero rows, if any, are situated at the very bottom of the matrix).
2. The leading non-zero entry (pivot) of each non-zero row occurs in a column strictly to the right of the leading entry of the row immediately above it.
3. All entries in a column directly below a leading pivot are strictly zero.

The **rank** of a matrix $A$, denoted $\operatorname{rank}(A)$ or $\rho(A)$, is defined as the maximum number of linearly independent rows (or columns) in $A$. Because elementary row operations preserve row spaces and linear independence, the rank of $A$ is precisely equal to the number of non-zero rows in its row echelon form.

Let us reduce the given $3 \times 4$ matrix $A$ to row echelon form step-by-step:
$$A = \begin{bmatrix} 1 & 2 & -1 & 3 \\ 2 & 4 & 1 & -2 \\ 3 & 6 & 3 & -7 \end{bmatrix}$$

**Step 1: Eliminate entries below the pivot in Column 1 ($a_{11} = 1$).**
Perform row operations $R_2 \to R_2 - 2R_1$ and $R_3 \to R_3 - 3R_1$:
$$R_2 - 2R_1 = [2 - 2(1), \; 4 - 2(2), \; 1 - 2(-1), \; -2 - 2(3)] = [0, \; 0, \; 3, \; -8]$$
$$R_3 - 3R_1 = [3 - 3(1), \; 6 - 3(2), \; 3 - 3(-1), \; -7 - 3(3)] = [0, \; 0, \; 6, \; -16]$$

The intermediate matrix is:
$$A \sim \begin{bmatrix} 1 & 2 & -1 & 3 \\ 0 & 0 & 3 & -8 \\ 0 & 0 & 6 & -16 \end{bmatrix}$$

**Step 2: Eliminate entries below the pivot in Column 3 ($a_{23} = 3$).**
Notice that row 3 is an exact scalar multiple of row 2 ($2 \times R_2$). Perform row operation $R_3 \to R_3 - 2R_2$:
$$R_3 - 2R_2 = [0 - 0, \; 0 - 0, \; 6 - 2(3), \; -16 - 2(-8)] = [0, \; 0, \; 0, \; 0]$$

The matrix is now in row echelon form:
$$U = \begin{bmatrix} 1 & 2 & -1 & 3 \\ 0 & 0 & 3 & -8 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$

The leading pivots are at position $(1, 1)$ and position $(2, 3)$. Row 3 consists entirely of zeros. Counting the non-zero rows in $U$:
$$\text{Number of non-zero rows} = 2 \implies \operatorname{rank}(A) = 2$$
"""
            },
            {
                "qid": "lac-q3",
                "marks": 7,
                "type": "Analytical Problem",
                "title": 'Consistency and Parametric Analysis of Linear System with Lambda and Mu',
                "yt_query": 'values of lambda and mu for unique infinite no solution system of linear equations',
                "img_path": "",
                "img_caption": "",
                "answer": r"""
Consider the system of three linear equations in three variables $x, y, z$:
$$x + y + z = 6$$
$$x + 2y + 3z = 10$$
$$x + 2y + \lambda z = \mu$$

**Step 1: Form the Augmented Matrix $[A | B]$**
$$[A | B] = \begin{bmatrix} 1 & 1 & 1 & | & 6 \\ 1 & 2 & 3 & | & 10 \\ 1 & 2 & \lambda & | & \mu \end{bmatrix}$$

**Step 2: Reduce to Row Echelon Form using Elementary Row Operations**
First, eliminate the first column entries in rows 2 and 3 using $R_2 \to R_2 - R_1$ and $R_3 \to R_3 - R_1$:
$$R_2 - R_1 = [1 - 1, \; 2 - 1, \; 3 - 1, \; | \; 10 - 6] = [0, \; 1, \; 2, \; | \; 4]$$
$$R_3 - R_1 = [1 - 1, \; 2 - 1, \; \lambda - 1, \; | \; \mu - 6] = [0, \; 1, \; \lambda - 1, \; | \; \mu - 6]$$

The augmented matrix becomes:
$$[A | B] \sim \begin{bmatrix} 1 & 1 & 1 & | & 6 \\ 0 & 1 & 2 & | & 4 \\ 0 & 1 & \lambda - 1 & | & \mu - 6 \end{bmatrix}$$

Next, eliminate the second column entry in row 3 using $R_3 \to R_3 - R_2$:
$$R_3 - R_2 = [0 - 0, \; 1 - 1, \; (\lambda - 1) - 2, \; | \; (\mu - 6) - 4] = [0, \; 0, \; \lambda - 3, \; | \; \mu - 10]$$

The final row echelon form of the augmented matrix is:
$$[A | B] \sim \begin{bmatrix} 1 & 1 & 1 & | & 6 \\ 0 & 1 & 2 & | & 4 \\ 0 & 0 & \lambda - 3 & | & \mu - 10 \end{bmatrix}$$

**Step 3: Comprehensive Investigation of Cases**

**(i) No Solution (Inconsistent):**
A system has no solution if $\operatorname{rank}(A) \neq \operatorname{rank}([A | B])$, which requires $\operatorname{rank}(A) = 2$ and $\operatorname{rank}([A | B]) = 3$.
From row 3, this condition is satisfied when:
$$\lambda - 3 = 0 \implies \lambda = 3 \quad \text{and} \quad \mu - 10 \neq 0 \implies \mu \neq 10$$
Under this condition, the third equation reduces to $0x + 0y + 0z = \mu - 10 \neq 0$, which is geometrically contradictory.

**(ii) Unique Solution:**
A system possesses a unique solution when $\operatorname{rank}(A) = \operatorname{rank}([A | B]) = 3$ (number of unknowns $n = 3$).
This requires that the pivot position in row 3 is non-zero:
$$\lambda - 3 \neq 0 \implies \lambda \neq 3 \quad \text{for any arbitrary real value of } \mu$$

*Explicit Solution for $\lambda = 4, \mu = 13$:*
Substitute $\lambda = 4, \mu = 13$ into the echelon form:
$$\begin{bmatrix} 1 & 1 & 1 & | & 6 \\ 0 & 1 & 2 & | & 4 \\ 0 & 0 & 1 & | & 3 \end{bmatrix}$$
From row 3:
$$1z = 3 \implies z = 3$$
From row 2:
$$y + 2(3) = 4 \implies y = 4 - 6 = -2$$
From row 1:
$$x + (-2) + 3 = 6 \implies x + 1 = 6 \implies x = 5$$
Thus, the unique solution is $(x, y, z) = (5, -2, 3)$.

**(iii) Infinitely Many Solutions:**
A system has infinitely many solutions when $\operatorname{rank}(A) = \operatorname{rank}([A | B]) = 2 < n = 3$.
This requires both pivot terms in the third row to vanish simultaneously:
$$\lambda - 3 = 0 \implies \lambda = 3 \quad \text{and} \quad \mu - 10 = 0 \implies \mu = 10$$

*Explicit Solution for $\lambda = 3, \mu = 10$:*
The echelon form becomes:
$$\begin{bmatrix} 1 & 1 & 1 & | & 6 \\ 0 & 1 & 2 & | & 4 \\ 0 & 0 & 0 & | & 0 \end{bmatrix}$$
Here $n - r = 3 - 2 = 1$ free variable exists. Choose $z = k$, where $k \in \mathbb{R}$ is an arbitrary parameter.
From row 2:
$$y + 2k = 4 \implies y = 4 - 2k$$
From row 1:
$$x + (4 - 2k) + k = 6 \implies x + 4 - k = 6 \implies x = 2 + k$$
Therefore, the infinite family of solutions is parameterized as:
$$\begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 2 + k \\ 4 - 2k \\ k \end{bmatrix} = \begin{bmatrix} 2 \\ 4 \\ 0 \end{bmatrix} + k \begin{bmatrix} 1 \\ -2 \\ 1 \end{bmatrix}, \quad \forall k \in \mathbb{R}$$
"""
            },
            {
                "qid": "lac-q4",
                "marks": 7,
                "type": "Analytical Problem",
                "title": 'Gauss Elimination and Complete Solution of Underdetermined System',
                "yt_query": 'gauss elimination test consistency underdetermined system infinitely many solutions',
                "img_path": "",
                "img_caption": "",
                "answer": r"""
We are required to test for consistency and solve the following system of 3 linear equations in 4 unknowns $x_1, x_2, x_3, x_4$:
$$x_1 - 2x_2 + x_3 - 4x_4 = 1$$
$$x_1 + 3x_2 + 7x_3 + 2x_4 = 2$$
$$x_1 - 12x_2 - 11x_3 - 16x_4 = -1$$

**Step 1: Set up the Augmented Matrix $[A | B]$**
$$[A | B] = \begin{bmatrix} 1 & -2 & 1 & -4 & | & 1 \\ 1 & 3 & 7 & 2 & | & 2 \\ 1 & -12 & -11 & -16 & | & -1 \end{bmatrix}$$

**Step 2: Perform Forward Gauss Elimination**
Eliminate $x_1$ from rows 2 and 3 using $R_2 \to R_2 - R_1$ and $R_3 \to R_3 - R_1$:
$$R_2 - R_1 = [1 - 1, \; 3 - (-2), \; 7 - 1, \; 2 - (-4), \; | \; 2 - 1] = [0, \; 5, \; 6, \; 6, \; | \; 1]$$
$$R_3 - R_1 = [1 - 1, \; -12 - (-2), \; -11 - 1, \; -16 - (-4), \; | \; -1 - 1] = [0, \; -10, \; -12, \; -12, \; | \; -2]$$

The augmented matrix becomes:
$$[A | B] \sim \begin{bmatrix} 1 & -2 & 1 & -4 & | & 1 \\ 0 & 5 & 6 & 6 & | & 1 \\ 0 & -10 & -12 & -12 & | & -2 \end{bmatrix}$$

Next, eliminate the entry below pivot $a_{22} = 5$ by performing $R_3 \to R_3 + 2R_2$:
$$R_3 + 2R_2 = [0 + 2(0), \; -10 + 2(5), \; -12 + 2(6), \; -12 + 2(6), \; | \; -2 + 2(1)] = [0, \; 0, \; 0, \; 0, \; | \; 0]$$

The row echelon form of the augmented matrix is:
$$[A | B] \sim \begin{bmatrix} 1 & -2 & 1 & -4 & | & 1 \\ 0 & 5 & 6 & 6 & | & 1 \\ 0 & 0 & 0 & 0 & | & 0 \end{bmatrix}$$

**Step 3: Test for Consistency**
The number of non-zero rows in coefficient matrix $A$ is 2, so $\operatorname{rank}(A) = 2$.
The number of non-zero rows in augmented matrix $[A | B]$ is 2, so $\operatorname{rank}([A | B]) = 2$.
Since $\operatorname{rank}(A) = \operatorname{rank}([A | B]) = 2$, the system is **consistent**.
Because the rank $r = 2$ is strictly less than the number of variables $n = 4$, the system has **infinitely many solutions**.
The number of free parameters is $n - r = 4 - 2 = 2$.

**Step 4: Back-Substitution with Free Parameters**
Pivots exist in columns 1 and 2 ($x_1, x_2$). The non-pivot variables $x_3$ and $x_4$ are chosen as independent free parameters:
$$x_3 = s, \quad x_4 = t, \quad \text{where } s, t \in \mathbb{R}$$

From Row 2:
$$5x_2 + 6x_3 + 6x_4 = 1 \implies 5x_2 + 6s + 6t = 1$$
$$x_2 = \frac{1 - 6s - 6t}{5} = \frac{1}{5} - \frac{6}{5}s - \frac{6}{5}t$$

From Row 1:
$$x_1 - 2x_2 + x_3 - 4x_4 = 1 \implies x_1 = 1 + 2x_2 - x_3 + 4x_4$$
Substitute $x_2, x_3, x_4$:
$$x_1 = 1 + 2\left(\frac{1}{5} - \frac{6}{5}s - \frac{6}{5}t\right) - s + 4t$$
$$x_1 = 1 + \frac{2}{5} - \frac{12}{5}s - \frac{12}{5}t - s + 4t = \frac{7}{5} - \left(\frac{12}{5} + 1\right)s + \left(4 - \frac{12}{5}\right)t$$
$$x_1 = \frac{7}{5} - \frac{17}{5}s + \frac{8}{5}t$$

**Step 5: General Solution Vector**
The general solution in vector form is:
$$\begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{bmatrix} = \begin{bmatrix} 7/5 \\ 1/5 \\ 0 \\ 0 \end{bmatrix} + s \begin{bmatrix} -17/5 \\ -6/5 \\ 1 \\ 0 \end{bmatrix} + t \begin{bmatrix} 8/5 \\ -6/5 \\ 0 \\ 1 \end{bmatrix}, \quad \forall s, t \in \mathbb{R}$$
"""
            },
            {
                "qid": "lac-q5",
                "marks": 7,
                "type": "Analytical Problem",
                "title": 'Homogeneous System Solution Space, Nullity, and Basis Determination',
                "yt_query": 'homogeneous system of linear equations nullity basis solution space',
                "img_path": "",
                "img_caption": "",
                "answer": r"""
Consider the homogeneous system of three linear equations in three unknowns $x, y, z$:
$$x + 2y + 3z = 0$$
$$3x + 4y + 4z = 0$$
$$7x + 10y + 12z = 0$$

In matrix form, this is $AX = 0$, where:
$$A = \begin{bmatrix} 1 & 2 & 3 \\ 3 & 4 & 4 \\ 7 & 10 & 12 \end{bmatrix}, \quad X = \begin{bmatrix} x \\ y \\ z \end{bmatrix}, \quad 0 = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$$

**Step 1: Reduce Coefficient Matrix $A$ to Row Echelon Form**
Apply row operations $R_2 \to R_2 - 3R_1$ and $R_3 \to R_3 - 7R_1$:
$$R_2 - 3R_1 = [3 - 3(1), \; 4 - 3(2), \; 4 - 3(3)] = [0, \; 4 - 6, \; 4 - 9] = [0, \; -2, \; -5]$$
$$R_3 - 7R_1 = [7 - 7(1), \; 10 - 7(2), \; 12 - 7(3)] = [0, \; 10 - 14, \; 12 - 21] = [0, \; -4, \; -9]$$

Matrix $A$ becomes:
$$A \sim \begin{bmatrix} 1 & 2 & 3 \\ 0 & -2 & -5 \\ 0 & -4 & -9 \end{bmatrix}$$

Next, eliminate the entry in row 3, column 2 using $R_3 \to R_3 - 2R_2$:
$$R_3 - 2R_2 = [0 - 2(0), \; -4 - 2(-2), \; -9 - 2(-5)] = [0, \; 0, \; -9 + 10] = [0, \; 0, \; 1]$$

The row echelon form of $A$ is:
$$U = \begin{bmatrix} 1 & 2 & 3 \\ 0 & -2 & -5 \\ 0 & 0 & 1 \end{bmatrix}$$

**Step 2: Determine Rank, Nullity, and Solution Type**
Counting non-zero rows in $U$:
$$\operatorname{rank}(A) = 3$$
The number of unknowns is $n = 3$.
By the fundamental **Rank-Nullity Theorem**:
$$\operatorname{Nullity}(A) = n - \operatorname{rank}(A) = 3 - 3 = 0$$

Because $\operatorname{rank}(A) = n = 3$, the columns of $A$ are linearly independent and $\det(A) \neq 0$.
A homogeneous system $AX = 0$ possesses non-trivial solutions if and only if $\operatorname{rank}(A) < n$.
Since $\operatorname{rank}(A) = 3 = n$, the system has **ONLY the trivial solution**:
$$x = 0, \quad y = 0, \quad z = 0$$

Let us confirm this via back-substitution:
From Row 3: $1z = 0 \implies z = 0$.
From Row 2: $-2y - 5z = 0 \implies -2y - 5(0) = 0 \implies y = 0$.
From Row 1: $x + 2y + 3z = 0 \implies x + 2(0) + 3(0) = 0 \implies x = 0$.

**Step 3: Basis and Dimension of the Solution Space**
The solution space (null space $\operatorname{Null}(A)$) contains only the zero vector:
$$\operatorname{Null}(A) = \left\{ \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix} \right\}$$
The dimension of the solution space is its nullity:
$$\operatorname{dim}(\operatorname{Null}(A)) = 0$$
By standard mathematical definition in linear vector spaces, the zero vector subspace $\{0\}$ has no linearly independent vectors. Hence, the basis of this solution space is the **empty set** $\emptyset$.
"""
            },
        ]
    },
    {
        "module_id": "lac-m2",
        "module_num": "Module 2",
        "module_title": "Eigenvalues, Cayley-Hamilton Theorem & Diagonalisation of Symmetric Matrices",
        "questions": [
            {
                "qid": "lac-q6",
                "marks": 3,
                "type": "Short Answer",
                "title": 'Cayley-Hamilton Theorem Application to Inverse and Higher Powers',
                "yt_query": 'cayley hamilton theorem matrix inverse higher power engineering mathematics',
                "img_path": "",
                "img_caption": "",
                "answer": r"""
The **Cayley-Hamilton theorem** is one of the most powerful foundational theorems in linear algebra. It states that every square matrix satisfies its own characteristic equation. That is, if $A$ is an $n \times n$ matrix with characteristic polynomial equation:
$$p(\lambda) = \det(A - \lambda I) = (-1)^n \lambda^n + c_{n-1} \lambda^{n-1} + \dots + c_1 \lambda + c_0 = 0$$
then substituting the matrix $A$ in place of the scalar variable $\lambda$ and replacing the scalar constant $c_0$ with the scalar multiple of the identity matrix $c_0 I$ yields the zero matrix $O$:
$$p(A) = (-1)^n A^n + c_{n-1} A^{n-1} + \dots + c_1 A + c_0 I = O$$

Let us apply this theorem to the $2 \times 2$ matrix $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$.

**Step 1: Determine the Characteristic Equation of $A$**
$$\det(A - \lambda I) = \begin{vmatrix} 1 - \lambda & 2 \\ 3 & 4 - \lambda \end{vmatrix} = 0$$
$$(1 - \lambda)(4 - \lambda) - (2)(3) = 0$$
$$\lambda^2 - 5\lambda + 4 - 6 = 0 \implies \lambda^2 - 5\lambda - 2 = 0$$

**Step 2: Apply Cayley-Hamilton Theorem**
By the Cayley-Hamilton theorem, $A$ satisfies this scalar polynomial:
$$A^2 - 5A - 2I = O$$

**Step 3: Compute $A^{-1}$**
Since $\det(A) = (1)(4) - (2)(3) = -2 \neq 0$, $A^{-1}$ exists. Premultiply the matrix equation by $A^{-1}$:
$$A^{-1}(A^2 - 5A - 2I) = A^{-1} O$$
$$A - 5I - 2A^{-1} = O \implies 2A^{-1} = A - 5I \implies A^{-1} = \frac{1}{2}(A - 5I)$$

Now compute the matrix difference $A - 5I$:
$$A - 5I = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} - \begin{bmatrix} 5 & 0 \\ 0 & 5 \end{bmatrix} = \begin{bmatrix} 1 - 5 & 2 - 0 \\ 3 - 0 & 4 - 5 \end{bmatrix} = \begin{bmatrix} -4 & 2 \\ 3 & -1 \end{bmatrix}$$
Therefore:
$$A^{-1} = \frac{1}{2}\begin{bmatrix} -4 & 2 \\ 3 & -1 \end{bmatrix} = \begin{bmatrix} -2 & 1 \\ 3/2 & -1/2 \end{bmatrix}$$

**Step 4: Compute $A^3$**
From the Cayley-Hamilton equation, express $A^2$ as a linear combination of lower degree matrices:
$$A^2 = 5A + 2I$$
Multiply both sides by $A$:
$$A^3 = A \cdot A^2 = A(5A + 2I) = 5A^2 + 2A$$
Substitute $A^2 = 5A + 2I$ into this expression:
$$A^3 = 5(5A + 2I) + 2A = 25A + 10I + 2A = 27A + 10I$$

Now substitute the numerical values of $A$ and $I$:
$$27A = 27 \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} = \begin{bmatrix} 27 & 54 \\ 81 & 108 \end{bmatrix}$$
$$10I = \begin{bmatrix} 10 & 0 \\ 0 & 10 \end{bmatrix}$$
Summing the matrices gives:
$$A^3 = \begin{bmatrix} 27 + 10 & 54 + 0 \\ 81 + 0 & 108 + 10 \end{bmatrix} = \begin{bmatrix} 37 & 54 \\ 81 & 118 \end{bmatrix}$$
"""
            },
            {
                "qid": "lac-q7",
                "marks": 3,
                "type": "Short Answer",
                "title": 'Eigenvalues, Eigenvectors, and Orthogonality of Symmetric Matrices',
                "yt_query": 'eigenvalues eigenvectors orthogonal verification symmetric matrix',
                "img_path": "",
                "img_caption": "",
                "answer": r"""
Let us determine the eigenvalues and corresponding eigenvectors of the real symmetric matrix:
$$A = \begin{bmatrix} 3 & 1 \\ 1 & 3 \end{bmatrix}$$
and verify that the eigenvectors associated with distinct eigenvalues are mutually orthogonal.

**Step 1: Find the Eigenvalues**
The characteristic equation of $A$ is given by $\det(A - \lambda I) = 0$:
$$\det\begin{bmatrix} 3 - \lambda & 1 \\ 1 & 3 - \lambda \end{bmatrix} = (3 - \lambda)^2 - 1 = 0$$
$$\lambda^2 - 6\lambda + 9 - 1 = 0 \implies \lambda^2 - 6\lambda + 8 = 0$$
$$(\lambda - 4)(\lambda - 2) = 0 \implies \lambda_1 = 4, \quad \lambda_2 = 2$$
The eigenvalues are distinct real numbers: $\lambda_1 = 4$ and $\lambda_2 = 2$.

**Step 2: Find the Eigenvector for $\lambda_1 = 4$**
The eigenvector $X_1 = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$ satisfies $(A - 4I)X_1 = 0$:
$$\begin{bmatrix} 3 - 4 & 1 \\ 1 & 3 - 4 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \implies \begin{bmatrix} -1 & 1 \\ 1 & -1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$
Both rows represent the single scalar equation:
$$-x_1 + x_2 = 0 \implies x_1 = x_2$$
Choosing the non-zero parameter $x_1 = 1$, we obtain $x_2 = 1$. Thus:
$$X_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$$

**Step 3: Find the Eigenvector for $\lambda_2 = 2$**
The eigenvector $X_2 = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$ satisfies $(A - 2I)X_2 = 0$:
$$\begin{bmatrix} 3 - 2 & 1 \\ 1 & 3 - 2 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \implies \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$
Both rows represent the scalar equation:
$$x_1 + x_2 = 0 \implies x_2 = -x_1$$
Choosing $x_1 = 1$, we obtain $x_2 = -1$. Thus:
$$X_2 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$$

**Step 4: Verify Orthogonality of Eigenvectors**
Two vectors in $\mathbb{R}^n$ are orthogonal if their inner (dot) product is zero. Let us compute the inner product $X_1^T X_2$:
$$X_1^T X_2 = \begin{bmatrix} 1 & 1 \end{bmatrix} \begin{bmatrix} 1 \\ -1 \end{bmatrix} = (1)(1) + (1)(-1) = 1 - 1 = 0$$
Since $X_1^T X_2 = 0$, the eigenvectors $X_1$ and $X_2$ corresponding to the distinct eigenvalues $\lambda_1 = 4$ and $\lambda_2 = 2$ are **mutually orthogonal**. This verifies the universal spectral theorem for real symmetric matrices: eigenvectors corresponding to distinct eigenvalues are always mutually orthogonal.
"""
            },
            {
                "qid": "lac-q8",
                "marks": 7,
                "type": "Analytical Problem",
                "title": 'Complete Eigen-Analysis of 3x3 Matrix with Repeated Roots and Trace-Determinant Verification',
                "yt_query": 'eigenvalues eigenvectors 3x3 repeated roots trace determinant verification',
                "img_path": "",
                "img_caption": "",
                "answer": r"""
We consider the $3 \times 3$ real matrix:
$$A = \begin{bmatrix} 2 & 2 & 1 \\ 1 & 3 & 1 \\ 1 & 2 & 2 \end{bmatrix}$$

**Step 1: Characteristic Equation using Invariant Trace and Minor Coefficients**
The characteristic equation of a $3 \times 3$ matrix is given by:
$$\lambda^3 - s_1 \lambda^2 + s_2 \lambda - s_3 = 0$$
where:
1. $s_1 = \operatorname{tr}(A) = 2 + 3 + 2 = 7$.
2. $s_2 = \text{Sum of principal minors of } A = M_{11} + M_{22} + M_{33}$:
   $$M_{11} = \begin{vmatrix} 3 & 1 \\ 2 & 2 \end{vmatrix} = (3)(2) - (1)(2) = 6 - 2 = 4$$
   $$M_{22} = \begin{vmatrix} 2 & 1 \\ 1 & 2 \end{vmatrix} = (2)(2) - (1)(1) = 4 - 1 = 3$$
   $$M_{33} = \begin{vmatrix} 2 & 2 \\ 1 & 3 \end{vmatrix} = (2)(3) - (2)(1) = 6 - 2 = 4$$
   $$s_2 = 4 + 3 + 4 = 11$$
3. $s_3 = \det(A)$:
   $$\det(A) = 2(6 - 2) - 2(2 - 1) + 1(2 - 3) = 2(4) - 2(1) + 1(-1) = 8 - 2 - 1 = 5$$

Hence the characteristic equation is:
$$\lambda^3 - 7\lambda^2 + 11\lambda - 5 = 0$$

Testing integer factors of $5$ ($\pm 1, \pm 5$):
For $\lambda = 1$:
$$1^3 - 7(1^2) + 11(1) - 5 = 1 - 7 + 11 - 5 = 0$$
Thus $(\lambda - 1)$ is a factor. Dividing $\lambda^3 - 7\lambda^2 + 11\lambda - 5$ by $(\lambda - 1)$:
$$(\lambda - 1)(\lambda^2 - 6\lambda + 5) = 0 \implies (\lambda - 1)(\lambda - 1)(\lambda - 5) = 0$$
The eigenvalues of $A$ are:
$$\lambda_1 = 5, \quad \lambda_2 = 1, \quad \lambda_3 = 1$$

**Step 2: Verification of Trace and Determinant Properties**
- **Sum of eigenvalues:**
  $$\sum_{i=1}^3 \lambda_i = 5 + 1 + 1 = 7 = \operatorname{tr}(A)$$
  This precisely matches the trace of $A$ ($2 + 3 + 2 = 7$).
- **Product of eigenvalues:**
  $$\prod_{i=1}^3 \lambda_i = (5)(1)(1) = 5 = \det(A)$$
  This precisely matches the determinant of $A$ ($\det(A) = 5$). Both properties are fully verified.

**Step 3: Eigenvector for $\lambda_1 = 5$**
Solve $(A - 5I)X = 0$:
$$\begin{bmatrix} 2 - 5 & 2 & 1 \\ 1 & 3 - 5 & 1 \\ 1 & 2 & 2 - 5 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix} \implies \begin{bmatrix} -3 & 2 & 1 \\ 1 & -2 & 1 \\ 1 & 2 & -3 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$$
Taking the first two rows and applying the cross-multiplication rule:
$$-3x_1 + 2x_2 + x_3 = 0$$
$$x_1 - 2x_2 + x_3 = 0$$
$$\frac{x_1}{(2)(1) - (1)(-2)} = \frac{-x_2}{(-3)(1) - (1)(1)} = \frac{x_3}{(-3)(-2) - (2)(1)}$$
$$\frac{x_1}{2 + 2} = \frac{-x_2}{-3 - 1} = \frac{x_3}{6 - 2} \implies \frac{x_1}{4} = \frac{x_2}{4} = \frac{x_3}{4} \implies \frac{x_1}{1} = \frac{x_2}{1} = \frac{x_3}{1}$$
Hence the eigenvector corresponding to $\lambda_1 = 5$ is:
$$X_1 = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$$

**Step 4: Eigenvectors for Repeated Root $\lambda_2 = \lambda_3 = 1$**
Solve $(A - I)X = 0$:
$$\begin{bmatrix} 2 - 1 & 2 & 1 \\ 1 & 3 - 1 & 1 \\ 1 & 2 & 2 - 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix} \implies \begin{bmatrix} 1 & 2 & 1 \\ 1 & 2 & 1 \\ 1 & 2 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$$
All three rows are completely identical. They reduce to a single linear equation:
$$x_1 + 2x_2 + x_3 = 0 \implies x_1 = -2x_2 - x_3$$
Since $\operatorname{rank}(A - I) = 1$, the geometric multiplicity (nullity) is:
$$n - \operatorname{rank}(A - I) = 3 - 1 = 2$$
This guarantees the existence of two linearly independent eigenvectors.

1. Set $x_2 = 1, x_3 = 0 \implies x_1 = -2(1) - 0 = -2$:
   $$X_2 = \begin{bmatrix} -2 \\ 1 \\ 0 \end{bmatrix}$$
2. Set $x_2 = 0, x_3 = 1 \implies x_1 = -2(0) - 1 = -1$:
   $$X_3 = \begin{bmatrix} -1 \\ 0 \\ 1 \end{bmatrix}$$

Thus, the repeated eigenvalue $\lambda = 1$ possesses two linearly independent eigenvectors $X_2$ and $X_3$.
"""
            },
            {
                "qid": "lac-q9",
                "marks": 7,
                "type": "Analytical Problem",
                "title": 'Cayley-Hamilton Verification for 3x3 Matrix and Derivation of A^(-1) and A^4',
                "yt_query": 'verify cayley hamilton theorem 3x3 matrix compute inverse and A4',
                "img_path": "",
                "img_caption": "",
                "answer": r"""
We consider the $3 \times 3$ matrix:
$$A = \begin{bmatrix} 1 & 0 & 3 \\ 2 & 1 & -1 \\ 1 & -1 & 1 \end{bmatrix}$$

**Step 1: Obtain the Characteristic Polynomial**
The characteristic polynomial is $\det(A - \lambda I) = \lambda^3 - s_1 \lambda^2 + s_2 \lambda - s_3 = 0$:
1. $s_1 = \operatorname{tr}(A) = 1 + 1 + 1 = 3$.
2. $s_2 = M_{11} + M_{22} + M_{33}$:
   $$M_{11} = \begin{vmatrix} 1 & -1 \\ -1 & 1 \end{vmatrix} = 1 - 1 = 0$$
   $$M_{22} = \begin{vmatrix} 1 & 3 \\ 1 & 1 \end{vmatrix} = 1 - 3 = -2$$
   $$M_{33} = \begin{vmatrix} 1 & 0 \\ 2 & 1 \end{vmatrix} = 1 - 0 = 1$$
   $$s_2 = 0 + (-2) + 1 = -1$$
3. $s_3 = \det(A)$:
   $$\det(A) = 1(1 - 1) - 0 + 3(-2 - 1) = 1(0) - 0 + 3(-3) = -9$$

Thus the characteristic equation is:
$$\lambda^3 - 3\lambda^2 - \lambda + 9 = 0$$

**Step 2: Explicit Verification of Cayley-Hamilton Theorem**
We must prove that $A^3 - 3A^2 - A + 9I = O$. First compute $A^2$:
$$A^2 = \begin{bmatrix} 1 & 0 & 3 \\ 2 & 1 & -1 \\ 1 & -1 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 & 3 \\ 2 & 1 & -1 \\ 1 & -1 & 1 \end{bmatrix} = \begin{bmatrix} 1(1)+0+3(1) & 1(0)+0-3(1) & 1(3)+0+3(1) \\ 2(1)+1(2)-1(1) & 0+1(1)-1(-1) & 2(3)+1(-1)-1(1) \\ 1(1)-1(2)+1(1) & 0-1(1)+1(-1) & 1(3)-1(-1)+1(1) \end{bmatrix} = \begin{bmatrix} 4 & -3 & 6 \\ 3 & 2 & 4 \\ 0 & -2 & 5 \end{bmatrix}$$

Next compute $A^3 = A^2 \cdot A$:
$$A^3 = \begin{bmatrix} 4 & -3 & 6 \\ 3 & 2 & 4 \\ 0 & -2 & 5 \end{bmatrix} \begin{bmatrix} 1 & 0 & 3 \\ 2 & 1 & -1 \\ 1 & -1 & 1 \end{bmatrix} = \begin{bmatrix} 4-6+6 & 0-3-6 & 12+3+6 \\ 3+4+4 & 0+2-4 & 9-2+4 \\ 0-4+5 & 0-2-5 & 0+2+5 \end{bmatrix} = \begin{bmatrix} 4 & -9 & 21 \\ 11 & -2 & 11 \\ 1 & -7 & 7 \end{bmatrix}$$

Now evaluate $A^3 - 3A^2 - A + 9I$:
$$-3A^2 = \begin{bmatrix} -12 & 9 & -18 \\ -9 & -6 & -12 \\ 0 & 6 & -15 \end{bmatrix}, \quad -A = \begin{bmatrix} -1 & 0 & -3 \\ -2 & -1 & 1 \\ -1 & 1 & -1 \end{bmatrix}, \quad 9I = \begin{bmatrix} 9 & 0 & 0 \\ 0 & 9 & 0 \\ 0 & 0 & 9 \end{bmatrix}$$
Summing all four matrices term-by-term:
- Row 1:
  - $(1,1): 4 - 12 - 1 + 9 = 0$
  - $(1,2): -9 + 9 + 0 + 0 = 0$
  - $(1,3): 21 - 18 - 3 + 0 = 0$
- Row 2:
  - $(2,1): 11 - 9 - 2 + 0 = 0$
  - $(2,2): -2 - 6 - 1 + 9 = 0$
  - $(2,3): 11 - 12 + 1 + 0 = 0$
- Row 3:
  - $(3,1): 1 + 0 - 1 + 0 = 0$
  - $(3,2): -7 + 6 + 1 + 0 = 0$
  - $(3,3): 7 - 15 - 1 + 9 = 0$

$$A^3 - 3A^2 - A + 9I = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix} = O$$
Cayley-Hamilton theorem is verified.

**Step 3: Compute $A^{-1}$**
From $A^3 - 3A^2 - A + 9I = O$, multiply by $A^{-1}$:
$$A^2 - 3A - I + 9A^{-1} = O \implies 9A^{-1} = -A^2 + 3A + I$$
$$A^{-1} = \frac{1}{9}(-A^2 + 3A + I)$$
Calculate $-A^2 + 3A + I$:
$$-A^2 = \begin{bmatrix} -4 & 3 & -6 \\ -3 & -2 & -4 \\ 0 & 2 & -5 \end{bmatrix}, \quad 3A = \begin{bmatrix} 3 & 0 & 9 \\ 6 & 3 & -3 \\ 3 & -3 & 3 \end{bmatrix}, \quad I = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$
Summing:
$$-A^2 + 3A + I = \begin{bmatrix} -4+3+1 & 3+0+0 & -6+9+0 \\ -3+6+0 & -2+3+1 & -4-3+0 \\ 0+3+0 & 2-3+0 & -5+3+1 \end{bmatrix} = \begin{bmatrix} 0 & 3 & 3 \\ 3 & 2 & -7 \\ 3 & -1 & -1 \end{bmatrix}$$
Therefore:
$$A^{-1} = \frac{1}{9}\begin{bmatrix} 0 & 3 & 3 \\ 3 & 2 & -7 \\ 3 & -1 & -1 \end{bmatrix}$$

**Step 4: Compute $A^4$**
Express $A^3 = 3A^2 + A - 9I$. Multiply by $A$:
$$A^4 = A \cdot A^3 = A(3A^2 + A - 9I) = 3A^3 + A^2 - 9A$$
Substitute $A^3 = 3A^2 + A - 9I$:
$$A^4 = 3(3A^2 + A - 9I) + A^2 - 9A = 9A^2 + 3A - 27I + A^2 - 9A = 10A^2 - 6A - 27I$$

Calculate each term:
$$10A^2 = 10\begin{bmatrix} 4 & -3 & 6 \\ 3 & 2 & 4 \\ 0 & -2 & 5 \end{bmatrix} = \begin{bmatrix} 40 & -30 & 60 \\ 30 & 20 & 40 \\ 0 & -20 & 50 \end{bmatrix}$$
$$-6A = -6\begin{bmatrix} 1 & 0 & 3 \\ 2 & 1 & -1 \\ 1 & -1 & 1 \end{bmatrix} = \begin{bmatrix} -6 & 0 & -18 \\ -12 & -6 & 6 \\ -6 & 6 & -6 \end{bmatrix}$$
$$-27I = \begin{bmatrix} -27 & 0 & 0 \\ 0 & -27 & 0 \\ 0 & 0 & -27 \end{bmatrix}$$

Summing all three matrices:
$$A^4 = \begin{bmatrix} 40 - 6 - 27 & -30 + 0 + 0 & 60 - 18 + 0 \\ 30 - 12 + 0 & 20 - 6 - 27 & 40 + 6 + 0 \\ 0 - 6 + 0 & -20 + 6 + 0 & 50 - 6 - 27 \end{bmatrix} = \begin{bmatrix} 7 & -30 & 42 \\ 18 & -13 & 46 \\ -6 & -14 & 17 \end{bmatrix}$$
"""
            },
            {
                "qid": "lac-q10",
                "marks": 7,
                "type": "Analytical Problem",
                "title": 'Orthogonal Diagonalisation of Symmetric Matrix and Quadratic Form Reduction',
                "yt_query": 'orthogonal diagonalisation quadratic form canonical form rank index signature definiteness',
                "img_path": "",
                "img_caption": "",
                "answer": r"""
We consider the real symmetric matrix:
$$A = \begin{bmatrix} 6 & -2 & 2 \\ -2 & 3 & -1 \\ 2 & -1 & 3 \end{bmatrix}$$
associated with the quadratic form:
$$Q = 6x^2 + 3y^2 + 3z^2 - 4xy + 4xz - 2yz$$

**Step 1: Characteristic Equation and Eigenvalues**
The characteristic equation is $\lambda^3 - s_1 \lambda^2 + s_2 \lambda - s_3 = 0$:
1. $s_1 = \operatorname{tr}(A) = 6 + 3 + 3 = 12$.
2. $s_2 = M_{11} + M_{22} + M_{33}$:
   $$M_{11} = (3)(3) - (-1)(-1) = 9 - 1 = 8$$
   $$M_{22} = (6)(3) - (2)(2) = 18 - 4 = 14$$
   $$M_{33} = (6)(3) - (-2)(-2) = 18 - 4 = 14$$
   $$s_2 = 8 + 14 + 14 = 36$$
3. $s_3 = \det(A)$:
   $$\det(A) = 6(9 - 1) - (-2)(-6 + 2) + 2(2 - 6) = 6(8) + 2(-4) + 2(-4) = 48 - 8 - 8 = 32$$

Characteristic equation:
$$\lambda^3 - 12\lambda^2 + 36\lambda - 32 = 0$$
Testing integer roots: $\lambda = 2 \implies 2^3 - 12(4) + 36(2) - 32 = 8 - 48 + 72 - 32 = 0$.
Factorizing:
$$(\lambda - 2)(\lambda^2 - 10\lambda + 16) = 0 \implies (\lambda - 2)(\lambda - 2)(\lambda - 8) = 0$$
The eigenvalues are $\lambda_1 = 8, \lambda_2 = 2, \lambda_3 = 2$.

**Step 2: Eigenvector for $\lambda_1 = 8$**
Solve $(A - 8I)X = 0$:
$$\begin{bmatrix} -2 & -2 & 2 \\ -2 & -5 & -1 \\ 2 & -1 & -5 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$$
Using rows 1 and 2:
$$-2x_1 - 2x_2 + 2x_3 = 0 \implies x_1 + x_2 - x_3 = 0$$
$$-2x_1 - 5x_2 - x_3 = 0 \implies 2x_1 + 5x_2 + x_3 = 0$$
Applying cross multiplication:
$$\frac{x_1}{(1)(1) - (-1)(5)} = \frac{-x_2}{(1)(1) - (-1)(2)} = \frac{x_3}{(1)(5) - (1)(2)}$$
$$\frac{x_1}{1 + 5} = \frac{-x_2}{1 + 2} = \frac{x_3}{5 - 2} \implies \frac{x_1}{6} = \frac{-x_2}{3} = \frac{x_3}{3} \implies \frac{x_1}{2} = \frac{x_2}{-1} = \frac{x_3}{1}$$
$$X_1 = \begin{bmatrix} 2 \\ -1 \\ 1 \end{bmatrix}, \quad \|X_1\| = \sqrt{2^2 + (-1)^2 + 1^2} = \sqrt{6}$$
Normalized eigenvector:
$$u_1 = \frac{1}{\sqrt{6}}\begin{bmatrix} 2 \\ -1 \\ 1 \end{bmatrix}$$

**Step 3: Eigenvectors for Repeated Eigenvalue $\lambda = 2$**
Solve $(A - 2I)X = 0$:
$$\begin{bmatrix} 4 & -2 & 2 \\ -2 & 1 & -1 \\ 2 & -1 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$$
All three rows reduce to the single plane equation:
$$2x_1 - x_2 + x_3 = 0 \implies x_2 = 2x_1 + x_3$$
Choose $x_1 = 0, x_3 = 1 \implies x_2 = 1$:
$$X_2 = \begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix}, \quad \|X_2\| = \sqrt{0^2 + 1^2 + 1^2} = \sqrt{2}$$
Normalized eigenvector:
$$u_2 = \frac{1}{\sqrt{2}}\begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix}$$

Now find $X_3 = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}$ such that it lies in the plane $2x_1 - x_2 + x_3 = 0$ AND is orthogonal to $X_2$:
$$X_2^T X_3 = 0 \implies 0x_1 + 1x_2 + 1x_3 = 0 \implies x_2 + x_3 = 0 \implies x_3 = -x_2$$
Substitute $x_3 = -x_2$ into $2x_1 - x_2 + x_3 = 0$:
$$2x_1 - x_2 - x_2 = 0 \implies 2x_1 - 2x_2 = 0 \implies x_1 = x_2$$
Choose $x_1 = 1 \implies x_2 = 1, x_3 = -1$:
$$X_3 = \begin{bmatrix} 1 \\ 1 \\ -1 \end{bmatrix}, \quad \|X_3\| = \sqrt{1^2 + 1^2 + (-1)^2} = \sqrt{3}$$
Normalized eigenvector:
$$u_3 = \frac{1}{\sqrt{3}}\begin{bmatrix} 1 \\ 1 \\ -1 \end{bmatrix}$$

**Step 4: Form Orthogonal Matrix $P$**
The modal matrix $P = [u_1 \; u_2 \; u_3]$ is:
$$P = \begin{bmatrix} 2/\sqrt{6} & 0 & 1/\sqrt{3} \\ -1/\sqrt{6} & 1/\sqrt{2} & 1/\sqrt{3} \\ 1/\sqrt{6} & 1/\sqrt{2} & -1/\sqrt{3} \end{bmatrix}$$
Since columns are orthonormal, $P$ is an orthogonal matrix ($P^T = P^{-1}$), and:
$$P^T A P = D = \begin{bmatrix} 8 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 2 \end{bmatrix}$$

**Step 5: Canonical Form and Properties**
Under the orthogonal coordinate transformation $X = P Y$ where $Y = [y_1, y_2, y_3]^T$:
$$Q = X^T A X = (PY)^T A (PY) = Y^T (P^T A P) Y = Y^T D Y$$
$$Q = 8y_1^2 + 2y_2^2 + 2y_3^2$$

- **Rank ($r$):** Number of non-zero terms in the canonical form = 3.
- **Index ($p$):** Number of positive terms in the canonical form = 3.
- **Signature ($s$):** Positive terms minus negative terms = $2p - r = 2(3) - 3 = 3$.
- **Nature / Definiteness:** All eigenvalues $\lambda_1 = 8, \lambda_2 = 2, \lambda_3 = 2$ are strictly positive ($> 0$). Therefore, the quadratic form $Q$ is **Strictly Positive Definite**.
"""
            },
        ]
    },
    {
        "module_id": "lac-m3",
        "module_num": "Module 3",
        "module_title": "Calculus of Single Variable, Taylor Series & Indeterminate Forms",
        "questions": [
            {
                "qid": "lac-q11",
                "marks": 3,
                "type": "Short Answer",
                "title": "Evaluation of Indeterminate Form 0/0 via L'Hopital's Rule and Series Expansion",
                "yt_query": 'limit x minus sin x over x cubed lhopital rule taylor series engineering mathematics',
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
                "title": 'Concavity, Convexity, and Points of Inflection Analysis',
                "yt_query": 'intervals of concavity points of inflection second derivative test engineering mathematics',
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
                "title": 'Evaluation of Exponential (infinity^0) and Difference (infinity - infinity) Indeterminate Forms',
                "yt_query": 'indeterminate forms infinity to power 0 infinity minus infinity lhopital rule',
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
                "title": 'Taylor Series Expansion of Logarithmic Cosine and Numerical Approximation',
                "yt_query": 'taylor series ln cos x about 0 maclaurin expansion approximation',
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
                "title": 'Maclaurin Series Expansion of Composite Product Function and Derivative Deduction',
                "yt_query": 'maclaurin series e^x cos x product of series fourth derivative deduction',
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
            },
        ]
    },
    {
        "module_id": "lac-m4",
        "module_num": "Module 4",
        "module_title": "Multivariable Differential Calculus, Partial Derivatives & Optimization",
        "questions": [
            {
                "qid": "lac-q16",
                "marks": 3,
                "type": "Short Answer",
                "title": "Euler's Theorem on Homogeneous Functions Applied to Implicit Functions",
                "yt_query": 'eulers theorem homogeneous functions multivariable calculus engineering mathematics',
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
                "title": 'Coordinate Invariance of Gradient Magnitude in Polar Form',
                "yt_query": 'multivariable chain rule partial derivatives cartesian to polar gradient invariance',
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
                "yt_query": 'eulers theorem second order partial derivatives tan inverse homogeneous engineering mathematics',
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
                "title": 'Local Extrema and Saddle Points of Two-Variable Functions',
                "yt_query": 'maxima minima saddle points two variables hessian second derivative test',
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
                "title": 'Lagrange Multiplier Optimization for Maximal Inscribed Parallelepiped',
                "yt_query": 'maximum volume rectangular box inscribed in ellipsoid lagrange multipliers',
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
            },
        ]
    },
    {
        "module_id": "lac-m5",
        "module_num": "Module 5",
        "module_title": "Multiple Integrals, Polar Transformations & Volume Computation",
        "questions": [
            {
                "qid": "lac-q21",
                "marks": 3,
                "type": "Short Answer",
                "title": 'Double Integral Evaluation via Transformation to Polar Coordinates',
                "yt_query": 'evaluate double integral polar coordinates unit circle first quadrant',
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
                "title": 'Reversal of Order of Integration for Parabolic-Linear Enclosed Domain',
                "yt_query": 'change order of integration double integral parabola line engineering mathematics',
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
                "title": 'Improper Double Integral in Polar Form and Proof of the Gaussian Integral',
                "yt_query": 'gaussian integral evaluation using polar coordinates double integral e^-x^2',
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
                "title": 'Order of Integration Reversal and Evaluation of Rational Double Integral',
                "yt_query": 'change order of integration x over x^2 plus y^2 double integral',
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
                "title": 'Double Integral Area Computation Enclosed by Conjugate Parabolas',
                "yt_query": 'area bounded by parabolas y^2=4ax and x^2=4ay double integration',
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
                "title": 'Triple Integral Volume Determination of Truncated Right Circular Cylinder',
                "yt_query": 'volume bounded by cylinder x^2+y^2=4 planes y+z=4 z=0 triple integration',
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
            },
        ]
    },
]
