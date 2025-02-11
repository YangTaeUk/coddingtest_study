from pprint import pprint

def solution(triangle):
    reversetri = triangle[::-1]

    for i in range(len(reversetri) -1):
        for j in range(len(reversetri[i]) -1):
            reversetri[i+1][j] += max(reversetri[i][j], reversetri[i][j+1])

    return reversetri[-1][0]

# 20 21 22 23 24
triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
pprint(solution(triangle))


# n = 1
# arr = [[7],[3, 8],[8, 1, 0],[2, 7, 4, 4],[4, 5, 2, 6, 5],[4, 5, 2, 6, 5, 9]]
# dp = [[0]*(i+1) for i in range(n)]
# if n == 1:
#     print(arr[0][0])
# else:
#     dp[0] = arr[0]
#     for i in range(n):
#         for j in range(i+1):
#             if j == 0:
#                 dp[i][j] = dp[i-1][0]+arr[i][0]
#             elif j == i:
#                 dp[i][j] = dp[i-1][j-1]+arr[i][j]
#             else:
#                 dp[i][j] = max(
#                     dp[i - 1][j - 1]+arr[i][j],
#                     dp[i - 1][j] + arr[i][j]
#                 )
#     for i in range(n):
#         print(dp[i])
#     print(max(dp[n-1]))

# n = 6
# arr = [[7],[3, 8],[8, 1, 0],[2, 7, 4, 4],[4, 5, 2, 6, 5],[4, 5, 2, 6, 5, 9]]
# reversetri = arr[::-1]
# print(reversetri)
# for i in range(len(reversetri) - 1):
#     for j in range(len(reversetri[i]) - 1):
#         reversetri[i + 1][j] += max(reversetri[i][j], reversetri[i][j + 1])
#
# print(reversetri)
# print(reversetri[-1][0])