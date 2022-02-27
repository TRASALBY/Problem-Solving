import sys


N, M = map(int,sys.stdin.readline().split())
a = set()
for i in range(N):
    a.add(sys.stdin.readline().rstrip())

b = set()
for i in range(N):
    b.add(sys.stdin.readline().rstrip())

answer = sorted(list(a&b))

print(len(answer))
for i in answer:
    print(i)