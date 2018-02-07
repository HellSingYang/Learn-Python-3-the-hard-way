

def value_1(a, b):
	print(f"Adding: {a} + {b}")
	return a + b

def value_2(c, d):
	print(f"Subtracting: {c} - {d}")
	return c - d

def value_3(e, f):
	print(f"Dividing: {e} / {f}")
	return e / f


#print("Show all of results here: ")

x = value_1(2, 2)
y = value_2(5, 1)
z = value_3(9, 3)

print(f"""First value: {x}
Second value: {y}
Third value: {z}
""")

print("Complex formula:")
T = value_1(1, value_2(x, value_3(x, 2)))
print("result: ", T)

print("nhap gia tri u: ")
u = input()
print(f"{u}")
