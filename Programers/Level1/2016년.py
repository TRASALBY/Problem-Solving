def solution(a, b):
    day = 5
    week = ['SUN','MON','TUE','WED','THU','FRI', 'SAT']
    if a != 1:
        
        for i in range(1,a):
            if i == 2:
                day += 29
            elif i in [1,3,5,7,8,10,12]:
                day += 31
            else:
                day += 30
    
    day += b-1
    
    day %= 7
    answer = week[day]
    return answer