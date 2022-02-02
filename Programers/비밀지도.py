def solution(n, arr1, arr2):
    answer = []
    realmap = list(map(lambda x, y : x|y,arr1,arr2))
    
    for i in range(n):
        answer.append(bin(realmap[i]))
        answer[i] = str(answer[i][2:])
        while(len(answer[i])>n):
            answer[i] = answer[i][1:]
        while(len(answer[i])<n):
            answer[i] = "0"+answer[i]
        answer[i] = list(answer[i])
        for j in range(n):            
            if answer[i][j] == "1":
                answer[i][j] = "#"
            else:
                answer[i][j] = " "
        answer[i] = ''.join(answer[i])
    return answer