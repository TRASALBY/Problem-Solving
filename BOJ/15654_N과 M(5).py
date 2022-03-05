import sys

N, M = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))
arr.sort()
visited = [False] * N

answer = []


def dfs(cnt):
    if cnt == M:
        for i in answer:
            print(i, end=' ')
        print()
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            answer.append(arr[i])
            dfs(cnt + 1)
            answer.pop()
            visited[i] = False

dfs(0)