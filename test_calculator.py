from calculator import add, sub, div, mult

def test_add():
    result = ("OK", 5, "")
    assert add(2, 3) == result

def test_sub():
    result = ("OK", 10, "")
    assert add(20, 10) == result

def test_div():
    result = ("OK", 3, "")
    assert add(15, 5) == result

def test_mult():
    result = ("OK", 10, "")
    assert add(2, 5) == result