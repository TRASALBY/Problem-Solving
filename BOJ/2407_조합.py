import sys

input = sys.stdin.readline
n,m = map(int,input().split())

answer = 1

dp = [1] * (n+1)


for i in range(2,n+1):
    dp[i] = dp[i-1] * i
    
print((dp[n]//(dp[m]*dp[n-m])))