def solution(dartResult):
    
    def cal_option(option,count):
        if option == "*":
            if count == 1:
                score_stack[0] *= 2
            else:
                score_stack[count-1] *= 2
                score_stack[count-2] *= 2
        if option == "#":
            score_stack[count-1] = -score_stack[count-1]
        
    score_stack = []
    option_list = ["*", "#"]
    count = 0
    while dartResult != "":
        if(dartResult[0] in option_list):
            cal_option(dartResult[0],count)
            dartResult = dartResult[1:]
        else:
            i = 0
            while(dartResult[i].isdigit()):
                i+=1
            score = int(dartResult[0:i])
            bonus = dartResult[i]
            if bonus == "S":
                score = pow(score,1)
            elif bonus == "D":
                score = pow(score,2)
            else:
                score = pow(score,3)
            dartResult = dartResult[i+1:]
            score_stack.append(score)
            count+=1
    
    return sum(score_stack)