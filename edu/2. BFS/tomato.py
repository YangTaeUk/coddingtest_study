#사용자가 언급한 내용이 맞습니다. 예제 입력으로 주어진 grid = [[0, 1, 0],
#[-1, 0, 1], [0, -1, 0]]에서, 익을 수 없는 토마토(값이 0인 칸)가 존재합니다.
#예를 들어, grid[2][0]은 익은 토마토(값 1)와 연결되지 않았기 때문에 익을 수
#없습니다. 따라서 정답은 -1이어야 합니다.
from collections import deque

def solution(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_tomatoes = 0  # 익지 않은 토마토 개수
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # 초기 상태 설정
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # 익은 토마토
                queue.append((i, j, 0))  # (행, 열, 시간)
            elif grid[i][j] == 0:  # 익지 않은 토마토
                fresh_tomatoes += 1

    # BFS 탐색
    days = 0
    while queue:
        x, y, days = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                grid[nx][ny] = 1  # 토마토 익히기
                fresh_tomatoes -= 1
                queue.append((nx, ny, days + 1))

    # 익지 않은 토마토가 남아 있는 경우
    if fresh_tomatoes > 0:
        return -1

    return days
