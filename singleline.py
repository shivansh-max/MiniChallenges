eq = " + 12x + 24 + "

eq = eq.replace(" ", "")



listeq = list(eq)

# print(listeq[30])

c = 0
v = 0
# 48-57
plus = ord("+")
subt = ord("-")
equa = ord("=")
xxxx = ord("x")

list_segments = []



for i in range(len(listeq)):

    """
    if ord(listeq[i]) >= 48 and ord(listeq[i]) <= 57 and i != len(listeq) - 1 and ord(listeq[i + 1]) == 120:
        if ord(listeq[i - 1]) == plus:
            v += int(listeq[i])
        else:
            v -= int(listeq[i])
    elif ord(listeq[i]) >= 48 and ord(listeq[i]) <= 57:
        if ord(listeq[i - 1]) == plus:
            c += int(listeq[i])
        else:
            c -= int(listeq[i])
    """

    if ord(listeq[i]) == plus or ord(listeq[i]) == subt and i != len(listeq):

        current=i

        if i != len(listeq)-1:

            current = i + 1


        cc = listeq[i]
        while True:

            cc += listeq[current]

            if ord(listeq[current]) == plus or ord(listeq[i]) == subt:
                break

            if current == len(listeq) - 1:
                break
            else:
                current += 1

        # print(cc)
        list_segments.append(cc)
        # cc = ""
        # current=0
list_segments.pop(len(list_segments)-1)

list_segments.pop(0)


for i in range(len(list_segments)):
    cl = list(list_segments[i])
    if cl[len(cl) - 2] == "x":
        if cl[0] == "+":
            cl.pop(0)
            cl.pop(len(cl) - 2)
            cl.pop(len(cl) - 1)
            cs = ""
            for i in range(len(cl)):
                cs += cl[i]

            v += int(cs)
        if cl[0] == "-":
            cl.pop(0)
            cl.pop(len(cl) - 2)
            cl.pop(len(cl) - 1)
            cs = ""
            for i in range(len(cl)):
                cs += cl[i]

            v -= int(cs)
    else:
        if cl[0] == "+":
            cl.pop(0)
            cl.pop(len(cl) - 1)
            cs = ""
            for i in range(len(cl)):
                cs += cl[i]

            c += int(cs)
        if cl[0] == "-":
            cl.pop(0)
            cl.pop(len(cl) - 1)
            cs = ""
            for i in range(len(cl)):
                cs += cl[i]

            c -= int(cs)

# v *= -1

print(c / v)
