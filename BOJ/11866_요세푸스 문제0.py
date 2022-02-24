import sys

n, k = map(int,sys.stdin.readline().split())

arr = [i for i in range(1,n+1)]
answer = []
ind = 0
while arr != []:
    ind += k -1
    while ind >= len(arr):
        ind -= len(arr)
    answer.append(arr[ind])
    arr.remove(arr[ind])


print("<", end='')
for i in range(n):
    print(answer[i] , end='')
    if i < n-1:
        print(", ", end='')
    
print(">")

