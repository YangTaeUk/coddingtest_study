"""
5 5
....1
#1###
.1.#0
....A
.1.#.
"""
from collections import defaultdict, deque
import sys

# 입력을 한 번에 읽음
input_data = sys.stdin.read().splitlines()
# 첫 줄에서 행(R)과 열(C) 읽기
row, col = map(int, input_data[0].split())
# 나머지 줄을 격자 형태로 저장
inputboard  = [list(l) for l in input_data[1:]]

def bfs_escape_maze(grid, start, R, C):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # BFS 큐: (x, y, keys, distance)
    queue = deque([(start[0], start[1], 0, 0)])  # (x, y, keys, distance)
    visited = set()
    visited.add((start[0], start[1], 0))

    while queue:
        x, y, keys, dist = queue.popleft()

        # 출구에 도달하면 거리 반환
        if grid[x][y] == '1':
            return dist

        # 네 방향으로 이동
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < R and 0 <= ny < C:
                cell = grid[nx][ny]

                # 벽(#)은 통과 불가
                if cell == '#':
                    continue

                # 열쇠(a~f) 주움
                if 'a' <= cell <= 'f':
                    new_keys = keys | (1 << (ord(cell) - ord('a')))
                else:
                    new_keys = keys

                # 문(A~F) 체크: 열쇠가 없으면 통과 불가
                if 'A' <= cell <= 'F' and not (new_keys & (1 << (ord(cell) - ord('A')))):
                    continue

                # 새로운 상태 (nx, ny, new_keys)가 방문되지 않았을 때만 추가
                if (nx, ny, new_keys) not in visited:
                    visited.add((nx, ny, new_keys))
                    queue.append((nx, ny, new_keys, dist + 1))

    # 출구에 도달할 수 없는 경우
    return -1

start = (-1,-1)
for i in range(row):
    for j in range(col):
        if inputboard[i][j] == '0':
            start = (i, j)
if start != (-1,-1):
    print(bfs_escape_maze(inputboard, start, row, col))
else:
    print(-1)