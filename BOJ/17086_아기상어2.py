import sys
from collections import deque



input = sys.stdin.readline

graph = []
n,m = map(int,input().split())

for i in range(n):
    graph.append(list(map(int,input().split())))

shark = []
inf = int(1e9)
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            shark.append([i,j])

dist = [[inf] * m for _ in range(n)]

dx = [1,-1,0,0,1,-1,1,-1]
dy = [0,0,1,-1,1,-1,-1,1]

for s in shark:
    q = deque([[s[0],s[1]]])
    visited = [[0] * m for _ in range(n)]
    visited[s[0]][s[1]] = 1
    dist[s[0]][s[1]] = 0
    while(q):
        x,y = q.popleft()

        for l in range(8):
            nx = x + dx[l]
            ny = y + dy[l]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append([nx,ny])
                dist[nx][ny] = min(dist[x][y] + 1,dist[nx][ny])

answer = max(sum(dist,[]))

print(answer)