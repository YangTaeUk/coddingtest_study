import heapq
def dijkstra(start, graph, n):
    distances = [float('inf') * (n+1)]
    distances[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        current_distance, current_node = heapq.heappop(q)
        if current_distance > distances[current_node]:
            continue
        for adjacent, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[adjacent] :
                distances[adjacent] = distance
            heapq.heappush(q, (distance, adjacent))

    return distances