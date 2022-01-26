from collections import deque


def bfs(x):
    queue = deque()
    queue.append(x)
    while queue:
        x = queue.popleft()
        

        for i in range(3):
            if i == 2:
                nx = x * 2
            else:
                nx = x + dx[i]
            
            
            
            if nx > 100000 or nx < 0:
                continue

            if check[nx]:
                continue

            if graph[nx] != -2:
                graph[nx] = graph[x] + 1
                queue.append(nx)
                check[nx] = True

            elif graph[nx] == -2:
                return graph[x] + 1

n, k = map(int,input().split())

graph = [0] * 100001
check = [False] * 100001

graph[k] = -2

dx = [-1, 1]

if n == k:
    print(0)
else:
    print(bfs(n))