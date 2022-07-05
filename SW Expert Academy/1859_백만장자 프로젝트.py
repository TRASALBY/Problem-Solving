import sys

input = sys.stdin.readline

T = int(input())

for t in range(1,T+1):
    n = int(input())
    price = list(map(int,input().split()))

    price.reverse()

    max_p = -1
    money = 0
    for p in price:
        if p > max_p:
            max_p = p
        else:
            money += max_p - p
    print('#' + str(t), money)