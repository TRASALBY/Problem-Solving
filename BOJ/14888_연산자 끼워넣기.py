import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_val = -float("inf") #최대 최소값 +-무한으로 지정
min_val = float("inf")


def dfs(n,num,add,sub, mul, div,count): #재귀적으로 모든 경로를 탐색하면서
    global max_val
    global min_val

    count+=1
    if count == n :              #모든 연산을 다 했을때 값을 최대 최소와 비교하여 저장
        max_val = max(max_val, num)
        min_val = min(min_val, num)
        return
    
    if add:                     #각 연산 값이 0이 아닐때 재귀적으로 깊이탐색을 진행하며 모든 경우 연산 진행
        dfs(n,num + a[count],add-1,sub,mul,div,count)
    if sub:
        dfs(n,num - a[count],add,sub-1,mul,div,count)
    if mul:
        dfs(n,num * a[count],add,sub,mul-1,div,count)
    if div: 
        dfs(n,int(num / a[count]),add,sub,mul,div-1,count)

dfs(n,a[0],add,sub, mul, div,0)

print(max_val)                 #결과 출력
print(min_val)