from typing import Dict, List


class Graph:
    def __init__(self):
        self.nodes: Dict[List[int]] = {}

    def add_edge(self, node, neighbor):
        if node not in self.nodes:
            self.nodes[node] = [neighbor]
        else:
            self.nodes[node].append(neighbor)

        if neighbor not in self.nodes:
            self.nodes[neighbor] = [node]
        else:
            self.nodes[neighbor].append(node)


def bfs(graph, start, goal=None):  # Breath-First Search
    visited = set()
    queue = [(start, [start])]

    while queue:
        (node, path) = queue.pop(0)

        if node not in visited:
            if node == goal:
                return path
            visited.add(node)

            for neighbor in graph.nodes[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return None  # Return None if goal is not found


def dfs(graph, start, goal=None, path=None, visited=None):  # Depth-First Search
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

    print("BFS starting from node A:")
    print(bfs(graph, "A", "I"))

    print("DFS starting from node A:")
    print(dfs(graph, "A", "I"))
