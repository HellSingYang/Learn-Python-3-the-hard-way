from sys import argv
script, file = argv

file_open = open(file)

def open_file(a):
	print(a.read())

open_file(file_open)