def solution(brown, yellow):
    
    t = brown + yellow
    
    h = 3
    while (h ** 2) - (brown//2 + 2) * h  + t != 0:
        h += 1
    
    w = t / h
    return [w,h]