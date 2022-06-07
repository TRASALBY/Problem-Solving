def solution(array, commands):
    
    answer = []
    for command in commands:
        new_array = array[command[0]-1:command[1]]        
        n = sorted(new_array)
        answer.append(n[command[2]-1])
    
    return answer