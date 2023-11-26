import networkx as nx
def hits_algorithm(graph, max_iter=100, tol=1e-6):
    """
    Compute HITS (Hubs and Authorities) scores for nodes in a graph.

    Parameters:
    - graph: NetworkX graph
    - max_iter: Maximum number of iterations (default: 100)
    - tol: Tolerance to declare convergence (default: 1e-6)

    Returns:
    - hubs: Dictionary of hub scores for each node
    - authorities: Dictionary of authority scores for each node
    """
    # Initialize hub and authority scores
    hubs = {node: 1 for node in graph.nodes}
    authorities = {node: 1 for node in graph.nodes}

    # HITS algorithm iteration
    for _ in range(max_iter):
        prev_hubs = hubs.copy()
        prev_authorities = authorities.copy()

        # Update authority scores based on hub scores
        for node in graph.nodes:
            authorities[node] = sum(prev_hubs[neighbor] for neighbor in graph.predecessors(node))

        # Update hub scores based on authority scores
        for node in graph.nodes:
            hubs[node] = sum(prev_authorities[neighbor] for neighbor in graph.successors(node))

        # Normalize scores
        norm_factor_hubs = max(hubs.values())
        norm_factor_authorities = max(authorities.values())

        for node in graph.nodes:
            hubs[node] /= norm_factor_hubs
            authorities[node] /= norm_factor_authorities

        # Check convergence
        hub_convergence = sum(abs(hubs[node] - prev_hubs[node]) for node in graph.nodes)
        authority_convergence = sum(abs(authorities[node] - prev_authorities[node]) for node in graph.nodes)

        if hub_convergence < tol and authority_convergence < tol:
            break

    return hubs, authorities

# Example usage
# Create a directed graph (use any graph of your choice)
G = nx.DiGraph()
G.add_edges_from([(1, 2), (2, 3), (3, 1)])

# Compute HITS scores
hubs, authorities = hits_algorithm(G)

# Print results
print("Hub Scores:", hubs)
print("Authority Scores:", authorities)
