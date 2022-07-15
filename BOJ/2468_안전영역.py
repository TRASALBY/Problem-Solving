import sys
from collections import deque

input = sys.stdin.readline


def bfs(n,a,b):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    q = deque([(a,b)])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if -1 < nx < n and -1 < ny < n and visited[ny][nx] == 0:
                q.append((nx,ny))
                visited[ny][nx] = 1


n = int(input())
global graph
global visited
graph = []
for j in range(n):
    graph.append(list(map(int,input().split())))

answer = 1
y = max(sum(graph,[]))
for k in range(1,y):
    now_answer = 0
    visited = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):                
            if graph[y][x] <= k:
                visited[y][x] = 1

    for x in range(n):
        for y in range(n):
            if visited[y][x] == 0:
                bfs(n,x,y)
                now_answer += 1
    
    answer = max(answer,now_answer)
print(answer)
                
        
