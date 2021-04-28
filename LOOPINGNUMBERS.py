size = 3 # input("ENT0R NUMBER >>>")
row = size
rowst = 0
colst = 0
col = size
lists = []
# current_number = 1

for i in range(row):
    lists.append([])
    for s in range(col):
        lists[i].append(0)
        # current_number += 1
# current_number = 1

i = 0
j = 0
current_number = 1
ch=0;
while current_number <60:
    j = colst
    # print(j,rowst,row,col)
    while j <= col - 1:
        lists[rowst][j] = current_number
        current_number += 1
        j += 1
    rowst += 1
    i = rowst
    while i <= row - 1:
        lists[i][j - 1] = current_number
        current_number += 1
        i += 1
    j -= 1
    while j > colst:
        j -= 1
        lists[row - 1][j] = current_number
        current_number += 1
    i -= 1
    while i > rowst:
        i -= 1
        lists[i][j] = current_number
        current_number += 1
    # rowst += 1
    colst += 1
    col -= 1
    row -= 1
    # print(current_number)
    ch += 1
    if(ch > 5):
        current_number=70
# print(i, j)


for i in range(size):
    print(lists[i])
