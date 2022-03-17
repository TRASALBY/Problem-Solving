import sys

input = sys.stdin.readline

def find_parent(parent,x): # 경로 압축 부모테이블을 루트노드로 갱신
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union(parent,a,b):     #루트노드를 비교해서 다른 집합이면 합쳐 준다.
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n,m = map(int, input().split())
parent = [i for i in range(0,n+1)]  # 부모테이블 초기화


for _ in range(1,m+1):
    t, a, b = map(int,input().split())
    if t == 0:
        union(parent,a,b)
    else:
        a_root = find_parent(parent, a)
        b_root = find_parent(parent,b)
        if a_root == b_root:
            print("YES")
        else:
            print("NO")