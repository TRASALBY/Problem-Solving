from itertools import combinations

def solution(relation):
    answer = 0
    ind_list = [i for i in range(len(relation[0]))]
    comb = []
    for i in range(1,len(relation[0])+1):
        comb += list(combinations(ind_list,i))
    comb.reverse()
    break_point = False
    
    while(comb):
        values = []
        keys = comb.pop()
        for i in range(len(relation)):
            if break_point == True:
                break_point = False
                break
            value = []
            for j in keys:                
                value.append(relation[i][j])
            if value in values:
                break
            else:
                values.append(value)
        if len(values) == len(relation):
            answer += 1
            new_comb = []
            for i in comb:
                cnt = 0
                for key in keys:
                    if key in i:
                        cnt += 1
                if cnt != len(keys):
                    new_comb.append(i)
            comb = new_comb

    return answer