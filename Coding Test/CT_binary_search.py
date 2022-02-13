# 재귀함수
def binary_search(array, target, start, end):
    if start > end:
        return None
    
    mid = (start+end) // 2
     
    if array[mid] == target:
        return mid # target의 인덱스 반환
    
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    
    else:
        return binary_search(array, target, mid+1, end)

# 반복문
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    
    return None