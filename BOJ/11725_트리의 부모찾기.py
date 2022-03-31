import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
children = [[] for i in range(n+1)]
parents = [0 for i in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    children[a].append(b)
    children[b].append(a)


def find_child(now, children):
    global parents
    q = deque(children[now])

    while q:
        t = q.popleft()
        if parents[t] != 0:
            continue
        else:
            parents[t] = now
        find_child(t,children)
        if 0 not in parents[1:]:
            break
    
find_child(1, children)

for i in parents[2:]:
    print(i)