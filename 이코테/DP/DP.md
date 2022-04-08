# 다이나믹 프로그래밍
한번 계산한 적이 있다면 중복하여 계산하지 않도록 하자  
연산속도와 메모리 공간을 최대한으로 활용할 수 있는 효율적인 알고리즘 작성

### 조건
1) 최적 부분 구조 (Optimal Substructure)
: 큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결

2) 중복되는 부분 문제 (Overlapping Subproblem)
: 동일한 작은 문제를 반복적으로 해결해야 한다.

### 피보나치 수열  
1 1 2 3 5 8 13 ....  
![image](https://user-images.githubusercontent.com/54586491/162430072-49b4f0f5-ce3f-481e-bb55-bd40456cc96a.png)

```python
#단순 재귀로 구현한 피보나치
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)
```
![image](https://user-images.githubusercontent.com/54586491/162430355-5931ff45-0749-4437-b456-ee369608e561.png)  
중복되는 호출이 너무 많음

### 다이나믹 프로그래밍 방식
+ 탑다운(하향식) - 큰 문제 해결을 위해 작은 문제를 호출
+ 바텀업(상향식) - 작은 문제부터 순서대로 답을 도출

### 탑다운
메모이제이션 방식  
한 번 계산한 결과를 메모리 공간에 기록해 두고 필요할때 기록한 내용을 그대로 가져온다.

```python
d = [0] * 100

# 탑다운 피보나치
def fibo(x):

    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는지 확인
    if d[x] != 0:
        return d[x]
    #계산된 적이 없다면 점화식 수행
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]
```

### 바텀업
```python
d = [0] * 100


d[1] = 1
d[2] = 1
n = 99

# 바텀업 피보나치
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])
```

### 다이나믹 프로그래밍에 접근하는 방법

+ 해당 문제를 그리디, 구현, 완전탐색 등의 아이디어로 해결할 수 있는지 검토 후 풀이가 떠오르지 않는다면 다이나믹 프로그래밍을 고려해 본다.
+ 우선 재귀로 비효율적인 완전 탐색 코드를 작성후 코드를 개선하는 방법을 사용한다.

### 실전문제 개미병사

```python
n = int(input())
array = list(map(int, input().split()))

d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1]) 
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

print(d[n - 1])
```
