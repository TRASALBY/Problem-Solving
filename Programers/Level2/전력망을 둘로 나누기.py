from collections import deque
import copy


def bfs(q,graph,visited):
    cnt = 0
    while(q):
        v = q.popleft()
        visited[v] = 1
        cnt += 1
        for i in range(len(graph[v])):
            if graph[v][i] != 0 and visited[i] == 0:
                visited[i] = 1
                q.append(i)
    return cnt
            

def solution(n, wires):
    answer = n
    
    graph = [[0] * (n+1) for _ in range(n+1) ]
    for wire in wires:
        start,end = wire
        graph[start][end] = 1
        graph[end][start] = 1
        
    for wire in wires:
        start,end = wire
        new_graph = copy.deepcopy(graph)
        new_graph[start][end] = 0
        new_graph[end][start] = 0
        
        visited = [0] * (n+1)
        q1 = deque([start])
        q2 = deque([end])
        
        answer = min(answer, abs(bfs(q1,new_graph,visited)-bfs(q2,new_graph,visited)))
        
    return answer