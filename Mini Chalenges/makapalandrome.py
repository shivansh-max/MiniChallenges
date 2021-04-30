word = input("ENTER THE WORD >>>")


word_list = list(word)

list_adding_chars = []

for i in range(len(word_list)):
	# print(word_list[i])
	# print("\n")
	count = 1
	for s in range(len(word_list)):
		if i != s:
			if word_list[i] == word_list[s]:
				if count == 0:
					count = 1
				else:
					count = 0
	if count == 1 and word_list[i] not in list_adding_chars:
		list_adding_chars.append(word_list[i])
	# print(word_list[s])

	# print()

print(list_adding_chars)

if len(list_adding_chars) > 0:
	list_adding_chars.pop(0)

print(f"You must add {list_adding_chars}")