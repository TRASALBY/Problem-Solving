import sys

def search(a: list,b: list):
    result = []
    a.sort()
    for i in b:
        left = 0
        right = len(a) -1
        while(left <= right):
            mid = (left + right) // 2
            if a[mid] < i:
                left=mid+1
            elif a[mid] >i:
                right = mid -1
            else:
                result.append(i)
                break
    return sorted(result)

N, M = map(int,sys.stdin.readline().split())
a = []
for i in range(N):
    a.append(sys.stdin.readline().rstrip())

b = []
for i in range(M):
    b.append(sys.stdin.readline().rstrip())

answer = search(a,b)

print(len(answer))
for i in answer:
    print(i)