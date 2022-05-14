def solution(s):
    if len(s) % 2 == 1:
        return 0
    
    s = list(s)
    stack = []
    
    while s:
        stack.append(s.pop())
        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
    
    if stack:
        return 0
    else:
        return 1

    return 0