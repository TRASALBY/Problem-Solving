import sys

input = sys.stdin.readline

t = int(input())
for i in range(t):
    cloth = dict()
    n = int(input())
    for i in range(n):
        a,b = input().split()
        if b in cloth:
            cloth[b].append(a)
        else:
            cloth[b] = [a]
    answer = 1
    for i in cloth:
        answer *= (len(cloth[i])+1)
    
    print(answer -1)

