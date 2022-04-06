import sys
from bisect import bisect_left,bisect_right

input = sys.stdin.readline

#고정점 : 인덱스와 값이 같은 원소

n = int(input())

arr = list(map(int,input().split()))

def binary_search(arr, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] > mid :
            end = mid - 1
        else :
            start = mid + 1
    return -1


print(binary_search(arr,0,len(arr)))

