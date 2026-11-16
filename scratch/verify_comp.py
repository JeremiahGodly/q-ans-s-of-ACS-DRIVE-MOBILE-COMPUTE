# -*- coding: utf-8 -*-
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_comprehensive import COMPREHENSIVE_MODULES, COMPREHENSIVE_BYHEART, COMPREHENSIVE_EXAM_QUESTIONS

print(f"Total modules: {len(COMPREHENSIVE_MODULES)}")
assert len(COMPREHENSIVE_MODULES) == 5, "Expected 5 modules"

all_qids = []
for m_idx, m in enumerate(COMPREHENSIVE_MODULES, 1):
    num = m["module_num"]
    title = m["module_title"]
    mid = m["module_id"]
    print(f"\n--- {num}: {title} (ID: {mid}) ---")
    print(f"Questions count: {len(m['questions'])}")
    for q in m["questions"]:
        qid = q["qid"]
        all_qids.append(qid)
        assert q["marks"] in [3, 7], f"Unexpected marks: {q['marks']}"
        assert len(q["title"]) > 10, f"Title too short: {q['title']}"
        assert len(q["yt_query"]) > 5, f"yt_query too short: {q['yt_query']}"
        assert len(q["img_path"]) > 5, f"img_path too short: {q['img_path']}"
        assert len(q["img_caption"]) > 5, f"img_caption too short: {q['img_caption']}"
        assert len(q["answer"]) > 1000, f"Answer too short: {len(q['answer'])} chars in {qid}"
        assert qid in COMPREHENSIVE_BYHEART, f"Missing byheart for {qid}"
        assert qid in COMPREHENSIVE_EXAM_QUESTIONS, f"Missing exam question for {qid}"
        qlen = len(q["answer"])
        qtitle = q["title"]
        print(f"  [{qid}] {qtitle} ({qlen} chars)")

expected_qids = [f"comp-q{i}" for i in range(1, 27)]
assert all_qids == expected_qids, f"Mismatch in qids: {all_qids} vs {expected_qids}"
assert len(COMPREHENSIVE_BYHEART) == 26, f"Expected 26 byheart entries, got {len(COMPREHENSIVE_BYHEART)}"
assert len(COMPREHENSIVE_EXAM_QUESTIONS) == 26, f"Expected 26 exam questions, got {len(COMPREHENSIVE_EXAM_QUESTIONS)}"

print("\nALL 26 QUESTIONS VALIDATED PERFECTLY!")
