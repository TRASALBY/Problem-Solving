import sys
import heapq

input = sys.stdin.readline


INF = float('inf')
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

start, goal = map(int,input().split())

def dij(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dij(start)

print(distance[goal])



