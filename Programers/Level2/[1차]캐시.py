def solution(cacheSize, cities):
    
    answer = 0
    cache = []
    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        elif cacheSize == 0:
            answer+=5
        else:
            answer += 5
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.pop(0)
                cache.append(city)
    return answer


'''
LRU 가장 오래 참조하지 않은 요소를 삭제
캐시의 사이즈를 잘 확인해야 한다.
캐시크기가 0일때는 삽입을 시킬 수 없다.
'''