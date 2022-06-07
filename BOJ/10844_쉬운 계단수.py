import sys


N = int(sys.stdin.readline())

dp = [0] * 101
arr = [0] * 101
arr[1] = 9
arr[2] = 8

for i in range(3,N+1):
    dp[i] = (dp[i-1] + 18)%100000000

print(dp[N])