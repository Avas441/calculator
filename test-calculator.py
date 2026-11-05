from calculator import add, sub, mult, div

print("Debug")

def test_add():
	assert add(2, 3) == 5
def test_div():
	assert div(6, 2) == 3
def test_sub():
	assert sub(5, 3) == 2
def test_mult():
	assert mult(5, 2) == 10

