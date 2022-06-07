import math
def make_num(n, k):
    num = ''

    while n > 0:
        n, mod = divmod(n, k)
        num += str(mod)

    return num[::-1] 
    
def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def solution(n, k):
    num = make_num(n,k)
    number_list = num.split('0')
    answer = 0
    for x in number_list:
        if x:            
            if is_prime_number(int(x)):
                answer+=1
    return answer