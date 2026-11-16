# -*- coding: utf-8 -*-
"""
Module 1 for Subject 1: Linear Algebra and Calculus (MAT101 / MATHS - LAC)
Linear Systems of Equations, Gauss Elimination & Rank
"""

M1_QUESTIONS = [
    {
        "qid": "lac-q1",
        "marks": 3,
        "type": "Short Answer",
        "title": "Consistency Criteria of Linear Systems: Rouché-Capelli Theorem",
        "yt_query": "consistency of system of linear equations rouche capelli theorem rank matrix",
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
        "title": "Row Echelon Form and Rank Determination by Row Reduction",
        "yt_query": "row echelon form of matrix rank reduction engineering mathematics",
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
        "title": "Consistency and Parametric Analysis of Linear System with Lambda and Mu",
        "yt_query": "values of lambda and mu for unique infinite no solution system of linear equations",
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
        "title": "Gauss Elimination and Complete Solution of Underdetermined System",
        "yt_query": "gauss elimination test consistency underdetermined system infinitely many solutions",
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
        "title": "Homogeneous System Solution Space, Nullity, and Basis Determination",
        "yt_query": "homogeneous system of linear equations nullity basis solution space",
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
    }
]

M1_BYHEART = {
    "lac-q1": {
        "eq": r'$$\operatorname{rank}(A) = \operatorname{rank}([A|B]) = r \implies \begin{cases} r = n & \text{Unique solution} \\ r < n & \text{Infinitely many solutions ($n-r$ free parameters)} \\ \operatorname{rank}(A) < \operatorname{rank}([A|B]) & \text{Inconsistent (No solution)} \end{cases}$$',
        "text": r'<strong>Rouché-Capelli Theorem:</strong> A linear system $AX = B$ is consistent iff $\operatorname{rank}(A) = \operatorname{rank}([A|B]) = r$. If $r = n$, unique solution; if $r < n$, infinitely many solutions with $n-r$ independent parameters; if $\operatorname{rank}(A) \ne \operatorname{rank}([A|B])$, no solution.'
    },
    "lac-q2": {
        "eq": r'$$U = \begin{bmatrix} 1 & 2 & -1 & 3 \\ 0 & 0 & 3 & -8 \\ 0 & 0 & 0 & 0 \end{bmatrix} \implies \operatorname{rank}(A) = \text{number of non-zero rows} = 2$$',
        "text": r'<strong>Row Echelon Form & Rank:</strong> Elementary row operations preserve the rank of a matrix. The rank equals the number of non-zero rows in the row echelon form.'
    },
    "lac-q3": {
        "eq": r'$$\begin{bmatrix} 1 & 1 & 1 & | & 6 \\ 0 & 1 & 2 & | & 4 \\ 0 & 0 & \lambda - 3 & | & \mu - 10 \end{bmatrix} \implies \begin{cases} \lambda = 3, \mu \ne 10 & \text{No solution} \\ \lambda \ne 3, \forall \mu & \text{Unique solution} \\ \lambda = 3, \mu = 10 & \text{Infinite solutions} \end{cases}$$',
        "text": r'<strong>Consistency Analysis with Parameters:</strong> At $\lambda = 3$, row 3 of $A$ vanishes. If $\mu \ne 10$, augmented matrix has rank 3 while $A$ has rank 2 (inconsistent). If $\mu = 10$, both ranks are 2 (infinitely many solutions). If $\lambda \ne 3$, rank is 3 for any $\mu$ (unique solution).'
    },
    "lac-q4": {
        "eq": r'$$\operatorname{rank}(A) = \operatorname{rank}([A|B]) = 2 < n=4 \implies X = \begin{bmatrix} 7/5 \\ 1/5 \\ 0 \\ 0 \end{bmatrix} + s \begin{bmatrix} -17/5 \\ -6/5 \\ 1 \\ 0 \end{bmatrix} + t \begin{bmatrix} 8/5 \\ -6/5 \\ 0 \\ 1 \end{bmatrix}$$',
        "text": r'<strong>Gauss Elimination Free Parameters:</strong> When $r < n$, the solution space is an affine subspace with dimension $n - r$. The variables corresponding to non-pivot columns become arbitrary parameters $s, t \in \mathbb{R}$.'
    },
    "lac-q5": {
        "eq": r'$$\operatorname{rank}(A) = 3 = n \implies \operatorname{Nullity}(A) = n - r = 3 - 3 = 0 \implies X = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix} \text{ (Trivial solution only)}$$',
        "text": r'<strong>Homogeneous System & Rank-Nullity:</strong> A homogeneous system $AX = 0$ possesses non-trivial solutions if and only if $\det(A) = 0$ ($\operatorname{rank}(A) < n$). When $\operatorname{rank}(A) = n$, the null space is trivial and contains only the origin.'
    }
}
