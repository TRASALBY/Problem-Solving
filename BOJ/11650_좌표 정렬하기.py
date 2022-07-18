n = int(input())

points = []
for i in range(n):
    points.append(list(map(int,input().split())))

    
points.sort(key = lambda x : (x[0],x[1]))

for i in points:
    print(*i)