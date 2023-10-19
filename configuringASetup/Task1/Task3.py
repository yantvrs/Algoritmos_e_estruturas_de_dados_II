import networkx as nx
import matplotlib.pyplot as plt

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

pos = {}
pos.update((node, (1, index)) for index, node in enumerate(bottle_nodes))
pos.update((node, (2, index)) for index, node in enumerate(attribute_nodes))

edge_weights = {(u, v): data['weight'] for (u, v, data) in G2.edges(data=True)}

G3 = G2.copy()

import matplotlib.patches as mpatches

# Create custom labels and handles for the legend
legend_labels = {
    'Bottles': mpatches.Patch(color='darkblue', label='Bottles'),
    'Attributes': mpatches.Patch(color='green', label='Attributes'),
}

plt.figure(figsize=(15, 15))
node_colors = ['darkblue' if node in bottle_nodes else 'green' for node in G3.nodes]
nx.draw(G3, pos, with_labels=True, node_size=700, node_color=node_colors, font_size=10, edge_color='gray')
labels = nx.get_edge_attributes(G3, 'weight')
edge_labels = {k: v for k, v in labels.items()}
nx.draw_networkx_edge_labels(G3, pos, edge_labels=edge_labels)

# Add the legend to the plot
plt.legend(handles=legend_labels.values(), loc='best', title='Node Types')

plt.title("Bipartite Graph of Bottles and Attributes")
plt.show()
