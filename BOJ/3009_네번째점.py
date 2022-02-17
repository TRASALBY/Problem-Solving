x1 = []
x2 = []
x3 = []
x4 = []

for i in x1,x2,x3:
    x,y = map(int,input().split())
    i.append(x)
    i.append(y)

if x1[0] == x2[0]:
    x4.append(x3[0])
elif x1[0] == x3[0]:
    x4.append(x2[0])
else:
    x4.append(x1[0])
if x1[1] == x2[1]:
    x4.append(x3[1])
elif x1[1] == x3[1]:
    x4.append(x2[1])
else:
    x4.append(x1[1])
    
print(x4[0],x4[1])