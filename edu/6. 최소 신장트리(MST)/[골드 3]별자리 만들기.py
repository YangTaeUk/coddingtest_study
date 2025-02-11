from itertools import combinations
from collections import defaultdict
import sys
data = sys.stdin.readlines()
n = int(data[0])
arr = [list(map(float, d.strip().split()))+[index] for index, d in enumerate(data[1:])]
graph = defaultdict(list)
index = 0
edge = []
for ([x1, y1, index1], [x2, y2, index2]) in combinations(arr, 2 ):
    edge.append((index1, index2, round((abs(x1-x2)**2+abs(y1-y2)**2)**0.5, 2)))

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        root_x = self.parent[x]
        root_y = self.parent[y]
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

def kruskal(n, edge):
    edge.sort(key=lambda x: x[2]) # 가중치 위치 가 0인경우, 2,3,위치에 따라 조정.
    uf = UnionFind(n)
    #mst = []
    mst = 0
    for u,v,weight in edge:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst += weight
    return mst

print(kruskal(n, edge))