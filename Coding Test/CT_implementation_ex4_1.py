
N = int(input())
trip = list(map(str,input().split()))
location = [1,1]

for x in trip:
    if x == 'L' and location[1] > 1:
        location[1] -= 1
    elif x == 'R' and location[1] < N:
        location[1] += 1
    elif x == 'U' and location[0] > 1:
        location[0] -= 1
    elif x == 'D' and location[0] < N:
        location[0] += 1

print(*location)