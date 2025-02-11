def app_memory(n, m, memories, costs):
    max_cost = sum(costs)  # 종료 비용의 최대 합
    dp = [0] * (max_cost + 1)  # dp[c]: 비용 c로 확보 가능한 최대 메모리

    for i in range(n):
        for c in range(max_cost, costs[i] - 1, -1):
            dp[c] = max(dp[c], dp[c - costs[i]] + memories[i])

    # 최소 비용 찾기
    for c in range(max_cost + 1):
        if dp[c] >= m:
            return c
    return -1  # 조건을 만족하는 최소 비용이 없는 경우


n, m = map(int, input().strip().split())
memories = list(map(int, input().strip().split()))
costs = list(map(int, input().strip().split()))

print(app_memory(n, m, memories, costs))