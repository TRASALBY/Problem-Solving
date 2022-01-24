#Fly me to the Alpha Centauri

T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    cnt = 0
    b = y - x
    while(True):
