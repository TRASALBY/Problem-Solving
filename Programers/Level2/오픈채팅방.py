def solution(record):
    answer = []
    
    room = []
    names = {}
    for i in record:
        rec = list(map(str,i.split()))
        state = rec[0]
        id_num = rec[1]
        
        if state == 'Leave':
            room.append([id_num,'out'])
        else:            
            name = rec[2]            
            if state == 'Enter':
                room.append([id_num,'in'])          
                names[id_num] = name
            else:
                names[id_num] = name
            
            
    for i in room:
        if i[1] == 'in':
            answer.append(names[i[0]] + '님이 들어왔습니다.')
        else:
            
            answer.append(names[i[0]] + '님이 나갔습니다.')
    
    
    return answer
