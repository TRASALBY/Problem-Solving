def solution(answers):
    answer = []
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    
    c = [0,0,0]
    
    for i in range(len(answers)):
        if p1[i % len(p1)] == answers[i]:
            c[0] += 1
        if p2[i % len(p2)] == answers[i]:
            c[1] += 1
        if p3[i % len(p3)] == answers[i]:
            c[2] += 1
            
    max_c = max(c)
    
    for i in range(3):
        if c[i] == max_c:
            answer.append(i+1)
    return sorted(answer)