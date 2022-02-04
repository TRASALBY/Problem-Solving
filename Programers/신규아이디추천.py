
def class1(id_list):    
    ch = ['-', '_', '.']
    for i in range(len(id_list)):
        if not (id_list[i].isalpha() or id_list[i].isdigit()):
            if id_list[i] not in ch:
                id_list[i] = ""

    return list(''.join(id_list))
                
def class2(id_list):
    for i in range(len(id_list)):
        if id_list[i] == '.':
            for j in range(i+1,len(id_list)):
                if id_list[j] == '.':
                    id_list[j] = ""
                else:
                    break
    return list(''.join(id_list))

def class3(id_list):
    while(id_list[0] == '.'):
        id_list[0] = ""
    while(id_list[-1] == '.'):
        id_list[-1] = ""
    
    return list(''.join(id_list))

def class4(id_list):
    new_id = ''.join(id_list)
    if new_id == '':
        new_id = 'a'
            
    return list(new_id)   

def class5(id_list):
    if len(id_list) >=16:
        id_list = id_list[:16]
        id_list = class3(id_list)
    return id_list

def solution(new_id):
    answer = ''    
    answer_list = []
    new_id = new_id.lower()
    id_list = list(new_id)
    
    id_list = class1(id_list)
    id_list = class2(id_list)
    id_list = class3(id_list)
    id_list = class4(id_list)
    

    
    return ''.join(id_list)

print(solution("...!@BaT#*..y.abcdefghijklm"))
