import sys

input = sys.stdin.readline

n = int(input())
t = list(map(int,input().split()))
result = [0 for _ in range(n)]
stack = []

for i in range(n):
    now = t[i]
    while stack and now > t[stack[-1]]:
        stack.pop()
    
    if stack:
        result[i] = stack[-1] + 1
    
    stack.append(i)

print(*result)