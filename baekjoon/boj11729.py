n = int(input())
stepList = []

def solve(n, start, end, tmp):
    if n == 1:
        stepList.append((start, end))
    else:
        solve(n-1, start, tmp, end)
        stepList.append((start, end))
        solve(n-1, tmp, end, start)
        # n개를 옮기면, 1. n-1개를 start->tmp에, 2. 맨밑의(n번째)거를 목표(start->end)에, 3. n-1개를 tmp->end에 
    
solve(n, 1, 3, 2)

# 정답 출력
print(len(stepList))

for step in stepList:
    print(step[0], step[1], sep=' ')
