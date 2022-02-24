import sys


n = int(sys.stdin.readline())

x = list(map(int, sys.stdin.readline().split()))
for i in range(n):
    x[i] = [x[i],i]
x2 = sorted(x, key=lambda x : x[0])
ind = 0
for i in range(len(x2)):

    if i >= 1 and x2[i][0] == x2[i-1][0]:
        x2[i].append(x2[i-1][2])
        ind-=1
    else:
        x2[i].append(ind)
    ind+=1

x2.sort(key=lambda x: x[1])

for i in x2:
    print(i[2],end=" ")