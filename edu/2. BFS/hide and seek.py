from collections import deque
# BFS 사용한 풀이
def hide_and_seek_bfs(n, k):
    max_pos = 100000
    visited = [-1] * (max_pos + 1)  # 방문 여부 및 거리 저장
    queue = deque([n])
    visited[n] = 0  # 시작점

    while queue:
        current = queue.popleft()

        # 목표에 도달
        if current == k:
            return visited[current]

        # 이동 가능한 위치 탐색
        for next_pos in (current - 1, current + 1, current * 2):
            if 0 <= next_pos <= max_pos and visited[next_pos] == -1:
                visited[next_pos] = visited[current] + 1
                queue.append(next_pos)

# 그리디 접근을 사용한 풀이
def solution(n, k):
    time = 0

    while k != n:
        # 목표 지점이 현재보다 큰 경우
        if k > n:
            # 순간이동 가능하고, k가 짝수라면 순간이동
            if k % 2 == 0:
                k //= 2
            else:  # 그렇지 않다면 뒤로 이동
                k += 1
        else:
            # 현재 위치가 목표보다 작은 경우 한 칸씩 이동
            time += n - k
            return time

        time += 1

    return time

# 테스트
N = 5
K = 17
print(solution(N, K))  # 출력: 4