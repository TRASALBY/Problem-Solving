def solution(dirs):
    answer = 0
    x,y = 0,0
    road = []
    for i in range(len(dirs)):
        nx,ny = x,y
        if dirs[i] == 'U':
            ny += 1
        if dirs[i] == 'D':
            ny -= 1
        if dirs[i] == 'R':
            nx += 1
        if dirs[i] == 'L':
            nx -= 1
        
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            start_end = sorted([[x,y],[nx,ny]])
            if start_end not in road:
                answer += 1
                road.append(sorted([[x,y],[nx,ny]]))            
            x,y = nx,ny
            
            
    return answer