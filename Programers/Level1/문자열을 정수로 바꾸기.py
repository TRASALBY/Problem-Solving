def solution(s):
    if s[0] == '+':
        return int(s[1:])
    elif s[0] =='-':
        return -int(s[1:])
    else:
        return int(s)    


##알고보니 int함수는 부호를 포함해서 변환시켜 준다. int('-1234') = -1234