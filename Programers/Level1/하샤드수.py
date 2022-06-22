def solution(x):
    answer = True
    x2 = [int(i) for i in str(x)]
    if x % sum(x2) != 0:
        answer = False          
    
    return answer