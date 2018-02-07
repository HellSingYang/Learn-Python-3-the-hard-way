five = 10-2+3-6
print(f"This should be five: {five}")

def secret_formula(started):
	jelly_beans = start_point * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

start_point = float(input("Enter start point value: "))
beans, jars, crates = secret_formula(start_point)

print(f"We'd have {beans} beans, {jars} jars and {crates} crates")

print("We can also do that this way:")

formula = secret_formula(start_point)

print("We'd have {} beans, {} jars and {} crates.".format(*formula))