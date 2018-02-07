from sys import argv
script, encoding, error, languages = argv

def main(language_file, encoding, errors):
	line = language_file.readline()
	if line:
		print_line(line, encoding, errors)
		return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
	next_lang = line.strip()
	raw_bytes = next_lang.encode(encoding, errors = errors)
	cooked_line = raw_bytes.decode(encoding, errors = errors)
	print(raw_bytes, "<===>", cooked_line)


file = open(languages, encoding = "utf-8")
main(file, encoding, error)