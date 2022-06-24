def check_correct_bracket(s):
    stack = []
    for i in range(len(s)):
        stack.append(s[i])
            
        if i != 0 and len(stack) >=2 :
            if stack[-2] =='(' and stack[-1] == ')':
                stack.pop()
                stack.pop()
    if stack == []:
        return True
    else:
        return False
    
def check_balance_bracket(s):
    if s.count('(') == s.count(')'):
        return True
    else:
        False
        
def find_balance_bracket(s):
    for i in range(2,len(s)+1,2):
        if check_balance_bracket(s[:i]) and check_balance_bracket(s[i:]):
            return s[:i],s[i:]
        
def res(w):
    if w == '':
        return ''
    u,v = find_balance_bracket(w)
    if check_correct_bracket(u):
        return u + res(v)
    else:
        new_w = "(" + res(v) + ')'
        
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] =='(':
                u[i] = ')'
            else:
                u[i] = '('
        s = ''.join(u)
        return new_w + s

def solution(p):
    if check_correct_bracket(p):
        return p
    return res(p)
