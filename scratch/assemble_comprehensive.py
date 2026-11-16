# -*- coding: utf-8 -*-
"""
Assembles standalone scratch/gen_comprehensive.py using exact raw multiline strings r\"\"\"...\"\"\"
Exports: COMPREHENSIVE_MODULES, COMPREHENSIVE_BYHEART, COMPREHENSIVE_EXAM_QUESTIONS
"""

import sys
import os

# Add scratch to sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from comp_m1 import M1_QUESTIONS
from comp_m2 import M2_QUESTIONS
from comp_m3 import M3_QUESTIONS
from comp_m4 import M4_QUESTIONS
from comp_m5 import M5_QUESTIONS
from comp_extra import COMPREHENSIVE_BYHEART, COMPREHENSIVE_EXAM_QUESTIONS

MODULES_DEF = [
    {
        "module_id": "comp-m1",
        "module_num": "Module 1",
        "module_title": "Electrical Circuits & Electromagnetic Fields",
        "questions": M1_QUESTIONS
    },
    {
        "module_id": "comp-m2",
        "module_num": "Module 2",
        "module_title": "Electrical Machines & Power Systems",
        "questions": M2_QUESTIONS
    },
    {
        "module_id": "comp-m3",
        "module_num": "Module 3",
        "module_title": "Control Systems & Instrumentation",
        "questions": M3_QUESTIONS
    },
    {
        "module_id": "comp-m4",
        "module_num": "Module 4",
        "module_title": "Analog & Digital Electronics",
        "questions": M4_QUESTIONS
    },
    {
        "module_id": "comp-m5",
        "module_num": "Module 5",
        "module_title": "Power Electronics & Electric Drives",
        "questions": M5_QUESTIONS
    }
]

def serialize_modules(modules):
    out = ["COMPREHENSIVE_MODULES = ["]
    for m in modules:
        out.append("    {")
        out.append(f'        "module_id": "{m["module_id"]}",')
        out.append(f'        "module_num": "{m["module_num"]}",')
        out.append(f'        "module_title": "{m["module_title"]}",')
        out.append('        "questions": [')
        q_blocks = []
        for q in m["questions"]:
            qb = []
            qb.append("            {")
            qb.append(f'                "qid": "{q["qid"]}",')
            qb.append(f'                "marks": {q["marks"]},')
            qb.append(f'                "type": "{q["type"]}",')
            qb.append(f'                "title": "{q["title"]}",')
            qb.append(f'                "yt_query": "{q["yt_query"]}",')
            qb.append(f'                "img_path": "{q["img_path"]}",')
            qb.append(f'                "img_caption": "{q["img_caption"]}",')
            ans_clean = q["answer"].strip()
            qb.append('                "answer": r"""')
            qb.append(ans_clean)
            qb.append('"""')
            qb.append("            }")
            q_blocks.append("\n".join(qb))
        out.append(",\n".join(q_blocks))
        out.append("        ]")
        out.append("    },")
    out.append("]\n")
    return "\n".join(out)

def serialize_byheart(byheart):
    out = ["COMPREHENSIVE_BYHEART = {"]
    entries = []
    for qid, val in byheart.items():
        eb = []
        eb.append(f'    "{qid}": {{')
        eb.append('        "eq": r"""' + val["eq"].strip() + '""",')
        eb.append('        "text": r"""' + val["text"].strip() + '"""')
        eb.append("    }")
        entries.append("\n".join(eb))
    out.append(",\n".join(entries))
    out.append("}\n")
    return "\n".join(out)

def serialize_exam_questions(exam_q):
    out = ["COMPREHENSIVE_EXAM_QUESTIONS = {"]
    entries = []
    for qid, qtext in exam_q.items():
        q_escaped = qtext.replace('"', '\\"')
        entries.append(f'    "{qid}": "{q_escaped}"')
    out.append(",\n".join(entries))
    out.append("}\n")
    return "\n".join(out)

def main():
    header = '# -*- coding: utf-8 -*-\n' + '"""\n' + """Content generator for Subject 11: Comprehensive Course Work (EET308 / COMPREHENSIVE)
KTU 2019 Scheme S6 Electrical & Electronics Engineering Core Disciplines.
All answers are written from the perspective of an experienced electrical engineering professor:
clear, direct, mathematically rigorous, with step-by-step intermediate equations.
All strings are raw multiline strings (r'''...''') to prevent LaTeX backslash corruption.

Covers 5 Core Modules:
- Module 1: Electrical Circuits and Electromagnetic Fields
- Module 2: Electrical Machines and Power Systems
- Module 3: Control Systems and Instrumentation
- Module 4: Analog and Digital Electronics
- Module 5: Power Electronics and Electric Drives

Exports:
- COMPREHENSIVE_MODULES (5 modules, 26 questions: comp-q1 to comp-q26)
- COMPREHENSIVE_BYHEART (26 entries: qid -> {eq, text})
- COMPREHENSIVE_EXAM_QUESTIONS (26 entries: qid -> question_text)
""" + '"""\n'
    content = (
        header + "\n" +
        serialize_modules(MODULES_DEF) + "\n" +
        serialize_byheart(COMPREHENSIVE_BYHEART) + "\n" +
        serialize_exam_questions(COMPREHENSIVE_EXAM_QUESTIONS) + "\n" +
        '''__all__ = ["COMPREHENSIVE_MODULES", "COMPREHENSIVE_BYHEART", "COMPREHENSIVE_EXAM_QUESTIONS"]

if __name__ == "__main__":
    total_q = sum(len(m["questions"]) for m in COMPREHENSIVE_MODULES)
    print(f"gen_comprehensive.py verified: {len(COMPREHENSIVE_MODULES)} modules, {total_q} questions, "
          f"{len(COMPREHENSIVE_BYHEART)} byheart cards, {len(COMPREHENSIVE_EXAM_QUESTIONS)} exam questions.")
'''
    )
    
    target_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gen_comprehensive.py")
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Successfully generated {target_path} ({len(content)} bytes)")

if __name__ == "__main__":
    main()
