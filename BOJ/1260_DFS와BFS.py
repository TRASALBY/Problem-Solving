from collections import deque


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v,end = ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m, v = map(int, input().split())

graph = [[] for i in range (n+1)]

for i in range(1, m+1):
    snode, enode = map(int,input().split())
    graph[snode].append(enode)
    graph[enode].append(snode)

for i in range(1,n+1):
    graph[i].sort()
visited = [False] * (n+1)

dfs(graph, v, visited)
visited = [False] * (n+1)
print()
bfs(graph,v,visited)