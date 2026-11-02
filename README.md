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
