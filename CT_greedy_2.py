import sys
# 풀이 2
N, M, K = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()

first = arr[-1] # 가장 큰 수
second = arr[-2] # 두 번째로 큰 수

count_first = (M // (K+1)) * K + (M % (K+1)) # 가장 큰 수가 나타나는 횟수
count_second = M - count_first

answer = 0

answer += count_first * first
answer += count_second * second

print(answer)