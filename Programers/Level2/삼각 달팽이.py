def solution(n):
    answer = []
    n = int(n)
    list_n = [[0 for i in range(_) ] for _ in range(1,n+1)]
    end_num = (n * (n+1))//2 + 1
    now = 1
    x,y = 0,0
    while now != end_num:
        for i in range(n):
            list_n[y][x] = now
            y+=1
            now+=1
        y-=1
        n -= 1
        for i in range(n):
            x+=1
            list_n[y][x] = now            
            now+=1
        n -= 1
        for i in range(n):
            x-=1
            y-=1
            list_n[y][x] = now
            now+=1
        n -= 1
        y+=1
    for i in list_n:
        answer += i
    return answer