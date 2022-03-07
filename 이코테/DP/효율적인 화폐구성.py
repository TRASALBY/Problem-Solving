import sys


N, M = map(int,sys.stdin.readline().split())
dp = [10001] * 10001
dp[0] = 0
coin = []
for i in range(N):
    coin.append(int(sys.stdin.readline()))
for i in range(N):
    for j in range(coin[i],M+1):
        if dp[j-coin[i]]!= 10001:
            dp[j] = min(dp[j],dp[j-coin[i]]+1)

if dp[M] == 10001:
    print(-1)
else:
    print(dp[M])