# Taking the input to reverse
to_reverse = input("Please enter the scentence that you would like to reverse : ")

# Functions
# This is the main function that will reverse the word
def reverse(to_reverse):
	word_list = to_reverse.split()
	amount_of_words = len(word_list)
	reverse_list = []
	reversed = False
	how_much_to_move_to_the_next_index = 1
	current_index = amount_of_words -1


	while not(reversed):
		reverse_list.append(word_list[current_index])
		current_index -= how_much_to_move_to_the_next_index

		if current_index == -1:
			reversed = True

	reverse_sentence = ""
	full_scentence = False
	current_index = amount_of_words -1
	for i in range(amount_of_words):
		reverse_sentence += reverse_list[i] + " "
		# current_index -= how_much_to_move_to_the_next_index

		# if current_index == -1:
		# 	reversed = True
	print(reverse_sentence)

reverse(to_reverse)