from sys import argv
script, first, second, third = argv

print ("First number: ", end = ' ')
x = float(input())
print ("Second number: ", end = ' ')
y = float(input())
total = (x+y)
print (f"Result of this: {total}")

print ("The script is called: ", script)
print ("The first variable is: ", first)
print ("The second variable is: ", second)
print ("The third variable is: ", third)
