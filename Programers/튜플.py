def solution(s):
    answer = []
    s = s[1:-1]
    s = s.split('}')
    num_list = []
    for i in s:
        if i == "":
            s.remove("")
    for temp in s:
        temp = temp.strip('{'',')
        num_list.append(temp)
        

    for i in range(1,len(num_list)+1):
        for j in num_list:
            j = j.split(',')
            if len(j) == i:
                for k in j:
                    if int(k) not in answer:
                        answer.append(int(k))
        
    return answer