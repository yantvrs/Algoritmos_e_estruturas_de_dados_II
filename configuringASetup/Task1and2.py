import matplotlib.pyplot as plt
import networkx as nx
import seaborn as sns

from configuringASetup.Setups import CarSetups


# Task 1
all_setups = []
team_scores = []
cutoff = 880
setup_id = 'Setup '
id_count = 0
for breaks in CarSetups.breaksOptions:
    for gearBox in CarSetups.gearBoxesOptions:
        for rearWing in CarSetups.rearWingsOptions:
            for frontWing in CarSetups.frontWingsOptions:
                for suspension in CarSetups.suspensionsOptions:
                    for engine in CarSetups.enginesOptions:
                        setup = CarSetups(breaks, gearBox, rearWing, frontWing, suspension, engine)
                        contributions = setup.sum_contributions()

                        setup_data = {
                            "id": setup_id + str(id_count),
                            "setup": setup,
                            "contributions": contributions
                        }
                        all_setups.append(setup_data)
                        id_count += 1

                        team_score = contributions["speed"] + contributions["cornering"] + contributions["powerUnit"] + contributions["reliability"] + contributions["averagePitStopTime"] / 0.02

                        if team_score >= cutoff:
                            team_scores.append(team_score)

plt.figure(figsize=(8, 6))
plt.hist(team_scores, bins=50, color='blue', edgecolor='black')
plt.xlabel("Team Score")
plt.ylabel("Número de Configurações")
plt.title(f"Histograma do Team Score (Limite = {cutoff})")
plt.show()  # Mostra o histograma




# Task 2
G1 = nx.DiGraph()
config_count = {}
for setup_data in all_setups:
    contributions = setup_data["contributions"]
    score = (contributions["speed"] +
             contributions["cornering"] +
             contributions["powerUnit"] +
             contributions["reliability"] +
             contributions["averagePitStopTime"] / 0.02)
    if score >= cutoff:
        setup_id = setup_data["id"]
        G1.add_node(setup_id, setup=setup_data["setup"], score=score)
        for component in ["breaks", "gearBox", "rearWing", "frontWing", "suspension", "engine"]:
            component_value = setup_data["setup"].__dict__[component]
            if component_value not in G1:
                G1.add_node(component_value, score=0)
                config_count[component_value] = 1
            else:
                config_count[component_value] += 1
            G1.add_edge(setup_id, component_value)

sizes = [
    G1.nodes[node]['score'] * 10 if 'score' in G1.nodes[node] and G1.nodes[node]['score'] else config_count[node] * 100 for
    node in G1.nodes()]

colors = ['red' if 'score' in G1.nodes[node] and G1.nodes[node]['score'] else 'black' for node in G1.nodes()]


plt.figure(figsize=(15, 15))
pos = nx.kamada_kawai_layout(G1, scale=2.0)
nx.draw(G1, pos, with_labels=True, node_size=sizes, node_color=colors, font_size=8, alpha=0.7)
plt.title("Relação entre Configurações e Componentes")
plt.show()

out_degrees = [deg for node, deg in G1.out_degree() if 'score' in G1.nodes[node]]


plt.figure(figsize=(10, 6))
sns.kdeplot(out_degrees, fill=True)
plt.title('PDF do "Out Degree" dos setups')
plt.xlabel('Out Degree')
plt.ylabel('Densidade')
plt.show()


