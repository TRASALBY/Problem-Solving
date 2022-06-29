import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [[]for _ in range(n + 1)]

if n == 1:
    print(0)
else:
    for _ in range(n-1):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])
        graph[b].append([a, c])


    leaf = []
    for a in range(1, n + 1):
        if len(graph[a]) == 1:
            leaf.append(a)

    max_len = 0
    start = leaf[0]
    for i in range(2):
        q = deque([start])
        visited = [0] * (n+1)
        dist = [0] * (n+1)

        visited[start] = 1
        while(q):
            v = q.popleft()

            for i in graph[v]:
                if visited[i[0]] == 0:
                    visited[i[0]] = 1
                    q.append(i[0])
                    dist[i[0]] += dist[v] + i[1]
        now_max = max(dist)
        if max_len < now_max:
            max_len = now_max
            start = dist.index(now_max)
        elif max_len == now_max:
            break

print(max_len)