def solution(N, stages):
    answer = []
    clear = []
    
    for i in range(1,N+1):
        c,f = 0,0
        for j in range(len(stages)):
            if i == stages[j]:
                f+=1
            if i <= stages[j]:
                c+=1
        if c == 0:
            clear.append([0,i])
        else:
            clear.append([f/c,i])
        
    clear.sort(key = lambda x : x[0],reverse = -1)
    print(clear)
    
    for i in range(len(clear)):
        answer.append(clear[i][1])
    return answer