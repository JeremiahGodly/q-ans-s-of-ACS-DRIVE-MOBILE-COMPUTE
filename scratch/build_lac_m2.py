# -*- coding: utf-8 -*-
"""
Module 2 for Subject 1: Linear Algebra and Calculus (MAT101 / MATHS - LAC)
Eigenvalues, Cayley-Hamilton Theorem & Diagonalisation of Symmetric Matrices
"""

M2_QUESTIONS = [
    {
        "qid": "lac-q6",
        "marks": 3,
        "type": "Short Answer",
        "title": "Cayley-Hamilton Theorem Application to Inverse and Higher Powers",
        "yt_query": "cayley hamilton theorem matrix inverse higher power engineering mathematics",
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
        "title": "Eigenvalues, Eigenvectors, and Orthogonality of Symmetric Matrices",
        "yt_query": "eigenvalues eigenvectors orthogonal verification symmetric matrix",
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
        "title": "Complete Eigen-Analysis of 3x3 Matrix with Repeated Roots and Trace-Determinant Verification",
        "yt_query": "eigenvalues eigenvectors 3x3 repeated roots trace determinant verification",
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
        "title": "Cayley-Hamilton Verification for 3x3 Matrix and Derivation of A^(-1) and A^4",
        "yt_query": "verify cayley hamilton theorem 3x3 matrix compute inverse and A4",
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
        "title": "Orthogonal Diagonalisation of Symmetric Matrix and Quadratic Form Reduction",
        "yt_query": "orthogonal diagonalisation quadratic form canonical form rank index signature definiteness",
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
    }
]

M2_BYHEART = {
    "lac-q6": {
        "eq": r'$$A^2 - 5A - 2I = O \implies A^{-1} = \frac{1}{2}(A - 5I) = \begin{bmatrix} -2 & 1 \\ 1.5 & -0.5 \end{bmatrix}, \quad A^3 = 27A + 10I = \begin{bmatrix} 37 & 54 \\ 81 & 118 \end{bmatrix}$$',
        "text": r'<strong>Cayley-Hamilton Theorem:</strong> Every square matrix satisfies $\det(A - \lambda I) = 0$. Premultiplying or postmultiplying the matrix polynomial by $A^{-1}$ enables direct calculation of matrix inverse and high powers without determinants.'
    },
    "lac-q7": {
        "eq": r'$$\lambda_1 = 4 \implies X_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}, \quad \lambda_2 = 2 \implies X_2 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}, \quad X_1^T X_2 = 1 - 1 = 0$$',
        "text": r'<strong>Orthogonality of Real Symmetric Matrix Eigenvectors:</strong> Eigenvectors of any real symmetric matrix associated with distinct eigenvalues are strictly orthogonal: $X_i^T X_j = 0$ for $\lambda_i \ne \lambda_j$.'
    },
    "lac-q8": {
        "eq": r'$$\lambda = 5, 1, 1 \implies \sum \lambda_i = 7 = \operatorname{tr}(A), \quad \prod \lambda_i = 5 = \det(A); \quad X_{\lambda=5} = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}, X_{\lambda=1} = \left\{ \begin{bmatrix} -2 \\ 1 \\ 0 \end{bmatrix}, \begin{bmatrix} -1 \\ 0 \\ 1 \end{bmatrix} \right\}$$',
        "text": r'<strong>Eigenvalue Properties & Multiplicity:</strong> Sum of eigenvalues equals the matrix trace, and product equals the determinant. For repeated eigenvalues, geometric multiplicity equals the nullity $n - \operatorname{rank}(A - \lambda I)$.'
    },
    "lac-q9": {
        "eq": r'$$A^3 - 3A^2 - A + 9I = O \implies A^{-1} = \frac{1}{9}\begin{bmatrix} 0 & 3 & 3 \\ 3 & 2 & -7 \\ 3 & -1 & -1 \end{bmatrix}, \quad A^4 = 10A^2 - 6A - 27I$$',
        "text": r'<strong>Matrix Inverse via Characteristic Equation:</strong> For $A^3 - s_1 A^2 + s_2 A - \det(A)I = O$, multiplying by $A^{-1}$ yields $A^{-1} = \frac{1}{\det(A)}(A^2 - s_1 A + s_2 I)$, bypassing matrix cofactors.'
    },
    "lac-q10": {
        "eq": r'$$Q = 8y_1^2 + 2y_2^2 + 2y_3^2, \quad \operatorname{rank} = 3, \quad \operatorname{index} = 3, \quad \operatorname{signature} = 3, \quad \text{Strictly Positive Definite}$$',
        "text": r'<strong>Orthogonal Diagonalisation & Quadratic Forms:</strong> Any real symmetric matrix $A$ can be diagonalised by an orthogonal matrix $P$ ($P^T A P = D$). Canonical form is $\sum \lambda_i y_i^2$. If all $\lambda_i > 0$, the quadratic form is strictly positive definite.'
    }
}
