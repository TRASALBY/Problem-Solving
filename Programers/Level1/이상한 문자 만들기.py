def solution(s):
    answer = ''
    s = list(s)
    j = 0
    for i in range(len(s)):
        if s[i] == ' ':
            j = 0
            continue
        if j % 2 == 0:
            s[i] = s[i].upper()
        else:
            s[i] = s[i].lower()            
        j += 1
        
    answer = ''.join(s)
    return answer