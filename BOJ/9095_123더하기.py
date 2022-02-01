import sys
T = int(sys.stdin.readline())


for i in range(T):
    dp = [1,2,4]
    n = int(sys.stdin.readline())
    for i in range(3,n):
        dp.append(dp[i-3] + dp[i-2] + dp[i-1])
    print(dp[n-1])