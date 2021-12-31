n = int(input())
plans = input().split() # 이동 계획
x,y = 1,1 # 초기 좌표

move_type = ['L','R','U','D']
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for plan in plans:
    for i in range(len(move_type)):
        if plan == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x,y = nx,ny

print(x,y)
