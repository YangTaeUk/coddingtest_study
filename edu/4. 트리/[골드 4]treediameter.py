"""
12
1 2 3
1 3 2
2 4 5
3 5 11
3 6 9
4 7 1
4 8 7
5 9 15
5 10 4
6 11 6
6 12 10
"""
from collections import defaultdict, deque
import sys
sys.setrecursionlimit(1000000)
def dfs(node, dist, graph, visited):
    visited[node] = False
    max_dist_node = node
    max_dist = dist
    for weight, ne in graph[node]:
        if visited[ne]:
            ne_node, distance = dfs(ne, dist+weight, graph, visited)
            if max_dist < distance:
                max_dist_node = ne_node
                max_dist = distance

    return max_dist_node, max_dist


data = sys.stdin.readlines()
n = int(data[0])
graph = defaultdict(list)
for d in data[1:]:
    p, c, weight = map(int, d.strip().split())
    graph[p].append((weight, c))
    graph[c].append((weight, p))

visited = [True] * (n+1)
max_dist_by_one_node, _ = dfs(1, 0, graph, visited)
visited = [True] * (n+1)
_, max_dist_answer = dfs(max_dist_by_one_node, 0, graph, visited)

print(max_dist_answer)
