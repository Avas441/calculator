"""Complete this function for the SCCM4910 coursework.

Place this file beside your existing lab calculator.py. The runner and
file handling are supplied; write your own processing logic and tests.
"""

from calculator import add, sub, mult, div


def process_calculation(operation, a_text, b_text):

    result = () #A empty typle to contain the three outputs that the batch runner expects
    status = "" #Empty string that will contain either the status "OK" on pass or "EEROR" in the event of a failure
    calculation = 0.0 # A empty float to hold the resulting calculation
    error_code = "" #A string that will only be populated if the program encounters an error

    list_of_ops = ["add", "subtract", "divide", "multiply"]

    if operation in list_of_ops:
        try:
            a_text = float(a_text) 
            b_text = float(b_text)
        except:
            status = "ERROR"
            error_code = "INVALID_NUMBER"
            result = (status, calculation, error_code) #Sets the result and fills it with the error codes and status outlined in the given breif
            return result #Prematurley exits program because it cannot convert the inputs to a float
            
        if operation == "add":
            calculation = add(a_text, b_text)
            status = "OK"
        elif operation == "subtract":
            calculation = sub(a_text, b_text)
            status = "OK"

        elif operation == "multiply":
            calculation = mult(a_text, b_text)
            status = "OK"

        elif operation == "divide":
            if a_text == 0 or b_text == 0:
                status = "ERROR"
                error_code = "DIVISION_BY_ZERO"
            else:
                calculation = div(a_text, b_text)
                status = "OK"
        else:
            status = "ERROR"
            error_code = "RAN INTO UNEXPECTED PROBLEM"

        result = (status, calculation, error_code)

        return result
    else:
        status = "ERROR"
        result = (status, calculation, error_code) #Sets the result and fills it with the error codes and status outlined in the given breif
        error_code = "UNKNOWN_OPERATION"
        result = (status, calculation, error_code)
        return result #Prematurley exits program because it cannot find the chosen operation in the list of allowed ones 

    """Return (status, result, error_code) for one calculation.

    Inputs are strings. Trim whitespace and use the four imported lab functions.
    Success: ("OK", numeric_result, "").
    The error_code is empty on success because there is no error to report.
    Error: ("ERROR", "", error_code).

    Check errors in order: UNKNOWN_OPERATION, INVALID_NUMBER, DIVISION_BY_ZERO.
    See the brief for the full contract. You may add small helper functions.
    """
    raise NotImplementedError("Complete process_calculation for the coursework")
