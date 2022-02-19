import sys


T = int(sys.stdin.readline())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())

    print("yes")

#어떤 수에 -1, 1을 곱하여 원래 식을 만든다면
#모든 정수 A는 어떤 정수 B로 변할 수 있다.
#A * -1 * -1 * 1 = A