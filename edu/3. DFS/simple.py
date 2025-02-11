def solution(graph):
    visit = set([])

    def dfs (node):
        if node not in visit:
            visit.add(node)
            print(node, end=' ')
            for neighbor in graph[node]:
                dfs(neighbor)
    dfs(1)
# 그래프 정의 (인접 리스트)
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [],
    6: []
}

solution(graph)


