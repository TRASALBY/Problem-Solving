import sys

def hanoi(n,b,c):
    if n == 1:
        print(b,c)
    else:
        hanoi(n-1,b,6-b-c)
        print(b,c)
        hanoi(n-1,6-b-c,c)
n = int(sys.stdin.readline())    
print(2**n - 1)
hanoi(n,1,3)
