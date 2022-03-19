from multiprocessing.connection import answer_challenge
import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_val = -1e9
min_val = 1e9
count = 0
def dfs(n,num,add,sub, mul, div,count):
    global max_val
    global min_val


    if count == n -1:
        max_val = max(max_val, num)
        min_val = min(min_val, num)
        return
    count+=1
    if add:
        dfs(n,num + a[count],add-1,sub,mul,div,count)
    if sub:
        dfs(n,num - a[count],add,sub-1,mul,div,count)
    if mul:
        dfs(n,num * a[count],add,sub,mul-1,div,count)
    if div:
        if num < 0:
            num = -num
            dfs(n,-(num // a[count]),add,sub,mul,div-1,count)
        else:
            dfs(n,num // a[count],add,sub,mul,div-1,count)

    return
dfs(n,a[0],add,sub, mul, div,0)

print(max_val)
print(min_val)