import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)
inputA = sys.stdin.read
data = inputA().splitlines()
n = int(data[0])
arr = [-1] + list(map(int, data[1].strip().split()))
edge = [tuple(map(int, d.strip().split())) for d in data[2:]]
graph = defaultdict(list)

for u,v in edge:
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)
dp = [[0,0] for _ in range(n+1)]
dp_trace = [[[],[]] for _ in range(n+1)]

def dfs(node):
    dp[node][1] = arr[node]
    dp_trace[node][1].append(node)
    visited[node] = True

    for ne in graph[node]:
        if not visited[ne]:
            dfs(ne)
            if dp[ne][0] < dp[ne][1]:
                dp[node][0] += dp[ne][1]
                dp_trace[node][0].extend(dp_trace[ne][1])
            else:
                dp[node][0] += dp[ne][0]
                dp_trace[node][0].extend(dp_trace[ne][0])
            dp[node][1] += dp[ne][0]
            dp_trace[node][1].extend(dp_trace[ne][0])
dfs(1)
if dp[1][0] < dp[1][1]:
    print(dp[1][1])
    dp_trace[1][1].sort()
    print(" ".join(map(str, dp_trace[1][1])))
else:
    print(dp[1][0])
    dp_trace[1][0].sort()
    print(" ".join(map(str, dp_trace[1][0])))
