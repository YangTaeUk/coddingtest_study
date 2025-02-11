import sys
data = sys.stdin.readlines()
n, m = map(int, data[0].strip().split())

parent = [i for i in range(n+1)]
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:  # 루트가 다르면 병합
        parent[root_y] = root_x

for d in data[1:]:
    order, a, b = map(int, d.strip().split())
    if order == 0:
        union(a, b)
    elif order == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")