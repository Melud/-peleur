def letter_to_word(letter, word_table):
	letter_number = 0
	if 65 <= ord(letter) <= 90:
		letter_number = ord(letter) - 65
	elif 97 <= ord(letter) <= 122:
		letter_number = ord(letter) - 97
	else:
		letter_number = None
	return "" if letter_number is None else word_table[letter_number]


def main(texte_à_épeler):
	word_table = []
	with open('word_table', encoding='utf8') as f:
		for line in f:
			word_table.append(line.rstrip("\n"))
	res = ""
	for lettre in texte_à_épeler:
		word = letter_to_word(lettre, word_table)
		if word == "":
			res += "\n" + lettre
		else:
			res += "\n" + lettre + " comme " + word
	print(f'{res}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
	main(texte_à_épeler="tzowk7tin@mozmail.com"
	     )
