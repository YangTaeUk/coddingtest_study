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
                self.parent[y] = root_x
            elif self.rank[root_y] > self.rank[root_x]:
                self.parent[x] = root_y
            else:
                self.parent[y] = root_x
                self.rank[x] += 1
def kruskal(graph, n):
    #graph.sort(key) 가중치가 음슴
    uf = UnionFind(n)
    mst = 0
    for u, v in graph:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst += 1
    return mst

from collections import deque
def prim(graph, n, start=1):
    q = deque([start])
    visited = [False] * n
    mst_cost = 0
    visited[start] = True
    while q:
        node = q.popleft()
        if not visited[node]:
            visited[node] = True
            mst_cost += 1
        for ne in graph[node]:
            if not visited[ne]:
                q.append(ne)

    return mst_cost

from collections import defaultdict
import sys
data = sys.stdin.readlines()
T = int(data[0].strip())
index = 1
for _ in range(T):
    N, M = map(int, data[index].strip().split())
    arr = [list(map(int, d.strip().split())) for d in data[index+1:M+index+1]]
    index += M+1
    graph = defaultdict(list)
    for a in arr:
        graph[a[1]].append(a[0])
        graph[a[0]].append(a[1])

    print(kruskal(arr, N+1))
    # print(prim(graph, N+1))