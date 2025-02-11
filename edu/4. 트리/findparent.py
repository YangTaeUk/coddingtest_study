"""
7
1 6
6 3
3 5
4 1
2 4
4 7
"""
import sys
from collections import defaultdict, deque

data = sys.stdin.readlines()
n = int(data[0])
graph = defaultdict(list)
for d in data[1:]:
    u, v = map(int, d.strip().split())
    graph[u].append(v)
    graph[v].append(u)
q = deque([])
parent = [-1] * (n+1)
parent[1] = 1
q.append(1)
while q:
    node = q.popleft()
    for ne in graph[node]:
        if parent[ne] == -1:
            parent[ne] = node
            q.append(ne)
for p in parent[2:]:
    print(p)


