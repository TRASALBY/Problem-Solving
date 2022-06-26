'''
a 시작
b 경유
c 목표
'''
def hanoi(i,a,b,c):
    global answer
    if i == 1:
        answer.append([a,c]) 
    else:
        hanoi(i-1,a,c,b)
        answer.append([a,c])
        hanoi(i-1,b,a,c)

def solution(n):
    global answer
    answer = []
    hanoi(n,1,2,3)
    return answer