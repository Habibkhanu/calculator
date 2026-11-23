"""Complete this function for the SCCM4910 coursework.

Place this file beside your existing lab calculator.py. The runner and
file handling are supplied; write your own processing logic and tests.
"""

from calculator import add, subtract, multiply, divide


def process_calculation(operation, a_text, b_text):
    operation = operation.strip()
    a_text = a_text.strip()
    b_text = b_text.strip()

   

		

"""Inputs are strings. Trim whitespace and use the four imported lab functions.
    Success: ("OK", numeric_result, "").
    The error_code is empty on success because there is no error to report.
    Error: ("ERROR", "", error_code).

Check errors in order: UNKNOWN_OPERATION, INVALID_NUMBER, DIVISION_BY_ZERO.
    See the brief for the full contract. You may add small helper functions.
    """

