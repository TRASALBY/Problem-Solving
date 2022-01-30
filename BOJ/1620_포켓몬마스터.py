n, m = map(int, input().split())
Pokédex = []
for i in range(n):
    Pokédex.append((i+1,input()))

for i in range(m):
    search = input()
    if search.isdecimal():
        for j in range(n):
            if Pokédex[j][0] == int(search):
                print(Pokédex[j][1])
                break
    else:
        for j in range(n):
            if Pokédex[j][1] == search:
                print(Pokédex[j][0])
                break