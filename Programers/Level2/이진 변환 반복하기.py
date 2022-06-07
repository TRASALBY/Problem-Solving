def solution(s):
    answer = []
    s = list(s)
    count_0 = 0
    count_repeat = 0
    while s != ['1']:
        count = s.count('0')
        s = len(s) - count
        s = list(bin(s))
        s = s[2:]
        count_0 += count
        count_repeat+=1
        
    answer.append(count_repeat)
    answer.append(count_0)
    return answer