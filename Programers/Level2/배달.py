from collections import deque


def solution(N, road, K):
    answer = 0
    road.sort(key = lambda x : x[2],reverse = 1)
    inf = 9999999999999
    graph = [
        [inf] * (N + 1) for _ in range(N+1)
    ]
    distance = [inf] * (N+1)
    for n in road:
        start,goal,cost = n
        graph[start][goal] = cost
        graph[goal][start] = cost
        
    start = 1
    distance[1] = 0
    
    q = deque([start])
    while (q):      
        v = q.popleft()
        if v == 0:
            continue
        for i in range(len(graph[v])):
            if graph[v][i] != inf:
                n_dis = distance[i]
                distance[i] = min(distance[i], distance[v] + graph[v][i])
                if n_dis != distance[i]:
                    q.append(i)
    for i in distance[1:]:
        if i <= K:
            answer += 1
    return answer


'''
다익스트라를 직접 구현한 것
각 노드가 연결이 가능한 노드를 확인해 그 노드까지의 거리를 구한다
만약 노드까지의 거리가 갱신이 되었다면 다시한번 그 노드를 넣어 값을 계산한다.
'''