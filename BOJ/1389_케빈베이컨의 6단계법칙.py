import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[0] * (n+1) for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

k = []
for start in range(1,n+1):
    q = deque([start])
    visited = [0] * (n+1)
    dist = [0] * (n+1)

    visited[start] = 1
    while(q):
        v = q.popleft()
        for i in range(1,len(graph[v])):
            if graph[v][i] != 0 and visited[i] == 0:
                visited[i] = 1
                dist[i] = dist[v]+1
                q.append(i)
    k.append(sum(dist))

print(k.index(min(k))+1)






