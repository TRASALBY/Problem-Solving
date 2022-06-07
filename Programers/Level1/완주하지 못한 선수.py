def solution(participant, completion):
    answer = ''
    
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if completion[i] != participant[i]:
            return ''.join(participant[i])
    
    return ''.join(participant[-1])
