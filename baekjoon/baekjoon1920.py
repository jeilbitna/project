import sys
input = sys.stdin.readline

n = int(input())
array = input().strip().split(' ')
m = int(input())
targets = input().strip().split(' ')
array = set(array)

for target in targets:
    print(1 if target in array else 0)
