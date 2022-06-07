def solution(n):
    answer = 0
    list3 = []
    
    while(n != 0):
        list3.append(n%3)
        n = n//3
    #0,0,2,1 1,2,0,0
    list3.reverse()
    for i in range(len(list3)):
        answer += list3[i] * pow(3,i)
    return answer
