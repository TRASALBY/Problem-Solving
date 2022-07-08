import sys

input = sys.stdin.readline


k = int(input())
stk = []
last_num = 0
for i in range(k):
    n = int(input())
    if n != 0:
        stk.append(n)
    else:
        stk.pop()
        
print(sum(stk))