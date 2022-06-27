import sys
from collections import deque

input = sys.stdin.readline
answer = 0
n,m = map(int,input().split())

graph = [[0 for i in range(n+1)] for j in range(n+1)]
visited = [0 for i in range(n+1)]
for i in range(m):
    u,v = map(int,input().split())
    graph[u][v] = 1
    graph[v][u] = 1

for i in range(1,n+1):
    if visited[i] == 0:
        q = deque([i])

        while(q):
            v = q.popleft()
            for j in range(len(graph[v])):
                if graph[v][j] == 1 and visited[j] == 0:
                    q.append(j)
                    visited[j] = 1
        
        answer += 1

print(answer)