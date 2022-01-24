cnt = int(input())

arr = list(map(int, input().split()))

max = arr[0]
min = arr[0]
for i in range(cnt):
    if(max < arr[i]):
        max = arr[i]
    if(min > arr[i]):
        min = arr[i]

n = min * max
print(n)