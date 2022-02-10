import sys


n = int(sys.stdin.readline())
arr = [[] for _ in range(n)]
maxnum = [[] for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int,sys.stdin.readline().split()))

maxnum[n-1] = arr[n-1]

for i in range(n-1,0,-1):
    for j in range(i):
        maxnum[i-1].append(arr[i-1][j] + max(maxnum[i][j],maxnum[i][j+1]))
    
print(maxnum[0][0])