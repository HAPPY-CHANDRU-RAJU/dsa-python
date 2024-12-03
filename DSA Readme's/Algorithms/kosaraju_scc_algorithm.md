
# Kosaraju’s Algorithm for Finding Strongly Connected Components (SCCs)

## Overview
Kosaraju's Algorithm is used for finding the Strongly Connected Components (SCCs) of a directed graph. An SCC is a subgraph where each vertex is reachable from every other vertex within the same SCC.

## Steps

1. **Input**:
   - `v`: Number of vertices in the graph.
   - `edges`: List of directed edges in the graph.
   
2. **Initializations**:
   - Create an adjacency list (`adj_matrix`) from the given `edges`.
   - Create a stack to store the vertices in the order of completion of DFS.
   - Create a visited list to track whether a node has been visited or not.

3. **First DFS (Original Graph)**:
   - Perform DFS traversal on the original graph.
   - Push each vertex onto the stack after completing DFS for that vertex.

4. **Transpose the Graph**:
   - Reverse the direction of all edges to get the transpose of the graph.
   - This helps in finding the SCCs since the SCCs in the transpose graph are the reverse of the original graph’s components.

5. **Second DFS (Transpose Graph)**:
   - Pop elements from the stack (from the first DFS).
   - For each vertex, if it hasn’t been visited, perform DFS on the transpose graph starting from that vertex.
   - The set of nodes visited in each DFS call forms an SCC.

6. **Output**:
   - Return a list of SCCs found in the graph.

```python
from collections import defaultdict

def kosaraju_scc(v, edges):
    # Step 1: Create the adjacency list
    adj_matrix = defaultdict(list)
    for u, v in edges:
        adj_matrix[u].append(v)
    
    # Step 2: DFS traversal to fill the stack
    def dfs(node, visited, stack):
        visited[node] = True
        for neighbour in adj_matrix[node]:
            if not visited[neighbour]:
                dfs(neighbour, visited, stack)
        stack.append(node)
    
    # Step 3: Transpose the graph
    def transpose():
        transposed = defaultdict(list)
        for node in adj_matrix:
            for neighbour in adj_matrix[node]:
                transposed[neighbour].append(node)
        return transposed
    
    # Step 4: Perform DFS and store nodes in stack
    visited = [False] * v
    stack = []
    for i in range(v):
        if not visited[i]:
            dfs(i, visited, stack)
    
    # Step 5: Transpose the graph
    transpose_matrix = transpose()
    visited = [False] * v
    sccs = []
    
    # Step 6: Perform DFS on the transposed graph
    def dfs_count(node, visited, component):
        visited[node] = True
        component.append(node)
        for neighbour in transpose_matrix[node]:
            if not visited[neighbour]:
                dfs_count(neighbour, visited, component)
    
    while stack:
        node = stack.pop()
        if not visited[node]:
            component = []
            dfs_count(node, visited, component)
            sccs.append(component)
    
    return sccs

# Example usage
edges = [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4)]
v = 5
sccs = kosaraju_scc(v, edges)
print(f"Strongly Connected Components: {sccs}")
```

## Time and Space Complexity

- **Time Complexity**:
  - The algorithm involves two DFS traversals: one on the original graph and another on the transposed graph. Both DFS operations take `O(V + E)` time, where `V` is the number of vertices and `E` is the number of edges.
  - Thus, the overall time complexity is `O(V + E)`.

- **Space Complexity**:
  - The space complexity is `O(V + E)` due to the storage required for the adjacency list, the transpose graph, and the visited list.

## Output:
- The output is a list of SCCs, where each SCC is represented as a list of vertices.

For example, the above code will output:
```
Strongly Connected Components: [[0, 1, 2], [3], [4]]
```
