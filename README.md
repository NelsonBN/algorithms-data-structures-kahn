# Algorithms and Data Structures - Kahn

The Kahn's algorithm is a method for **topological sorting** of a **directed acyclic graph (DAG)**. It works by iteratively removing nodes with no incoming edges and adding them to the sorted order. The process continues until all nodes are removed or a cycle is detected.


## Characteristics
- Time complexity: O(V + E) - Because the algorithm processes each vertex and edge exactly once.
  - V = number of vertices
  - E = number of edges
- Space complexity: O(V) - The algorithm use a list to store the in-degree of each vertex and a queue to store the vertices with in-degree 0.



## Demos

### Using Numbered Vertices

```mermaid
graph LR
  5((5)) --> 2
  5 --> 0((0))
  4((4)) --> 0
  4 --> 1((1))
  2((2)) --> 3
  3((3)) --> 1
```

[Implementation](./src/01-kahn-using-numbered-vertices.py)


### Using Labelled Vertices

**DAG**:
```mermaid
graph LR
  A((A)) --> B((B))
  B --> C
  B --> D
  C((C)) --> E
  D((D)) --> E
  D --> F
  E((E)) --> G((G))
  F((F)) --> G
```
**Cycle**:
```mermaid
graph LR
  A((A)) --> B
  B((B)) --> C
  C((C)) --> A
  D((D)) --> B
  D --> C
  E((E)) --> C
  E --> D

  linkStyle 0,1,2 stroke:#f00
```

[Implementation](./src/02-kahn-using-labelled-vertices.py)


### Detect if has more than one topological sorting

```mermaid
graph LR
  A((A)) --> B
  B((B)) --> C((C))
```
```mermaid
graph LR
  A((A)) --> B
  A --> C

  B((B)) --> C
  B --> D((D))
  B --> E

  C((C)) --> E((E))
  C --> F((F))
```

[Implementation](./src/03-kahn-detecting-multiple-topological-sorting.py)



## References
- [Topological Sorting with DFS](https://github.com/NelsonBN/algorithms-data-structures-topological-sorting-dfs)
- [Other Algorithms & Data Structures](https://github.com/NelsonBN/algorithms-data-structures)
