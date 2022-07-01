import sys

input = sys.stdin.readline


def gcd(a,b):

    while (b > 0):
        tmp = a
        a = b
        b = tmp%b

    return a;


a,b = map(int,input().split())
g = gcd(a,b)
print(g)

print(a * b // g )