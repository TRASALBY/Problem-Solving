import sys

input = sys.stdin.readline

t = int(input())


for _ in range(t):
    n = int(input())
    dp_top = [0] *(n+1)
    dp_bottom = [0] *(n+1)
    arr = [[],[]]
    arr[0] = list(map(int,input().split()))
    arr[1] = list(map(int,input().split()))
    dp_top[1] = arr[0][0]
    dp_bottom[1] = arr[1][0]

    for i in range(2,n+1):
            dp_top[i] = max(dp_bottom[i-1] + arr[0][i-1],dp_top[i-1])
            dp_bottom[i] = max(dp_top[i-1] + arr[1][i-1],dp_bottom[i-1])
  

    print(max(dp_top[n], dp_bottom[n]))

