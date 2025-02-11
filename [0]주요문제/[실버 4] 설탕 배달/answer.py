
target = int(input())

dp = [float('inf')]*(target+1)
dp[0] = 0
if target < 5:
    if target == 3 or target == 5:
        print(1)
    else:
        print(-1)
else:
    dp[3] = 1
    dp[5] = 1
    for i in range(6, target+1):
        dp[i] = min(dp[i-3]+1, dp[i-5]+1)

    print(dp[target] if dp[target] != float('inf') else -1)
