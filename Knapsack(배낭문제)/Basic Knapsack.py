"""
배낭 문제(Knapsack Problem)**를 해결하기 위한 동적 계획법(Dynamic Programming) 접근 방식
각각의 아이템을 배낭에 담을 때, 주어진 최대 무게를 초과하지 않으면서 얻을 수 있는 최대 가치를 산정.

0-1 배낭 문제는 제한된 무게(배낭의 용량)를 초과하지 않으면서 물건을 배낭에 담아 얻을 수 있는 최대 가치를 계산하는 문제입니다.
각각의 아이템은 "담는다(1)" 또는 "담지 않는다(0)"라는 두 가지 선택만 가능합니다.

배낭 용량의 감소 방향: 거꾸로 순회하는 이유는 이미 계산된 값을 덮어쓰지 않기 위해서입니다.
최대값 계산:
dp[i]: 현재 용량 i에서 아이템을 담지 않았을 때의 가치.
dp[i - weight] + dopa: 현재 아이템을 담았을 때의 가치.
이 둘 중 큰 값을 선택하여 dp[i]를 업데이트합니다.
"""

cnt, max_weight = map(int, input().strip().split())
dp = [0]*(max_weight+1)

for _ in range(cnt):
    weight, dopa = map(int, input().strip().split())
    for i in range(max_weight, weight-1, -1):
        dp[i] = max(dp[i], dp[i-weight]+dopa)
print(dp[max_weight])