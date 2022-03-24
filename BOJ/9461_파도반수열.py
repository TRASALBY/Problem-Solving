import sys

input = sys.stdin.readline

t = int(input())

dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
for i in range(t):
    n = int(input())
    if dp[n] != 0 or n<5:
        print(dp[n])
    else:
        for j in range(5,n+1):
            dp[j] = dp[j-5] + dp[j-1]
        print(dp[n])