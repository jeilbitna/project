import sys
input = sys.stdin.readline

k= int(input())
array = []
for _ in range(k):
    num = int(input())
    if num == 0:
        array.remove(array[-1])
    else:
        array.append(num)
print(sum(array))