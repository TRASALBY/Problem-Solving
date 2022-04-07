import sys

input = sys.stdin.readline

arr1 = input().strip()
arr2 = input().strip()

len1 = len(arr1)
len2 = len(arr2)

dp = [[0 for _ in range(len1)] for _ in range(len2)]
check_point = False
for j in range(0,len1):
    if check_point == True:
        dp[0][j] = dp[0][j-1]
        continue
    if j == 0:
        if arr2[0] == arr1[j]:
            dp[0][j] = 1
            check_point = True
        else:
            dp[0][j] = 0
        continue
    if arr2[0] == arr1[j]:
        dp[0][j] = dp[0][j-1] + 1
        check_point = True
    else:
        dp[0][j] = dp[0][j-1]
for i in range(1,len2):
    for j in range(0,len1):
        if arr2[i] == arr1[j]:
            dp[i][j] = dp[i][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])

print(dp[-1][-1])