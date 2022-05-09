import math

def cal_time(start,end):
    sh, sm = map(int,start.split(':'))
    eh, em = map(int,end.split(':'))
        
    time_m = ((eh * 60) + em) - ((sh * 60) + sm)

    return time_m

def cal_money(minute,fees):      
    if minute <= fees[0]:
        return fees[1]
    else:
        return fees[1] + math.ceil((minute - fees[0])/fees[2]) * fees[3]         

def solution(fees, records):
    answer = []
    car = [[0,0] for i in range(10000)]
    min_s = [0 for i in range(10000)]
    for record in records:
        time, num, state = record.split()
        if state == "IN":
            car[int(num)] = [time, state]
        else:            
            min_s[int(num)] += cal_time(car[int(num)][0],time)
            car[int(num)] = [time, state]
    for i in range(10000):
        if car[i][1] == 'IN':
            min_s[i] += cal_time(car[i][0],'23:59')

    for i in min_s:
        if i != 0:
            price = cal_money(i,fees)
            answer.append(price)
    return answer 