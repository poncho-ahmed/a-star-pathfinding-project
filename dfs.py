from bfs import Graph


def dfs(graph, start, goal=None, path=None, visited=None): # Depth-First Search
    if visited is None:
        visited = set()
    if path is None:
        path = [start]

    visited.add(start)

    if start == goal:
        return path

    for neighbor in graph.nodes[start]:
        if neighbor not in visited:
            # Recursive call to travel down depths
            new_path = dfs(graph, neighbor, goal, path=path + [neighbor], visited=visited)

            if new_path:
                return new_path
    return None


if __name__ == '__main__':
    graph = Graph()

    edges = [
        ('A', 'B'),
        ('A', 'C'),
        ('B', 'D'),
        ('B', 'E'),
        ('B', 'H'),
        ('C', 'F'),
        ('D', 'E'),
        ('E', 'F'),
        ('E', 'G'),
        ('G', 'I'),
        ('H', 'I')
    ]

    for edge in edges:
        graph.add_edge(*edge)

    print("DFS starting from node A:")
    print(dfs(graph, "A", "I"))