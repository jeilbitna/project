import sys

N, K = map(int, sys.stdin.readline().split())
t = 0

while N >= K:
    if N % K == 0:
        t += 1
        N //= K
    else:
        t += 1
        N -= 1

while N > 1:
    N -= 1
    t += 1

print(t)