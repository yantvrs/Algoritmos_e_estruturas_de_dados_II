import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns

# Carregando o grafo a partir de um arquivo de adjacência
G = nx.read_adjlist("../../soc-sign-Slashdot081106.txt")

# average degree of neighbors
degree, avg_neigh_degree = zip(*nx.average_degree_connectivity(G).items())

# convert to list
degree = list(degree)
avg_neigh_degree = list(avg_neigh_degree)

plt.style.use("fivethirtyeight")
fig, ax = plt.subplots(1,1,figsize=(12,8))

sns.regplot(x=degree,y=avg_neigh_degree,ax=ax)

ax.set_xlabel("Node Degree")
ax.set_ylabel("Average neigbhor degree")
ax.set_xlim(0, None)

# Setting a title
ax.set_title("Degree Assortativity in Network 3 ")

# Save figure
plt.savefig("./imagens/degree_assortativity_rede_03.png",
            format="png",
            dpi=400,
            bbox_inches="tight",
            transparent=True)

plt.show()
