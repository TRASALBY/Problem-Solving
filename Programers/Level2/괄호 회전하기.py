def check_bracket(s):
    stack = []
    bracket_open = ['[','(','{']
    bracket_close = [']',')','}']
    
    for i in range(len(s)):
        bracket = s[i]
        
        if bracket in bracket_open:
            stack.append(bracket)    
        else:
            if stack == []:
                return False
            if stack[-1] == bracket_open[bracket_close.index(bracket)]:
                stack.pop()
            else:
                return False
    if stack == []:
        return True
def solution(s):
    answer = 0
    
    for i in range(len(s)):
        ns = s[i:] + s[:i]
        if check_bracket(ns):
            answer +=1
    return answer