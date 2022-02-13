from collections import Counter
import sys
input = sys.stdin.readline

a = []
n = int(input()) # 1 <= n <= 500,000 (단, n은 홀수)

for _ in range(n):
    a.append(int(input()))

# 1.산술평균
print(round(sum(a)/len(a) ))

# 2.중앙값
a.sort()
print(a[len(a)//2])

# 3.최빈값
counter = Counter(a).most_common(2)

if len(a) > 1:
    
    if counter[0][1] == counter[1][1]: # 최빈값이 같은 게 2개 있을 경우
        print(counter[1][0])
    
    else:
        print(counter[0][0])
else:
    print(counter[0][0])
# 4.범위
print(max(a)-min(a))
