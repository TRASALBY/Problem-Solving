from cgitb import reset


n,k = map(int,input().split())
moneys = []
result = 0
for i in range(n):
    moneys.append(int(input()))

moneys.reverse()
for money in moneys:
    if(k >= money):
        result += k // money
        k = k % money
            

print(result)