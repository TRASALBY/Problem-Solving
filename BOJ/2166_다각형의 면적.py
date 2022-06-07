import sys

input = sys.stdin.readline

n = int(input())

points = []
for i in range(n):
    x,y  = map(int,input().split())
    points.append((x,y))

points.sort(key = lambda x: x[0],x[1])
x1, y1 = points[0]
sum = 0

check = []
for i in range(2,n):
    if points[i][1] < points[i-1][1] and points[i][1] < points[i+1][1]:
        check.append(i)

for i in range(1, n-1):
       
    if i in check :
        x2,y2 = points[i-1]
        x3,y3 = points[i+1]
    elif i+1 in range:
        x2,y2 = points[i]
        x3,y3 = points[i+1]
    

    area = (x1*y2) + (x2*y3) + (x3*y1) - (x2*y1) - (x3*y2) - (x1*y3)
    if area < 0:
        area = -area
    sum += area/2

print(round(sum,2))