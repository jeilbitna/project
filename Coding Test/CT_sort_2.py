import sys
input = sys.stdin.readline

n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

array = sorted(array, reverse = True)

for num in array:
    print(num,end=' ')