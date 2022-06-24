def gcd(x,y):
    while(y):
        x,y = y,x%y
    return x


def solution(w,h):
    g = gcd(w,h)
    ww, hh = w/g, h/g
    
    
    sq = ww + hh -1
    
    answer = w * h - sq*g
    return answer


'''
유클리드 호제법을 이용한 최대공약수 계산
최소 단위로 반복되는 제거할 사각형을 계산
반복되는 만큼 제거
'''