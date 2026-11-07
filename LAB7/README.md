# Lab 7 Fuzz Testing

**Name:** Ahana Srinivas Sivaram  
**SRN:** PES1UG24CS910  
**Section:** H  
**Assigned repository:** [L6_L7_64_bowling_alley](https://github.com/AhanaSrinivas/L6_L7_64_bowling_alley)

## Contents

- `processor.py` - fixed Bowling Alley input processor.
- `test_processor.py` - Hypothesis properties and regression examples for all three functions.
- `requirements.txt` - Hypothesis and pytest dependencies.
- `pytest.ini` - keeps pytest focused on the completed Lab 7 tests, not the preserved starter template.
- `Lab 7 Report(PES1UG24CS910_Ahana_Srinivas_Sivaram).pdf` - final screenshot report with SS1 to SS4.
- `Lab 7 Report(PES1UG24CS910_Ahana_Srinivas_Sivaram).docx` - editable source for the final PDF.
- `screenshots/` - terminal captures; SS2 traceback continuations are kept separately.
- `original/` - the starter files as they appeared in the cloned repository, plus the frozen buggy baseline used to reproduce SS2.

## Install and run

From this folder, using Python 3.8 or newer:

```powershell
python -m pip install -r requirements.txt
python -m pytest -q test_processor.py
```

The fixed implementation passes all four tests. To reproduce the initial buggy stage, temporarily back up `processor.py`, copy `original/processor_buggy.py` over it, run the application and tests, then restore the fixed source from the backup.

## Input handling

`format_player_name` returns an empty string for non-string input; `parse_frame` returns `(0, 0)` for invalid notation; and `parse_scoreboard` skips malformed entries and returns an empty mapping for non-string input. Valid examples retain their expected results.
