nations = {
	'Vietnam': 'VN',
	'Japane': 'JP',
	'German': 'GE',
	'Russia': 'RS',
	'Findland': 'FL'
}

for nation in nations:
	print(nation)

print("Let's add some orther nation into our list")
print("Enter your first nation:")

choice_1 = input('>>> ')
word_list_1 = list(choice_1)
x = word_list_1[0].upper()
y = word_list_1[1].upper()

print("Enter your next nation:")
choice_2 = input(">>> ")
word_list_2 = list(choice_2)
z = word_list_2[0].upper()
t = word_list_2[1].upper()

nations[f'{choice_1}'] = f'{x}{y}'
nations[f'{choice_2}'] = f'{z}{t}'
print("Now, our list include: ")
for nation_plus in nations:
	print(nation_plus)


for nation, abbrev in list(nations.items()):
	print(f"{nation} with abbreviation: {abbrev}")

#choice = input('>>> ')
#word_list = list(choice)
#print(word_list[0].upper(), end = '')
#print(word_list[1].upper())