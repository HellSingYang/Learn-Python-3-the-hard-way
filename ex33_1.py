a = 0
numbers = []

def function_1(i):
	print(f"At the top i is: {i}")
	numbers.append(i)
	i = i + 1
	print(f"Numbers now: {numbers}")
	print(f"At the bottom i is: {i}")
a += 1
function_1(a)

def function_2(i):
	print(f"At the top i is: {i}")
	numbers.append(i)
	i += 1
	print(f"Numbers now: {numbers}")
	print(f"At the bottom i is: {i}")
a += 1
function_2(a)

def function_3(i):
	print(f"At the top i is: {i}")
	numbers.append(i)
	i += 1
	print(f"Numbers now: {numbers}")
	print(f"At the bottom i is: {i}")
a += 1
function_3(a)

def function_4(i):
	print(f"At the top i is: {i}")
	numbers.append(i)
	i += 1
	print(f"Numbers now: {numbers}")
	print(f"At the bottom i is: {i}")
a += 1
function_4(a)

def function_5(i):
	print(f"At the top i is: {i}")
	numbers.append(i)
	i += 1
	print(f"Numbers now: {numbers}")
	print(f"At the bottom i is: {i}")
a += 1
function_5(a)

#def function_6(i):
#	print(f"At the top i is: {i}")
#	numbers.append(i)
#	i += 1
#	print(f"Numbers now: {numbers}")
#	print(f"At the bottom i is: {i}")
#a += 1
#function_6(a)

print(f"Numbers now: ")
for num in numbers:
	print(num)
#def num(a):
	#print