class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [0] * (n+1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_y] > self.rank[root_x]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
def kruskal(arr, n):
    arr.sort(key = lambda x: x[2])
    uf = UnionFind(n)
    mst = 0
    for x,y,z in arr:
        if uf.find(x) != uf.find(y):
            uf.union(x, y)
            mst += z
    return mst

from itertools import combinations
import sys
data = sys.stdin.readlines()

N,M = map(int, data[0].strip().split())
locations = [list(map(int, d.strip().split()))+[index+1] for index, d in enumerate(data[1:N+1])]
route = [list(map(int, d.strip().split()))+[0] for d in data[N+1:N+1+M]]

for ([x1,y1,index1],[x2,y2,index2]) in combinations(locations, 2):
    route.append([index1, index2, round((abs(x1-x2)**2 + abs(y1-y2)**2)**0.5,2)])

print(kruskal(route, N))
