class Module(object):

	def __init__(self, sentences):
		self.sentences = sentences

	def break_words(self):
		words_list = self.sentences.split(' ')
		return words_list

	def print_first_word(words_list):
		first_word = words_list[0]
		print(first_word)

	def print_last_word(words_list):
		last_word = words_list[-1]
		print(last_word)

	def sort_sentence(words_list):
		return sorted(words_list)

sentence = Module("All the good things come to those who still waiting for.")

words_list = sentence.break_words()
print(words_list)

Module.print_first_word(words_list)

Module.print_last_word(words_list)