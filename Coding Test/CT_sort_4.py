import sys
input = sys.stdin.readline

n, k = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

# 1번 풀이
for _ in range(k):
    a[a.index(min(a))], b[b.index(max(b))] = b[b.index(max(b))], a[a.index(min(a))]

print(sum(a))

# 2번 풀이
a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
    
print(sum(a))