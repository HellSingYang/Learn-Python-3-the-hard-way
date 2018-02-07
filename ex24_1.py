def formula(started):
	jelly_beans = start_point*500
	jars = jelly_beans / 1000
	crates = jars /100
	return jelly_beans, jars, crates

start_point = int(input("With starting point is: "))
#start_point = int(input('>>> '))

beans, jars, crates = formula(start_point)
#print("With starting point is: ".format(start_point))

print(f"We have {beans} beans, {jars} jars and {crates} crates in the box.")

print("Or we can do this way:")
start_point = start_point/10
secret_formula = formula(start_point)
print("We have {} beans, {} jars and {} crates in the box.".format(*secret_formula))