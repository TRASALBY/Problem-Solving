import sys


input = sys.stdin.readline

expression = list(input().strip())

stk = []
res = ''
for s in expression:
    if s.isalnum():
        res+=s
    else:
        if s == '(':
            stk.append(s)
        elif s == '*' or s == '/':
            while stk and (stk[-1] == '*' or stk[-1] =='/'):
                res += stk.pop()
            stk.append(s)
        elif s == '+' or s == '-':
            while stk and stk[-1] != '(':
                res += stk.pop()
            stk.append(s)
        elif s == ')':
            while stk and stk[-1] != '(':
                res += stk.pop()
            stk.pop()

while stk:
    res+=stk.pop()
print(res)