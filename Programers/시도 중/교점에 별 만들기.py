def solution(line):
    answer = []
    result = []
    stars = []
    for line1 in line:
        A,B,E = map(int,line1)
        for line2 in line:
            C,D,F = map(int,line2)
            '''2,-1,4
               0,-1,1'''
            
            '''
            -1 - -4 = 3
            -2 - 0 = -2
            '''
            if line1 == line2:
                continue
            else:
                if  (A*D - B*C) == 0:
                    continue
                if (B*F - E*D) % (A*D - B*C) != 0 or (E*C - A*F) % (A*D - B*C) !=0:
                    continue
                x = (B*F - E*D) / (A*D - B*C)
                y = (E*C - A*F) / (A*D - B*C)
            if [x,y] not in stars:
                stars.append([x,y])
    
    x_min = 1001
    x_max = -1001
    y_min = 1001
    y_max = -1001
    
    for i in range(len(stars)):
        x_min = int(min(x_min,stars[i][0]))
        x_max = int(max(x_max,stars[i][0]))
        y_min = int(min(y_min,stars[i][1]))
        y_max = int(max(y_max,stars[i][1]))
    
    stars.sort(key = lambda x : x[1])
    stars.reverse()
    star = ''
    for i in range(x_min, x_max+1):
        star+= '.'
    for i in range(y_min, x_max+1):
        result.append(list('' + star))
        
    for i in stars:
        if x_min > 0:
            xp = 0
        else:
            xp = x_min-1

        if y_min > 0:
            yp = 0
        else:
            yp = y_min-1
        result[int(i[1]) + yp][int(i[0]) + xp] = '*'
    
    result.reverse()

    for i in result:
        answer.append(''.join(i))
    return answer

print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))