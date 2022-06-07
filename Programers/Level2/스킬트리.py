def solution(skill, skill_trees):
    answer = 0
    
    skill_len = len(skill)
    
    for tree in skill_trees:
        temp = []
        tree_list = list(tree)
        for i in range(skill_len):
            if skill[i] in tree_list:
                temp.append(tree_list.index(skill[i]))
            else:
                temp.append(-1)
        check_break = True
        for i in range(1,len(temp)):
            if temp[i-1] == -1:
                if temp[i] == -1:
                    continue
                else:
                    check_break = False
                    break
            if temp[i] < temp[i-1]:
                if temp[i] == -1:
                    continue
                else:
                    check_break = False
                    break
 
        if check_break == True:
            answer += 1
                
            
    return answer


"""

def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer
"""