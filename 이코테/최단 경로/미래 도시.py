import sys

input = sys.stdin.readline
INF = float('inf') # 무한

N, M = map(int, input().split()) #회사의 개수 N, 경로의 개수 M

graph = [[INF] * (N+1) for _ in range(N+1) ] 

for _ in range(M):
    a, b = map(int,input().split()) # 연결된 회사 , 양방향
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1,N+1):      #자기자신으로 가는 것 0으로 초기화
    graph[i][i] = 0

X, K = map(int, input().split()) #도착 X, 방문 K

for i in range(1, N+1):     #플로이드워셜 알고리즘 모든 노드에 대해 다른노드로 가는 최단경로 계산
    for j in range(1, N+1):
        for k in range(1,N+1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

answer = graph[1][K] + graph[K][X] #K를 거쳐 X로 가는 경로 : 1에서 K까지 + K에서 X까지

if answer == INF:
    print(-1)
else:
    print(answer)

