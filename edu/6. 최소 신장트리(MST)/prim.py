import heapq

def prim(graph, start=0):
    n = len(graph)
    visited = [False] * n
    pq = [(0, start)]
    mst_cost = 0
    mst_edges = []
    while pq:
        weight, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        mst_cost += weight
        mst_edges.append(u)

        for v, w in graph[u]:
            if not visited:
                heapq.heappush(pq, (w, v))

    return mst_cost, mst_edges

