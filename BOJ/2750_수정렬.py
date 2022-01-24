from tkinter import N


def bubble_sort(list):
    for i in range(len(list)):
        for j in range(i):
            if(list[i]<list[j]):
                list[i], list[j] = list[j], list[i]
                

n = int(input())
list = []
for i in range(n):
    a = int(input())
    list.append(a)
bubble_sort(list)

for i in range(n):
    print(list[i])
