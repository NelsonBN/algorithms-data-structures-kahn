# Algorithms and Data Structures - Kahn

The Kahn's algorithm is a method for **topological sorting** of a **directed acyclic graph (DAG)**. It works by iteratively removing nodes with no incoming edges and adding them to the sorted order. The process continues until all nodes are removed or a cycle is detected.


## Characteristics
- Time complexity: O(V + E)
  - V = number of vertices
  - E = number of edges
- Space complexity: O(V + E)



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

[Implementation](./src/02-kahn-using-labelled-vertices.py)



## References
- [Other Algorithms & Data Structures](https://github.com/NelsonBN/algorithms-data-structures)
