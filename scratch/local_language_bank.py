# scratch/local_language_bank.py
# Master Local Language Bank for KTU University Examination Prep
# Combines authentic Manglish and Malayalam (മലയാളം) local study guides across all 3 subjects:
# - Advanced Control Systems (ACS): 29 questions
# - Electric Drives (Drives): 27 questions
# - Mobile Computing: 38 questions
# Total: 94 questions

from acs_local_bank import ACS_LOCAL_ANSWERS
from drive_local_bank import DRIVE_LOCAL_ANSWERS
from mobile_local_bank import MOBILE_LOCAL_ANSWERS

LOCAL_LANG_BANK = {}
LOCAL_LANG_BANK.update(ACS_LOCAL_ANSWERS)
LOCAL_LANG_BANK.update(DRIVE_LOCAL_ANSWERS)
LOCAL_LANG_BANK.update(MOBILE_LOCAL_ANSWERS)

# Backward-compatibility alias
LOCAL_LANG_DEMO = LOCAL_LANG_BANK
