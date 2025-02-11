"""
첫째 줄에는 테스트케이스의 개수 T

첫째 줄에 건물의 개수 N과 건물간의 건설순서 규칙의 총 개수 K이 주어진다. (건물의 번호는 1번부터 N번까지 존재한다)
둘째 줄에는 각 건물당 건설에 걸리는 시간 D1, D2, ..., DN이 공백을 사이로 주어진다. 셋째 줄부터 K+2줄까지 건설순서 X Y가 주어진다.
(이는 건물 X를 지은 다음에 건물 Y를 짓는 것이 가능하다는 의미이다)
마지막 줄에는 백준이가 승리하기 위해 건설해야 할 건물의 번호 W가 주어진다.

2       T

4 4 첫째 줄에 건물의 개수 N , 건물간의 건설순서 규칙의 총 개수 K
10 1 100 10 둘째 줄에는 각 건물당 건설에 걸리는 시간 (N=4) D1, D2, D3, D4
1 2 건설순서 X Y
1 3 건설순서 X Y
2 4 건설순서 X Y
3 4 건설순서 X Y
4  승리하기 위해 건설해야 할 건물의 번호 W

8 8 첫째 줄에 건물의 개수 N, 건물간의 건설순서 규칙의 총 개수 K
10 20 1 5 8 7 1 43  둘째 줄에는 각 건물당 건설에 걸리는 시간 (N=8) D1, D2, D3, D4...D8
1 2 건설순서 X Y
1 3 건설순서 X Y
2 4 건설순서 X Y
2 5 건설순서 X Y
3 6 건설순서 X Y
5 7 건설순서 X Y
6 7 건설순서 X Y
7 8 건설순서 X Y
7 승리하기 위해 건설해야 할 건물의 번호 W

"""

# from collections import defaultdict,deque
# import heapq
# def min_target_build_time(nodelist, graph, target):
#     status = 0
#     time = 0
#     neednodelist = [target]
#
#     q = deque([graph[target]])
#     while q:
#         nlist = q.popleft()
#         neednodelist.extend(nlist)
#         for i in nlist:
#             q.append(graph[i])
#
#     inbuild = []
#     visited = set()
#     while neednodelist:
#
#         re = True
#         while re:
#             re = False
#             node = neednodelist.pop()
#             can = True
#             for i in graph[node]:
#                 if not bool(status & (1 << i-1)):
#                     can = False
#                     break
#             if can and node not in visited:
#                 if node != target:
#                     re = True
#                 visited.add(node)
#                 heapq.heappush(inbuild, (time+nodelist[node-1], node))
#             elif node in visited:
#                 re = True
#             else:
#                 re = False
#                 neednodelist.append(node)
#         a = heapq.heappop(inbuild)
#         status ^= (1 << (a[1]-1))
#         time = a[0]
#
#     return time
# # testcase = int(input())
# # for _ in range(testcase):
# #     n, k = map(int, input().split())
# #     buildtime = map(int, input().split())
# #     neednode = defaultdict(list)
# #     for _ in range(k):
# #         a,b = map(int, input().split())
# #         neednode[b].append(a)
# #     target = int(input())
# #     print(min_target_build_time(buildtime, neednode, target))
# e = [(1,2),(1,3),(2,4),(3,4)]#
# e2 = [(1,2),(1,3),(2,4),(2,5),(3,6),(5,7),(6,7),(7,8)]
# neednode = defaultdict(list)
# for a,b in e:
#     neednode[b].append(a)
# print(min_target_build_time([10,1, 100, 10], neednode, 4))
# neednode2 = defaultdict(list)
#
# for a,b in e2:
#     neednode2[b].append(a)
# print(min_target_build_time([10, 20, 1, 5, 8, 7, 1, 43], neednode2, 7))


# 상위 코드는 메모리 초과

from collections import defaultdict, deque
def acm_craft(n, build_times, rules, target):
    # 그래프 및 진입 차수 초기화
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    dp = [0] * (n + 1)

    # 그래프 구성
    for x, y in rules:
        graph[x].append(y)
        in_degree[y] += 1

    # 위상 정렬
    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
            dp[i] = build_times[i - 1]

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            dp[neighbor] = max(dp[neighbor], dp[node] + build_times[neighbor - 1])
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # 목표 건물의 건설 완료 시간 반환
    return dp[target]

# 테스트 케이스 입력 처리
t = int(input())  # 테스트 케이스 수
results = []

for _ in range(t):
    n, k = map(int, input().split())  # 건물 개수, 규칙 수
    build_times = list(map(int, input().split()))  # 각 건물의 건설 시간
    rules = [tuple(map(int, input().split())) for _ in range(k)]  # 건설 순서 규칙
    target = int(input())  # 목표 건물

    results.append(acm_craft(n, build_times, rules, target))

# 결과 출력
for result in results:
    print(result)