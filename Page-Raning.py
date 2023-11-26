def pagerank(graph, damping_factor=0.85, max_iterations=100, tol=1e-6):
    # Initialize PageRank scores.
    num_pages = len(graph)
    pr = {page: 1 / num_pages for page in graph}

    for _ in range(max_iterations):
        new_pr = {}
        for page in graph:
            new_pr[page] = (1 - damping_factor) / num_pages + \
                           damping_factor * sum(pr[link] / len(graph[link]) for link in graph if page in graph[link])

        # Check for convergence
        if all(abs(new_pr[page] - pr[page]) < tol for page in graph):
            break

        pr = new_pr

    return pr

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A', 'B'],
}

# Calculate PageRank
result = pagerank(graph)
print("PageRank Scores:")
for page, score in sorted(result.items(), key=lambda x: x[1], reverse=True):
    print(f"{page}: {score:.4f}")
