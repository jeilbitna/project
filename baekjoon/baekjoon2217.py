import sys
input = sys.stdin.readline

n = int(input())
rope = []

for _ in range(n):
    rope.append(int(input()))

rope.sort(reverse=True)
max_weight = rope[0] # 초기 값
for i in range(1,len(rope)):
    if max_weight < (i+1) * rope[i]:
        max_weight = (i+1) * rope[i]

print(max_weight)
