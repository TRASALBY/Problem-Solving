def solution(d, budget):
    money = 0
    d.sort()
    for i in range(len(d)):
        money += d[i]
        if money > budget:
            return i
                
    return len(d)