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

## Acceptance Criteria

1. The calculator must support addition, subtraction, multiplication and division.
2. It must accept positive numbers, negative numbers and decimals.
3. It must ignore unnecessary spaces in the input.
4. It must give the correct answer for valid calculations.
5. It must show an error for an unknown operation.
6. It must show an error for invalid or empty numbers.
7. It must show an error when dividing by zero.
8. It must continue working even when a calculation has an error.
9. The original calculator must still work.

## Acknowledgements

I have used my existing university calculator project as the starting point. I have also reused the files provided in the coursework, including the CSV files and supporting templates. I will build on these materials to complete the project.