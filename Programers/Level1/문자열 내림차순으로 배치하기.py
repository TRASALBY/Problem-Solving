def solution(s):
    answer = ''
    s = list(s)
    answer = ''.join(sorted(s)[::-1])
    return answer