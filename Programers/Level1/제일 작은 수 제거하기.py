def solution(arr):
    
    min_val = min(arr)
    ind = arr.index(min_val)
    arr.pop(ind)
    
    if arr == []:
        arr = [-1]
    return arr