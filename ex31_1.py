print("""We are going to stay out there. Let's choose your tents:
First tent, second tent or no tent.""")
tent = input("> ")
if tent == "1":
	print("1. Party at night.")
	print("2. Sleeping.")

	choose = input("> ")
	if choose == "1":
		print("Jack Saw are under the table.")
		print("1. Against him.")
		print("2. Run away.")

		do_1 = input("> ")
		if do_1 == "1":
			print("You die.")
		else:
			print("Meeting orther people in forest and keep running.")
	else:
		print("You was awakened when Jack Saw killing people.")
		print("1. Stay in the tent.")
		print("2. Run away.")

		do_2 = input("> ")
		if do_2 == "1":
			print("You die.")
		else:
			print("Meeting orther people in forest and keep running.")
elif tent == "2":
	print("1. Joining Ouija game.")
	print("2. Joining conversation with orther.")

	do_3 = input("> ")
	if do_3 == "1":
		print("Anabella appear.")
		print("1. Running away.")
		print("2. Dead fake.")

		do_4 = input("> ")
		if do_4 == "1":
			print("You die. Nobody can run away from her.")
		else:
			print("You are haunted.")
	else:
		print("Jack Saw and Anabella come together and kill all.")
else:
	print("See Pennywise under water.")
	print("1. Fish and kill Pennywise.")
	print("2. Run away.")

	do_5 = input("> ")
	if do_5 == "1":
		print("You die. You can not kill him.")
	else:
		print("Meeting orther people in forest and keep running.")

print("You are still alive, pick up your weapons")
print("1. Gun with Jack Saw chasing on you.")
print("2. Knife with Pennywise chasing on you.")
print("3. Axe with Anabella chasing on you.")

Weapon = input("> ")
if Weapon == "1":
	print("You die, noone can kill Jack Saw.")
elif Weapon == "2":
	print("You die, you can not kill Pennywise.")
else:
	print("You die.")