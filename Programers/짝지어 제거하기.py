def solution(s):
    if len(s) % 2 == 1:
        return 0
    
    while len(s) > 1:
        start = -1
        end = -1
        for i in range(len(s)-1):                
            if start == -1 and s[i] == s[i+1]:
                start = i
                end = i+2
                break
        if start == end:
            return 0
        s = s[0:start] + s[end:]
        if len(s) == 2 and s[0] == s[1]:
            return 1

    return 0