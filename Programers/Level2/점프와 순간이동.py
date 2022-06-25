def solution(n):
    answer = 0 
    while(n > 0):
        if n % 2 == 0:
            n = n // 2
        else:
            n -= 1
            answer += 1
            
    return answer

'''
바텀탑방식의 dp로 접근하여 문제를 해결했었으나 효율성에서 문제가 났다.
확인해 보니 이런 문제는 탑다운 방식이 더 적합하다고 한다.
탑다운 방식으로 변경하여 문제를 해결하였다.
'''