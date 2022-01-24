arr = input()

length = len(arr)

for i in range(length):
    ASCII = ord(arr[i])
    if(ASCII-3<ord("A")):
        ASCII = ord(arr[i])+26
    print(chr(ASCII-3),end="")
