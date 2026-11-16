# scratch/build_lcs.py
import sys
import os

print("Writing scratch/gen_lcs.py...")

header = r'''# -*- coding: utf-8 -*-
"""
Content generator for Subject 4: Linear Control Systems (EET302 / LCS)
KTU 2019 Scheme Syllabus Comprehensive Question Bank.
All answers are elaborated in lecturer format with complete step-by-step mathematical working.
All strings are raw multiline strings (r\"\"\"...\"\"\") to prevent any LaTeX escape corruptions.
"""
'''

print("Building LCS module...")
