def solution(n, words):
    answer = []
    words_list = []
    player = [0 for i in range(n)]
    
    for i in range(len(words)):
        now = i % n
        if words[i] in words_list:
            return [now + 1, player[now]+1]
        elif i != 0 and words[i-1][-1] != words[i][0]:
            return [now + 1, player[now]+1]
            
        else:
            words_list. append(words[i]) 
            player[now] += 1


    return [0,0]