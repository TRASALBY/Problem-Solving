import sys


M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

min_val = 10001
sum_val = 0
for i in range(M,N+1):
    if i == 1:
        continue
    check = True
    for j in range(2,i):
        if i % j != 0:
            continue
        else:
            check = False
            break
    if check == True:
        if min_val >= i:
            min_val = i
        sum_val += i
  
if sum_val == 0:
    print(-1)  
else:
    print(sum_val)
    print(min_val)
        