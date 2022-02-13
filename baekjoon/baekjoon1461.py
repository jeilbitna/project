import sys
input = sys.stdin.readline
# 문제 풀이 keyword 1.양의 방향, 음의 방향 나누기 2. 거리가 가장 먼 곳은 나중에(손해 줄이기) 3. 원소 묶기(가까운 곳은 가는 김에 책 떨구고 가면 되므로 큰 값만 필요) 
n, m = map(int,input().split()) # n = 책의 개수, m = 한번에 가능 갯수
book = list(map(int,input().split())) # 책의 위치 모음 리스트
book.sort()
positive = [x for x in book if x > 0] # 양의 방향
negative = [x for x in book if x < 0] # 음의 방향
distance = [] # 가는 위치들(가다가 들리는 곳 말고)
result = 0
# 양의 방향
positive.sort(reverse=True)
for i in range(len(positive)//m):
    distance.append(positive[i*m])
if len(positive) % m != 0: #m개씩 묶어도 남는 게 생길 때
    distance.append(positive[(len(positive)//m) * m])


# 음의 방향
for i in range(len(negative)//m):
    distance.append(negative[i*m])
if len(negative) % m != 0:
    distance.append(negative[(len(negative)//m)*m])

distance = [abs(x) for x in distance] # 거리는 양수이므로 절댓값으로 바꿔줌
distance.sort()
result += distance.pop() # 오름차순 정렬이므로 distance.pop() 은 원점에서 가장 먼 위치가 나오게 된다. 이곳은 마지막에 들릴 곳이므로 *2를 하지 않는다.
result += sum(distance)*2 # 나머지 위치들은 책을 꽂아놓고 다른 책을 가지러 원점으로 와야하므로 *2를 해준다.
print(result)