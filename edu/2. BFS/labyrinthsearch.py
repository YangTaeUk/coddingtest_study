from collections import deque

def solution(maze):

    m = len(maze)
    n = len(maze[0])
    q = deque([(0, 0, 1)])
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    visit = {(0, 0)}  # visit = {0, 0}는 잘못된 초기화 주의 바람
    while q:
        x, y, distance = q.popleft()

        if (x ,y) == (n-1, m-1):
            return distance

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 이동 가능 여부 확인
            if (0 <= ny < m and 0 <= nx < n and maze[ny][nx] == 1
                # 0 <= by < m이 0 <= nx < n 보다 먼저 체크.
                # ax, by는 직관적이지 않으므로 nx, ny(next x, next y)로 변경.
                    and (nx, ny) not in visit):
                visit.add((nx, ny))
                q.append((nx, ny, distance + 1))

    return -1  # 도달할 수 없는 경우 반드시!! 명시

maze = [
    [1, 1, 0, 1],
    [0, 1, 0, 1],
    [0, 1, 1, 1],
    [1, 0, 0, 1]
]
print(solution(maze))