import sys

input = sys.stdin.readline

n,m = map(int,input().split())




tree = list(map(int,input().split()))

first, last = 0, sum(tree)
while first<=last:
    mid = (first + last) // 2
    cnt = 0
    for t in tree:
        if t > mid:
            cnt += t - mid
    if cnt >= m:
        first = mid + 1
    else:
        last = mid - 1
print(last)

