
from collections import deque


def move(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        
        if board[y][x] == -1:
            return 0

        for i in range(8):
            nx = x + dx1[i]
            ny = y + dy1[i]

            if(nx < 0 or nx >=I or ny<0 or ny >= I):
                continue
            if(board[ny][nx] > 0):
                continue
            if(board[ny][nx] != -1):
                    board[ny][nx] = board[y][x] + 1
                    queue.append((nx,ny))
            if(board[ny][nx] == -1):
                board[ny][nx] = board[y][x] + 1
                return board[ny][nx]
    
    

n = int(input())
result = []


for _ in range(n):
    I = int(input())
    x,y = map(int,input().split())
    start = (x,y)
    x,y = map(int,input().split())
    goal = (x,y)
    board = [[0]*I for i in range(I)]
    board[goal[1]][goal[0]] = -1

    dx1 = [-2,-2,-1,-1,1,1,2,2]
    dy1 = [1,-1,2,-2,2,-2,1,-1]
    
    result.append(move(start[0],start[1]))
    
for i in result:
    print(i)


