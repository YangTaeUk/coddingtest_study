"""

나 이거 풀었었어
트리의 정점의 수 N과 루트의 번호 R, 쿼리의 수 Q가 주어진다. (2 ≤ N ≤ 105, 1 ≤ R ≤ N, 1 ≤ Q ≤ 105)
이어 N-1줄에 걸쳐, U V의 형태로 트리에 속한 간선의 정보가 주어진다. (1 ≤ U, V ≤ N, U ≠ V)
이는 U와 V를 양 끝점으로 하는 간선이 트리에 속함을 의미한다.
이어 Q줄에 걸쳐, 문제에 설명한 U가 하나씩 주어진다. (1 ≤ U ≤ N)
입력으로 주어지는 트리는 항상 올바른 트리임이 보장된다.
"""
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
inputA = sys.stdin.read
data = inputA().splitlines()
n,r,q = map(int, data[0].strip().split())
edge = [tuple(map(int, d.strip().split())) for d in data[1:n]]
arr = [int(d.strip()) for d in data[n:n+q]]
graph = defaultdict(list)
for u,v in edge:
    graph[u].append(v)
    graph[v].append(u)

sub_node = [-1] * (n+1)
visited = [False] * (n+1)
def dfs(node):
    sub_node[node] = 1
    visited[node] = True
    for ne in graph[node]:
        if not visited[ne]:
            dfs(ne)
            sub_node[node] += sub_node[ne]

dfs(r)

for a in arr:
    print(sub_node[a])

