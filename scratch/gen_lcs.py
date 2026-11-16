# -*- coding: utf-8 -*-
"""
Content generator for Subject 4: Linear Control Systems (EET302 / LCS)
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
    from lcs_m1 import M1_QUESTIONS
    from lcs_m2 import M2_QUESTIONS
    from lcs_m3 import M3_QUESTIONS
    from lcs_m4 import M4_QUESTIONS
    from lcs_m5 import M5_QUESTIONS
    from lcs_extra import LCS_BYHEART, LCS_EXAM_QUESTIONS
except ImportError:
    from scratch.lcs_m1 import M1_QUESTIONS
    from scratch.lcs_m2 import M2_QUESTIONS
    from scratch.lcs_m3 import M3_QUESTIONS
    from scratch.lcs_m4 import M4_QUESTIONS
    from scratch.lcs_m5 import M5_QUESTIONS
    from scratch.lcs_extra import LCS_BYHEART, LCS_EXAM_QUESTIONS

LCS_MODULES = [
    {
        "module_id": "lcs-m1",
        "module_num": "Module 1",
        "module_title": "Mathematical Modeling of Control Systems",
        "questions": M1_QUESTIONS
    },
    {
        "module_id": "lcs-m2",
        "module_num": "Module 2",
        "module_title": "Time Domain Analysis and Controllers",
        "questions": M2_QUESTIONS
    },
    {
        "module_id": "lcs-m3",
        "module_num": "Module 3",
        "module_title": "Stability Analysis and Root Locus Technique",
        "questions": M3_QUESTIONS
    },
    {
        "module_id": "lcs-m4",
        "module_num": "Module 4",
        "module_title": "Frequency Response Analysis and Nyquist Criterion",
        "questions": M4_QUESTIONS
    },
    {
        "module_id": "lcs-m5",
        "module_num": "Module 5",
        "module_title": "Compensator Design and State Space Basics",
        "questions": M5_QUESTIONS
    }
]

__all__ = ["LCS_MODULES", "LCS_BYHEART", "LCS_EXAM_QUESTIONS"]

if __name__ == "__main__":
    total_q = sum(len(m["questions"]) for m in LCS_MODULES)
    print(f"gen_lcs.py verified: {len(LCS_MODULES)} modules, {total_q} questions, {len(LCS_BYHEART)} byheart entries, {len(LCS_EXAM_QUESTIONS)} exam questions.")
