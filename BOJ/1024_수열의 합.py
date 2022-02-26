import sys


N,L = map(int,sys.stdin.readline().split())         

def solution(start,end):
    for i in range(start,end+1):
        print(i,end=" ")

for l in range(L,100+1):
    end = int(N / l + l /2)
    start = end - l + 1

    if start < 0:
        continue
    elif end > N:
        continue
    elif N*2 == end * (end+1) - start*(start-1):
        solution(start,end)
        break
else:
    print(-1)
  