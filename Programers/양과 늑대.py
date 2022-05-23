
def getCanGoNodes(node, edges):
    canGoNodes = []
    for edge in edges:
        if edge[0] in node and edge[1] not in node:
            canGoNodes.append(edge[1])
        elif edge[1] in node and edge[0] not in node:
            canGoNodes.append(edge[0])
    return canGoNodes


def dfs(now, edges, info, sheep, wolf):
    global answer
    canGoNodes =  getCanGoNodes (now, edges)
    for i in canGoNodes:
        now.append(i)
        if info[i] == 0:
            sheep += 1
        else:
            wolf += 1
            
        if wolf >= sheep:
            
            wolf-=1
            now.pop()
            if answer < sheep:
                answer = sheep
        else:
            dfs(now,edges,info,sheep,wolf)
            if info[now.pop()] == 0:
                sheep -= 1
            else:
                wolf -= 1
            
            
    

def solution(info, edges):
    global answer
    answer = 0
    if info[0] == 0:
        sheep = 1
        wolf = 0
    else:
        sheep = 0
        wolf = 1    
    dfs([0], edges, info, sheep, wolf)

    return answer