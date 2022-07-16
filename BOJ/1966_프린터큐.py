test_case = int(input())
 
for i in range(test_case):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))
    cnt = 0	
    while(m != -1):
        if queue[0] == max(queue):
            del queue[0]
            m -= 1
            cnt += 1
        else:
            queue.append(queue[0])
            del queue[0]
            
            if m == 0:
                m = len(queue) - 1
            else:
                m -= 1
                
    print(cnt)