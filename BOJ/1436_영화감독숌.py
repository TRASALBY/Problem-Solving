n = int(input())
end_num = 666
check = 0
while(True):
    num = str(end_num)
    if '666' in num:
        check+=1
    if check == n:
        break
    end_num+=1
print(end_num)