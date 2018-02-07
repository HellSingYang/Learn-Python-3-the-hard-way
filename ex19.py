# Functionb and variables

def cheese_and_cracker(cheese_count, box_of_crackers):
	print(f"You have {cheese_count} cheeses!")
	print(f"You have {box_of_crackers} boxes of crackers!")
	print("Man that's enough for the party!")
	print("Get a blanket.")
	print("\n")
print("We can just give the function numbers directly: ")
cheese_and_cracker(20, 30)

print("Or, we can you variables from our script: ")

amount_of_cheese = 10
amount_of_cracker = 50

cheese_and_cracker(amount_of_cheese, amount_of_cracker)

print("We can even do math inside too: ")
cheese_and_cracker(10 + 20, 5 + 6)

print("And we can combine two, variables and math: ")
cheese_and_cracker(amount_of_cheese + 100, amount_of_cracker + 1000)

