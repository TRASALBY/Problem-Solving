def solution(line):
    answer = []
    star = set()
    for l1 in line:
        for l2 in line:
            if l1 == l2:
                continue
            else:
                A,B,E = l1
                C,D,F = l2
                
                if (A*D - B*C) == 0:
                    continue
                x = (B*F - E*D) / (A*D - B*C)
                y = (E*C - A*F) / (A*D - B*C)
                
                if x % 1 == 0 and y % 1 == 0:
                    star.add((int(x),int(y)))
    star = list(star)
    x_max,y_max, x_min,y_min = -int(1e15),-int(1e15),int(1e15),int(1e15)
    
    for i in range(len(star)):
        x_max = max(x_max,star[i][0])
        y_max = max(y_max,star[i][1])
        x_min = min(x_min,star[i][0])
        y_min = min(y_min,star[i][1])
    
    w = int(abs(x_max - x_min) + 1)
    h = int(abs(y_max - y_min) + 1)
    
    
    if len(star) == 1:
        answer = ['*']
    else:
        answer = [['.']*w for j in range(h)]
        for s in star:
            answer[-s[1]+y_max][s[0]-x_min] = '*'
    
    stars = []
    for i in range(len(answer)):
        stars.append(''.join(answer[i]))
    
    return stars