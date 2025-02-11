from collections import defaultdict
def solution(linklist):
    net = defaultdict(list)
    for l in linklist:
        net[l[1]].append(l[0])
        net[l[0]].append(l[1])

    def dfs_stack(start):
        stack = [start]
        visited = set()
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                print(node, end = " ")

                for n in reversed(net[node]):
                    stack.append(n)

    dfs_stack(1)
linklist = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]
solution(linklist)