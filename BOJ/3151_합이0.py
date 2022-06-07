import sys
input = sys.stdin.readline
n = int(input())
answer = 0

students = sorted(list(map(int,input().split())))

'''
-6 -5 -4 -4 0 1 2 2 3 7
'''
result = []
for i in range(n-2):
    target = students[i] 
    start = i+1
    end = n-1
    while(start < end):

        if students[start] + students[end]  < -target:
            start += 1
        elif students[start] + students[end] > -target:
            end -= 1
        elif students[start] + students[end] == -target:
            if students[start] == students[end]:
                answer += end - start
            else:
                l = 1
                r = 1
                while True:
                    if students[start] == students[start+1]:
                        l += 1
                        start += 1
                    else:
                        break
                while True:
                    if students[end] == students[end-1]:
                        r += 1
                        end -= 1
                    else:
                        break
                answer += l * r
                break
print(answer)