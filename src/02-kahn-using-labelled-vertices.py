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

    topological_sort = []

    # Step 3: Process until queue is empty
    while queue: # O(V + E)
        u = queue.popleft() # Remove node from queue (O(1))
        topological_sort.append(u) # Add to topological order (O(1))

        # Guard rail to ensure the vertex exists in the graph as a key.
        # This can happen when a node is a leaf node and has no outgoing edges.
        if u not in graph:
            continue

        # Decrease in-degree of all adjacent vertices (O(E))
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0: # If a vertex has no more incoming edges, it can be processed as all its dependencies are satisfied
                queue.append(v)

    if len(topological_sort) != len(in_degree):
        raise Exception("Graph contains at least one cycle - Topological sort is not possible")

    return topological_sort


dag = {
    'A': ['B'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['E', 'F'],
    'E': ['G'],
    'F': ['G']
}

cycle = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A'],
    'D': ['B', 'C'],
    'E': ['C', 'D']
}

dag = dag


print(f'Topological Sort: {kahn(dag)}')
