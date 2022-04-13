import sys

N = int(sys.stdin.readline())
T = [998 for i in range(N+1)]
P = [0 for i in range(N+1)]
for i in range(1,N+1):
    t, p = map(int, sys.stdin.readline().split())
    if t + i > N+1:
        T[i] = 999
        continue
    else:
        T[i] = t
        P[i] = p
ind = T.index(999)
T = T[:ind]
P = P[:ind]
temp = [998] + [999 for _ in range(len(T)-1)]

sum = 0
while(T != temp):
    profit_T = min(T)
    max_P = 0
    d = 0
    for i in range(1,len(T)):
        if T[i] == profit_T:
            
            if 999 in T[i:i+T[i]]:
                T[i] = 998
                max_P = 0
                d = 0
                break
            

            if P[i] >= max_P:
                max_P = P[i]
                d = i
    sum += max_P
        
    if d != 0:
        for i in range(profit_T):
            if d + i >= len(T):
                break
            T[d+i] = 999
            P[d+i] = 0

print(sum)