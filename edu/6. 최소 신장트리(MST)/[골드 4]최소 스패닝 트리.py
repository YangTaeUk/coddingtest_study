class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
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
def kruskal(graph, n):
    graph.sort(key=lambda x:x[2])
    uf = UnionFind(n)
    mst = 0
    for u, v, weight in graph:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst += weight
    return mst

import heapq
def prim(graph, n, start=1):
    q =[(0, start)]
    visited = [False] * n
    mst_cost = 0
    visited[start] = True
    while q:
        (weight, node) = heapq.heappop(q)
        if not visited[node]:
            visited[node] = True
            mst_cost += weight
        for w, ne in graph[node]:
            if not visited[ne]:
                heapq.heappush(q, (w, ne))

    return mst_cost

from collections import defaultdict
import sys
data = sys.stdin.readlines()
V, E= map(int, data[0].strip().split())
arr = [list(map(int, d.strip().split())) for d in data[1:]]
graph = defaultdict(list)
for a in arr:
    graph[a[0]].append((a[2], a[1]))

print(kruskal(arr, V+1))
print(prim(graph, V+1))