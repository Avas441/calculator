"""Complete this function for the SCCM4910 coursework.

Place this file beside your existing lab calculator.py. The runner and
file handling are supplied; write your own processing logic and tests.
"""

from calculator import add, sub, mult, div


def process_calculation(operation, a_text, b_text):

    if operation == "+":
        calculation = add(a_text, b_text)
        result = ("OK", calculation, "")
    elif operation == "-":
        calculation = sub(a_text, b_text)
        result = ("OK", calculation, "")
    elif operation == "*":
        calculation = mult(a_text, b_text)
        result = ("OK", calculation, "")
    elif operation == "/":
        calculation = div(a_text, b_text)
        result = ("OK", calculation, "")
    else:
        print("Sorry something went wrong")

    return result

    """Return (status, result, error_code) for one calculation.

    Inputs are strings. Trim whitespace and use the four imported lab functions.
    Success: ("OK", numeric_result, "").
    The error_code is empty on success because there is no error to report.
    Error: ("ERROR", "", error_code).

    Check errors in order: UNKNOWN_OPERATION, INVALID_NUMBER, DIVISION_BY_ZERO.
    See the brief for the full contract. You may add small helper functions.
    """
    raise NotImplementedError("Complete process_calculation for the coursework")
