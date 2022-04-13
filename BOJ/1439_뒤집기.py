import sys

input = sys.stdin.readline

s = str(input().strip())
check = 1
check_str = s[0]
for i in range(1,len(s)):
    if check_str == s[i]:
        continue
    else:
        check+=1
        if check_str == '0':
            check_str = '1'
        else:
            check_str = '0'

print(check // 2)
