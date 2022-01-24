n = int(input())
meetting_list = []
for i in range(n):
    start,end = map(int,input().split())
    meetting_time = (start,end)
    meetting_list.append(meetting_time)

meetting_list.sort(key = lambda x:(x[1],x[0]))

start_meetting = meetting_list[0]
attive_meeting = []
cnt = 0
start_meetting = (0,0)
for meeting in meetting_list:
    if start_meetting[1] <= meeting[0]:
        attive_meeting.append(meeting)
        start_meetting = meeting
              

print(len(attive_meeting))