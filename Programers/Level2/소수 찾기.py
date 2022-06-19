from itertools import permutations

def is_prime(num):
    if num < 2:
        return 0
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return 0
    
    return 1


def solution(numbers):
    answer = 0
    nums = list(numbers)
    arr = []
    
    for i in range(1,len(nums)+1):
        arr += list(permutations(nums,i))
        
    arr = list(set(arr))
    for i in range(len(arr)):
        arr[i] = int(''.join(arr[i]))
    
    arr = list(set(arr))

    for i in arr:
        answer += is_prime(i)
    
    return answer


'''
문자를 리스트로 분리 후 모든 순열을 구한다.
0이 앞에 올 경우 제거해 주고 set으로 변환하는 과정을 거쳐 같은수를 없앤다
각 숫자가 소수인지 확인한다.
이때 숫자의 절반이하까지만 확인해도 된다. 반보다 크면 무조건 소수점이 나오기 때문
'''