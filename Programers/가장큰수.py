def solution(numbers):
    answer = ''
    temp_number = []
    ind = 0
    for number in numbers:        
        cnt = 0
        
        if number!= 0:
            while number < 10000:
                number *=  10
                cnt+=1
            temp_number.append([number,ind,cnt])
            ind += 1
        
    temp_number.sort(key = lambda x: (x[0],x[2]))
    temp_number.reverse()
    temp_answer = []
    for i in range(len(numbers)):   
        answer += str(numbers[temp_number[i][1]])
                      
    return answer

print(solution([12, 121]))