import itertools

def solution(k, dungeons):
    answer = -1
    
    nPr = itertools.permutations(dungeons, len(dungeons))

    
    for per_dungeons in nPr:
        K = k
        cnt = 0
        for dungeon in per_dungeons:
            if dungeon[0] <= K:
                K -= dungeon[1]
                cnt += 1      
            else:
                answer = max(answer,cnt)
                break
        else:
             return len(dungeons)   
    return answer

'''
문제조건으로 최대 8개의 던전이라고 했으니 완전탐색으로 가능하다.
순열을 통해 모든 순서를 구해 두고 반복문을 통해 각각의 경우의 최대 값을 구한다.
'''