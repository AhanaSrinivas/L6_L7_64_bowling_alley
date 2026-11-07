# L6_L7_64 - Bowling Alley

Lab 7: Fuzzing for Input Validation Bugs

## About

A small Python module that reads bowling alley details typed in by a user: player names, frames and scoreboards. It assumes every input is well formed.

## Files

| File | Description |
|------|-------------|
| `bowling_alley_parser.py` | The buggy module you will fuzz and fix |
| `test_bowling_alley_parser.py` | Hypothesis test template to complete |

Keep all your Lab 7 work in this `LAB7` folder.

Follow the lab handout for the full instructions. Use the file names above wherever the handout refers to the code and test files.

## Screenshots

| Screenshot | What it must show |
|------------|-------------------|
| SS1 | `python bowling_alley_parser.py` run on the buggy module |
| SS2 | `pytest test_bowling_alley_parser.py` with the completed tests failing on the buggy module |
| SS3 | `python bowling_alley_parser.py` run on the fixed module |
| SS4 | `pytest test_bowling_alley_parser.py` with all tests passing on the fixed module |

## Deliverables

Commit these three files in the `LAB7` folder:

1. `bowling_alley_parser.py`: the fixed module. All three functions must handle unexpected inputs without crashing.
2. `test_bowling_alley_parser.py`: completed Hypothesis tests, one for each function.
3. `SRN_NAME_LAB7.pdf`: screenshots SS1 to SS4 and answers to the reflection questions.

Be ready to explain the bugs found and how they were fixed.
