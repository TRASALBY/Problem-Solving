import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
answer = []
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

for i in range(n):
    visited = [0] * n
    q = deque([i])

    while(q):
        v = q.popleft()

        for i in range(len(graph[v])):
            if graph[v][i] == 1 and visited[i] == 0:
                visited[i] = 1
                q.append(i)
    answer.append(visited)

for i in range(len(answer)):
    print(*answer[i])