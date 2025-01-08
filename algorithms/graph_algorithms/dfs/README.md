# Depth First Search

## Description
Depth-First Search (DFS) is an algorithm used to traverse or search through a graph or tree data structure. It starts at a root node (or any arbitrary node in the graph) and explores as far as possible along each branch before backtracking to explore other branches. DFS is often used when you need to explore as deeply as possible into a structure before returning to previous nodes. It is particularly useful in problems requiring exhaustive search or when exploring potential paths or solutions.

Key characteristics of DFS:
    - Depth-order traversal: It explores nodes by going deep along a path before backtracking.
    - Stack: DFS uses a stack (either explicitly or via recursion) to store the nodes to be explored.
    - Ideal for pathfinding: DFS can be used to find paths, connected components, or solve problems like maze exploration or topological sorting.

DFS Algorithm Steps:
    - Start with a node and mark it as visited.
    - Push the node onto a stack.
    - While the stack is not empty:
    - Pop the top node from the stack.
    - Visit all its unvisited neighbors, mark them as visited, and push them onto the stack.


### Shell Code

#### Recursive

```python
def dfs(graph, v, visited):
    """
    Recursive Depth-First Search (DFS) function.
    
    Arguments:
    graph -- the adjacency matrix (2D list) representing the graph
    v -- the current node to start the DFS
    visited -- list to keep track of visited nodes
    """
    # Mark the current node as visited
    visited[v] = True
    print(f"Visiting node: {v}")

    # Explore all the neighbors of node v
    for i in range(len(graph)):
        # If there is an edge between v and i, and i is not visited
        if graph[v][i] == 1 and not visited[i]:
            dfs(graph, i, visited)  # Recursively visit the neighbor
```

#### Stack

```python
def dfs(graph, start):
    """
    Depth-First Search (DFS) function using a stack.
    
    Arguments:
    graph -- the adjacency matrix (2D list) representing the graph
    start -- the node to start the DFS from
    """
    # Number of nodes in the graph
    n = len(graph)

    # List to track visited nodes
    visited = [False] * n

    # Stack to store the nodes for DFS
    stack = [start]

    while stack:
        # Pop a node from the stack
        node = stack.pop()
        
        # If the node has not been visited yet
        if not visited[node]:
            visited[node] = True
            print(f"Visiting node: {node}")

            # Add all unvisited neighbors of the node to the stack
            for i in range(n - 1, -1, -1):  # Traverse neighbors in reverse to maintain the correct order
                if graph[node][i] == 1 and not visited[i]:
                    stack.append(i)
```