# -*- coding: utf-8 -*-
"""
Assembler to write self-contained scratch/gen_maths_lac.py
"""

import sys
sys.path.append('scratch')
import build_lac_m1
import build_lac_m2
import build_lac_m3
import build_lac_m4
import build_lac_m5

def assemble():
    exam_questions = {
        "lac-q1": "State the conditions for consistency of a non-homogeneous system of linear equations AX = B in terms of ranks of the coefficient matrix and the augmented matrix using the Rouché-Capelli theorem. Explain when the system has a unique solution, infinitely many solutions, and no solution.",
        "lac-q2": "Define row echelon form of a matrix. Reduce the matrix A = [[1, 2, -1, 3], [2, 4, 1, -2], [3, 6, 3, -7]] to row echelon form and determine its rank.",
        "lac-q3": "Investigate for what values of lambda and mu the system of equations x + y + z = 6, x + 2y + 3z = 10, x + 2y + lambda*z = mu has: (i) no solution, (ii) a unique solution, and (iii) infinitely many solutions. Also find the solutions when lambda = 4, mu = 13 and when lambda = 3, mu = 10.",
        "lac-q4": "Test for consistency and solve the system of linear equations using Gauss elimination: x1 - 2x2 + x3 - 4x4 = 1, x1 + 3x2 + 7x3 + 2x4 = 2, x1 - 12x2 - 11x3 - 16x4 = -1.",
        "lac-q5": "Find the non-trivial solutions of the homogeneous system of equations: x + 2y + 3z = 0, 3x + 4y + 4z = 0, 7x + 10y + 12z = 0. Determine the basis and dimension (nullity) of the solution space.",
        "lac-q6": "State Cayley-Hamilton theorem. Use it to find A^(-1) and A^3 for the matrix A = [[1, 2], [3, 4]].",
        "lac-q7": "Find the eigenvalues and eigenvectors of the matrix A = [[3, 1], [1, 3]] and verify that the eigenvectors corresponding to distinct eigenvalues are mutually orthogonal.",
        "lac-q8": "Find the eigenvalues and eigenvectors of the 3x3 matrix A = [[2, 2, 1], [1, 3, 1], [1, 2, 2]]. Verify that the sum of the eigenvalues equals the trace of A and the product of the eigenvalues equals the determinant of A.",
        "lac-q9": "Verify Cayley-Hamilton theorem for the matrix A = [[1, 0, 3], [2, 1, -1], [1, -1, 1]] and hence compute A^(-1) and A^4.",
        "lac-q10": "Orthogonally diagonalise the symmetric matrix A = [[6, -2, 2], [-2, 3, -1], [2, -1, 3]]. Hence reduce the quadratic form Q = 6x^2 + 3y^2 + 3z^2 - 4xy + 4xz - 2yz into canonical form and determine its rank, index, signature, and nature.",
        "lac-q11": "Evaluate the limit lim_{x->0} (x - sin x) / x^3 using L'Hopital's rule, and verify the result using Maclaurin series expansion.",
        "lac-q12": "Determine the intervals of concavity, convexity, and points of inflection for the function f(x) = x^4 - 4x^3 + 10.",
        "lac-q13": "Evaluate the indeterminate forms: (i) lim_{x->0+} (cot x)^(sin x) (form infinity^0), and (ii) lim_{x->0} (1/x^2 - cot x / x) (form infinity - infinity).",
        "lac-q14": "Find the Taylor series expansion of f(x) = ln(cos x) about x = 0 up to the term containing x^4 and deduce an approximation for ln(cos 0.1).",
        "lac-q15": "Find the Maclaurin series expansion of f(x) = e^x cos x up to the term in x^4. Hence determine f^(4)(0) and calculate an approximate value for e^(0.1) cos(0.1).",
        "lac-q16": "State Euler's theorem on homogeneous functions. If u = sin^(-1)((x^2 + y^2)/(x + y)), prove that x du/dx + y du/dy = tan u.",
        "lac-q17": "If z = f(x, y) where x = r cos theta and y = r sin theta, show that (dz/dx)^2 + (dz/dy)^2 = (dz/dr)^2 + (1/r^2)(dz/d theta)^2.",
        "lac-q18": "If u = tan^(-1)((x^3 + y^3)/(x - y)), prove that: (i) x du/dx + y du/dy = sin 2u, and (ii) x^2 d^2u/dx^2 + 2xy d^2u/dxdy + y^2 d^2u/dy^2 = 2 cos 3u sin u.",
        "lac-q19": "Find all local maxima, local minima, and saddle points of the multivariable function f(x, y) = x^3 + 3xy^2 - 15x^2 - 15y^2 + 72x.",
        "lac-q20": "Find the maximum volume of a rectangular parallelepiped inscribed in the ellipsoid x^2/a^2 + y^2/b^2 + z^2/c^2 = 1 using Lagrange's method of undetermined multipliers.",
        "lac-q21": "Evaluate the double integral int_0^1 int_0^(sqrt(1-x^2)) (x^2 + y^2) dy dx by transforming into polar coordinates.",
        "lac-q22": "Change the order of integration in int_0^1 int_x^(sqrt(x)) f(x, y) dy dx.",
        "lac-q23": "Evaluate the improper double integral int_0^infinity int_0^infinity e^(-(x^2 + y^2)) dx dy by transforming into polar coordinates, and hence deduce the value of the Gaussian integral int_0^infinity e^(-x^2) dx = sqrt(pi)/2.",
        "lac-q24": "Change the order of integration and evaluate: int_0^a int_y^a x / (x^2 + y^2) dx dy.",
        "lac-q25": "Find the area bounded by the parabolas y^2 = 4ax and x^2 = 4ay using double integration.",
        "lac-q26": "Find the volume of the solid bounded by the cylinder x^2 + y^2 = 4 and the planes y + z = 4 and z = 0 using triple integration."
    }

    modules = [
        {
            "module_id": "lac-m1",
            "module_num": "Module 1",
            "module_title": "Linear Systems of Equations, Gauss Elimination & Rank",
            "questions": build_lac_m1.M1_QUESTIONS
        },
        {
            "module_id": "lac-m2",
            "module_num": "Module 2",
            "module_title": "Eigenvalues, Cayley-Hamilton Theorem & Diagonalisation of Symmetric Matrices",
            "questions": build_lac_m2.M2_QUESTIONS
        },
        {
            "module_id": "lac-m3",
            "module_num": "Module 3",
            "module_title": "Calculus of Single Variable, Taylor Series & Indeterminate Forms",
            "questions": build_lac_m3.M3_QUESTIONS
        },
        {
            "module_id": "lac-m4",
            "module_num": "Module 4",
            "module_title": "Multivariable Differential Calculus, Partial Derivatives & Optimization",
            "questions": build_lac_m4.M4_QUESTIONS
        },
        {
            "module_id": "lac-m5",
            "module_num": "Module 5",
            "module_title": "Multiple Integrals, Polar Transformations & Volume Computation",
            "questions": build_lac_m5.M5_QUESTIONS
        }
    ]

    byheart = {}
    byheart.update(build_lac_m1.M1_BYHEART)
    byheart.update(build_lac_m2.M2_BYHEART)
    byheart.update(build_lac_m3.M3_BYHEART)
    byheart.update(build_lac_m4.M4_BYHEART)
    byheart.update(build_lac_m5.M5_BYHEART)

    lines = []
    lines.append("# -*- coding: utf-8 -*-")
    lines.append('"""')
    lines.append("Content generator for Subject 1: Linear Algebra and Calculus (MAT101 / MATHS - LAC)")
    lines.append("KTU 2019 Scheme Electrical & Electronics Engineering (EEE) Question Bank.")
    lines.append("All answers written from the perspective of an experienced engineering mathematics professor.")
    lines.append("Contains complete step-by-step mathematical working, intermediate equations, and highlighted results.")
    lines.append("All strings use raw multiline strings to prevent any LaTeX escape corruptions.")
    lines.append("Equations use standard KaTeX syntax: $$...$$ for display equations, $...$ for inline math.")
    lines.append('"""\n')

    # MATHS_LAC_EXAM_QUESTIONS
    lines.append("MATHS_LAC_EXAM_QUESTIONS = {")
    for qid, qtext in exam_questions.items():
        lines.append(f'    "{qid}": {repr(qtext)},')
    lines.append("}\n")

    # MATHS_LAC_BYHEART
    lines.append("MATHS_LAC_BYHEART = {")
    for qid, bh in byheart.items():
        lines.append(f'    "{qid}": {{')
        lines.append(f'        "eq": r"""{bh["eq"]}""",')
        lines.append(f'        "text": r"""{bh["text"]}"""')
        lines.append("    },")
    lines.append("}\n")

    # MATHS_LAC_MODULES
    lines.append("MATHS_LAC_MODULES = [")
    for m in modules:
        lines.append("    {")
        lines.append(f'        "module_id": "{m["module_id"]}",')
        lines.append(f'        "module_num": "{m["module_num"]}",')
        lines.append(f'        "module_title": "{m["module_title"]}",')
        lines.append('        "questions": [')
        for q in m["questions"]:
            lines.append("            {")
            lines.append(f'                "qid": "{q["qid"]}",')
            lines.append(f'                "marks": {q["marks"]},')
            lines.append(f'                "type": "{q["type"]}",')
            lines.append(f'                "title": {repr(q["title"])},')
            lines.append(f'                "yt_query": {repr(q["yt_query"])},')
            lines.append(f'                "img_path": "{q["img_path"]}",')
            lines.append(f'                "img_caption": "{q["img_caption"]}",')
            lines.append(f'                "answer": r"""{q["answer"]}"""')
            lines.append("            },")
        lines.append("        ]")
        lines.append("    },")
    lines.append("]\n")

    content = '\n'.join(lines)
    with open('scratch/gen_maths_lac.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("scratch/gen_maths_lac.py written successfully! Total size:", len(content))

if __name__ == "__main__":
    assemble()
