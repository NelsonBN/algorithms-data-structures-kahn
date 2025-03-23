def topological_sort(graph):
    total_nodes = len(graph)

    visited = [False] * total_nodes # Marks all vertices as not visited (O(V))
    result = []

    def dfs(v):
        visited[v] = True # Mark the current vertex as visited (O(1))
        for neighbor in graph[v]: # Traverse the neighbors (O(E) in total)
            if not visited[neighbor]:
                dfs(neighbor)
        result.append(v) # Push the vertex after visiting all neighbors (O(1))

    # Call DFS for each unvisited vertex
    for v in range(total_nodes): # O(V)
        if not visited[v]:
            dfs(v)

    # Reverse the stack to get the correct topological order
    return result[::-1]


graph = {
    0: [],
    1: [],
    2: [3],
    3: [1],
    4: [0, 1],
    5: [2, 0]
}

print(f'Topological Sort: {topological_sort(graph)}')
