A, B, C = map(int, input().split())  #공백을 두고 A,B,C를 입력

if B>=C:
    print(-1)
else:
    print(A//(C-B)+1)