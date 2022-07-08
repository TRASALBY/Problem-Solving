def is_pos(answer):
    for x,y,a in answer:
        if a == 0:
            if y == 0 or [x,y-1,0] in answer or [x,y,1] in answer or [x-1,y,1] in answer:
                continue
            else:
                return False
        else:
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1]in answer):
                continue
            else:
                return False
    return True



def solution(n, build_frame):
    answer = []
    for f in build_frame:
        x,y,a,b = f
        if b == 0:
            answer.remove([x,y,a])
            if not is_pos(answer):
                answer.append([x,y,a])

        else:
            answer.append([x,y,a])
            if not is_pos(answer):
                answer.remove([x,y,a])         

    answer.sort(key = lambda x : (x[0], x[1], x[2]))


    return answer