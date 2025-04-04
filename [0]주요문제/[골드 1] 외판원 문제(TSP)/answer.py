def tsp_with_constraints(n, dist, constraints=None):
    """
    제약 조건을 고려한 TSP (외판원 순회) 문제를 DP와 비트마스킹으로 해결하는 함수.

    매개변수:
      n: 정점의 개수
      dist: n x n 크기의 거리 행렬 (경로가 없으면 0 또는 INF)
      constraints: 제약 조건 리스트, 각 원소는 (i, j) 형태로,
                   "i번 정점은 j번 정점을 방문하기 전에 반드시 방문되어야 한다"를 의미.
                   제약 조건이 없으면 None을 전달.

    반환:
      모든 정점을 방문한 후 시작 정점으로 돌아오는 최소 비용을 반환합니다.
      조건을 만족하는 경로가 없으면 INF를 반환합니다.
    """
    INF = float('inf')
    # dp[mask][i]: mask(비트마스크)에 포함된 정점들을 방문했으며, 마지막 정점이 i일 때의 최소 비용.
    dp = [[INF] * n for _ in range(1 << n)]

    # 초기 상태: 시작 정점 0만 방문한 상태 (비트마스크 1<<0 == 1)
    dp[1][0] = 0

    # 모든 비트마스크(상태)를 순회
    for mask in range(1 << n):
        for i in range(n):
            # 만약 현재 mask에 i가 포함되지 않거나 dp[mask][i]가 INF라면 해당 상태는 무시합니다.
            if not (mask & (1 << i)) or dp[mask][i] == INF:
                continue

            # 다음에 방문할 정점 j를 고려합니다.
            for j in range(n):
                # 이미 j가 방문된 상태이면 건너뜁니다.
                if mask & (1 << j):
                    continue
                # i에서 j로 가는 경로가 없으면 건너뜁니다.
                if dist[i][j] == 0 or dist[i][j] == INF:
                    continue

                # 제약 조건 확인:
                # 만약 constraints가 주어졌다면, j가 어떤 (c1, c2) 조건에서 c2에 해당하는 경우,
                # 현재 상태(mask)에 c1이 포함되어 있어야 합니다.
                valid = True
                if constraints:
                    for c1, c2 in constraints:
                        # 만약 j가 c2라면, c1이 반드시 이미 방문되어 있어야 함.
                        if j == c2 and not (mask & (1 << c1)):
                            valid = False
                            break
                if not valid:
                    continue  # 제약 조건을 만족하지 않으므로 j는 건너뜁니다.

                # j를 방문하는 상태로 전이합니다.
                next_mask = mask | (1 << j)
                dp[next_mask][j] = min(dp[next_mask][j], dp[mask][i] + dist[i][j])

    # 모든 정점을 방문한 상태 (모든 비트가 1인 상태)
    final_mask = (1 << n) - 1
    result = INF
    # 모든 정점을 방문한 후, 마지막 정점 i에서 시작 정점 0으로 돌아오는 비용을 고려합니다.
    for i in range(n):
        if dist[i][0] and dp[final_mask][i] < INF:
            result = min(result, dp[final_mask][i] + dist[i][0])

    return result


# ------------------ 예제 입력 처리 ------------------

if __name__ == "__main__":
    # 정점의 개수 입력
    n = int(input("정점의 수를 입력하세요: "))
    # 거리 행렬 입력 (n x n)
    dist = [list(map(int, input("정점 간의 거리를 공백으로 구분하여 입력하세요: ").split()))
            for _ in range(n)]

    # 제약 조건 입력 처리 (없으면 'n'을 입력)
    constraints = None
    has_constraints = input("제약 조건이 있습니까? (y/n): ").strip().lower()
    if has_constraints == 'y':
        num_constraints = int(input("제약 조건의 개수를 입력하세요: "))
        constraints = []
        for _ in range(num_constraints):
            # 각 제약 조건은 "c1 c2" 형태로 입력, c1번 정점을 반드시 c2번 정점 이전에 방문해야 함.
            c1, c2 = map(int, input("제약 조건 (c1, c2)를 입력하세요: ").split())
            constraints.append((c1, c2))

    result = tsp_with_constraints(n, dist, constraints)
    if result == float('inf'):
        print("조건을 만족하는 경로가 존재하지 않습니다.")
    else:
        print("최소 비용:", result)
