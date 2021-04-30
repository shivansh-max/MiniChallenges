number = input("Enter the number : ")

number_list = list(number)

number_len = len(number_list)

sumn = 0
product = 1
diffrence = 0
greater = True

for i in range(number_len):
    sumn += int(number_list[i])
# print(sumn)

for i in range(number_len):
    product = product * int(number_list[i])
    # print(product)
# print(sumn)

diffrence = product - sumn

print(f"DIFFRENCE : diffrence")

if diffrence < 0:
    greater = False

# print(0-9)

print(f"Diffrence is greater than 0 : {greater}")



"""
1234
7890
1234567890
123456789
"""