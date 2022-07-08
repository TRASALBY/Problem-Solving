import sys
from collections import deque

input = sys.stdin.readline

def bfs(x,y):
    q.append([x,y])
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    while(q):
        x,y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] == graph[x][y] and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append([nx,ny])





n = int(input())
q = deque()
cnt = [0,0]
graph = []
for i in range(n):
    graph.append(list(input().strip()))

visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j] :
            bfs(i,j)
            cnt[0]+=1

visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if not visited[i][j] :
            bfs(i,j)
            cnt[1]+=1

print(*cnt)