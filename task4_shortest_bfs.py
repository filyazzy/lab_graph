from collections import deque
from task3_dijkstra import dijkstra

graph = [
    [0, 1, 0, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0]
]


def shortest_path_bfs(graph, start, finish):
    if start == finish:
        return 0, [start]

    n = len(graph)
    visited = [False] * n
    parent = [-1] * n
    queue = deque([start])
    visited[start] = True

    while queue:
        u = queue.popleft()
        if u == finish:
            break
        for v in range(n):
            if graph[u][v] == 1 and not visited[v]:
                visited[v] = True
                parent[v] = u
                queue.append(v)

    if not visited[finish]:
        return None, []

    path = []
    curr = finish
    while curr != -1:
        path.append(curr)
        curr = parent[curr]
    path.reverse()

    return len(path) - 1, path


if __name__ == "__main__":
    pairs = [(0, 7), (1, 5), (2, 4)]
    for s, f in pairs:
        edges_cnt, bfs_path = shortest_path_bfs(graph, s, f)
        dijk_dist, dijk_path = dijkstra(graph, s, f)
        print(f"Пара ({s}, {f}):")
        print(f"  BFS:      рёбер = {edges_cnt}, маршрут = {bfs_path}")
        print(f"  Дейкстра: расст = {dijk_dist}, маршрут = {dijk_path}\n")