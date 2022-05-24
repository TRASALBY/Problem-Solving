def solution(board):
    answer = 1234
    board_list = []
    for i in range(len(board)):
        start = -1
        end = -1
        for j in range(len(board[i])):
            if start == -1 and board[i][j] == 1:
                start = j
            if start != -1 and board[i][j] == 0:
                end = j -1 
            if end != -1 and board[i][j] == 1:
                start == j
                end = -1
            if end != -1 and board[i][j] == 0:
                end = j-1
            if j == len(board[i])-1:
                end = j
            if start != -1 and end != -1:
                board_list.append([i,start,end])
                start = -1
                end = -1
    return board_list

solution(	[[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]])