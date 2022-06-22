def solution(n):
    answer = 0
    while(answer ** 2 < n):
        answer += 1
        if answer ** 2 == n:
            answer += 1
            return (answer ** 2)
    return -1


'''
def solution(n):
    answer = 0
    s = n ** (1/2)

    if s % 1 == 0:
        return (s + 1)**2
    return -1
'''