import networkx as nx
import seaborn as sns
import matplotlib.pyplot as plt

from configuringASetup.Setups import CarSetup
from Setups import Driversbottles
from Setups import CarSetup
from Setups import drivers

"""Task 1"""
# Define a function to calculate team score
def calculate_team_score(contributions):
    score = contributions["speed"] + contributions["cornering"] + contributions["power_unit"] + contributions["reliability"] + (contributions["avg_pit_stop_time"] / 0.02)
    return score

# Define a function to generate setups
def generate_setups():
    all_setups = []
    setup_id = 'Setup '
    id_count = 0

    for brakes in CarSetup.brakes:
        for gearbox in CarSetup.gearboxes:
            for rear_wing in CarSetup.rear_wings:
                for front_wing in CarSetup.front_wings:
                    for suspension in CarSetup.suspensions:
                        for engine in CarSetup.engines:
                            setup = CarSetup(brakes, gearbox, rear_wing, front_wing, suspension, engine)
                            contributions = setup.sum_contributions()

                            setup_data = {
                                "id": setup_id + str(id_count),
                                "setup": setup,
                                "contributions": contributions
                            }
                            all_setups.append(setup_data)
                            id_count += 1

    return all_setups

# Define a function to plot the histogram
def plot_histogram(team_scores, cutoff):
    plt.figure(figsize=(7, 7))
    plt.hist(team_scores, bins=80,color='blue', edgecolor='black')
    plt.xlabel("Team Score")
    plt.ylabel("Number of Configurations")
    plt.title(f"Team Score Histogram (Cutoff = {cutoff})")
    plt.grid(axis='y', linestyle='--')
    plt.show()

# Main part of the code
if __name__ == "__main__":
    all_setups = generate_setups()
    cutoff = 0
    team_scores = []

    for setup_data in all_setups:
        team_score = calculate_team_score(setup_data["contributions"])
        if team_score >= cutoff:
            team_scores.append(team_score)

    plot_histogram(team_scores, cutoff)

"""Task 2"""

# Create a directed graph based on Team Score
def create_directed_graph(all_setups, cutoff):
    G1 = nx.DiGraph()
    config_count = {}

    for setup_data in all_setups:
        contributions = setup_data["contributions"]
        score = (
            contributions["speed"]
            + contributions["cornering"]
            + contributions["power_unit"]
            + contributions["reliability"]
            + (contributions["avg_pit_stop_time"] / 0.02)
        )
        if score >= cutoff:
            setup_id = setup_data["id"]
            G1.add_node(setup_id, setup=setup_data["setup"], score=score)

            for component in ["brakes", "engine", "suspension", "front_wing", "rear_wing", "gearbox"]:
                component_value = setup_data["setup"].__dict__[component]
                if component_value not in G1:
                    G1.add_node(component_value, score=0)
                    config_count[component_value] = 1
                else:
                    config_count[component_value] += 1
                G1.add_edge(setup_id, component_value)

    sizes = [
        G1.nodes[node]['score'] * 10 if 'score' in G1.nodes[node] and G1.nodes[node]['score'] else config_count[node] * 100
        for node in G1.nodes()
    ]

    colors = ['red' if 'score' in G1.nodes[node] and G1.nodes[node]['score'] else 'black' for node in G1.nodes()]

    return G1, sizes, colors

# Plot the directed graph
def plot_directed_graph(G1):
    plt.figure(figsize=(15, 15))
    pos = nx.kamada_kawai_layout(G1)
    nx.draw(G1, pos, with_labels=True, node_size=sizes, node_color=colors, font_size=8, alpha=0.7)
    plt.title("Relação entre Configurações e Componentes")
    plt.show()

# Create and plot the Probability Density Function (PDF)
def create_and_plot_pdf(out_degrees):
    plt.figure(figsize=(10, 6))
    sns.kdeplot(out_degrees, fill=True)
    plt.title('PDF do "Out Degree" dos setups')
    plt.xlabel('Out Degree')
    plt.ylabel('Densidade')
    plt.show()

# Main part of the code
G1, sizes, colors = create_directed_graph(all_setups, cutoff)
plot_directed_graph(G1)

out_degrees = [deg for node, deg in G1.out_degree() if 'score' in G1.nodes[node]]
create_and_plot_pdf(out_degrees)

""""Task 3"""


# Create a bipartite graph from Driversbottles
def create_bipartite_graph(Driversbottles):
    G2 = nx.Graph()

    for bottle, attributes in Driversbottles.items():
        G2.add_node(bottle, bipartite=0)
        for attr, value in attributes.items():
            if not G2.has_node(attr):
                G2.add_node(attr, bipartite=1)
            G2.add_edge(bottle, attr, weight=value)

    return G2


# Separate nodes into two groups: bottles and attributes
def separate_nodes(G2):
    bottle_nodes = [n for n, d in G2.nodes(data=True) if d['bipartite'] == 0]
    attribute_nodes = [n for n, d in G2.nodes(data=True) if d['bipartite'] == 1]
    return bottle_nodes, attribute_nodes


# Define positions for nodes
def define_node_positions(bottle_nodes, attribute_nodes):
    pos = dict()
    pos.update((node, (1, index)) for index, node in enumerate(bottle_nodes))
    pos.update((node, (2, index)) for index, node in enumerate(attribute_nodes))
    return pos


# Consolidate and calculate edge weights
def consolidate_edge_weights(G2):
    edge_weights = {}
    for (u, v, data) in G2.edges(data=True):
        edge = (u, v) if u < v else (v, u)  # Ensure consistent edge order
        if edge not in edge_weights:
            edge_weights[edge] = data['weight']
        else:
            edge_weights[edge] += data['weight']
    return edge_weights


# Create a new graph with consolidated edges
def create_new_graph_with_consolidated_edges(G2, edge_weights):
    G3 = nx.Graph()
    G3.add_nodes_from(G2.nodes(data=True))
    for (u, v), weight in edge_weights.items():
        G3.add_edge(u, v, weight=weight)
    return G3


# Plot the bipartite graph
def plot_bipartite_graph(G3, pos):
    plt.figure(figsize=(15, 15))
    nx.draw(G3, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10)
    labels = nx.get_edge_attributes(G3, 'weight')
    nx.draw_networkx_edge_labels(G3, pos, edge_labels=labels)
    plt.title("Grafo Bipartido das Garrafinhas e Propriedades")
    plt.show()


# Main function to execute the entire process
def main(Driversbottles):
    G2 = create_bipartite_graph(Driversbottles)
    bottle_nodes, attribute_nodes = separate_nodes(G2)
    pos = define_node_positions(bottle_nodes, attribute_nodes)
    edge_weights = consolidate_edge_weights(G2)
    G3 = create_new_graph_with_consolidated_edges(G2, edge_weights)
    plot_bipartite_graph(G3, pos)


# Call the main function with the Driversbottles data
main(Driversbottles)