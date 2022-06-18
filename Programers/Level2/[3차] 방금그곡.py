import math


def cal_time(time):
    hour, minute = time.split(":")
    return (60 * int(hour)) + int(minute)
    
def solution(m, musicinfos):
    # #은 소문자로 치환    
    answer = ''    
    m = list(m)
    while(m.count('#') != 0):
        ind = m.index('#')
        m.remove('#')
        m[ind-1] = m[ind-1].lower()
    
    m = ''.join(m)
    for i in range(len(musicinfos)):
        
        start,end,title,code = musicinfos[i].split(',')
        play_time = cal_time(end) - cal_time(start)
        
        musicinfos[i] = [start,end,title,code,play_time,i]
        
    musicinfos.sort(key = lambda x: (-x[4],x[5]))
    
    
    for musicinfo in musicinfos:
        start = musicinfo[0]
        end = musicinfo[1]
        title = musicinfo[2]
        code = list(musicinfo[3])
        play_time = musicinfo[4]
        
        while(code.count('#') != 0):
            ind = code.index('#')
            code.remove('#')
            code[ind-1] = code[ind-1].lower()
        code = ''.join(code)
        
        repeat = math.ceil(play_time / (len(code)))
        song_code = code * (repeat + 1)
        song_code = song_code[:play_time]
        
        if m in song_code :
            return title
        
    return "(None)"
