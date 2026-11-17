from batch_calculator import process_calculation

def test_add():
    result = ("OK", 5.0, "")
    assert process_calculation("add", 2, 3) == result

def test_sub():
    result = ("OK", 10.0, "")
    assert process_calculation("subtract", 15, 5) == result

def test_div():
    result = ("OK", 3.0, "")
    assert process_calculation("divide", 15, 5) == result

def test_mult():
    result = ("OK", 10.0, "")
    assert process_calculation("multiply", 2, 5) == result