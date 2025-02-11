"""
문제 개요:
동일한 물건을 여러 번 선택할 수 있습니다.
예를 들어, 물건의 무게가 3이고 가치가 6이라면, 이 물건을 3번 선택하여 총 무게 9, 가치 18로 만들 수 있습니다.
해결 방법:
동적 계획법(DP)을 사용합니다.
dp[i]는 배낭 용량이 i일 때 얻을 수 있는 최대 가치를 나타냅니다.
점화식: 𝑑𝑝[𝑖]=max⁡(𝑑𝑝[𝑖],𝑑𝑝[𝑖−𝑤𝑒𝑖𝑔ℎ𝑡]+𝑣𝑎𝑙𝑢𝑒)
dp[i]=max(dp[i],dp[i−weight]+value)
물건들을 하나씩 반복하며 DP 배열을 갱신합니다.
시간 복잡도:
𝑂(𝑛×𝑊) O(n×W), 여기서 𝑛, n은 물건의 개수, 𝑊
W는 배낭의 최대 용량입니다.
"""

def unbounded_knapsack(items, max_weight):
    dp = [0] * (max_weight + 1)
    for value, weight in items:
        for i in range(weight, max_weight + 1):
            dp[i] = max(dp[i], dp[i - weight] + value)
        print(dp)
    return dp[max_weight]

# Example
items = [(10, 2), (15, 3), (40, 5)]  # (value, weight)
max_weight = 8
print(unbounded_knapsack(items, max_weight))  # Output: 50
