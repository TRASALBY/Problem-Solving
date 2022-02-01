def solution(board, moves):
    basket_stack = []
    size = len(board[0])
    line = [[]for _ in range(size)]
    answer = 0
    for i in range(size-1,-1,-1):
        for j in range(size):
            if board[i][j] == 0:
                continue
            line[j].append(board[i][j])

    for move in moves:
        if len(line[move-1]) == 0:
            continue
        basket_stack.append(line[move-1].pop())
        if len(basket_stack)>=2 and basket_stack[-1] == basket_stack[-2]:
            for _ in range(2):
                basket_stack.pop()
                answer+=1

    return answer