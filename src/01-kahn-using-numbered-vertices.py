from collections import deque


def kahn(graph):
    total_nodes = len(graph)
    in_degree = [0] * total_nodes  # Track in-degree for each vertex/node (O(V))

    # Step 1: Compute in-degrees (O(E))
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1 # Increment in-degree of destination vertex

    # Step 2: Enqueue vertices with in-degree 0 (O(V))
    queue = deque()
    for i in range(total_nodes):
        if in_degree[i] == 0:
            queue.append(i)

    topological_sort = []

    # Step 3: Process until queue is empty
    while queue: # O(V + E)
        u = queue.popleft() # Remove node from queue (O(1))
        topological_sort.append(u) # Add to topological order (O(1))

        # Decrease in-degree of all adjacent vertices (O(E))
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0: # If a vertex has no more incoming edges, it can be processed as all its dependencies are satisfied
                queue.append(v)

    if len(topological_sort) != total_nodes:
        raise Exception("Graph contains at least one cycle - Topological sort is not possible")

    return topological_sort


graph = {
    0: [],
    1: [],
    2: [3],
    3: [1],
    4: [0, 1],
    5: [2, 0]
}

print(f'Topological Sort: {kahn(graph)}')
