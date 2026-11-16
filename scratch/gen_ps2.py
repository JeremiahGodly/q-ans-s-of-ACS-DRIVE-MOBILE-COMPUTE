# -*- coding: utf-8 -*-
"""
Content generator for Subject 5: Power System II (EET304 / PS2)
KTU 2019 Scheme Syllabus Comprehensive Question Bank.
All answers are elaborated in lecturer format with complete step-by-step mathematical working.
All strings are raw multiline strings (r\"\"\"...\"\"\") to prevent any LaTeX escape corruptions.
"""
import sys
import os

_dir = os.path.dirname(os.path.abspath(__file__))
if _dir not in sys.path:
    sys.path.insert(0, _dir)

try:
    from ps2_m1 import M1_QUESTIONS
    from ps2_m2 import M2_QUESTIONS
    from ps2_m3 import M3_QUESTIONS
    from ps2_m4 import M4_QUESTIONS
    from ps2_m5 import M5_QUESTIONS
    from ps2_extra import PS2_BYHEART, PS2_EXAM_QUESTIONS
except ImportError:
    from scratch.ps2_m1 import M1_QUESTIONS
    from scratch.ps2_m2 import M2_QUESTIONS
    from scratch.ps2_m3 import M3_QUESTIONS
    from scratch.ps2_m4 import M4_QUESTIONS
    from scratch.ps2_m5 import M5_QUESTIONS
    from scratch.ps2_extra import PS2_BYHEART, PS2_EXAM_QUESTIONS

PS2_MODULES = [
    {
        "module_id": "ps2-m1",
        "module_num": "Module 1",
        "module_title": "Symmetrical Faults and Z-bus Formulation",
        "questions": M1_QUESTIONS
    },
    {
        "module_id": "ps2-m2",
        "module_num": "Module 2",
        "module_title": "Symmetrical Components and Unsymmetrical Faults",
        "questions": M2_QUESTIONS
    },
    {
        "module_id": "ps2-m3",
        "module_num": "Module 3",
        "module_title": "Power Flow Analysis",
        "questions": M3_QUESTIONS
    },
    {
        "module_id": "ps2-m4",
        "module_num": "Module 4",
        "module_title": "Power System Dynamics and Transient Stability",
        "questions": M4_QUESTIONS
    },
    {
        "module_id": "ps2-m5",
        "module_num": "Module 5",
        "module_title": "Power System Control and Economic Dispatch",
        "questions": M5_QUESTIONS
    }
]

__all__ = ["PS2_MODULES", "PS2_BYHEART", "PS2_EXAM_QUESTIONS"]

if __name__ == "__main__":
    total_q = sum(len(m["questions"]) for m in PS2_MODULES)
    print(f"gen_ps2.py verified: {len(PS2_MODULES)} modules, {total_q} questions, {len(PS2_BYHEART)} byheart entries, {len(PS2_EXAM_QUESTIONS)} exam questions.")
