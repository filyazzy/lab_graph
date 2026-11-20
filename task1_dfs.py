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


def dfs(graph, start):
    visited = [False] * len(graph)
    order = []

    def _dfs(v):
        visited[v] = True
        order.append(v)
        for neighbor in range(len(graph)):
            if graph[v][neighbor] == 1 and not visited[neighbor]:
                _dfs(neighbor)

    _dfs(start)
    return order


if __name__ == "__main__":
    print("DFS от вершины 0:", dfs(graph, 0))
    print("DFS от вершины 4:", dfs(graph, 4))