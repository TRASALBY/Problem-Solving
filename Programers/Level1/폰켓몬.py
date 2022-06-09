def solution(nums):
    answer = 0
    poket = [0 for i in range(200001)]
    for num in nums:
        poket[num] += 1
    for i in poket:
        if i > 0:
            answer += 1
        if answer > len(nums)/2:
            answer -= 1
            break
    return answer


'''
다른풀이 
def solution(nums):
    answer = 0
    poket_set = set(nums)
    answer = min(len(set), nums/2)
    return answer


'''