import sys
import heapq

input = sys.stdin.readline


t = int(input())
for i in range(t):
    k = int(input())
    min_heap = []
    max_heap = []
    visited = [False] * k
    for idx in range(k):
        a,b = input().split()
        b = int(b)
        if a == 'I':
            heapq.heappush(min_heap, (b, idx))
            heapq.heappush(max_heap, (-b, idx))
            visited[idx] = True
        else:
            if b == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    data, idx = heapq.heappop(max_heap)
                    visited[idx] = False
            else:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    data, idx = heapq.heappop(min_heap)
                    visited[idx] = False


    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap) 

    if max_heap and min_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')
