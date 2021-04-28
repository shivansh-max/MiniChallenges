lista = int(input("ENTER THE AMOUNT OF INDEXS IN THE FIRST MATRIX >>>"))
mainA = []
for i in range(lista):
    mainA.append(int(input("ENTER THE NUMBER >>>")))
# print(mainA)

listb = int(input("ENTER THE AMOUNT OF INDEXS IN THE FIRST MATRIX >>>"))
mainB = []
for i in range(listb):
    mainB.append(int(input("ENTER THE NUMBER >>>")))
# print(mainB)

thing = input("ENTER THE SYMBOL OF WHAT YOU WANT TO DO >>>")

if len(mainA) < len(mainB):
    greater = len(mainB) - len(mainA)
    for i in range(greater):
        mainA.append(0)
if len(mainB) < len(mainA):
    greater = len(mainA) - len(mainB)
    for i in range(greater):
        mainB.append(0)
# print(mainA)
# print(mainB)


mainMatric = []

if thing == "+":
    for i in range(len(mainA)):
        mainMatric.append(mainA[i] + mainB[i])
elif thing == "-":
    for i in range(len(mainA)):
        mainMatric.append(mainA[i] - mainB[i])

print(mainMatric)