import sys

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

input = sys.stdin.readline
n, m  = map(int, input().split())
parent = [i for i in range(0,n+1)]

edges = []

for _ in range(m):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

edges.sort()
max_value = 0

result = 0
for edge in edges:
    cost, a,b = edge
    if find_parent(parent,a) != find_parent(parent, b):
        union_parent(parent, a,b)
        result += cost
        max_value = cost

print(result - max_value)