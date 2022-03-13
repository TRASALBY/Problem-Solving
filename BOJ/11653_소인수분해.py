import sys
input = sys.stdin.readline
N = int(input())
for i in range(2, N + 1):
    while N % i == 0: # i는 순서대로 들어가니까 안나눠지기 전까지 i를 출력함
        print(i)
        N = N // i