import sys
# 풀이 1
N, M, K = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))
arr.sort()

first = arr[-1]
second = arr[-2]
answer = 0

while True:
    for _ in range(K):
        if M == 0:
            break
        answer += first
        M -= 1
    
    if M == 0:
        break
    answer += second
    M -= 1

print(answer)