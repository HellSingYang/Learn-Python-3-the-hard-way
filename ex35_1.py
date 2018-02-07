def turn():
	print("This is first line")
	print("This is second line")

#turn()

def orther_turn():
	print("This is third line.")
	print("This is fourth line.")

def start():
	print("We start here.")
	print("Don't know why this start here.")

	choice = input("> ")
	if choice == "1":
		turn()
	elif choice == "2":
		orther_turn()
	else:
		print("Nothing here to show the function.")
start()