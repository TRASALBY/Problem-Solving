import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수(n)과 간선의 개수(m) 입력
n = int(input())

# 2차원 리스트 (그래프 표현) 만들고, 무한대로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(n-1):
    # A -> B로 가는 비용을 C라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c


leaf = []
for a in range(1, n + 1):
    if graph[a].count(INF) == len(graph[a])-2:
        leaf.append(a)

max_len = 0
for start in leaf:
    q = deque([start])
    visited = [0] * (n+1)
    dist = [0] * (n+1)

    while(q):
        v = q.popleft()

        for i in range(len(graph[v])):
            if graph[v][i] != INF and visited[i] == 0:
                visited[i] = 1
                q.append(i)
                dist[i] += dist[v] + graph[v][i]

    for d in dist:
        if d > max_len:
            max_len = d




print(max_len)



'''
# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

max_len = 0
for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b] > max_len:
                max_len = graph[a][b]

print(max_len)
'''