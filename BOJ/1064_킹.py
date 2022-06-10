import sys
def king_moving(X):
    global king
    global king_copy

    if X == 'L':
        king_copy[0] -= 1
    if X == 'R':
        king_copy[0] += 1
    if X == 'B':
        king_copy[1] -= 1
    if X == 'T':
        king_copy[1] += 1


def stone_moving(X):
    global stone
    global stone_copy

    if X == 'L':
        stone_copy[0] -= 1
    if X == 'R':
        stone_copy[0] += 1
    if X == 'B':
        stone_copy[1] -= 1
    if X == 'T':
        stone_copy[1] += 1


global king
global stone
global king_copy
global stone_copy

input = sys.stdin.readline
king, stone, n = map(str,input().split())

column = ['A','B','C','D','E','F','G','H']
king = [column.index(king[0]),int(king[1])]
stone = [column.index(stone[0]),int(stone[1])]

king_copy,stone_copy = king.copy(),stone.copy()

for i in range(int(n)):
    king_copy = king.copy()
    stone_copy = stone.copy()

    move = input().rstrip()
    for j in range(len(move)):
        king_moving(move[j])
    
    if (king_copy[0] >= 0 and king_copy[0] < 8) and (king_copy[1] > 0 and king_copy[1] < 9):
        if king_copy == stone:
            for k in range(len(move)):
                stone_moving(move[k])
            if (stone_copy[0] >= 0 and stone_copy[0] < 8) and (stone_copy[1] > 0 and stone_copy[1] < 9):
                stone = stone_copy.copy()
                king = king_copy.copy()
        else:
            king = king_copy.copy()
print(column[king[0]]+str(king[1]))
print(column[stone[0]]+str(stone[1]))
