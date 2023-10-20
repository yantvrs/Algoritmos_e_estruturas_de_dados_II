import matplotlib.pyplot as plt
import networkx as nx
import seaborn as sns
import itertools

from configuringASetup.Setups import CarSetups

# Task 1
def generate_all_setups(limiter):
    """
    Generate all possible car setups and calculate team scores.

    Parameters:
    - limiter (int): The score threshold to filter setups.

    Returns:
    - allSetups (list): A list of dictionaries containing setup information.
    - teamScores (list): A list of team scores that meet the limiter criteria.
    """
    setupId = 'Setup '
    idCount = 0
    allSetups = []
    teamScores = []

    options_lists = [
        CarSetups.breaksOptions,
        CarSetups.gearBoxesOptions,
        CarSetups.rearWingsOptions,
        CarSetups.frontWingsOptions,
        CarSetups.suspensionsOptions,
        CarSetups.enginesOptions
    ]

    for option_combination in itertools.product(*options_lists):
        breaks, gearBox, rearWing, frontWing, suspension, engine = option_combination
        setup = CarSetups(breaks, gearBox, rearWing, frontWing, suspension, engine)
        contributions = setup.sum_contributions()

        setup_data = {
            "id": setupId + str(idCount),
            "setup": setup,
            "contributions": contributions
        }
        allSetups.append(setup_data)

        idCount += 1

        teamScore = contributions["speed"] + contributions["cornering"] + contributions["powerUnit"] + contributions["reliability"] + contributions["averagePitStopTime"] / 0.02

        if teamScore >= limiter:
            teamScores.append(teamScore)

    return allSetups, teamScores

def plot_team_score_histogram(teamScores, limiter):
    """
    Plot a histogram of team scores.

    Parameters:
    - teamScores (list): A list of team scores.
    - limiter (int): The score threshold used for filtering setups.
    """
    plt.figure(figsize=(8, 6))
    plt.hist(teamScores, bins=30, color='darkblue', edgecolor='black')
    plt.xlabel("Team Score")
    plt.ylabel("Setups Number")
    plt.title(f"Histogram Team Score (Limit = {limiter})")
    plt.legend([f'Limit: {limiter}'])
    plt.show()

# Task 2
def create_and_visualize_graph(allSetups, limiter):
    """
    Create and visualize a directed graph of car setups and components.

    Parameters:
    - allSetups (list): A list of dictionaries containing setup information.
    - limiter (int): The score threshold used for filtering setups.
    """
    config_count = {}
    G = nx.DiGraph()

    for setup_data in allSetups:
        contributions = setup_data["contributions"]

        score = (contributions["speed"] +
                 contributions["cornering"] +
                 contributions["powerUnit"] +
                 contributions["reliability"] +
                 contributions["averagePitStopTime"] / 0.02)

        if score >= limiter:

            setupId = setup_data["id"]
            G.add_node(setupId, setup=setup_data["setup"], score=score)

            for component in ["breaks", "gearBox", "rearWing", "frontWing", "suspension", "engine"]:
                component_value = setup_data["setup"].__dict__[component]

                if component_value not in G:
                    G.add_node(component_value, score=0)
                    config_count[component_value] = 1

                else:
                    config_count[component_value] += 1
                G.add_edge(setupId, component_value)

    pos = nx.spring_layout(G, seed=42)

    sizes = [
        G.nodes[node]['score'] * 10 if 'score' in G.nodes[node] and G.nodes[node]['score'] else config_count[node] * 100 for
        node in G.nodes()]

    colors = ['red' if G.nodes[node].get('score', False) else 'black' for node in G.nodes()]

    plt.figure(figsize=(12, 12))
    nx.draw(G, pos, with_labels=True, node_size=sizes, node_color=colors, font_size=8, alpha=0.7)
    plt.title("Relationship between Configurations and Components")
    plt.legend([f'Limit: {limiter}'])
    plt.show()

    out_degrees = [deg for node, deg in G.out_degree() if 'score' in G.nodes[node]]

    plt.figure(figsize=(10, 6))
    sns.kdeplot(out_degrees, fill=True)
    plt.title('PDF of the Out Degree of the setups')
    plt.xlabel('Out Degree')
    plt.ylabel('Density')
    plt.legend([f'Limit: {limiter}'])
    plt.show()

if __name__ == "__main__":
    limiter = 850
    allSetups, teamScores = generate_all_setups(limiter)
    plot_team_score_histogram(teamScores, limiter)
    create_and_visualize_graph(allSetups, limiter)
