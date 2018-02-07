#Functions can return somethings

def add(a, b):
	print(f"Adding: {a} + {b}")
	return a + b

def subtract(a, b):
	print(f"Subtracting: {a} - {b}")
	return a - b

def multiply(a, b):
	print(f"Multiplying: {a} * {b}")
	return a * b

def divide(a, b):
	print(f"Dividing: {a} / {b}")
	return a / b

print("nhap gia tri x: ")
x = float(input('>>> '))
print("nhap gia tri y: ")
y = float(input('>>> '))
First_equation = add(x, y)
Second_equation = subtract(5, 3)
Third_equation = multiply(3, 3)
Fourth_equation = divide(4, 2)


print(f"""First_equation: {First_equation},
Second_equation: {Second_equation}, 
Third_equation: {Third_equation},
Fourth_equation: {Fourth_equation}.
""")

print("Here is a puzzle.")

what = add(First_equation, subtract(Second_equation, multiply(Third_equation, divide(Fourth_equation, 2))))
print("That becomes: ", what, "Can you do this by hand?")