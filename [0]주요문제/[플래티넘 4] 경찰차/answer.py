"""

시작시 항상 경찰차1은 (1, 1)의 위치에 있고 경찰차2는 (N, N)의 위치

처리해야 할 사건들이 순서대로 주어질 때, 두 대의 경찰차가 이동하는 거리의 합을 최소화 하도록 사건들을 맡기는 프로그램

첫째 줄에는 동서방향 도로의 개수를 나타내는 정수 N(5 ≤ N ≤ 1,000)이 주어진다.
둘째 줄에는 처리해야 하는 사건의 개수를 나타내는 정수 W(1 ≤ W ≤ 1,000)가 주어진다.

셋째 줄부터 (W+2)번째 줄까지 사건이 발생된 위치가 한 줄에 하나씩 주어진다.

경찰차들은 이 사건들을 주어진 순서대로 처리해야 한다.
각 위치는 동서방향 도로 번호를 나타내는 정수와 남북방향 도로 번호를 나타내는 정수로 주어지며 두 정수 사이에는 빈칸이 하나 있다.
두 사건이 발생한 위치가 같을 수 있다.


첫째 줄에 두 경찰차가 이동한 총 거리를 출력
둘째 줄부터 시작하여 (i+1)번째 줄에 i(1 ≤ i ≤ W)번째 사건이 맡겨진 경찰차 번호 (1, 2) 출력
"""
import sys
sys.setrecursionlimit(10**6)
data = sys.stdin.readlines()
N = int(data[0].strip())
W = int(data[1].strip())
events = [(1, 1), (N, N)] + [list(map(int, d.split())) for d in data[2:]]
dp = [[-1] * (W+2) for _ in range(W+2)]
dp_trace = [[-1] * (W+2) for _ in range(W+2)]

def manhattan_dist(start, end):
    return abs(events[start][0]-events[end][0])+abs(events[start][1]-events[end][1])

def solve(police1, police2):
    next_event = max(police1, police2) + 1
    if next_event == W+2:
        return 0
    if dp[police1][police2] != -1:
        return dp[police1][police2]

    dist1 = solve(next_event, police2) + manhattan_dist(police1, next_event)
    dist2 = solve(police1, next_event) + manhattan_dist(police2, next_event)
    if dist1 < dist2:
        dp_trace[police1][police2] = 1
        dp[police1][police2] = dist1
    else:
        dp_trace[police1][police2] = 2
        dp[police1][police2] = dist2

    return dp[police1][police2]

print(solve(0, 1))
m, n = 0, 1
for i in range(2, W + 2):
    print(dp_trace[m][n])
    if dp_trace[m][n] == 1:
        m = i
    else:
        n = i