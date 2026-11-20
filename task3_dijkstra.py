weighted_graph = [
    [0, 4, 0, 2, 9, 0, 0, 0],
    [4, 0, 3, 0, 0, 0, 0, 0],
    [0, 3, 0, 8, 0, 0, 4, 0],
    [2, 0, 8, 0, 0, 6, 0, 0],
    [9, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 6, 1, 0, 0, 3],
    [0, 0, 4, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 3, 2, 0]
]


def dijkstra(graph, start, finish):
    if start == finish:
        return 0, [start]

    n = len(graph)
    dist = [float('inf')] * n
    parent = [-1] * n
    visited = [False] * n
    dist[start] = 0

    for _ in range(n):
        u = -1
        min_d = float('inf')
        for v in range(n):
            if not visited[v] and dist[v] < min_d:
                min_d = dist[v]
                u = v

        if u == -1 or u == finish:
            break

        visited[u] = True
        for v in range(n):
            weight = graph[u][v]
            if weight > 0 and not visited[v]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    parent[v] = u

    if dist[finish] == float('inf'):
        return None, []

    path = []
    curr = finish
    while curr != -1:
        path.append(curr)
        curr = parent[curr]
    path.reverse()

    return dist[finish], path


if __name__ == "__main__":
    for s, f in [(0, 7), (2, 4), (3, 3)]:
        distance, route = dijkstra(weighted_graph, s, f)
        if distance is None:
            print(f"Путь от {s} до {f} не существует.")
        else:
            print(f"Маршрут ({s} -> {f}): длина = {distance}, путь = {route}")