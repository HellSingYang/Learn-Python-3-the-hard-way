from sys import exit

def gold_room():
	print("This room is full of gold. How much do you take?")

	choice = float(input(">>> "))
	
	#how_much = float(choice)
	if choice < 50:
		print("You are not greedy, you win.")
	else:
		print("You greedy, bastard!")

def bear_room():
	print("There is a bear here.")
	print("The bear has a bunch of honey.")
	print("The fat bear is in front of another door.")
	print("How are you going to move the bear.")

	bear_moved = False

	while True:
		choice = input(">>> ")
		if choice == "take cake":
			dead("The bear look at you and then slap your face off.")
		elif choice == "taunt bear" and not bear_moved:
			print("The bear go way with bunch of honey.")
			print("You go through the door.")
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("The bear chews your leg off.")
		elif choice == "open door" and bear_moved:
			cthulhu_room()
		else:
			print("I got no idea what that means.")

def cthulhu_room():
	print("Here you see the great evil Cthulhu.")
	print("He, it, whatever stares at you and you go insane.")
	print("Do you flee for your life or eat your head?")

	choice = input(">>> ")

	if "flee" in choice:
		gold_room()
	elif "head" in choice:
		dead("Well that was tastly!")
	else:
		cthulhu_room()

def dead(why):
	print(why, "Good job!")
	exit(0)

def start():
	print("You are in the dark room.")
	print("There are two doors for you go right or left.")
	print("Which one do you take?")

	choice = input(">>> ")
	if "right" in choice:
		cthulhu_room()
	elif "left" in choice:
		gold_room()
	else:
		dead("You stumble around the room until you starve.")
start()