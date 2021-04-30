number_of_times = 6


THE_GOLDEN_NUMBER = 11

list1 = []
storag_list = []
the_string = ""
THE_STRING = ""
line_number_list = []
current_number = 0

THE_FINAL_STRING = ""

for i in range(number_of_times):
	current_number = THE_GOLDEN_NUMBER**i

	the_string += str(current_number)

	storag_list = list(the_string)

	for j in range(len(storag_list)):
		THE_STRING += str(storag_list[j])
	the_string += "\n"

	# print(THE_STRING)
	# line_number_list.append(THE_STRING)
	# print(THE_STRING)
	
	storag_list = []
	# print(THE_STRING)
	# storag_list.clear()

THE_FINAL_STRING += the_string
	

print(THE_FINAL_STRING)


# print(line_number_list)
	# list1.append(THE_STRING)

# list1234 = list(the_string)
# print(list1234)
# for i in range(len(line_number_list)):
# 	for j in range(line_number_list[i]):
# 		# print(j)
# 		print(THE_FINAL_STRING)
		
# # # print(list1)