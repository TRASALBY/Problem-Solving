import sys
input = sys.stdin.readline

n = int(input())

num = 1

for i in range(2,n+1):
    num = num * i

answer = str(num)[::-1]
cnt = 0
for i in range(len(answer)):
    if answer[i] == '0':
        cnt+=1
    else:
        break

print(cnt)