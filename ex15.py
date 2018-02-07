from sys import argv

script, filename = argv
txt = open(filename)

print(f"Here's your {filename} file")
print(txt.read())

print("Type the filename again: ")
file_again = input('> ')
txt_again = open(file_again)

#print message from ex15_sample.txt again
print(txt_again.read())

#txt.close()
#txt_again.close()

print(f"We're going to erase {filename}")
print("If you don't want this, hit CTRL-C (^C).")
print("If you want this, hit RETURN.")

input("?")

print("Open the file ...")

target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these to the file")

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
target.write(f"""
	{line1}
	{line2}
	{line3}
	""")
	
print(f"""
	{line1}
	{line2}
	{line3}
	""")

print("And finally, we're close it.")
target.close()

print("Type the new file here: ")
newfile = input('>>> ')
opennewfile = open(newfile)
print(opennewfile.read())