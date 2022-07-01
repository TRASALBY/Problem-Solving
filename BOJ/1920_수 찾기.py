import sys

def binary(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return True # 함수를 끝내버린다.
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return False


input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))

A.sort()

for b in B:
    if binary(b,A):
        print(1)
    else:
        print(0)