import sys

n = int(sys.stdin.readline())

graph = []
count = {-1: 0, 0 : 0, 1: 0 }

def solve(graph, n):
    new_list = list(set(sum(graph, [])))

    if len(new_list) == 1:
        count[new_list[0]] += 1
    else:
        new_graph = [[] for _ in range(9)]
        t = 0
        num2 = 0
        for num1 in range(9):
            t = num1//3 * n//3
            for temp in range(t,t+n//3):
                new_graph[num1].append(graph[temp][num2:num2+n//3])  
            
            num2+=n//3
            if num2 >= n:
                num2 = 0
        
        for o in range(9):
            solve(new_graph[o],int(n/3))
        return
            

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
solve(graph, n)

for i in [-1,0,1]:
    print(count[i])