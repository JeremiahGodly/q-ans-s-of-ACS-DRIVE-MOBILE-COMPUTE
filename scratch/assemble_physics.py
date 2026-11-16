# -*- coding: utf-8 -*-
"""
Assembles standalone scratch/gen_physics.py using exact raw multiline strings r\"\"\"...\"\"\"
"""

import sys
import os

# Add scratch to sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from phy_m1 import MODULE_1
from phy_m2 import MODULE_2
from phy_m3 import MODULE_3
from phy_m4 import MODULE_4
from phy_m5 import MODULE_5
from phy_byheart_exam import PHYSICS_BYHEART, PHYSICS_EXAM_QUESTIONS

def serialize_modules(modules):
    out = ["PHYSICS_MODULES = ["]
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
    out = ["PHYSICS_BYHEART = {"]
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
    out = ["PHYSICS_EXAM_QUESTIONS = {"]
    entries = []
    for qid, qtext in exam_q.items():
        q_escaped = qtext.replace('"', '\\"')
        entries.append(f'    "{qid}": "{q_escaped}"')
    out.append(",\n".join(entries))
    out.append("}\n")
    return "\n".join(out)

def main():
    modules = [MODULE_1, MODULE_2, MODULE_3, MODULE_4, MODULE_5]
    
    header = '''# -*- coding: utf-8 -*-
"""
Content generator for Subject 3: Engineering Physics A (PHT100)
KTU 2019 Scheme Syllabus Comprehensive Question Bank.
All answers are elaborated in paragraph format with step-by-step mathematical derivations.
All strings are raw multiline strings to prevent any LaTeX escape corruptions.
Exports: PHYSICS_MODULES, PHYSICS_BYHEART, PHYSICS_EXAM_QUESTIONS
"""
'''
    content = header + "\n" + serialize_modules(modules) + "\n" + serialize_byheart(PHYSICS_BYHEART) + "\n" + serialize_exam_questions(PHYSICS_EXAM_QUESTIONS)
    
    target_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gen_physics.py")
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Successfully generated {target_path}")

if __name__ == "__main__":
    main()
