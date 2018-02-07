def number_of_student(number_of_boy, number_of_girl):
	print("There are 50 students in my class.")
	print(f"There are {number_of_boy} boys")
	print(f"There are {number_of_girl} girls.")
	print("\n")

print("The first way, we can use the number in function")
number_of_student(20,30)

print("The second way, we can assign variable")
number_of_boys = 15
number_of_girls = 35
number_of_student(number_of_boys, number_of_girls)

print("The third way, we can use between number and string")
number_of_student(number_of_boys + 10, number_of_girls - 10)

print("Fourthly, we can use math inside")
number_of_student(10+2, 30+8)

print("5th, use input")
a = input('>>> ')
b = input(">>> ")
number_of_student(a ,b)

print("6th, use function to function")
