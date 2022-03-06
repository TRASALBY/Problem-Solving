import sys


for i in sys.stdin:
    try:
        i = int(i)    
        dp = [0] * 251
        dp[1] = 1
        dp[2] = 3
        for j in range(3,i+1):
            dp[j] = dp[j-1] + 2 * dp[j-2]
    except EOFError:
        break

    

    print(dp[i])