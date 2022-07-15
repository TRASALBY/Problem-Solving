import datetime as dt
def get_time(time):
    h,m,s = map(int,time.split(':'))
    
    s = m * 60 + h * 3600 + s
    return s

def sec_to_time(time):
    h = time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    time = time % 3600
    m = time // 60
    m = '0' + str(m) if m < 10 else str(m)
    time = time % 60
    s = '0' + str(time) if time < 10 else str(time)
    return h + ':' + m + ':' + s

def solution(play_time, adv_time, logs):
    start = []
    end = []
    end_time = get_time(play_time)
    time_to_sec = [0 for i in range(end_time + 1)]
    
    for log in logs:
        s,e = log.split('-')
        time_to_sec[get_time(s)] += 1
        time_to_sec[get_time(e)] -= 1
    
    for _ in range(2):
        for i in range(1,end_time):
            time_to_sec[i] += time_to_sec[i-1]
    
    ad_time = get_time(adv_time)

    max_view = 0 
    max_time = 0                          
    for i in range(ad_time - 1, end_time):
        if i >= ad_time:
            now_view = time_to_sec[i] - time_to_sec[i - ad_time]
            if max_view < now_view:
                max_view = now_view
                max_time = i - ad_time + 1
        else:
            if max_view < time_to_sec[i]:
                max_view = time_to_sec[i]
                max_time = i - ad_time + 1

    return sec_to_time(max_time)