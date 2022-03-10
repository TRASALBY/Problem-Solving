import sys
import heapq

from turtle import distance

INF = float('inf')
input = sys.stdin.readline

V, E = map(int,input().split()) #정점개수 V, 간선개수 E
K = int(input())    # 시작 정점 K

graph = [[] for i in range(V+1)]
distance = [INF] * (V+1)


for _ in range(1, E+1):
    u,v,w = map(int, input().split()) # 간선 시작정점 u, 종점 v, 가중치 w
    graph[u].append((v,w))

def dijkstra(start):
    h = []
    heapq.heappush(h,(0,start))
    distance[start] = 0
    while h:
        dist, now = heapq.heappop(h)
        if distance[now] <dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(h,(cost,i[0]))
dijkstra(K)

for i in range(1,V+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
