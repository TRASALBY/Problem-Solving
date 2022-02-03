def solution(N, stages):
    answer = [ 0 for _ in range(N)] 
    result = []                 #1/8 , 3/7, 2/4, 1/2, 0
                                #0.125, 0.428, 0.5, 0.5, 0
    people = len(stages)        #8
    for i in range(1,N+1):
        count1 = 0
        count2 = 0
        for stage in stages:
            if i <= stage:
                count1 += 1
            if i == stage:
                count2 += 1
        if count1 == 0:
            count1+=1
        result.append(count2/count1)
    def solution(N, stages):
    answer = []
    result = []                 #1/8 , 3/7, 2/4, 1/2, 0
                                #0.125, 0.428, 0.5, 0.5, 0
    people = len(stages)        #8
    for i in range(1,N+1):
        count1 = 0
        count2 = 0
        for stage in stages:
            if i <= stage:
                count1 += 1
            if i == stage:
                count2 += 1
        if count1 == 0:
            count1+=1
        result.append(count2/count1)
    

    for k in range(len(result)):
        max = -1
        for i in result:
            if i > max:
                max = i
        answer.append(result.index(max) + 1)
        result[result.index(max)] = -1
    return answer
    rank = 1
    for k in range(len(result)):
        max = -1
        for i in result:
            if i > max:
                max = i
        answer[result.index(max)] = rank
        rank += 1
        result[result.index(max)] = -1
    return answer

stages= 	[4,4,4,4,4]
N = 4

solution(N,stages)