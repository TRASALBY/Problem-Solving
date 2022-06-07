def solution(board):
    answer = 0
    height = len(board)
    width = len(board[0])

    for n in range(1,min(height,width)+1):
        cnt = 0
        arr = [1 for _ in range(n)]
        for i in range(height):
            for j in range(width):
                for k in range(0,n):

                    temp = board[i+k][j:j+n] 
                    if temp == arr:
                        cnt+=1
                    else:
                        break
                if cnt == n:
                    answer = pow(cnt,2)
                    break
                else:
                    cnt = 0
            if cnt == n:
                break
            
    return answer

print(solution(	[[0]]))