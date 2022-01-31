import sys

n, m = map(int, sys.stdin.readline().split())
Pokédex1 = {}
Pokédex2 = {}
for i in range(1,n+1):
    name = sys.stdin.readline().rstrip()
    Pokédex1[i] = name
    Pokédex2[name] = i

for i in range(m):
    search = sys.stdin.readline().rstrip()
    if search.isdecimal():
        print(Pokédex1[int(search)])
    else:
        print(Pokédex2[search])