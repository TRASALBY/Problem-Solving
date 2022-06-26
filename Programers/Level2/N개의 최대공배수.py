def solution(arr):
    answer = 0
    Max = max(arr)
    
    i = 1
    while(True):
        n = Max * i
        
        if all(n % i == 0 for i in arr):
            return n
        i +=1