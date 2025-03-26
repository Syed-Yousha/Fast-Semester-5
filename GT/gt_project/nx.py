import networkx as nx
import matplotlib.pyplot as plt

# ----------------------------------------------
# Function Definitions
# ----------------------------------------------

def print_welcome_message():
    """Prints the welcome message and program instructions."""
    print("=" * 50)
    print("Welcome to the Social Media Influencer Detection Tool!")
    print("This tool helps identify key influencers in a social network.")
    print("=" * 50)

def display_help_menu():
    """Displays a help menu with program instructions."""
    print("\n--- Help Menu ---")
    print("1. Enter graph connections in the format 'A->B'.")
    print("2. Type 'done' to finish entering connections.")
    print("3. Enter ground-truth influencers as a comma-separated list.")
    print("4. Visualizations and reports will be generated automatically.")
    print("5. Outputs include evaluation metrics and saved graph images.")
    print("=" * 50)

def create_graph():
    """Creates a directed graph from user input."""
    print("\nEnter social media connections (e.g., 'A->B'). Type 'done' when finished.")
    G = nx.DiGraph()
    while True:
        connection = input("Enter connection: ").strip()
        if connection.lower() == 'done':
            break
        if "->" not in connection:
            print("Invalid format. Please use 'A->B'.")
            continue
        source, target = connection.split("->")
        G.add_edge(source.strip(), target.strip())
    return G

def display_graph_info(G):
    """Displays basic information about the graph."""
    print("\n--- Graph Information ---")
    print(f"Nodes: {list(G.nodes())}")
    print(f"Edges: {list(G.edges())}")
    print(f"Number of Nodes: {G.number_of_nodes()}")
    print(f"Number of Edges: {G.number_of_edges()}")
    print("=" * 50)

def calculate_centralities(G):
    """Calculates in-degree and out-degree centralities for the graph."""
    print("\nCalculating centralities...")
    in_deg_centrality = nx.in_degree_centrality(G)
    out_deg_centrality = nx.out_degree_centrality(G)
    print("Centralities calculated.")
    return in_deg_centrality, out_deg_centrality

def find_top_influencers(centrality):
    """Finds the nodes with the highest centrality scores."""
    max_centrality = max(centrality.values())
    influencers = [node for node, score in centrality.items() if score == max_centrality]
    return influencers

def visualize_graph(G, centrality, title, filename=None):
    """Visualizes the graph with node sizes proportional to centrality scores."""
    pos = nx.spring_layout(G)
    node_sizes = [5000 * centrality[node] for node in G.nodes()]
    nx.draw(
        G, pos, with_labels=True, node_color='skyblue', node_size=node_sizes, edge_color='gray'
    )
    plt.title(title)
    if filename:
        plt.savefig(filename, format='png', dpi=300)
        print(f"Graph saved as {filename}")
    plt.show()

def save_scores(filename, in_deg, out_deg):
    """Saves centrality scores to a file."""
    with open(filename, "w") as file:
        file.write("Node\tIn-Degree Centrality\tOut-Degree Centrality\n")
        for node in in_deg:
            file.write(f"{node}\t{in_deg[node]:.4f}\t{out_deg[node]:.4f}\n")
    print(f"Centrality scores saved to {filename}")

def evaluate_performance(detected, ground_truth):
    """Evaluates precision, recall, and F1 score for detected influencers."""
    detected_set = set(detected)
    ground_truth_set = set(ground_truth)
    
    true_positives = len(detected_set & ground_truth_set)
    false_positives = len(detected_set - ground_truth_set)
    false_negatives = len(ground_truth_set - detected_set)
    
    precision = true_positives / (true_positives + false_positives) if true_positives + false_positives > 0 else 0
    recall = true_positives / (true_positives + false_negatives) if true_positives + false_negatives > 0 else 0
    f1 = 2 * (precision * recall) / (precision + recall) if precision + recall > 0 else 0
    
    return precision, recall, f1

def generate_report(G, in_deg, out_deg):
    """Generates a detailed report of the graph metrics."""
    print("\n--- Detailed Report ---")
    print("Node\tIn-Degree\tOut-Degree")
    for node in G.nodes():
        print(f"{node}\t{G.in_degree(node)}\t\t{G.out_degree(node)}")
    print("\nCentrality Scores:")
    print("Node\tIn-Degree Centrality\tOut-Degree Centrality")
    for node in in_deg:
        print(f"{node}\t{in_deg[node]:.4f}\t\t{out_deg[node]:.4f}")

# ----------------------------------------------
# Main Workflow
# ----------------------------------------------

def main():
    print_welcome_message()
    display_help_menu()
    
    # Step 1: Create the graph
    G = create_graph()
    if len(G) == 0:
        print("No connections entered. Exiting program.")
        return
    
    # Step 2: Display graph information
    display_graph_info(G)
    
    # Step 3: Calculate centralities
    in_deg_centrality, out_deg_centrality = calculate_centralities(G)
    
    # Step 4: Find influencers
    influencers_in = find_top_influencers(in_deg_centrality)
    influencers_out = find_top_influencers(out_deg_centrality)
    
    print("\nInfluencers based on In-Degree Centrality:")
    print(", ".join(influencers_in))
    print("\nInfluencers based on Out-Degree Centrality:")
    print(", ".join(influencers_out))
    
    # Step 5: Generate report
    generate_report(G, in_deg_centrality, out_deg_centrality)
    
    # Step 6: Visualize graphs
    visualize_graph(G, in_deg_centrality, "Graph - In-Degree Centrality", "in_degree.png")
    visualize_graph(G, out_deg_centrality, "Graph - Out-Degree Centrality", "out_degree.png")
    
    # Step 7: Save centrality scores
    save_scores("centrality_scores.txt", in_deg_centrality, out_deg_centrality)
    
    # Step 8: Evaluate performance
    ground_truth = input("\nEnter ground truth influencers (comma-separated): ").split(",")
    ground_truth = [node.strip() for node in ground_truth]
    
    precision_in, recall_in, f1_in = evaluate_performance(influencers_in, ground_truth)
    precision_out, recall_out, f1_out = evaluate_performance(influencers_out, ground_truth)
    
    print("\n--- Evaluation Results ---")
    print(f"In-Degree Centrality: Precision={precision_in:.4f}, Recall={recall_in:.4f}, F1 Score={f1_in:.4f}")
    print(f"Out-Degree Centrality: Precision={precision_out:.4f}, Recall={recall_out:.4f}, F1 Score={f1_out:.4f}")
    
    print("\nThank you for using the tool!")

# Run the program
if __name__ == "_main_":
    main()