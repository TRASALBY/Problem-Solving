def cnt1(n):
    cnt = 0
    for i in range(len(n)):
        if n[i] =='1':
            cnt+=1
    return cnt

def solution(n):
    answer = 0
    n1 = bin(n)[2:]
    n_cnt1 = cnt1(n1)
            
    while(True):
        n += 1
        n2 = bin(n)[2:]
        n_cnt2 = cnt1(n2)
        if n_cnt1 == n_cnt2:
            return n