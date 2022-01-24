
def dfs(graph, v, visited,cnt):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph,i,visited,cnt)

    return visited.count(True)
    


n= int(input())
m = int(input())
cnt = 0
visited = [False] * n
graph=[[] for i in range(n+1)]
for i in range(1,m+1):
    s_node, e_node = map(int,input().split())
    graph[s_node].append(e_node)
    graph[e_node].append(s_node)

for i in range(1,n+1):
    graph[i].sort()


print(dfs(graph,1,visited,cnt)-1)