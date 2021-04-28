thestarternumbers = input("Enter two digit number to start the seiries : ")
NOOFTIMES = int(input("Enter how long to do"))


stringer = list(thestarternumbers)
lista = [int(stringer[0]), int(stringer[1])]
listb = lista


start1, start2 = lista[0], lista[1]
sum = start1 + start2

for i in range(NOOFTIMES):
	listb.append(sum)
	sum = listb[len(listb) - 1] + listb[len(listb) - 2]

print(listb)