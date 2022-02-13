import sys
input = sys.stdin.readline

n, m = map(int,input().split())
a = set()
b = set()
for _ in range(n): #듣도 못한 사람
    a.add(input().rstrip())

for _ in range(m):
    b.add(input().rstrip())

c = a&b # 교집합
c = list(c)
c.sort()
print(len(c))
for name in c:
    print(name)

# 시간 1등 답안
import sys
n, m = map(int, input().split())
nameList = sys.stdin.read().splitlines()
hearset = set(nameList[:n])
seeset = set(nameList[n:])
ret = list(hearset & seeset)
ret.sort()
print(len(ret))
for i in ret:
    print(i)