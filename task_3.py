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


def dijkstra_path(graph, start, goal):
    return nx.dijkstra_path(graph, start, goal)


start = 'Station A'
goal = 'Station E'
dijkstra_result = dijkstra_path(G, start, goal)
print(f"Дейкстра шлях: {dijkstra_result}")
