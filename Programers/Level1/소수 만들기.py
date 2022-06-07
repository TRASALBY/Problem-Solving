def is_pri(s):
    for i in range(2,s):
        if s % i == 0:
            return 0
    return 1
        

def solution(nums):
    answer = 0
    n = len(nums)
    
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                s = nums[i] + nums[j] + nums[k]
                answer += is_pri(s)
    return answer
