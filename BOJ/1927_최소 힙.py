import heapq
import sys

N = int(sys.stdin.readline())
h = []
for i in range(N):
    x = int(sys.stdin.readline())
    if x >0:
        heapq.heappush(h,x)
    else:
        if h == []:
            print(0)
        else:
            print(heapq.heappop(h))
        