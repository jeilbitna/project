import sys
# 해설
n,m = map(int,sys.stdin.readline().split())

d = [[0]*m for _ in range(n)] # 방문한 위치 저장

x, y, direction = map(int,sys.stdin.readline().split())
d[x][y] = 1 # 방문 처리

#전체 맵 정보
array = [] 
for _ in range(n):
    array.append(list(map(int,sys.stdin.readline().split()))) # 맵 정보 넣기

# 북,동,남,서 순으로 방향 정의
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 왼쪽에서 회전하는 기능을 하는 함수
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션
count = 1
turn_time = 0

while True:
    turn_left() # 왼쪽으로 돈다.
    nx = x + dx[direction] # 새로운 x좌표
    ny = y + dy[direction] # 새로운 y좌표
    # 회전하고 정면에 가보지 않은 칸이 있을 때 -> 이동한다.
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1 # 가본 땅으로 처리
        x,y = nx,ny # 이동했으므로 x,y 좌표 바꿔줌
        count += 1 # 가본 칸 수 추가
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x,y = nx,ny
        else:
            break
        turn_time = 0

print(count)
