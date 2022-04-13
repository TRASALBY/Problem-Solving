import sys


t = int(input())



def fibo(n):
    if n == 0:
        cnt[0] +=1
    elif n == 1:
        cnt[1] += 1
    if n != 0 and dp[n] == 0:
        dp[n] = fibo(n-1) + fibo(n-2)
        
    return dp[n]
        

for _ in range(t):
    dp = [0] * 41
    dp[1] = 1
    cnt = [0,0]
    test_case = int(sys.stdin.readline())
    fibo(test_case)
    print(cnt[0],end=' ')
    print(cnt[1])