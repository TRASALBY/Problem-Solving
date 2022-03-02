
import sys

def check_bracket(a):           #추가된 괄호로 인한 연산
    break_point = False         #올바른 괄호가 아닐때 True

    if a == ')':                #들어온 괄호가 )일때
        n = 2
        b = '['
        c = '('
    else:
        n = 3                   #들어온 괄호가 ]일때
        b = '('
        c = '['
    arr = []
    cnt = 1
    for j in range(len(stack)-1,-1,-1):
        if stack[j].isdigit():          #여는괄호와 닫는괄호 사이에 숫자를 저장한다.
            arr.append(int(stack[j]))
        if stack[j] == b:
            break_point = True
            break
        if stack[j] == c:
            num = sum(arr)              #괄호 사이의 모든 숫자를 더한후
            if num == 0:                #사이에 아무 숫자도 없었다면 2 또는 3을 저장
                num = n
            else:
                num *= n                #더해진 값에 2 또는 3을 곱
            for k in range(cnt):        #양끝괄호와 숫자들을 없애고 계산된 숫자를 저장
                stack.pop()
            stack.append(str(num))
            break
        cnt+=1
    else:
        break_point = True              #반복문을 모두 돌았다는 것은 올바르지 않은 괄호라는 것
    return break_point


bracket = sys.stdin.readline().rstrip()
stack = []
break_point = False

for i in range(len(bracket)):   
    if break_point == True:         #올바른 괄호가 아닐경우 중단.
        break
    stack.append(bracket[i])        #괄호를 하나씩 스택에 추가
    if stack[-1] in [']', ')']:
        break_point = check_bracket(bracket[i]) #추가된 괄호로 인한 연산

if '(' in stack or '[' in stack:    #모든 연산이 진행되었는데 stack에 괄호가 남아있다면 올바르지 않은 괄호
    break_point = True

if break_point == True:             #올바르지 않은 괄호라면 0출력
    print(0)
else:                       
    result = 0                      #올바른 괄호라서 모든 괄호가 사라지고 숫자만 남았다면 숫자들의 합
    for i in stack:
        result+=int(i)
    print(result)
        
