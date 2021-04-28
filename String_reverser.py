# Taking the input to reverse
to_reverse = input("Please enter the word that you would like to reverse : ")

# Functions
# This is the main function that will reverse the word
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

	print(reverse_word)

	# print(word_list)

reverse(to_reverse)