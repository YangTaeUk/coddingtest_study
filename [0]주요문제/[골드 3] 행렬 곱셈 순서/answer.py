import sys

def matrix_chain_multiplication(arr):
    n = len(arr)

    # DP 배열 초기화
    dp = [[0] * n for _ in range(n)]

    # 구간 길이를 2 이상으로 점차 증가시키며 DP 계산
    for length in range(2, n + 1):  # 구간 길이
        for start in range(n - length + 1):
            end = start + length - 1
            dp[start][end] = float('inf')
            for k in range(start, end):
                cost = dp[start][k] + dp[k + 1][end] + arr[start][0] * arr[k][1] * arr[end][1]
                dp[start][end] = min(dp[start][end], cost)

    return dp[0][n - 1]


# 입력 처리
input = sys.stdin.read
data = input().split()
n = int(data[0])
arr = [list(map(int, data[i * 2 + 1:i * 2 + 3])) for i in range(n)]

# 결과 출력
print(matrix_chain_multiplication(arr))