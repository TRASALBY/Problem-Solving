def solution(progresses, speeds):
    answer = []
    while progresses != []:
        return_cnt = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        if progresses[0] >= 100:
            while progresses != []:
                if progresses[0] >= 100:
                    return_cnt +=1
                    progresses.remove(progresses[0])
                    speeds.remove(speeds[0])
                else:
                    break
            answer.append(return_cnt)      
    return answer