# 이진 탐색
import sys
input = sys.stdin.readline

def binary_search(array, target, start, end):
    if start > end:
        return None
    
    mid = (start+end) // 2

    if array[mid] == target:
        return "yes"

    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    
    else:
        return binary_search(array, target, mid+1, end)



n = int(input())
array = list(map(int,input().split()))
m = int(input())
targets = list(map(int,input().split()))

array.sort()
for target in targets:
    result = binary_search(array, target, 0, n-1)
    if result == None:
        print("no", end=' ')
    else:
        print(result, end=' ')