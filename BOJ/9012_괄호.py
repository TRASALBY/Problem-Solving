import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    stack = []

    arr = input().strip()
    b = True


    for i in range(len(arr)):
        if arr[i] == '(':
            stack.append(arr[i])
        elif len(stack) == 0:
            b = False
            break
        else:
            if stack[-1] == '(':
                stack.pop()
    if not b or len(stack) != 0:
        print("NO")

    else:
        print("YES")

 