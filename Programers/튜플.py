def solution(s):
    answer = []

    s = s.lstrip('{').rstrip('}').split('},{')
    num_list = []
    for num in s:
        num = num.strip("{""}")
        num_list.append(num)
        
    for i in range(1,len(num_list)+1):
        for j in num_list:
            j = j.split(',')
            if len(j) == i:
                for k in j:
                    if int(k) not in answer:
                        answer.append(int(k))
        
    return answer