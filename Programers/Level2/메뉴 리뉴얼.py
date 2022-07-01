# 함께 많이 주문한 단품을 최소 2가지 이상
# 최소 2명 이상 주문한 조합


from itertools import combinations

def solution(orders, course):
    
    answer = []           
    for i in course:
        comb = set()
        for order in orders:
            comb = comb | set(combinations(sorted(list(order)),i))          #order가 정렬된 상태로 들어오지 않는다. WXA
        comb = list(comb)
        
        
        now_comb = []       #각 메뉴 수 별 세트
        max_order = 0       #최대 주문 수
        
        for c in comb:            
            order_p = 0
            for order in orders:
                check = 0
                if set(c) == set(c) & set(order):   #교집합을 통해 해당 세트가 주문되었는지 확인한다.
                    order_p +=1
                    
            if order_p >= 2:
                if order_p > max_order:             #최대값이 갱신되면 세트 초기화
                    max_order = order_p
                    now_comb = [''.join(c)]
                    
                elif order_p == max_order:          #최대값이 같으면 여러개가 들어갈 수 있다.
                    now_comb.append(''.join(c))
                                    
        answer += now_comb
                                    
    return sorted(answer)