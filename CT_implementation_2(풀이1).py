import sys
# 내 풀이
n,m = map(int,sys.stdin.readline().split()) # 맵 크기
row, column, direction = map(int,sys.stdin.readline().split())
maps = []

for _ in range(n):
    maps.append(list(map(int,sys.stdin.readline().split())))

drow = [-1,0,1,0]
dcolumn = [0,-1,0,1]

# 바다로 된 공간은 갈 수 없음.
# 1. 왼쪽 방향부터 갈 곳 정함.
# 2-1. 안 가본 칸 있을 때 = 왼쪽 회전 + 한 칸 전진
# 2-2. 안 가본 칸 없을 때 = 왼쪽 회전
# 3. 네 방향 모두 가본칸 or 바다일 때 = 방향 유지 + 뒤로 1칸 (단, 뒤쪽 방향이 바다이면(뒤로 갈 수 없으면) 움직임 멈춤.)
# 가본 칸은 -1로 바꿀것.
result = 1 # 결과
cannot = 0 # 이동하지 못한 횟수

while True:
    new_direction = (direction+1)%4 # 현재 보는 방향 기준 왼쪽 방향
    new_row, new_column = (row + drow[new_direction]), (column + dcolumn[new_direction]) # 새로운 row, column

    if maps[new_row][new_column] == 0: # 가보지 않은 칸이 있는 경우(육지)
        result += 1 # 가본 칸 추가
        maps[row][column] = -1 # 원래 있던 칸을 -1로 바꾸면서 가본 칸 표시
        row, column, direction = new_row, new_column, new_direction
        cannot = 0
    
    else: # 가보지 않은 칸이 없거나 바다인 경우
        cannot += 1
        if cannot == 4: # 종료 조건
            new_direction = (direction+2)%4 # 반대 방향 설정
            row, column = (row + drow[new_direction]), (column + dcolumn[new_direction])
            if maps[row][column] == 1: # 뒤로 한칸 갔는데 바다인 경우
                break # 종료
            cannot = 0 # 다시 못간 횟수 초기화
            
        else:
            direction = new_direction
    

print(result)
