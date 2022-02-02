import sys

password = {}
N, M = map(int, sys.stdin.readline().split())
for i in range(N):
    a, b = map(str, sys.stdin.readline().rstrip().split())
    password[a] = b
for i in range(M):
    print(password[sys.stdin.readline().rstrip()])