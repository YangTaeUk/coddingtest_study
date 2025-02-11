"""
Fractional Knapsack (분할 배낭 문제)
문제 개요:
물건을 쪼개서 배낭에 담을 수 있습니다.
물건의 일부만 선택할 수 있으므로, 가치를 최대화하려면 단위 무게당 가치가 높은 물건부터 선택합니다.
해결 방법:

**탐욕적 알고리즘(Greedy Algorithm)**을 사용합니다.
물건들을 단위 무게당 가치 (value/weight) 기준으로 내림차순 정렬합니다.
배낭이 가득 찰 때까지 가능한 물건을 담고, 남은 공간에는 물건을 쪼개서 담습니다.
"""
def fractional_knapsack(items, max_weight):
    # items: [(value, weight), ...]
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    total_value = 0
    for value, weight in items:
        if max_weight >= weight:
            total_value += value
            max_weight -= weight
        else:
            total_value += value * (max_weight / weight)
            break
    return total_value

# Example
items = [(60, 10), (100, 20), (120, 30)]  # (value, weight)
max_weight = 50
print(fractional_knapsack(items, max_weight))  # Output: 240.0