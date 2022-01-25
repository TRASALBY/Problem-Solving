from collections import deque


def bfs(tomatoes):
    queue = deque()
    for i in tomatoes:
        queue.append((i[0],i[1]))

    while queue:
        x, y = queue.popleft()
        for i in range(4):            
            nx = x + dx[i]
            ny = y + dy[i]
        
            if (nx < 0 or ny < 0 or nx >= m or ny >= n):
                continue
            if(graph[ny][nx] == -1):
                continue
            if(graph[ny][nx] >= 0):   
                if(graph[ny][nx] == 0):
                    graph[ny][nx] = graph[y][x] + 1
                    queue.append((nx,ny))
                    continue
                if(graph[ny][nx] < graph[y][x] + 1):
                    continue
 
    
                


m,n = map(int,input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input().split())))
tomatoes = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            tomatoes.append((j,i))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
bfs(tomatoes)

check = 0
max = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            check+=1
        if graph[i][j] >= max:
            max = graph[i][j]
if check != 0:
    print(-1)
else:
    print(max-1)
        
