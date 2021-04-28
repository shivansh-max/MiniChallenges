number = input()

number_list = list(number)
number_len = len(number_list)
seperated = ""
current_index = 1

for i in range (number_len):
	seperated += number_list[i]
	if current_index % 3 == 0 and current_index < number_len:
		seperated += ","
	current_index += 1

print(seperated)