from collections import deque
import sys

input = sys.stdin.readline
global a,b

a,b = map(int,input().split())

def make_tree():
    global a,b
    q = deque([])
    q.append((a,1))
    answer = -1
    while q:
        at,cnt = q.popleft()
        cnt+=1
        a1 = at*2
        a2 = (at*10) + 1
        if a1 == b or a2 == b:
            answer = cnt
            break
        if a1 < b:
            q.append((a1,cnt))
        if a2 < b:
            q.append((a2,cnt))
    return answer
 
answer = make_tree()
print(answer)