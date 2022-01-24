A,B,V=map(int,input().split())

n=int((V-B)/(A-B))
if (V-B)%(A-B) == 0:
    print(n)
else:
    print(n+1)