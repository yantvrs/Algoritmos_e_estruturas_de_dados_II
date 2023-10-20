import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import math

# Import data from the 'bottles' module
from configuringASetup.Setups import bottles

# Create an empty graph to represent the relationship between bottles and attributes
G2 = nx.Graph()

# Populate the graph with nodes and edges based on the 'bottles' data
for bottle, attributes in bottles.items():
    G2.add_node(bottle, bipartite=0)  # Assign bottles to bipartite set 0
    for attr, value in attributes.items():
        # If the attribute node does not exist, create it in bipartite set 1
        if not G2.has_node(attr):
            G2.add_node(attr, bipartite=1)
        # Add an edge with weight representing the strength of the relationship between bottle and attribute
        if G2.has_edge(bottle, attr):
            G2[bottle][attr]['weight'] += value
        else:
            G2.add_edge(bottle, attr, weight=value)

# Separate nodes into two sets: 'bottle_nodes' and 'attribute_nodes' based on their bipartite attribute
bottle_nodes = {n for n, d in G2.nodes(data=True) if d['bipartite'] == 0}
attribute_nodes = {n for n, d in G2.nodes(data=True) if d['bipartite'] == 1}

# Calculate positions for the nodes in a custom layout
max_nodes = max(len(bottle_nodes), len(attribute_nodes))
radius = 6
angle_step = (2 * math.pi) / max_nodes
current_angle = 0

# Create a dictionary 'pos' to store custom positions for the nodes
pos = {}

# Calculate the center of the ellipse
center_x = 0
center_y = 0

# Position the 'bottle_nodes' in an elliptical layout
for bottle in bottle_nodes:
    x = center_x + radius * math.cos(current_angle)
    y = center_y + radius * math.sin(current_angle)
    pos[bottle] = (x, y)
    current_angle += angle_step

# Adjust the starting angle to position 'attribute_nodes' closer to the 'bottle_nodes'
start_angle = math.pi / 4  # Start from 45 degrees
angle_step = (2 * math.pi) / len(attribute_nodes)

# Position the 'attribute_nodes' on an elliptical line closer to the 'bottle_nodes'
for attr in attribute_nodes:
    x = center_x + radius * 0.7 * math.cos(start_angle)  # Reduce the radius to bring them closer
    y = center_y + radius * 0.7 * math.sin(start_angle)
    pos[attr] = (x, y)
    start_angle += angle_step

# Create a copy of the graph 'G2' to add edge weights
edge_weights = {(u, v): data['weight'] for (u, v, data) in G2.edges(data=True)}
G3 = G2.copy()

# Create custom labels and handles for the legend
legend_labels = {
    'Bottles': mpatches.Patch(color='lightblue', label='Bottles'),
    'Attributes': mpatches.Patch(color='lightgreen', label='Attributes'),
}

# Create a figure for the graph visualization
plt.figure(figsize=(10, 10))
node_colors = ['lightblue' if node in bottle_nodes else 'lightgreen' for node in G3.nodes]

# Draw the graph with labels, node sizes, colors, and edge colors
nx.draw(G3, pos, with_labels=True, node_size=700, node_color=node_colors, font_size=10, edge_color='gray')

# Extract edge labels and display them on the graph
labels = nx.get_edge_attributes(G3, 'weight')
edge_labels = {k: v for k, v in labels.items()}
nx.draw_networkx_edge_labels(G3, pos, edge_labels=edge_labels)

# Add the legend to the graph with a title 'Node Types'
plt.legend(handles=legend_labels.values(), loc='best', title='Node Types')

# Set the title of the graph
plt.title("Bipartite Graph of Bottles and Attributes")

# Turn off the axes for a cleaner visualization
plt.axis('off')

# Display the graph
plt.show()
