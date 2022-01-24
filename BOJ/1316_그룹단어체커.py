n = int(input())
words = []
for i in range(n):
    word = input()
    words.append(word)

cnt = 0
for i in words:
    s = []
    s.append(i[0])
    for j in range(1,len(i)):
        if(i[j-1] != i[j]):
            if(i[j] in s):
                cnt+=1
                break
            else:
                s.append(i[j])
print(n-cnt)