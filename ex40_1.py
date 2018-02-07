class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)

	def break_word(self):
		word_list = self.lyrics.split(' ')
		return word_list

happy_bday_1 = Song(["Happy birth day to you"])
happy_bday_2 = Song(["I don't want to get sued"])
happy_bday_3 = Song(["So I'll stop right there"])

bulls_on_parade_1 = Song(["They rally around tha family"])
bulls_on_parade_2 = Song(["With pockets full of shells"])

sentence = Song("All the good things come to those who still waiting for.")

happy_bday_1.sing_me_a_song()
happy_bday_2.sing_me_a_song()
happy_bday_3.sing_me_a_song()

bulls_on_parade_1.sing_me_a_song()
bulls_on_parade_2.sing_me_a_song()

word = sentence.break_word()
print(word[0])
