import sys
input = sys.stdin.readline

n = int(input()) # 가지고 있는 카드 개수
a = list(map(int,input().split())) # 가지고 있는 거
a_dict = dict.fromkeys(a) # 가진 카드들이 담긴 딕셔너리
m = int(input())
b = list(map(int,input().split()))

for i in range(len(b)):
    if b[i] in a_dict:
        b[i] = 1
    else:
        b[i] = 0

print(*b)