# 뿌엥틀림...

MOD = 998244353

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1
        return True
    return False

def kruskal_variation(n, edges):
    edges.sort(key=lambda x: x[2])  # 가중치 순으로 정렬
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    result = 1
    i = 0

    while i < len(edges):
        # 동일한 가중치를 가진 간선 그룹 찾기
        j = i
        while j < len(edges) and edges[j][2] == edges[i][2]:
            j += 1

        # 간선 그룹에서 유니온-파인드 실행
        group_edges = edges[i:j]
        group_count = len(group_edges)
        included_count = 0

        # MST에 포함된 간선 확인
        for u, v, w in group_edges:
            if find(parent, u) != find(parent, v):
                included_count += 1

        # 그룹의 가능한 순서 조합 계산
        group_combinations = pow(2, included_count, MOD)
        result = (result * group_combinations) % MOD

        # 그룹의 간선을 실제 MST에 추가
        for u, v, w in group_edges:
            union(parent, rank, u, v)

        i = j

    return result

# 입력 처리
n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

# 결과 계산 및 출력
print(kruskal_variation(n, edges))
