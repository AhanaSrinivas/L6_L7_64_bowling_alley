# Lab 6: Code and Branch Coverage Analysis

**Name:** Ahana Srinivas Sivaram  
**SRN:** PES1UG24CS910  
**Section:** H  
**Assigned application:** Bowling Alley

## Objective

Measure statement/code coverage and branch coverage for the assigned Bowling Alley application, then exercise the application paths with focused test cases.

## Files and deliverables

- `bowling_alley.py` - assigned application under test.
- `CodeCoverageTest_910_bowling_alley.py` - test suite for code coverage.
- `BranchCoverageTest_910_bowling_alley.py` - test suite for branch coverage.
- `CodeCoverage_Result.txt` and `BranchCoverage_Result.txt` - saved successful terminal output.
- `CodeCoverage_Screenshot.png` and `BranchCoverage_Screenshot.png` - terminal screenshots to add after running the commands below.

## Coverage analysis

The code coverage run executes all 35 executable statements in `bowling_alley.py` (100%). The branch coverage run exercises all 26 decision outcomes (100%). The branch suite additionally covers alternate outcomes such as invalid input, league-member discount, strike/spare/open frames, and lane assignment decisions.

## Run and capture the required terminal screenshots

Open PowerShell in this `LAB6` directory. Install dependencies once:

```powershell
python -m pip install -r requirements.txt
```

Run the code coverage suite and report:

```powershell
python -m coverage erase
python -m coverage run --source=bowling_alley -m pytest -q CodeCoverageTest_910_bowling_alley.py
python -m coverage report -m
```

Capture the terminal showing the passing tests and the 100% report. Save it in this directory as `CodeCoverage_Screenshot.png`.

Run the branch coverage suite and report:

```powershell
python -m coverage erase
python -m coverage run --branch --source=bowling_alley -m pytest -q BranchCoverageTest_910_bowling_alley.py
python -m coverage report -m
```

Capture the terminal showing the passing tests and the 100% branch report. Save it in this directory as `BranchCoverage_Screenshot.png`.

## Required commits

The handout requires at least two commits: one containing the code coverage test and its screenshot, and one containing the branch coverage test and its screenshot. Make the first commit after adding `CodeCoverage_Screenshot.png`; make the second after adding `BranchCoverage_Screenshot.png`.
