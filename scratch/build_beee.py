# -*- coding: utf-8 -*-
"""
Builder script to generate scratch/gen_beee.py
Subject 10: Basics of Electrical & Electronics Engineering (EST130 / BEEE)
KTU 2019 Scheme Electrical & Electronics Engineering
"""

import sys
import os

def get_module_content(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    start_idx = 0
    for idx, l in enumerate(lines):
        if l.startswith('MODULE_'):
            start_idx = idx
            break
    first_line = '    {\n'
    rest = lines[start_idx+1:]
    indented = ['    ' + l if l.strip() else l for l in rest]
    return ''.join([first_line] + indented).rstrip()

def get_extra_content(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    # Find start of BEEE_BYHEART
    idx = content.find('BEEE_BYHEART = {')
    return content[idx:].rstrip()

def main():
    print("Building scratch/gen_beee.py...")
    
    header = r'''# -*- coding: utf-8 -*-
"""
Content generator for Subject 10: Basics of Electrical & Electronics Engineering (EST130 / BEEE)
KTU 2019 Scheme Electrical & Electronics Engineering Comprehensive Question Bank.
All answers are written from the perspective of an experienced engineering professor:
clear, direct, mathematically rigorous, with step-by-step intermediate equations.
All strings are raw multiline strings (r'...' or r"...") to prevent LaTeX backslash corruption.
"""

BEEE_MODULES = [
'''
    module_pieces = []
    for i in range(1, 6):
        piece = get_module_content(f'scratch/beee_m{i}.py')
        module_pieces.append(piece)
    
    modules_body = ',\n'.join(module_pieces) + '\n]\n\n'
    extra_body = get_extra_content('scratch/beee_extra.py') + '\n'
    
    full_content = header + modules_body + extra_body
    
    out_path = 'scratch/gen_beee.py'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(full_content)
        
    print(f"Successfully generated {out_path} ({len(full_content)} bytes)")

if __name__ == '__main__':
    main()
