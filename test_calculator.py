#from batch_calculator import process_calculation

from calculator import add, sub, mult, div, CircleArea

def test_add():
    result = (5)
    assert add(2, 3) == result

def test_sub():
    result = (10)
    assert sub(15, 5) == result

def test_div():
    result = (3)
    assert div(15, 5) == result

def test_mult():
    result = (10)
    assert mult(2, 5) == result

def test_circle_are():
    assert CircleArea(-4) == "Error"