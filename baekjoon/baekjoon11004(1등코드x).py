import sys
input = sys.stdin.readline

n, k = map(int,input().split())
s = sorted(map(int,input().split()))
print(s[k-1])

# 시간 1등 코드
