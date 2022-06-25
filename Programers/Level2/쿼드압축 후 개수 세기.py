from collections import deque

def check01(arr):
    global answer

    arr = sum(arr,[])
    s = sum(arr)
    if s == len(arr):
        answer[1] += 1
        return False
    elif s == 0:
        answer[0] += 1
        return False
    else:
        return True
        


def quad(arr):
    global answer
    n = len(arr)
    arr_list = []
    temp = []


    for i in range(n//2):        
        temp.append(arr[i][:n//2])

    if check01(temp):
        arr_list.append(temp)

    temp = []
    
    for i in range(n//2):
        temp.append(arr[i][n//2:])

    if check01(temp):
        arr_list.append(temp)

    temp = []
    
    for i in range(n//2,n):
        temp.append(arr[i][:n//2])
    if check01(temp):
        arr_list.append(temp)

    temp = []
    
    for i in range(n//2,n):
        temp.append(arr[i][n//2:])
    if check01(temp):
        arr_list.append(temp)
    return arr_list
    

def solution(arr):   
    global answer
    answer = [0,0]
    if check01(arr):
        arr_list = deque(quad(arr))
        while(arr_list):
            arr = arr_list.popleft()
            arr_list += quad(arr)
        
    return answer