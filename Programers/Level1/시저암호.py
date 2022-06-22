# a = 97 z = 122
# A = 65 Z = 90

def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
            continue
        a =  ord(s[i]) + n            
        if (s[i].isupper() and a > 90) or (s[i].islower() and a > 122):
            a -= 26
        answer += chr(a)
        
    return answer