def solution(s):
    answer = True
    st = []
    for i in range(len(s)):
        if s[i] =='(':
            st.append(s[i])
        if s[i] == ')':
            if len(st) == 0:
                return False
            else:
                st.pop(-1)
    if len(st) > 0:
        return False
            
    else:
        return True