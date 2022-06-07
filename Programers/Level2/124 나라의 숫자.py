def solution(n):
    answer = ''
    while n >0:
        reminder = n % 3
        n = n // 3
        
        if reminder == 0:
            reminder = 4
            n-=1
        
        answer = str(reminder) + answer
    
    return answer
