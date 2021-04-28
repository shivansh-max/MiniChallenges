import numpy as np

cor = input("Enter the coordinates : ")

cor_list = list(cor)

spots = []

length = len(cor_list)

height = 0
width = 0

# increase_teller = {'N': "h+1", 'S':"h-1", 'E':"w+1", 'W':"w-1"}

def create_grid():
	grid = np.zeros((length,length) ,dtype = str , order="F")
	return grid

grid = create_grid()
finish = False



def convert_to_checkable_list(lista):
	changed_list = []

	# for i in range(len(lista)):
	# 	print(lista[i])


	for i in range(len(lista)):
		storrer = lista[i]
		changed_list.append(str(storrer))

	# for i in range(len(lista)):
	# 	print(type(changed_list[i]))

	return changed_list



def check_if_duplicate(list_to_check):
	a_list = list_to_check

	a_set = set(a_list)

	contains_duplicates = len(a_list) != len(a_set)

	return contains_duplicates

# print(contains_duplicates)

filler = "%"
for j in range(length):
	grid[height][width] = filler

	current_index = [height, width]

	length_for_spots = len(spots)

	if cor_list[j].upper() == 'N':
		filler = "|"
		height -= 1
	if cor_list[j].upper() == 'S':
		filler = "|"
		height += 1
	if cor_list[j].upper() == 'W':
		width -= 1
		filler = "_"
	if cor_list[j].upper() == 'E':
		width += 1
		filler = "_"

	spots.append([height, width])

def print_output():
	print(f"COORDINATES : {cor_list}")
	# print(f"GRID : \n{grid}")
	print(f"SPOT LIST : {spots}")
	print(f"REPEATS : {check_if_duplicate(convert_to_checkable_list(spots))}")

print_output()