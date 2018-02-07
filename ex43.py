from textwrap import dedent

print(dedent("""
	The sentence will show you
	Come to the end.
	"""))

print("""
	The sentence will show you
	Come to the end.
	""")

def re(x, y):
	print(f"{x} + {y}")
	return x + y


age  = re(2, 1)
print(f"{age}")