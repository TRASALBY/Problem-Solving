def solution(n, left, right):
    answer = []
    arr = [i for i in range(1,n+1)]
    
    for i in range((left // n) + 1,(right // n) +2):
        answer += [i]*i +arr[i:]
    
    
    left = left % n
    right = -(n - (right+1) % n)
    
    if right == -n:
        return answer[left:]
    return answer[left:right]


'''
모든 배열을 구하여 슬라이싱 하려고 시도하면 시간초과 발생
left와 right가 포함된 배열범위만 구하여 그 값을 슬라이싱 해 준다.
'''