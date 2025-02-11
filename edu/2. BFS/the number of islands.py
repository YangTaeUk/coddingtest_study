from collections import deque

def solution(grid):

    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    xl = len(grid[0])
    yl = len(grid)
    q = deque() # deque([]) 대신 deque()로 선언하는 것이 더 간결
    count = 0
    # count를 활용하여 섬의 개수를 기록했는데, 방문 처리를 단순히 0으로 바꿔도 충분
    # count는 섬의 개수를 세는 데만 사용
    for i in range(0, yl):
        for j in range(0, xl):
            if grid[i][j] == 1:
                count += 1
                q.append((j, i))
                grid[i][j] = 0
                while q:
                    x, y = q.popleft()
                    for a, b in directions:
                        # 변수 이름을 직관적으로 변경 (ax, by → nx, ny
                        ax, by = x+a, y+b
                        if 0 <= ax < xl and 0 <= by < yl and grid[by][ax] == 1:
                            grid[by][ax] = 0
                            q.append((ax, by))
    return count

grid = [
    [1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0]
]
print(solution(grid))