
def dfs (grid, x, y, rows, cols, directions):
     grid[y][x] = 0
     for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
            dfs(grid, nx, ny, rows, cols, directions)
         

def solution(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]


    print("dfs")

grid = [
    [1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0]
]
print(solution(grid))