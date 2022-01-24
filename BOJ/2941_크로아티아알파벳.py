word = input()

croatia=['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in croatia:
    if(i in word):
        word = word.replace(i,'*')
print(word)