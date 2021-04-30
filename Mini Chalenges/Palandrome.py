word = input("ENTER > ")

first_list = list(word)

pala = False

print(first_list)

rev_word = ""

def reverse(to_reverse):
	word_list = list(to_reverse)
	reverse_word = ""
	length_of_list = len(to_reverse)
	# print(length_of_list)
	reversed = False

	next_letter = 1
	while not(reversed):
		reverse_letter = word_list[length_of_list - 1]
		length_of_list -= next_letter
		reverse_word += reverse_letter
		if length_of_list == 0:
			reversed = True

	return reverse_word

if word == reverse(word):
	pala = True

print(pala)