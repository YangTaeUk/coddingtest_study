from collections import deque
from pprint import pprint
import sys
sys.setrecursionlimit(10**6)

def incoordinates(rectangle, coordinates):
    if rectangle[0] < rectangle[2]: bigx, smallx = rectangle[2], rectangle[0]
    else: bigx, smallx = rectangle[0], rectangle[2]
    if rectangle[1] < rectangle[3]: bigy, smally = rectangle[3], rectangle[1]
    else : bigy, smally = rectangle[1], rectangle[3]
    bigx = bigx * 2
    smallx = smallx * 2
    bigy = bigy * 2
    smally = smally * 2

    for i in range(smallx, bigx + 1):
        for j in range(smally, bigy + 1):
            if coordinates[j][i] == 0 or coordinates[j][i] == 3:
                if i == smallx or j == smally or i == bigx or j == bigy:
                    coordinates[j][i] = 3
                else:
                    coordinates[j][i] = 5

    return coordinates

def solution(rectangle, characterX, characterY, itemX, itemY):

    q = deque([(characterX * 2,characterY * 2, 0)])
    directions = [(-1,0),(0,-1),(1,0),(0,1)]
    visit = set((characterX * 2, characterY * 2))

    coordinates = [[0 for i in range(102)] for i in range(102)]
    for rect in rectangle:
        incoordinates(rect, coordinates)


    while q:
        x, y, distance = q.popleft()

        if x == itemX * 2 and y == itemY * 2:
            # for ar in coordinates:
            #     print(ar)
            return int(distance / 2)

        for dx, dy in directions:  # 네 방향으로 이동
            nx, ny = x + dx, y + dy

            if coordinates[ny][nx] == 3 and (nx, ny) not in visit:
                coordinates[ny][nx] = 7
                q.append((nx, ny, distance + 1))
                visit.add((nx, ny))


    return -1  # 목적지에 도달할 수 없는 경우 -1 반환
# 11 14 17 74

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],
               1,3,7,8))
print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]],
               9,7,6,1))
print(solution([[1,1,5,7]],
               1,1,4,7))
print(solution([[2,1,7,5],[6,4,10,10]],
               3,1,7,10))
