import heapq
def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while(scoville[0] <K):
        if len(scoville) <2:
            return -1
        s1 = heapq.heappop(scoville)
        s2 = heapq.heappop(scoville)
        heapq.heappush(scoville,s1 + (s2*2))
        answer += 1
        
    return answer

print(solution([1, 2, 3, 9, 10, 12],7))

'''
heapq 자료구조 사용 (파이썬에서 기본은 최소힙)
heapq.heapify를 통해 정렬된다.
우선순위를 두고 그 우선순위가 높은것을 먼저 pop한다.
2개를 pop 해야하므로 2개보다 값이 적을때는 에러 -1 리턴
'''