n = int(input())
arr = list(map(int, input().split()))
arr.sort()

group_cnt = 0
count = 0 

#1 2 2 2 3 
for i in arr:
    count += 1
    if count >= i: #인원수가 공포도를 넘었는지 확인
        count = 0  #인원수 초기화
        group_cnt+=1
    

print(group_cnt)    