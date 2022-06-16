def solution(clothes):
        
    answer = 1
    cloth_dic = {}
    
    for cloth in clothes:
        if cloth[1] in list(cloth_dic.keys()):
            cloth_dic[cloth[1]].append(cloth[0])
            
        else:
            cloth_dic[cloth[1]] =[cloth[0]]
            
    keys = list(cloth_dic.keys())
    
    for key in keys:
        answer *= len(cloth_dic[key])+1
    return answer-1

'''
각 종류별 개수 + 1 (아무것도 안입었을 경우를 고려해 1을 더해줌)의 값들을 모두 곱해 전체 경우의 수를 구해줌
그 중 모든 종류의 옷을 안입었을 경우 1을 빼주면 최소 하나이상은 옷을 입은 상태가 된다.
'''