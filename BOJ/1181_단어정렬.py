n = int(input())
temp = set([])
for i in range(n):
    word = input()
    temp.add(word)

temp = list(temp)
for i in range(len(temp)):
    temp[i] = [temp[i],len(temp[i])]

temp.sort(key = lambda x : (x[1], x[0]))

for i in range(len(temp)):
    print(temp[i][0])