import sys

input = sys.stdin.readline

n = int(input())
arr = [[0] for _ in range(n)]
dp_red = [0] * 1001
dp_green = [0] * 1001
dp_blue = [0] * 1001
for i in range(n):
    arr[i] = list(map(int,input().split()))

dp_red[1] = arr[0][0]
dp_green[1] = arr[0][1]
dp_blue[1] = arr[0][2]

for i in range(2,n+1):
    dp_red[i] = min(dp_blue[i-1],dp_green[i-1]) + arr[i-1][0]
    dp_green[i] = min(dp_blue[i-1],dp_red[i-1]) + arr[i-1][1]
    dp_blue[i] = min(dp_red[i-1],dp_green[i-1]) + arr[i-1][2]


print(min(dp_red[n],dp_blue[n],dp_green[n]))
