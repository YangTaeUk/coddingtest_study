#num1, num2 = map(int, input().split())

num1 = 4
num2 = 5

dp = [[1] * (i + 1) for i in range(num1 + 1)]
dp[0][0] = 1
dp[1][0], dp[1][1] = 1, 1

for i in range(2, num1 + 1):
    for j in range(1, i):
        print(i,j)
        dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

for i in range(num1 + 1):
    print(dp[i])
#print(dp[num1][num2])