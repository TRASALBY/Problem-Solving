def solution(n, lost, reserve):
    students = []
    for i in range(n):
        students.append(1)
        
    lost = list(map(lambda x: x-1, lost))
    reserve = list(map(lambda x: x-1, reserve))  
    for i in range(n):
        if i in lost:
            students[i]-=1
        if i in reserve:
            students[i]+=1
            
    for i in range(n):
        if students[i] == 0:
            if i == 0:
                if students[i+1] >= 2:
                    students[i+1] -=1
                    students[i] +=1
                    continue
            elif i == n-1:
                if i == 0:
                    if students[i-1] >= 2:
                        students[i-1] -=1
                        students[i] +=1
                        continue
                       
            elif students[i-1] >= 2:
                students[i-1] -=1
                students[i] +=1
                continue
            elif students[i+1] >= 2:
                students[i+1] -=1
                students[i] +=1
                continue
            

    answer = 0
    for i in range(n):
        if students[i] >= 1:
            answer +=1
        
    return answer

print(solution( 5, [5,3,1], [2,4] ))