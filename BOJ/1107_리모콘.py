import sys

input = sys.stdin.readline


n = int(input())
m = int(input())

inf = int(1e9)

dp = [inf] * 1000002
dp[100] = 0

if m > 0:
    broken = list(map(int,input().split()))
else:
    broken = []
for i in range(1000001):
    if i == 101:
        print()
    num_list = list(str(i))
    if all(int(k) not in broken for k in num_list):
        dp[i] = min(len(num_list),dp[i-1]+1,dp[i])
    else:
        dp[i] = min(dp[i-1]+1,dp[i])

for i in range(1000000,-1,-1):
    if i == 101:
        print()
    dp[i] = min(dp[i+1]+1,dp[i])

print(dp[n])
    

