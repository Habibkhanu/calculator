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

    if operation == "divide":
        if b == 0:
            return ("ERROR", "", "DIVISION_BY_ZERO")
        numeric_result = divide(a, b)

    elif operation == "add":
        numeric_result = add(a, b)

    elif operation == "subtract":
        numeric_result = subtract(a, b)

    elif operation == "multiply":
        numeric_result = multiply(a, b)

    return ("OK", numeric_result, "")

		

"""Inputs are strings. Trim whitespace and use the four imported lab functions.
    Success: ("OK", numeric_result, "").
    The error_code is empty on success because there is no error to report.
    Error: ("ERROR", "", error_code).

Check errors in order: UNKNOWN_OPERATION, INVALID_NUMBER, DIVISION_BY_ZERO.
    See the brief for the full contract. You may add small helper functions.
    """

