from collections import defaultdict, deque


def kahn(graph):
    in_degree = defaultdict(int) # Track in-degree for each vertex/node (O(V))

    # Step 1: Compute in-degrees (O(E))
    for u in graph:
        if u not in in_degree:
            in_degree[u] = 0
        for v in graph[u]:
            in_degree[v] += 1

    # Step 2: Enqueue vertices with in-degree 0 (O(V))
    queue = deque()
    for u in in_degree:
        if in_degree[u] == 0:
            queue.append(u)

    topological_sorting = []
    has_multiple_topological_sorting = False

    # Step 3: Process until queue is empty
    while queue: # O(V + E)
        if has_multiple_topological_sorting == False and len(queue) > 1:
            has_multiple_topological_sorting = True
        u = queue.popleft() # Remove node from queue (O(1))
        topological_sorting.append(u) # Add to topological order (O(1))

        # Guard rail to ensure the vertex exists in the graph as a key.
        # This can happen when a node is a leaf node and has no outgoing edges.
        if u not in graph:
            continue

        # Decrease in-degree of all adjacent vertices (O(E))
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0: # If a vertex has no more incoming edges, it can be processed as all its dependencies are satisfied
                queue.append(v)

    if len(topological_sorting) != len(in_degree):
        raise Exception("Graph contains at least one cycle - Topological sort is not possible")

    return topological_sorting, has_multiple_topological_sorting


graph1 = {
    'A': ['B'],
    'B': ['C']
}

graph2 = {
    'A': ['B', 'C'],
    'B': ['C', 'D', 'E'],
    'C': ['E', 'F']
}

graph = graph2

topological_sorting, has_multiple_topological_sorting = kahn(graph)

print(f'Topological Sorting: {topological_sorting}')
if has_multiple_topological_sorting:
    print("Graph has multiple topological sorting.")
