import sys


M = int(sys.stdin.readline())
S = set()
S_all = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
for i in range(M):
    cal_str= list(map(str,sys.stdin.readline().split()))
    cal = cal_str[0]
    if len(cal_str) >= 2:

        num = int(cal_str[1])
        
    if cal == "add":
        S.add(num)
    elif cal == "check":
        if num in S:
            print(1)
        else:
            print(0)
    elif cal == "remove":
        S.discard(num)
    elif cal == "toggle":
        if num in S:
            S.remove(num)
        else:
            S.add(num)
    elif cal == "all":
        S = S_all
    else:
        S = set()