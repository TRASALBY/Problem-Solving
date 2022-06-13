def solution(s):

    p_cnt = 0
    y_cnt = 0
    for i in range(len(s)):
        if s[i].lower() == 'p':
            p_cnt+=1
        if s[i].lower() =='y':
            y_cnt+=1
    
    if p_cnt == y_cnt:
        return True
    else:
        return False