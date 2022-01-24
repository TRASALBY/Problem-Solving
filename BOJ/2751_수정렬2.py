
def merge(list, m, middle, n):
    i = m
    j = middle + 1
    k = m
    #작은순서 대로 배열에 삽입

    while(i<=middle and j<=n):
        if list[i] <= list[j]:
            sorted_list[k] = list[i]
            i+=1
        else:
            sorted_list[k] = list[j]
            j+=1
        k+=1
    
    if(i>middle):
        for t in range(j,n):
            sorted_list[k] = list[t]
            k+=1
    else:
        for t in range(j,n):
            sorted_list[k] = list[t]
            k+=1
    
    for i in range(len(list)):
        list[i] = sorted_list[i]


def merge_sort(list, m, n):
    if m < n:
        middle = (m + n) // 2
        merge_sort(list, m, middle)
        merge_sort(list, middle+1, n)
        merge(a,m,middle,n)

n = int(input())
list = []
sorted_list = []

for i in range(n):
    a = int(input())
    list.append(a)

merge_sort(list, 0, len(list))
for i in range(n):
    print(list[i])