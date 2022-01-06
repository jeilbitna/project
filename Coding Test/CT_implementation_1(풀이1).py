location = list(map(str,input()))
change = ['','a','b','c','d','e','f','g','h']
location[0] = change.index(location[0])
location = list(map(int,location))
print(location)

dx = [2,2,-2,-2,1,1,-1,-1]
dy = [1,-1,1,-1,2,-2,2,-2]

result = 0

for i in range(8):
    if 1 <= (location[0] + dx[i]) <= 8 and 1 <= (location[1] + dy[i]) <= 8:
        result += 1

print(result)