def solution(graph):
    visited= set()
    components = []

    def dfs(node, component):
        visited.add(node)
        component.append(node)
        for n in graph[node]:
            if n not in visited:
                dfs(n, component)
    for node in graph:
        if node not in visited:
            component = []
            dfs(node, component)
            components.append(component)

    print(components)

graph = {
    1: [2],
    2: [1, 3],
    3: [2],
    4: [5],
    5: [4]
}

solution(graph)