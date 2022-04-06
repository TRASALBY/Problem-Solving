import sys
from bisect import bisect_right, bisect_left

input = sys.stdin.readline

n, x = map(int,input().split())

arr = list(map(int,input().split()))

left_ind = bisect_left(arr,x)
right_ind = bisect_right(arr,x)

answer = right_ind-left_ind
if answer <= 0:
    answer = -1
print(answer)