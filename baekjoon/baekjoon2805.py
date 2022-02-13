# Counter 쓰는게 훨씬 빠름
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
trees = list(map(int,input().split())) # tree <= 1e9

start = 0
end = max(trees)
result = 0 # 정답
# 이진 탐색
while (start <= end):
    total = 0
    mid = (start+end) // 2

    for tree in trees:
        if tree > mid:
            total += (tree-mid)
    
    if total >= m: # 나무를 너무 많이 자름 -> 줄여야 함
        result = mid
        start = mid + 1
    else: # 나무를 너무 적게 자름 -> 늘려야 함
        end = mid - 1

print(result)       
        