import sys
data = sys.stdin.readlines()

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, size, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        parent[root_y] = root_x
        size[root_x] += size[root_y]
        size[root_y] = size[root_x]

    return size[root_x]

T = int(data[0])
index = 1
results = []
for _ in range(T):
    f = int(data[index])
    index += 1

    parent = {}
    size = {}
    id_map = {}
    id_counter = 0
    for _ in range(f):
        a, b = data[index].split()
        index += 1

        # 문자열 아이디를 숫자 인덱스로 변환
        if a not in id_map:
            id_map[a] = id_counter
            parent[id_counter] = id_counter
            size[id_counter] = 1
            id_counter += 1

        if b not in id_map:
            id_map[b] = id_counter
            parent[id_counter] = id_counter
            size[id_counter] = 1
            id_counter += 1

        # 유니온 연산 후 네트워크 크기 출력
        result = union(parent, size, id_map[a], id_map[b])
        results.append(result)

sys.stdout.write("\n".join(map(str, results)) + "\n")