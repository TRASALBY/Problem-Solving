from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    now_bridge = deque()
    truck_time = deque()
    answer = 0    
    time = 1
    
    now_bridge.append(truck_weights.popleft())
    truck_time.append(time)
    time += 1
    while(now_bridge):
        for i in range(len(truck_time)):
            truck_time[i] += 1
        time_copy = truck_time.copy()
        bridge_copy = now_bridge.copy()
        for i in range(len(time_copy)):
            if truck_time[i] > bridge_length:
                bridge_copy.remove(now_bridge[i])
                time_copy.remove(truck_time[i])
        truck_time = time_copy
        now_bridge = bridge_copy
        if truck_weights != deque([]):
            if truck_weights[0] + sum(now_bridge) <= weight:
                    now_bridge.append(truck_weights.popleft())
                    truck_time.append(1)
        time += 1
    
    return time - 1

'''
반복문에서 pop 또는 remove를 사용할때 인덱스의 오류가 나는 것 주의
copy를 사용해 해결할 수 있었다.
'''