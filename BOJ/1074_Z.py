import sys
input = sys.stdin.readline
n,r,c = map(int,input().split())



s = 1
e = 2** (2* n)

if r==0 and  c ==0:
    print(0)
else:
    while(r >= 1 or c >= 1):
        l = 2**n
        m =e-s
        if r < l//2 and c <l//2:
            e = s + m // 4


        elif r < l//2  and l//2 <= c:
            s,e  = s + m//4,s + m//2
            c = c - l//2

        elif l//2 <= r and c <l//2:
            s,e = s + m//2,s + 3*m//4
            r = r - l//2

        else:
            s = s + 3*m//4
            r = r - l//2
            c = c - l//2
        n -= 1

    print(s)
