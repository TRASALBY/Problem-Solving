str = input().split("-")

for i in range(len(str)):
    str2 = str[i].split("+")
    sum = 0
    for j in range(len(str2)):
        sum += int(str2[j])
    str[i] = sum

sum = int(str[0]) * 2
for k in str:
    sum -= int(k)
print(sum)