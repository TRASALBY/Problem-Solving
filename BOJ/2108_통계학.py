
from random import randrange


n = int(input())
list1 = []
for i in range(n):
    list1.append(int(input()))
    
print(round(sum(list1)/n))
sorted_list = sorted(list1)
print(sorted_list[int(n/2)])

list2 = []
for i in list1:
    list2.append(list1.count(i))

list3 = []
m = max(list2)
for i in range(len(list2)):
    if list2[i] == m:
        list3.append(i)
list4 = []
for i in range(len(list3)):
    list4.append(list1[list3[i]])
if len(list4) == 1:
    print(list4[0])
else:
    set = set(list4)
    list4 = list(set)
    list4 = sorted(list4)
    
    print(list4[1])
print(max(list1) - min(list1))