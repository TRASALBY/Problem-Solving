def solve(queen,n,y):
    count = 0
    
    if n == y:
        return 1
    for col in range(n):
        queen[y] = col

        # for-else구문
        for x in range(y):
            # 세로로 겹치면 안됨
            if queen[x] == queen[y]: 
                break
                
            # 대각선으로 겹치면 안됨
            if abs(queen[x]-queen[y]) == (y-x):
                break
        else:
            count += solve(queen, n, y+1)

    return count

n = int(input())
queen = [0]*n


print(solve(queen,n,0))