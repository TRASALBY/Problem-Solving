from itertools import permutations
def solution(expression):
    oper = ['-','+','*']
    start = 0
    stack = []
    for i in range(len(expression)):
        if not expression[i].isdigit():
            stack.append(expression[start:i])
            stack.append(expression[i])
            start = i+1
    stack.append(expression[start:])
    
    opers_list = [["-","+","*"],["-","*","+"],["+","-","*"],["+","*","-"],["*","-","+"],["*","+","-"]]
    answer = 0
    check = 0
    for opers in opers_list:
        stack1 = stack.copy()
        for oper in opers:
            stack2 = []
            for i in range(len(stack1)):
                if  check != 0:
                    check-=1
                    continue
                if stack1[i] == oper:
                    stack2.append(stack1[i])
                    stack2.append(stack1[i+1])   
                    s = ''.join(stack2[-3:])
                    a = eval(s)
                    for i in range(3):
                        stack2.pop()
                        check = 1
                    if a > 0:
                        a = str(a)
                    else:
                        a = str(a)
                    stack2.append(a)

                else:
                    stack2.append(stack1[i])
            
            stack1 = stack2.copy()
        answer = max(abs(int(stack1[0])),answer)
    return answer