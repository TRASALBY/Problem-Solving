import sys


N,L = map(int,sys.stdin.readline().split())         

def solution(N,L):

    val = 0
    for i in range(0,N+1):
        val += i
        sum_val[i] = val
    

    temp = 101
    start = 0
    end = 0
    for i in range(N):
        for j in range(i+L,len(sum_val)):
            val = sum_val[j] - sum_val[i]
            if val > N:
                break
            elif val == N:
                if temp > j-i-1 and j-i >=L:
                    start = i+1
                    end = j
                    temp = j-i-1
    if temp != 101:
        return start, end
    else:
        return -1,-1

i, j = solution(N,L)

if i == -1:
    print(-1)
else:
    for num in range(i-1,j):
        print(num, end=" ")