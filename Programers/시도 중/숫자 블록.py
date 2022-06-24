def isPrime(n):
    global a
    a = [True] * (n + 1)
    m = int(n**0.5)

    for i in range(2, m + 1):
        if a[i] == True:
            for j in range(i + i, n + 1, i):
                a[j] = False

def getMyDivisor(n):

    divisorsList = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            if i == 1:
                continue
            divisorsList.append(i) 
            if ( (i**2) != n) : 
                divisorsList.append(n // i)
    divisorsList.sort()
    return divisorsList
    
def solution(begin, end):
    answer = []
    MAX = 10000000
    isPrime(end)
    global a
    for i in range(begin,end+1):
        if i == 1:
            answer.append(0)
        elif i % 2 == 0:
            answer.append(i //2)
        elif a[i]:
            answer.append(1)
        else:
            d = getMyDivisor(i).pop()
            while(d > MAX):
                 d = getMyDivisor(i).pop()               
            answer.append(d)
    return answer


'''
문제에 오류가 있다는 질문글이 있음
소수일때는 1, 그 외의 수는 약수중 가장 큰 수를 넣는다.
이때 최대 수가 정해져 있기 때문에 그 이하의 값만 넣도록 한다.
'''