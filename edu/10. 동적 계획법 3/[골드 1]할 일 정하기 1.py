import sys

input = sys.stdin.readline

def assign_jobs(n, D):
    dp = [float('inf')]*(1 << n)
    dp[0] = 0
    for mask in range(1 << n):
        i = bin(mask).count("1")
        if i >= n:
            continue
        for j in range(n):
            if not (mask & (1 << j)):  # j번째 작업이 아직 선택되지 않은 경우
                next_mask = mask | (1 << j)
                dp[next_mask] = min(dp[next_mask],dp[mask]+D[i][j])

    return dp[(1 << n) - 1]

n = int(input())
D = [list(map(int, input().strip().split())) for _ in range(n)]
print(assign_jobs(n, D))