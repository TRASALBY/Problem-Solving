def solution(arr1, arr2):
    answer = []
    arr2_temp =[]
    for i in range(len(arr2[0])):
        temp = []
        for j in range(len(arr2)):
            temp.append(arr2[j][i])
        arr2_temp.append(temp)
        
    for i in arr1:
        temp = []
        for j in arr2_temp:
            temp.append(sum(list(map(lambda x,y : x * y, i,j))))
        answer.append(temp)
    return answer