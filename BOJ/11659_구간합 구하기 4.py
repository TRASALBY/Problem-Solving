import sys


N,M = map(int, sys.stdin.readline().split())

n = list(map(int ,sys.stdin.readline().split()))
prefix_sum = [0]
sum_value = 0
for i in n:
    sum_value += i
    prefix_sum.append(sum_value)
for _ in range(M):
    i,j  =  map(int, sys.stdin.readline().split())
    print(prefix_sum[j]-prefix_sum[i-1])
