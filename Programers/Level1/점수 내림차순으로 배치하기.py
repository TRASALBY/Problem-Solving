def solution(n):
    answer = 0
    n = sorted([i for i in str(n)],reverse = 1)
    answer = int(''.join(n))
    return answer