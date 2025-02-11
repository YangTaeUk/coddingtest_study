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
    edge.sort(key=lambda x: x[0]) # 가중치 위치 가 0인경우, 2,3,위치에 따라 조정.
    uf = UnionFind(n)
    mst = []
    for u,v,weight in edge:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u,v,weight))
    return mst