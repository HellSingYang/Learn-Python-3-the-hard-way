##
class Animals(object):
	pass

##
class Dog(Animals):

	def __init__(self, name):
		##
		self.name = name

##
class Cat(Animals):

	def __init__(self, name):
		##
		self.name = name

##
class Person(object):

	def __init__(self, name):
		##
		self.name = name

		##
		self.pet = None

##
class Employee(Person):

	def __init__(self, name, salary):
		##
		super(Employee, self).__init__(name)
		##
		self.salary = salary

##
class Fish(object):
	pass

##
class Salmon(object):
	pass

##
class Halibut(object):
	pass

##
rover = Dog("Rover")

##
satan = Cat("Satan")

##
mary = Person("Mary")

##
mary.pet = satan

##
frank = Employee("Frank", 120000)

##
Frank.pet = rover

##
flipper = Fish()

##
crouse = Salmon()

##
harry = Halibut()