
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # 부모 초기화
        self.rank = [0] * n  # 트리 깊이 저장
        self.parent_size = [1] * n  # 각 그룹의 크기 저장

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:  # 다른 집합이면 병합
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
                self.parent_size[root_x] += self.parent_size[root_y]
                self.parent_size[root_y] = self.parent_size[root_x]
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
                self.parent_size[root_y] += self.parent_size[root_x]
                self.parent_size[root_x] = self.parent_size[root_y]
            else:
                self.parent[root_y] = root_x
                self.parent_size[root_x] += self.parent_size[root_y]
                self.parent_size[root_y] = self.parent_size[root_x]
                self.rank[root_x] += 1
import sys
data = sys.stdin.readlines()
n = int(data[0].strip())
vector_list = list(tuple(map(int, d.strip().split())) for d in data[1:])
vector_set = UnionFind(n)

def ccw(x1,y1,x2,y2,x3,y3):
    return (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)
def cross_check(point1, point2):
    x1, y1, x2, y2 = point1
    x3, y3, x4, y4 = point2
    ccw1 = ccw(x1,y1,x2,y2,x3,y3)
    ccw2 = ccw(x1,y1,x2,y2,x4,y4)
    ccw3 = ccw(x3,y3,x4,y4,x1,y1)
    ccw4 = ccw(x3,y3,x4,y4,x2,y2)

    if ccw1 * ccw2 < 0 and ccw3 * ccw4 < 0:
        return 1

    def is_between(a,b,c):
        return min(a,b) <= c <= max(a,b)

    if ccw1 == 0 and is_between(x1, x2, x3) and is_between(y1, y2, y3):
        return 1
    if ccw2 == 0 and is_between(x1, x2, x4) and is_between(y1, y2, y4):
        return 1
    if ccw3 == 0 and is_between(x3, x4, x1) and is_between(y3, y4, y1):
        return 1
    if ccw4 == 0 and is_between(x3, x4, x2) and is_between(y3, y4, y2):
        return 1

for i in range(n):
    for j in range(i+1, n):
        if vector_set.find(i) != vector_set.find(j):
            if cross_check(vector_list[i],vector_list[j]) == 1:
                vector_set.union(i, j)

print(len(set(vector_set.find(i) for i in range(n))))
print(max(vector_set.parent_size))