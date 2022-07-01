from re import M
import sys

input = sys. stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0] *(n +1)
dp[0] = arr[0]
m = 0
for i in range(1,n):
    if dp[i-1] > 0 and dp[i] + dp[i-1] > 0:
        dp[i] = arr[i] + dp[i-1]
    else:
        dp[i] = arr[i]
    if m < dp[i]:
        m = dp[i]

print(m)
    