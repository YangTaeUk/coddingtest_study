def traveling_sales_man(n, costs):
    inf = float('inf')
    dp = [[inf] * n for _ in range(1 << n)]
    dp[1][0] = 0

    for mask in range(1 << n):
        for i in range(n):
            if not (mask & (1 << i)):
                continue
            for j in range(n):
                if (mask & (1 << j)) or costs[i][j] == 0 or costs[i][j] == inf:
                    continue
                next_mask = mask | (1 << j)
                dp[next_mask][j] = min(dp[next_mask][j], dp[mask][i] + costs[i][j])
    final_mask = (1 << n) - 1
    result = inf
    for k in range(1, n):
        if costs[k][0] != 0:
            result = min(result, dp[final_mask][k] + costs[k][0])
    return result

import sys
input_text = sys.stdin.read()
data = input_text.splitlines()
print(traveling_sales_man(int(data[0]), [list(map(int, d.strip().split())) for d in data[1:]]))