"""
문제 개요:
여러 개의 배낭이 존재하며, 각 배낭마다 용량이 다릅니다.
물건들을 배낭에 담아 가치를 최대화해야 합니다.
각 물건은 최대 1번만 선택할 수 있습니다.
해결 방법:
동적 계획법(DP)을 확장하여 각 배낭을 독립적으로 처리합니다.
dp[j][k]를 사용하여,𝑗j-번째 배낭에𝑘k 무게까지 담을 때의 최대 가치를 계산합니다.
점화식: dp[j][k]=max(dp[j][k],dp[j][k−weight]+value)
배낭 개수만큼 반복하며 각 배낭에 대해 DP 배열을 갱신합니다.
시간 복잡도:
𝑂(𝑚×𝑛×𝑊)O(m×n×W), 여기서 𝑚m은 배낭의 개수,𝑛n은 물건의 개수, 𝑊W는 각 배낭의 최대 용량입니다.
"""
def multiple_knapsack(items, knapsacks):
    # items: [(value, weight), ...]
    # knapsacks: [capacity1, capacity2, ...]
    dp = [[0] * (max(knapsacks) + 1) for _ in range(len(knapsacks))]

    for j, capacity in enumerate(knapsacks):
        for value, weight in items:
            for k in range(capacity, weight - 1, -1):
                dp[j][k] = max(dp[j][k], dp[j][k - weight] + value)

    return sum(dp[j][knapsacks[j]] for j in range(len(knapsacks)))

# Example
items = [(10, 2), (15, 3), (40, 5)]  # (value, weight)
knapsacks = [5, 8]  # 두 개의 배낭 용량
print(multiple_knapsack(items, knapsacks))  # Output: 65
