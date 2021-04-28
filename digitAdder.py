number = input("Enter the number : ")

number_digit_list = list(number)

number_lenght = len(number_digit_list)

sum = 0

for i in range(number_lenght):
	sum += int(number_digit_list[i])

print(f"SUM : {sum}")