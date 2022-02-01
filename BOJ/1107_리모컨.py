import sys

def count_button(goal, count):
    if len(goal) == 0:
        return count
    
    if (goal[0] not in broken):
        count += 1
        goal = goal[1:]
        return count_button(goal,count)
    else:
        mul = len(goal)
        temp = int(map(int,goal))
        under = round(temp,-mul+1) - pow(10,mul-1)
        upper = round(temp,-mul+1)
        if upper - temp < temp - under:
            goal[0] = str(int(goal[0])+1)
            for i in range(1,len(goal)):
                goal[i] = '0'
        else:
            goal[0] = str(int(goal[0])-1)
            for i in range(1,len(goal)):
                goal[i] = '9'          

n = sys.stdin.readline().rstrip()
m = int(sys.stdin.readline())
if m > 0:
    broken = list(map(str,sys.stdin.readline().split()))

count = 0

print(count_button(list(n), count))

    