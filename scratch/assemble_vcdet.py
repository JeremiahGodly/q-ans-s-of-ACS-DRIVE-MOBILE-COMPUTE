# -*- coding: utf-8 -*-
"""
Assembler to write self-contained scratch/gen_maths_vcdet.py
"""

import sys
sys.path.append('scratch')
import build_vcdet_m1
import build_vcdet_m2
import build_vcdet_m3
import build_vcdet_m4
import build_vcdet_m5

def assemble():
    exam_questions = {
        "vcdet-q1": "Solve Bernoulli's differential equation dy/dx + y = y^2 (cos x - sin x).",
        "vcdet-q2": "Solve the second order differential equation (D^2 - 4D + 4)y = 8e^(2x) + sin 2x.",
        "vcdet-q3": "Solve the differential equation d^2y/dx^2 + y = sec x tan x using the method of variation of parameters.",
        "vcdet-q4": "Solve the Cauchy-Euler differential equation: x^2 d^2y/dx^2 - 3x dy/dx + 4y = 2x^2 using the transformation x = e^z.",
        "vcdet-q5": "Solve the non-homogeneous higher order linear differential equation: (D^2 - 2D + 1)y = x e^x sin x using the exponential shift operator.",
        "vcdet-q6": "Find the directional derivative of phi(x, y, z) = x^2 y z + 4 x z^2 at the point (1, -2, -1) in the direction of the vector a = 2i - j - 2k.",
        "vcdet-q7": "Find the unit normal vector to the surface x^2 + y^2 + 2z^2 = 4 at the point (1, 1, 1), and find the equation of the tangent plane.",
        "vcdet-q8": "Show that the vector field F = (2xy + z^3)i + x^2 j + 3xz^2 k is conservative and irrotational. Find its scalar potential phi(x, y, z) such that F = grad phi. Hence evaluate the work done in moving a particle from (1, -2, 1) to (3, 1, 4).",
        "vcdet-q9": "Find constants a, b, c such that the vector field F = (x + 2y + az)i + (bx - 3y - z)j + (4x + cy + 2z)k is irrotational. Also show that F is solenoidal for all values of a, b, c.",
        "vcdet-q10": "If r = x i + y j + z k and r = |r|, prove that: (i) grad(r^n) = n r^(n-2) r, (ii) div(r^n r) = (n+3)r^n, and (iii) Laplacian(r^n) = n(n+1)r^(n-2). Hence show that 1/r is harmonic for r != 0.",
        "vcdet-q11": "Using Green's theorem, evaluate the line integral oint_C [(x - y) dx + (x + y) dy] where C is the closed curve bounded by y = x^2 and y^2 = x traversed counter-clockwise.",
        "vcdet-q12": "State Gauss divergence theorem and explain its physical significance in electrostatics and fluid mechanics.",
        "vcdet-q13": "Verify Green's theorem in the plane for oint_C [(xy + y^2) dx + x^2 dy] where C is the closed curve bounded by y = x and y = x^2.",
        "vcdet-q14": "Verify Gauss divergence theorem for F = 4xz i - y^2 j + yz k over the cube bounded by x = 0, x = 1, y = 0, y = 1, z = 0, z = 1.",
        "vcdet-q15": "Verify Stokes' theorem for F = (2x - y)i - yz^2 j - y^2 z k over the upper hemisphere S: x^2 + y^2 + z^2 = 1, z >= 0 bounded by the circle C: x^2 + y^2 = 1 in the xy-plane.",
        "vcdet-q16": "State Dirichlet's conditions for the existence of Fourier series of a function f(x) in an interval (c, c + 2L). What does the Fourier series converge to at a point of finite discontinuity?",
        "vcdet-q17": "Find the half-range Fourier sine series expansion for f(x) = k (constant) in the interval 0 < x < pi.",
        "vcdet-q18": "Find the Fourier series of f(x) = x^2 in the interval -pi <= x <= pi. Hence deduce that: (i) sum_{n=1}^infinity (-1)^(n-1)/n^2 = pi^2/12, and (ii) sum_{n=1}^infinity 1/n^2 = pi^2/6.",
        "vcdet-q19": "Find the Fourier series of the periodic square wave: f(x) = -k for -pi < x < 0 and k for 0 < x < pi with period 2pi. Hence deduce the Gregory-Leibniz series for pi: 1 - 1/3 + 1/5 - 1/7 + ... = pi/4.",
        "vcdet-q20": "Find the Fourier cosine and sine transforms of f(x) = e^(-ax) (a > 0). Hence evaluate the integral int_0^infinity cos(omega*x) / (a^2 + omega^2) d(omega).",
        "vcdet-q21": "Find the Laplace transform of f(t) = t^2 e^(-3t) sin 2t.",
        "vcdet-q22": "State the Convolution Theorem for Laplace transforms. Use it to find L^(-1){1 / (s(s^2 + 1))}.",
        "vcdet-q23": "Evaluate L{(cos at - cos bt) / t} and hence compute the improper integral int_0^infinity (cos t - cos 2t) / t dt.",
        "vcdet-q24": "Using the Convolution Theorem, find the inverse Laplace transform of F(s) = 1 / (s^2 + a^2)^2.",
        "vcdet-q25": "Solve the initial value problem using Laplace transform: d^2y/dt^2 + 4 dy/dt + 4y = 6 e^(-2t) subject to y(0) = -2 and y'(0) = 8.",
        "vcdet-q26": "Solve the system of simultaneous ordinary differential equations using Laplace transform: dx/dt + y = sin t, dy/dt + x = cos t subject to x(0) = 1 and y(0) = 0."
    }

    modules = [
        {
            "module_id": "vcdet-m1",
            "module_num": "Module 1",
            "module_title": "Ordinary Differential Equations, Bernoulli & Cauchy-Euler Equations",
            "questions": build_vcdet_m1.M1_QUESTIONS
        },
        {
            "module_id": "vcdet-m2",
            "module_num": "Module 2",
            "module_title": "Vector Differentiation, Gradient, Divergence, Curl & Potentials",
            "questions": build_vcdet_m2.M2_QUESTIONS
        },
        {
            "module_id": "vcdet-m3",
            "module_num": "Module 3",
            "module_title": "Vector Integration, Green's, Gauss Divergence & Stokes' Theorems",
            "questions": build_vcdet_m3.M3_QUESTIONS
        },
        {
            "module_id": "vcdet-m4",
            "module_num": "Module 4",
            "module_title": "Fourier Series, Harmonic Analysis & Fourier Integral Transforms",
            "questions": build_vcdet_m4.M4_QUESTIONS
        },
        {
            "module_id": "vcdet-m5",
            "module_num": "Module 5",
            "module_title": "Laplace Transforms, Convolution Theorem & Differential Systems",
            "questions": build_vcdet_m5.M5_QUESTIONS
        }
    ]

    byheart = {}
    byheart.update(build_vcdet_m1.M1_BYHEART)
    byheart.update(build_vcdet_m2.M2_BYHEART)
    byheart.update(build_vcdet_m3.M3_BYHEART)
    byheart.update(build_vcdet_m4.M4_BYHEART)
    byheart.update(build_vcdet_m5.M5_BYHEART)

    lines = []
    lines.append("# -*- coding: utf-8 -*-")
    lines.append('"""')
    lines.append("Content generator for Subject 2: Vector Calculus, Differential Equations and Transforms (MAT102 / MATHS - VCDET)")
    lines.append("KTU 2019 Scheme Electrical & Electronics Engineering (EEE) Question Bank.")
    lines.append("All answers written from the perspective of an experienced engineering mathematics professor.")
    lines.append("Contains complete step-by-step mathematical working, intermediate equations, and highlighted results.")
    lines.append("All strings use raw multiline strings to prevent any LaTeX escape corruptions.")
    lines.append("Equations use standard KaTeX syntax: $$...$$ for display equations, $...$ for inline math.")
    lines.append('"""\n')

    # MATHS_VCDET_EXAM_QUESTIONS
    lines.append("MATHS_VCDET_EXAM_QUESTIONS = {")
    for qid, qtext in exam_questions.items():
        lines.append(f'    "{qid}": {repr(qtext)},')
    lines.append("}\n")

    # MATHS_VCDET_BYHEART
    lines.append("MATHS_VCDET_BYHEART = {")
    for qid, bh in byheart.items():
        lines.append(f'    "{qid}": {{')
        lines.append(f'        "eq": r"""{bh["eq"]}""",')
        lines.append(f'        "text": r"""{bh["text"]}"""')
        lines.append("    },")
    lines.append("}\n")

    # MATHS_VCDET_MODULES
    lines.append("MATHS_VCDET_MODULES = [")
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
    with open('scratch/gen_maths_vcdet.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("scratch/gen_maths_vcdet.py written successfully! Total size:", len(content))

if __name__ == "__main__":
    assemble()
