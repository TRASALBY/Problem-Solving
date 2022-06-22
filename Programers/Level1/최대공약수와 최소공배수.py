def solution(n, m):
    n,m = min(n,m),max(n,m)
    a,b = 1,m*n
    for i in range(2,n*m):
        if n % i == 0 and m% i == 0:
            a = i
        if i % n == 0 and i % m == 0:
            b = min(b,i)
    answer = [a,b]
    return answer