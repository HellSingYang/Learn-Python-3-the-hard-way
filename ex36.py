from sys import exit
import timeit



def jig_saw_room():
	print("You stand in a dark room with the light door.")
	print("Your feeling let you know Jig Saw is somewhere in this room.")
	print("What you gonna do to get out of this room?")

	Jigsaw_die = False
	while True:
		choice = input(">>> ")
		if choice == "fight":
			dead("You die - Nothing can stop him.")
		elif choice == "pray":
			dead("You die - God doesn't exist.")
		elif choice == "run" and not Jigsaw_die:
			print("You still alive.")
			print("Touch the light door to open it.")
			Jigsaw_die = True
		#elif choice == "run" and Jigsaw_die:
		#	dead("You die - Noone can escape from him.")
		elif choice == "open door" and Jigsaw_die:
			cyberus_room()
		else:
			print("I got no idea what that mean.")

def diamond_room():
	print("This room have 30 kinds of diamond with Sphinx protect it, choose different types.")
	print("You have one minute to think what type you gonna take.")
	
	choice = input(">>> ")
	if "simplest" in choice:
		print("Clever boy, you win this game.")
		exit(0)
	else:
		dead("Sphinx eats your face off.")


def cyberus_room():
	print("There is a Cyberus here.")
	print("How you move it to go through this room?")
	print("There are a shortgun and an axe for you.")
	print("You can take one of them to against Cyberus.")


	cyberus_dead = False
	while True:
		choice = input(">>> ")
		if choice == "take a gun":
			dead("No bullets in the gun.")
		elif choice == "axe":
			dead("You can not get close to it.")
		elif "me" and "eat" and "taunt" and "away" in choice and not cyberus_dead:
			print("Although you lose a part of your body, you still alive.")
			print("You can go through it now.")
			cyberus_dead = True
		elif choice == "open door" and cyberus_dead:
			diamond_room()
		else:
			print("I got no idea what that mean.")


def dead(why):
	print(why, "Better luck next time!")
	exit(0)

def start_room():
	print("You are standing in a room with four doors.")
	print("Choosing your door to going out there.")

	choice = input(">>> ")
	if choice == "first":
		jig_saw_room()
	elif choice == "second":
		print("Welcome! You are here again.")
		print("Now, pick up your choice.")
		start_room()
	elif choice == "third":
		cyberus_room()
	elif choice == "fourth":
		dead("You go the hell.")
	else:
		print("I don't get what that mean.")

start_room()