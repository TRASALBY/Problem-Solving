import sys
input = sys.stdin.readline
n = int(input())
seat = [[0]*(n+1) for _ in range(n+1)]
friends = []
def check_black(x,y):
    cnt = 0
    if x+1 <= n and seat[y][x+1] == 0:
        cnt+=1
    if y+1 <= n and seat[y+1][x] == 0:
        cnt+=1
    if x-1 >= 1 and seat[y][x-1] == 0:
        cnt+=1
    if y-1 >= 1 and seat[y-1][x] == 0:
        cnt+=1
    return cnt

def check_friend(x,y,friend):           #주변에 친한친구 수 세기
    cnt = 0
    if x+1 <= n and seat[y][x+1] in friend:
        cnt+=1
    if y+1 <= n and seat[y+1][x] in friend:
        cnt+=1
    if x-1 >= 1 and seat[y][x-1] in friend:
        cnt+=1
    if y-1 >= 1 and seat[y-1][x] in friend:
        cnt+=1
    return cnt

def find_seat(student,friend): #자리 찾기 함수
    global seat
    now_x = -1  #찾을 자리의 x,y좌표
    now_y = -1
    max_val = 0
    seat_list = []          #모든 자리를 돌면서 주변에 친한 친구가 가장 많은 자리를 탐색한다.
    for y in range(1,n+1):
        for x in range(1,n+1):
            if seat[y][x] != 0:
                continue
            cnt = check_friend(x,y,friend)
            if max_val < cnt:
                seat_list = []
                seat_list.append((x,y))
                max_val = cnt
            elif max_val == cnt:
                seat_list.append((x,y))

    max_val = -1
    for x,y in seat_list:            
        cnt_blank = check_black(x,y)
        if max_val < cnt_blank:              
            max_val = cnt_blank
            now_x = x
            now_y = y
        
    seat[now_y][now_x] = student

def satisfaction(x,y,students):
    student = seat[y][x]
    cnt = check_friend(x,y,students[student])
    if cnt == 0:
        return 0
    else:
        return 10 **(cnt-1)
students = [0] *((n**2) + 1)
for i in range(n**2):
    temp = list(map(int,input().split()))
    
    student = temp[0]
    friend = temp[1:]
    students[student] = friend
    find_seat(student,friend)

answer = 0
for y in range(1,n+1):
    for x in range(1,n+1):
        answer += satisfaction(x,y,students)
print(answer)