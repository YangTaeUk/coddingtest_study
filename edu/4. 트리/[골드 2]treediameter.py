"""
5
1 3 2 -1
2 4 4 -1
3 1 2 4 3 -1
4 2 4 3 3 5 6 -1
5 4 6 -1
"""
# 메모리 초과
# import sys
#
# data = sys.stdin.readlines()
# n = int(data[0])
# inf = float('inf')
# route = [[inf] * (n+1) for _ in range(n+1)]
# for d in data[1:]:
#     arr = list(map(int, d.strip().split()))
#     node = arr[0]
#     loop = ()
#     for i in range(1, loop, 2):
#         route[arr[0]][arr[i]] = arr[i+1]
#
# for self in range(1, n+1):
#     route[self][self] = 0
#
# max_dist = 0
# for k in range(1, n+1):
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             route[i][j] = min(route[i][j], route[i][k]+route[k][j])
#             if route[i][j] != inf:
#                 max_dist = max(route[i][j], max_dist)
#
# print(max_dist)

import sys
from collections import defaultdict

sys.setrecursionlimit(1000000)
def dfs(node, distance, visited, graph):
    visited[node] = True
    max_distance = distance
    farthest_node = node

    for neighbor, weight in graph[node]:
        if not visited[neighbor]:
            dist, farthest = dfs(neighbor, distance + weight, visited, graph)
            if dist > max_distance:
                max_distance = dist
                farthest_node = farthest

    return max_distance, farthest_node

input = sys.stdin.read
data = input().splitlines()
n = int(data[0])

graph = defaultdict(list)
for line in data[1:]:
    arr = list(map(int, line.split()))
    node = arr[0]
    for i in range(1, len(arr) - 1, 2):
        neighbor = arr[i]
        weight = arr[i + 1]
        graph[node].append((neighbor, weight))

visited = [False] * (n + 1)
_, farthest_node = dfs(1, 0, visited, graph)  # 1번 노드에서 가장 먼 노드 찾기

visited = [False] * (n + 1)
diameter, _ = dfs(farthest_node, 0, visited, graph)  # 가장 먼 노드에서 다시 가장 먼 노드 찾기

print(diameter)

