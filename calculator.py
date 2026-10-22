# SCCM4910 (DevOps) lab project - A simple four operation calculator :)

def add(a, b):
	return a + b

def sub(a , b):
	return a -  b

def mult(a, b):
	return a * b

def div(a, b):
	return a / b

def main():
	while True:
		a = float(input("Please enter your first number: "))
		op = input("PLease enter your required operation (+ - * /): ")
		b = float(input("Please enter your second number: "))
		if op == "+":
			print("Result:", add(a, b))
		elif op == "-":
			print("Result:", sub(a, b))
		elif op == "*":
			print("Result", mult(a, b))
		elif op == "/":
			print("Result", div(a, b))
		else:
			print("Sorry, a error was encountered")

if __name__ == "__main__":
	main()
