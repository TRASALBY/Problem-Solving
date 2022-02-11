import sys


n = int(sys.stdin.readline())

dp = [[] for _ in range(n+1)]
stairs = [0]
for i in range(1,n+1):
    stairs.append(int(sys.stdin.readline()))
dp[0].append((0,0))
dp[1].append((stairs[1],0))
for i in range(2,n+1):
    for j in range(len(dp[i-1])):
        if j==0:
            if len(dp[i-2]) <= 1:
                dp[i].append((dp[i-2][j][0]+stairs[i],0))
            else:
                dp[i].append((max(dp[i-2][j][0],dp[i-2][j+1][0])+stairs[i],0))
        if dp[i-1][j][1] == 0:
            dp[i].append((dp[i-1][j][0]+stairs[i],1))
top = 0
for i in range(len(dp[-1])):
    if top <= dp[-1][i][0]:
        top = dp[-1][i][0]
print(top)