import sys
from collections import deque

input = sys.stdin.readline
t = int(input())

for i in range(t):
    p = input().strip()


    n = int(input())
    x = input().strip()
    if n == 0:
        x = []
    elif n > 1:
        x = x.split(',')
        x[0] = x[0][1:]
        x[-1] = x[-1][:-1]
    else:
        x = [x[1:-1]]
    
    x = deque(x)
    rcnt = 0
    for j in range(len(p)):
        if p[j] == "R":
            rcnt+=1
        elif p[j] == "D":
            if len(x) == 0:
                print("error")
                break
            else:
                if rcnt % 2 == 1:
                    x.pop()
                else:
                    x.popleft()

    else:
        if rcnt % 2 == 1:
            x.reverse()
        print("[",end = "")
        for i in range(len(x)):
            print(x[i],end="")
            if i != len(x)-1:
                print(",",end="")
        print("]")
