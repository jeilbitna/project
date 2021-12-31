location = input()

row = int(location[1]) # 가로 좌표값
column = int(ord(location[0])) - int(ord('a')) + 1 #세로 좌표값(원래 알파벳이었던 것)

moves = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
result = 0
for move in moves:
    new_row = row + move[0]
    new_column = column + move[1]

    if 1 <= new_row <= 8 and 1 <= new_column <= 8:
        result += 1

print(result)

