import sys
data = sys.stdin.readlines()

n = int(data[0].strip())
m = int(data[1].strip())
road = [list(map(int, d.strip().split())) for d in data[2:n+2]]
route = list(map(int, data[n+2].strip().split()))

parent = [i for i in range(n+1)]
rank = [0] * (n + 1)
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

for i in range(n):
    for j in range(n):
        if road[i][j] == 1:
            union(i+1, j+1)

start = parent[route[0]]
can = True
for r in route:
    if parent[r] != start:
        can = False
        break

print("YES" if can else "NO")