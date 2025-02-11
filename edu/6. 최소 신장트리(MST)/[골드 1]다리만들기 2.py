"""
첫째 줄에 지도의 세로 크기 N과 가로 크기 M.
둘째 줄부터 N개의 줄에 지도의 정보.
각 줄은 M개의 수로 이루어져 있으며, 수는 0 또는 1이다. 0은 바다, 1은 땅

모든 섬을 연결하는 다리 길이의 최솟값을 출력.(불가능하면 -1)
"""
from collections import deque
directions = [(0,1), (1,0), (-1,0), (0,-1)]
def check_the_island(board, n, m):
    q = deque([])
    visited = set()
    num = 1
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                num += 1
                q.append((i, j))
                visited.add((i, j))
                while q:
                    cx, cy = q.popleft()
                    board[cx][cy] = num
                    for dx, dy in directions:
                        nx, ny = cx+dx, cy+dy
                        if 0<=nx<n and 0<=ny<m and (nx, ny) not in visited and board[nx][ny] == 1:
                            visited.add((nx, ny))
                            q.append((nx, ny))
    return num
def planing_bridge(board, n, m):
    bridges = []
    for i in range(n):
        for j in range(m):
            if board[i][j] >= 2:
                start = board[i][j]
                for k in range(4):
                    sx, sy = i, j
                    length = 0
                    while True:
                        sx += directions[k][0]
                        sy += directions[k][1]
                        if not (0 <= sx < n and 0 <= sy < m):  # 지도 밖
                            break
                        if board[sx][sy] == start:  # 같은 섬
                            break
                        if board[sx][sy] == 0:  # 바다
                            length += 1
                        elif board[sx][sy] >= 2:  # 다른 섬 도착
                            if length >= 2:
                                bridges.append((start, board[sx][sy], length))
                            break
    return bridges
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
    uf.union(0, 2)
    uf.union(1, 2)
    mst = 0
    for x,y,z in arr:
        if uf.find(x) != uf.find(y):
            uf.union(x, y)
            mst += z
    union_num = uf.find(2)
    for i in range(3, n+1):
        if union_num != uf.find(i):
            return -1
    return mst

import sys
data = sys.stdin.readlines()
N, M = map(int, data[0].strip().split())
board = [list(map(int, d.strip().split())) for d in data[1:]]

count = check_the_island(board, N, M)
graph = planing_bridge(board, N, M)
print(kruskal(graph, count))