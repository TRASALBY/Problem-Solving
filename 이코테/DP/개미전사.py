import sys


N = int(sys.stdin.readline())
K = [0] + list(map(int, sys.stdin.readline().split()))
dp = [0] * (N+1)
dp[1] = K[1]
dp[2] = max(K[1],K[2])
for i in range(3,N+1):
    dp[i] = max(dp[i-1], dp[i-2] + K[i])

print(dp[N])