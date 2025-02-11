from collections import defaultdict
import sys
inputA = sys.stdin.read
data = inputA().splitlines()
n = int(data[0].strip())
arr = list(map(int, data[1].strip().split()))
edge = [tuple(map(int, d.strip().split())) for d in data[2:]]

graph = defaultdict(list)
for u, v in edge:
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

visited = [False] * n
dp = [[0, 0] for _ in range(n)]

def dfs(node):
    visited[node] = True
    dp[node][1] = arr[node]

    for ne in graph[node]:
        if not visited[ne]:
            dfs(ne)
            dp[node][0] += max(dp[ne][0],dp[ne][1])
            dp[node][1] += dp[ne][0]
dfs(0)

for i in range(n):
    print(dp[i])