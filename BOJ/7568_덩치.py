n = int(input())
people = []
for i in range(n):
    person = tuple(map(int, input().split()))
    people.append(person)
rank = [0] * n
ind = 0
for person1 in people:
    for person2 in people:
        if person1[0] < person2[0] and person1[1] < person2[1]:
            rank[ind] += 1
    ind+=1

rank = list(map(lambda x : x+1,rank))

for i in range(n):
    print(rank[i], end=" ")