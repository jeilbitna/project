import sys
input = sys.stdin.readline

n = int(input())
array = []
for i in range(1,n+1):
    age, name = map(str,input().rstrip().split())
    array.append((int(age),i,name))

array.sort(key=lambda data:(data[0],data[1]))

for age, rank, name in array:
    print(age, name)



