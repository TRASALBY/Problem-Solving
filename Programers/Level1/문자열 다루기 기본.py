def solution(s):
    if len(s) != 4 and len(s) !=6:
        return False
    for i in range(len(s)):
        if s[i].isdigit():
            continue
        else:
            return False
    return True