"""
첫 번째 줄에는 친구 관계 트리의 정점 개수 N이 주어진다.
단, 2 ≤ N ≤ 1,000,000이며, 각 정점은 1부터 N까지 일련번호로 표현된다.
두 번째 줄부터 N-1개의 줄에는 각 줄마다 친구 관계 트리의 에지 (u, v)를 나타내는 두 정수 u와 v가 하나의 빈칸을 사이에 두고 주어진다.
"""
import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)
inputA = sys.stdin.read
data = inputA().splitlines()
n = int(data[0])
edge = [tuple(map(int, d.strip().split())) for d in data[1:]]
graph = defaultdict(list)

for u,v in edge:
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)
dp = [[0, 0] for _ in range(n+1)]

def dfs(node):
    dp[node][1] = 1
    visited[node] = True
    for ne in graph[node]:
        if not visited[ne]:
            dfs(ne)
            dp[node][0] += dp[ne][1]  # 자식이 얼리 어답터일 경우
            dp[node][1] += min(dp[ne][0], dp[ne][1])  # 자식이 얼리 어답터일 수도, 아닐 수도 있음


dfs(1)

print(min(dp[1]))