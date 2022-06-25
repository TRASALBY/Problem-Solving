def find_dic(msg):
    global w
    global ind
    global dic
    
    ind+=1
    w = msg[:ind]
    while(w in dic):
        ind+=1
        if ind > len(msg):
            return True
        w = msg[:ind]
        
    
    dic.append(w)

                   

def solution(msg):
    answer = []
    global w
    global ind
    global dic
    
    ind = 0
    
    dic = list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    cnt = 0
    while(msg != ""):
        last_word = find_dic(msg)
        msg = msg[ind-1:]
        ind = 0
        if last_word == True:
            answer.append(dic.index(w))
        else:            
            answer.append(dic.index(w[:-1]))
        
    return answer
            