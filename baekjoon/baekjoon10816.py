from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
cnt = Counter(a)
m = int(input())
b = list(map(int,input().split()))

for i in range(len(b)):
    if b[i] in cnt:
        b[i] = cnt[b[i]]
    else:
        b[i] = 0
print(*b)