import random


sentence = "Posting guidelines frequently asked questions Subreddit rules Message the moderators."
words = sentence.split()
print(words)

for w in random.sample(words, 1):
	print(w)
