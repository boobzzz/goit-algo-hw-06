import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
stations = ['Station A', 'Station B', 'Station C', 'Station D', 'Station E']
G.add_nodes_from(stations)

edges = [
    ('Station A', 'Station B'),
    ('Station B', 'Station C'),
    ('Station C', 'Station D'),
    ('Station D', 'Station E'),
    ('Station A', 'Station C')
]
G.add_edges_from(edges)

# Візуалізація графа
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=3000, font_size=15)
plt.title("Transport Network Graph")
plt.show()

# Аналіз характеристик графа
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступінь вершин:")
for node, degree in degrees.items():
    print(f"{node}: {degree}")
