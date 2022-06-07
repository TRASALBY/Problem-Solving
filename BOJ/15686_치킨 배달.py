import sys

input = sys.stdin.readline

n, m = map(int,input().split())
house = []
chicken = []
for i in range(1,n+1):
    temp = list(map(int,input().split()))
    for j in range(1,n+1):
        if temp[j-1] == 1:
            house.append((i,j))
        elif temp[j-1] == 2:
            chicken.append((i,j))
print(house)
print(chicken)

