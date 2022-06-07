from collections import deque

def solution(priorities, location):
    
    for i in range(len(priorities)):
        priorities[i] = [priorities[i],10+i]
    priorities = deque(priorities)
    answer = 0
    goal = priorities[location][1]
    while priorities:
        doc = priorities.popleft()
        for i in priorities:
            if i[0] > doc[0]:
                priorities.append(doc)
                break
        else:
            answer += 1
            if doc[1] == goal:
                break
    return answer