import sys

thestarternumbers = input("Enter two digit number to start the seiries : ")

stringer = list(thestarternumbers)
lista = [int(stringer[0]), int(stringer[1])]
listb = lista

times_to_do = int(input("Enter how long to do"))

sys.setrecursionlimit(times_to_do +4)

start1, start2 = lista[0], lista[1]
sum = start1 + start2

i = 0

def main():
	global i
	global sum
	global listb
	# print(i)
	listb.append(sum)
	sum = listb[len(listb) - 1] + listb[len(listb) - 2]
	if i == times_to_do:
		return 0
	i += 1
	main()
main()
print(listb)
# print(main())