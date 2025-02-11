
from collections import defaultdict,deque
import sys
data = sys.stdin.readlines()
index = 0
case = 1
"""
Case 1: A forest of 3 trees.
Case 2: There is one tree.
Case 3: No trees
"""
while True:
    n, m = map(int, data[index].strip().split())
    if n == 0 and m == 0:
        break
    graph = defaultdict(list)
    for i in range(m):
        index += 1
        a, b = map(int, data[index].strip().split())
        graph[a].append(b)
        graph[b].append(a)

    q = deque([])
    visited = [-1] * (n+1)
    not_tree = []
    set_num = 0
    visited[0] = set_num
    for i in range(1, n+1):
        if visited[i] == -1:
            set_num += 1
            visited[i] = set_num
            q.append((i, -1))
        while q:
            node, parent = q.popleft()
            for ne in graph[node]:
                if visited[ne] == -1:
                    visited[ne] = set_num
                    q.append((ne, node))
                elif ne != parent:
                    not_tree.append(set_num)
    index += 1
    tree_count = len(set(visited[1:])-set(not_tree))
    if tree_count == 1:
        answer = "There is one tree."
    elif 1 < tree_count:
        answer = "A forest of "+str(tree_count)+" trees."
    else:
        answer = "No trees."
    print(f"Case {case}: {answer}")
    case += 1
