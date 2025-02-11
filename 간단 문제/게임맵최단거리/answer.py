from collections import deque


def solution(maps):
    n = len(maps)  # 세로 길이
    m = len(maps[0])  # 가로 길이

    # 상, 하, 좌, 우 방향 설정
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 큐 초기화
    q = deque([(0, 0, 1)])  # (x좌표, y좌표, 현재까지의 거리)
    visit = set((0, 0))  # 시작점을 방문한 상태로 초기화
    while q:
        x, y, distance = q.popleft()  # 큐의 맨 앞 요소를 꺼내 x, y, distance에 할당
        if x == n - 1 and y == m - 1:
            # 목적지에 도달했으면 현재까지의 거리를 반환
            return distance

        for dx, dy in directions:  # 네 방향으로 이동
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and (nx, ny) not in visit:
                # 범위 내에 있고, 이동 가능하며, 방문하지 않은 경우에만 이동
                q.append((nx, ny, distance + 1))
                visit.add((nx, ny))

    return -1  # 목적지에 도달할 수 없는 경우 -1 반환


print(solution([
    [1,0,1,1,1],
    [1,0,1,0,1],
    [1,0,1,1,1],
    [1,1,1,0,1],
    [0,0,0,0,1]
])) #	11
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])) #	-1