def convert_notation(num,n):
    rev_base = ''

    while num > 0:
        num, mod = divmod(num, n)
        if mod > 9:                         #10이상일때는 아스키 코드로 문자 출력
            mod = mod + 55                  # 'A' = 65
            rev_base += chr(mod)      
        else:
             rev_base += str(mod)
                
    if rev_base == '':                      #0일 경우 반복문을 돌지 않으니 '0'리턴
        return '0'
    return rev_base[::-1]                   #방향 역순


def solution(n, t, m, p):
    answer = ''
    num_str =''
    for i in range(t*m):
        num_str += convert_notation(i,n)
    p -= 1
    for i in range(t):
        if i == 0:            
            answer += num_str[p]
        else:
            p += m
            answer += num_str[p]
    return answer
