import sys
input = sys.stdin.readline

n = int(input())

steps = []

for _ in range(n):
    steps.append(list(map(int,input().split())))

for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            steps[i][j] = steps[i][j] + steps[i-1][j]
        
        elif j == i:
            steps[i][j] = steps[i][j] + steps[i-1][j-1]
        
        else:
            steps[i][j] = max(steps[i-1][j-1]+steps[i][j], steps[i-1][j]+steps[i][j])

print(max(steps[n-1]))