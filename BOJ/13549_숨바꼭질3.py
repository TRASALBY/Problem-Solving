from collections import deque


def bfs(x):
    queue = deque()
    queue.append(x)
    
    while queue:
        x = queue.popleft()

        temp = 1
        for i in range(3):
            
            if i == 0:
                nx = x * 2

                if nx >= 200001 or nx < 0:
                    continue

                if nx != k:
                    

                    if check[nx] == False:                        
                        queue.append(nx)
                        check[nx] = True
                        graph[nx] = graph[x]
                    else:
                        graph[nx] = min(graph[x],graph[nx])

                elif nx == k:
                    graph[nx] = min(graph[x],graph[nx])
            else:
                nx = x + temp

                temp = -temp

                if nx >= 200001 or nx < 0:
                    continue


                if nx != k:                                    
                    if check[nx] == False:  
                        graph[nx] = graph[x] + 1                      
                        queue.append(nx)
                        check[nx] = True
                    else:
                        graph[nx] = min(graph[x]+1,graph[nx])
                    

                elif nx == k:
                    graph[nx] = min(graph[x]+1,graph[nx])
            
            
    return graph[k]


n, k = map(int,input().split())

inf = float('inf')

graph = [inf] * 200001
check_count = [0] * 200001
check = [False] * 200001
check[n] = True
check_count[n] = 1
graph[n] = 0
dx = [-1, 1]

if n == k:
    print(0)
else:
    print(bfs(n)) 