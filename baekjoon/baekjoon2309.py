import sys
input = sys.stdin.readline

array = []
isbreak = False
for _ in range(9):
    array.append(int(input()))

array.sort()
goal = sum(array) - 100

for i in range(len(array)-1,-1,-1):
    for j in range(len(array)-1):
        if array[i] + array[j] == goal:
            del array[i],array[j]
            isbreak = True
            break
    if isbreak:
        break
    
for num in array:
    print(num)