"""Complete this function for the SCCM4910 coursework.

Place this file beside your existing lab calculator.py. The runner and
file handling are supplied; write your own processing logic and tests.
"""

from calculator import add, subtract, multiply, divide


def process_calculation(operation, a_text, b_text):
    operation = operation.strip()
    a_text = a_text.strip()
    b_text = b_text.strip()

    if operation not in ("add", "subtract", "multiply", "divide"):
        return ("ERROR", "", "UNKNOWN_OPERATION")

    try:	
        a = float(a_text)
        b = float(b_text)
    except ValueError:
        return ("ERROR", "", "INVALID_NUMBER")

    if operation == "divide" and b == 0:
        return ("ERROR", "", "DIVISION_BY_ZERO")

    if operation == "add":
        result = add(a, b)
    elif operation == "subtract":
        result = subtract(a, b)
    elif operation == "divide":
        result = divide(a, b)
    else:
        result = multiply(a, b)

    return ("OK", result, "")
    
