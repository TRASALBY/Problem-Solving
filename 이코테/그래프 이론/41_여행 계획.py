import sys

input = sys.stdin.readline

n, m = map(int, input().split())


def find_parent(parent,x): #부모찾기(루트노드)
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union(parent,a,b):     #루트노드 비교 후 합쳐주기
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(0,n+1)]  # 부모테이블 초기화

for a in range(1,n+1):
    graph = list(map(int,input().split()))
    for b in range(len(graph)):
        if graph[b] == 1:
            union(parent,a,b+1)

plan = list(map(int,input().split()))

parent_node = find_parent(parent,1)
for i in plan:
    if find_parent(parent,i) != parent_node:
        print('NO')
        break
    
else:
    print('YES')
