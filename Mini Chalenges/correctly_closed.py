import sys

finding = input("ENTER STRING >>>")
finding_list = list(finding)


def DOIT(list):
    # dictionary = {"OPEN" : "", "INDEX" : 0}
    a = []
    IMPORTANTLIST = ["(", "{", "["]
    for i in range(len(list)):
        if list[i] == IMPORTANTLIST[0] or list[i] == IMPORTANTLIST[1] or list[i] == IMPORTANTLIST[2]:
            print(list[i])
            a.append(list[i])
        elif list[i] == ")":
            if a[len(a) - 1] == "]" or a[len(a) - 1] == "}":
                return False
            else:
                a.pop(len(a) - 1)

        elif list[i] == "]":
            if a[len(a) - 1] == ")" or a[len(a) - 1] == "}":
                return False
            else:
                a.pop(len(a) - 1)

        elif list[i] == "}":
            if a[len(a) - 1] == "]" or a[len(a) - 1] == ")":
                return False
            else:
                a.pop(len(a) - 1)


    if len(a) > 0:
        return False
    else:
        return True
    # return dictionary


if DOIT(finding_list):
    print(f"THIS STRING : {finding}; IS CORRECTLY CLOSED.")
else:
    print(f"THIS STRING : {finding}; IS NOT CORRECTLY CLOSED")
