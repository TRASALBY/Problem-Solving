grade = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
T = int(input())

for t in range(1, T + 1):
    n, k = map(int,input().split())
    scores = []
    for i in range(n):
        mid, fin, assign = map(int,input().split())
        score = mid * 0.35 + fin * 0.45 + assign * 0.2
        scores.append((score,i))
    scores.sort(key = lambda x : x[0],reverse= -1)
    
    a = 0
    for i in range(len(scores)):        
        if scores[i][1] == k-1:
            a = i
            break
    
    b = int(a / n * 10)
    print('#'+str(t),grade[b])