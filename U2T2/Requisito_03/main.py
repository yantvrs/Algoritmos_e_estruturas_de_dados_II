import networkx as nx

def calculate_network_metrics(file_paths):
    for file_path in file_paths:
        G = nx.read_adjlist(file_path)
        print("Network data for {}: ".format(file_path))
        print("{} nodes and {} edges".format(G.number_of_nodes(), G.number_of_edges()))
        print("Degree Assortativity Coefficient: {}".format(nx.degree_assortativity_coefficient(G)))
        print("Number of connected components: {}".format(nx.number_connected_components(G)))
        largest_component = max(nx.connected_components(G), key=len)
        print("Size of largest connected component: {}".format(len(largest_component)))
        print("Average clustering coefficient: {}\n".format(nx.average_clustering(G)))

# List of file paths for the 5 input files
file_paths = ["../Amazon0601.txt","../p2p-Gnutella04.txt","../soc-sign-Slashdot081106.txt","../CollegeMsg.txt","../email-Eu-core.txt"]

# Call the function to calculate metrics for each file
calculate_network_metrics(file_paths)
