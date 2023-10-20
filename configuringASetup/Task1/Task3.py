import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import math

from Setups import bottles

G2 = nx.Graph()

for bottle, attributes in bottles.items():
    G2.add_node(bottle, bipartite=0)
    for attr, value in attributes.items():
        if not G2.has_node(attr):
            G2.add_node(attr, bipartite=1)
        if G2.has_edge(bottle, attr):
            G2[bottle][attr]['weight'] += value
        else:
            G2.add_edge(bottle, attr, weight=value)

bottle_nodes = {n for n, d in G2.nodes(data=True) if d['bipartite'] == 0}
attribute_nodes = {n for n, d in G2.nodes(data=True) if d['bipartite'] == 1}

# Calcule o raio e o ângulo da elipse
max_nodes = max(len(bottle_nodes), len(attribute_nodes))
radius = 6
angle_step = (2 * math.pi) / max_nodes
current_angle = 0

# Crie um dicionário de posições personalizadas para os nós
pos = {}

# Calcule o centro da elipse
center_x = 0
center_y = 0

# Posicione os nós de garrafas
for bottle in bottle_nodes:
    x = center_x + radius * math.cos(current_angle)
    y = center_y + radius * math.sin(current_angle)
    pos[bottle] = (x, y)
    current_angle += angle_step

# Ajuste o ângulo de início para posicionar os atributos mais próximos
start_angle = math.pi / 4  # Comece a partir de 45 graus
angle_step = (2 * math.pi) / len(attribute_nodes)

# Posicione os nós de atributos na mesma linha elíptica mais próxima dos nós de garrafas
for attr in attribute_nodes:
    x = center_x + radius * 0.7 * math.cos(start_angle)  # Reduza o raio para aproximá-los
    y = center_y + radius * 0.7 * math.sin(start_angle)
    pos[attr] = (x, y)
    start_angle += angle_step

edge_weights = {(u, v): data['weight'] for (u, v, data) in G2.edges(data=True)}

G3 = G2.copy()

# Crie custom labels e handles para a legenda
legend_labels = {
    'Bottles': mpatches.Patch(color='lightblue', label='Bottles'),
    'Attributes': mpatches.Patch(color='lightgreen', label='Attributes'),
}

plt.figure(figsize=(10, 10))
node_colors = ['lightblue' if node in bottle_nodes else 'lightgreen' for node in G3.nodes]
nx.draw(G3, pos, with_labels=True, node_size=700, node_color=node_colors, font_size=10, edge_color='gray')
labels = nx.get_edge_attributes(G3, 'weight')
edge_labels = {k: v for k, v in labels.items()}
nx.draw_networkx_edge_labels(G3, pos, edge_labels=edge_labels)

# Adicione a legenda ao gráfico
plt.legend(handles=legend_labels.values(), loc='best', title='Node Types')

plt.title("Bipartite Graph of Bottles and Attributes")
plt.axis('off')  # Desligue os eixos
plt.show()
