import sys

def speed_pow(a,b,c):
    if b == 0:
        return 1
    if b % 2 == 0:
        half = speed_pow(a,b//2,c)
        return  half * half %c
    else:
        return a * speed_pow(a,b-1,c) % c

a,b,c = map(int, sys.stdin.readline().split())

a = speed_pow(a,b,c)

print(a%c)