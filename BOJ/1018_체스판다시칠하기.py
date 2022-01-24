def check_board(boards):
    n = m = 8
    cnt1 = cnt2 = 0
    for i in range(n):
        for j in range(m):
            if (i % 2 == 0):
                if (j % 2 == 0 and boards[i][j] == 'B'):
                    cnt1+=1
                    
                elif(j%2 ==1 and boards[i][j] != 'B'):
                    cnt1+=1
            else:
                if (j % 2 == 0 and boards[i][j] == 'W'):
                    cnt1+=1
                    
                elif(j%2 ==1 and boards[i][j] != 'W'):
                    cnt1+=1


    for i in range(n):
        for j in range(m):
            if (i % 2 == 0):
                if (j % 2 == 0 and boards[i][j] == 'W'):
                    cnt2+=1
                    
                elif(j%2 ==1 and boards[i][j] != 'W'):
                    cnt2+=1
            else:
                if (j % 2 == 0 and boards[i][j] == 'B'):
                    cnt2+=1
                    
                elif(j%2 ==1 and boards[i][j] != 'B'):
                    cnt2+=1
    if cnt1 <= cnt2:
        return cnt1
    else:
        return cnt2

n, m = map(int, input().split())
boards = []
for i in range(n):
    boards.append(input())


min = m * n
for l in range(m-7):
    for k in range(n-7):
        new_boards =[]
        for i in range(8):
            board = []
            for j in range(8):
                board.append(boards[i+k][j+l])
            test = ''.join(board)
            new_boards.append(test)
        count_board = check_board(new_boards)
        if count_board < min:
            min = count_board
    
print(min)