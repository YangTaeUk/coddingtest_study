

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
max_cost = 0
for i in range(n):
    for j in range(n):
        if max_cost < cost[i][j]:
            max_cost = cost

dp = [0]*n for _ in range()
def DFS(current_node, visited, preprice):
    nonlocal
# 최대 그림 소유자 dp[이력][현재 소유자][구매가]
