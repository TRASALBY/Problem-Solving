def solution(citations):
    answer = 0
    citations.sort()
    h_max = 0
    for h in range(len(citations)+1):
        for j in range(len(citations)):
            if citations[j] >= h:                
                if len(citations) - j >= h:
                    h_max = max(h_max,h)
                break
            
    return h_max


'''
정렬을 진행하면 자신의 오른쪽에 있는 것들은 모두 나보다 큰 것들이다. 그것을 활용하여 h보다 큰 값인지 계산한다.
h값은 0~최대 리스트의 값 갯수까지 될 수 있으므로 for문의 범위를 h+1로 둔다.
'''