import sys
data = sys.stdin.readlines()
n = int(data[0].strip())
price = [list(map(int, d.strip().split())) for d in data[1:]]
inf = float('inf')

result = inf
for first_color in range(3):
    dp  = [[inf] * 3 for _ in range(n)]
    dp[0][first_color] = price[0][first_color]
    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1],dp[i-1][2])+price[i][0]
        dp[i][1] = min(dp[i-1][0],dp[i-1][2])+price[i][1]
        dp[i][2] = min(dp[i-1][1],dp[i-1][0])+price[i][2]
    for last_color in range(3):
        if first_color != last_color:
            result = min(result, dp[n-1][last_color])
print(result)