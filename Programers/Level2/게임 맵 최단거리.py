from collections import deque

def bfs(m):    
    global distance
    global visited
    inf = -1

    q = deque([])
    
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    
    q.append([0,0])

    while(q):
        y,x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if -1 < nx < len(m[0]) and -1 < ny < len(m) and visited[ny][nx] == 0:
                if m[ny][nx] == 1:
                    visited[ny][nx] = 1 
                    
                    q.append([ny,nx])
                    distance[ny][nx] = distance[y][x] + 1
                    
        

def solution(maps):
    global distance
    global visited
    
    m = maps
    inf = -1
                
    distance = [[inf] * len(m[0]) for _ in range(len(m))]
    visited = [[0] * len(m[0]) for _ in range(len(m))]
    distance[0][0] = 0
    visited[0][0] = 1
    answer = 0
    
    bfs(m)
    
    if distance[-1][-1] == -1:
        return -1
    return distance[-1][-1] + 1