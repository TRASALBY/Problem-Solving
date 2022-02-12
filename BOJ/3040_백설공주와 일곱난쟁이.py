import sys


dwarf = []
sum = 0
for i in range(9):
    n = int(sys.stdin.readline())
    sum += n
    dwarf.append(n)
sum -= 100
point = False
fake_dwarf = []
for i in range(0,9):
    for j in range(i+1,9):
        if sum == dwarf[i] + dwarf[j]:
            fake_dwarf.append(i)
            fake_dwarf.append(j)
            point = True
            break
    if point == True:
        break

for i in range(9):
    if i in fake_dwarf:
        continue
    else:
        print(dwarf[i])