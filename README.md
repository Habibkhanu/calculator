# Calculator

A Python 3 calculator used from the Terminal, built step by step in SCCM4910

## What it will do
Add, subtract, multiply and divide two numbers; display the result.

## How to run it
Run: ./run.sh
Enter the first number, operator (+ - * /), then second number.
The program prints Result: followed by the answer.

## How to check it
Run: ./check.sh
should pass all 5 tests.
Run: echo $?
should give the input 0 to show that the tests succeeded.
1 means some tests failed; 5 means no tests were collected. 
Other non-zero
statuses can indicate setup or tool errors. 
Run it immediately after pytest, because another command replaces the stored status.

# SCCM4910 DevOps Coursework

## Description

This project improves my existing Python calculator by allowing it to do calculations using CSV files. It supports addition, subtraction, multiplication and division. It also checks for mistakes, such as invalid numbers and dividing by zero. The original calculator will still work.


## Acknowledgements

I have used my existing university calculator project as the starting point. I have also reused the files provided in the coursework, including the CSV files and supporting templates. I will build on these materials to complete the project.

## Acceptance Criteria

1. Support addition, subtraction, multiplication and division.

2. Accept positive, negative and decimal numbers.

3. Ignore unnecessary spaces.

4. Return correct results for valid calculations.

5. Handle unknown operations.

6. Handle invalid or empty numbers.

7. Handle division by zero.


## How to Run

## Run the quality check:

./check.sh

## Batch Processing

Normal dataset:

python3 batch_runner.py data/normal.csv results.csv

Mixed dataset:

python3 batch_runner.py data/mixed.csv mixed-results.csv

## Pre-commit Hook Setup

The pre-commit hook automatically runs the quality checks before a commit is made.

Create the hooks directory and hook file:

mkdir -p hooks
nano hooks/pre-commit

Add the pre-commit script, then make it executable:

chmod +x hooks/pre-commit

Configure Git to use the hooks directory:

git config core.hooksPath hooks

The hook runs ./check.sh, displays the exit code and prevents a commit if the checks fail.


# Evidence

Coursework evidence, including test results, CI runs and batch outputs, is stored in the evidence/ folder. Further details are provided in EVIDENCE.md.