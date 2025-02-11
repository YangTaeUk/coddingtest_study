"""
첫 번째 줄에는 점의 개수를 나타내는 정수 3 ≤ n ≤ 500,000 과 진행된 차례의 수를 나타내는 정수 3 ≤ m ≤ 1,000,000
이어지는 m 개의 입력 줄에는 각각 i번째 차례에 해당 플레이어가 선택한 두 점의 번호
6 5
0 1
1 2
2 3
5 4
0 4

새로운 간선이 생길 때 마다 사이클 check
"""
import sys
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
            root_x += 1
    else:
        return True
    return False
data = sys.stdin.readlines()
node_c, edge_c = map(int, data[0].strip().split())
data_parent = [i for i in range(node_c)]
data_rank = [0] * node_c
answer = 0

for i in range(edge_c):
    a, b = map(int, data[i+1].strip().split())
    if union(data_parent, data_rank, a, b):
        answer = i+1
        break
print(answer)