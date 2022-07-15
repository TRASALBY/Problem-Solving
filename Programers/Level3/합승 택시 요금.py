from collections import deque

def bfs(n,s,graph):
    
    inf = int(1e15)
    visited = [0] * (n+1)
    visited[s] = 1
    dist = [inf] * (n +1)
    dist[s] = 0
    q = deque([s])
    while(q):
        v = q.popleft()
        for i in range(len(graph[v])):
            if graph[v][i] != inf:
                if dist[i] > dist[v] + graph[v][i]:
                    dist[i] = dist[v] + graph[v][i]
                    q.append(i)
                
    return dist
    

def solution(n, s, a, b, fares):        #출발s 도착 a,b 
    inf = int(1e15)
    answer = inf
    graph = [[inf]* (n+1) for _ in range(n+1)]   
    
    for fare in fares:
        q,w,e = fare
        graph[q][w] = e
        graph[w][q] = e
        
    dist_start = bfs(n,s,graph)
    dist_end1 = bfs(n,a,graph)
    dist_end2 = bfs(n,b,graph)  
    
        
    answer = dist_start[a]+dist_start[b]

    for i in range(1,n+1):
        answer = min(dist_start[i] + dist_end1[i] + dist_end2[i],answer)
        
    return answer