from batch_calculator import process_calculation

def test_unknown_op():
    result = ("ERROR", 0.0, "UNKNOWN_OPERATION")
    assert process_calculation("invalid", "5", "4") == result

def test_invalid_number():
    result = ("ERROR", 0.0, "INVALID_NUMBER")
    assert process_calculation("add", "hello", "World") == result

def test_division_by_0():
    result = ("ERROR", 0.0, "DIVISION_BY_ZERO")
    assert process_calculation("divide", "0", "2") == result