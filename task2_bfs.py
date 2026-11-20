from collections import deque

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


def bfs(graph, start):
    visited = [False] * len(graph)
    queue = deque([start])
    visited[start] = True
    order = []

    while queue:
        v = queue.popleft()
        order.append(v)
        for neighbor in range(len(graph)):
            if graph[v][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return order


if __name__ == "__main__":
    print("BFS от вершины 0:", bfs(graph, 0))
    print("BFS от вершины 4:", bfs(graph, 4))