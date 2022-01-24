def dfs(x, y):
    global check
    if x<=-1 or x >= n or y<=-1 or y>=n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        check+=1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False
        




n = int(input())

graph =[]
for i in range(n):
    graph.append(list(map(int,input())))

result = 0
global check 
check_list = []
for i in range(n):
    for j in range(n):
        check = 0
        if dfs(i, j) == True:
            result +=1
            check_list.append(check)
check_list.sort()
print(result)
for i in check_list:
    print(i)