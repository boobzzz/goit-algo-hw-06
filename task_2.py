import networkx as nx

G = nx.Graph()
stations = ['Station A', 'Station B', 'Station C', 'Station D', 'Station E']
G.add_nodes_from(stations)

edges = [
    ('Station A', 'Station B', 1.5),
    ('Station B', 'Station C', 2.1),
    ('Station C', 'Station D', 1.7),
    ('Station D', 'Station E', 2.2),
    ('Station A', 'Station C', 2.5)
]
G.add_weighted_edges_from(edges)


def dfs_path(graph, start, goal):
    visited = set()
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)
            for neighbor in set(graph.neighbors(vertex)) - visited:
                stack.append((neighbor, path + [neighbor]))
    return None


def bfs_path(graph, start, goal):
    visited = set()
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)
            for neighbor in set(graph.neighbors(vertex)) - visited:
                queue.append((neighbor, path + [neighbor]))
    return None


# Порівняння DFS та BFS
start = 'Station A'
goal = 'Station E'
dfs_result = dfs_path(G, start, goal)
bfs_result = bfs_path(G, start, goal)

print(f"DFS шлях: {dfs_result}")
print(f"BFS шлях: {bfs_result}")