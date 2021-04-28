number_list = []

amount_of_indexs = int(input("How many numbers are there in the list : "))

for i in range(amount_of_indexs):
	index = int(input(f"What is the {i} element : "))

	number_list.append(index)

added_list = []

sum = 0
for j in range(amount_of_indexs):
	sum = sum + number_list[j]
	added_list.append(sum)
	# print(added_list)

original_list_indexs = len(number_list)
added_list_indexs = len(added_list)
print(f"ORIGINAL LIST : {number_list}, TOTAL INDEXS : {original_list_indexs}")
print(f"CHANGED LIST : {added_list}, ADDED INDEXS : {added_list_indexs}")