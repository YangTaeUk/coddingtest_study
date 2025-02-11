

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

directions = [(1,0),(0,1),(-1,0),(0,-1)]
dp = [[-1]*m for _ in range(n)]

def dfs(x, y):
    if x == n-1 and y == m-1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0

    for dx,dy in directions:
        nx, ny = x+dx, y+dy
        if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] < arr[x][y]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]

print(dfs(0,0))