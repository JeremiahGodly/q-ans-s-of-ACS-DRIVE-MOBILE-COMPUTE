# -*- coding: utf-8 -*-
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_pe as pe

print("PE_MODULES count:", len(pe.PE_MODULES))
module_q_counts = [len(m["questions"]) for m in pe.PE_MODULES]
print("Questions per module:", module_q_counts)
total_questions = sum(module_q_counts)
print("Total questions:", total_questions)
print("PE_BYHEART count:", len(pe.PE_BYHEART))
print("PE_EXAM_QUESTIONS count:", len(pe.PE_EXAM_QUESTIONS))

expected_qids = [f"pe-q{i}" for i in range(1, 27)]
actual_qids = [q["qid"] for m in pe.PE_MODULES for q in m["questions"]]
assert actual_qids == expected_qids, f"Mismatched module QIDs: {actual_qids}"
assert list(pe.PE_BYHEART.keys()) == expected_qids, "Mismatched BYHEART QIDs"
assert list(pe.PE_EXAM_QUESTIONS.keys()) == expected_qids, "Mismatched EXAM QIDs"

for m in pe.PE_MODULES:
    mid = m["module_id"]
    mtitle = m["module_title"]
    qcount = len(m["questions"])
    print(f"{mid}: {mtitle} -> {qcount} questions")
    for q in m["questions"]:
        qid = q["qid"]
        ans_len = len(q["answer"])
        assert ans_len > 1500, f"Answer too short for {qid}: {ans_len}"
        assert "$$" in q["answer"], f"Missing KaTeX display math in {qid}"

for qid in expected_qids:
    bh = pe.PE_BYHEART[qid]
    assert "eq" in bh and len(bh["eq"]) > 0, f"Empty eq in byheart {qid}"
    assert "text" in bh and len(bh["text"]) > 0, f"Empty text in byheart {qid}"
    eq = pe.PE_EXAM_QUESTIONS[qid]
    assert len(eq) > 10, f"Exam question too short in {qid}"

print("\n>>> ALL 26 QUESTIONS AND EXPORTS VERIFIED PERFECTLY! <<<")
