n = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

A = sorted(A)

sum = 0
for i in range(n):
    sum += A[i] * max(B)
    B.remove(max(B))

print(sum)