import sys

input = sys.stdin.readline

n = int(input())

user = []
for i in range(n):
    t = list(map(str,input().split()))
    t[0] = int(t[0])
    user.append(t)
    
user.sort(key = lambda x : (x[0]))

for i in range(n):
    print(*user[i])
    