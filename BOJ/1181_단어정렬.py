n = int(input())
temp = []
for i in range(n):
    word = input()
    temp.append([word,len(word)])

temp.sort(key = lambda x : (x[1], x[0]))
for i in range(n):
    temp[i] = temp[i][0]
for i in range(n):
    if i >0:
        if temp[i-1] == temp[i]:
            continue
        else:
            print(temp[i])
    else:
        print(temp[i])