import sys


N, K = map(int,sys.stdin.readline().split())
dp = [[] for _ in range(K+1)] 

for i in range(N):
    w,v = map(int,sys.stdin.readline().split())
    dp[w].append(v)

    

for i in range(1,K+1):
    for j in range(1,(i//2)+1):
        if dp[i] < dp[i-j] + dp[j]:
            dp[i] = dp[i-j] + dp[j]
print(dp[-1])