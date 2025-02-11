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
    all_route = 0
    mst = 0
    for x,y,z in arr:
        if uf.find(x) != uf.find(y):
            uf.union(x, y)
            mst += z
        all_route += z
    return all_route - mst

import sys
data = sys.stdin.readlines()
index = 0
while True:
    m, n = map(int, data[index].strip().split())
    if m == 0 and n == 0:
        break
    xyz = [list(map(int, d.strip().split())) for d in data[index+1:index+1+n]]
    print(kruskal(xyz, m))
    index += n+1
