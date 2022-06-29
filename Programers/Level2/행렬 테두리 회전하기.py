import copy

def rotate(query,arr):
    
    
    for i in range(len(query)):
        query[i] -= 1
    x1,y1,x2,y2 = query
    arr_copy = copy.deepcopy(arr)
    m = int(1e9)

    for x in range(x1,x2+1):
        # x = 0, y = 2 x1 == 0, x2 = 1 y1 = 1 y2 = 2
        for y in range(y1,y2+1):
            if x == x1 and y1 <= y < y2:
                arr[x][y+1] = arr_copy[x][y]
                m = min(m,arr_copy[x][y])
            elif x1 <= x < x2 and y == y2:
                arr[x+1][y] = arr_copy[x][y]
                m = min(m,arr_copy[x][y])
            elif x == x2 and y1 < y <= y2:
                arr[x][y-1] = arr_copy[x][y]
                m = min(m,arr_copy[x][y])
            elif x1 < x <= x2 and y == y1:
                arr[x-1][y] = arr_copy[x][y]
                m = min(m,arr_copy[x][y])

    return m,arr

def solution(rows, columns, queries):
    
    answer = []
    arr = [[i+j*columns for i in range(1,columns+1)] for j in range(rows)]
    for query in queries:
        m,arr =  rotate(query,arr)
        answer.append(m)
    
    
    return answer