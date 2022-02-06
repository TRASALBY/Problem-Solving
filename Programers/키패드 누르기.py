def solution(numbers, hand):
    answer = ''
    global left_hand
    global right_hand
    left_hand = '*'
    right_hand = '#'
    
    def compare(left,right,goal,num):
        keypad = [[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]]
        global left_hand
        global right_hand

        for i in range(4):
            if left in keypad[i]:
                left_now = i,keypad[i].index(left)

            if right in keypad[i]:
                right_now = i,keypad[i].index(right)

            if goal not in keypad[i]:
                continue
            goal_now = i,keypad[i].index(goal)

        left_len = abs(goal_now[0] - left_now[0]) + abs(goal_now[1] - left_now[1])
        right_len = abs(goal_now[0] - right_now[0]) + abs(goal_now[1] - right_now[1])
        if left_len < right_len:
            left_hand = numbers[num]
            return "L"
        elif left_len == right_len:
            if hand == "right":
                right_hand = numbers[num]
                return "R"
            else:
                left_hand = numbers[num]
                return "L"
        else:
            right_hand = numbers[num]
            return "R"
    
    for i in range(len(numbers)):
        if numbers[i] in [1,4,7]:
            left_hand = numbers[i]
            answer = answer + "L"
        elif numbers[i] in [3,6,9]:
            right_hand = numbers[i]
            answer = answer + "R"           
        else:
            answer += compare(left_hand,right_hand,numbers[i],i)
            
    return answer





solution(	[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left")
