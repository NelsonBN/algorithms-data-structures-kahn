from collections import defaultdict, deque


def kahn(graph):
    in_degrees = defaultdict(int) # Track in-degrees for each vertex/node (O(V))

    # Step 1: Compute in-degrees (O(E))
    for u in graph:
        if u not in in_degrees:
            in_degrees[u] = 0
        for v in graph[u]:
            in_degrees[v] += 1

    # Step 2: Enqueue vertices with in-degree 0 (O(V))
    queue = deque()
    for u in in_degrees:
        if in_degrees[u] == 0:
            queue.append(u)

    topological_sort = []

    # Step 3: Process until queue is empty
    while queue: # O(V + E)
        u = queue.popleft() # Remove node from queue (O(1))
        topological_sort.append(u) # Append to topological order (O(1))

        # Guard rails to ensure that the vertex exists in the graph has a key.
        # This can happen when a node is a leaf node and has no outgoing edges.
        if u not in graph:
            continue

        # Decrease in-degree of all adjacent (neighboring) vertices/nodes (O(E))
        for v in graph[u]:
            in_degrees[v] -= 1
            if in_degrees[v] == 0: # If a neighboring hasn't any incoming edges, already can be processed because all its dependencies are satisfied
                queue.append(v)

    return topological_sort


graph = {
    'A': ['B'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['E', 'F'],
    'E': ['G'],
    'F': ['G']
}


print(f'Topological Sort: {kahn(graph)}')
