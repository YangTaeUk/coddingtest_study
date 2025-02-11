def tsp_with_constraints(n, dist, constraints=None):
    """
    n: 정점의 개수
    dist: 거리 행렬 (n x n)
    constraints: 제약 조건, (i, j): i를 반드시 j 이전에 방문해야 한다
    """
    # 초기화: DP 배열, 무한대로 초기화
    INF = float('inf')
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0  # 시작 상태 (0번 정점에서 시작)

    # 모든 상태와 마지막 정점 탐색
    for mask in range(1 << n):
        for i in range(n):
            if not (mask & (1 << i)):  # i를 방문하지 않은 상태면 건너뜀
                continue

            for j in range(n):
                if mask & (1 << j):  # j가 이미 방문된 상태면 건너뜀
                    continue
                if dist[i][j] == 0 or dist[i][j] == INF:  # 경로가 존재하지 않는 경우 건너뜀
                    continue
                # 특정 조건 ex_) 방문 이전에 i를 반드시 방문 해야 한다.
                # if constraints:
                #     for c1,c2 in constraints:
                #         if j == c2 and (status & 1 << c1):
                #             break
                #         else:
                #             next_status = status | (1 << j)
                #             dp[next_status][j] = min(dp[next_status][j], dp[status][i] + dist[i][j])
                # else:
                next_mask = mask | (1 << j)
                dp[next_mask][j] = min(dp[next_mask][j], dp[mask][i] + dist[i][j])

    # 최소 비용 계산 (모든 정점 방문 후 시작점으로 돌아오기)
    final_mask = (1 << n) - 1  # 모든 정점을 방문한 상태
    result = INF
    for i in range(1, n):
        if dist[i][0] != 0:  # 시작점으로 돌아갈 수 있어야 함
            result = min(result, dp[final_mask][i] + dist[i][0])

    return result


# 입력 처리
n = int(input())  # 정점 수
dist = [list(map(int, input().split())) for _ in range(n)]

# 결과 출력
print(tsp_with_constraints(n, dist))
