word_list = []

stuff = ["Football", "Airplane", "Phone", "Mouse", "Laptop", "American", "Vietnam", "Dinner", "Lamb", "Game", "Song"]

while len(word_list) != 10:
	word = stuff.pop()
	word_list.append(word)

for one in word_list:
	print(one)