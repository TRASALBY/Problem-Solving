import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
result_list=[]
for q in range(t):
    m, n, k = map(int,input().split())

    graph = [[0]*m for j in range(n)]
    
    for _ in range(k):
        x, y = map(int,input().split())
        graph[y][x] = 1 
    result = 0
    
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                q = deque([(i,j)])
                dx = [-1,1,0,0]
                dy = [0,0,-1,1]

                while(q):
                    x,y = q.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx <n and 0 <= ny < m and graph[nx][ny] ==1:
                            q.append([nx,ny])
                            graph[nx][ny] = 0
                result+= 1
    result_list.append(result)
    
for answer in result_list:
    print(answer)
