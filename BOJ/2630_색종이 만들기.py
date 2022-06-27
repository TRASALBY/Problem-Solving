import sys

global blue
global white
blue,white = 0,0

def quad(n,arr):
    global blue
    global white
    arr1 = []
    for i in range(n//2):
        arr1.append(arr[i][:n//2])
        
    s = sum(sum(arr1,[]))
    if s == (n//2) ** 2:
        blue += 1
    elif s == 0:
        white += 1
    else:
        quad(n//2,arr1)
        
    arr2 = []
    for i in range(n//2):
        arr2.append(arr[i][n//2:])
    s = sum(sum(arr2,[]))
    if s == (n//2) ** 2:
        blue += 1
    elif s == 0:
        white += 1
    else:
        quad(n//2,arr2)
        
    arr3 = []
    for i in range(n//2,n):
        arr3.append(arr[i][:n//2])
    s = sum(sum(arr3,[]))
    if s == (n//2) ** 2:
        blue += 1
    elif s == 0:
        white += 1
    else:
        quad(n//2,arr3)
        
    arr4 = []
    for i in range(n//2,n):
        arr4.append(arr[i][n//2:])
    s = sum(sum(arr4,[]))
    if s == (n//2) ** 2:
        blue += 1
    elif s == 0:
        white += 1
    else:
        quad(n//2,arr4)


input = sys.stdin.readline

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))
    
s = sum(sum(graph,[]))
if s == (n) ** 2:
    blue += 1
elif s == 0:
    white += 1
else:
    quad(n,graph)

print(white)
print(blue)
    
    
