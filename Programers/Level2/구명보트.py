from collections import deque

def solution(people, limit):
    answer = 0
    people.sort(reverse = 1)
    people = deque(people)
    while (people):
        p1 = people[0]
        p2 = people[-1]
        
        people.popleft()
        if p1 + p2 <= limit and len(people) >= 1:
            people.pop()
        
        answer += 1
    return answer


'''
deque를 사용한 큐로 문제를 해결
굳이 큐를 사용하지 않고 단순히 리스트의 인덱스만을 가지고도 문제를 해결할 수 있다.
'''